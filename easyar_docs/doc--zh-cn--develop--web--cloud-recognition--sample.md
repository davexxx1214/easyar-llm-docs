---
source: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/sample.html
---

图像云识别 Web 示例 | EasyAR 文档
**
##### Table of Contents
**
# 图像云识别 Web 示例
本篇将带您深入分析样例代码，帮助您理解并在此基础上开发自己的实例。
sample 下载与配置说明，请参考[快速入门](quickstart.html)。
## 识别目标设置
在云识别管理中，[上传一张识别图片](../../cloud-recognition/management-adding.html)。
* 识别图片名称：给识别目标一个名称，如 demo。
* 上传识别图片：选择并上传一张图片，本样例中使用的图片为：
`https://www.easyar.cn/assets/images/webar/xiaoxiongmao.png`。
* 宽度：识别图的宽度（cm）。识别图的高度将由系统根据您上传的图片自动计算。识别图的大小和虚拟内容的大小对应，本样例中未使用。
* Meta：附加信息，一般用于存储AR内容信息，本样例中使用的内容为：` {"modelUrl": "asset/model/trex\_v3.fbx", "scale": 0.02}`。
![crs sample](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-sample-1.jpg)
## 识别目标获取
在调用云识别 API，识别到目标后，会返回目标信息，结构如下：
```
`{
"statusCode" : 0,
"result" : {
"target" : {
"targetId" : "375a4c2e\*\*\*\*\*\*\*\*915ebc93c400",
"meta" : "eyJtb2RlbFVybCI6ICJhc3NldC9tb2RlbC90cmV4X3YzLmZieCIsICJzY2FsZSI6IDAuMDJ9",
"name" : "demo",
"modified" : 1746609056804
}
},
"date" : "2026-01-05T05:50:36.484Z",
"timestamp" : 1767592236484
}
`
```
##### 提示
完整字段信息查看 [API 参考](../../../api/cloud/cloud-recognition/apis.html)
将 meta 使用 base64 解码，获取 meta 原始信息。
```
`// data 为返回的数据
const meta = data.result.target.meta;
const modelInfo = JSON.parse(atob(meta));
`
```
## 主要代码说明
* src/webar.js
封装了几个基本的操作，如初始化摄像头、截取图片、调用云识别等功能。
* src/app.js
封装了界面的基本操作，如摄像头切换、界面交互、以及 WebAR 的初始化操作。
* TokenVideoExample/asset/js/app.js 与 TokenThreeJsExample/asset/js/app.js
云识别的配置，及识别成功后的业务处理。
## 预期效果
* 摄像头初始化后界面
![预期效果](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-s-1.jpg)
* 播放视频效果
![预期效果](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-s-2.jpg)
* 渲染模型效果
![预期效果](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-s-3.jpg)
## 代码深入理解
若您期望对云识别开发进行更为深入的学习，强烈建议您阅读 sample 源码。在此基础上，您可以尝试对源码进行修改与扩展。
##### 提示
以下内容讲解基于您已具备一定程度的 HTML 与 JavaScript 开发能力这一前提条件。若您尚未掌握这些基础技能，建议先系统学习相关知识，以便更好地理解后续内容。
我们将以 TokenThreeJsExample （渲染3D模型）为例，介绍 sample 中主要的源码说明。
### 业务处理
文件 `TokenThreeJsExample/asset/js/app.js` 主要方法说明。
* 初始化 App 对象
```
`// 使用云识别的 Client-end URL 初始化 App 对象
const app = new App('https://af0c1ca3b........0601c74.cn1.crs.easyar.com:8443');
`
```
* 设置云识别相关信息
```
`// 设置云识别库 AppId 与 token，与 app.useEasyAr() 只能选一个使用
app.setToken({
'crsAppId': 'f7ff4977......9984ef8068c', // 云别库的 CRS AppId
'token': 'pQWnZo1Qt4drnc........QXUQambomdPWEj9So' // APIKey + APISecret 生成的 Token
});
// 如果使用 EasyAR 提供的集成环境
// app.useEasyAr();
`
```
* 业务逻辑处理
```
`app.callback = (msg) =&gt; {
// msg 为识别到目标的信息
// 解析其中的 meta 字段，处理业务逻辑
};
`
```
### UI 及初始化云识别
文件 `html/src/app.js`　主要方法说明。
* 初始化摄像头选择
```
`constructor(url = '') {
}
`
```
* 使用自定义 Token 配置云别识
```
`setToken(token) {
}
`
```
* 使用 EasyAR 集成环境配置云别识
```
`useEasyAr() {
}
`
```
### 云识别处理
文件 `html/src/webar.js` 主要方法说明。
* 摄像头截图与云识别配置
```
`constructor(interval, recognizeUrl, token, container) {
}
`
```
* 打开摄像头，检测设置横/竖屏视频流预览
```
`openCamera(constraints) {
}
`
```
* 开启识别
```
`startRecognize(callback) {
}
`
```
* 截图
```
`captureVideo() {
}
`
```
* 发送截图到云识别服务识别
```
`httpPost(data) {
}
`
```
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [云识别开快速入门](quickstart.html)
* [云识别开者指南](guide.html)
* [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)
* [three.js](https://threejs.org/)