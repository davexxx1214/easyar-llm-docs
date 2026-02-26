---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_0.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-4_0.md
normalized_at: 2026-02-27
---
# EasyAR Sense 4.0 发行说明
## 4.0.1
2020-05-13
EasyAR Sense 4.0.1 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + CloudRecognizer 状态回调增加“到达访问额度”状态
>
> + 增加输入帧录制和播放功能，用于调试
>
> + 增加 MotionTracking 适配机型
>
> * 修正 MotionTracking 中的内存泄露问题
>
> * MotionTracking 的相机对焦模式改为自动对焦
>
> * 修正 SparseSpatialMapManager.load 出错时会崩溃的问题
>
> * 修正 Android HelloARMotionTracking 示例摄像机图像不更新的问题
>
> * 修复了一些稳定性问题
>
## 4.0.0
2019-12-30
EasyAR 已经成长为一个大家族，从版本 4 开始，过去被大家熟知的 EasyAR SDK 将被赋予一个新的名字：EasyAR Sense。EasyAR Sense 提供感知真实世界的能力。这个版本包含了所有 3.0 的功能。
EasyAR Sense 是一个独立 SDK，它不依赖于非系统组件或是像 Unity3D 这样的工具，可以提供灵活的基于数据流的组件化 API。
而关于 Unity 的支持，EasyAR Sense Unity Plugin 是一个非常薄的封装，用于在 Unity 中暴露 EasyAR Sense 的功能。EasyAR Sense Unity Plugin 的所有代码经过良好的接口设计且都是开源的。你可以直接使用这个插件来快速创建 AR 体验，也可以参考插件代码来更加灵活和自定义的使用 EasyAR Sense 接口和功能，或是创建属于自己的 Unity 插件。
EasyAR Sense 4.0 带来了这些全新特性：
1. 稀疏空间地图 Sparse Spatial Map
稀疏空间地图提供了扫描物理空间同时生成点云地图并进行实时定位的能力，开发者可以快速基于现实空间创建应用，如 AR 说明书以及 AR 导航导览等。在点云地图上部署的虚拟内容，同时也会被持久化放置在现实空间中，实现虚拟世界和物理世界的连接。此外，多人 AR 互动也能在此基础上实现。
2. 稠密空间地图 Dense Spatial Map
虚拟内容与物理世界产生交互碰撞，AR 体验才更加逼真。EasyAR Sense 4.0 支持实时重建环境的稠密空间地图，可以实现碰撞、遮挡等效果，从而构建更真实的 AR 体验。
3. 运动跟踪 Motion Tracking
提供多传感融合的方式解算位置和姿态，降低了相机运动带来的漂移，让虚拟物体在空间更加稳定。同时提供重定位功能，在跟踪丢失后可以恢复定位。使用运动跟踪的应用，不依赖于 ARCore，也不需要最终用户通过 Google 服务框架安装 ARCore 服务。
4. ARKit/ARCore 支持
支持在 iOS 上使用 ARKit，在 Android 上使用 ARCore，并可以与 EasyAR Sense 的其他功能一起使用。
EasyAR Sense Unity 插件同样获得了巨大提升，主要集中在这几方面：
1. 连贯的设计演化
EasyAR Sense 1/2/3 的 Unity 插件的所有功能和优点都在这个版本中保留了下来。
这个版本的插件尽可能多的使用了 Unity 本身的功能，比如使用 OnEnable/OnDisable 来控制 start/stop。大多数 EasyAR Sense 功能都可以不需要写脚本直接工作。
所有 EasyAR Sense 4.0 的新功能都已经支持，许多 bug 也已经修复。
2. 编辑器体验优化
编辑器中可以显示 image target 的 gizmo，以更好的体验替代过去版本中编辑模式下自动生成的 mesh。
严重错误（比如 license key 验证失败）会通过弹出消息在屏幕上显示，用于帮助 debug。
除 API 外，提供了 Unity 工具窗口来生成 image target data。
3. 更多样例，覆盖更多细节 API
添加了展示所有新功能以及不同算法组合工作的样例。
添加了 AR 眼镜支持的样例，预先标定了两款 AR 眼镜：影创 Action One 及 EPSON BT-350。
社区中许多关于“如何使用”的问题在这些样例中都有解答。感谢大家的反馈！
EasyAR Sense 4.0 提供免费个人版、月付费专业版和定制化功能企业版三种订阅模式。
功能、定价、付款方式等的详细信息可以在 [产品页面](https://www.easyar.cn/view/sdk.html) 及 [价格页面](https://www.easyar.cn/price.html) 了解。
