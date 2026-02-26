---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_3.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-4_3.md
normalized_at: 2026-02-27
---
# EasyAR Sense 4.3 发行说明
## 4.3.0
2021-04-07
EasyAR Sense 4.3.0 增加了一些小功能，修复了一些兼容性问题。
详细更新内容如下：
>
> + 增加 MotionTrackerCameraDevice.getQualityLevel，用于获取设备的 MotionTracking 适配质量
>
> + 增加 MotionTrackerCameraDevice.setTrackingMode，用于支持不同的跟踪模式
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ARCoreCameraDevice 在 Android 11 上的兼容性说明
>
> * 在 MotionTracking 中优化了 hittest
>
> * 在 MotionTracking 中提升了大场景下鲁棒性
>
> * 在 DenseSpatialMap 中减小了 block size，提升 incremental update 的性能
>
> * 升级 XCode 版本到 12，iOS 最低版本到 9.0
>
> * 升级 Android Gradle Plugin 版本到 4.1.0，NDK 到 r22
>
> * 修复 Android 平台上 HelloARRecording 示例对 Android 10 和 Android 11 的兼容性问题
>
> * 修复 Android 平台上 CameraDevice 使用 camera2 时有时候退出时会崩溃的问题
>
> * 修复了一些稳定性问题
>
