<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://ctf.mzy0.com"><img src="https://github.com/Tokeii0/LovelyMem/blob/main/res/logo.png" width="250" height="250" alt="lovelymem"></a>
</p>
<div align="center">

# LovelyMem

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
_✨ 基于*Memprocfs*和*Volatility*的可视化内存取证工具 ✨_
<!-- prettier-ignore-end -->
<a href="https://jq.qq.com/?_wv=1027&k=DzOtbzU4"><img src="https://img.shields.io/badge/QQ%E7%BE%A4-856729462-orange?style=flat-square" alt="QQGroup"></a>
  <a href="http://ctf.dog"><img src="https://img.shields.io/badge/CTF%E5%AF%BC%E8%88%AA%E7%AB%99-ctf.dog-5492ff?style=flat-square" alt="ctfnav"></a>
  <a href=".."><img src="https://img.shields.io/badge/Python%20-%203.10.11-def1f2?style=flat-square" alt="python"></a>
</div>


### 这是什么
一款基于memprocfs、Volatility2、Volatility3的快捷内存取证工具

区别于VolatilityPro：https://github.com/Tokeii0/VolatilityPro

有着更快的取证速度以及更便捷的功能

视频展示：https://www.bilibili.com/video/BV1z912YpECB

### 界面展示
![afaaaddd5831755531faf4cf8b5bf0e3](https://github.com/user-attachments/assets/3908f151-fe34-4395-b948-912897a8a041)
![image](https://github.com/user-attachments/assets/86f9a7d4-1155-4c89-948e-8fe658753fbd)


### 功能展示
![image](https://github.com/user-attachments/assets/d8444026-8961-4abb-82ef-552202fa24e9)

![image](https://github.com/user-attachments/assets/bd621138-92bd-45e1-b1a6-c605cfff3827)
![image](https://github.com/user-attachments/assets/e661a949-7861-404e-b031-410857f02e14)
![image](https://github.com/user-attachments/assets/b527cff8-d42f-4072-ac33-b3810eab96aa)


### 适合什么题
  - 没有套娃的取证题目
  - *Windows*内存取证
### 更新
![image](https://github.com/user-attachments/assets/7104b3cd-8023-4909-9268-bc65d495211e)

  
### 你都更新了点啥

📌 **更新日志**  
1. 🎨 全新界面设计，提供上百种可选择的主题配色！  
2. 🛠️ 重写了标题栏及窗口控制按钮（关闭/最小化）。  
3. 🧰 **Memprocfs** 功能区域进行了基础功能和时间线的分类，新增系统信息查看功能，集成了 `systeminfo` 的内容。  
4. 🚀 在 **vol2** 区域，功能划分为六大类：基础功能、高级功能、系统信息、用户信息、文件导出和扩展功能。  
5. 🔍 **vol3** 区域采用了与 vol2 不同的分类方式：进程信息、系统信息、文件与网络、注册表、恶意代码检测、其他功能。后续会根据用户反馈考虑是否统一分类方式。  
6. 🐍 **vol2** 版本从封装好的 exe 程序转为 Python 2 版本，需在使用前安装 VCForPython27。  
7. 📁 **Tools** 分类从 `lovelymem` 文件夹移出，与其并列存放，若不适应可自行调整位置，并修改 `lovelymem/config/base_config.yaml` 文件。  
8. ⚡ 优化了 CSV 文件的读取速度，现在速度更快。  
9. 📊 为常用功能（如 `filescan`、`pslist`）设置了表格查看时的专用菜单。  
10. 🔎 表格内搜索现在直接显示在界面下方，不会弹出新窗口。  
11. 🚀 预设槽与正则槽支持快速任务执行，帮助你快速定位所需内容。  
12. 📚 新增 **vol2** 常备知识功能，方便学习使用。  
13. 🖥️ 现在支持通过 **memprocfs**、**vol2** 和 **vol3** 三种途径导出文件，支持快速将 `memdump` 转为 GIMP 文件。

这样看起来更简洁活泼，也更容易阅读了！

### 其他
远离内卷，还CTF圈一个朗朗乾坤

愿望是取证像喝水一样简单

