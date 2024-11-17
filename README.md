# Locate_location

## Intro

本工具制作初衷是为了快速定位到网站中哪一个js文件存在`location.href`/`location.assign`/`location.replace`反调试代码，以便快速替换。

## 实现原理

通过mitmproxy代理抓包，将存在以上那三个方法/属性的js文件下载到本地，并且会自动copy一份，copy的js文件名格式为：`xxx.temp.js`。copy的那一份js文件主要是为了方便使用者快速定位到反调试代码，然后再去源js文件删除那段js代码即可。

## 快速上手

使用之前需要安装一下mitmproxy库：

```shell
pip install mitmproxy
```

如果不懂怎么使用mitmproxy，可以看一下我的文章：<a href="https://mp.weixin.qq.com/s/6i2IQX4W3ZE0fQiKpfvN8w">JS逆向系列07-实战详解如何实现自动化加解密</a>

启动命令建议：
```shell
mitmdump -q -p 8888 -s main.py
```
这里我指定的8888端口，可自行更换。

具体注意事项参考我公众号最新文章(Spade sec)。

## Contact

如有bug或其他问题可提交issues，或者关注公众号Spade sec联系我。