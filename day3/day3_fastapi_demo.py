from fastapi import FastAPI
import uvicorn

app = FastAPI(title="AI学习服务", version="1.0")

@app.get("/hello")
def hello():
    return {
        "code": 200,
        "message": "Hello World",
        "data": "java转ai,稳步转型"
    }

@app.get("/ai/chat")
def ai_chat(question: str):
    return {
        "question": question,
        "answer": "FastApi 调用接口正常，为后续大模型对接做好准备"
    }

@app.post("/ai/send")
def send_msg(content: str):
    return {
        "status": "success",
        "input": content,
        "tip": "FastApi 调用接口正常，为后续大模型对接做好准备"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)