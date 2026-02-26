---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/sample.html
original_file: doc--zh-cn--develop--wechat--cloud-recognition--sample.md
normalized_at: 2026-02-27
---
# 图像云识别微信小程序示例说明
本篇将带您深入分析样例代码，帮助您理解并在此基础上开发自己的实例。
sample 下载与配置说明，请参考[快速入门](quickstart.html)。
## 识别目标设置
在云识别管理中，[上传一张识别图片](../../cloud-recognition/management-adding.html)。
* 识别图片名称：给识别目标一个名称，如“熊猫”。
* 上传识别图片：选择并上传一张图片，本样例中使用的图片为：
![sample](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/model.jpg)
* 宽度：识别图的宽度（cm）。识别图的高度将由系统根据您上传的图片自动计算。识别图的大小和虚拟内容的大小对应，本样例中未使用。
* Meta：附加信息，一般用于存储 AR 内容信息，本样例中使用的内容：
```
{"modelUrl": "https://sightp-assets.sightp.com/crs-mini/xiaoxiongmao.glb", "scale": 0.4}
```
![sample](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-sample-1.jpg)
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
"trackingImage": "/9j/4AAQSkZJRgABAQ\*\*\*\*\*\*\*\*\*\*\*\*/9k=",
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
> **注意**
微信小程序中没有 `atob` 方法，需要自行实现。
实现方法在示例目录 `libs/atob.js` 文件中。
## 主要代码说明
* components/easyar-cloud/easyar-cloud.js
使用 `wx.createCameraContext` 打开摄像头、截取图片及访问云识别的等方法。
* components/easyar-ar/easyar-ar.js
使用 xr-frame 打开摄像头、截取图片、访问云识别及播放视频与渲染模板的等方法。
* components/libs/crs-client.js
Token 生成及云识别访问等方法。
> **警告**
不要在客户端（如 Web，微信小程序等）应用上直接使用 API Key 与 API Secret。
这里仅作演示使用，生产环境使用时请在服务端生成 Token。
## 代码深入理解
若您期望对云识别开发进行更为深入的学习，强烈建议您阅读 sample 源码。在此基础上，您可以尝试对源码进行修改与扩展。
> **提示**
以下内容讲解基于您已具备一定程度的 HTML 与 JavaScript 开发能力这一前提条件。若您尚未掌握这些基础技能，建议先系统学习相关知识，以便更好地理解后续内容。
微信小程序上使用的 XR/3D 引擎是 [XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)，如果您不熟悉，建议先参考一下文档。
我们将以渲染 3D 模型为例，介绍 sample 中主要的源码说明。
### UI 及场景处理
文件 `components\\easyar-ar\\easyar-ar.wxml`说明。
XR 场景及 Marker 设置。
```
<xr-scene ar-system="modes:Marker" id="xr-scene" bind:ready="handleReady" bind:ar-ready="handleARReady" bind:tick="handleTick">
<xr-node>
<xr-ar-tracker wx:if="{{markerImg != ''}}" mode="Marker" src="{{markerImg}}" id="arTracker"></xr-ar-tracker>
<xr-camera id="camera" node-id="camera" position="0.8 2.2 -5" clear-color="0.925 0.925 0.925 1" background="ar" is-ar-camera></xr-camera>
</xr-node>
<xr-shadow id="shadow-root"></xr-shadow>
<xr-node node-id="lights">
<xr-light type="ambient" color="1 1 1" intensity="2" />
<xr-light type="directional" rotation="180 0 0" color="1 1 1" intensity="1" />
</xr-node>
</xr-scene>
```
> **提示**
markerImg 为识别图片地址，云识别识别到目标时会返回。
### 业务处理
文件 `components\\easyar-ar\\easyar-ar.js` 主要代码说明。
```
handleTick() {
// 截图并发送到云识别服务
this.capture().then(base64 => this.crsClient.searchByBase64(base64.split('base64,').pop())).then(res => {
// 云识别返回的结果
console.info(res)
// 返回为 0 表示未识别到目标
if (res.statusCode != 0) {
return;
}
const target = res.result.target;
// 设置marker
this.loadTrackingImage(target.trackingImage.replace(/[\\r\\n]/g, ''));
// 从meta信息中检测是模型，还是视频
try {
const setting = JSON.parse(atob(target.meta));
if (setting.modelUrl) {
this.loadModel(target.targetId, setting);
} else if (setting.videoUrl) {
this.loadVideo(target.targetId, setting);
}
} catch (e) {
console.error(e);
}
}).catch(err => {
console.info(err)
});
},
capture() {
// 获取摄像头图片
const opt = { type: 'jpg', quality: this.properties.config.jpegQuality };
if (this.scene.share.captureToDataURLAsync) {
return this.scene.share.captureToDataURLAsync(opt);
}
return Promise.resolve(this.scene.share.captureToDataURL(opt));
},
```
> **提示**
完整代码请查看示例源文件。
### 云识别处理
文件 `components/libs/crs-client.js` 主要方法说明。
发送图片 base64 数据到云识别服务 API。
```
searchByBase64(img) {
const params = {
image: img,
notracking: 'false',
appId: this.config.crsAppId,
};
return this.queryToken().then(token => {
return new Promise((resolve, reject) => {
wx.request({
url: `${this.config.clientEndUrl}/search`,
method: 'POST',
data: params,
header: {
'Authorization': token,
'content-type': 'application/json'
},
success: res => resolve(res.data),
fail: err => reject(err),
});
});
});
}
```
## 预期效果
* 示例首页
![预期效果](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-xr-frame.jpg)
* 渲染模型效果
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [云识别开快速入门](quickstart.html)
* [云识别开者指南](guide.html)
* [微信小程序开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)
