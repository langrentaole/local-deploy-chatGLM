from langchain.llms import ChatGLM

endpoint_url = 'http://127.0.0.1:8000'
llm = ChatGLM(
    endpoint_url=endpoint_url,
    max_tokens=80000,
    top_p=0.9
)
while True:
    user_input = input('user:')
    print(f'chatGLM:{llm(user_input)}')
