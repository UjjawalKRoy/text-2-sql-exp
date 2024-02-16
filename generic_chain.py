from langchain.callbacks import FileCallbackHandler
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from loguru import logger
from prompts import generic_system_prompt

from main import llm

logfile = "output.log"

logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)


def get_generic_response(query: str):
    try:
        prompt = PromptTemplate(input_variables=["query"], template=generic_system_prompt)
        final_chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler], verbose=True)
        res = final_chain.invoke({"query": query})
        return res["text"]
    except:
        return "Can you please rephrase the question?"
