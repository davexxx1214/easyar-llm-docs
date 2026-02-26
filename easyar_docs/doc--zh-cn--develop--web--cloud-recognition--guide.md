---
source: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/guide.html
---

图像云识别 Web 开发者指南 | EasyAR 文档
**
##### Table of Contents
**
# 图像云识别 Web 开发者指南
在 Web 端实现图像云识别的关键流程涵盖以下几个核心环节：首先通过浏览器调用摄像头捕获实时画面，随后将采集到的图像数据上传至云端服务器进行识别处理，最终接收并解析云端返回的结果，完成整个图像识别闭环。
## 开发步骤
不同浏览器对摄像头处理的实现存在差异，本文示例代码未涵盖所有浏览器兼容性问题，建议根据实际环境进行调整。
流程如下：
```
`flowchart LR
A((初始化摄像头)) --&gt; B[截取摄像头图片] --&gt; C{调用云识别 API}
C ----&gt; |未识别到目标| B
C ----&gt; |识别到目标| D((业务逻辑处理))
`
```
### 前置设置
在 html 页面中添加以下元素：
```
`&lt;video id="video"&gt;&lt;/video&gt;
&lt;canvas id="canvas"&gt;&lt;/canvas&gt;
`
```
在 js 代码中添加以下内容，获取必需的对象：
```
`const videoEl = document.querySelector('#video');
const canvasEl = document.querySelector('#canvas');
const canvasCtx = canvasEl.getContext('2d');
`
```
* `videoEl` 为 `video` 元素，将摄像头视频流绑定到 `video` 上实时预览
* `canvasEl` 为 `canvas` 元素
* `canvasCtx` 为 `canvas` 的 context 2d 对象
### 初始化摄像头
```
`const constraints = {
audio: false,
video: true,
};
navigator.mediaDevices.getUserMedia(constraints).then((stream) =&gt; {
videoEl.srcObject = stream;
videoEl.play();
}).catch((err) =&gt; {
console.error(err);
alert('打开摄像头错误');
});
`
```
* 摄像头参数设置
* `constraints.video` 为 `true`，自动选择摄像头
* `constraints.video` 为 `{facingMode: {exact: 'user'}}`，使用前置摄像头
* `constraints.video` 为 `{facingMode: {exact: 'environment'}}`，使用后置摄像头
##### 提示
更多摄像头参数，参考 [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)。
### 截取摄像头图片
```
`canvasCtx.drawImage(videoEl, 0, 0, videoEl.offsetWidth, videoEl.offsetWidth);
const image = canvasElement.toDataURL('image/jpeg', 0.8).split('base64,').pop();
`
```
### 调用云识别 API
```
`// 云图库的 Client-end URL
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
}).then(res =&gt; res.json()).then(data =&gt; {
console.info(data);
// TODO: 识别结果处理
});
`
```
##### 提示
发送网络请求可以使用 `fetch`、`XMLHttpRequest` 或 `axois` 库等。
### 识别结果处理
云识别服务 API 接收到请求后，若成功识别到目标则返回识别结果；若未识别到目标，则返回未识别到状态码；若是其它错误，返回对应错误码及提示信息。
#### 未识别到目标
如果未识别到目标，`statusCode` 为 17， 返回结果如下：
```
`{
"statusCode" : 17,
"result" : {
"message" : "No result: there is no matching."
},
"date" : "2026-01-05T05:49:02.651Z",
"timestamp" : 1767592142651
}
`
```
#### 识别到目标
如果识别到目标，`statusCode` 为 0，返回结果如下：
```
`{
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
`
```
主要字段说明：
* targetId: 目标 id
* meta: base64 编码的附加信息，在上传识别图时添加的 3D 内容或视频 URL 等内容
* name: 目标名称
* active: "1" 为启用状态，"0" 为禁用状态
##### 提示
完整字段信息查看 [API 参考](../../../api/cloud/cloud-recognition/apis.html)
### 业务逻辑处理
您可以使用 `meta` 中的信息处理后续业务逻辑，如播放视频，渲染 3D 模型等。
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)