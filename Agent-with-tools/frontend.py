
import streamlit as st
from backend import agent

# Page configuration
st.set_page_config(
    page_title="Weather & News AI",
    page_icon="🌤️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    .stChatMessage {
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<div class="main-title">🌤️ Weather & News AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI assistant for weather updates and latest news.</div>',
    unsafe_allow_html=True
)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:
    st.title("🌍 Weather & News AI")

    st.write(
        "Ask me about the weather or latest news "
        "from any city around the world."
    )

    st.divider()

    st.subheader("Try asking")

    examples = [
        "What's the weather in Butwal?",
        "Latest news in Kathmandu",
        "Tell me the weather in New Delhi",
        "What's happening in Pokhara today?"
    ]

    for example in examples:
        if st.button(example, use_container_width=True):
            st.session_state.user_prompt = example

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
prompt = st.chat_input("Ask about weather or news of any city...")

# Handle sidebar example
if "user_prompt" in st.session_state:
    prompt = st.session_state.pop("user_prompt")


if prompt:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = agent.invoke({
                    "messages": st.session_state.messages
                })

                answer = response["messages"][-1].content

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Something went wrong: {e}")
