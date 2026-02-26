---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_1.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-2_1.md
normalized_at: 2026-02-27
---
# EasyAR Sense 2.1 发行说明
## 2.1.0
2017-09-08
EasyAR SDK 2.1.0 增加了一些新特性，并针对使用稳定性做了增强，主要集中在这几方面：
1. 新的编程语言支持。
EasyAR 现在支持使用 iOS 的 Swift 和 Android 的 Kotlin 进行编程。我们同时添加了在 EasyAR SDK 中使用 Swift 和 Kotlin 的样例。
2. Android arm64 支持。
EasyAR SDK 将从 2.1 版本开始添加 Android arm64-v8a 架构的文件。
3. Bug 修复和稳定性增强。
我们修复了一些由 EasyAR SDK 2.0 版本引入的 bug，包括调用 ImageTarget.setupAll 时产生的 local reference table overflow 以及 iOS 11 视频播放失败。我们同时修复了 camera 图像在屏幕上显示色彩失真的一个长期存在的问题。
详细更新内容如下：
>
> + 添加新的编程语言支持：Swift for iOS
>
> + 添加 Android 使用的 arm64-v8a 库文件
>
> + 添加新接口（Buffer），实现在 Android Java API 中访问图像数据
>
> + 添加 Android Kotlin 样例
>
> + 添加 iOS dynamic framework 样例
>
> * All: 所有接口都不会抛出异常
>
> * All: 修复 camera 图像在屏幕显示的色彩失真
>
> * Unity: 修复 iOS Unity 录屏后的系统杂音
>
> * Unity: 如果 OnPreRender 中修改了 RevertBackfacing，会在 OnPostRender 中重置
>
> * Unity: 添加 ObjectTargetBaseBehaviour 中缺失的 LoadList*接口
>
> * Unity: 默认不在 AndroidManifest 中添加音频权限
>
> * Unity: 修改容易产生误导的错误信息，"EasyAR is running on an unsupported graphics device" 改为 "EasyAR is running with an unsupported graphics API"
>
> * Android: Engine API 已经可以替换 cn.easyar.engine.EasyAR。cn.easyar.engine.EasyAR 已经弃用并将在今后版本中移除
>
> * Android: 修复调用 ImageTarget.setupAll 配置大量 target 时可能产生的 local reference table overflow
>
> * Android: 修复在 Android 平板和眼镜上 SLAM 不正常的漂移
>
> * Android: 修复在某些罕见 Android 设备上拒绝 camera 权限导致的崩溃
>
> * Android: 改善在某些罕见 Android 设备上的 camera 分辨率选择策略
>
> * iOS: 修复 iOS 11 视频播放
>
> * iOS: framework 将不会再包含签名
>
> * iOS: 修复在某些设备上的某些分辨率下 camera 显示问题
>
> * iOS: 修复录屏内存泄漏
>
> * Sample: 重命名 Unity 样例代码的文件名和 namespace，划分样例代码和 SDK 的明确边界
>
> * Sample: 删除 HelloARCloud 样例中的本地目标
>
> * Sample: 改善 Android/iOS HelloARQRCode 样例中 QR Code 检测到之后的信息显示
>
> * Sample: 在 iOS Unity 上默认打开 IL2CPP
>
> * 其它修正和完善
>
