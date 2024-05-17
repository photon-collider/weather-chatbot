import os
import tools
from autogen import ConversableAgent, register_function

from dotenv import load_dotenv

load_dotenv()

assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI weather assistant. "
    "You can help with providing recommendations to the user based on available weather data. "
    "Return 'TERMINATE' when the task is done.",
    llm_config={
        "config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}],
        "cache_seed": None,
    },
)

user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None
    and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

register_function(
    tools.get_current_weather,
    caller=assistant,
    executor=user_proxy,
    description="A tool for obtaining weather information. Units are given in metric.",
)

chat_result = user_proxy.initiate_chat(
    assistant,
    message="I'm visiting San Francisco. Do I need to carry an umbrella today?",
)
