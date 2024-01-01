import requests
import json
from project.config import ai_token

url = "https://api.theb.ai/v1/chat/completions"
# url = "https://api.baizhi.ai/v1/chat/completions"

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "what is protein"
    }
  ],
  "stream": False
})
headers = {
  'Authorization': f'Bearer {ai_token}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())

