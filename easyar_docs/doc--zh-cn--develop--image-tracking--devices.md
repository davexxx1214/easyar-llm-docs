---
source: https://www.easyar.cn/doc/zh-cn/develop/image-tracking/devices.html
---

设备与平台支持 | EasyAR 文档
**
##### Table of Contents
**
# 设备与平台支持
本篇详细说明平面图像跟踪功能所支持的设备、操作系统、硬件要求，以及该功能同运动跟踪、自定义相机相结合使用时的相关支持情况，帮助开发者评估项目可行性并提前准备软硬件环境。
## 支持的设备和平台
EasyAR Sense 作为跨平台 AR SDK，为平面图像跟踪功能提供了广泛的操作系统和硬件支持。
### 操作系统与版本要求
|设备类型|操作系统版本|备注|
|PC|• Windows 7 及以上
• macOS Catalina 10.15 及以上|N/KN 版 Windows 需安装 Media Feature Pack 以使用相机|
|手机/平板|• Android 5.0 及以上
• iOS 12.0 及以上|包括 HarmonyOS 1.x-4.x|
|XR 头显|• Android
• visionOS 2.0 及以上|详细支持设备及系统要求参考：[头显支持](../headsets/headsets.html#supportlist)|
### CPU 架构支持
|操作系统|支持的 CPU 架构|
|Windows|x86, x86\_64|
|macOS|x86\_64, arm64 (Apple Silicon)|
|Android|armv7a, arm64-v8a|
|iOS|arm64|
### 硬件要求
平面图像跟踪功能**必需相机**，无额外传感器要求。相比其他 AR 功能（如 [表面跟踪](../surface-tracking/intro.html)），该功能对硬件依赖较低，适用于几乎所有设备。
### 兼容性说明
* **Android/iOS 未来版本**
EasyAR Sense 不依赖大量系统 API，因此新发布的 Android/iOS 版本一般可立即支持。
* **64 位架构要求**
自 2019 年起，Google Play Store 要求新提交应用需支持 64 位；中国主流应用商店也已强制执行。EasyAR 同时提供 `armv7a` 和 `arm64-v8a` 的二进制文件。
## 运动融合的设备支持
运动融合（Motion Fusion）指将平面图像跟踪与设备运动跟踪功能相结合，以提升跟踪稳定性或实现更复杂的 AR 交互。虽然平面图像跟踪本身不强制要求运动传感器，但若需启用运动融合功能，需满足以下条件：
### 运动融合硬件要求
* **必需传感器**：加速度计和陀螺仪
* **适用场景**：当目标图像从当前相机视野之中离开之时，利用设备运动数据维持虚拟物体的位姿持续性以保持稳定、连续跟踪
### 平台支持
* **iOS**: 支持 ARKit 的设备。
* **Android**: 支持 ARCore/AR Engine/EasyAR Motion Tracker 的设备。
* **Windows/macOS**: 通常无内置传感器，需外接设备或放弃运动融合。
##### 提示
对于 EasyAR 支持的 [XR 头显设备](../headsets/headsets.html#supportlist)，运动融合功能天然支持。
### 注意事项
* 平面图像跟踪与运动融合可独立使用。若仅需图像识别，无需额外传感器。
* 运动融合的具体机型列表和性能要求，请参考：[运动跟踪支持机型](../motion-tracking/devices.html)。
## 自定义相机的支持
在某些特殊场景下（如特定分辨率/帧率需求、外部视频流接入），开发者可能需要自定义相机。EasyAR 平面图像跟踪功能支持与自定义相机结合使用。
您可以参考 [自定义相机](../cameras/custom-camera.html) 中的内容建立对自定义相机的认识。目前，我们支持在 Unity 和 原生平台进行自定义相机的集成。
### 实现方式与注意事项
针对不同的平台，我们提供了相应的专题页面。
* [Unity 中的自定义相机实现](../unity/cameras/external-frame-source.html)
* [创建图像输入扩展](../unity/cameras/external-image-stream-frame-source.html)
* [创建图像和设备运动数据输入扩展](../unity/cameras/external-device-frame-source.html)
使用自定义相机时，时刻关注以下**关键限制**：
* 自定义相机需确保帧格式（如 YUV/RGB）与 EasyAR 输入要求匹配。
* 会增加开发复杂度，且可能影响性能，建议仅在标准方案无法满足时使用。
* 需自行处理相机权限、生命周期管理和帧同步。
## 最佳实践建议
平面图像跟踪功能对硬件和平台的要求相对宽松，仅需相机即可运行，适合大多数移动设备和桌面系统。开发者需关注 Android 64位打包规范，并在需要运动融合时检查设备支持情况。自定义相机虽可行，但仅建议在标准方案无法满足需求时采用。