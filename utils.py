from openai import OpenAI
from config import *
def get_chat_completion(chat, histroy=[], model=default_gpt_model, max_tokens=2048):
    if not isinstance(chat, list):
        chat = histroy+[{"role": "user", "content": chat}]
    client = OpenAI(api_key=personal_key, base_url=personal_base)
    chat_completion = client.chat.completions.create(model=model,
                                                   messages=chat,
                                                   response_format={"type": "text"},
                                                   max_tokens=max_tokens,
                                                   temperature=0.1,
                                                   frequency_penalty=0.0,
                                                   presence_penalty=0.0)
    chat = chat + [{"role": "assistant", "content": chat_completion.choices[0].message.content}]
    return chat_completion.choices[0].message.content, chat # response,history
