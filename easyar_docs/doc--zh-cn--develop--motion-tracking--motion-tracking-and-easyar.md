---
source: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/motion-tracking-and-easyar.html
---

为其他功能提供数据的运动跟踪 | EasyAR 文档
**
##### Table of Contents
**
# 为其他功能提供数据的运动跟踪
运动跟踪是增强现实与环境交互的基础功能之一。运动跟踪组件在提供这项功能的同时可以为其他功能提供输入帧数据，同时具有运动跟踪和摄像头控制的功能。
运动跟踪与 EasyAR 其他功能的关系主要有以下几种情况：
* 部分 EasyAR 的功能必须依赖运动跟踪功能。
* 功能不完全依赖运动跟踪，但是在支持运动跟踪的机型上效果更好。
* 部分功能独立于运动跟踪即可工作。
|EasyAR 功能|是否依赖运动跟踪功能|
|平面检测|是|
|稀疏空间地图|是|
|稠密空间地图|是|
|图片跟踪|否|
|3D 物体识别|否|
|表面跟踪|否|
|EasyAR Mega|否|
##### 注意
EasyAR Mega 功能并不依赖运动跟踪功能，但是在支持运动跟踪功能的设备上可以体验最优的 Mega 效果。
##### 注意
图片跟踪可以不依赖运动跟踪独立运行，也可以联合运动跟踪实现融合跟踪的效果。详情参见 [运动融合|扩展跟踪](../image-tracking/motion-fusion.html)
##### 注意
物体跟踪可以不依赖运动跟踪独立运行，也可以联合运动跟踪实现融合跟踪的效果。详情参见 [运动融合|扩展跟踪](../object-tracking/motion-fusion.html)
## 相关主题
* [运动跟踪](intro.html)
* [摄像头和输入扩展](../cameras/cameras.html)