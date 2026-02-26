---
source: https://www.easyar.cn/doc/zh-cn/develop/getting-started/ar.html
---

EasyAR 增强现实入门 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR 增强现实入门
EasyAR Sense 是增强现实（Augmented Reality，AR）引擎，提供感知真实世界的能力。
EasyAR 的核心在于跟踪 （Tracking） 和渲染 （Rendering）。
* 跟踪：计算摄像机在真实世界中的位置和姿态（六自由度，6-DoF），确保虚拟对象稳定附着在目标上。
* 渲染：将 3D 模型、视频、动画等虚拟内容与真实场景融合，支持交互、碰撞和遮挡。
## EasyAR 功能概述
EasyAR 支持多种现实感知和虚实融合的能力，包括已知 2D/3D 目标的图像跟踪或者物体跟踪，以及无需标记物的运动跟踪和表面跟踪等。EasyAR 同时提供大范围的视觉定位和空间计算方案 [EasyAR Mega](../mega/intro.html)。
* EasyAR Mega
端云协同的空间计算技术，持久化的的数字孪生空间，大规模、高精度的室内外定位与虚实遮挡。
* 运动跟踪 (Motion Tracking)
无标记持续跟踪设备在三维空间中的六自由度（6DoF）位置和姿态。
* 稀疏空间地图 (Sparse Spatial Map)
设备端、小范围环境重建和视觉跟踪，小空间多人和持久化体验。
* 稠密空间地图 (Dense Spatial Map)
扫描环境生成实时 3D 网格，支持高级效果如真实碰撞和遮挡。
* 表面跟踪 (Surface Tracking)
实时检测物体表面并跟踪，支持虚拟对象放置在桌面、地面或墙面上。
* 图像跟踪 (Planar Image Tracking)
识别并跟踪平面图像，在图像上叠加虚拟内容。
* 图像云识别 (Cloud Recognition Service, CRS)
云端识别海量的平面图像，可结合本地跟踪。
* 物体跟踪 (Object Tracking)
直接从 OBJ 模型实时生成目标，识别并跟踪真实 3D 对象。
## 开发平台快速入门
EasyAR 支持 Unity, 原生平台（Android/ iOS/ windows/ macOS）， 微信小程序和 Web 平台。根据选定的开发平台，查阅对应的快速入门教程。
* [快速入门](../unity/getting-started/quickstart.html)
* [启用 EasyAR](../unity/getting-started/enable-easyar.html)
* [配置 AR 场景](../unity/getting-started/scene.html)
* [场景中的诊断信息](../unity/getting-started/diagnostics.html)
* [使用 Universal Render Pipeline（URP）](../unity/getting-started/universal-render-pipeline.html)
* [示例启动器使用说明](../unity/getting-started/sample-launcher.html)
* [选择 3D 引擎](../native/getting-started/choosing-an-engine.html)
* 快速入门
* [Android](../native/getting-started/quickstart-android.html)
* [iOS](../native/getting-started/quickstart-ios.html)
* [Windows](../native/getting-started/quickstart-windows.html)
* 启用 EasyAR
* [选择发布变种](../native/getting-started/variants.html)
* [Android](../native/getting-started/enable-easyar-android.html)
* [iOS](../native/getting-started/enable-easyar-ios.html)
* [微信小程序开发指南](../wechat/getting-started/quickstart.html)
* [快速入门](../web/getting-started/quickstart.html)