from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    lastName: str
    born: int 

class Instrumentos(BaseModel):
    
    Marca: str
    Modelo: str
    Precio: int
    Stock: int          
