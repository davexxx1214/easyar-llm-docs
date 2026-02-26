---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_2.html
---

EasyAR Sense 4.2 发行说明 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR Sense 4.2 发行说明
## 4.2.0
2021-01-25
EasyAR Sense 4.2.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + 增加 iOS 不带录屏和视频播放器功能版本，以满足部分应用的 AppStore 隐私政策合规要求
>
> + 增加 MacOS 上的 framework 版本
>
> + FrameRecorder 播放时增加暂停/继续和获取总播放时间、当前播放时间、初始屏幕旋转方向、是否已完成的功能
>
> + 将 Android 的 CameraDevice 实现提取到了 HelloARCustomCamera 示例中，便于进行修改
>
> + 在 Android 的 aar 库中增加了 ProGuard 规则，不再需要手动指定
>
> + 在 MotionTracking 中优化了平面检测，提升了跟踪鲁棒性和重定位能力
>
> + 增加 MotionTracker 标定参数网络更新功能(CalibrationDownloader)
>
> + 增加 MotionTracking 适配机型
>
> + 增加 CameraDeviceSelector.getFocusMode 以在使用 SurfaceTracking 或 MotionTracking 时获得推荐的对焦模式
>
> + 增加 Storage.setAssetDirPath 以设置加载 image target 等文件时的根目录
>
> + 增加 Log.setLogFuncWithScheduler 以在无法或不便保证线程安全时使用自定义日志函数
>
> * Android 平台示例均升级到 Android 11 (API Level 30)目标
>
> * 修复了一些稳定性问题
>