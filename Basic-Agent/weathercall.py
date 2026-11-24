from langchain.chat_models import init_chat_model
from langchain.tools import tool
from dotenv import load_dotenv
from rich import print
load_dotenv()


# tools
@tool
def get_weather(location:str)->str:
    '''Get the weather of the location '''
    return f"The weather of the location {location} is sunny. "



llm = init_chat_model("groq:openai/gpt-oss-20b")


tools = [get_weather]


llm_with_tools = llm.bind_tools(tools)


response = llm_with_tools.invoke("What is the current weather of Butwal?")

print(response)