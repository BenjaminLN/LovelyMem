import hashlib

plugin_info = {
    "title": "文件哈希计算", 
    "description": "计算文件的MD5, SHA1和SHA256哈希值",
    "usage": "选择一个文件,然后点击此插件",
    "category": "文件分析"
}

def run(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        print(f"MD5: {hashlib.md5(data).hexdigest()}")
        print(f"SHA1: {hashlib.sha1(data).hexdigest()}")
        print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
