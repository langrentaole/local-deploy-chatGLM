from langchain.llms import ChatGLM

endpoint_url = 'http://127.0.0.1:8000'
llm = ChatGLM(
    endpoint_url=endpoint_url,
    max_tokens=80000,  # 最大传入字符数
    top_p=0.9  # 控制生成文字的随机性 default 1，between 1 to 2，越大越随机
)
while True:
    user_input = input('user:')
    print(f'chatGLM:{llm(user_input)}')
