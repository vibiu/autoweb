## 用途

试图自动生成 python 脚本从而重现一次由 chrome 发出的请求.

## 用法

从 chrome 浏览器(必须是 chrome )的控制台的 Network 上的找到某个请求, 右键复制为curl(bash)格式(Copy as cURL(bash)), 然后粘贴到你的python脚本的第一行(注意是第一行), 然后按下组合建[ctrl+alt+shift+w], curl 就成为了一段可以直接用于 requests 请求的python脚本.

## 安装

1, 在 Sublime Text 上的主菜单上 Preferences -> Browse Packages 进入 sublime 的 packages 目录.

2, `git clone https://github.com/vibiu/autoweb`.

3, 重启 Sublime Text.

## 例子

在`req.py`中第一行有一个从 chrome 复制的请求[https://www.python.org/](https://www.python.org/)的 curl(bash) 命令:
```bash
curl 'https://www.python.org/' -H 'Accept-Encoding: gzip, deflate, sdch, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Referer: https://www.google.com/' -H 'Cookie: _ga=GA1.2.2111869917.1463301618; __utma=32101439.2111869917.1463301618.1465809531.1465881334.14; __utmz=32101439.1465881334.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)' -H 'Connection: keep-alive' --compressed
```

按下组合建 [ctrl+alt+shift+w].

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
