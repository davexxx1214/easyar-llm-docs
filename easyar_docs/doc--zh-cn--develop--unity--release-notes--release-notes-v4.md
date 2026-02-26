---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/release-notes/release-notes-v4.html
---

EasyAR Sense Unity Plugin 版本 4 发行说明 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR Sense Unity Plugin 版本 4 发行说明
##### 注意
最新的 EasyAR Sense Unity Plugin 版本为 4000.0。更多信息请参阅 [发行说明](release-notes.html)。
从版本 4 开始，过去被大家熟知的 EasyAR SDK 被赋予了一个新的名字：EasyAR Sense。EasyAR Sense 提供感知真实世界的能力。在 Unity 上，EasyAR Sense Unity Plugin 提供了一个 EasyAR Sense 的封装，方便开发者在 Unity 中使用 EasyAR Sense 的能力。
## 版本 4.6.5
>
> 发布日期：2024-12-25
>
EasyAR Sense Unity Plugin 4.6.5 绕过了一个可能的 Unity bug。
这将是最后一个支持 Unity 2019、Unity 2020 以及 AR Foundation 4 的发布版本。从 4.7 版本开始，EasyAR Sense Unity Plugin 将只支持 Unity 2021.3+ 以及 AR Foundation 5+。众多头显和眼镜的支持也将同步到来。
详细更新内容如下：
* 🩹 绕过一个可能的 Unity 6 URP 17 render graph bug，它会使 Windows DX11 上的渲染效果变得不可预测
## 版本 4.6.4
>
> 发布日期：2024-12-17
>
EasyAR Sense Unity Plugin 4.6.4 修复了稠密空间地图的显示问题，并提供 Unity 6+、URP 17+ 及 AR Foundation 5/6+ 的兼容性。
详细更新内容如下：
* ✨ 添加 Unity 6（URP 17+）的 Render Graph 支持
* ✨ 添加 AR Foundation 5/6 的 XROrigin 支持
* 🐛 修复使用稠密空间地图时的网格撕裂问题
* 🐛 修复使用稠密空间地图时生成的碰撞网格出现的错误日志
## 版本 4.6.3
>
> 发布日期：2023-10-13
>
EasyAR Sense Unity Plugin 4.6.3 修复了几个问题，并提供在 Unity 2023 中使用 URP 时的兼容性问题。
详细更新内容如下：
* ✨ 添加 URP 15 兼容性
* 🐛 修复仅使用 AR Engine 时相机朝向错误的方向
## 版本 4.6.2
>
> 发布日期：2023-04-03
>
EasyAR Sense Unity Plugin 4.6.2 修复了一些 bug。
详细更新内容如下：
* 🐛 修复线性色彩空间下稠密空间地图 mesh 的显示问题
* 🩹 解决（workaround）Camera\_CustomCamera 样例在 Unity 2022.2 和 2023.1（可能还有其它版本）中 Android 上可能崩溃的问题，看上去 Unity 的 JNI 部分在这些版本中存在 bug
## 版本 4.6.1
>
> 发布日期：2023-03-24
>
EasyAR Sense Unity Plugin 4.6.1 增加了一些小功能，修复了一些 bug。
详细更新内容如下：
* ⬆️ 更新 Sense 到 4.6.1.10366
* 🐛 修复稠密 mesh 在某些特殊情况下使用自定义相机时显示位置不对的问题
## 版本 4.6.0
>
> 发布日期：2023-02-13
>
EasyAR Sense Unity Plugin 4.6.0 带来了许多优化和改进，主要集中在这几方面：
1. 添加原生 Apple silicon 支持
我们从 EasyAR Sense 4.3 开始发布了 Apple silicon 的库文件。但在 Unity 自己支持之前，我们并没有办法让 Unity 认识这个库。在这个新的发布版中，我们将这个库文件引入 Unity 中，以支持最近一些为 Apple silicon 编译的 Unity 编辑器版本。
2. 添加内建 AR Engine 支持
我们在插件中添加了内建的 AR Engine 支持，可以使用用以支持 EasyAR Mega 和其它 EasyAR 功能的能力。这个改动用于替换华为老旧的 Unity 包，它在新的 Unity 版本中无法使用。如果您不希望使用 AR Engine，也可以很方便地关闭。
3. 拆分 AR Foundation 和 Nreal 支持到独立的扩展包
我们将 AR Foundation 和 Nreal 支持从主体插件包中拆了出来并做成了扩展包。这两个功能最初是通过使用条件编译加入插件包的。但是 Unity 对条件编译的支持并不非常完美，从而给开发者带来了很多障碍。将它们拆成扩展包的同时也可以让眼镜等设备支持的分发变得更加容易。今后会有许多使用 EasyAR 的新设备。
详细更新内容如下：
* ✨ 添加原生 Apple silicon 支持
* ✨ 添加内建 AR Engine 支持（所有 Unity 版本可用）
* 🚚 拆分和优化 Nreal（&gt;= 1.6）支持
* 🚚 拆分和优化 AR Foundation（&gt;= 4.1.3）支持
* ✨ 添加对 AR Foundation 5.x 包结构的兼容性
* ✨ 添加 UnityPackage 类用于在脚本中更方便地获取包版本和名字等
* ✨ 添加关闭所有自定义相机的选项
* ⚡ 优化 EasyAR Mega 支持
* ⚡ 优化没有可用 frame source 时的信息
* ⚡ 优化右键菜单
* ⚡ 切换使用新的运动融合接口
* 🐛 修复在文件不存在时，target 文件加载卡住且不报错
* 🐛 修复某个特殊情况下 frame source 无法使用
* 🔥 删除内置华为官方 Unity 插件支持（官方已不维护）
* 🔥 删除早于 4.4 版本的废弃接口和 prefab
* 🔥 删除构建 iOS 时 Universal architecture 的支持
* ⬆️ 更新 Sense 到 4.6.0
## 版本 4.5.0
>
> 发布日期：2022-03-04
>
EasyAR Sense Unity Plugin 4.5.0 增加了一些小功能，修复了一些 bug，增强了用户体验。根据 Google 的政策，这个版本将 ARCore SDK 更新至 1.23.0，并且在构建过程中添加了更加严格的检查。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🚚 移动 EasyAR Settings 到 Unity Project Settings，settings asset 将不再以资源形式加载
* ✨ 添加在构建过程校验 license key 的选项
* ✨ 添加支持使用 AR Foundation 及其它一些组件时使用彩色图像输入的选项
* ⚡ 优化在运动跟踪状态不稳定时的运动融合
* ⚡ 优化 CloudRecognizer 或 CloudLocalizer 创建失败的错误信息
* 🐛 修复 MotionTrackerFrameSource.CheckAvailability 在非 active 的 GameObject 上无法结束的问题
* ⬆️ ARCore：更新 ARCore SDK 至 1.23.0
* ⬆️ ARCore：在使用 ARCore 的构建中，Gradle 版本必需 &gt;= 5.6.4
* 🔧 ARCore：使用 ARCore 的构建中，如果打包仅含 32 位的应用将会弹出警告信息
* ⬆️ 更新 Sense 到 4.5.0
**EasyAR Sense Unity Plugin Samples**
* 🔧 在融合样例中关闭 AR Foundation 的更新尝试
* 🔧 修改 ImageTracking\_CloudRecognition 样例，以更好的使用连接超时参数
## 版本 4.4.0
>
> 发布日期：2021-10-28
>
EasyAR Sense Unity Plugin 4.4.0 增加了许多新功能和改进，主要集中在这几方面：
1. 支持 Unity AR Foundation
EasyAR 现在可以与 AR Foundation 协同工作，这增强了 EasyAR 与 AR Foundation 双方的能力，可以同时获得双方的优势。比如，在现实环境中使用 EasyAR 稀疏空间地图定位设备的同时，可以利用 AR Foundation 暴露的 ARKit 或 ARCore 的能力，比如环境探针。
AR Foundation 支持是通过插件底层 EasyAR Sense 的灵活功能之一，自定义相机实现的。以此作为参考，现在可以比以往更容易地自定义插件来支持其它 AR 框架。
2. 支持 Nreal 眼镜（带有 VIO 能力的 AR 眼镜）
EasyAR 现在可以支持 Nreal 眼镜。Nreal 支持是通过插件底层 EasyAR Sense 的灵活功能之一，自定义相机实现的。
3. 支持 Unity 通用渲染管线（Universal Render Pipeline）
从这个版本开始，URP 支持将会内置在插件中。
4. 支持 EasyAR Cloud SpatialMap
EasyAR Cloud SpatialMap 提供城市级 AR 云方案。EasyAR Sense Unity Plugin 是在应用端支撑 EasyAR Cloud SpatialMap 的重要开发工具之一。
5. 新增运动融合功能
只要任意一种运动跟踪功能可以使用，EasyAR 运动融合就可以让静止图像和物体的跟踪更加稳定，并且可以在目标离开相机视野之后继续跟踪。这个新功能不是像在之前版本中可以做到的那样简单的同时运行运动跟踪和图像跟踪，而是在融合两个跟踪的基础上提供了更优的跟踪结果。
6. 全新的 AR Session 创建流程
AR session 及其它 AR 组件的创建现在可以使用 GameObject 菜单完成，使用更加灵活方便。Prefab 已经标记为过时，并将在将来的发布中删除。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🚀 添加 Unity AR Foundation 支持
* 🚀 添加 Unity 通用渲染管线（URP）支持
* 🚀 添加 Nreal 眼镜支持
* 🚀 添加运动融合功能，在运动跟踪可用的时候优化图像和 3D 物体跟踪
* 🚀 添加 `CloudSpatialMapLocalizerFrameFilter` 以支持 EasyAR Cloud SpatialMap
* 🚀 引入创建 AR session 和其它 AR 组件的新方法
* ✨ 添加以功能组织的 GameObject 菜单项，用于创建 AR session 和其它 GameObject
* ✨ 添加许多有用的 GameObject 预设菜单项
* 🔥 prefab 已经标记为过时，并将在将来的发布中删除
* ✨ 添加更多 frame source 以扩展 AR 框架和设备支持
* ✨ 添加 `ARCoreFrameSource` &amp; `ARKitFrameSource` &amp; `MotionTrackerFrameSource` 以替换 `VIOCameraDeviceUnion`，运行时的策略选择由更灵活的 `ARComponentPicker` 替换
* ✨ 添加 `ARFoundationFrameSource` 以支持 Unity AR Foundation
* ✨ 添加 `HuaweiAREngineFrameSource` 以支持华为 AR Engine
* 🔥 `VIOCameraDeviceUnion` 已经标记为过时，并将在将来的发布中删除
* 🚚 `VideoCameraDevice` 重命名为 `CameraDeviceFrameSource`
* 🚚 `RenderCamera` 被移动到了 `FrameSource` GameObject 上
* 🔧 AR session 中的 `Camera` 会由 `FrameSource` 在运行时进行选择
* 🔧 `MotionTrackerFrameSource` 默认会尝试从服务器更新设备支持列表，超时时间为 2s
* ✨ `ARCoreFrameSource` &amp; `ARKitFrameSource` 获得了可以控制自动对焦开关的能力
* ✨ 优化 AR session 工作量和接口
* ✨ 添加 `ARComponentPicker` 组件来在运行时挑选可用的 frame source 及其它组件
* ✨ 添加 `ARSession.AvailableCenterMode` 以查询在一个 session 中所有可用的中心模式
* ✨ 添加 `ARSession.Origin` 以获取在运动跟踪功能在运行时，相机运动的相对物体
* ✨ 添加 `ARSession.TrackingStatus` 以获取设备运动跟踪质量
* ✨ 添加 `ARSession.State` &amp; `ARSession.StateChanged` 以查询 ARSession 的状态
* ✨ 优化中心模式处理
* 🔧 一个 session 中可用的中心模式将由运行时选择的 frame source 来决定
* 🔧 空间地图可用在所有中心模式下使用
* 🔥 删除 `ARCenterMode.ExternalControl`，其功能被 `FrameSource.IsCameraUnderControl` == `false` 所替代
* 🚚 重命名 `ARCenterMode.WorldRoot` 为 `ARCenterMode.SessionOrigin`
* ✨ 优化初始化过程，尤其是首次使用体验
* ✨ 添加 `EasyARController.Initialize` &amp; `EasyARController.Deinitialize` 接口以在启动后支持手动初始化
* 🔧 如果 EasyAR 库文件未加载成功，会由错误提示
* 🔧 改善许可证校验失败的弹出信息
* ✨ 优化构建过程，尤其是首次使用体验
* ✨ 如果插件包未由 Unity 包管理器正确导入，将会生成编译时和加载时错误
* ✨ 在 pre-build 或 post-build 过程中如果出错，构建将会失败
* ✨ 在使用 ARCore XR Plugin 的时候，ARCore SDK 的选择默认将会自动处理
* ✨ 添加在构建中检查 iOS usage description 的功能
* 🔧 构建中将不再使用 `Assets/HiddenEasyAR`
* ⚡ 优化稀疏空间地图的跟踪稳定性
* 🔧 `SurfaceTrackerFrameFilter` 可用与运动跟踪设备一同使用
* 🐛 修复在某些情况下， target controller 事件可能会在组件销毁后触发的问题
* 🐛 修复 `MotionTrackerCameraDevice` 的跟踪模式未正确设置
* 🔧 相机的 `field of view` 现在将被设置成与投影矩阵一致
* ⬆️ 更新 Sense 到 4.4.0
**EasyAR Sense Unity Plugin Samples**
* ✨ 添加新样例 `ARFoundation` 以展示结合 Unity AR Foundation 的使用
* ✨ 添加新样例 `HuaweiAREngine` 以展示结合华为 AR Engine 的使用
* ✨ 添加新样例 `Eyewear\_Nreal\_SpatialMap\_Building` 以展示如何在 Nreal 眼镜上使用空间地图
* ✨ 添加新样例 `Eyewear\_Nreal\_ImageTracking\_InWorld` 以展示如何在 Nreal 眼镜上使用图像跟踪
* ✨ 添加新样例 `MotionTracking\_Fusion` 以展示在单一场景中启动时自动选择以及运行时手动切换可用的 frame sources，以支持最多的设备并在支持的设备上启用每个 AR 框架的独有功能
* 🔧 修改 `FrameRecording` 样例以在运动跟踪功能可用时自动录制运动跟踪 session
* 🚚 重命名样例 `ImageTracking\_MotionExtend` 为 `ImageTracking\_MotionFusion` 以展示新的运动融合功能
* 🚚 重命名样例 `Eyewear\_ImageTracking` 为 `Eyewear\_DeviceHasNoTracking` 以明确样例的用途
* 🚚 重命名样例 `MapLocalizing\_Sparse` 为 `SpatialMap\_Sparse\_Localizing`
* 🚚 重命名样例 `SpatialMap\_Dense\_BallGame` 为 `SpatialMap\_Dense\_BallGame`
* 🚚 重命名样例 `SpatialMap\_Sparse\_ImageTarget` 为 `SpatialMap\_Sparse\_ImageTarget`
* 🚚 重命名样例 `MapBuilding\_Sparse` 为 `SpatialMap\_Sparse\_Building`
* 🚚 重命名样例 `MapBuilding\_Sparse\_Dense` 为 `SpatialMap\_Sparse\_Dense\_Building`
## 版本 4.3.0
>
> 发布日期：2021-04-07
>
EasyAR Sense Unity Plugin 4.3.0 使用 [Unity package](https://docs.unity3d.com/Manual/Packages.html) 组织文件，简化了打包过程中的配置，解决了插件更新难的问题。从这个版本开始，仅支持 Unity 2019.4 及更高版本。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🚀 使用 Unity Package 替换 Asset Package，兼容 Unity 2019.4 及以上版本，老版本不再兼容
* ✨ iOS：自动配置 bitcode，不再需要修改 XCode 工程的 bitcode 设置
* ✨ iOS：使用 Sense 的动态库 framework，不再需要修改 XCode 工程的 framework 设置
* ✨ Android：使用 Sense 的 aar 文件，包含 proguard rule
* ✨ Android：不再使用 Plugins 文件夹中的 Android Manifest，可以根据使用的功能控制 Manifest 中的权限设置
* ⬆️ ARCore：替换随插件分发的 ARCore SDK 为官方 ARCore SDK 1.6 版本的 aar 文件
* ✨ ARCore：添加控制 ARCore 使用的选项，解决与 AR Foundation 的冲突
* 🔧 合并菜单项
* ⬆️ 更新 Sense 到 4.3.0
**EasyAR Sense Unity Plugin Samples**
* 🔥 删除为老版本 Unity 准备的视频播放 workaround
* 🐛 修复 custom camera sample 在某些 Android 设备上无法打开 camera
## 版本 4.2.0
>
> 发布日期：2021-01-25
>
EasyAR Sense Unity Plugin 4.2.0 增加了 InputFrameRecorder/InpuptFramePlayer 支持，可以用于在编辑器中测试和调试设备上的运行效果。同时修复了一些 bug，增强了用户体验。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* ✨ 添加 InputFrameRecorder/InpuptFramePlayer 支持
* ✨ 运动跟踪标定参数默认会从服务器更新
* 🚚 重新组织文件
* ⚡ 简化 hit test 调用
* 🐛 修复 tracker 销毁后 target 不会丢失
* 🐛 修复某些情况下相机图像旋转 180 度
* 🐛 修复线性颜色空间下相机图像色彩
* ⬆️ 更新 Sense 到 4.2.0
**EasyAR Sense Unity Plugin Samples**
* ✨ 添加 FrameRecording sample 以演示 InputFrameRecorder/InpuptFramePlayer 的使用
* ⚡ 优化运动跟踪 sample 的平面检测
## 版本 4.1.0
>
> 发布日期：2020-07-16
>
EasyAR Sense Unity Plugin 4.1.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* ✨ 插件脚本中添加完整的文档
* ✨ 插件详细的使用说明和样例解析文档上线
* ♻️ 重写 CloudLocalizerFrameFilter 以支持单次扫描
* 🐛 修复当 camera 图像使用 ARHorizontalFlipMode.World 进行翻转时 invert culling 对场景中其它相机的污染
* 🐛 修复高 dpi 显示器上 image target gizmo 的显示问题
* 🐛 修复 RGB/RGBA 像素类型的 camera 图像旋转
* ⬆️ 更新 Sense 到 4.1.0
**EasyAR Sense Unity Plugin Samples**
* ♻️ 重写 MotionTracking sample，演示运动跟踪的平面检测功能
* ♻️ 重写 ImageTracking\_CloudRecognition sample，使用新的接口功能
* 🔧 修改 ImageTracking\_Targets sample，使用水平和垂直摆放的 image target
## 版本 4.0.1
>
> 发布日期：2020-05-13
>
EasyAR Sense Unity Plugin 4.0.1 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🐛 小修复
* ⬆️ 更新 Sense 到 4.0.1
**EasyAR Sense Unity Plugin Samples**
* ♻️ 重写 TargetOnTheFly sample，更加简洁和稳定
## 版本 4.0.0
>
> 发布日期：2019-12-30
>
EasyAR 已经成长为一个大家族，从版本 4 开始，过去被大家熟知的 EasyAR SDK 将被赋予一个新的名字：EasyAR Sense。EasyAR Sense 提供感知真实世界的能力。这个版本包含了所有 3.0 的功能。
EasyAR Sense 是一个独立 SDK，它不依赖于非系统组件或是像 Unity3D 这样的工具，可以提供灵活的基于数据流的组件化 API。
而关于 Unity 的支持，EasyAR Sense Unity Plugin 是一个非常薄的封装，用于在 Unity 中暴露 EasyAR Sense 的功能。EasyAR Sense Unity Plugin 的所有代码经过良好的接口设计且都是开源的。您可以直接使用这个插件来快速创建 AR 体验，也可以参考插件代码来更加灵活和自定义的使用 EasyAR Sense 接口和功能，或是创建属于自己的 Unity 插件。
EasyAR Sense Unity 插件获得了巨大提升，主要集中在这几方面：
1. 连贯的设计演化
EasyAR Sense 1/2/3 的 Unity 插件的所有功能和优点都在这个版本中保留了下来。
这个版本的插件尽可能多的使用了 Unity 本身的功能，比如使用 OnEnable/OnDisable 来控制 start/stop。大多数 EasyAR Sense 功能都可以不需要写脚本直接工作。
所有 EasyAR Sense 4.0 的新功能都已经支持，许多 bug 也已经修复。
2. 编辑器体验优化
编辑器中可以显示 image target 的 gizmo，以更好的体验替代过去版本中编辑模式下自动生成的 mesh。
严重错误（比如 license key 验证失败）会通过弹出消息在屏幕上显示，用于帮助 debug。
除 API外，提供了 Unity 工具窗口来生成 image target data。
3. 更多样例，覆盖更多细节 API
添加了展示所有新功能以及不同算法组合工作的样例。
添加了 AR 眼镜支持的样例，预先标定了两款 AR 眼镜：影创 Action One 及 EPSON BT-350。
社区中许多关于“如何使用”的问题在这些样例中都有解答。感谢大家的反馈！
EasyAR Sense 4.0 提供免费个人版、月付费专业版和定制化功能企业版三种订阅模式。
功能、定价、付款方式等的详细信息可以在 [产品页面](https://www.easyar.cn/view/sdk.html) 及 [价格页面](https://www.easyar.cn/price.html) 了解。
详细更新内容如下：
**Unity Plugin for EasyAR Sense 4.0.0**
* 🚀 支持 EasyAR Sense 4.0.0 的所有新功能: 稀疏空间地图、稠密空间地图以及运动跟踪
* 🚀 恢复类似 Sense 2.3 的接口设计和行为，并有非常多改进
* ✨ 添加严重出错情况的弹出消息（可在 EasyARController 上关闭）
* ✨ Components: 大多数组件可以使用 Unity 组件的 enabled 来控制 start/stop
* ✨ Component ARSenssion: AR 入口，控制 center mode，具备支持外部设备的能力，比如自定义相机及 AR 眼镜
* ✨ Component ARAssembly: 展示 EasyAR Sense 组件化 API 的组装过程，支持所有 EasyAR Sense 的组件
* ✨ Component ImageTargetController: 改善对不同类型输入的支持，可以从本地文件系统或 web URL 加载图像和 .etd 文件
* ✨ Component CameraImageRenderer: camera 图像渲染可由 disable 该组件来关闭
* ✨ Component VIOCameraDeviceUnion: 运动跟踪，可自动选取使用设备可用的 ARKit、ARCore 或 EasyAR 运动跟踪功能
* ✨ Scene: 添加 target gizmo，可在 Unity 编辑器中显示 target 细节
* ✨ Asset: 添加全局服务配置及 gizmo 控制选项
* ✨ Window: 添加生成 image target data（.etd 文件）的窗口
* ✨ Window: 添加菜单跳转到 license key 设置界面和其他全局配置
* 🐛 修复目标跟踪存在一帧延迟的问题
* 🐛 修复阻塞式 target 加载，减少 target 加载时间
* 🐛 修复 target size 获取
* 🐛 许多其他改进及 bug 修复
* ⬆️ 更新 Sense 到 4.0.0
**Samples of Unity Plugin for EasyAR Sense 4.0.0**
* 🚀 添加许多 sample，展示 Sense 功能及接口使用
* 🚀 添加回所有 Sense 2.3 的 sample
* 🚀 添加展示新功能的 sample，包括稀疏空间地图、稠密空间地图以及运动跟踪，还有这些功能如何与图像跟踪等其他组件同时使用的 sample
* ✨ 添加 sample 启动器，可以通过启动器加载所有 samples
* ✨ 添加屏幕上显示的组件状态信息，覆盖所有 sample
* ✨ 添加展示 AR 眼镜支持的 sample
* ✨ 添加表面跟踪与图像跟踪同时使用的 sample
* ✨ 添加获取 camera 图像贴图和控制 camera 显示的 sample
* ✨ 添加修改视频 aspect ratio （Unity VideoPlayer 功能） 适配 image target 的 sample
* ✨ 添加展示从图像扩展跟踪的 sample
* ♻️ 云识别 sample 现在使用本地缓存，并在跟踪状态下停止云端识别，以覆盖常见的使用场景
* 🐛 优化 coloring3D sample，修复 bug