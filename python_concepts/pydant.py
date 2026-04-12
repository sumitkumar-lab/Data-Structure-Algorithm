"""
Structured Data for AI Systems...

Pydantic turns your type hints into runtime validators. When your AI agent receives 
a JSON response or a tool call, Pydantic validates the data structure automatically 
and raises clear errors when something is wrong. This is essential for reliable AI systems.

📦 Why Pydantic?  LLM outputs are unpredictable. Pydantic gives you automatic validation, 
clear error messages, easy serialization to/from JSON, and nested model support — all 
critical for production AI pipelines.
"""
class User:
    def unique():
        name: str = "sumit"
        age: int = 25


user = User()
print(user.unique())








# from typing import Optional
# from pydantic import BaseModel, Field, field_validator

# class User(BaseModel):
#     name: str = Field(..., description="User's full name")
#     # age: Optional[int]
#     age: int
#     in_stock: bool
#     classes: int = Field(gt=2)

#     @field_validator("name")
#     @classmethod
#     def validate_name(cls, v):
#         if not v.isidentifier():
#             raise ValueError("Invalid name")
#         return v
    
#     @field_validator("age")
#     @classmethod
#     def validate_age(cls, v):
#         if v < 0:
#             raise ValueError("Age can't be Negative")
#         return v

# user = User(name="Sumit" , age=25 ,in_stock=False, classes=5)
# print(user.name)








# from pydantic import BaseModel, Field, field_validator
# from typing import Optional, Literal, Any
# from datetime import datetime

# # Model for an LLM Tool/Functional call
# class ToolCall(BaseModel):
#     name: str = Field(..., description='Name of the tool to call')
#     arguments: dict[str, Any] = Field(default_factory=dict)

#     @field_validator('name')
#     @classmethod
#     def name_must_be_valid(cls, v: str) -> str:
#         if not v.isidentifier():
#             raise ValueError(f"Tool name '{v}' must be a valid python identifier")
#         return v
    
# tool = ToolCall(name="valid")
# # print(tool.name_must_be_valid("Document"))

# print(tool.model_dump())