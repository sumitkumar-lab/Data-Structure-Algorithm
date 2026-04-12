"""
Why Type Hints in AI Engineering?
AI pipelines pass complex data between many components — prompts, responses, tool calls, 
agent states, API payloads. Without type hints, it's a mystery what each function expects. 
Type hints make code self-documenting, enable IDE autocomplete, and catch bugs at development time instead of production.

"""
from typing import Optional, Union, Any
from collections.abc import Callable


# Basic type
def greet(name: str, times: int = 1) -> str:
    return f"Hello {name} ! " * times

print(greet("sumit"))

# Collections
def process_messages(messages: list[str]) -> dict[str, int]:
    return {msg: len(msg) for msg in messages}

print(process_messages(["Sumit", "Kumar"]))

# Optional -- Value can be None
def get_system_prompt(role: Optional[str] = None) -> str:
    if role is None:
        return "You are a helpful assistant."
    return f"You are an {role}"

print(get_system_prompt("Experienced AI Engineer !"))

# Union -- value can be one of several types
def parse_response(response: Union[str, dict]) -> str:
    if isinstance(response, dict):
        return response.get("content", "")
    return response

print(parse_response([{"sumit":25}]))

# Callable -- functionals as parameters (common in agent callabacks)
def with_retry(func: Callable, max_retries: int = 3) -> Any:
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            if i == max_retries -1:
                raise e
            
def callback():
    return "LLM start !"

print(with_retry(callback))

# ------------------------------------------------------------------------
from collections.abc import Callable
from typing import Any
import time


def with_retry(func: Callable, max_retries: int = 3, delay: float = 1.0) -> Any:
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            time.sleep(delay)

import random

def unreliable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

result = with_retry(unreliable_function, max_retries=3)
print(result)

# --------------- FallBack --------------- #
from langchain.chat_models import ChatOpenAI

primary = ChatOpenAI(model="gpt-4")
fallback = ChatOpenAI(model="gpt-3.5-turbo")

llm = primary.with_fallbacks([fallback])