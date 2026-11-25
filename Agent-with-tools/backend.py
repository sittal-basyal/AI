from langchain.tools import tool
from langchain.agents import create_agent
from tavily import TavilyClient


from dotenv import load_dotenv

import os 
import requests

load_dotenv()
API_KEY = os.getenv('OPEN_WEATHER_API_KEY')


# llm = init_chat_model("groq:openai/gpt-oss-20b")

@tool
def get_weather(city:str)->str:
    '''Get the current wweather of the given city'''
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return f"Error: {data.get('message' ,'Something went wrong.')}"

    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return f"Weather is {city} :{desc} {temp}°C"




tavily_client = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))
                             
@tool
def get_news(city:str)->str:
    '''Get latest news about the city'''
    
    response = tavily_client.search(
        query=f"Latest news in {city} today",
        search_depth = 'basic',
        max_results=3
    )
    results = response.get('results',[])

    if not results :
        return f"No news found about {city}"

    news_list = []

    for r in results:
        title = r.get('title','No title')
        url = r.get('url','')
        snippet= r.get('content','')

        news_list.append(
            f"{title}\n {url}\n {snippet[:100]}"
        )
    return f"Latest news in {city} :\n\n"+"\n\n".join(news_list)

agent = create_agent(
    model = "groq:openai/gpt-oss-20b",
    tools = [get_news,get_weather],
    system_prompt="You are an helpful AI assistant ",


)
