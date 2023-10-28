from pydantic import BaseModel
from aiopayAPI.payok import GetAll, PayOk



        

class Get:
    def __init__(self) -> None:
        self.some: Some = Some()

    def get_name(self):
        return self.some.name

class Some(BaseModel):
    """
    :param name: Имя
    :type name: :obj:`str`
    """
    name: str = "John"
    """Имя
    :type name: :obj:`str`
    """


    def get_name(self):
        return self.name


some = Some(name="Mike")
print(some.get_name())




