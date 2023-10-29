===============
Примеры
===============

На этой странице есть коды использования **aiopayAPI**


Получение баланса
-------------
.. code:: python

    from aiopayAPI import PayOk
    import asyncio

    async def main():
        pay = PayOk(
            API_ID=1111,
            API_KEY="xxxxxxxxxxxxxxxxxx",  
            shop=2222
        )
        balance = await pay.get.balance()
        print(balance)

    if __name__ == "__main__":
        asyncio.run(main())



Генерация ссылки
------------------
.. code:: python

    from aiopayAPI import QuickPay
    import asyncio

    async def main():
        quick = PayOk(
            amount=20.5, # Сумма 
            currency="RUB",
            payment=123456 # Номер заказа, уникальный в вашей системе (необязательно)
            desc="Description", # Описание платежа
            shop=2222 # ID вашего магазина
        )
        trans = quick.generate_paylink()
        print(trans)


Создание оплаты
-----------
.. code:: python

    from aiopayAPI import PayOk, Method
    import asyncio

    async def main():
        pay = PayOk(
            API_ID=1111, # ID вашего ключа
            API_KEY="xxxxxxxxxxxxxxxxxx", # Сам ваш ключ
            shop=4444, # ID магазина
            amount=20.5, # Сумма для перевода
            reciever="карта/номер получателя",
            method=Method.card # Методы оплаты
        )
        payout = await pay.payment()
        print(payout)

    if __name__ == "__main__":
        asyncio.run(main())


Получение оплаты
-------------
.. code:: python

    from aiopayAPI import PayOk, Method
    import asyncio

    async def main():
        pay = PayOk(
            API_ID=1111, # ID вашего ключа
            API_KEY="xxxxxxxxxxxxxxxxxx", # Сам ваш ключ
        )
        payout = await pay.get.payout()
        print(payout)

    if __name__ == "__main__":
        asyncio.run(main())

Получение транзакций
--------------
.. code:: python

    from aiopayAPI import PayOk, Method
    import asyncio

    async def main():
        quick = QuickPay(
            API_ID=1111, # ID вашего ключа
            API_KEY="xxxxxxxxxxxxxxxxxx", # Сам ваш ключ
            shop=2222
        )
        trans = await quick.get_transaction()
        print(trans)

    if __name__ == "__main__":
        asyncio.run(main())



Если вам не понятны данные примеры, вы можете посмотреть более подробные примеры на GitHub

