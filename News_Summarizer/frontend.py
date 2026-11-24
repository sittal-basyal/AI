
import streamlit as st
from backend import chain, search_tool

st.set_page_config(
    page_title="News Summarizer",
    page_icon="📰",
    layout="centered"
)

st.title("📰 News Summarizer")
st.write("Search and summarize the latest news.")

news = st.text_input("Enter a topic to search for news")

if st.button("Summarize News"):
    if news:
        with st.spinner("Searching and summarizing news..."):
            search_results = search_tool.invoke({"query": news})

            response = chain.invoke({
                "news": search_results
            })

            st.subheader("News Summary")
            st.markdown(response)
    else:
        st.warning("Please enter a topic.")
