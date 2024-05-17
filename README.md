# 🌤️ Weather Chatbot Demo with Autogen

## Getting Started

Create a Python virtual environment and install required dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

In `run.py`, create a custom query to the chatbot by first editing the message field in the `user_proxy.initiate_chat function call:

```python
chat_result = user_proxy.initiate_chat(
    assistant,
    message="I'm visiting San Francisco. Do I need to carry an umbrella today?",
)
```

Now, execute `run.py` to see the chatbot's response.