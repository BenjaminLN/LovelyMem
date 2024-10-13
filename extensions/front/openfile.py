from plugin.NewtableWidget import NewtableWidget
from plugin.QuicklyView import QuicklyView
from PySide6.QtWidgets import QApplication
import os
import csv
import chardet
import traceback

class OpenFile:
    def __init__(self):
        self.table_widget = None

    def run(self, file_path):
        print(f"文件分析器正在处理文件: {file_path}")
        
        file_size = os.path.getsize(file_path)
        file_extension = os.path.splitext(file_path)[1]
        
        try:
            with open(file_path, 'rb') as file:
                raw_content = file.read(1000)
            encoding = chardet.detect(raw_content)['encoding']
            content = raw_content.decode(encoding or 'utf-8', errors='replace')
        except Exception as e:
            content = f"无法读取文件内容: {str(e)}"
        
        # 首先判断是否为CSV文件
        if file_extension.lower() == '.csv':
            try:
                self.table_widget = NewtableWidget(file_path, f"CSV内容 - {os.path.basename(file_path)}")
                self.table_widget.show()
                print("CSV文件内容已在表格中显示")
            except Exception as e:
                print(f"无法解析CSV文件: {str(e)}")
                traceback.print_exc()
        else:
            try:
                quick_view = QuicklyView(f"文件内容预览 - {os.path.basename(file_path)}")
                quick_view.load_file_content(file_path)
                QApplication.instance().processEvents()
                quick_view.show_and_exec()
                print("文件内容预览已在新窗口中打开")
            except Exception as e:
                print(f"显示 QuicklyView 时发生错误：{str(e)}")
                traceback.print_exc()
        
        print(f"文件大小: {file_size} 字节")
        print(f"文件扩展名: {file_extension}")
        print("文件分析器执行完毕")