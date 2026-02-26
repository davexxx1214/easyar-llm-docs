---
source: https://www.easyar.cn/doc/zh-cn/develop/overview.html
---

EasyAR 开发简介 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR 开发简介
EasyAR 让 AR 开发变得简单高效。使用 EasyAR，您可以轻松地将增强现实功能集成到各种平台的应用中。
## EasyAR 产品概览
EasyAR 为 AR 开发提供了三大产品：`EasyAR Mega`、`EasyAR CRS`（Cloud Recognition Service）和 `EasyAR Sense`。
* `EasyAR Mega` 是大场景空间识别定位服务，提供大规模场景和复杂物体的 AR 能力。
* `EasyAR CRS` 是高性能云端图像识别服务，提供传统图像识别 AR 能力。
* `EasyAR Sense` 是增强现实 SDK，提供跨平台的 AR 集成能力。
下图从产品结构上做了细分：
```
`block
columns 1
block:groupTitle
Title["EasyAR 产品结构简图"]
end
block:groupTool
Tool["工作流工具"]
MegaToolbox["Mega Toolbox"]
MegaStudio["Mega Studio"]
space
end
block:groupSDK
SDK["SDK"]
Sense["Sense"]
SenseUnity["Sense&lt;br&gt;Unity Plugin"]
MegaWeChat["Mega&lt;br&gt;WeChat MiniProgram Plugin"]
end
block:groupService
Service["云服务"]
Mega["Mega&lt;br&gt;Service"]
SpatialMap["SpatialMap&lt;br&gt;Service"]
CRS["Cloud Recognition&lt;br&gt;Service"]
end
style groupTitle fill:none,stroke:none,stroke-width:0px
style Title fill:none,stroke:none,stroke-width:0px
style Tool fill:none,stroke:none,stroke-width:0px
style SDK fill:none,stroke:none,stroke-width:0px
style Service fill:none,stroke:none,stroke-width:0px
`
```
* **云服务**提供大规模识别定位能力
* **Mega Service**：`EasyAR Mega` 的核心部件。
* **SpatialMap Service**：为 `EasyAR Sense` 的稀疏空间地图提供云端支持的服务。
* **Cloud Recognition Service**：`EasyAR CRS` 的核心部件。
* **SDK** 提供丰富的本地功能，并利用**云服务**提供更加强大的能力
* **Sense**：`EasyAR Sense` 的核心 SDK。
* **Sense Unity Plugin**： `EasyAR Sense` 的 Unity 插件。
* **Mega WeChat MiniProgram Plugin**：`EasyAR Mega` 的微信小程序插件。
* **工作流工具**提供可视化的管理和测试工具
* **Mega Toolbox**：`EasyAR Mega` 的可视化采集和测试工具。
* **Mega Studio**：`EasyAR Mega` 的可视化编辑和管理工具。
在开发 AR 应用时，可能会同时使用一个或多个产品模块以满足不同场景下的功能需求。
>
> 比如：
>
>
* > 开发涂涂乐应用时，可以使用
**> Sense Unity Plugin
**> 在 Unity 中开发跨平台应用，跟踪图像并渲染 3D 模型。
>
* > 开发 Live 照片应用时，可以使用
**> Sense
**> 开发 Android 和 iOS 原生应用识别跟踪照片并播放视频；或使用
**> Cloud Recognition Service
**> 提供海量照片的云端识别服务，并在微信小程序中直接调用该服务接口实现照片识别功能。
>
* > 开发 AR 导航应用时，可以使用
**> Mega Service
**> 来实现大场景定位；使用
**> Sense Unity Plugin
**> 在 Unity 中调用 EasyAR Mega 的接口和 EasyAR Sense 的运动跟踪功能实现 AR 导航能力；使用
**> Mega Studio
**> 来加载真实世界模型并辅助导航路线的摆放；使用
**> Mega Toolbox
**> 来快速验证定位跟踪效果。
>
>
`EasyAR Mega` 提供了这些 AR 能力，可以用于构建各种手机应用、微信小程序等多种平台的 AR 应用：
* **Mega 固定空间**：适用于 AR 导航、文旅导览、地标秀、大空间游戏等大空间场景。
* **Mega 复杂物体**：适用于 AR 文物讲解、工厂培训、AR 手办特效、车展营销等复杂物体。
`EasyAR CRS` 提供了这些 AR 能力，可以用于构建各种手机应用、微信小程序、Web 应用等多种平台的 AR 应用：
* **图像云识别**：适用于AR 绘本、文创产品、TCG 卡牌、Live 照片等大规模图像识别场景。
`EasyAR Sense` 提供了这些 AR 能力，可以用于构建手机、XR 头显、PC 等多种平台的 AR 应用：
* **运动跟踪**：适用于 AR 空间画笔、远程协作等场景。
* **平面检测**：适用于 AR 商品展示、虚拟装饰等场景。
* **稀疏空间地图（房间级锚点）**：适用于小空间交互和游戏等场景。
* **稠密空间地图（网格化）**：适用于环境交互游戏等场景。
* **表面跟踪（无尺度锚定）**：适用于 AR 空间特效等场景。
* **图像跟踪**：适用于 AR 卡片、涂涂乐、品牌营销等场景。
* **物体跟踪**：适用于 AR 地球仪等场景。
此外，`EasyAR Sense` 可集成并使用以下云端或高级能力：
* **Mega 固定空间**
* **Mega 复杂物体**
* **图像云识别**
## 开发不同平台的 AR 应用
使用 EasyAR 可以在不同平台上开发 AR 应用。
### Unity `（推荐）`
使用 Unity 开发 AR 应用是比较推荐的一种方式。使用 Unity 可以高效地开发跨平台 3D 内容和交互。
![alt text](https://doc-asset.easyar.com/develop/media/unity.png)
使用 Unity 开发的 AR 应用可以使用以下功能：
* `EasyAR Mega` 的全部功能
* `EasyAR CRS` 的全部功能
* `EasyAR Sense` 的全部功能
使用 Unity 开发的 AR 应用可以发布到以下设备和平台：
* Android 手机和平板等设备
* iOS 手机和平板
* 各类 XR 头显
* Windows 电脑
* macOS 电脑
### 微信小程序
在 [微信小程序](https://developers.weixin.qq.com/miniprogram/dev/framework/) 平台上，可以使用 **Mega WeChat MiniProgram Plugin** 或 **Cloud Recognition Service** 接口开发微信 AR 应用。在小程序上，可以使用 [XR-Frame](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/) 进行 3D 渲染和交互开发。另外也可以使用其它 Web 3D 引擎（如 [PlayCanvas](https://playcanvas.com/) 或 [Three.js](https://threejs.org/)）进行开发，但是需要较为复杂的额外适配工作。
![alt text](https://doc-asset.easyar.com/develop/media/wechat.png)
微信小程序平台上的 AR 应用可以使用以下功能：
* `EasyAR Mega` 的全部功能（仅支持 XR-Frame）
* `EasyAR CRS` 的全部功能
* 运动跟踪[1](#fn:1)
* 平面检测[1](#fn:1)
* 图像跟踪[1](#fn:1)（不能与 `EasyAR Mega` 同时使用）
* 物体跟踪[1](#fn:1)（不能与 `EasyAR Mega` 同时使用）
在微信平台上，我们还为 [AR 导航](https://www.sightp.com/nav.html) 和 [AR 文旅](https://www.sightp.com/tourism.html) 提供了成熟的解决方案。如有需求请联系 EasyAR 商务。
### 原生应用
直接使用原生接口开发 AR 应用也是可以的，但并不推荐。主要原因是通常 AR 所需的 3D 内容和交互在不使用 3D 引擎的情况下实现起来比较复杂，且内容制作效率很低。一般只有在绘制简单几何体或播放视频这些简单内容时才建议使用。
![alt text](https://doc-asset.easyar.com/develop/media/native.png)
使用原生接口开发的 AR 应用可以使用以下功能：
* `EasyAR Mega` 的全部功能
* `EasyAR CRS` 的全部功能
* `EasyAR Sense` 的全部功能
使用原生接口开发的 AR 应用可以发布到以下设备和平台：
* Android 手机和平板等设备
* iOS 手机和平板
* 各类 XR 头显[2](#fn:2)
* Windows 电脑
* macOS 电脑
### 搭建自己的 AR 平台
如果您研发了一款 3D 引擎，或是希望在某款 EasyAR 尚未提供支持的 3D 引擎中使用 EasyAR，可以使用 `EasyAR Sense` 的原生 SDK 在您的 3D 引擎中集成 EasyAR 功能。这个过程通常需要较强的 C/C++ 开发经验，以及对 3D 引擎实现的充分理解和控制力。一般来说，我们建议不希望在应用中引入 Unity 的企业考虑这种方式。
使用这种方式搭建的 AR 平台或应用可以使用以下功能：
* `EasyAR Mega` 的全部功能
* `EasyAR CRS` 的全部功能
* `EasyAR Sense` 的全部功能
使用这种方式搭建的 AR 平台或应用可以发布到以下设备和平台：
* Android 手机和平板等设备
* iOS 手机和平板
* 各类 XR 头显[2](#fn:2)
* Windows 电脑
* macOS 电脑
### Unreal
EasyAR 的 Unreal 支持尚处于实验阶段，如有需求可以联系 EasyAR 商务商讨定制开发事宜。
![alt text](https://doc-asset.easyar.com/develop/media/unreal.png)
与此同时，如果您或您的团队有较好的 C/C++ 开发经验，尤其是对 Unreal 引擎渲染管线和插件开发有一定了解，可以考虑使用 `EasyAR Sense` 的原生 SDK 在 Unreal 引擎中集成 EasyAR 功能。
## 从这里开始
* [EasyAR 增强现实入门](getting-started/ar.html)
* [Unity 开发快速入门](unity/getting-started/quickstart.html)
* [微信小程序开发快速入门](wechat/getting-started/quickstart.html)
* [原生开发入门](native/getting-started/choosing-an-engine.html)
* [Web 开发入门](web/getting-started/quickstart.html)
* [初见 Mega](../mega/overview.html)
* [基础组件](fundamentals/fundamentals.html)
* [摄像头和输入扩展](cameras/cameras.html)
* [XR 头显](headsets/headsets.html)
* [输入帧录制和模拟运行](simulation/simulation.html)
* [问题诊断和报告](diagnostics/diagnostics.html)
* [Mega （固定空间和复杂物体）](mega/intro.html)
* [运动跟踪](motion-tracking/intro.html)
* [平面检测](plane-detection/intro.html)
* [稀疏空间地图（房间级空间锚点）](sparse-spatial-mapping/intro.html)
* [稠密空间地图（网格化）](dense-spatial-mapping/intro.html)
* [表面跟踪（无尺度锚定）](surface-tracking/intro.html)
* [图像跟踪](image-tracking/intro.html)
* [图像云识别](cloud-recognition/intro.html)
* [物体跟踪](object-tracking/intro.html)
* [EasyAR Sense 支持的设备和平台](devices-sense.html)
* [EasyAR Mega 支持的设备和平台](mega/devices.html)
* [EasyAR CRS 支持的设备和平台](devices-crs.html)
* [EasyAR 支持的 XR 头显](headsets/headsets.html)
1. 由微信 [VisionKit](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/base.html) 提供支持。[↩](#fnref:1)[↩](#fnref:2)[↩](#fnref:3)[↩](#fnref:4)
2. 要让原生应用支持头显通常还需要设备厂商提供专门的 SDK 支持。除 Apple Vision Pro 外，大部分设备厂商并未在原生 SDK 中公开对接 EasyAR 所需的接口和数据。[↩](#fnref:5)[↩](#fnref:6)