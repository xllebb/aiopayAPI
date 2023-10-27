class URL:
    """ 
    Класс со всеми ссылками для запросов

    """
    balance: str = "https://payok.io/api/balance"
    """Ссылка для получения баланса"""

    transaction: str = "https://payok.io/api/transaction"
    """Сслыка для получения всех транзакций"""

    payout: str = "https://payok.io/api/payout"
    """Ссылка для получения выплат"""

    create: str = "https://payok.io/api/payout_create"
    """Создание выплат"""
