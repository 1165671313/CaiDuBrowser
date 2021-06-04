import sys
import webbrowser
import urllib.parse
import tkinter.messagebox
import easygui
import time
root = tkinter.Tk()
root.withdraw()
t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
xuanze = tkinter.messagebox.askokcancel('选择引擎', '是否使用百度作为引擎/必应')
time = open('Time.txt', 'a+')
xuanze2 = tkinter.messagebox.askokcancel('无痕浏览', '是否使用无痕浏览？')
def sousuo():
    global url
    if sousuokuang == 'news' or sousuokuang == '新闻':
        url = r'https://www.toutiao.com/'
    elif sousuokuang == 'fanyi' or sousuokuang == '翻译':
        url = r'https://translate.google.cn/'
    elif sousuokuang == '开发者社区' or sousuokuang == '编程':
        url = r'https://www.csdn.net/'
    elif True == xuanze:
        url = r'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + mr + '&rsv_pq=e4cc087c00319f1e&rsv_t=11de%2F5rzvp7nS7o%2FyWSXYL45YjaRlfnvVfroVVk7Jotq8cnMOItCJa3IFm4&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=5555&rsv_sug3=18&rsv_sug1=13&rsv_sug7=101&rsv_sug2=0&rsv_sug4=5555'
    elif False == xuanze:
        url = r'https://cn.bing.com/search?q=' + mr
    webbrowser.open(url)
while True:
    try:
        for i in range(9999999**2):
            sousuokuang = easygui.enterbox('请输入您要搜索网页:', '彩度搜索0.0.5', '搜索', True)
            if sousuokuang =='' or sousuokuang == '搜索':
                tkinter.messagebox.showerror('错误', '您没有输入搜索内容')
                break
            else:
                mr = urllib.parse.quote(sousuokuang)
                sousuo()
                if not xuanze == True:
                    yinqing = '搜搜引擎：必应'
                else:
                    yinqing = '搜索引擎：百度'
                if xuanze2 != True:
                    time.write(t +'  ' + '搜索内容：' + sousuokuang + ' ' + yinqing + '\n')
                    sys.path.append("libs")
                    time.close()
                else:
                    sys.path.append("libs")

    except TypeError:
        TO=tkinter.messagebox.askokcancel('关闭', '是否关闭彩度浏览器0.0.5')
        if True == TO:
            tkinter.messagebox.showinfo('已关闭', '已关闭，如有疑难杂症或建议请发邮件至otnplbysn@foxmail.com')
            break
print(webbrowser.get())
