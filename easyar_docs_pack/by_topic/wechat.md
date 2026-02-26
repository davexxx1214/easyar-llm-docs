# EasyAR 专题包：wechat

适用于上下文长度有限时的分卷输入。

## 目录
- `wechat/cloud-recognition/guide.md`
- `wechat/cloud-recognition/quickstart.md`
- `wechat/cloud-recognition/sample.md`
- `wechat/diagnostics/report.md`
- `wechat/getting-started/quickstart.md`
- `wechat/mega/content-annotation-creation.md`
- `wechat/mega/content-load.md`
- `wechat/mega/content-realworld-alignment.md`
- `wechat/mega/content-simple.md`
- `wechat/mega/content-simulation.md`
- `wechat/mega/content-unity-setup.md`
- `wechat/mega/fullstart.md`
- `wechat/mega/integration.md`
- `wechat/mega/known-issues.md`
- `wechat/mega/occlusion.md`
- `wechat/mega/quickstart.md`
- `wechat/mega/release-notes.md`
- `wechat/mega/sample.md`
- `wechat/mega/session-device-orientation.md`
- `wechat/mega/session-dump.md`
- `wechat/mega/session-gnss-simulation.md`
- `wechat/mega/session-plane-detection-error.md`
- `wechat/mega/session-state.md`
- `wechat/mega/session.md`
- `wechat/mega/tracker-access.md`
- `wechat/mega/tracker-external-sensor.md`
- `wechat/mega/tracker-landmark.md`
- `wechat/mega/tracker.md`
- `wechat/mega/transparent-video.md`

---

## 图像云识别微信小程序开发者指南
- 章节路径: `wechat/cloud-recognition/guide.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/guide.html

# 图像云识别微信小程序开发者指南
本章主要介绍 EasyAR 云识别和微信小程序结合的常用功能以及实现方法。
## 功能和使用
微信小程序 XR-FRAME 是微信官方推出的 XR/3D 应用开发解决方案，采用混合渲染技术实现接近原生的性能表现，兼具视觉效果与开发便捷性，可快速构建 AR 应用。该框架支持图像跟踪、3D 模型加载、动画控制、视频播放及粒子特效等核心功能，开发模式以 WXML 模板化编程为主，仅需少量逻辑代码即可实现高质量视觉效果。
EasyAR 云识别（CRS）服务专注于海量图像库的以图搜图场景，通过云端算法实现高效目标识别，具有高性价比和低接入门槛的特点，开发者可快速集成并完成功能开发。
### 数据流
```
flowchart TB
B[API 或者 EasyAR Web] --> A[云识别 CRS] <--> D[设备端 微信小程序]
C[虚拟内容] <--> D[设备端 微信小程序]
```
XR-FRAME 和云识别两者结合以后，本地设备将不再受目标图数量的限制，可以解决应用对超大范围的需求。
### 实现流程
1. 云识别服务调用‌
* 通过 EasyAR 云识别（CRS）API 发起图像识别请求
* 处理识别结果（识别成功/失败，处理 Meta 等）
* 跟踪图配置‌
* 根据识别结果中的 trackingImage，动态设置 xr-ar-tracker
‌
* 虚拟资源加载‌
* 解析 Meta 数据中的资源标识符
* 使用 xr-asset 下载 3D 模型或视频等虚拟资产
* 将虚拟资产加入到场景中，并配置资源属性（如缩放比例、初始位置等）
‌
* AR 内容呈现‌
* 将虚拟资产与识别标记进行空间绑定
* 实现虚实融合的渲染效果
* 处理用户交互事件（如点击、拖拽等）
## 常用功能
云识别获取结果以后，微信小程序中常用的 AR 功能包括以下几种：
* 仅识别并展示识别结果
* 仅识别并展示识别目标关联的视频、动画、模型、脚本
* 识别 + 跟踪叠加视频、动画、模型、脚本
## 相关主题
* [微信小程序开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)

---

## 图像云识别微信小程序开发快速入门
- 章节路径: `wechat/cloud-recognition/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/quickstart.html

# 图像云识别微信小程序开发快速入门
本篇将带大家快速开发微信小程序上基于 EasyAR 图像云识别的 AR 应用，通过本文介绍，开发者可以掌握如何在微信小程序环境中集成 EasyAR 的云识别能力，并利用 XR-FRAME 框架构建交互式 AR 体验。
## 开发准备
1. [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。
2. 获取 “AppID(小程序ID)”，如果没有，请注册[微信公众平台账号](https://mp.weixin.qq.com/)或[申请测试账号](https://developers.weixin.qq.com/miniprogram/dev/devtools/sandbox.html)。
3. 微信开发者工具[下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。
4. 支持云识别的 [API Key](../../apikey-auth.html)。
5. 运行中的[云识别库](../../cloud-recognition/management.html)。
## 上传云识别图片
准备一张识别图片，并上传到云识别库，上传方法参考 [图库管理](../../cloud-recognition/management-adding.html)。
## 下载 Sample
在 [EasyAR 下载页面](https://www.easyar.cn/view/download.html)下载 “EasyAR CRS 微信小程序Sample”。
![crs-wx](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-dl-1.jpg)
## 配置 sample
* 将下载的 “EasyAR-miniprogram-WebAR-Demo-tracking.zip”，解压到你的目录。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-21.png)
* 导入微信开发者工具。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-22.jpg)
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-23.jpg)
* 在“详情”下的“本地设置”中勾选“不检验合法域名、web-view（业务域名）、TLS版本以及HTTPS证书”。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-24.jpg)
* “微信开发者工具”中的预览效果。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-25.jpg)
* sample 代码中已预留配置项，请根据实际环境进行配置。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-26.jpg)
## 效果预览
* 在“微信开发者工具”上点击“预览”。
* 选择“启动手机端自动预览”。
* 点击“编译并预览”
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-27.jpg)
> **提示**
不要使用“真机调试”。
* 在手机上的运行效果。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-1.jpg)
* 如果你未将域名添加到合法请求列表中，请开启“开发调试”。打开方法如下：
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-2.jpg)
* 如果是首次运行，点击“允许”授权摄像头访问权限。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-3.jpg)
* 点击预览页面中的“云识别功能”。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-5.jpg)
* 将手机摄像头对准您上传的识别图片，点击“点击识别”，如果识别到目标，则会弹出识别目标的名称。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-4.jpg)
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)

---

## 图像云识别微信小程序示例说明
- 章节路径: `wechat/cloud-recognition/sample.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/sample.html

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

---

## 微信小程序问题报告
- 章节路径: `wechat/diagnostics/report.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/diagnostics/report.html

# 微信小程序问题报告
为了能够快速、准确地定位您在开发或使用使用 EasyAR 提供的能力（Mega 或 CRS）的微信小程序时遇到的问题，在提交反馈前参考本指南提供必要的信息和数据以显著减少排查问题的往返沟通时间。
## 问题预检
在报告问题前，可以先尝试通过一些基本手段或阅读文档快速解决问题。
**使用 Mega 插件：**
* 确认使用 2.x 版本的小程序插件（1.x 版本的 Mega 小程序插件已不再维护）
* 阅读 [Mega 插件已知问题和限制](../mega/known-issues.html)确认是否为已知问题。
* 参考修改为 [Mega Sample](../mega/sample.html) 或 [CRS Sample](../cloud-recognition/sample.html) 中的实现方式，确认问题依然存在。
## 反馈问题时需要的数据
一份完整的问题报告通常需要包含以下数据，使 EasyAR 开发团队能够进行准确的分析。
### 运行环境数据
* **设备型号**：可以尝试通过 `wx.getDeviceInfo().model` 获取。
* **微信客户端平台**：通过 `wx.getDeviceInfo().system` 获取。
* **微信版本号**: 通过 `wx.getAppBaseInfo().version` 获取。
* **微信小程序客户端基础库版本**：通过 `wx.getAppBaseInfo().SDKVersion` 获取。
* **（若使用 Mega 插件）使用的 Mega 插件版本**：可以通过工程 `app.json` 文件中的 `plugins` 字段中的 `version` 获取。
### [Mega] AR Session dump 文件（至关重要）
能够复现问题的 AR Session dump 文件是分析微信小程序上定位、跟踪问题最重要的数据。
参考 [如何使用你的小程序录制 AR Session dump 文件](../../../mega/data-collection/wechat/wechat-dump.html)实现 dump 文件的记录与转发。
此外若定位问题可以稳定复现，您也可以通过 Mega toolbox 来录制这段数据并转发，参考[使用微信小程序 Mega Toolbox 记录与转发 session dump 数据](../../../mega/data-collection/wechat/toolbox-dump.html)。
### 屏幕录制（建议）
若使用 Mega 插件，请务必在录制屏幕的同时进行 AR Session dump。这能让我们将视频中的视觉现象与底层算法数据对齐。
### 运行日志
若在 vConsole 中出现了报错，您需要提交详细的错误信息，详细方法参考 [微信小程序上的日志分析](../../diagnostics/log-wechat.html)
> **重要事项**
如果使用 Mega 时遇到定位或跟踪相关的问题而不是程序异常，请务必提供当时的 **session dump 文件和录屏文件**。纯日志文件仅能提供侧面参考，dump 数据与录屏才是排查问题的**核心依据**。

---

## 在微信小程序中使用 AR
- 章节路径: `wechat/getting-started/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/getting-started/quickstart.html

# 在微信小程序中使用 AR
在微信小程序中开发 AR 应用，依赖微信提供的 VisionKit 和 xr-frame 组件。开发者可以实现图像跟踪、运动跟踪等功能。通过 EasyAR，在微信小程序上还支持 Mega 和图像云识别（CRS）功能。
为了实现小程序上的 AR 体验，需要多个组件共同工作：
* XR-Frame 负责小程序上相机控制和 3D 虚拟内容的渲染和叠加。
* VisionKit 负责提供图像跟踪、设备本地运动跟踪等。
* EasyAR CRS 提供图像云识别相对于已知平面目标的位置和姿态。
* Mega 提供设备相对于已知空间环境的六自由度位置和姿态。
## 后续步骤
为方便您快速开发微信小程序的应用，请参阅相关入门指南和示例代码。
* [图像云识别快速入门](../cloud-recognition/quickstart.html)
* [Mega 快速入门](../mega/quickstart.html)

---

## 使用 Unity 编辑器创建并上传标注
- 章节路径: `wechat/mega/content-annotation-creation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-annotation-creation.html

# 使用 Unity 编辑器创建并上传标注
这篇文章介绍了如何使用 Unity 编辑器上的 Mega Studio 创建并上传标注。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)
* 准备模型： 使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[XRFame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)，准备符合 xr-frame 要求的模型文件。
* 将模型的文件导入 Unity 。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
## 为什么需要标注
EasyAR Mega Annotation（EMA） 可用于同步跨平台的（坐标系定义不同）空间位置。
![Unity](https://doc-asset.easyar.com/develop/wechat/mega/media/content-transform-sync01.png)
Unity 环境下标注的本地坐标系： X 正方向朝后，Y 正方向朝上，Z 正方向朝右。
![xr-frame](https://doc-asset.easyar.com/develop/wechat/mega/media/content-transform-sync02.png)
xr-frame 环境下标注的本地坐标系： X 正方向朝后，Y 正方向朝上，Z 正方向朝左。
上述方向差异源于 Unity 与 xr-frame 采用的坐标系定义（左手/右手系）不同。
使用 EMA 同步空间位置有以下显著优势：
1. 简化开发流程： 自动处理跨平台坐标转换，规避了手动计算导致的繁琐逻辑及易错性。
2. 提升调试效率： 能够直接在 [MegaToolbox](../../../mega/reference/toolbox-wechat/intro.html) 上加载，便于快速进行真机测试与数据验证。
## 操作步骤
1. **创建标注工具**
在 Unity 的 **Hierarchy** 面板中点击右键，依次选择： **EasyAR Mega** > **Tool** > **Annotation Tool（Edit Mode）**。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation01.png)
创建完成后，场景中生成 EasyAR.Mega.Annotation 和 MegaBlocks 两个节点。
选中 EasyAR.Mega.Annotation 节点，在其 **Inspector** 面板中会出现用户名/邮箱及密码输入框。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation02.png)
2. **登录账号**
输入 EasyAR 账号，密码后点击登录，若成功 **Inspector** 面板中会出现 Studio 工具。
3. **选择 Mega 云定位库**
点击 Mega Cloud Service 右侧的图标。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation04.png)
选择要使用的库。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation05.png)
加载定位库及 Mega Blocks 信息成功后， Studio 工具面板如图所示。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation06.png)
4. **加载Block稠密模型**
点击 Block 名称右侧的 加载 即可动态加载该 Block 的稠密模型。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation07.png)
模型加载完成后出现在 Scene 标签页面中，注意当左下角出现图中标识时当前视野内的模型尚未加载完成，稍等一会儿待该标识消失表示加载已经完成。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation08.png)
5. **创建标注**
在场景中按住 Ctrl （Windows） / Command （Mac） 键，然后在需要标注的地方点击鼠标左键即可。
6. **使用模型**
将导入的模型拖到场景节点，作为标注的子节点。
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0** ， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
7. **[可选] 精确调整模型位置**
如果需要精确调整模型位置和朝向，可以参考[如何使用 Unity 编辑器使 3D 内容与实景精确对齐](content-realworld-alignment.html#wechat-mega-content-realworld-alignment-precise-adjustment)。
8. **新建标注数据包**
点击 **Inspector** 面板中的标注数据包右侧的图标。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation16.png)
在框中填入标注数据的名称，并点击右侧的勾。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation17.png)
创建成功后应如图所示，之后点击下方的确定。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation18.png)
点击上传图标进行上传。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation19.png)
上传成功后弹出提示。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation20.png)
9. **记录标注 ID**
您需要记录标注数据的名称或 ID 以在 xr-frame 上加载对应的标注数据。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation21.png)
在上传成功后，您在云定位库中也可以看到相应的信息。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation22.png)
此处也可以查看上传的标注数据名称和 ID。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 后续步骤
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* 尝试[在 Unity 编辑器上模拟运行](content-simulation.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)

---

## 如何在 xr-frame 运行时加载 AR 场景下的 3D 内容
- 章节路径: `wechat/mega/content-load.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-load.html

# 如何在 xr-frame 运行时加载 AR 场景下的 3D 内容
本文详细阐述了 xr-frame 资源加载与节点挂载的分离机制，通过脚本动态实现 3D 内容在 Block 节点下的灵活挂载，实现 AR。
## 官方资料
* [xr-frame 开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)：微信官方 XR 引擎文档。
* [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)：包含各类基础与进阶用法示例。
官方资料中已经有充分的内容说明如何在运行时加载 3D 内容，本文中仅简要说明一些 AR 场景下常用的内容和加载方式。
## 资源加载 vs 节点挂载
在 xr-frame 中，显示一个 3D 模型分为两个阶段：
1. 资源加载：指将模型文件（如 `.glb` ）从网络或本地下载并解析到内存中。此时模型已就绪，但在场景中不可见。
2. 节点挂载：指在场景树中创建一个节点，并将已加载的资源关联到该节点上。此时模型才会正式出现在渲染画布中。
## 如何使用代码动态加载 3D 内容
1. 资源加载
通过 xr-frame 场景的资源管理系统调用 [loadAsset](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetsSystem.html#loadAsset)手动加载资源。
参数中的 `type` 指资源类型，`assetId` 指加载后的资源 id，`src` 指资源的 url，一般是资源托管服务器的地址。
需要记录 `assetId` 用于后续的挂载和释放资源。
```
try {
await scene.assets.loadAsset({type: 'gltf', assetId: 'panda', src: 'url/EasyARPanda.glb'});
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
```
2. 节点挂载
使用 `element.addChild()` 将加载好的模型放在 ShadowRoot 下。
```
const root = scene.getElementById("shadow-root");
let panda = scene.createElement(xrFrameSystem.XRGLTF,
{
"model": "panda",
"anim-autoplay": ""
}
);
root.addChild(panda);
```
ShadowRoot 元素是 xr-frame 专门用来防止动态创建和移除节点的根节点，详见 [Shadow节点](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/shadow.html)。
使用插件对象提供的 [createXRNodeFromNodeAnnotation](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_createXRNodeFromNodeAnnotation_member) 方法能够根据 EMA 数据创建 Block 的子节点，确保 3D 内容显示在正确的空间位置。
```
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
let panda = scene.createElement(xrFrameSystem.XRGLTF,
{
"model": "panda",
"anim-autoplay": ""
}
);
xrNode.addChild(panda);
```
## 如何在 Block 下不使用标注直接挂载内容
> **警告**
使用此方法的前提是，您已验证该 LocalTransform 的数值在 xr-frame 坐标系下能够实现预期的渲染效果。
除此以外的情况请[使用 Unity 编辑器的标注功能](content-annotation-creation.html)实现。
通过 [getBlockById(id)](../../../api/wechat/easyar.BlockHolder.html#w_easyar_BlockHolder_getBlockById_member_1_) 获取场景树上的 block 节点对象，如果不存在相应的 block 节点说明对这个 Block 的定位还未成功过（在第一次定位到该 Block 时节点会被自动创建）。可以用 [holdBlock(blockInfo, blockTransformInput)](../../../api/wechat/easyar.BlockHolder.html#w_easyar_BlockHolder_holdBlock_member_1_) 创建一个该 Block 的节点，也可以在定位回调中判断对该 Block 的定位成功再挂载内容。
> **提示**
在 Unity 编辑器的场景树中选择 **Block 节点** 记录它 **Inspector** 面板上显示的 **ID**
![Unity编辑器中的BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/content-load01.png)
也可以在云定位库页面中查到 **Block ID**
![定位库中的BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/content-load02.png)
```
const blockID = "aaaa1234-bbbb-cccc-dddd-eeeeee123456"
if (!blockHolder.getBlockById(blockParent.id)) {
// 没有存在的 Block 节点，创建一个
blockHolder.holdBlock({
id: blockID
})
}
let blockElement = blockHolder.getBlockById(blockParent.id).el;
```
将模型节点以挂载到指定的 Block 下，分别用 `position.setArray()`，`quaternion.set()` 和 `scale.setArray()` 把修改模型节点的 **LocalTransform** 。
```
export interface LocalTransform {
/\*\* @description 位置 \*/
position: xrfs.Vector3;
/\*\* @description 旋转 \*/
rotation: xrfs.Quaternion;
/\*\* @description Scale \*/
scale: xrfs.Vector3;
}
// 假设有一个已知的在 Block 下的 LocalTransform
const targetTransform: LocalTransform;
blockElement.addChild(modelNode);
let modelTransform = modelNode.getComponent(xrFrameSystem.Transform);
modelTransform.position.setArray([
targetTransform.position.x,
targetTransform.position.y,
targetTransform.position.z
]);
let annoRotation = new xrFrameSystem.Quaternion().setValue(
targetTransform.rotation.x,
targetTransform.rotation.y,
targetTransform.rotation.z,
targetTransform.rotation.w
);
modelTransform.quaternion.set(annoRotation);
modelTransform.scale.setArray([
targetTransform.scale.x,
targetTransform.scale.y,
targetTransform.scale.z
]);
```
## xr-frame 支持的资源类型
* Texture 纹理和图像
* CubeTexture 立方体纹理
* VideoTexture 视频纹理
* EnvData 环境
* GLTF 模型
* Keyframe 帧动画
* Atlas 图集
每种资源的加载方法详细见[微信官方文档](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render)及 [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)
> **注意**
支持的 GLTF 格式及拓展参考 [xr-frame 官方 GLTF 使用说明](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)

---

## 如何使用 Unity 上的 Mega Studio 创建与实景精确对齐的 3D 内容
- 章节路径: `wechat/mega/content-realworld-alignment.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-realworld-alignment.html

# 如何使用 Unity 上的 Mega Studio 创建与实景精确对齐的 3D 内容
尽管 xr-frame 没有提供 3D 编辑器功能，您还是可以借助 Mega Studio 将虚拟物体准确地摆放在现实空间的某个位置，在 AR 体验中与现实空间精确对齐。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* 准备模型： 使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[XRFame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)，准备符合 xr-frame 要求的模型文件。
* 将模型的文件导入 Unity 。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
## 将 3D 内容作为标注的子节点
将导入的模型拖到场景节点，作为标注的子节点。
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0**， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![修改模型Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
## 精确调整模型位置
选择 **标注节点** 在场景中对着稠密模型调整模型的位置和旋转。
> **注意**
模型相对于标注的 Position 和 Rotation 必须始终全部为 **0** ，否则您无法在 xr-frame 上得到正确的渲染结果。
## [可选] 根据全景图精确调整模型位置
点击 **Inspector** 面板中的全景标记右侧的加载按钮，场景中出现全景标记。
![加载全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation13.png)
![显示全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation14.png)
点击任意一个全景标记，就可以在其位置进行全景下的摆放，您可以切换全景的位置以确认模型在不同视角下的位置都是准确的。
![全景编辑](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation15.png)
## 如果加载的 Block 模型不水平怎么办
在 **Hierarchy** 面板中选择 **Block Root** ，在 **Inspector** 面板中修改 **Rotation** 直到稠密模型的朝向在 Unity 编辑器中看起来正确。
> **重要事项**
Block Root 是在 3D 引擎场景节点树上所有 Block 节点的父节点。
Block Root 在世界坐标系下的 Transform **不会**影响 Block 的**本地坐标系**，也因此**不会影响标注和标注下模型的渲染结果**。它的 Transform 和最终的显示效果**无关**。
## 如果加载的 Block 模型有破碎，缺损的部分怎么办
在三维重建过程中，若受采集视角覆盖不全的影响，生成的密模型中可能会出现破碎或缺损的部分。
![破碎缺损](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment02.png)
面对不完整的模型，若破碎/缺损部分的 3D 内容对齐精度要并不高，可以通过点击**全景标记**对照**全景图**的方式来摆放 3D 内容。之后可以通过点击附近不同的**全景标记**位置来验证效果。
![通过全景图摆放](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment03.png)
得到摆放结果。
![摆放结果](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment04.png)
若破碎/缺损部分的 3D 内容对齐精度要求非常高，则需要通过[补充更新](../../../mega/scene-update/incremental.html)或[无损全量更新](../../../mega/scene-update/full.html)进行地图的补充或更新。一般来说这样的区域意味着采图过程中没有覆盖，在这样的区域内部 Mega 定位效果会受到影响，仅在编辑器中对齐 3D 内容是不够的。
## 后续步骤
* 尝试[在 Unity 编辑器中模拟运行](content-simulation.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
**微信小程序 Mega 插件**：
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
**Mega Studio**：
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)

---

## 如何使用 Unity 上的 Mega Studio 摆放 3D 内容
- 章节路径: `wechat/mega/content-simple.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-simple.html

# 如何使用 Unity 上的 Mega Studio 摆放 3D 内容
这篇文档将带您快速学习如何在 Unity 编辑器上使用标注工具进行模型摆放，为后续在 xr-frame 上的渲染做准备。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)
## 准备 GLTF 模型并拖入 Unity Assets
可以使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[xr-frame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)准备自己的模型并上传到资源托管服务器。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
![模型拖入 Unity Assets](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple01.png)
## 选择Mega云定位库
点击 **Mega Cloud Service** 右侧的图标。
![Studio工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation04.png)
选择要使用的库。
![选择库](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation05.png)
加载定位库及 Mega Blocks 信息成功后， Studio 工具面板如图所示。
![加载后的Studio工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation06.png)
## 加载Block稠密模型
点击 Block 名称右侧的 加载 即可动态加载该 Block 的稠密模型。
![点击Block加载](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation07.png)
## 创建标注
在场景中按住 Ctrl （Windows） / Command （Mac） 键，然后在需要标注的地面上点击鼠标左键即可。
![创建标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple06.png)
## 将 3D 内容作为标注的子节点
将导入的模型拖到场景节点，作为标注的子节点。
![拖入模型](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple07.png)
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0**， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![修改模型Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
## [可选]调整模型位置
选择 **标注节点** 在场景中对着稠密模型调整模型的位置和旋转。
> **注意**
模型相对于标注的 Position 和 Rotation 必须始终全部为 **0** ，否则您无法在 xr-frame 上得到正确的渲染结果。
![修改标注节点Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple09.png)
## 新建标注数据包
点击 **Inspector** 面板中的标注数据包右侧的图标。
![添加标注数据](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation16.png)
在框中填入标注数据的名称，并点击右侧的勾。
![填入标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation17.png)
创建成功后应如图所示，之后点击下方的确定。
![确定创建标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation18.png)
点击上传图标进行上传。
![上传标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple13.png)
上传成功后弹出提示。
![成功提示](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation20.png)
## 确认标注数据
您需要记录标注数据的 **ID** 以在 xr-frame 上加载对应的标注数据。
![标注数据面板](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation21.png)
在上传成功后，您在云定位库中也可以看到相应的信息，这个页面中列表里的 ID 是 **标注数据包 ID**。
![云定位库中的标注信息](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple16.png)
此处也可以查看上传的标注数据名称和 ID，这个页面中列表里的 ID 是 **标注点 ID**。
![云定位库中的标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 后续步骤
* 使用上传的标注[完整运行示例工程](fullstart.html)
* 尝试[使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
## 相关主题
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)

---

## 在 Unity 编辑器中模拟运行
- 章节路径: `wechat/mega/content-simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-simulation.html

# 在 Unity 编辑器中模拟运行
这篇文档将指引您通过 Unity 编辑器模拟真实场景定位，帮助您在小程序上线前完成虚拟内容的静态对齐检查。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* [确认定位库已经可以使用](../../mega/localization-verify.html)。
* 使用 Mega Toolbox 工具[采集模拟运行数据](../../mega/input-recording.html)。
* [使用标注工具创建标注](content-annotation-creation.html)。
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)，比如：
![摆放完成的场景](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation08.png)
> **重要事项**
使用现场录制的 EIF 数据可以直观地验证虚拟内容的位置摆放是否准确。
但由于 xr-frame 和 Unity 平台环境不同，代码脚本逻辑和渲染结果无法在模拟运行中得到验证。
## 模拟运行
1. 创建一个 **Sense 许可证**
由于在 Unity 上模拟运行需要用到 EasyAR Sense ，需要准备一个 Sense 的许可证（它可以是试用的）。
在 EasyAR 开发中心中选择 [**Sense 授权管理**] > [**创建一个新的 Sense 许可证密钥**]：
![Sense许可证](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation01.png)
* 选择 EasyAR Sense 个人版。
* 在‘是否使用稀疏空间’选项中选择‘否’。
* 填写任意的应用名称，iOS Bundle ID 及 Android Package Name。
* 点击确定，此后在开发中心的 Sense 授权管理中会出现申请的许可证。
![Sense许可证信息](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation02.png)
* 在 EasyAR 开发中心中选择准备工作中申请的 Sense 许可证。
![Sense许可证列表](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation03.png)
点击复制：
![Sense许可证复制](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation04.png)
* 点击 Unity 编辑器上方菜单栏中的 **[EasyAR]** > **[Mega]** > **[Configuration]** 进入配置页面：
![Configuration](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation05.png)
* 点击左侧 **Sense** 进行配置，填入 **Sense 许可证**。
![Sense许可证填入](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation06.png)
* 启用验证工具，点击**运行**。
![摆放完成的场景](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation09.png)
在弹出窗口中点击 **OK**。
![弹出窗口](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation10.png)
* 点击**加载按钮**，加载 EIF 文件。
![加载按钮](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation11.png)
选择准备工作中保存的 EIF 文件（后缀名为 `.eif` 或 `.mkveif`）。
![选择EIF](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation12.png)
* **隐藏 Block Mesh**。
* 可以将 Block Mesh 全部设置为**隐藏**。
![隐藏Block Mesh](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation13.png)
* 可以在验证工具中将 **Block Mesh Alpha** 设置为 0，即透明。
![更改Alpha](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation14.png)
将控制条拖至最左侧。
* **播放 EIF**
> **重要事项**
在 Unity 编辑器上播放 EIF 时使用的 SDK 以及输入帧数据与 xr-frame 小程序使用的均不同，因此这种方式：
✅ 可以用于直观地验证虚拟内容的位置摆放是否准确，验证云定位服务在该位置的定位准确度。
❌ 不能用于验证 xr-frame 小程序实机运行的最终效果。
工作原理与预期： 在 Unity 播放 EIF 数据时，EasyAR SDK 会调用录制的输入帧数据，向配置的定位服务发起**真实**的云端请求。
* **若定位成功且表现稳定**： 模型位置准确且无漂移，则可预期该场景在 xr-frame 小程序上也能达到较理想的效果。
* **若定位失败或表现异常**： 模型出现频繁跳动、偏移或无法定位，通常意味着 xr-frame 小程序实机运行时也会面临相似的问题。
## 相关主题
* [使用Session验证工具播放EIF文件](../../unity/simulation/tool.html)

---

## 如何安装 Unity 并使用 Mega Studio
- 章节路径: `wechat/mega/content-unity-setup.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-unity-setup.html

# 如何安装 Unity 并使用 Mega Studio
这篇文章将介绍如何安装 Unity 以及如何下载并加载 Mega Unity 插件以在 Unity 编辑器上使用 Mega Studio。
## 安装 2021.3 或更高版本的 Unity 长期支持版本（LTS）
从 [Unity 官方网站](https://unity.com/download)，在中国大陆可以从[Unity 中文页面](https://unity.cn/releases)获取安装包，遵循官方指引进行安装。
您可以先下载 Unity Hub，之后在网页上选择 Unity 版本并从 Hub 下载或在 Unity Hub 中选择并安装。
![网页上安装Unity](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup01.png)
## 新建 Unity 项目
使用 **Built-in Render Pipeline**
![创建项目](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup05.png)
![下载模板](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup06.png)
在一些版本上，比如 Unity 6 ，您需要先下载对应的模板再创建项目
## 下载 Mega Unity 插件
![下载页面导航](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup07.png)
登录 EasyAR 账号，进入下载页面。
![下载Mega插件](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup08.png)
下载 **EasyAR Sense Unity Plugin(for Mega)**。
![解压文件](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup09.png)
解压下载的 `.zip` 压缩包后，您将获得以下目录结构：
> **重要事项**
注意：请勿解压 `.tgz` 文件。 这些是 Unity 软件包，需通过 Unity Package Manager 直接导入。
```
.
└── EasyARSenseUnityPluginForMega\_\*\*.zip # 完整安装包
├── com.easyar.mega-\*\*.tgz # 包含标注工具及 Block 浏览工具
├── com.easyar.sense-\*\*.tgz # 包含 EasyAR Sense 核心库及 Unity 插件
├── readme.cn.txt # 中文自述文件
└── readme.en.txt # 英文自述文件
```
版本号说明： 文件名中的 \*\* 代表版本号，格式为：**Major.Minor.Patch + BuildNum.BuildHash** 。请以官方发布的最新版本为准。
## 在项目中导入 package （UPM 包）
请依次导入：
```
com.easyar.sense-\*\*.tgz
com.easyar.mega-\*\*.tgz
```
> **注意**
在导入之前，建议将 `.tgz` 文件先拷贝到您的 Unity 项目文件夹内（例如存放在 Packages 目录下）。
导入后请勿移动或删除这些 `.tgz` 源文件，否则 Unity 将无法加载对应的包。
点击 **Window** > **Package Management** > **Package Manager** ，在弹出的窗口左上角点击 **+** 号，选择 **Install package from tarball...**
![Install package](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup10.png)
## 创建标注工具
在 **Hierarchy** 面板中空白处右键 **EasyAR Mega** > **Tool** > **Annotation Tool（Edit Mode）** 创建标注工具
![创建标注工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup11.png)
## 登录后使用 Mega Studio
在 **Hierarchy** 面板中点击 `EasyAR.Mega.Annotation`，在 **Inspector** 面板中输入 EasyAR 账号，密码后点击登录。
![登录 Mega Studio](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup12.png)
登陆成功后即可使用 Mega Studio 的编辑器功能。
![登录 Mega Studio 成功](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup13.png)
## 后续步骤
* [使用 Unity 编辑器摆放 3D 内容](content-simple.html)
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [在Unity 编辑器中模拟运行](content-simulation.html)

---

## 完整运行微信小程序 Mega 插件示例工程
- 章节路径: `wechat/mega/fullstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/fullstart.html

# 完整运行微信小程序 Mega 插件示例工程
这篇文章将介绍如何完整运行微信小程序 Mega 插件的示例项目（包含标注的使用）。
## 开始之前
* 完成[快速运行示例工程](quickstart.html)。
* 完成[使用 Unity 上的 Mega Studio 摆放 3D 内容](content-simple.html)，获取**标注数据包 ID 和标注点 ID**。
**[Block 云定位]** > **[标注数据]** 在云定位库列表里的 ID 是 **标注数据包 ID**。
![云定位库中的标注信息](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple16.png)
点击右侧 **[查看]** 可以查看上传的标注数据名称和 ID，这个页面中列表里的 ID 是 **标注点 ID**。
![云定位库中的标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 配置 Mega 标注数据包 ID
在 `miniprogram/components/sample-data/easyar-settings.ts` 中填入标注数据包 ID：
```
/\*\* 填 Mega 标注数据包 ID \*/
export const MegaAnnotationId: string = "";
```
## 配置标注点要展示的模型
在 `miniprogram/components/sample-data/annotation-metadata.ts` 中通过将 `key` 改成标注点 id 配置要替换的标注，如果要替换多个则用逗号隔开。
```
export const AnnotationMetaData: Record<string, any> = {
/\*\* 填标注点 ID \*/
"aaaaaaaa-bbbb-cccc-dddd-123456789012": {
assetId: "panda",
scale: "1 1 1"
},
"aaaaaaaa-bbbb-cccc-dddd-123456789013": {
assetId: "panda",
scale: "1 1 1"
}
};
```
>
> 关于如何记录和对应标注点 ID 可以参考
[> 确认标注数据
](content-simple.html#wechat-mega-content-simple-save-annotation-id)> 。
>
## 实机运行
1. 点击小程序开发工具上方栏的实机预览按钮，通过扫描二维码加载。
> **注意**
不能在开发工具上直接模拟运行带有 AR 功能的 xr-frame 组件。
![二维码加载](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart06.png)
2. 点击 **EasyAR Mega Samples** 进入示例项目的 AR 场景。
![Sample入口](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart08.png)
3. 屏幕中提示 `EasyAR Session is initializing` 表示微信平面检测正在初始化。
> **提示**
确保在光线充足的环境下测试，避开大面积纯色墙面或纯色地板。
对着地面或其他平面匀速左右摆动以加快这个过程。
![初始化](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart09.png)
4. 初始化完成后，将手机竖直使相机拍到正常的现实画面，当定位成功， debug 信息中出现 `Found` 字样，并且右下方的状态指示物变为绿色。
![定位](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart10.png)
5. 将在标注的位置加载并渲染 GLTF 模型或方块（取决于是否配置了 `assetId`）。
运行效果：
## 相关主题
* [Mega 简介](../../mega/intro.html)
* [获取和使用 APIKey](../../apikey-auth.html)
* [开始开发之前](../../mega/localization-verify.html)
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [示例说明](sample.html)

---

## 将 Mega 插件接入您的微信小程序
- 章节路径: `wechat/mega/integration.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/integration.html

# 将 Mega 插件接入您的微信小程序
本文档将带您完成 Mega 插件在 xr-frame 小程序环境下的接入。
## 开始之前
* 参考 [xr-frame 开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)及 [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)学习如何使用微信官方提供的 XR-3D 引擎，内容包括：
* 常规微信小程序页面中引入 xr-frame 组件的方式。
* xr-frame 组件与小程序传统组件的通信方式。
* 如何从场景中获取或创建一个元素并修改部分属性比如 `Transform`。
* 加载和释放资源，例如 GLTF 模型。
## 全局配置
在小程序根目录下的 `app.json` 全局配置文件中添加对 Mega 小程序插件的依赖，并将[依赖加载](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/lazyload.html)改为**按需注入**。
```
{
"lazyCodeLoading": "requiredComponents",
"plugins": {
"easyar-wechat-miniprogram": {
"version": "2.0.2", //使用最新的插件版本
"provider": "wx27fa3b52b5462e8f" // Mega 小程序插件固定 id
}
}
}
```
## 加载插件
您可以通过[插件接口](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/using.html#js-接口)引入插件，直接使用插件的部分方法以验证插件是否已经被正确加载。
例如使用通过微信提供的 `requirePlugin(string path)` 接口拿到 [EasyARWechatMiniprogramPlugin](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html) 后，使用它的 [isMegaTrackerSupported](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_isMegaTrackerSupported_member) 方法判断设备是否支持。
```
//如果已经引入了 typings 文件
//const easyarPlugin: easyar.EasyARWechatMiniprogramPlugin = requirePlugin("easyar-wechat-miniprogram") as easyar.EasyARWechatMiniprogramPlugin;
const easyarPlugin = requirePlugin("easyar-wechat-miniprogram") as any;
//调用 isMegaTrackerSupported 判断当前设备是否支持，若不支持则弹窗提示
if (!easyarPlugin.isMegaTrackerSupported()) {
const message = `当前设备不支持 VK v1 和 v2，请参考微信官方文档：https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html`;
wx.showModal({
title: "设备不支持",
content: message,
showCancel: false,
});
console.error(message);
return;
}
```
>
> 这个例子中首先通过微信提供的
`> requirePlugin(string path)
`> 接口拿到了
`> easyarPlugin
`> 即插件暴露的接口对象，之后调用了其提供的
[> isMegaTrackerSupported
](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_isMegaTrackerSupported_member)> 方法判断当前运行环境下是否可用。若不可用则弹窗提示。
>
## 引入类型
建议使用 **Typescript** 进行开发。
样例工程中的路径：`/typings/types/easyar/lib.easyar.d.ts` 。
拷贝到工程相同目录，并在 `/typings/types/index.d.ts` 中以**三斜杠指令**引用：
```
/// <reference path="./easyar/lib.easyar.d.ts" />
```
当需要使用类型对象时，可以通过 [getMegaSystem](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_getMegaSystem_member) 获取 EasyAR Mega 微信小程序插件的类型系统 [IMegaSystem](../../../api/wechat/easyar.IMegaSystem.html)。
```
const mega: easyar.IMegaSystem = easyarPlugin.getMegaSystem();
```
之后可以使用 [IMegaSystem](../../../api/wechat/easyar.IMegaSystem.html) 中暴露的类型进行类型比较，例如可以用 `state` 比较与 `mega.SessionState.Running` 是否相等判断 session 是否初始化成功：
```
const newState: easyar.SessionState = event.detail.value;
if (newState === mega.SessionState.Running) {
console.log("EasyAR Session initialized succeeded. Start running.");
}
```
## xr-frame 场景搭建（WXML）
在页面的 WXML 文件中，`xr-easyar-mega` 组件必须作为 `xr-scene` 的子节点，并正确绑定相机与追踪器的 `id` ，若不填写 `id` 则组件会使用在场景中第一个查找到的 `xr-camera` 和 `xr-ar-tracker` 组件。
```
<xr-scene id="xr-scene" ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
<xr-easyar-mega
id="easyar-mega"
camera-id="xrCamera"
ar-tracker-id="xrARTracker"
></xr-easyar-mega>
<xr-node>
<xr-ar-tracker id="xrARTracker" mode="Plane"></xr-ar-tracker>
<xr-camera id="xrCamera" node-id="xrCamera" clear-color="0.925 0.925 0.925 1" background="ar" is-ar-camera></xr-camera>
</xr-node>
<xr-shadow id="shadow-root" node-id="xrShadow"></xr-shadow>
</xr-scene>
```
> **小心**
`ar-system` 的 `planeMode` 必须设置为 `1`
## 注册 Mega 插件的事件回调
```
<xr-easyar-mega
id="easyar-mega"
camera-id="xrCamera"
ar-tracker-id="xrARTracker"
bind:sessionStateChange="onSessionStateChange"
bind:megaLocalizationResult="onMegaLocalizationResult"
bind:postSessionUpdate="onPostSessionUpdate"
></xr-easyar-mega>
```
在 WXML 中绑定 xr-frame Element 代理分发的事件，xr-frame 的事件分发机制请参考 [xr-frame 事件机制](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/event.html)
插件分发的事件有：
|事件名称|参数类型|说明|
|`SessionStateChange`|[SessionState](../../../api/wechat/easyar.SessionState.html)|Session 状态改变时立即触发。参数为 Session 新的状态，用于处理 Session 初始化开始与成功的回调。|
|`MegaLocalizationResult`|[MegaLocalizationResult](../../../api/wechat/easyar.MegaLocalizationResult.html)|收到 Mega 定位结果的渲染帧完成更新后触发。事件触发时，该渲染帧内所有受 EasyAR 控制的 Transform 变化已经完成。|
|`PostSessionUpdate`|无参数|Session 在该渲染帧完成更新后立即触发。此时该帧内所有受 EasyAR 控制的 Transform 变化已经完成。|
## AR Session
session 的创建，启动及销毁请见 [AR Session 流程控制](session-state.html)
通过 `sessionStateChange` 事件回调确认初始化是否成功。当状态变为 [Running](../../../api/wechat/easyar.SessionState.html#w_easyar_SessionState_Running_member) 时，即可认为 ARSession 已就绪。
在 WXML 中通过 `bind:sessionStateChange="onSessionStateChange"` 将 xr-frame 组件中的 `onSessionStateChange()` 函数注册为 `sessionStateChange` 事件的回调：
```
<xr-easyar-mega
bind:sessionStateChange="onSessionStateChange"
></xr-easyar-mega>
```
在 xr-frame 组件中的回调函数 `onSessionStateChange()` 中将 session 状态与 [SessionState](../../../api/wechat/easyar.SessionState.html) 的各个枚举进行比较可判断 session 当前状态。
```
onSessionStateChange(event) {
const newState: easyar.SessionState = event.detail.value;
console.log(`EasyAR Session state changed to: ${mega.SessionState[newState]}`);
let displayInfoStr: string = "";
if (newState === mega.SessionState.None) {
displayInfoStr = "EasyAR Session is inactive.";
} else if (newState === mega.SessionState.Initializing) {
displayInfoStr = "EasyAR Session is initializing...";
} else if (newState === mega.SessionState.Running) {
displayInfoStr = "EasyAR Session initialized succeeded. Start running.";
}
this.triggerEvent("sessionDisplayInfoEvent", displayInfoStr);
}
```
>
> 上述代码中，初始化完成后控制台应打印 "EasyAR Session initialized succeeded. Start running."
>
## 相关主题
* [完整运行示例工程](fullstart.html)
* [AR Session 流程控制](session-state.html)
* [示例工程说明](sample.html)

---

## 微信小程序 Mega 插件已知问题与限制
- 章节路径: `wechat/mega/known-issues.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/known-issues.html

# 微信小程序 Mega 插件已知问题与限制
这篇文章介绍了 Mega 小程序插件在使用过程中的已知问题和限制。
## 微信已知问题
当前微信 xr-frame 或 VisionKit 已确认的缺陷。发生时将导致 AR 功能失效，请在开发时留意相关触发场景。
### 微信平面检测异常
在特定情况下（如画面中出现大片白墙、相机长时间被遮挡等），微信提供的平面检测可能出现状态异常。在这种状态下，MegaTracker 无法正常工作。
处理方法参考 [平面 AR 追踪器异常处理](session-plane-detection-error.html)。
### Session 初始化时间较长
AR Session 需要等待微信平面检测初始化完成后才能完成初始化。在某些情况下，微信平面检测初始化时间较长。
AR Session 需要等待 xr-frame ARTracker 初始化完成的原因 请见 [MegaTracker 是如何在 xr-frame 上工作的](tracker.html)。
* **状态参考**：[微信小程序 AR 追踪器状态文档](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#获取追踪状态)。
* **监听示例**：
```
<xr-ar-tracker id="xrARTracker" mode="Plane" bind:ar-tracker-state="handleARTrackerState"></xr-ar-tracker>
```
```
handleARTrackerState({detail}) {
if (detail.value.state == xrFrameSystem.EARTrackerState.Detected) {
console.log('Plane is now detected by XR-Frame ARTracker.');
}
}
```
### 节点的 worldPosition 在当前帧不会被立刻更新
这个例子中 `trs.worldPosition` 未被及时更新：
```
public onTick(delta, data) {
const trs = this.el.getComponent(xrFrameSystem.Transform);
// 更新前该节点的 WorldPosition
console.log(`World Position before update: ${trs.worldPosition.x}, ${trs.worldPosition.y}, ${trs.worldPosition.z}`);
// 更新前该节点的 LocalPosition
console.log(`Local Position before update: ${trs.Position.x}, ${trs.Position.y}, ${trs.Position.z}`);
trs.position.x += 0.1;
trs.position.y += 0.1;
trs.position.z += 0.1;
// 该节点的 WorldPosition 未被更新
console.log(`World Position after update: ${trs.worldPosition.x}, ${trs.worldPosition.y}, ${trs.worldPosition.z}`);
// 该节点的 LocalPosition 被更新
console.log(`Local Position after update: ${trs.Position.x}, ${trs.Position.y}, ${trs.Position.z}`);
}
```
在开发中建议一直使用 LocalTransform ， 即 `el.getComponent(xrFrameSystem.Transform).position` 和 `el.getComponent(xrFrameSystem.Transform).rotation`。
### 屏幕方向切换异常
在微信小程序全局配置 `app.json` 中的 `window` 若填入 "auto"。
设备以横屏模式离开小程序后，若以竖屏模式重新进入，会出现 AR 画面异常的情况。
因此任何时候**不要**在 AR 小程序应用中使用 "auto"。
## 使用限制
功能运行的硬性要求。未满足时功能不可用，但可通过调整配置或环境予以避免。
### 机型限制
运行 Mega 小程序插件的设备需要至少支持 **微信 VisionKit V1 平面接口**。为获得理想效果，建议使用支持 **微信 VisionKit V2 平面接口** 的设备。
* **支持机型列表**：参考 [V2 平面 AR 接口支持列表](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)。
* **快速判断方法**：
1. 扫描微信小程序官方 Sample 二维码。
![微信小程序官方 Sample 二维码](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites01.png)
2. 进入小程序后，导航至 **接口** > **VisionKit 视觉能力** > **水平面 AR-v2**，即可快速判断当前设备是否支持。
如果需要在不支持 VisionKit 的设备上使用 Mega 服务，请参考[导航场景最佳实践](../../mega/navigation.html) 使用支持几乎所有设备的**视＋ AR 导航产品**。
### PlaneMode 强制配置
受部分微信接口支持限制，**planeMode** 必须设置为 **1** 。
```
<xr-scene ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
```
### GPS 功能限制
暂不支持通过 GPS 对齐 Block。
暂不支持通过 GPS 摆放标注数据。
## 相关主题
* [MegaTracker的概念与工作流](tracker.html)
* [平面 AR 追踪器异常处理](session-plane-detection-error.html)
* [AR Session 屏幕旋转适配](session-device-orientation.html)

---

## 使用 Mega 插件实现遮挡
- 章节路径: `wechat/mega/occlusion.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/occlusion.html

# 使用 Mega 插件实现遮挡
遮挡 （Occlusion） 是提升 AR 虚实融合沉浸感的关键技术。本文将指导您如何在 xr-frame 环境下，通过 EasyAR 云定位与标注实现遮挡效果。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* 能够[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
* 能够[创建与实景对齐的内容](content-realworld-alignment.html)。
## 遮挡的实现方式
* 离线建模：利用 Unity 编辑器在 Block 坐标系下，针对现实世界中的实体（如墙体、立柱、大型设备）创建 1:1 匹配的几何体；或通过对 Block 稠密模型进行裁剪与减面处理得到优化后的模型。
* 运行时对齐：在 xr-frame 运行时，通过云定位将 Block 坐标系与现实空间对齐，并加载对应的几何体。
* 材质替换：为这些几何体赋予特殊的遮挡材质。
* 视觉效果：当 GPU 渲染其他虚拟物体时，会因深度测试未通过而自动剔除被遮挡部分的像素，从而使虚拟物体遵循现实物理空间的遮挡逻辑。
## 如何布置简单几何体的遮挡
1. 对照稠密模型及全景图精确摆放方块标注。摆放后标注看起来就像是一面“墙”或者“柱子”。
![标注作为遮挡](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion02.png)
2. 修改标注的名称（如 `occlusion\_wall` ），记录 ID ，上传标注。
3. 在 xr-frame 小程序中利用其内置几何体加载作为遮挡的标注。
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRMesh,{})` 创建简单的几何体赋予 `easyar-occulusion` 材质。
> **注意**
`easyar-occulusion` 材质的加载，注册，反注册，卸载由 AR Session 控制。
```
````ts
handleEmaResult(ema: easyar.ema.v0\_5.Ema) {
let blockHolder: easyar.BlockHolder = session.blockHolder;
ema.blocks.forEach(emaBlock => {
const blockInfo: easyar.BlockInfo = {
id: emaBlock.id
};
// 若 Block 节点不存在，创建 Block 节点
blockHolder.holdBlock(blockInfo, easyarPlugin.toXRFrame(emaBlock.transform));
});
ema.annotations.forEach(annotation => {
if (annotation.type != mega.EmaV05AnnotationType.Node) {
return;
}
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
const emaName: string = nodeAnnotation.name;
const geometryStr: string = nodeAnnotation.geometry === "cube" ? "cube" : "sphere";
const assetInfo = AnnotationMetaData[nodeAnnotation.id as keyof typeof AnnotationMetaData];
let model: xrfs.Element;
if (assetInfo) {
// GLTF部分
} else {
model = scene.createElement(
xrFrameSystem.XRMesh,
{
// 使用插件注册好的遮挡材质
material: "easyar-occlusion",
// 使用 xr-frame 内置几何体，此处也可以直接使用 "cube"
geometry: geometryStr,
name: emaName,
"receive-shadow": "false",
"cast-shadow": "false"
// 注意不要修改 Scale
}
);
xrNode.addChild(model);
}
})
}
```
```
```
<video src="https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion03.mp4" style="width:480px; max-width:100%; height:auto;" muted playsinline controls></video>
> 有了遮挡后，这个熊猫就可以躲在墙后面跳舞了。
```
## 如何布置复杂几何体的遮挡
适用于异形设备、不规则建筑等需要高精度遮挡的场景。
您可以利用 Block 的稠密模型裁剪并减面得到您需要用于遮挡的白模。
1. 在 Unity 场景中点击 **Mega Block** 节点，在 **Inspector** 面板中记录 BlockID
![记录BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion08.png)
2. 在 Mega Studio 的 **Block** 中选择导出。
![选择导出](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion04.png)
3. 修改导出选项后导出。
![导出选项](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion05.png)
图中 1 为 LOD 层级，层级越低模型越简单，面数越少，若需要最高的精度选择2，若能接受降低精度以减少面数选择 1 或者 0。
图中 2 为导出贴图选项，由于我们只需要白模作为遮挡，不需要贴图。
4. 将导出后的模型在数字内容创建软件（例如 Blender）中进行裁剪，减面，保存为 `Glb`。
> **提示**
例子中使用的是 Blender 的 Decimate Modifier
![裁剪前](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion06.png)
裁剪并减面后：
![裁剪后](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion07.png)
5. 将遮挡用的 `Glb` 文件挂载到文件服务器，得到一个用于加载的 url。
6. 在 xr-frame 小程序中加载作为遮挡的 GLTF。
首先**加载**遮挡用的 GLTF 模型，然后使用 `scene.createElement(xrFrameSystem.XRGLTF,options)` 创建 GLTF 模型。
使用 `assets.getAsset("material", "easyar-occlusion")` 获取材质对象
使用 `model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {m.setData({ neverCull: true, material: occlusionMaterial });}` 修改 GLTF 模型的材质。
> **注意**
`easyar-occulusion` 材质的加载，注册，反注册，卸载由 AR Session 控制。
```
````ts
const sampleAssets = {
occlusion1: {
assetId: "occlusion1",
type: "gltf",
src: "url/occlusion1.glb",
options: {}
}
}
async loadAsset() {
if (!scene) {console.error("Empty scene"); return;}
try {
await scene.assets.loadAsset(sampleAssets.occlusion1);
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
},
addOcclusion() {
model = scene.createElement(
xrFrameSystem.XRGLTF,
{
"model": assetInfo.assetId,
"anim-autoplay": assetInfo.animation ? assetInfo.animation : "",
"scale": assetInfo.scale ? assetInfo.scale : "1 1 1",
name: "tree"
}
);
const blockID = "aaaa1234-bbbb-cccc-dddd-eeeeee123456" //此处应填写 Block ID
if (!blockHolder.getBlockById(blockParent.id)) {
// 若没有存在的 Block 节点，则创建一个
blockHolder.holdBlock({
id: blockID
})
}
// 获取 xr-frame 场景中的 Block 节点
let blockElement = blockHolder.getBlockById(blockParent.id).el;
// 将裁剪后的遮挡模型挂载到 Block 节点下，作为其子节点
blockElement.addChild(model);
/\*\*
\* 由于 GLTF 加载器的行为不同，为了保证模型在 xr-frame 上的朝向 与 Unity 的渲染结果完全一致
\* 有时需要对加载后的模型原地绕 Y 轴旋转 180 度
\*/
let modelTransform = model.getComponent(xrFrameSystem.Transform);
let currentRotation = modelTransform.quaternion.clone();
let targetRotation = currentRotation.multiply(new xrFrameSystem.Quaternion().setValue(0, 1, 0, 0));
modelTransform.quaternion.set(targetRotation);
//注意必须在修改 Transform 后修改材质
if (assetInfo.assetId == 'occlusion1') {
//获取 mega 插件提供的遮挡材质
let occlusionMaterial = scene.assets.getAsset("material", "easyar-occlusion");
//修改遮挡材质
model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {
m.setData({ neverCull: true, material: occlusionMaterial });
});
}
}
```
```
```
> [!NOTE]
> 这里使用 Mega Block 稠密模型进行裁剪后作为遮挡不需要使用标注同步空间位置，这是因为在数字内容创建软件（如 Blender） 中，可以在不改变坐标系定义的情况下对模型进行减免和裁剪。
>
> 若需要精确摆放自己制作的 GLTF 模型遮挡，请参考[如何摆放与空间对齐的遮挡模型](./sample.md#wechat-mega-sample-precise-occulusion-model)
最终实机运行效果见文章顶部视频。
```
## 遮挡的效果预期
xr-frame 小程序上遮挡的效果主要由以下几点影响：
* 定位跟踪本身的精度
* 模型摆放的准确程度
* 模型本身的精度（如果不是简单的几何体）
在定位漂移时出现数公分未对齐的情况是正常的。
遮挡用的模型面数太多容易影响性能，建议只在必要区域使用，并且尽量使用简单的几何体作为遮挡。
## 后续步骤
* [完整运行示例工程](fullstart.html)
* [示例工程说明](sample.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)

---

## 快速运行微信小程序 Mega 插件示例工程
- 章节路径: `wechat/mega/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/quickstart.html

# 快速运行微信小程序 Mega 插件示例工程
这篇文章将介绍如何快速运行微信小程序 Mega 插件的示例工程。您将学习如何：
* 搭建与配置示例工程的开发环境。
* 运行示例的部分功能：使用 Mega 云定位。
## 开始之前
* 参考文档 [我的定位库可以使用了吗？](../../mega/localization-verify.html) 确认定位库已正确创建并添加 Mega Block。
## 确认小程序主体为企业主体
> **重要事项**
Mega 小程序插件**仅支持企业主体**的微信小程序。
个人主体类型的小程序**无法**使用 Mega 小程序插件。
需要确认在 [小程序后台](https://mp.weixin.qq.com) 中 **设置** > **基本信息** > **主体信息** 显示为 **企业法人或个体工商户**。
由于 Mega 功能以小程序插件形式提供，您必须拥有一个**企业主体**的微信小程序作为宿主环境。
即使仅为了运行我们提供的示例工程，您也需要配置**自己的微信小程序 AppID** 才能在开发者工具中进行调试和预览。
## 下载示例工程
1. 前往 [开发工具下载页面](https://www.easyar.cn/view/download.html)。
2. 确认 *EasyAR 隐私政策* 后点击下载。
![下载Sample](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart02.png)
3. 下载完成后，在本地解压缩 `.zip` 包。
## 配置示例工程
1. 登录微信小程序开发者工具。
2. 使用微信小程序开发者工具导入示例项目。
* 打开开发者工具后，点击导入按钮， 选择本地解压好的目录。
![导入开发者工具](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart03.png)
![选择本地目录](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart04.png)
* 确保 AppID 与 **申请 Mega 许可证时填写的 AppID** 一致，开发模式为**小程序**，点击创建。
> **注意**
AppID 不一致会导致许可证校验不通过
![导入开发者工具选项](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart05.png)
* 配置 Mega 许可证及云服务
打开文件 `miniprogram/components/sample-data/easyar-settings.ts`，根据准备工作中的许可证和服务信息填入该文件中的相应字段：
* **Mega 许可证**
```
/\*\* 您的小程序 Mega 许可证 \*/
export const EasyARLicenseKey: string = "";
```
**如何获取 Mega 微信小程序许可证**
>
> 在
> EasyAR 开发中心
> 中选择
> Mega 微信小程序
> 。
>
![许可证列表](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites04.png)
>
> 列表中应存在要使用的
> Mega 微信小程序许可证
> 。（若不存在可用许可证，请检查您的账号和用于创建 Mega 定位库的账号是否是同一个）
>
> 点击
> 小程序名称
> 可以获取该小程序的 Mega 许可证（点击右侧复制，然后粘贴至
`> easyar-settings.ts
`> 文件中作为
`> EasyARLicenseKey
`> 的值），并确认其关联的 AppID 与您的微信小程序 AppID 完全一致。
>
![许可证详细信息](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart13.png)
>
* **云服务 API Key 及 Seceret**
```
/\*\* 您的云服务 API Key 及 Seceret \*/
export const EasyARAPIKey: string = "";
export const EasyARAPISecret: string = "";
```
**如何获取云服务 API Key 及 Seceret**
>
> 在
> EasyAR 开发中心
> 选择
> 云服务 API KEY
> 。
>
> 若先前已经创建过云服务 API Key 及 Seceret，此处可以依次点击右侧复制，粘贴至
`> easyar-settings.ts
`> 文件中作为
`> EasyARAPIKey
`> 和
`> EasyARAPISecret
`> 的值。
>
![云服务 API KEY](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites08.png)
>
> 若之前没有创建过云服务 API Key 及 Seceret，可以通过以下方式创建：
>
> 在
> Easy> AR 开发中心
> 选择
> 云服务 API KEY
> >
> 创建 API KEY
> 。
>
![创建 API KEY](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites06.png)
>
![创建 API KEY 详细](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites07.png)
>
> 输入应用名称，选中需要使用的云服务：
> Mega Block
> 和/或
> Mega Landmark
> ，点击确定。
>
* **云服务 ServerAddress 及 AppID**：
```
/\*\* 您的 Mega 云定位库的 ServerAddress 及 AppID \*/
export const MegaTrackerServerAddress: string = "";
export const MegaTrackerAppID: string = "";
```
**如何获取 Mega 云定位库的 ServerAddress 及 AppID**
>
> 在
> EasyAR 开发中心
> 选择
> Block 云定位
> ，之后选择您的
> Mega 云定位服务组
> 。
>
![选择云定位服务组](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites09.png)
>
> 选择您的 Mega 云定位库：
>
![选择云定位库](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites10.png)
>
![获取云定位信息](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites11.png)
>
> 点击
> 密钥
> ，在下方依次获取云定位库的 AppID 和 Server Address （点击右侧复制，然后粘贴至
`> easyar-settings.ts
`> 文件中作为
`> MegaTrackerAppID
`> 和
`> MegaTrackerServerAddress
`> 的值）。
>
## 实机运行示例
1. 点击小程序开发工具上方栏的实机预览按钮，通过扫描二维码加载到开发用的手机。
> **小心**
不能在开发工具上直接模拟运行带有 AR 功能的 xr-frame 组件。
![模拟运行](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart07.png)
![二维码加载](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart06.png)
> **注意**
当您在微信开发者工具中首次运行示例项目时，如果尚未获得插件权限，工具通常会弹窗提示插件未授权。可以通过微信开发者工具自动授权，或参考 [插件接入流程](https://developers.weixin.qq.com/miniprogram/introduction/plugin.html#插件开发接入流程)
2. 点击 **EasyAR Mega Samples** 进入示例项目的 AR 场景。
![Sample入口](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart08.png)
> **注意**
若无法进入示例项目的 AR 场景，可能是由于当前设备不支持微信的视觉算法组件 VisionKit，具体请参考[机型限制](known-issues.html#wechat-mega-known-issues-devices)。
3. 屏幕中提示 `EasyAR Session is initializing` 表示微信平面检测正在初始化。
> **提示**
确保在光线充足的环境下测试，避开大面积纯色墙面或纯色地板。
对着地面或其他平面匀速左右摆动以加快这个过程。
![初始化](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart09.png)
4. 初始化完成后，将手机竖直使相机拍到正常的现实画面，当定位成功，Debug 信息中出现 `Found` 字样，并且右下方的状态指示物由白色变为绿色。
![定位](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart10.png)
## 后续步骤
* [在 Unity 里使用 Mega Studio](content-unity-setup.html)
* [使用 Unity 编辑器 摆放 3D 内容](content-simple.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
* [Mega 简介](../../mega/intro.html)
* [获取和使用 APIKey](../../apikey-auth.html)

---

## EasyAR Mega 微信小程序插件发布日志
- 章节路径: `wechat/mega/release-notes.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/release-notes.html

# EasyAR Mega 微信小程序插件发布日志
本页面记录了 EasyAR Mega 微信小程序插件各个版本的发布日志。
> **重要事项**
**版本维护及升级建议**
* **2.0.0 及以上版本**：建议所有用户升级至 [最新版本 (2.0.2)](#mega-wechat-miniprogram-plugin-v202) 以获得最佳稳定性。
* **2.0.0 以下版本**：已完全重构并不再维护，请迁移至新版本。
## 快速导航
* [🚀 最新版本 (2.0.2)](#mega-wechat-miniprogram-plugin-v202)
* [📦 2.x 版本历史记录](#mega-wechat-miniprogram-plugin-v2-series)
* [📜 1.x 历史版本 (已不再维护)](#mega-wechat-miniprogram-plugin-v1-series)
## 2.0.2
>
> 发布日期：2025-11-19
>
* 修复了高网络延迟环境下，初始的定位跟踪效果不如预期的问题。
## 2.x 版本历史记录
2.x 是重构后稳定版本，提供了更加鲁棒的 AR 体验和更清晰的 API 调用方式。
### 2.0.1
* 优化了跟踪效果。
### 2.0.0
* **新增**：Sample, Toolbox 及 API 文档全面更新。
* **新增**：支持 APIToken。
* **新增**：全方位支持 TypeScript 类型推断。
* **新增**：支持使用旋转后的屏幕。
* **优化**：提供了更流畅的 AR 体验，不再会因获取图片卡顿。
* **优化**：使用微信原生提供的图片接口，更鲁棒。
* **优化**：AR 内容的跟踪更平滑，更稳定。
* **重构**：重写了 MegaSession 的工作流，大幅简化流程，支持纯代码创建。
* **重构**：解耦 Ema 标注数据的获取和场景中加载过程。
## 1.x 历史版本记录
1.x 是历史版本，已停止维护，以下内容仅供参考。
### 1.1.12
* 支持 v4DH CLS 库。
### 1.1.10
* 修复了上个版本中 `viewLocalizationInfo` 的版本兼容性问题。
### 1.1.9
* 增加了定位成功时的上报信息。
### 1.1.2 - 1.1.8
* 优化跟踪效果。
* 修复 Android 8.0.37 获取图像为纯黑问题。
* 修复无 Ema 时 Block 默认位置到世界原点。
### 1.1.1
* 修复不设置配置信息时运行错误。
### 1.1.0
* **新增**：导出数学方法。
* **新增**：调整为组件，使用 XML 标签方式引入插件。
* **修复**：修复重新设置 Mega 参数时的异常。
* **优化**：插件退出时增加资源释放，优化内部实现。
### 1.0.5
* 首次上线。

---

## 微信小程序 Mega 插件示例工程说明
- 章节路径: `wechat/mega/sample.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/sample.html

# 微信小程序 Mega 插件示例工程说明
这篇文章详细说明了示例工程展示的各功能使用方法，实现方式与注意事项。
## 开始之前
* 能够[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)，并记录标注名称与其 ID。
* 能够[使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)。
* 能够[完整运行示例工程](fullstart.html)。
## 如何在标注位置展示模型
1. **在 Unity 编辑器中精确摆放并上传标注，记录标注名称与其 ID**
![Unity标注位置](https://doc-asset.easyar.com/develop/wechat/mega/media/sample01.png)
2. **添加 GLTF 模型资源**
在 `miniprogram/components/sample-easyar-mega/index.ts` 中的 `sampleAssets` 中添加模型资源。
```
const sampleAssets = {
your\_model\_name: {
assetId: "your\_model\_asset\_id",
type: "gltf",
src: "url/model.glb",
options: {}
}
}
```
3. **加载添加的模型资源**
在 `miniprogram/components/sample-easyar-mega/index.ts` 中的 `loadAsset()` 函数中加载模型。
```
async loadAsset() {
try {
await scene.assets.loadAsset(sampleAssets.your\_model\_name);
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
}
```
4. **配置要替换的标注**
在 `miniprogram/components/sample-data/annotation-metadata.ts` 中配置要替换的标注，如果要替换多个则用逗号隔开。
```
export const AnnotationMetaData: Record<string, any> = {
"aaaaaaaa-bbbb-cccc-dddd-123456789012": {
assetId: "panda",
scale: "0.5 0.5 0.5"
},
"aaaaaaaa-bbbb-cccc-dddd-123456789013": {
assetId: "your\_model\_asset\_id",
scale: "1 1 1"
}
};
```
5. **替换标注加载模型**
在 EMA 加载的回调中使用 xr-frame 的“工厂方法” `scene.createElement(xrFrameSystem.XRGLTF, options)`创建模型节点。
* 参数：
* `xrFrameSystem.XRGLTF`：指定创建的元素类型为 GLTF 模型。
* `options`：初始化配置项，对应组件的属性。
* 代码中的关键属性：
* `"model"`：必填，指向已加载的资源 ID（asset-id）。
* `"anim-autoplay"`：选填，指定加载后自动播放的动画名称。
* `"scale"`: 选填， `assetInfo.scale` 或 "1 1 1"。
* `name`: 必填，标注名称。
> **小心**
注意区分属性 Key 的字符串和非字符串，完全按照示例中的方式填写。
将模型挂载到标注节点下 `xrNode.addChild(child)`。
为了保证 GLTF 模型在不同平台的加载器下看到一样的结果，需要对加载后的模型原地绕 Y 轴旋转 180 度。
```
if (assetInfo && assetInfo.assetId && assetInfo.assetId.trim().length > 0) {
model = scene.createElement(
xrFrameSystem.XRGLTF,
{
/\*\* 即前一步骤中的 assetId \*/
"model": assetInfo.assetId,
/\*\* 可以在此处指定播放的模型动画 \*/
"anim-autoplay": assetInfo.animation ? assetInfo.animation : "",
"scale": assetInfo.scale ? assetInfo.scale : "1 1 1",
name: emaName
}
);
xrNode.addChild(model);
/\*\*
\* 由于 GLTF 加载器的行为不同，为了保证模型在 xr-frame 上的朝向 与 Unity 的渲染结果完全一致
\* 需要对加载后的模型原地绕 Y 轴旋转 180 度
\*/
let modelTransform = model.getComponent(xrFrameSystem.Transform);
let currentRotation = modelTransform.quaternion.clone();
let targetRotation = currentRotation.multiply(new xrFrameSystem.Quaternion().setValue(0, 1, 0, 0));
modelTransform.quaternion.set(targetRotation);
}
```
* **实机运行**
* 实机运行的结果如下，可以与**第 1 步**中 Unity 编辑器上的位置进行比照：
* 打开左侧透明视频按钮，世界坐标系原点（坐标为 `(0, 0, 0)` 的位置）出现透明视频材质的方块。
> **注意**
原点位置可能是随机在空间中的任意位置。可以利用标注将遮挡模型放置到您希望的位置，详见[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
* 打开左侧遮挡按钮，世界坐标系原点（坐标为 `(0, 0, 0)` 的位置）出现熊猫模型和上下层叠的方块，中间的方块具有遮挡材质，另一侧有一个带有遮挡材质的静态熊猫模型。
> **注意**
原点位置可能是随机在空间中的任意位置。可以利用标注将遮挡模型放置到您希望的位置，详见[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
![模型和遮挡](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart11.png)
## 如何将透明视频在标注位置播放
1. **加载类型为 `video-texture` 的视频资源**。
```
async loadAsset() {
const videoTexture = {
assetId: "fireball",
type: "video-texture",
// 视频资源 URL
src: "url/video-resource.mp4",
options: {
autoPlay: true,
loop: true,
}
};
try {
// 加载 video-texture 类型资源
await scene.assets.loadAsset(videoTexture);
} catch (err) {
console.error(`Failed to load video texture: ${err.message}`);
}
}
```
2. **修改 EMA 加载回调**
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRMesh,options)` 创建简单的几何体赋予 `easyar-video-tsbs` 材质， 并修改 `uniform` 为 `u\_baseColorMap:video-{$assetId}`。
* 参数：
* `xrFrameSystem.XRMesh`：指定创建的元素类型为基础几何体。
* `options`：初始化配置项，对应组件的属性。
* 代码中的关键属性：
* `"geometry"`: "cube"：使用 xr-frame 内置的立方体几何数据。
* `"material"`: "easyar-video-tsbs"：指定一个预定义的材质（根据命名推测，这是一个支持视频纹理的特殊材质）。
* `"uniforms"`: "u\_baseColorMap:video-{$assetId}"：
> **小心**
注意区分属性 Key 的字符串和非字符串，完全按照示例中的方式填写。
这是材质参数的动态绑定。
它将名为 `video-{$assetId}` 的视频资源（纹理）映射到了材质的基色图上。
效果：这会产生一个表面正在播放视频的立方体。
```
model = scene.createElement(xrFrameSystem.XRMesh, {
geometry: "cube",
material: "easyar-video-tsbs",
uniforms: "u\_baseColorMap:video-fireball",
});
xrNode.addChild(model);
```
> **注意**
在使用 `video-texture` 时，若控制台出现 `wx.createVideoDecoder with type: 'wemedia' is deprecated` 警告，请忽略。
经与微信官方团队确认，该警告不影响使用。
* **实机运行**
## 如何摆放与空间对齐的遮挡模型
1. **精确摆放用于遮挡的模型并上传标注。**
![精确对齐](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion10.png)
2. **在 xr-frame 小程序中加载作为遮挡的 GLTF。**
通过 `scene.assets.loadAsset()` 加载模型资源（需要手动卸载）。
```
const sampleAssets = {
occlusion1: {
assetId: "occlusion1",
type: "gltf",
src: "url/occlusion1.glb",
options: {}
}
}
async loadAsset() {
if (!scene) {console.error("Empty scene"); return;}
try {
await scene.assets.loadAsset(sampleAssets.occlusion1);
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
}
```
3. **运行时在 EMA 加载回调中加载模型并赋予遮挡材质**
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRGLTF,options)` 创建模型节点。
* 参数：
* `xrFrameSystem.XRGLTF`：指定创建的元素类型为 GLTF 模型。
* `options`：初始化配置项，对应组件的属性。
* 代码中的关键属性：
* `"model"`：必填，指向已加载的资源 ID（asset-id）。
* `"scale"`: 选填 `assetInfo.scale` 或 "1 1 1"。
* `name`: 必填，标注名称。
> **小心**
注意区分属性 Key 的字符串和非字符串，完全按照示例中的方式填写。
将模型挂载到标注节点下 `xrNode.addChild(child)`。
为了保证 GLTF 模型在不同平台的加载器下看到一样的结果，需要对加载后的模型原地绕 Y 轴旋转 180 度。
最终使用 `model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {m.setData({ neverCull: true, material: occlusionMaterial });}` 修改 GLTF 模型的材质。
> **注意**
`easyar-occulusion` 材质的加载，注册，反注册，卸载由 AR Session 控制。
使用模型在标注位置作为遮挡：
```
if (...) {
model = scene.createElement(
xrFrameSystem.XRGLTF,
{
"model": assetInfo.assetId,
"scale": assetInfo.scale ? assetInfo.scale : "1 1 1",
name: emaName
}
);
/\*\*
\* 由于 GLTF 加载器的行为不同，为了保证模型在 xr-frame 上的朝向 与 Unity 的渲染结果完全一致
\* 有时需要对加载后的模型原地绕 Y 轴旋转 180 度
\*/
let modelTransform = model.getComponent(xrFrameSystem.Transform);
let currentRotation = modelTransform.quaternion.clone();
let targetRotation = currentRotation.multiply(new xrFrameSystem.Quaternion().setValue(0, 1, 0, 0));
modelTransform.quaternion.set(targetRotation);
//注意必须在修改 Transform 后修改材质
if (assetInfo.assetId == 'occlusion1') {
//获取 mega 插件提供的遮挡材质
let occlusionMaterial = scene.assets.getAsset("material", "easyar-occlusion");
//修改遮挡材质
model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {
m.setData({ neverCull: true, material: occlusionMaterial });
});
}
}
```
* **实机运行**
可与 Unity 编辑器上模拟运行的结果进行比照。
## 相关主题
* [环境遮挡](occlusion.html)
* [透明视频](transparent-video.html)
* [使用 Unity 编辑器模拟运行](content-simulation.html)

---

## AR Session 屏幕旋转适配
- 章节路径: `wechat/mega/session-device-orientation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-device-orientation.html

# AR Session 屏幕旋转适配
这篇文章介绍了当需要横屏运行微信小程序时如何配置 AR Session。
## 开始之前
* 通过 [AR 驱动的 3D 渲染](../../fundamentals/fundamentals.html)了解相机图像相对于屏幕方向的旋转角是什么。
* 了解 [AR Session 的概念与流程](session-state.html)。
## Mega 小程序插件的屏幕朝向枚举
> **注意**
手机屏幕的朝向定义请参考 IOS, Android 等系统的官方定义。
Mega 小程序插件的屏幕朝向枚举 [DeviceOrientation](../../../api/wechat/easyar.DeviceOrientation.html):
|Constant|Value|Description|
|`Portrait`|0|Portrait|
|`LandscapeLeft`|90|LandscapeLeft|
|`PortraitUpsideDown`|180|PortraitUpsideDown|
|`LandscapeRight`|270|LandscapeRight|
## 在微信小程序全局配置中修改屏幕朝向
在 `app.json` 中添加 `window` 配置，具体定义见 [响应显示区域变化](https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html) 。
```
"window": {
"pageOrientation": "landscape"
}
```
根据实际情况填入 "portrait"（竖屏） 或者 "landscape"（横屏）。
> **小心**
任何时候**不要**在 AR 小程序应用中使用 "auto"，在某些情况下会导致 AR 画面严重异常。
## 设置屏幕朝向
调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_) 传入屏幕旋转的方向，可随时调用，立即生效。
比如需要在屏幕相对自然竖直位置逆时针旋转 90 度的横屏模式下使用：
```
let deviceOrientation = mega.DeviceOrientation.LandscapeLeft;
session.setDeviceOrientation(deviceOrientation);
```
mega 插件提供的屏幕朝向设置是为了**弥补微信小程序屏幕朝向监听缺失**。微信在 `pageOrientation` 设置中仅提供了 `portrait` 和 `landscape` 两个选项，而对于 AR 应用来说仅这两个选项是不够的。例如自然朝向逆时针旋转90度的横屏和自然朝向逆时针旋转270度的横屏完全不同。
因此当 `app.json` 中 `pageOrientation` 设置为 `portrait` 时，可以不调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_)，因为一般手机的自然竖直方向是 session 的默认朝向。
当 `app.json` 中 `pageOrientation` 设置为 `landscape` 时，必须调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_) 将屏幕朝向固定为 [LandscapeLeft](../../../api/wechat/easyar.DeviceOrientation.html#w_easyar_DeviceOrientation_LandscapeLeft_member) 或 [LandscapeRight](../../../api/wechat/easyar.DeviceOrientation.html#w_easyar_DeviceOrientation_LandscapeRight_member)

---

## 如何记录与转发 AR Session dump 文件
- 章节路径: `wechat/mega/session-dump.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-dump.html

# 如何记录与转发 AR Session dump 文件
AR Session dump 文件是 EasyAR 团队排查定位、跟踪问题的核心依据。
## 开始之前
* 了解什么是 [AR Session](session.html)。
* 确保您的项目已经[启用 EasyAR Mega](integration.html)。
## 什么是 AR Session dump 文件
> **重要事项**
AR Session dump 文件是微信小程序上分析和解决 Mega 定位、跟踪问题**最重要的依据**。
AR Session dump 文件记录了小程序进行 Mega 定位请求时的关键时空上下文。
## 如何记录与转发
通过调用 `session.dumpSession(signal: boolean)` 接口控制记录流程：
* **传入 `true`**：启动记录。
* **传入 `false`**：停止记录，并返回生成的 **文件临时路径 (tempFilePath)**。
通常建议将记录逻辑与 UI 按钮绑定，在开始记录时通过 [wx.showToast()](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html) 方法提示记录开始，在记录结束时通过 [wx.shareFileMessage()](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareFileMessage.html) 方法将记录的文件通过微信聊天转发。
```
/\*\*
\* 处理 Session 记录逻辑
\* @param signal true 为开始记录，false 为结束记录并转发
\*/
dumpSession(signal: boolean): void {
// 调用接口获取路径
const recordPath = session.dumpSession(signal);
// signal 为 true 时，接口返回空字符串，表示正在记录
if (recordPath.length == 0) {
wx.showToast({
title: '开始记录数据',
icon: 'success',
duration: 2000
});
return;
}
// signal 为 false 时，处理返回的文件路径
wx.shareFileMessage({
filePath: recordPath,
success() {
wx.showToast({
title: '记录转发成功',
icon: 'success',
duration: 2000
});
},
fail() {
wx.showToast({
title: '记录转发失败',
icon: 'error',
duration: 2000
});
}
})
}
```
>
> 这个例子演示了如何在 xr-frame 组件中使用
`> session.dumpSession()
`> 方法记录并转发 AR Session dump 文件，并且给出相应的 Toast 提示。
>
> **注意**
由于小程序本地空间限制（通常为 200MB），建议单次录制时间不要过长，且最长录制时间不能超过 10 分钟。
## 相关主题
* [使用微信小程序 Mega Toolbox 记录与转发 session dump 数据](../../../mega/data-collection/wechat/toolbox-dump.html)
* [使用你的小程序录制 AR Session dump 文件](../../../mega/data-collection/wechat/wechat-dump.html)
* [微信小程序问题报告注意事项](../diagnostics/report.html)

---

## AR Session 非现场使用
- 章节路径: `wechat/mega/session-gnss-simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-gnss-simulation.html

# AR Session 非现场使用
这篇文章介绍了如何不在现场时使用 AR Session。
## 开始之前
* 了解 [AR Session 的概念与流程](session-state.html)
## 启用 Simulator 模式
使用 **Simulator** 模式可以避免开发 AR 应用过程中开发者必须长期驻场的情况。
在该模式下，session 不使用 GNSS 数据或使用虚假的 GNSS 数据输入。
> **警告**
启用 Simulator 模式后，画面会出现特定水印。
小程序正式发布时，AR Session 不允许使用 Simulator 模式。请务必在上线前移除相关配置。
### 不使用 GNSS 数据
使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [setGeoLocationInput(inputMode, geoLocation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setGeoLocationInput_member_1_) 方法 仅传入 "Simulator" 字符串。此后 session 不进行任何经纬度相关的定位。
```
session.setGeoLocationInput("Simulator");
```
### 使用模拟的 GNSS 数据
若需模拟用户处于特定位置，使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [setGeoLocationInput(inputMode, geoLocation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setGeoLocationInput_member_1_) 方法传入 "Simulator" 字符串和指定的经纬度。此后 session 使用模拟的经纬度数据进行定位。
```
const targetLongitude = 123.45; // 经度
const targetLatitude = 32.1; // 纬度
session.setGeoLocationInput("Simulator", { longitude: targetLongitude, latitude: targetLatitude });
```
> **警告**
模拟输入必须使用 WGS-84 坐标系的经纬度数据。
使用错误的经纬度数据可能会导致定位失败或错乱。

---

## 平面 AR 追踪器异常处理
- 章节路径: `wechat/mega/session-plane-detection-error.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-plane-detection-error.html

# 平面 AR 追踪器异常处理
这篇文章介绍了如何通过注册回调处理微信平面 AR 追踪器的异常。
## 开始之前
* 通过[MegaTracker 工作流](tracker.html)了解：
* xr-frame 的[平面AR追踪器](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#Plane) 本质上是 [VisionKit 6DoF-平面能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)的封装。
* MegaTracker 是如何在 xr-frame 上工作的。
* 了解 [AR Session 的概念与流程](session-state.html)
## 为什么会出现平面检测异常
在特定情况下（如画面中出现大片白墙、摄像头长时间被遮挡等），微信平面 AR 追踪器可能出现状态异常。
此时平面 AR 追踪器无法正常输出每帧的相机位姿（即 6DoF 数据）这会导致 MegaTracker 无法工作。
当画面正常（纹理丰富，摄像头不被遮挡）一段时间后平面 AR 追踪器会恢复工作，同时 MegaTracker 也会恢复工作。
## 设置平面检测异常时的行为
通过 [setPlaneDetectionErrorBehavior(behavior)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setPlaneDetectionErrorBehavior_member_1_) 注册异常处理回调。当检测到异常时，该回调会被触发，开发者可在其中实现自定义提示，隐藏 3D 内容或其他处理逻辑。
```
session.setPlaneDetectionErrorBehavior(() => {
wx.showToast({
icon: 'none',
title: `微信平面检测结果异常，请将相机对着平面来回移动以恢复跟踪`,
duration: 2000,
});
});
```
>
> 这个例子中使用 session 的
[> setPlaneDetectionErrorBehavior(behavior)
](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setPlaneDetectionErrorBehavior_member_1_)> 接口注册了一个弹出 Toast 窗口的回调，当平面检测异常时触发。
>

---

## AR Session 流程控制
- 章节路径: `wechat/mega/session-state.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-state.html

# AR Session 流程控制
这篇文档将介绍 AR Session 流程控制，包括如何创建、启动、停止并销毁 AR Session。
## 开始之前
* 了解 [AR Session 的概念与流程](session-state.html)
## 创建
使用配置中的云定位库 `appId`，云服务 `serverAddress`，云服务 `apiKey` 和 `apiSecret` 创建 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)。
然后使用创建的 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member) 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
再使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
```
createSession() {
// 获取场景中挂载的 megaComponent
const megaElement = scene.getElementById('easyar-mega');
const megaComponent = megaElement.getComponent("easyar-mega") as easyar.EasyARMegaComponent;
// MegaTracker 云服务鉴权配置
const apiKeyAccess = new mega.APIKeyAccessData(this.data.appId, this.data.serverAddress, this.data.apiKey, this.data.apiSecret);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess
}
// Session 配置
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
}
// 创建实例
session = megaComponent.createSession(sessionConfigs);
}
```
>
> 这段代码演示了如何从场景中获取
`> megaComponent
`> 之后使用配置创建 session 实例。
>
> **小心**
单实例限制：一个场景中仅允许存在一个 Session 实例。在创建新 Session 前，必须确保已调用 [closeSession()](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_closeSession_member_1_) 销毁旧实例，否则将导致创建失败。
## 启动
一般在 xr-frame 的 AR 系统准备就绪的回调中使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 方法启动 session。
> **警告**
MegaTracker 依赖于平面 AR 追踪器提供的数据，在平面追踪器初始化完成前无法工作。
在 WXML 中使用 `bind:ready="handleReady"` 注册 AR 系统准备就绪事件：
```
<xr-scene ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
```
在 xr-frame 组件中的回调函数 `handleReady` 中使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 方法启动 session。
```
handleReady: function(event) {
try {
//启动 Session，默认失败重试 5 次
await session.start();
} catch (err) {
console.error(`EasyAR Session initialization failed: ${err.message}`);
return;
}
}
```
## 停止并销毁
使用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [closeSession()](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_closeSession_member_1_) 方法销毁 session。
建议在 xr-frame 组件生命周期的 [detached](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) 中调用保证在离开页面时（即组件实例被从页面节点树移除时）销毁。
```
lifetimes: {
detached: function() {
const megaElement = scene.getElementById('easyar-mega');
const megaComponent = megaElement.getComponent("easyar-mega") as easyar.EasyARMegaComponent;
megaComponent.closeSession();
}
}
```
## 前后台切换
在页面退到后台时使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [pause()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_pause_member_1_) 方法暂停 session。
在页面回到前台时使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [resume()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_resume_member_1_) 方法恢复 session。
```
/\*\* 小程序页面的调用\*/
onHide() {
if (this.ar) {
this.ar.pauseSession();
}
},
onShow() {
if (this.ar) {
this.ar.resumeSession();
}
}
/\*\* xr-frame 组件中的函数\*/
pauseSession(): void {
if (!session) { console.error("EasyAR Session is not ready"); return;}
session.pause();
},
resumeSession(): void {
if (!session) { console.error("EasyAR Session is not ready"); return;}
session.resume();
}
```
>
> 这段代码中 xr-frame 组件暴露了
`> pauseSession()
`> 和
`> resumeSession()
`> 两个函数。
>
> 在小程序页面中在
[> onHide
](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onHide)> 即小程序从前台进入后台时调用
`> pauseSession()
`> 暂停 session。
>
> 在
[> onShow
](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppShow.html)> 即小程序从后台进入前台时调用
`> resumeSession()
`> 恢复 session。
>

---

## Mega 微信小程序插件上的 AR Session 概念与流程
- 章节路径: `wechat/mega/session.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session.html

# Mega 微信小程序插件上的 AR Session 概念与流程
这篇文档将介绍 Mega 微信小程序插件上的 AR Session 的概念与流程。
## AR Session 是什么
Mega 微信小程序插件提供的 AR Session 是所有 AR 功能的入口。它管理运行过程和状态：包括从 VisionKit 和微信提供的传感器 API 获取数据、融合云定位与本地 AR 跟踪器结果、驱动场景中相机等其它部分物体的移动和渲染等。
```
flowchart LR
Pose(VisionKit 相机位姿) -- 每帧同步 --> Session[Session]
Image(计算该帧相机位姿所使用的相机图片) -. 仅 Mega 定位时发送 .-> Session
Sensor(微信传感器数据) -. 异步 .-> Session
Session -- Transform --> Camera(xr-frame 摄像机)
```
## AR Session 的流程
```
flowchart LR
Start((" "))
End((" "))
Init[Initializing]
Run[Running]
Check{Success?}
Start -->|调用 start| Init
Init --> Check
Check -->|是| Run
Check -->|否 / 重试次数超过上限| End
Run -->|调用 stop| End
```
启动： session 状态转为 Initializing 。包含环境检查、资源加载以及等待微信 xr-frame 的 AR 系统就绪。
运行： session 状态转为 Running 。在此阶段，session 每帧输出跟踪结果并更新 xr-frame 相机的 Transform。
停止： session 状态转为 None 。包含释放资源、重置状态、销毁 MegaTracker。
> **警告**
AR 功能必须在 session 启动成功后才能使用。
AR Session 状态：
|状态|描述|
|None|初始状态，session 未启动或初始化失败|
|Initializing|初始化过程中|
|Running|运行状态，session已启动且初始化完成|
## [可选] 微信小程序插件上的 AR Session 与 Unity 上的 AR Session
> **注意**
仅针对 Unity 项目迁移的开发者。
Mega 微信小程序插件上的 AR Session 是 Unity 上 AR Session 的简化版本。由于不支持其他算法组件同时使用，微信小程序上的 AR Session 使用预集成的数据源组件和算法组件，用户不能选择数据源和/或组装算法组件。
此外，可以认为 Mega 微信小程序插件仅支持以 Block 为 target 且使用以 target 为中心的中心模式。
## 后续步骤
* [AR Session 流程控制](session-state.html)
## 相关主题
* [MegaTracker 的概念与工作流](tracker.html)

---

## MegaTracker 云服务鉴权
- 章节路径: `wechat/mega/tracker-access.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-access.html

# MegaTracker 云服务鉴权
这篇文章介绍了如何指定 MegaTracker 使用云服务时的鉴权方式。
## 开始之前
* 了解[MegaTracker 的概念与工作流](tracker.html)
* [获取和使用 APIKey](../../apikey-auth.html)
## 使用 API Key 和 API Secret 鉴权
这种方式适用于传统的密钥对验证。你需要使用 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member) 来构造 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 中的 `access` 对象。
```
const apiKeyAccess = new mega.APIKeyAccessData(
settings.MegaTrackerAppID, // Mega 定位服务 AppID
settings.MegaTrackerServerAddress, // Mega 定位服务地址
settings.EasyARAPIKey, // APIKey 字符串
settings.EasyARAPISecret // APISecret 字符串
);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
>
> 这个例子中先使用配置中的云定位库
`> appId
`> ，云服务
`> serverAddress
`> ，云服务
`> apiKey
`> 和
`> apiSecret
`> 创建了
[> APIKeyAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)> 。
>
> 然后使用了创建的
[> APIKeyAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)> 创建
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> 。 这代表将使用 API Key 和 API Secret 鉴权
>
## 使用 API Token 鉴权
若能够使用服务器定时（每几分钟或几个小时）更新和下发 `APIToken`，使用这种方式避免了直接使用 APISecret 对定位请求进行签名，安全性更高。`APIToken` 的更新方式请参考 [Token的创建和使用方法](../../apikey-auth.html)。
可以根据 Token 的有效期，在前端设置定时器进行更新。
首先使用设置中的 Mega 定位库 AppID 和定位服务地址创建 [TokenAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member)。
然后使用创建的 [TokenAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member) 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
然后使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
当 Token 过期时，必须调用 [updateToken(apiToken)](../../../api/wechat/easyar.MegaTracker.html#w_easyar_MegaTracker_updateToken_member_1_) 进行更新，否则 Mega 服务将不可用，定位结果中的状态始终为 [ApiTokenExpired](../../../api/wechat/easyar.MegaLocalizationStatus.html#w_easyar_MegaLocalizationStatus_ApiTokenExpired_member)。
```
const tokenAccess = new mega.TokenAccessData(
settings.MegaTrackerAppID, // Mega 定位服务 AppID
settings.MegaTrackerServerAddress, // Mega 定位服务地址
"your\_api\_token" // APIToken 字符串
);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: tokenAccess
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
>
> 这个例子演示了如何使用
[> TokenAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member)> 创建
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> ，并且用这个
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> 创建 session 以使用
`> APIToken
`> 鉴权。
>

---

## MegaTracker 传感器外部控制
- 章节路径: `wechat/mega/tracker-external-sensor.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-external-sensor.html

# MegaTracker 传感器外部控制
默认情况下，MegaTracker 会自动管理加速度计和 GNSS 数据的监听接口。但在某些复杂应用场景中，开发者可能需要手动控制这些接口的开启和关闭，以实现更精细的功耗管理或权限控制。
## 开始之前
* 了解[MegaTracker 的概念与工作流](tracker.html)
## 外部控制约束逻辑
在 session 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 时，可以通过 [MegaTrackerSensorOptions](../../../api/wechat/easyar.MegaTrackerSensorOptions.html) 配置传感器的监听接口。
|参数名|类型|默认值|说明|
|isAcceExternalControl|`boolean`|`false`|加速度计是否由外部（开发者）控制。|
|isGeoExternalControl|`boolean`|`false`|GNSS 数据是否由外部（开发者）控制。|
> **提示**
**适用场景**：如果您的应用除了 Mega 功能外，本身不直接订阅传感器数据，建议保持默认值 `false`，由 Mega 自动处理。
当上述参数设置为 `true` 时，开发者必须严格遵守以下调用顺序：
* **启动流程**
在调用 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) **之前**，必须确保已手动开启对应的传感器监听：
* **加速度计**：调用 [wx.startAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.startAccelerometer.html)。
* **GNSS**：调用 [wx.startLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)。
* **停止流程**
在调用 [stop()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_stop_member_1_) **之后**，方可关闭对应的传感器监听：
* **加速度计**：调用 [wx.stopAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.stopAccelerometer.html)。
* **GNSS**：调用 [wx.stopLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.stopLocationUpdate.html)。
> **小心**
**冲突警告**：若设置为 `false`（Mega 托管），不能在 Session 运行期间调用微信原生的停止传感器接口，否则会导致数据中断。
```
const megaTrackerSensorOptions: easyar.MegaTrackerSensorOptions = {
isAcceExternalControl: false,
isGeoExternalControl: true
};
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess,
options: megaTrackerSensorOptions
};
session = megaComponent.createSession(megaTrackerConfigs);
```
>
> 这个例子演示了如何外部控制开启和关闭微信地理位置数据监听，在调用
[> start(options)
](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_)> 之前，需要调用
[> wx.startLocationUpdate
](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)> 以开启微信地理位置数据监听。
>

---

## 使用 Mega Landmark 服务
- 章节路径: `wechat/mega/tracker-landmark.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-landmark.html

# 使用 Mega Landmark 服务
这篇文章介绍了在微信小程序 Mega 插件接入后，如何使用 Mega Landmark 的定位服务。
## 开始之前
* [获取和使用 APIKey](../../apikey-auth.html)（必须包括**Mega Landmark**）。
* 了解 [MegaTracker 的概念与工作流](tracker.html)。
* 了解 [MegaTracker 云服务鉴权](tracker-access.html)。
## 启用 Mega Landmark
首先使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 作为 `apiType` 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
然后使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
```
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess,
apiType: mega.MegaApiType.Landmark
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
## 如何使用 LandmarkFilter
当使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 创建时，MegaTracker 会自动内部实例化 [MegaLandmarkFilter](../../../api/wechat/easyar.MegaLandmarkFilter.html)。
它的功能是 MegaTracker 在使用 Landmark 服务时通过 SpotId 或 GNSS 数据筛选当前最合适的 Mega 定位库。
筛选接口只能在 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 成功后调用。
当 MegaTracker 使用 Landmark 服务而**没有**筛选成功时，定位状态始终为 [MissingSpotVersionId](../../../api/wechat/easyar.MegaLocalizationStatus.html#w_easyar_MegaLocalizationStatus_MissingSpotVersionId_member)
* **使用提供的 SpotID 匹配定位库**：
使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 的 [filterBySpotId(spotId)](../../../api/wechat/easyar.MegaLandmarkFilter.html#w_easyar_MegaLandmarkFilter_filterBySpotId_member_1_) 方法通过 SpotID 匹配定位库：
```
async landmarkFilter() {
const res = await session.megaTracker.landmarkFilter.filterBySpotId(settings.LandmarkSpotId);
if (res.status != mega.MegaLandmarkFilterStatus.Found) {
console.error(`LandmarkFilter Failed, status: ${mega.MegaLandmarkFilterStatus[res.status]}, exceptionInfo : ${res.exceptionInfo}`)
}
}
```
* **使用当前的 GNSS 数据匹配定位库**：
使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 的 [filterByLocation()](../../../api/wechat/easyar.MegaLandmarkFilter.html#w_easyar_MegaLandmarkFilter_filterByLocation_member_1_) 方法通过使用当前的 GNSS 数据 匹配定位库：
```
async landmarkFilter() {
const res = await session.megaTracker.landmarkFilter.filterByLocation();
if (res.status != mega.MegaLandmarkFilterStatus.Found) {
console.error(`LandmarkFilter Failed, status: ${mega.MegaLandmarkFilterStatus[res.status]}, exceptionInfo : ${res.exceptionInfo}`)
}
}
```

---

## MegaTracker 的概念与工作流
- 章节路径: `wechat/mega/tracker.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker.html

# MegaTracker 的概念与工作流
这篇文档将介绍 MegaTracker 的基本概念及 MegaTracker 与微信原生的 AR 系统 VisionKit 和渲染框架 xr-frame 的关系。
## 开始之前
通过 [Mega 简介](../../mega/intro.html) 了解：
* Mega 定位与跟踪的基本原理。
* 什么是 Mega Block。
* 集成 Mega 后的预期结果。
## 平面 AR 追踪器 是什么
xr-frame 的[平面AR追踪器](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#Plane) 本质上是 [VisionKit 6DoF-平面能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)的封装。
在 xr-frame 的摄像机组件开启 `isARCamera` 后，摄像机的三维变换**每帧**都会与 AR 系统 （VisionKit） 同步。
由 xr-frame 提供 3D 渲染能力，由 VisionKit 提供在现实空间坐标系下的**运动跟踪能力**。
平面 AR 跟踪器不能和其他 AR 跟踪器一起使用。
## MegaTracker 是什么
MegaTracker 是连接微信 AR 系统 （VisionKit） 与 Mega 空间计算服务的核心算法组件，由它提供云定位功能。
* **输入**：每一帧 VisionKit 计算出的**在 VisionKit 坐标系下的相机位姿**（即 6DoF 数据） 及 进行 Mega 定位那一帧时的**相机图片**。
* **输出**：当前定位和跟踪的 **Mega Block** 下的相机位姿 。
## MegaTracker 是如何在 xr-frame 上工作的
```
flowchart BT
subgraph Using xr-frame Only
direction BT
PlaneARTracker\_1[PlaneARTracker] -->|MotionData & Image| XRFrame\_1[xr-frame]
end
subgraph Using Mega Plugin
direction BT
PlaneARTracker\_2[PlaneARTracker] -->|MotionData & Image| MegaTracker
MegaTracker -->|CameraTransform| XRFrame\_2[xr-frame]
end
```
* 在微信原生提供的数据流中 xr-frame 的摄像机组件每帧由**平面 AR 追踪器**的结果直接更新。
* 在 Mega 小程序提供的数据流中 **在 VisionKit 坐标系下的相机位姿**（即 6DoF 数据）及定位帧的图片数据会输入给 **MegaTracker**，在云定位和本地计算之后输出当前定位和跟踪的 **Mega Block** 下的相机位姿 ，最终更新 xr-frame 场景中摄像机在 **Mega Block** 节点下的 LocalTransform，此时 **MegaTracker** 接管了摄像机的控制权， xr-frame **不再**根据 AR 追踪器更新摄像机。
**MegaTracker 的运行深度依赖于平面追踪器提供的 6DoF 运动数据**。 因此，在平面追踪器完成初始化并建立稳定的追踪状态前，MegaTracker 无法介入工作。此外，AR 追踪的稳定性受限于环境特征；在遇到大面积无纹理区域（如白墙）、相机长时间遮挡等极端场景时，若微信底层平面追踪发生漂移或丢失，MegaTracker 将因失去可靠的输入源而同步进入失效状态。
## 后续步骤
* [指定 MegaTracker 云服务鉴权方式](tracker-access.html)

---

## 在 xr-frame 微信小程序上播放透明视频
- 章节路径: `wechat/mega/transparent-video.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/transparent-video.html

# 在 xr-frame 微信小程序上播放透明视频
## 开始之前
* 准备需要播放的透明视频：将透明视频上传至文件服务器并获取用于在 xr-frame 中加载的 URL。
* 由于透明视频的播放依赖于替换场景中的贴图，需要事先标注播放透明视频的位置。
需要能够[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
## 什么是透明视频
**透明视频** 是一种为了在不原生支持透明通道的视频编码格式（如 H.264/AVC， H.265/HEVC） 中实现透明背景效果的技术方案。
该方案通过将视频画面的**颜色信息 （RGB）** 和**透明度信息 （Alpha）** 拆分，并按照特定的空间布局拼接到同一帧图像中，从而生成一个带有黑白遮罩的普通视频文件。在播放端，通过图形渲染管线实时采样并将两部分合成，还原出具有透明背景的动态画面。
根据颜色区域与 Alpha 区域的拼接方式，主要分为两种格式：
1. Side-by-Side （SBS）
Side-by-Side 是一种将 RGB 颜色帧与 Alpha 遮罩帧在**水平方向**上并排拼接的格式。通常约定左侧为颜色区域，右侧为对应的灰度 Alpha 区域。
2. Top-by-Bottom （TBB）
Top-by-Bottom 是一种将 RGB 颜色帧与 Alpha 遮罩帧在**垂直方向**上堆叠拼接的格式。通常约定上半部分为颜色区域，下半部分为对应的灰度 Alpha 区域。
## 在 xr-frame 小程序上标注位置播放透明视频
首先加载类型为 `video-texture` 的视频资源。
```
async loadAsset() {
const videoTexture = {
assetId: "fireball",
type: "video-texture",
// 视频资源 URL
src: "url/video-resource.mp4",
options: {
autoPlay: true,
loop: true,
}
};
try {
// 加载 video-texture 类型资源
await scene.assets.loadAsset(videoTexture);
} catch (err) {
console.error(`Failed to load video texture: ${err.message}`);
}
}
```
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRMesh,{})` 创建简单的几何体赋予 `easyar-video-tsbs` 材质， 并修改 `uniform` 为 `u\_baseColorMap:video-{$assetId}`。
> **注意**
`easyar-video-tsbs` 和 `easyar-video-ttbb` 材质的加载，注册，反注册，卸载由 AR Session 控制。
```
handleEmaResult(ema: easyar.ema.v0\_5.Ema) {
const blockHolder: easyar.BlockHolder = session.blockHolder;
ema.blocks.forEach(emaBlock => {
const blockInfo: easyar.BlockInfo = {
id: emaBlock.id
};
// 若 Block 节点不存在，创建 Block 节点
blockHolder.holdBlock(blockInfo, easyarPlugin.toXRFrame(emaBlock.transform));
});
ema.annotations.forEach(annotation => {
if (annotation.type !== mega.EmaV05AnnotationType.Node) {
return;
}
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
const assetInfo = AnnotationMetaData[nodeAnnotation.id as keyof typeof AnnotationMetaData];
let model: xrfs.Element;
if (assetInfo) {
// GLTF 部分
} else {
// 利用内置 Mesh 创建用于渲染的几何体
model = scene.createElement(xrFrameSystem.XRMesh, {
geometry: "cube",
material: "easyar-video-tsbs",
uniforms: "u\_baseColorMap:video-fireball",
});
xrNode.addChild(model);
}
});
}
```
> **注意**
在使用 `video-texture` 时，若控制台出现 `wx.createVideoDecoder with type: 'wemedia' is deprecated` 警告，请忽略。
经与微信官方团队确认，该警告不影响使用。
## 后续步骤
* [完整运行示例工程](fullstart.html)
* [示例工程说明](sample.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)
