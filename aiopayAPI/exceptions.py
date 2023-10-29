


class ValuesNotFound(Exception):
    """Ошибка которая возникает при не нахождение значений в обязательном параметре"""
    def __init__(self, message) -> None:
        self.message = message


    def __str__(self) -> str:
        return f"{self.message}"
    

class ResponseError(Exception):
    """Ошибка при обработке запроса"""
    def __init__(self, code: int) -> None:
        self.code = code
    def __str__(self) -> str:
        return "Произошла ошибка при обработке запроса, код сайта: {}".format(self.code)
    
class Error(Exception):
    """Обработка всех ошибок + их код"""
    def __init__(self, message: str, code: int) -> None:
        self.message = message
        self.code = code
        
    def __str__(self) -> str:
        return f"{self.message} (Код ошибки: {self.code})"
    

    


