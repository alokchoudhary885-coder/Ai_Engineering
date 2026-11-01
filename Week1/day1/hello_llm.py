# 1. Import libraries
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# 2. Load environment variables
load_dotenv()

# 3. Get API key
my_api_key = os.getenv("GROQ_API_KEY")

# 4. Check API key
if not my_api_key:
    raise ValueError("API key not found")

# 5. Create Groq client
client = Groq(api_key=my_api_key)

# 6. Select AI model
model = "openai/gpt-oss-120b"

# 7. Define role and prompt
role = "user"
prompt = "Explain Artificial Intelligence in simple words"

# 8. Create message
message = {
    "role": role,
    "content": prompt
}

# 9. Create messages list
messages = [message]

# 10. Send request to Groq
response = client.chat.completions.create(
    model=model,
    messages=messages
)

# 11. Print AI response
print(response.choices[0].message.content)