---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-compatibility.html
original_file: doc--zh-cn--develop--unity--fundamentals--unity-compatibility.md
normalized_at: 2026-02-27
---
# Unity 兼容性
本文介绍 EasyAR Sense Unity Plugin 所兼容的 Unity 版本和配置要求。
## Unity 版本
EasyAR Sense Unity Plugin 支持 **Unity 2021.3** 或更高版本。
开发 Mega 功能所需的 EasyAR Mega Studio 支持 **Unity 2021.3.30** 或更高版本。
> **提示**
通常来说, EasyAR 不依赖很多变化的 Unity API，所以如果 Unity 发布了新版本，EasyAR Sense Unity Plugin 一般都可以正常使用。
EasyAR Sense Unity Plugin 从版本 4.6.4 开始支持 Unity 6 的 URP 17+ Render Graph。
## 开发平台
|操作系统|操作系统版本|CPU 架构|补充说明|
|**Windows**|7 及以上版本（7/8.1/10/11）|x86, x86\_64|Windows N/KN 版本需要安装 Media Feature Pack 才能使用|
|**macOS**|10.15 及以上版本|x86\_64, arm64||
另外，需要满足对应版本的 [Unity 开发系统要求](https://docs.unity3d.com/Manual/system-requirements.html) 。
## 发布平台
|操作系统|操作系统版本|CPU 架构|补充说明|
|**Windows**|7 及以上版本（7/8.1/10/11）|x86, x86\_64|Windows N/KN 版本需要安装 Media Feature Pack 才能使用|
|**macOS**|10.15 及以上版本|x86\_64, arm64||
|**Android**|5.0 及以上版本|armv7a, arm64-v8a|arm64-v8a 支持需要开启 IL2CPP|
|**鸿蒙（手机端）**|1.0 – 4.x 原生支持
5 以上通过 Android 应用兼容层支持|arm64-v8a||
|**iOS**|12.0 及以上版本|arm64|Architecture 需配置为 ARM64，不支持配置为 Universal|
|**visionOS**|2.0 及以上版本|arm64||
另外，需要满足对应版本的 Unity 的发布平台要求：
* [Windows](https://docs.unity3d.com/Manual/windows-requirements-and-compatibility.html)
* [macOS](https://docs.unity3d.com/Manual/macos-requirements-and-compatibility.html)
* [Android](https://docs.unity3d.com/Manual/android-requirements-and-compatibility.html)
* [iOS](https://docs.unity3d.com/Manual/ios-requirements-and-compatibility.html)
* [visionOS](https://docs.unity3d.com/Manual/visionOS.html)
特殊说明：
* **关于 Mac Apple silicon：**
EasyAR Sense Unity Plugin 支持在 Apple silicon 设备上原生运行，且可以在 Unity 编辑器中正常使用。
由于 Unity 对原生插件支持的 bug，在部分 Unity 版本中，为 *"Apple silicon"* 或 *"Intel 64-bit + Apple silicon"* 构建的应用可能无法正常工作。如果发现应用在 Mac 上无法使用，且显示类似 "Fail to load EasyAR library" 或 "DllNotFoundException: EasyAR assembly" 的错误，建议使用新版本的 Unity 或向 Unity 和 Unity 社区寻求帮助。
* **关于 Android 16 KB 内存页面大小支持：**
EasyAR Sense Unity Plugin 从版本 4000 开始支持具有 16 KB 内存页面大小的设备。
这是 Android 15 中引入的功能。有关该功能的更多信息，请参阅 Android 文档中关于[支持 16 KB 页面大小](https://developer.android.com/guide/practices/page-sizes)的内容。
* **关于 WebGL：**
EasyAR Sense Unity Plugin 不支持 Unity 的 WebGL。
直接使用 EasyAR 云服务接口（比如 [CRS 服务接口](../../cloud-recognition/management.html)）开发的功能可以发布到 Web 平台。
* **关于录屏功能：**
录屏功能仅支持 Android 平台，且需配置 Graphics API 为 OpenGLES2 或 OpenGLES3。
## Graphics API
EasyAR Sense Unity Plugin 直接使用 Unity 的渲染管线，所有 Unity 中可以使用的图形 API 都可以支持。
## Scriptable Render Pipeline
EasyAR Sense Unity Plugin 支持 Universal Render Pipeline (URP) 7.0.0 或更新版本。
EasyAR Sense Unity Plugin 不支持 High Definition Render Pipeline (HDRP)。
> **注意**
**关于 Unity 6 URP 17+ render graph 支持的声明**
EasyAR 支持 Unity 6 URP 17+ render graph，但是 Unity 本身仍存在部分未解决的问题。在遇到异常情形时可以尝试使用 Unity 提供的 [URP 兼容模式](https://docs.unity3d.com/6000.2/Documentation/Manual/urp/compatibility-mode.html) 。
部分问题已经在最新版本的 Unity 中得到解决，建议使用 6.2 及以上版本。
非兼容模式下的已知问题包括：
1. [未解决] 当从 EasyAR 获取相机纹理（类似 ImageTracking\_Coloring3D 示例及 [ARSession 工作流（CameraDevice）](../cameras/sample-camera-device.html) 示例中的使用），在 iOS/Mac 设备上可以观察到视觉故障和伪影。我们已经在纯 Unity 包中复现该问题并报告给了 Unity： [Glitches on iOS with AR Camera Image Rendering (URP 17 render graph)](https://discussions.unity.com/t/glitches-on-ios-with-ar-camera-image-rendering-urp-17-render-graph/1548048) 。问题进展可以关注 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 更新以及 Unity 未来版本的发布日志。
对于所有版本的 Unity 6，可以使用 [部分缓解措施](../../../api/unity/easyar.EasyARSettings.Workaround.html#u_easyar_EasyARSettings_Workaround_URP17RG_IOS_Glitches_Partial)，默认开启。
对于 Unity 6.2 及更新版本，可以将 Universal Render Pipeline Asset 中的 Render Scale 设置为 0.96-1.05 以外的数值来规避这个问题。
2. [Unity 6.2 已修复] Windows DX11 上相机画面会让场景中的物体渲染效果不可预测。在 Unity 6.0 - 6.1 版本中，EasyAR 提供 [规避选项](../../../api/unity/easyar.EasyARSettings.Workaround.html#u_easyar_EasyARSettings_Workaround_URP17RG_DX11_RuinedScene)] 且默认开启。
