import requests

# ------------ 填入你自己的阿里云百炼 Key ------------
API_KEY = "youkey"
URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

def ali_llm_chat(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "qwen-turbo",
        "input": {
            "messages": [
                {"role": "user", "content": question}
            ]
        },
        "parameters": {
            "result_format": "text"
        }
    }

    # 发送请求
    res = requests.post(URL, headers=headers, json=body)

    # ========== 调试用：打印状态码 + 返回内容 ==========
    print("状态码:", res.status_code)
    print("返回内容:", res.text)
    # =================================================

    # 尝试解析
    try:
        json_data = res.json()
        return json_data["output"]["text"]
    except:
        return "解析失败，请检查KEY"

if __name__ == "__main__":
    print("===== Day4 大模型真实调用 =====")
    ask = "我有15年Java后端经验，怎么平稳转型AI应用开发？"
    ans = ali_llm_chat(ask)
    print("\n最终AI回复：", ans)
