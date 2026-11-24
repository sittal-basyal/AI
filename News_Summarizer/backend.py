from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.tools import tool 
from langchain_tavily import TavilySearch

from dotenv import load_dotenv

load_dotenv()


# initialize the llm
llm = init_chat_model("groq:openai/gpt-oss-20b")

# prompt
prompt = ChatPromptTemplate.from_template(
    '''
You are a helpful assistant 

Summarize the following news into clear bullet points

{news}
'''
)

# parser
parser = StrOutputParser()

# search tool

search_tool = TavilySearch(max_results= 5)


# chain 

chain = prompt | llm | parser
