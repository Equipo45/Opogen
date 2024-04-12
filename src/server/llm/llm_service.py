import os

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from llm.prompts import prompts
from utils.logger import logger


def init_config(key):
    os.environ["OPENAI_API_KEY"] = key["OPEN_AI_KEY"]


def get_opo_response(
    text_chunk,
    parser: PydanticOutputParser,
    options=3,
    prompt_version=1.0,
    model="gpt-3.5-turbo-instruct",
):
    try:
        template = prompts[prompt_version]
        prompt = PromptTemplate.from_template(
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        llm = ChatOpenAI(model=model)

        chain = prompt | llm | parser

        response = chain.invoke({"articles": text_chunk, "options": options})

        return response
    except Exception as e:
        str_exception = f"Some error occurr while getting openai response {e}"
        logger.error(str_exception)
        raise Exception(str_exception) from e
