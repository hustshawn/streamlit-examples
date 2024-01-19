import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.chat_models.bedrock import BedrockChat
from langchain.agents import AgentType, initialize_agent, load_tools


# Reference: https://python.langchain.com/docs/integrations/callbacks/streamlit
st.title('🦜🔗 Agent & Streaming App')


model_id = 'anthropic.claude-v2'
st_callback = StreamlitCallbackHandler(st.container())

llm = BedrockChat(
    credentials_profile_name='us-east-1',
    model_id=model_id,
    streaming=True
)

tools = load_tools(['ddg-search'])
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        response = agent.run(prompt, callbacks=[
                             st_callback])
        st.write(response)
