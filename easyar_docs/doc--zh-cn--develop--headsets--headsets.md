---
source: https://www.easyar.cn/doc/zh-cn/develop/headsets/headsets.html
---

EasyAR 的头显支持 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR 的头显支持
EasyAR SDK 提供了强大的跨平台 AR 功能，其设计理念同样适用于新兴的空间计算设备——头显（Headset）。本篇将介绍 EasyAR 如何支持头显设备，以及开发者可以如何利用这些功能来构建沉浸式体验。
## 术语说明
在本文档中，“头显”或 “Headset” 特指一类具备头部佩戴形态、支持沉浸式或透视式交互的计算设备，它们能够将虚拟内容呈现在用户眼前，实现增强现实（AR）或混合现实（MR）体验。这包括：
* **光学透视型头显 (Optical See-Through, OST)**：通过半透明镜片直接观看现实世界
* **视频透视型头显 (Video See-Through, VST)**：通过摄像头捕捉现实世界并以视频流的形式观看
## 头显的基本工作原理
为了更好地理解 EasyAR 对头显的支持原理，我们首先需要了解头显设备的基本工作流程：
1. **环境感知**：通过内置的多摄像头、深度传感器（如 iToF）和惯性测量单元（IMU）等，实时感知周围环境的几何结构、光照条件和物体表面。
2. **空间计算**：根据传感器数据，通过 SLAM 系统实时跟踪用户头部 6DoF 位姿（位置 + 朝向）。
3. **内容渲染与显示**：将 3D 内容（如模型、特效）根据设备位姿进行渲染，并将渲染结果投射到显示屏上。对于 VR 模式，显示的是纯虚拟画面；对于 AR/MR 模式，虚拟画面会与真实环境（VST 摄像头画面或 OST 透视背景）进行合成。
4. **交互系统**：通过手柄、手势识别、语音或眼球跟踪，接收用户指令并作出响应。
## EasyAR 支持头显的原理
EasyAR不替代头显原生的空间跟踪或渲染管线，而是以**空间计算增强**的角色与其协同工作。作为专业的 AR 算法引擎，提供多种 AR 场景的空间感知和计算能力，与设备原有的系统进行高效协同。
|职责范围|角色分工|
|头部 6DOF 跟踪、显示渲染、基础交互等|头显原生 SDK/运行时|
|图像/物体识别与跟踪、大空间定位等高级感知能力|EasyAR SDK|
EasyAR SDK 提供图像/物体识别、稀疏重建、稠密重建、大空间定位等世界感知的核心 AR 功能，负责“看懂”世界，并告诉头显的应用程序虚拟内容应该放在哪里。
EasyAR SDK 作为插件或库集成到头显的应用开发框架中（通常是 Unity或 Unreal）。它接收来自设备系统的原始数据流，进行处理和计算，然后输出一个相对于设备空间坐标系的位姿矩阵，最终由头显引擎的渲染管线将虚拟物体绘制在正确的位置。
## 支持情况与实现方式
EasyAR 对主流的头显开发平台提供了全面的支持，主要通过以下两种方式实现：
* **通过 Unity/Unreal Engine**：这是最主流和推荐的方式。头显厂商通常会提供专门的 Unity/Unreal 插件或 XR SDK。EasyAR 可以无缝接入厂商的 SDK 中使用。
* **通过原生平台 (Native)**：对于需要极致性能或特定原生开发的场景，可以使用 EasyAR 的 C++/Java/Objective-C 原生接口。这通常需要开发者自行处理与设备底层数据的接口对接。
EasyAR 已经在多个主流头显平台上通过 Unity 的方式进行了测试和验证。目前已经确认支持的设备如下：
|头显设备型号|系统/SDK 版本要求|
|Apple Vision Pro|visionOS 2 或更新版本|
|PICO 4 Ultra Enterprise|PICO Unity Integration SDK 3.1.0 或更新版本|
|Rokid AR Studio|Rokid Unity OpenXR Plugin 3.0.3 或更新版本|
|XREAL Air2 Ultra|XREAL SDK 3.1 或更新版本|
|Xrany X1|Xrany元霓 SDK|
##### 注意
Rokid AR Studio 可通过 Rokid Unity OpenXR Plugin 支持 Rokid UXR 3，但建议使用 XR Interaction Toolkit，尤其是跨设备使用。
##### 重要事项
Apple Vision Pro、PICO、XREAL 都需要其对应的企业授权才能使用，如有疑问请联系商务。
* 受 Apple Vision Pro 接口授权限制，仅支持获取了 Apple 企业 API 许可的设备。
* 受 PICO 接口授权限制，仅支持 PICO 企业版设备。
* 受 XREAL 接口授权限制，仅支持获取了企业授权的设备。
对于上述没有提及的其他厂商的头显设备，EasyAR 提供了自定义相机等的扩展接入方式。具体可以参考 [创建EasyAR头显扩展包](../unity/headsets/extension.html) 来进行接入，您可以自行完成对接。
这通常涉及以下步骤：
1. **获取设备开发权限**：申请目标头显的开发者账号和 SDK 文档。
2. **获取传感器数据流**：从设备 SDK 中获取摄像头图像（视频帧）、相机参数等必要数据。
3. **调用 EasyAR API**：使用 EasyAR 的底层 API，将获取到的传感器数据送入 EasyAR `FrameSource` 进行处理。
4. **获取并应用计算结果**：从 EasyAR 引擎中获取计算结果（相机位姿），并将其应用到您的 3D 渲染引擎中。
我们提供了详细的开发指南和示例代码，以帮助您完成这一过程。如果您在对接过程中遇到问题，欢迎在我们的开发者社区寻求技术支持。
## 可供使用的核心功能
在头显设备上，您可以充分利用 EasyAR 的全功能矩阵来构建丰富的空间应用：
* **平面图像跟踪**：识别并跟踪预设的图片，将动态视频或 3D 模型叠加在图片之上。
* **3D物体跟踪**：识别并跟踪预设的 3D 模型（如玩具、产品包装盒），并让虚拟内容与之互动。
* **稀疏空间地图**：扫描周围环境生成三维视觉地图，并提供视觉定位与跟踪功能。生成的地图可以保存或在多个设备间实时共享。
* **稠密空间地图**：扫描并生成周围环境的稠密点云地图和网格模型（Mesh），实现虚拟物体与真实物体的物理遮挡关系，极大地增强沉浸感。
* **云端图像识别**：连接 EasyAR 云端数据库，实现海量图片的识别与管理，适用于展览、教育等场景。
* **Mega 大空间定位**：城市级空间计算方案，连接 EasyAR 云定位服务，实现稳定、快速、精准的定位与跟踪，极大的突破和扩展 AR 体验的范围。
## 平台专用指南
为了帮助您快速上手特定平台，我们准备了详细的多平台集成指南。请点击下方的标签页，查看对应平台的快速入门教程。
* [简介](../unity/headsets/headsets.html)
* [使用头显样例](../unity/headsets/samples.html)
* [启用头显支持](../unity/headsets/enable-headset.html)
* 工程配置
* [Apple Vision Pro工程配置](../unity/headsets/setup-visionpro.html)
* [XREAL工程配置](../unity/headsets/setup-xreal.html)
* [其它Android设备工程配置](../unity/fundamentals/setup-player.html)
* 创建 EasyAR 头显扩展包
* [简介](../unity/headsets/extension.html)
* [为 EasyAR Sense Unity Plugin 写头显扩展](../unity/headsets/extension-imp.html)
* [运行验证（bring-up）头显扩展](../unity/headsets/extension-bring-up.html)
* [发布你的扩展包](../unity/headsets/extension-dist.html)