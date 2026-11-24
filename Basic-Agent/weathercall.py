from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv
from rich import print

load_dotenv()


# tools
@tool
def get_weather(location: str) -> str:
    '''Get the weather of the location'''
    return f"The weather of the location {location} is sunny."


llm = init_chat_model("groq:openai/gpt-oss-20b")

tools = [get_weather]

tools_name = {
    'get_weather': get_weather
}

llm_with_tools = llm.bind_tools(tools)


response = llm_with_tools.invoke(
    [HumanMessage("What is the weather in Butwal?")]
)

context = []
context.append(HumanMessage("What is the weather in Butwal?"))
context.append(response)

if response.tool_calls:
    used_tool_name = response.tool_calls[0]['name']
    tool_response = tools_name[used_tool_name].invoke(
        response.tool_calls[0]['args']
    )

    context.append(
        ToolMessage(
            content=str(tool_response),
            tool_call_id=response.tool_calls[0]['id']
        )
    )

print(llm_with_tools.invoke(context).content)
