import os

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from src.opogen.llm.prompts import prompts

def init_config(key):
    os.environ["OPENAI_API_KEY"] = key

def get_opo_response(title, text_chunk, parser:PydanticOutputParser , options = 3, prompt_version = 1.0):
    template = prompts[prompt_version]
    prompt = PromptTemplate.from_template(
        template=template,
        input_variables=["title", "articles", "options"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
        )
    llm = OpenAI()

    chain = prompt | llm | parser

    response = chain.invoke({
        "title": title,
        "articles": text_chunk,
        "options": options
                  })
    
    return response