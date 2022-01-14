"""
   File Name：     temp
   Description :
   Author :       本当迷
   date：          2022/1/14
"""
import os
import sys
import tkinter
import tkinter.messagebox
import webbrowser
from tkinter import ttk

# 获取路径
def get_resources_path(path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS  # 获取临时资源
    else:
        base_path = os.path.abspath(".")  # 获取临时路径
    return os.path.join(base_path, path)  # 返回绝对路径


LOGO_PATH = get_resources_path(os.path.join("resources", "favicon.ico"))

# 定义窗体类
class main_form:
    def __init__(self):
        self.window = tkinter.Tk()  # 实例化一个窗体，相当于创建有个窗体对象
        self.e = tkinter.StringVar()
        self. window.title("全网VIP电影免费播放——作者本当迷")  # 窗体标题
        self.window.iconbitmap(LOGO_PATH)  # 设置窗体的LOGO
        self.window["background"] = "#70f3ff"  # 设置窗体背景颜色
        self.window.geometry("600x300+400+200")  # 窗体配置 400x300为窗体大小  400+200为窗体位置
        self.lbl = tkinter.Label(self.window, text="请输入视频链接地址：", font=("微软雅黑", 18), justify="right")  # 文本标签
        self.lbl.pack()  # 文本显示
        self.entry = tkinter.Entry(self.window, validate='key', textvariable=self.e, width=50)

        self.entry.place(x=120, y=50)
        self.btn = tkinter.Button(self.window, text="点击自动播放", width=10, height=2)  # 按钮
        self.btn.bind('<Button-1>', lambda event : self.btn_click(self.e))
        self.btn.place(x=250, y=120)  # 按钮显示

        #定义下拉项
        self.frame = tkinter.Frame(self.window)
        tkinter.Label(self.frame, text="请选择视频源：", font=("微软雅黑", 15)).grid(row=0, column=0, sticky=tkinter.W)
        self.url_dict = {"比较稳定":"https://player.iuk.ink/m3u8.php?url=", "比较稳定1":"https://www.8090g.cn/jiexi/?url=" ,
                     "比较稳定2":"https://jx.1080jx.top/vipjx/?url=", "比较稳定3":"https://jiexi.zjmiao.com/?url="}
        self.url_key = ["比较稳定", "比较稳定1", "比较稳定2", "比较稳定3"]
        self.url_combobox = ttk.Combobox(self.frame, values=self.url_key)
        self.url_combobox.bind("<<ComboboxSelected>>", self.show_data)
        self.url_combobox.grid(row=0,column=1)
        self.frame.place(x=120, y=80)
        self.content = tkinter.StringVar()

        # 显示下拉项内容
        self.label1 = tkinter.Label(self.window, textvariable=self.content, font=("微软雅黑", 15), width=20, height=2)
        self.label1.place(x=170, y=200)

        self.window.protocol("WM_DELETE_WINDOW", self.close_handle)  # 窗体事件关闭操作

        tkinter.mainloop()

    # 拿到下拉组建内容
    def show_data(self, even):
        self.content.set("选择为：%s"% self.url_combobox.get())

    # 点击按钮转跳浏览器事件
    def btn_click(self, info):
        url = info.get()
        if url == '':
            url = "https://v.qq.com/x/cover/mzc00200zg9wfe2/c32396n71zw.html"
        source = self.url_dict[self.url_combobox.get()]
        final_url = source + str(url)
        webbrowser.open_new(final_url)
        tkinter.messagebox.showinfo("温馨提示！", "请耐心等待视频加载哦~~~")

    # 窗体关闭操作
    def close_handle(self):
        if tkinter.messagebox.askokcancel("程序关闭确认", "这么好的程序你舍得关闭吗？"):
            self.window.destroy() # 关闭程序

def main():  # 主函数
    main_form()

if __name__ == "__main__":
    main()  # 调用主函数
