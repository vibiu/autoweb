## 用途

试图自动生成python脚本从而重现一次由chrome发出的请求.

## 用法

从chrome浏览器（必须是chrome）的控制台的network上的找到某个请求，右键复制为curl(bash)格式(Copy as cURL(bash))，然后粘贴到你的python脚本的第一行（注意是第一行），然后按下组合建[ctrl+alt+shift+w],curl就成为了一段可以直接用于requests请求的python脚本.

## 安装

1, 在Sublime Text上的主菜单上Preferences -> Browse Packages 进入sublime 的packages 目录.

2, git clone https://github.com/vibiu/autoweb.

3, 重启sublime.

## 例子

在req.py中第一行有一个从chrome复制的请求[https://www.python.org/](https://www.python.org/)的curl(bash)命令:
```
curl 'https://www.python.org/' -H 'Accept-Encoding: gzip, deflate, sdch, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Referer: https://www.google.com/' -H 'Cookie: _ga=GA1.2.2111869917.1463301618; __utma=32101439.2111869917.1463301618.1465809531.1465881334.14; __utmz=32101439.1465881334.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)' -H 'Connection: keep-alive' --compressed
```

按下组合建[ctrl+alt+shift+r]

文件就转换成：
```
import requests
url = "https://www.python.org/"
headers = {
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36",
    "Cookie": "_ga=GA1.2.2111869917.1463301618; __utma=32101439.2111869917.1463301618.1465809531.1465881334.14; __utmz=32101439.1465881334.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
    "Referer": "https://www.google.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
}
data = None
if __name__ == '__main__':
    resp = requests.get(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.content)
```

可以直接这样运行脚本:
```
python req.py
```

## 执行python脚本依赖:
```
requests2.x
```
