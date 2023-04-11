import os
import openai

openai.api_key = "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"#os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Who are you?",
#   temperature=0.5,
#   max_tokens=1000#,
#   #top_p=1,
#   #frequency_penalty=0.0,
#  # presence_penalty=0.0,
#   #stop=["\n"]
# )

# print(response)
messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
    ]

def chat_response(message):

  messages.append(message)
  print(messages)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = messages

  )
  print(response["choices"][0]["message"])
  return response["choices"][0]["message"]

if __name__ == "__main__":
  message = {"role": "user", "content": "Who won the world series in 2020?"}
  print(chat_response(message)) #{"content":"xxxxxxxxxxx"}
