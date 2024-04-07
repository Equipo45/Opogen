import os

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from llm.prompts import prompts

def init_config(key):
    os.environ["OPENAI_API_KEY"] = key

def get_opo_response(text_chunk, parser:PydanticOutputParser , options = 3, prompt_version = 1.0):
    try:
        template = prompts[prompt_version]
        prompt = PromptTemplate.from_template(
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()}
            )
        llm = OpenAI()

        chain = prompt | llm | parser

        response = chain.invoke({
            "articles": text_chunk,
            "options": options
                    })
        
        return response
    except Exception as e:
        raise Exception(f"Some error occurr while getting openai response {e}")