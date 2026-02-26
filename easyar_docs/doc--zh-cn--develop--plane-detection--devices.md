---
source: https://www.easyar.cn/doc/zh-cn/develop/plane-detection/devices.html
---

平面检测支持的设备和平台 | EasyAR 文档
**
##### Table of Contents
**
# 平面检测支持的设备和平台
本章节介绍平面检测功能支持的设备硬件要求和支持的开发平台。
## 平面检测支持的设备
平面检测支持 Android，需要设备本身支持 6DoF 的 EasyAR Motion Tracker 开启时才生效。
如果要使用 ARKit 或 ARCore 等平面检测功能，无法通过 EasyAR 单独实现，在 Unity 上可以通过 [AR Foundation](../unity/fundamentals/arfoundation.html) 联合 EasyAR 实现，Native 开发上可以使用自定义相机同时使用 EasyAR 和 ARKit/ARCore。
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上的 Unity 或者原生上使用平面检测功能。需要注意的是是录制 EIF 的设备同样支持运动跟踪功能。
## 延伸阅读
* [运动跟踪与EasyAR其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker支持的设备](../motion-tracking/devices-easyar.html)