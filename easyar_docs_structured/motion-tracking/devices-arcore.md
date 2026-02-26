---
source: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices-arcore.html
original_file: doc--zh-cn--develop--motion-tracking--devices-arcore.md
normalized_at: 2026-02-27
---
# 谷歌 ARCore 与运动跟踪
谷歌的 ARCore 是用于在 Android 上的增强现实引擎。其为部分 Android 机型提供包括运动跟踪在内的多项能力。在 Unity 上为保证最佳效果，在 ARCore 支持的机型上，EasyAR Sense 默认选择 ARCore 的运动跟踪功能而不是 EasyAR 内置的 `Motion Tracker` 功能。
## ARCore 支持的机型和功能
与其他的 [运动跟踪](intro.html) 功能类似，ARCore 需要设备至少具备摄像头、陀螺仪和加速度计，而且经过谷歌标定并认证才可运行。
ARCore 官方支持的机型列表需要查阅 ARCore 官方文档（[中文](https://developers.google.cn/ar/devices?hl=zh-cn) / [English](https://developers.google.com/ar/devices)）。
> **注意**
需要注意的是，在支持机型上，需要安装额外的 `Google Play Services for AR` App 才可以运行 ARCore 功能，在部分机型可能已经预装，部分机型需要用户自行安装。
## 在 EasyAR 中调用 ARCore
在 EasyAR 使用 ARCore，支持的机型并不与官方机型一致, 主要体现在部分官方支持列表内的机型 ARCore 实测效果异常。可以通过 `ARCoreCameraDevice` 的 `isAvailable` 方法判断这些有问题的机型，然后禁用 ARCore。
ARCore 除了运动跟踪之外还支持环境理解、光照估计等功能，使用 EasyAR 运动跟踪仅调用 ARCore 的运动跟踪功能，不支持其他功能。
以下是 ARCore 效果测试异常禁用的机型列表，这些设备通过 `isAvailable` 检查 ARCore 可用性均返回 `False`。
|Brand|Model Name|
|Redmi|Redmi K40|
|Redmi|Redmi K30S Ultra|
|Redmi|Redmi K40 Gaming|
|Redmi|Redmi K40 Pro|
|Redmi|Redmi K50G|
|Redmi|K30 PRO|
|Redmi|Redmi K30 Pro Zoom Edition|
|Redmi|Redmi K40S|
|Redmi|Redmi K30|
|Xiaomi|Mi 10T|
|Xiaomi|Mi 10 Ultra|
|Xiaomi|MI 9|
|Xiaomi|Mi 10 Pro|
|Redmi|Redmi K20|
|Redmi|Redmi K20|
|Xiaomi|Mi 10T Lite|
|Xiaomi|Mi 10i|
|Xiaomi|MI 9 SE|
|Xiaomi|Mi 10 lite 5G|
|Xiaomi|Xiaomi 12X|
|Xiaomi|Mi 9 Lite|
|Redmi|Redmi K20 Pro|
|Redmi|Mi 9T Pro|
|Xiaomi|Mi 10|
|Xiaomi|Mi 10 Lite zoom|
## 延伸阅读
* [运动跟踪 支持的设备](devices.html)
* [EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系](comparison.html)
