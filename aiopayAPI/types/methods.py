class Method:
    """Методы оплаты (нужны для совершения оплаты)"""

    card = "card"
    """Банковская карта"""

    card_uah = "card_uah"
    """Украиснкая карта"""

    card_foreign = "card_foreign"
    """Зарубежная карта"""

    tinkoff = "tinkoff"
    """Оплата по Тинькофф"""

    sbp = "sbp"
    """Оплата по СБП"""

    qiwi = "qiwi"
    """Оплата по Qiwi"""

    yoomoney = "yoomoney"
    """Оплата по ЮМани"""

    payeer = "payeer"
    """Оплата Payeer"""

    advcash = "advcash"
    """Оплата по Advcash"""

    perfect_money = "perfect_money"
    """Оплата по Perfect Money"""

    webmoney = "webmoney"
    """Оплата по Webmoney"""

    bitcoin = "bitcoin"
    """Оплата Bitcoin"""

    litecoin = "litecoin"
    """Оплата Litecoin"""

    tether = "tether"
    """Оплата Tether USDT"""

    tron = "tron"
    """Оплата Tron"""

    dogecoin = "dogecoin"
    """Оплата Dogecoin"""

    ethereum = "ethereum"
    """Оплата Ethereum"""

    ripple = "ripple"
    """Оплата ripple"""




class PayMethod:
    """
    Все доступные платежные методы (нужны при генерации ссылки для оплаты)
    """
    
    bank = "cd"
    """Любой активный Банковский метод (cpa, cp2, cwo, cru)"""

    payok_card = "cpa"
    """Банк. Карты Payok"""

    p2p = "cp2"
    """Банк. Карты P2P"""

    world = "cwo"
    """Банк. Карты Весь мир"""

    form = "cru"
    """Банк. Карты Форма"""

    form2 = "cwo + currency=RUB"
    """Банк. Карты Форма #2"""

    uah = "cwo + currency=UAH"
    """Банк. Карты Форма UAH"""

    usd = "cwo + currency=USD"
    """Банк. Карты Форма USD"""

    eur = "cwo + currency=EUR"
    """Банк. Карты Форма EUR"""

    sbp = "sbp"
    """СБП"""

    qiwi = "qw"
    """Qiwi"""

    yoomoney = "yo"
    """Yoomoney"""

    perfect_money = "pm"
    """Perfect Money"""

    perfect_money_USD = "pm + currency=USD"
    """Perfect Money USD"""

    perfect_money_EUR = "pm + currency=EUR"
    """Perfect Money EUR"""

    megafon = "mg"
    """Мегафон"""

    beline = "bl"
    """Билайн"""

    bitcoin = "bt"
    """Bitcoin"""

    tether_TRC = "tt"
    """Tether TRC"""

    tether_ERC = "te"
    """Tether ERC"""

    litecoin = "lt"
    """Litecoin"""

    dogecoin = "dc"
    """Dogecoin"""

    ethereum = "et"
    """Ethereum"""

    tron = "tx"
    """Tron"""

    ripple = "rp"
    """Ripple"""