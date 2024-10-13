from PIL import Image
import binascii

plugin_info = {
    "title": "隐写术检测", 
    "description": "检测图片中可能存在的隐写内容",
    "usage": "选择一个图片文件,然后点击此插件",
    "category": "CTF工具"
}

def run(file_path):
    try:
        with Image.open(file_path) as img:
            # 检查LSB
            pixels = list(img.getdata())
            lsb = ''.join([bin(p)[-1] for p in pixels[:100]])
            print("前100像素的LSB:")
            print(lsb)
            
            # 检查EXIF数据
            exif = img._getexif()
            if exif:
                print("EXIF数据:")
                for tag_id, value in exif.items():
                    print(f"{tag_id}: {value}")
            else:
                print("没有EXIF数据")
    except Exception as e:
        print(f"分析图片时出错: {str(e)}")
