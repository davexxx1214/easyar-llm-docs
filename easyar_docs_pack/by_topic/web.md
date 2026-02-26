# EasyAR 专题包：web

适用于上下文长度有限时的分卷输入。

## 目录
- `web/cloud-recognition/guide.md`
- `web/cloud-recognition/quickstart.md`
- `web/cloud-recognition/sample.md`
- `web/getting-started/quickstart.md`

---

## 图像云识别 Web 开发者指南
- 章节路径: `web/cloud-recognition/guide.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/guide.html

# 图像云识别 Web 开发者指南
在 Web 端实现图像云识别的关键流程涵盖以下几个核心环节：首先通过浏览器调用摄像头捕获实时画面，随后将采集到的图像数据上传至云端服务器进行识别处理，最终接收并解析云端返回的结果，完成整个图像识别闭环。
## 开发步骤
不同浏览器对摄像头处理的实现存在差异，本文示例代码未涵盖所有浏览器兼容性问题，建议根据实际环境进行调整。
流程如下：
```
flowchart LR
A((初始化摄像头)) --> B[截取摄像头图片] --> C{调用云识别 API}
C ----> |未识别到目标| B
C ----> |识别到目标| D((业务逻辑处理))
```
### 前置设置
在 html 页面中添加以下元素：
```
<video id="video"></video>
<canvas id="canvas"></canvas>
```
在 js 代码中添加以下内容，获取必需的对象：
```
const videoEl = document.querySelector('#video');
const canvasEl = document.querySelector('#canvas');
const canvasCtx = canvasEl.getContext('2d');
```
* `videoEl` 为 `video` 元素，将摄像头视频流绑定到 `video` 上实时预览
* `canvasEl` 为 `canvas` 元素
* `canvasCtx` 为 `canvas` 的 context 2d 对象
### 初始化摄像头
```
const constraints = {
audio: false,
video: true,
};
navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
videoEl.srcObject = stream;
videoEl.play();
}).catch((err) => {
console.error(err);
alert('打开摄像头错误');
});
```
* 摄像头参数设置
* `constraints.video` 为 `true`，自动选择摄像头
* `constraints.video` 为 `{facingMode: {exact: 'user'}}`，使用前置摄像头
* `constraints.video` 为 `{facingMode: {exact: 'environment'}}`，使用后置摄像头
> **提示**
更多摄像头参数，参考 [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)。
### 截取摄像头图片
```
canvasCtx.drawImage(videoEl, 0, 0, videoEl.offsetWidth, videoEl.offsetWidth);
const image = canvasElement.toDataURL('image/jpeg', 0.8).split('base64,').pop();
```
### 调用云识别 API
```
// 云图库的 Client-end URL
const clientendUrl = '您云图库的 Client-end URL';
// 云图库的 Cloud Token
const token = '这里是云图库的 Cloud Token';
// 云图库的 CRS AppId
const appId = '这里是云图库的 CRS AppId';
// image 为上一步骤中截取的图片
const image = '/9j/4AAQSkZJRgABAQ......';
fetch(`${clientendUrl}/search`, {
method: 'POST',
body: `{ "image": "${image}", "appId": "${appId}", "notracking": true }`,
headers: {
'Content-Type': 'application/json;Charset=UTF-8',
'Authorization': token
}
}).then(res => res.json()).then(data => {
console.info(data);
// TODO: 识别结果处理
});
```
> **提示**
发送网络请求可以使用 `fetch`、`XMLHttpRequest` 或 `axois` 库等。
### 识别结果处理
云识别服务 API 接收到请求后，若成功识别到目标则返回识别结果；若未识别到目标，则返回未识别到状态码；若是其它错误，返回对应错误码及提示信息。
#### 未识别到目标
如果未识别到目标，`statusCode` 为 17， 返回结果如下：
```
{
"statusCode" : 17,
"result" : {
"message" : "No result: there is no matching."
},
"date" : "2026-01-05T05:49:02.651Z",
"timestamp" : 1767592142651
}
```
#### 识别到目标
如果识别到目标，`statusCode` 为 0，返回结果如下：
```
{
"statusCode" : 0,
"result" : {
"target" : {
"targetId" : "375a4c2e\*\*\*\*\*\*\*\*915ebc93c400",
"allowSimilar" : "0",
"detectableDistinctiveness" : 1,
"detectableFeatureCount" : 3,
"type" : "ImageTarget",
"trackableDistinctiveness" : 0,
"detectableFeatureDistribution" : 1,
"trackableFeatureCount" : 3,
"detectableRate" : 2,
"trackableFeatureDistribution" : 1,
"size" : "1",
"trackablePatchContrast" : 0,
"meta" : "eyJ2aWRlb1VybCI6Im\*\*\*\*\*\*\*\*pL0Vhc3lBUi1NZWdhLm1wNCJ9",
"grade" : "2",
"trackablePatchAmbiguity" : 3,
"name" : "Mega video",
"appKey" : "f7ff497\*\*\*\*\*\*\*\*f8068c",
"trackableRate" : 2,
"active" : "1",
"date" : "1746609056804",
"modified" : 1746609056804
}
},
"date" : "2026-01-05T05:50:36.484Z",
"timestamp" : 1767592236484
}
```
主要字段说明：
* targetId: 目标 id
* meta: base64 编码的附加信息，在上传识别图时添加的 3D 内容或视频 URL 等内容
* name: 目标名称
* active: "1" 为启用状态，"0" 为禁用状态
> **提示**
完整字段信息查看 [API 参考](../../../api/cloud/cloud-recognition/apis.html)
### 业务逻辑处理
您可以使用 `meta` 中的信息处理后续业务逻辑，如播放视频，渲染 3D 模型等。
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)

---

## 图像云识别 Web 开发快速入门
- 章节路径: `web/cloud-recognition/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/quickstart.html

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
./EasyAR-WebAR\_linux
```
* macOS 系统：
```
./EasyAR-WebAR\_darwin
```
* Windows 系统：
```
// 鼠标双击或在 cmd 中运行
EasyAR-WebAR\_windows.exe
```
## 体验 sample
在 PC 浏览器（需要摄像头）中输入 [http://127.0.0.1:3001/](http://127.0.0.1:3001/) ，建议使用火狐浏览器。
对准识别目标并查看 sample 的运行效果。
> **提示**
如果在手机上体验，需要配置支持 HTTPS 的域名。
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)

---

## 图像云识别 Web 示例
- 章节路径: `web/cloud-recognition/sample.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/sample.html

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
{
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
```
> **提示**
完整字段信息查看 [API 参考](../../../api/cloud/cloud-recognition/apis.html)
将 meta 使用 base64 解码，获取 meta 原始信息。
```
// data 为返回的数据
const meta = data.result.target.meta;
const modelInfo = JSON.parse(atob(meta));
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
> **提示**
以下内容讲解基于您已具备一定程度的 HTML 与 JavaScript 开发能力这一前提条件。若您尚未掌握这些基础技能，建议先系统学习相关知识，以便更好地理解后续内容。
我们将以 TokenThreeJsExample （渲染3D模型）为例，介绍 sample 中主要的源码说明。
### 业务处理
文件 `TokenThreeJsExample/asset/js/app.js` 主要方法说明。
* 初始化 App 对象
```
// 使用云识别的 Client-end URL 初始化 App 对象
const app = new App('https://af0c1ca3b........0601c74.cn1.crs.easyar.com:8443');
```
* 设置云识别相关信息
```
// 设置云识别库 AppId 与 token，与 app.useEasyAr() 只能选一个使用
app.setToken({
'crsAppId': 'f7ff4977......9984ef8068c', // 云别库的 CRS AppId
'token': 'pQWnZo1Qt4drnc........QXUQambomdPWEj9So' // APIKey + APISecret 生成的 Token
});
// 如果使用 EasyAR 提供的集成环境
// app.useEasyAr();
```
* 业务逻辑处理
```
app.callback = (msg) => {
// msg 为识别到目标的信息
// 解析其中的 meta 字段，处理业务逻辑
};
```
### UI 及初始化云识别
文件 `html/src/app.js`　主要方法说明。
* 初始化摄像头选择
```
constructor(url = '') {
}
```
* 使用自定义 Token 配置云别识
```
setToken(token) {
}
```
* 使用 EasyAR 集成环境配置云别识
```
useEasyAr() {
}
```
### 云识别处理
文件 `html/src/webar.js` 主要方法说明。
* 摄像头截图与云识别配置
```
constructor(interval, recognizeUrl, token, container) {
}
```
* 打开摄像头，检测设置横/竖屏视频流预览
```
openCamera(constraints) {
}
```
* 开启识别
```
startRecognize(callback) {
}
```
* 截图
```
captureVideo() {
}
```
* 发送截图到云识别服务识别
```
httpPost(data) {
}
```
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [云识别开快速入门](quickstart.html)
* [云识别开者指南](guide.html)
* [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)
* [three.js](https://threejs.org/)

---

## 在 Web 中使用 EasyAR
- 章节路径: `web/getting-started/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/getting-started/quickstart.html

# 在 Web 中使用 EasyAR
EasyAR WebAR 是以 Web 平台来集成 AR 技术，具有模式轻、部署快、传播性强等特点，可以轻松地运行在 Android，iOS，Windows，Mac 等系统的 Web 浏览器上，无需APP，真正实现跨平台。 EasyAR WebAR 当前支持 EasyAR 云识别服务，实现图像跟踪、图片云识别、3D渲染等功能。
> **注意**
目前 Web 平台仅支持图片云识别（CRS）功能，其他功能如物体识别、运动跟踪等不支持。
# 后续步骤
进一步了解如何快速在 Web 上部署 AR 内容，请参考。
* [web 快速入门](../cloud-recognition/quickstart.html)
