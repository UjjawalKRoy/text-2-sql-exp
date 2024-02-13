from langchain.callbacks import FileCallbackHandler
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from loguru import logger

from main import llm

logfile = "output.log"

logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)

system_prompt = """
    [INST]
    You are an AI assistant who is very helpful and answers the questions asked by the user. Yo are honest, helpful, 
    friendly and respectful. Below is the question asked by the user.
    
    ###QUESTION:
    {query}
    
    ###RESPONSE:
    [/INST]
    """


def get_generic_response(query: str):
    prompt = PromptTemplate(input_variables=["query"], template=system_prompt)
    final_chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])
    res = final_chain.invoke({"query": query})
    return res["text"]
