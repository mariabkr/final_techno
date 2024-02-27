from pydantic import BaseModel, Field
from uuid import uuid4



class Book(BaseModel):
    id: str
    name_book: str = Field(...,min_length=1,strip_whitespace=True)
    auteur:str=Field(...,min_length=1,strip_whitespace=True)
    editeur:str =Field(...,min_length=1,strip_whitespace=True)
