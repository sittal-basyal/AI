from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver

from langchain.messages import HumanMessage , SystemMessage 

from dotenv import load_dotenv

load_dotenv()

agent = create_agent(
    model = 'groq:openai/gpt-oss-20b',
    tools =[],
    system_prompt='You are a helpful AI assistant ',
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model = 'groq:openai/gpt-oss-20b',
            trigger=('messages',10),
            keep = ('messages',4)
        )
    ]
)


CONFIG = {
    'configurable':{
        'thread_id':"ss1"
    }
}

while True:
    query = input('User: ')
    if query in ['exit','bye']:
        break
    response = agent.invoke(
        {"messages": [HumanMessage(content=query)]},
        config=CONFIG)
    print(response["messages"][-1].content)