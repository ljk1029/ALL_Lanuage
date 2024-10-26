import os
import openai

#填入你的OPENAI_API_KEY
#openai.api_key = "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"
openai.api_key = "sk-you key"

#代理设置：如果你在墙内需要使用代理才能调用，支持http代理和socks代理
#openai.proxy = "http://127.0.0.1:1080"

#这里我们使用的model是gpt-3.5-turbo
#使用角色为role，提问的内容是：Hello!
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

#输出生成的内容
print(completion.choices[0].message)

#把整个响应输出一下
print(completion)