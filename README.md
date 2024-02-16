# 本地部署具体步骤
## Step1 下载模型
由于有墙的限制，在挂VPN的时候，通过程序下载模型容易被中断很不稳定。
所以我建议直接在huggingface官网上下载模型，然后将指定路径配置到api.py里面
这是模型下载地址[chatglm3-6b](https://huggingface.co/THUDM/chatglm3-6b/tree/main)
### 注意：不要全部下载完，根据下面图片内容下载
![image](https://github.com/langrentaole/local-deploy-chatGLM/assets/109889139/0953e593-c9ab-4361-82e6-c85b11e7381d)
## Step2 配置路径
将下载好的文件放在一个文件夹中，随意命名（不要有中文）。然后将该文件夹的路径放在api.py的model_path里面
### 例如
![image](https://github.com/langrentaole/local-deploy-chatGLM/assets/109889139/0bf88010-f560-462f-a4ed-193df5670eb8)
## Step3 运行程序
配置好路径之后，在终端或者idea里面运行api.py程序，静候其加载checkpoint。
直到本地部署完成
![image](https://github.com/langrentaole/local-deploy-chatGLM/assets/109889139/740182df-41ac-4bbe-b601-f7d9ad4b471d)

然后运行chatglm.py或者chatglm_langchain.py，你就可以开始和chatglm愉快的对话了
为了方便演示我开了两个终端。左边是请求记录，右边是你和chatglm的对话。当然这些都能在idea里面运行效果一致。
![image](https://github.com/langrentaole/local-deploy-chatGLM/assets/109889139/475790fa-6afa-4ac2-87a4-89f88281355d)




