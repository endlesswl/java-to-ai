from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FakeEmbeddings

# 1. 模拟企业私有文档
doc_content = """
聂哥-企业内部资料
1. 公司商城系统基于 RuoYi-Vue-Pro 开发
2. 后端核心技术：Java、SpringBoot、MySQL、Redis、Docker
3. 未来技术升级方向：整合AI大模型、RAG知识库、智能问答
4. 私有化部署要求：内网离线使用、数据不上云、安全可控
5. 团队技术栈统一：容器化部署、Linux运维、接口标准化
"""

# 2. 文本切块（Day6 写好的方法）
def split_text(text, chunk_size=80, overlap=15):
    chunks = []
    start = 0
    text = text.strip().replace("\n", "")
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

# 3. 初始化 嵌入模型 + 向量库
embedding = FakeEmbeddings(size=512)
vector_db = Chroma(
    collection_name="company_doc",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)

if __name__ == "__main__":
    print("===== Day7 极简RAG 完整闭环 =====")

    # 步骤1：文档切块
    text_chunks = split_text(doc_content)
    print(f"切块完成，共 {len(text_chunks)} 块")

    # 步骤2：写入向量库
    vector_db.add_texts(text_chunks)
    vector_db.persist()
    print("✅ 文档已存入向量库")

    # 步骤3：用户问题 + 语义相似检索
    user_query = "公司后端技术栈有哪些？"
    search_docs = vector_db.similarity_search(user_query, k=2)

    print("\n===== 检索到的私有知识库内容 =====")
    for doc in search_docs:
        print("-", doc.page_content)

    # 步骤4：拼接上下文，喂给大模型（后续对接阿里/百度模型）
    context = "\n".join([d.page_content for d in search_docs])
    prompt = f"""
请根据已知知识库内容回答问题，不要瞎编：
知识库内容：{context}
用户问题：{user_query}
"""
    print("\n===== 最终发给大模型的提示词 =====")
    print(prompt)