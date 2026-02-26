---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_5.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-4_5.md
normalized_at: 2026-02-27
---
# EasyAR Sense 4.5 发行说明
## 4.5.0
2022-03-04
EasyAR Sense 4.5.0 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 网络相关功能增加超时时间参数(CalibrationDownloader.download、CloudLocalizer.resolve、CloudRecognizer.resolve、SparseSpatialMapManager.host、SparseSpatialMapManager.load)
>
> + Image 增加 pixelWidth 和 pixelHeight 用于支持摄像机图像的 padding
>
> + 增加 MotionTracking 适配机型
>
> - 结束 Android 4.x 支持，最低支持版本为 5.0
>
> - 移除 C++03 接口
>
> - 停止获取 Android Build Serial 以满足 PlayStore Families Policy Requirements
>
> * Recorder、VideoPlayer 和各示例的 OpenGLES 2.0 升级为 3.0
>
> * 升级编译 SDK 的工具版本：XCode 13
>
> * 升级编译 SDK 的工具版本：Android Gradle Plugin 7.0.0，NDK r23
>
> * 升级各示例依赖的工具版本
>
> * 修正 ARCoreCameraDevice 在部分机型上出现的花屏等问题
>
> * 修正 CameraDevice 在 iPhone 上前置摄像头使用 setFocusMode 时崩溃的问题
>
> * 修复了一些稳定性问题
>
