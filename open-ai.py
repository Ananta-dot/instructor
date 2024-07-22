import openai

# Set up the OpenAI client
openai.api_key = 'sk-None-kXpAUQa1v3sD8lrGT5mhT3BlbkFJAW4k040umpbp6sFucA1X'  # Replace with your actual API key

# Test a simple API call
try:
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt="Hello, world!",
        max_tokens=5
    )
    print(response.choices[0].text.strip())
except openai.error.OpenAIError as e:
    print(f"Error: {e}")
