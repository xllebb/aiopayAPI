from ..exceptions import ValuesNotFound, Error
from typing import Dict, Callable
import time

class Checker:
    """Проверка данных"""
    def __init__(self, **params: dict | None) -> None:
        self.params = params


    def check_params(self) -> None:
        """Проверка необходимых параметров
        :return: Ошибка, если есть None в обязательном параметре"""
        missing_params = [param for param, value in self.params.items() if value is None]
        if missing_params:
            raise ValuesNotFound(f"Не найден обязательный параметр {', '.join(missing_params)}! Укажите его во время инициализации класса PayOk")
                
    

    def status(self, data: Dict) -> None:
        """
        Обработчик статуса даты
        """
        error = data.get("error_code")
        if error:
            text = data.get("error_text")
            if text:
                raise Error(text, error)
            else:
                text = data.get("text")
                raise Error(text, error)
        

   

    


