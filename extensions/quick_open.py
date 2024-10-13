from extensions.front.openfile import OpenFile # 调用快速


plugin_info = {
    "title": "快速打开文件", 
    "description": "快速打开文件",
    "usage": "选择一个文件,然后点击此插件",
    "category": "文件操作"
}


file_analyzer = OpenFile()

def run(file_path):
    file_analyzer.run(file_path)

