
name = "聂哥"
skill = "15年JAVA开发，转型AI应用开发有优势"
print(f"姓名：{name}")
print(f"技能：{skill}")

print("姓名：", name)
print("技能：", skill)

doc_list = ["企业制度文档","商城手册","客户资料"]
print("\n文档列表：",doc_list)

ai_config = {
    "model": "大模型",
    "api_key": "123456",
    "temperature": 0.7
}

print("\nAI配置：",ai_config)
print("模型名称：", ai_config["model"])

score = 90
if score >= 80:
    print("\n学习达标，稳步转型 AI")
else:
    print("继续加油")

print("\n遍历文档")
for doc in doc_list:
    print("-",doc)

def ai_hello():
    print("你好，我是AI")
    print("\n ====Day2 打卡成功 ====")
    print("Java转ai,稳步转型")

ai_hello()

if __name__ == "__main__":
    ai_hello()