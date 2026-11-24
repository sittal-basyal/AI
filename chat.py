import os 
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')


os.environ["LANGSMITH_PROJECT"] = "langchain-tutorial"


# Initialize LLM
llm = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq"
)


from langchain.agents import create_agent


agent = create_agent (
    "openai/gpt-oss-20b",
    model_provider="groq",
    tools = [],
    system_prompt='You are an helpful assistant',
    
)

print(agent)