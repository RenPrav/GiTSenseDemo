import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# Now you can safely call models:
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello!"
)
exec()
print(response.text)
