from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from llm.prompts import prompts
from utils.logger import logger

# Availible models
# gpt-3.5-turbo-instruct
# gpt-4-turbo-preview
# gpt-4-turbo

def get_opo_response(
    text_chunk,
    parser: PydanticOutputParser,
    options=3,
    prompt_version=1.4,
    model="gpt-3.5-turbo-instruct",
):
    try:
        template = prompts[prompt_version]
        prompt = PromptTemplate.from_template(
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        llm = OpenAI(model=model)

        chain = prompt | llm | parser

        response = chain.invoke({"articles": text_chunk, "options": options})

        return response
    except Exception as e:
        str_exception = f"Some error occurr while getting openai response {e}"
        logger.error(str_exception)
        raise Exception(str_exception) from e
