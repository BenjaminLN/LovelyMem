import binascii

plugin_info = {
    "title": "文件头分析", 
    "description": "分析文件头信息",
    "usage": "选择一个文件,然后点击此插件",
    "category": "文件分析"
}

def run(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(16)
    
    print("文件头(十六进制):")
    print(binascii.hexlify(header).decode())
    
    # 常见文件头签名
    signatures = {
        b'\x89PNG\r\n\x1a\n': 'PNG图像',
        b'GIF87a': 'GIF图像(87a)',
        b'GIF89a': 'GIF图像(89a)',
        b'\xff\xd8\xff': 'JPEG图像',
        b'PK\x03\x04': 'ZIP压缩文件',
        b'MZ': 'Windows可执行文件',
        b'%PDF': 'PDF文档'
    }
    
    for sig, file_type in signatures.items():
        if header.startswith(sig):
            print(f"识别为: {file_type}")
            return
    
    print("未识别的文件类型")
