from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class Three_answers_options(BaseModel):
    question: str = Field(description="Pregunta tipo test sobre el articulo concreto ")
    response: List[str] = Field(description="Tres respuestas tipo test de la pregunta con las letras A), B) Y C)")
    correct_response: str = Field(description="El numero de la respuesta correcta")


parsers = {
    "three_answers": PydanticOutputParser(pydantic_object=Three_answers_options)
}