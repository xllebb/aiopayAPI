class Some:
    """
    Some class

    :param user: Имя
    :type user: obj:`str`
    """
    def __init__(self, user: str | None) -> None:
        self.user: str = user
        """Имя"""

    def get_name(self) -> str:
        """
        Возвращает имя
        """
        return self.user