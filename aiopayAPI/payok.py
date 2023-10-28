import aiohttp
from .urls import URL
from .types import Method
import json
from .utils import Checker
from typing import Dict, Union
from .types.commisions import Commission




class PayOk:
    """
    Класс для работы с сайтом PayOk

    :param API_ID: ID ключа
    :type API_ID: :obj:`int`

    :param API_KEY: API Ключ
    :type API_KEY: :obj:`str`

    :param shop: ID магазина
    :type shop: :obj:`int`
    
    :param payment: ID платежа в вашей системе
    :type payment: :obj:`str`

    :param payout_id: ID выплаты в системе Payok
    :type payout_id: :obj:`int`

    :param offset: Отступ, пропуск указанного количества строк
    :type offset: :obj:`int`

    :param amount: Сумма выплаты
    :type amount: :obj:`float`

    :param method: Специальное значение метода выплаты, (default=Method.card)
    :type method: :obj:`Method`

    :param receiver: Реквизиты получателя выплаты
    :type receiver: :obj:`str`

    :param sbp_bank: Банк для выплаты по СБП
    :type sbp_bank: :obj:`str`

    :param commission_type: Тип расчета комиссии (Commission.balance | Commission.payment)
    :type commission_type: :obj:`str`

    :param url: URL для отправки Webhook при смене статуса выплаты
    :type url: :obj:`str`

    :param json_file: JSON файл для записи ответов
    :type json_file: :obj:`str`

    :param processing_error: Обработка ошибок (boolean, default=False)
    :type processing_error: :obj:`bool`
    """
    def __init__(self, API_ID: int, API_KEY: str,
                shop: int, payment: Union[str, None] = None, payout_id: Union[int, None] = None,
                offset: int = 0, amount: Union[float, None] = None, method: Method | None = None,
                receiver: Union[str, None] = None, sbp_bank: Union[str, None] = None, 
                commission_type: str = Commission.balance, url: Union[str, None] = None,
                json_file: Union[str, None] =  None, processing_error: bool = False):
        """
        Инициализация класса PayOk

        :param API_ID: ID ключа
        :type API_ID: :obj:`int`

        :param API_KEY: API Ключ
        :type API_KEY: :obj:`str`

        :param shop: ID магазина
        :type shop: :obj:`int`
        
        :param payment: ID платежа в вашей системе
        :type payment: :obj:`str`

        :param payout_id: ID выплаты в системе Payok
        :type payout_id: :obj:`int`

        :param offset: Отступ, пропуск указанного количества строк
        :type offset: :obj:`int`

        :param amount: Сумма выплаты
        :type amount: :obj:`float`

        :param method: Специальное значение метода выплаты, (default=Method.card)
        :type method: :obj:`Method`

        :param receiver: Реквизиты получателя выплаты
        :type receiver: :obj:`str`

        :param sbp_bank: Банк для выплаты по СБП
        :type sbp_bank: :obj:`str`

        :param commission_type: Тип расчета комиссии (Commission.balance | Commission.payment)
        :type commission_type: :obj:`str`

        :param url: URL для отправки Webhook при смене статуса выплаты
        :type url: :obj:`str`

        :param json_file: JSON файл для записи ответов
        :type json_file: :obj:`str`

        :param processing_error: Обработка ошибок (boolean, default=False)
        :type processing_error: :obj:`bool`
        """
        self.id: int = API_ID
        """ID вашего ключа API"""

        self.key: str = API_KEY
        """Ваш ключ API"""

        self.shop: int = shop
        """ID магазина"""

        self.amount: float | None = amount
        """Сумма выплаты"""

        self.receiver: str | None = receiver
        """Реквизиты получателя выплаты"""

        self.sbp: str | None = sbp_bank
        """Банк для выплаты по СБП"""

        self.commission: str | None = commission_type
        """Тип расчета комиссии (Commission.balance | Commission.payment)"""

        self.url: str | None = url
        """URL для отправки Webhook при смене статуса выплаты"""

        self.payout_id: int | None = payout_id
        """ID выплаты в системе Payok"""

        self.offset: int | None = offset
        """Отступ, пропуск указанного количества строк"""

        self.method: str | None = method
        """Специальное значение метода выплаты, (default=Method.card)"""

        self.payment_id: int | None = payment
        """ID платежа в вашей системе"""

        self.json: str | None = json_file
        """JSON файл для записи ответов"""

        self.error: bool | None = processing_error
        """Обработка ошибок"""

        self.get: function = GetAll(self)
        """Функция для получения возможных данных (баланс, выплаты)
        Отностится к классу GetAll"""

    async def payment(self) -> Dict:
        """
        Создание выплат (перевод)\n

        
        :param API_ID: ID вашего ключа API
        :type  API_ID: :obj:`int`, обязательно

        :param API_KEY: Ваш ключ API
        :type API_KEY: :obj:`str`, обязательно

        :param shop: ID магазина
        :type shop: :obj:`int`, обязательно

        :param amount: Сумма выплаты
        :type amount: :obj:`float`, обязательно

        :param method: Специальное значение метода выплаты, (default=Method.card)
        :type method: :obj:`Method`, обязательно

        :param reciever: Реквизиты получателя выплаты
        :type reciever: :obj:`str`, обязательно

        :param sbp_bank: Банк для выплаты по СБП
        :type sbp_bank: :obj:`str`, опционально

        :param commission_type: Тип расчета комиссии (Commission.balance | Commission.payment)
        :type commission_type: :obj:`str`, опционально

        :param url: URL для отправки Webhook при смене статуса выплаты
        :type url: :obj:`str`, опционально

        :param json_file: JSON файл для записи ответов
        :type json_file: :obj:`str`, опционально

        :param processing_error: Обработка ошибок (boolean, default=False)
        :type processing_error: :obj:`bool`, опционально

        :return: :obj:`dict` с данными 
        """
        Checker().check_params(amount=self.amount, method=self.method, reciever=self.receiver, commission=self.commission)
        data = {
            "API_ID": self.id,
            "API_KEY": self.key,
            "amount": self.amount,
            "method": self.method,
            "reciever": self.receiver
        }
        if self.sbp:
            data.update({"sbp_bank": self.sbp})

        if self.commission:
            data.update({"comission_type": self.commission})

        if self.url:
            data.update({"webhook_url": self.url})

        async with aiohttp.ClientSession() as session:
            async with session.post(URL.create,
                                    data=data) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    if self.json:
                        with open(self.json, "a", encoding='utf-8') as file:
                            json.dump(json.loads(text), file, indent=4, ensure_ascii=False)
                    if self.error is True:
                        Checker().status(json.loads(text))
                    return json.loads(text)
                else:
                    return {}
                

class GetAll:
    """
    Класс для получения данных
    """
    def __init__(self, payok: PayOk) -> None:
        self.pay = payok

    async def balance(self) -> dict:
        """
        Получение баланса

        :param shop: ID магазина
        :type shop: :obj:`int`, обязательно

        :param payment: ID платежа
        :type payment: :obj:`int`, опционально

        :param shop: ID магазина
        :type shop: :obj:`int`, обязательно
        
        :return: :obj:`dict` с данными баланса
        """
        data = {
            "API_ID": self.pay.id,
            "API_KEY": self.pay.key,
            "shop": self.pay.shop
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(URL.balance,
                                    data=data) as resp:
                if resp.status == 200:
                    text = await resp.text(encoding="utf-8")
                    json_resp = json.loads(text)
                    if self.pay.json:
                        with open(self.pay.json, 'a', encoding='utf-8') as file:
                            json.dump(json.loads(text), file, indent=4, ensure_ascii=False)
                    if self.pay.error is True:
                        Checker().status(json_resp)
                    return json_resp
                else:
                    return {}
                
    async def payout(self) -> dict:
        """
        Получение выплат (макс. 100)

        :param API_ID: ID вашего ключа API
        :type API_ID: :obj:`int`, обязательно

        :param API_KEY: Ваш ключ API
        :type API_KEY: :obj:`str`, обязательно

        :param offset: Отступ, пропуск указанного количества строк
        :type offset: :obj:`int`, опционально

        :param payout_id: ID выплаты в системе Payok
        :type payout_id: :obj:`int`, опционально

        :return: :obj:`dict` объект с данными выплат
        """
        data = {
            "API_ID": self.pay.id,
            "API_KEY": self.pay.key
        }
        if self.pay.payout_id:
            data.update({"payout_id": self.pay.payout_id})
        if self.pay.offset:
            data.update({"offset": self.pay.offset})
        async with aiohttp.ClientSession() as session:
            async with session.post(URL.payout, 
                                    data=data) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    if self.pay.json:
                        with open(self.pay.json, 'a', encoding='utf-8') as file:
                            json.dump(json.loads(text), file, indent=4, ensure_ascii=False)
                    if self.pay.error is True:
                        Checker().status(json.loads(text))
                    return json.loads(text)
                else:
                    return {}
                

        


        

