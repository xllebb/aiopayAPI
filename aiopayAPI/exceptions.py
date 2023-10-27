


class ValuesNotFound(Exception):
    """Ошибка которая возникает при не нахождение значений в обязательном параметре"""
    def __init__(self, message) -> None:
        self.message = message


    def __str__(self) -> str:
        return f"{self.message}"
    

class IPError(Exception):
    """Ошибка возникающая когда IP адрес не добавлен в список разрешенных IP адресов"""
    def __str__(self) -> str:
        return "IP с которого вы пытаететь авторизоваться не добавлен в список разрешенных IP адресов."
    
class Error(Exception):
    """Обработка всех ошибок + их код"""
    def __init__(self, message: str, code: int) -> None:
        self.message = message
        self.code = code
        
    def __str__(self) -> str:
        return f"{self.message} (Код ошибки: {self.code})"
    


