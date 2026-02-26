---
source: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/quickstart.html
---

图像云识别 Web 开发快速入门 | EasyAR 文档
**
##### Table of Contents
**
# 图像云识别 Web 开发快速入门
EasyAR WebAR 基于 Web 技术实现 AR 功能，与原生 AR 应用相比，具有轻量化、部署快、传播性广的特点。它无需安装 APP，即可在 Android、iOS、Windows、Mac 等系统的主流浏览器中运行，真正实现跨平台。
## 开始之前
在开始之前确保已经做好以下准备工作：
1. 支持云识别的 [API Key](../../apikey-auth.html)
2. 运行中的[云识别库](../../cloud-recognition/management.html)
## 上传云识别图片
准备一张识别图片，并上传到云识别库，上传方法参考 [图库管理](../../cloud-recognition/management-adding.html)。
## 下载 sample
为方便开发者快速开发，我们提供了示例代码 sample。开发者可下载这些示例，快速体验 WebAR 功能。
[点击下载](https://dl.easyar.cn/samples/EasyAR-WebAR-Demo.zip)
## 配置 sample
sample 代码中已预留配置项，请根据实际环境进行配置。
* 编辑 `config/application.txt` 文件
* 将 `API Key`、 `API Secret` 与 `CRS AppId` 替换到配置文件中
![云识别配置](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-config-1.jpg)
* 编辑示例目录下的 `asset/js/app.js` 文件
* 将云识别的 `Client-end (Target Recognition) URL` 替换到 `app.js` 中
![云识别配置](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-config-2.jpg)
## 运行 sample
`EasyAR-WebAR\_\*` 文件为 http 与 token 生成服务，如启动成功，会显示监听的端口号，启动方式如下：
* Linux 系统：
```
`./EasyAR-WebAR\_linux
`
```
* macOS 系统：
```
`./EasyAR-WebAR\_darwin
`
```
* Windows 系统：
```
`// 鼠标双击或在 cmd 中运行
EasyAR-WebAR\_windows.exe
`
```
## 体验 sample
在 PC 浏览器（需要摄像头）中输入 [http://127.0.0.1:3001/](http://127.0.0.1:3001/) ，建议使用火狐浏览器。
对准识别目标并查看 sample 的运行效果。
##### 提示
如果在手机上体验，需要配置支持 HTTPS 的域名。
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)