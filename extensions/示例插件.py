import zipfile
import os

# 插件信息字典,包含插件的基本信息
plugin_info = {
    "title": "解压文件",  # 插件标题
    "description": "解压ZIP、RAR等压缩文件",  # 插件描述
    "usage": "选择一个压缩文件,然后点击此插件",  # 使用说明
    "category": "文件操作"  # 插件类别
}

def run(file_path):
    """
    插件的主要执行函数
    
    参数:
    file_path (str): 要处理的文件的路径
    
    返回:
    None
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误: 文件 {file_path} 不存在")
        return

    # 获取文件扩展名
    _, file_extension = os.path.splitext(file_path)
    
    # 根据文件扩展名选择相应的解压方法
    if file_extension.lower() == '.zip':
        extract_zip(file_path)
    else:
        print(f"不支持的文件类型: {file_extension}")

def extract_zip(file_path):
    """
    解压ZIP文件
    
    参数:
    file_path (str): ZIP文件的路径，即文件槽内文件路径
    
    返回:
    None
    """
    try:
        # 创建输出目录
        output_dir = os.path.join('output', 'extracted_files')
        os.makedirs(output_dir, exist_ok=True)
        
        # 解压文件
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        
        print(f"文件已成功解压到: {output_dir}")
        
        # 列出解压后的文件
        print("解压的文件列表:")
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                print(os.path.join(root, file))
    
    except zipfile.BadZipFile:
        print("错误: 无效的ZIP文件")
    except Exception as e:
        print(f"解压过程中发生错误: {str(e)}")

# 注意: 如果需要支持其他类型的压缩文件(如RAR),
# 可以添加相应的解压函数并在run()中调用
