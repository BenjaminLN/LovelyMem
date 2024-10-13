import base64
import re

plugin_info = {
    "title": "Base64解码", 
    "description": "尝试解码文件中的Base64编码内容",
    "usage": "选择一个文件,然后点击此插件",
    "category": "CTF工具"
}

def run(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    base64_pattern = re.compile(r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?')
    matches = base64_pattern.findall(content)
    
    for match in matches:
        if len(match) > 20:  # 忽略短字符串
            try:
                decoded = base64.b64decode(match).decode('utf-8')
                print(f"原始Base64: {match[:20]}...")
                print(f"解码结果: {decoded[:50]}...")
                print("---")
            except:
                pass
