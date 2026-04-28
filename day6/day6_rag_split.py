
doc_content = """
聂哥-企业内部资料
1. 公司商城系统基于 RuoYi-Vue-Pro 开发
2. 后端核心技术：Java、SpringBoot、MySQL、Redis、Docker
3. 未来技术升级方向：整合AI大模型、RAG知识库、智能问答
4. 私有化部署要求：内网离线使用、数据不上云、安全可控
5. 团队技术栈统一：容器化部署、Linux运维、接口标准化
"""

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

if __name__ == "__main__":
    print("===== day6 ====")
    chunk_list = split_text(doc_content)

    print(f"原始长度：{len(doc_content)}")
    print(f"切分后块数：{len(chunk_list)}")
    print("\n切分后文本块数")
    for idx, chunk in enumerate(chunk_list):
        print(f"\n块{idx+1}:{chunk}")









