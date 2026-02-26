---
source: https://www.easyar.cn/doc/zh-cn/develop/mega/devices.html
original_file: doc--zh-cn--develop--mega--devices.md
normalized_at: 2026-02-27
---
# 支持的设备和平台应用
EasyAR Mega 旨在提供跨平台的、一致的空间计算体验。为了实现这一目标，我们对不同的设备和平台提供了专门的支持。本章将详细说明 Mega 可以在哪些设备和平台上运行，以及不同设备所能提供的体验区别。
## 设备、平台支持概览
Mega 云定位具备广泛的接入能力，支持各类能获取摄像头图像的设备和平台。支持的情况如下：
|设备类型|操作系统|目标平台|支持情况|
|智能手机/平板|• iOS
• iPadOS
• Android|• Native
• Unity
• 微信小程序|全面支持，几乎覆盖市面所有智能手机/平板|
|XR 头显|• visionOS
• Android XR|• Unity|有限支持，参考 [头显支持](../headsets/headsets.html) 查看具体的设备支持情况|
|PC|• Windows
• macOS|• Native
• Unity|有限支持，仅用于模拟效果预览，参考 [EIF 模拟运行](../../mega/simulation-verification/simulation.html)|
|自定义设备|• Android|• Native
• Unity|有限支持，需要使用 [自定义相机](../cameras/custom-camera.html) 功能，适合深度开发者|
## 不同设备上的体验差异
虽然 Mega 云定位功能广泛支持运行于不同的平台的各种设备，但最终的用户体验还依赖云端定位结果在客户端进行融合跟踪的效果。
根据具体设备与平台的硬件条件及软件能力，我们对不同设备按照 xDoF (x Degrees of Freedom，x 自由度) 的方式进行分类。xDoF 是衡量设备融合跟踪能力的关键指标，它直接影响 Mega 的体验质量。
|设备分类|硬件要求|软件要求|体验等级|
|0DoF|除摄像头外无硬性要求|• 无|**基础**，无终端跟踪能力，虚拟内容只能贴屏显示|
|3DoF|需要有陀螺仪|• EasyAR Sense 4.7.0 及以上|**一般**，受限的终端跟踪能力，体验受到行进方向和速度影响|
|5DoF|需要有陀螺仪和加速度计|• Android 7.0 及以上
• EasyAR Sense 4.7.0 (Lib Full)|**次佳**，一定的终端跟踪能力，但在高度方向上的体验会打折|
|6DoF|需要有良好的 IMU 传感器|支持以下任意：
• Apple ARKit
• Google ARCore
• Huawei AR Engine
• EasyAR Motion Tracker
|**最佳**，完整的终端融合跟踪能力，可以应对用户的各种运动模式|
> **注意**
对于 Apple 设备，是否支持 ARKit 请参考：[ARKit 验证设备支持](https://developer.apple.com/cn/documentation/arkit/verifying_device_support_and_user_permission/)。
对于 Android 设备，是否支持 ARCore 请参考：[支持 ARCore 的设备](https://developers.google.cn/ar/devices)。
对于华为设备，是否支持 AR Engine 请参考：[AR Engine 运动跟踪支持的设备](../motion-tracking/devices-arengine.html)。
对于其他设备，是否支持 EasyAR Motion Tracker 请参考：[EasyAR 运动跟踪支持的设备](../motion-tracking/devices-easyar.html)。
对于 XR 头显设备，目前支持集成 Mega 功能的设备均具备完整的 6DoF 能力。
> **重要事项**
为了保证良好的用户体验，对于使用 EasyAR Motion Tracker 的设备，Mega 功能在运行前会进行自检。具体地，程序会判断 `MotionTrackerCameraDeviceQualityLevel` 的状态：
* ≥ `Limited`：默认 6DoF，可以手动降级成 5DoF、3DoF、0DoF
* < `Limited`：默认 5DoF，可以手动降级成 3DoF、0DoF
相关概念请参考文档：[运动跟踪简介](../motion-tracking/intro.html)。
## 微信小程序的额外说明
在微信小程序内集成 Mega，对设备的要求与原生 或 Unity 开发有所不同。
* 设备需要至少支持 **微信VisionKit V1平面接口** 才能运行。
* 支持 **微信 VisionKit V2 平面接口** 才能获得比较理想的效果。
详细的设备支持列表请参考微信小程序官方文档：[V2平面AR接口支持列表](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)
EasyAR Mega 为主流移动平台提供了开箱即用的支持。在选择目标设备时，请优先考虑支持 ARKit/ARCore/AR Engine/EasyAR Motion Tracker 的机型或特定 XR 头显设备，以确保用户获得最佳的 Mega 空间体验。
