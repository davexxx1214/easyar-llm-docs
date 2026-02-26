---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_0.html
---

EasyAR Sense 2.0 发行说明 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR Sense 2.0 发行说明
## 2.0.0
2017-05-29
从 SDK 2.0 版本开始，EasyAR 将有两个产品，EasyAR SDK 和 EasyAR CRS (云识别服务)。EasyAR SDK 将有两个子版本，EasyAR SDK Basic 和 EasyAR SDK Pro。
EasyAR SDK 2.0 Pro 是个全新版本的 SDK，除了拥有 EasyAR SDK Basic 所有功能之外，还有更多激动人心的特性。EasyAR SDK Pro 是收费的 SDK，关于费用定价、付款方式等详细信息可以在 EasyAR 网站上查看。EasyAR SDK Pro 同时提供免费试用，试用期间 APP 每天的启动次数将会受限。
EasyAR SDK Pro 有这些全新特性：
1. 3D 物体跟踪
对日常生活中的常见有纹理 3D 物体进行实时识别与跟踪。
2. SLAM
单目实时 6 自由度相机姿态跟踪。
3. 录屏
高效易用的录屏功能。
EasyAR CRS 是云端图像识别服务，现在已经开放使用，可以在云端动态管理识别图，在 SDK 中使用对应 API 可以使用云服务识别云端存储的识别图，并从云端获取和识别图相关联的数据信息。EasyAR CRS 是收费服务，关于费用定价、付款方式等详细信息可以在 EasyAR 网站上查看。EasyAR CRS 同时提供免费试用，可以零成本测试相关功能。
EasyAR SDK 2.0 Basic 是 EasyAR SDK 1.x 的升级版。这个版本可以免费商用。EasyAR 1.x 的所有功能仍旧可以在这个版本中找到，我们没有添加任何限制或水印。EasyAR SDK 2.0 Basic 有许多改进，主要集中在这几方面：
1. 工作流和 API 改变
EasyAR 处在演化过程中，新的工作流将有更多的灵活性。我们正在完善的 EasyAR 一站式解决方案也将带给 2.0 越来越多的灵活性。这个改变在 Unity API 中表现的并不很明显，不过有些组件的名字已经变化。
2. 全新的编程语言支持
EasyAR SDK 现在导出了纯 C 接口，赋予开发者更大的自由空间。同时我们添加了对很多编程语言的支持，包括 C/C++11/traditional C++/Java for Android/Objective-C for iOS。所有的语言都有一个样例来演示基本的使用方式。我们会在未来的小版本升级中添加更多的语言支持。
3. 云识别支持
EasyAR SDK 现在内置云识别支持。
4. 许多改进、bug 修复和兼容性提升
我们提升了二维码的检测效果，调整了很多 API 以达到更高的灵活度。这个版本修复了许多 bug，包括在部分 Android 机型上显示不正确的问题和一些内存相关的问题。同时我们还提升了 EasyAR SDK 与 AMD CPU 的兼容性以及与 Unity3D、Google VR SDK 等第三方 SDK 的兼容性。
详细更新内容如下：
>
> ++ 全新的编程语言支持：C/C++11/traditional C++/Java for Android/Objective-C for iOS
>
> ++ 所有编程语言和不同 IDE 的 sample
>
> ++ 工作流和 API 变化
>
> ++ 云识别
>
> ++ 3D 跟踪 (pro)
>
> ++ SLAM (pro)
>
> ++ 录屏 (pro)
>
> + SDK API 导出为 C 接口，更容易在所有平台上导入其他语言
>
> + 添加 camera 权限申请 API
>
> + 添加 camera 缩放 API
>
> + 提升二维码检测效果
>
> + 优化内存使用
>
> + Unity: 添加默认的 found/lost 行为
>
> + Windows: DLL 将不再依赖于 CRT
>
> + Windows: 添加两个样例：一个关于如何使用 API，另一个演示在 Qt5 中的集成
>
> + Android: 添加 native 库文件的自定义加载路径和选择性加载支持
>
> - Unity: 删除了大部分非 behaviour API（所有功能被移动到了 behaviour 中）
>
> * 修复对 AMD CPU 的兼容性
>
> * 修复某些情况下渲染 camera 图像导致的 GL 状态污染
>
> * 修复视频播放前的黑色块
>
> * Unity: 修复 Unity 4.x 中 target 加载状态总是返回 true
>
> * Unity: 修复 Unity 5.0.0 和部分其他版本中屏幕闪烁
>
> * Windows: 修复某些情况下窗口关闭时崩溃
>
> * Android: 修复某些情况下调用 close 之后 camera 延迟关闭
>
> * Android: 修复从 native 线程中调用 camera API 崩溃
>
> * Android: 修复内存抖动和频繁 GC
>
> * Android: 修复在某些设备上 camera 的显示
>
> * Android: 修复某些类型 PNG 图像的加载和跟踪问题
>
> * iOS: 修复某些情况下关闭 camera 随机崩溃
>
> * iOS: 修复由于不兼容的 RTTI 配置导致的在与某些 SDK（比如 Google VR SDK）一起使用时出现的未被处理的异常（通常是 domain error）
>
> * iOS: 修复视频播放位置的时间单位
>