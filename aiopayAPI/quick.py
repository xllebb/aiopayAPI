import hashlib
from typing import Dict
import json
from .urls import URL
import aiohttp
from .utils import Checker
from .types import Method

 
class QuickPay:
    """Класс для создание оплаты в PayOk

    :param amount: Сумма оплаты
    :type amount: :obj:`float`

    :param payment: ID платежа в вашей системе
    :type payment: :obj:`str`, опционально

    :param shop: ID магазина
    :type shop: :obj:`int`

    :param desc: Описание платежа
    :type desc: :obj:`str`

    :param currency: Валюта платежа
    :type currency: :obj:`str`

    :param secret: Секретный ключ
    :type secret: :obj:`str`

    :param email: E-mail получателя
    :type email: :obj:`str`, опционально

    :param success_url: URL для отправки Webhook при смене статуса выплаты
    :type success_url: :obj:`str`, опционально

    :param method: Специальное значение метода выплаты, (default=Method.card)
    :type method: :obj:`Method`, опционально

    :param lang: Язык выплаты
    :type lang: :obj:`str`, опционально

    :param custom: Ваш параметр, который вы хотите передать в уведомлении
    :type custom: :obj:`str`, опционально

    :param API_ID: ID ключа (нужен ТОЛЬКО для получения транзакций)
    :type API_ID: :obj:`int`, опционально

    :param API_KEY: API Ключ (нужен ТОЛЬКО для получения транзакции)
    :type API_KEY: :obj:`str`, опционально

    :param json_file: JSON файл для записи ответов
    :type json_file: :obj:`str`, опционально

    :param processing_error: Обработка ошибок (boolean, default=False)
    :type processing_error: :obj:`bool`, опционально
    """
    def __init__(self, amount: float, shop: int, desc: str, currency: str, secret: str, 
                 email: str | None = None, payment: str | None = None,
                 success_url: str | None = None, method: str | None = Method.card, 
                 lang: str | None = None, custom: str | None = None,
                 API_ID: int | None = None, API_KEY: str | None = None, 
                 json_file: str | None = None, processing_error: bool = False) -> None:
        """
        Инициализация класса Quickpay
        """
        self.amount: float = amount
        """Сумма оплаты"""

        self.payment: int = payment
        """ID платежа в вашей системе"""

        self.shop: int = shop
        """ID магазина"""

        self.desc: str = desc
        """Описание платежа"""

        self.currency: str = currency
        """Валюта платежа (RUB, USD и т.д.)"""

        self.secret: str = secret
        """Секретный ключ"""

        self.email: str | None = email
        """E-mail получателя"""

        self.success_url: str | None = success_url
        """URL для отправки Webhook при смене статуса выплаты"""

        self.method: str | Method.card = method
        """Специальное значение метода выплаты, (default=Method.card)"""

        self.lang: str | None = lang
        """Язык выплаты"""

        self.custom: str | None = custom
        """Ваш параметр, что вы хотите передать в уведомлении"""

        self.api: Dict = {"API_ID": API_ID, "API_KEY": API_KEY, "shop": shop}

        self.json: str | None = json_file
        """Файл для записи ответов"""

        self.error: bool | None= processing_error
        """Обработка ошибок"""

        self.link: str | None = self.generate_paylink()
        """Генерация сылка для оплаты (переменная)"""
    def generate_paylink(self) -> str:
        """
        Генерация ссылки для оплаты (функция)

        :return: Ссылка
        """
        
        url = f"https://payok.io/pay?amount={self.amount}&currency={self.currency}&payment={self.payment}&desc={self.desc}&shop={self.shop}"
        if self.method:
            url += f"&method={self.method}"
        else:
            url += f"&method=cd"

        if self.email:
            url += "&email=" + self.email
        
        if self.success_url:
            url += f"&success_url={self.success_url}"

        if self.lang:
            url += f"&lang={self.lang}"

        if self.custom:
            url += f"&custom={self.custom}"

        secret = hashlib.md5(f"{self.amount}|{self.payment}|{self.shop}|{self.currency}|{self.desc}|{self.secret}".encode('utf-8')).hexdigest()
        url += f"&sign={secret}"
        
        return url
    
    async def get_transaction(self) -> Dict:
        """
        Получение всех транзакций (макс. 100)

        :param API_ID: ID ключа (нужен ТОЛЬКО для получения транзакций)
        :type API_ID: :obj:`int`, обязательно

        :param API_KEY: API Ключ (нужен ТОЛЬКО для получения транзакции)
        :type API_KEY: :obj:`str`, обязательно

        :param shop: ID магазина
        :type shop: :obj:`int`, обязательно

        :param payment: ID платежа
        :type payment: :obj:`int`, опционально

        :param json_file: JSON файл для записи ответов
        :type json_file: :obj:`str`, опционально

        :param processing_error: Обработка ошибок (boolean, default=False)
        :type processing_error: :obj:`bool`, опционально

        :return: :obj:`dict` с данными транзакции
        """
        data = self.api
        if self.payment:
            data.update({"payment": self.payment})

        async with aiohttp.ClientSession() as session:
            async with session.post(URL.transaction, 
                                    data=data) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    if self.json:
                        with open(self.json, 'a', encoding='utf-8') as file:
                                json.dump(json.loads(text), file, indent=4, ensure_ascii=False)
                    if self.error is True:
                        Checker().status(json.loads(text))
                    return json.loads(text)
                else:
                    return {}
                

                
    