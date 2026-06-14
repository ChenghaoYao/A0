import os
from docx import Document

folder = r"C:\Users\Administrator\Desktop\20260125"

for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith(".docx"):
            docx_path = os.path.join(root, filename)
            txt_path = os.path.join(root, filename.replace(".docx", ".txt"))
            doc = Document(docx_path)
            with open(txt_path, "w", encoding="utf-8") as f:
                for para in doc.paragraphs:
                    f.write(para.text + "\n")
            print(f"已转换: {docx_path} → {txt_path}")

