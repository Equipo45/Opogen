from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class Three_answers_options(BaseModel):
    pregunta: str = Field(description="preguntas tipo test sobre el articulo concreto con 3 posible respuestas correctas")
    response: List[str] = Field(description="la letra de la respuesta correcta en cada pregunta")


parsers = {
    "three_answers": PydanticOutputParser(Three_answers_options)
}