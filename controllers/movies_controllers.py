from pydantic import BaseModel
from datetime import date, time, datetime

class Movie(BaseModel):
    autor: str
    Descripcion: str
    Fecha_Estreno: date


db_params = {
    'dbname': 'my_collections', #postgres
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': 'local_host',
    'port': '5432',
}
