---
source: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/devices.html
---

稀疏空间地图支持的设备和平台 | EasyAR 文档
**
##### Table of Contents
**
# 稀疏空间地图支持的设备和平台
本章节介绍稀疏空间地图功能 (Sparse Spatial Map) 支持的设备硬件要求和开发平台。
## 稀疏空间地图支持的设备
稀疏空间地图支持 iOS/Android/鸿蒙以及部分头显平台。硬件上，需要设备本身支持 6DoF 的[运动跟踪](../motion-tracking/intro.html)功能。
稀疏空间地图可用的运动跟踪类型包括：
* EasyAR 运动跟踪（Motion Tracker）
* 谷歌 ARCore
* 苹果 ARKit
* 华为 AR Engine
* 六自由度跟踪能力的头显或眼镜
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上通过 Unity 或者原生使用稀疏空间地图功能。需要注意的是录制 EIF 的设备必须支持运动跟踪功能。
如果您的设备支持运动跟踪功能，可以参照 [自定义相机](../cameras/custom-camera.html) 的方式接入 EasyAR 并使用稀疏空间地图功能。
## 延伸阅读
* [运动跟踪与 EasyAR 其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker支持的设备](../motion-tracking/devices-easyar.html)
* [华为 AR Engine支持的设备](../motion-tracking/devices-arengine.html)