import requests
import streamlit as st
import base64
import time


def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )


# main_bg("path/to/your/background.png")

fastgpt_api_key = r"fastgpt-fug3pW7s3iywgggQWjS4wTvtl0vwlh30yltlk0TSGFk2rrmtYVOBve0"
fastgpt_api_url = r"https://bfnicgrb.bja.sealos.run/api/v1/chat/completions"

# 设置页面标题和唯一的session_state键
page_id = "page2"  
st.header("💞 孕小心", divider="rainbow")

# 使用唯一的session_state键
message_key = f"messages_{page_id}"

if message_key not in st.session_state:
    st.session_state[message_key] = [
        {
            "role": "assistant",
            "content": "您好！我是孕小心，请问有什么可以帮助您的吗？",
        }
    ]

# 显示聊天历史记录
for msg in st.session_state[message_key]:
    st.chat_message(msg["role"]).write(msg["content"])

# 获取输入
if prompt := st.chat_input():
    if not fastgpt_api_key:
        st.info("请添加密钥以继续。")
        st.stop()

    # 将用户输入添加到消息历史
    st.session_state[message_key].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # 显示进度条和动态文本
    progress_bar = st.progress(0)
    progress_text = st.empty()  # 使用 st.empty() 动态显示文本

    # 准备请求头和数据
    headers = {
        "Authorization": f"Bearer {fastgpt_api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "chatId": "abcd",  # 使用唯一的 ID 进行每个会话
        "stream": False,
        "detail": False,
        "variables": {
            "uid": "asdfadsfasfd2323",  # 用户唯一标识
            "name": "张三",  # 用户姓名
        },
        "messages": st.session_state[message_key],  # 发送整个消息历史
    }

    # 调用 FastGPT API
    try:
        # 模拟进度条更新
        progress = 0
        progress_step = 5  # 每次更新进度条的增量

        while progress < 80:
            time.sleep(0.1)
            progress += progress_step
            progress_bar.progress(progress)
            progress_text.text(f"孕小心思考中... {progress}% 完成")  # 动态更新进度条文字

        response = requests.post(fastgpt_api_url, headers=headers, json=data)
        response.raise_for_status()  # 如果响应错误，抛出异常

        # 打印完整响应内容
        response_data = response.json()
        # st.write("API 响应:", response_data)  # 打印响应以供调试

        # 从响应中提取内容
        if "choices" in response_data and len(response_data["choices"]) > 0:
            msg_content = response_data["choices"][0]["message"]["content"]
        else:
            raise KeyError(
                "'choices' key or its content is missing in the API response."
            )

        # 将回复添加到消息历史
        st.session_state[message_key].append(
            {"role": "assistant", "content": msg_content}
        )
        st.chat_message("assistant").write(msg_content)

        # 完成后将进度条更新至 100%，并显示完成的文字
        progress_bar.progress(100)
        progress_text.text("")

    except requests.exceptions.RequestException as e:
        st.error(f"网络请求错误: {str(e)}")
    except (KeyError, IndexError) as e:
        st.error(f"API 响应解析错误: {str(e)}")
    except Exception as e:
        st.error(f"未知错误: {str(e)}")
