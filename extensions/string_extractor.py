import re

plugin_info = {
    "title": "字符串提取", 
    "description": "从文件中提取可打印字符串",
    "usage": "选择一个文件,然后点击此插件",
    "category": "文件分析"
}

def run(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    
    strings = re.findall(b'[\x20-\x7E]{4,}', content)
    print("提取的字符串:")
    for s in strings[:20]:  # 只打印前20个字符串
        print(s.decode())
    print(f"总共提取了 {len(strings)} 个字符串")
