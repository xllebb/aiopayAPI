from aiopayAPI import PayOk

import asyncio

async def main():
    pay = PayOk(
        API_ID=1111,
        API_KEY=2222,
        shop=3333
    )
    await pay.get.balance()
