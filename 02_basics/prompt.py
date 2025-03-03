"""
Install an additional SDK for JSON schema support Google AI Python SDK

$ pip install google.ai.generativelanguage
"""

import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  tools = [
    genai.protos.Tool(
      google_search = genai.protos.Tool.GoogleSearch(),
    ),
  ],
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "What is the weather today in Zurich?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The weather in Zurich, Switzerland today, January 28, 2025, is as follows:\n\n*   **Temperature:** The temperature is currently around 5°C (41°F). The high for today is expected to be 8°C (46°F) and the low is 4°C (39°F)\n*   **Precipitation:** There is a high chance of rain today, with some sources stating a 90-100% chance of precipitation, with up to 2.9mm of rainfall possible. Some sources indicate a possibility of thunderstorms.\n*   **Conditions:** The weather is described as overcast with light to heavy rain. It feels like 3.56°C (38.4°F)\n*   **Wind:** The wind is light and variable, coming from the Southwest at around 9 km/h (6 mph).\n*   **Humidity:** The humidity is around 77-94%.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)