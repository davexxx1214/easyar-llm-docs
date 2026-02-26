---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_6.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-4_6.md
normalized_at: 2026-02-27
---
# EasyAR Sense 4.6 发行说明
## 4.6.1
2023-03-24
EasyAR Sense 4.6.1 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 增加 MotionTracking 适配机型
>
> * 修正 MotionTrackerCameraDevice 的 hitTestAgainstPointCloud、hitTestAgainstHorizontalPlane、getLocalPointsCloud 无返回结果的问题
>
## 4.6.0
2023-02-13
EasyAR Sense 4.6.0 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 增加 MegaTracker，集成 CloudLocalizer 和 RealTimeCoordinateTransform，下个版本将删除 RealTimeCoordinateTransform
>
> + 增加 CloudLocalizer.resolve 参数以支持辅助邻近位置和指南针读数输入
>
> + 增加 Accelerometer.output 以配合 MegaTracker 输入
>
> + 增加 MotionTrackerCameraDeviceTrackingMode.LargeScale 模式降低大空间跑飞概率
>
> + 增加 MotionTracking 跟踪稳定性
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ImageTracker.setResultPostProcessing、ObjectTracker.setResultPostProcessing、SparseSpatialMap.setResultPoseType 以集成 RealTimeCoordinateTransform 功能
>
> + 增加 ARCore 机型列表以判断设备是否支持 ARCore，HelloARMotionTracking 示例增加 ARCore 下载引导
>
> + 增加 MacOS arm64 的支持
>
> - 移除 iOS armv7 空库
>
> - 结束 iOS 9.x-10.x 支持，最低支持版本为 11.0
>
> - 停止获取 Android SSAID(ANDROID_ID)以满足中国大陆监管要求。请受到影响的用户尽快升级。同时，从 EasyAR Sense 4.6.0 开始，将无法连接按日活计费的 CRS 服务，请迁移到按调用次数计费模式
>
> * 优化 CloudLocalizer 接口，修正对相机旋转方向的处理
>
> * 修改 CloudLocalizerStatus 错误值定义
>
> * 简化 TargetInstance 和 TargetStatus
>
> * 修正 Java binding 中回调的参数没有自动释放的问题
>
> * 升级编译 SDK 的工具版本：Android Gradle Plugin 7.2.0，NDK r25
>
> * 升级编译 SDK 的工具版本：XCode 14
>
> * 修复了一些稳定性问题
>
