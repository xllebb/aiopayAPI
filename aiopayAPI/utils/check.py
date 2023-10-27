from ..exceptions import ValuesNotFound, Error
from typing import Dict, Callable
import time

class Checker:
    """Проверка данных """
    def __init__(self, **params: Dict | None) -> None:
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
        

   
    # def status_wait(status: int = 1, update_time: int = 2, object_with_data: Dict = None) -> Callable:
    #         """
    #         Декоратор, который проверяет статус транзакции. Если оно равно 1, то функция выполняется.
        
    #         :param status: Статус транзакции (default=1)
    #         :type status: int
        
    #         :param update_time: Время обновления запроса в секундах (default=2)
    #         :type update_time: int, seconds
        
    #         :return: Функцию
    #         :rtype: Callable
    #         """
    #         def decorator(func: Callable) -> Callable:
    #             trans_status = object_with_data["1"]["transaction_status"]
        
    #             def wrapper():
    #                 while True:
    #                     if trans_status != 1:
    #                         time.sleep(update_time)
    #                     else:
    #                         func()
    #                         break
                
    #             return wrapper
        
    #         return decorator
    


