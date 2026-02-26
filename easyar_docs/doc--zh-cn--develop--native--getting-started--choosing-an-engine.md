---
source: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/choosing-an-engine.html
---

在进行增强现实开发前选择一款 3D 引擎 | EasyAR 文档
**
##### Table of Contents
**
# 在进行增强现实开发前选择一款 3D 引擎
AR 开发的第一步是选择合适的 3D 引擎，这一章介绍为什么需要 3D 引擎、AR 开发中常见的 3D 引擎及各自优缺点。
## 为什么 AR 需要 3D 引擎
增强现实并不是简单地在相机画面上叠加 2D 或 3D 图像，而是一个实时三维系统，其核心能力可能还包括：
* 真实相机建模
为了渲染的虚拟物体看起来在现实中更真实，需要根据实际相机画面使用的参数（例如内外参，畸变模型等）调整用于渲染的 3D 引擎中的摄像机的投影矩阵。
* 空间坐标系统管理
统一管理设备、环境、AR 内容等之间的位置和姿态，负责世界坐标、相机坐标、设备坐标之间的选择、设置和转换。
* 实时三维渲染
根据实时估计的场景深度或重建的网格实现虚拟物体和环境的真实遮挡效果，根据光照估计算法模拟阴影，实现逼真的虚实融合效果。
* 资源与生命周期管理
管理虚拟的 AR 资源、内容，覆盖其加载、展示、卸载等生命周期管理。
这些能力构成了典型 3D 引擎的核心职责。因此根据具体的项目需求，选择合适的 3D 引擎是快速实现 AR 效果的必要前提之一。
## 常见的 3D 引擎
EasyAR 支持多种 3D 引擎，包括常见的 3D 引擎如 Unity，Unreal 或者原生开发(Native)。 EasyAR 提供 Unity 和 Native 的样例及开发文档。
### Unity
Unity 定位通用实时 3D 引擎， 是当前大多数 AR 开发者的第一选择。Unity 原生支持 Windows/ macOS 以及 iOS / Android / visionOS 等跨平台开发。 Unity 生态成熟，文档与示例完善。
### Native
相较于使用 Unity 等高层封装引擎，直接基于原生图形 API（如 OpenGL、Vulkan、Metal）进行 AR 开发的优势可概括如下：系统依赖少，运行环境可极度精简，可深度定制相机模型及底层算法。原生 API 开发，工程成本和维护成本高，缺乏成熟编辑器与调试工具，迭代效率低，跨平台难度大，不利于产品级快速交付，通常用于一些简单功能的实现。
### Web
Web 无需安装，基于浏览器即可使用，分发和触达成本极低。 天然跨平台，适合快速上线与大规模用户访问。 开发门槛相对较低，前端生态成熟。
目前 Web 在 AR 应用中仍然较为受限，主要体现在性能受浏览器与安全沙箱限制对运动跟踪、遮挡、精确光照等 AR 核心能力支持不足，设备能力访问受限，稳定性和一致性难以保障。
因此 Web AR 适合“轻量展示与营销”，不适合高精度、强交互的复杂 AR 应用。
## 延伸阅读
* [Android Native 快速入门](quickstart-android.html)
* [iOS Native 快速入门](quickstart-ios.html)
* [Windows Native 快速入门](quickstart-windows.html)
* [Unity 快速入门](../../unity/getting-started/quickstart.html)