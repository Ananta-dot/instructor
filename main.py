import instructor
from pydantic import BaseModel
from openai import OpenAI

class UserInfo(BaseModel):
    name: str
    age: int

client = instructor.from_openai(OpenAI(api_key='sk-None-kXpAUQa1v3sD8lrGT5mhT3BlbkFJAW4k040umpbp6sFucA1X'))

user_info = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=UserInfo,
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(user_info.name)
# John Doe
print(user_info.age)
# 30
