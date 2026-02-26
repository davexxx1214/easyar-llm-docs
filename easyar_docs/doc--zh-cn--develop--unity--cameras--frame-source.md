---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source.html
original_file: doc--zh-cn--develop--unity--cameras--frame-source.md
normalized_at: 2026-02-27
---
# Unity 中的摄像头及输入帧数据来源 —— 帧数据源（Frame Source）
帧数据源是 Unity 中摄像头及输入帧数据的提供者。本文介绍了帧数据源的基本概念、类型以及运行时的选取方法。
## 开始之前
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程。
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
## 帧数据源是什么
帧数据源（[FrameSource](../../../api/unity/easyar.FrameSource.html)）是输入帧（[InputFrame](../../../api/unity/easyar.InputFrame.html)）的提供者，抽象了摄像头以及其它提供输入帧数据的设备和功能。
下图展示了帧数据源在 session 中的位置：
```
flowchart LR
F[Frame Source]
A((Input Frame))
B[Session]
C([Camera])
O([Origin])
T([Target])
F --> A
A --> B
B -. transform .-> C
B -. transform .-> O
B -. transform .-> T
style F fill:#6e6ce6,stroke:#333,color:#fff
```
帧数据源可能只是提供数据给下游 AR 功能使用，也可能它自身就实现了一些 AR 功能，比如运动跟踪。部分帧数据源会提供摄像头设备的控制接口，允许用户选择摄像头参数，比如分辨率、对焦模式等。
## 帧数据源的类型
以提供帧数据源的 Unity 包区分，帧数据源可以分为两大类：
* 内置帧数据源：由 EasyAR Sense Unity 插件包提供的帧数据源，通常支持大部分常见的使用场景和部分头显。
* 外部帧数据源：由 EasyAR Sense Unity 插件扩展包提供的帧数据源，通常用于支持特定的头显设备。很多时候，外部帧数据源是由头显厂商或第三方开发者提供的。
区分于外部帧数据源，[自定义相机](../../cameras/custom-camera.html) 并不一定是外部提供的，内置帧数据源中也有部分是自定义相机。
帧数据源可以提供不同自由度的运动数据：0DoF、3DoF、5DoF 和 6DoF，同一个帧数据源有可能在不同工作状态下提供不同自由度的运动数据。
下面的表格列出了由 EasyAR 提供的帧数据源：
|名称|内置|自定义相机|运动数据|说明|
|[CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|是|否|无（0DoF）|普通摄像头，支持前后摄和 PC|
|[EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|是|否|无（0DoF）|普通摄像头，仅支持在编辑器下调试使用|
|[FramePlayer](../../../api/unity/easyar.FramePlayer.html)|是|否|播放文件决定|回放 EIF 文件，实现模拟运行|
|[ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)|是|否|3DoF|提供 3DoF 跟踪能力|
|[InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)|是|否|5DoF|提供惯性导航能力|
|[MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)|是|否|6DoF|提供 EasyAR 实现的运动跟踪|
|[ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)|是|否|6DoF|提供 ARCore 的运动跟踪|
|[ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)|是|否|6DoF|提供 ARKit 的运动跟踪|
|[AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)|是|是|6DoF|提供 AR Engine 的运动跟踪|
|[VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)|是|是|6DoF|提供 VisionOS ARKit 的运动跟踪 [1](#fn:1)|
|[XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)|是|是|6DoF|提供 XREAL 设备的运动跟踪 [1](#fn:1)|
|[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)|是|是|6DoF|提供 ARFoundation 对应 ARCore 的运动跟踪|
|[ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)|是|是|6DoF|提供 ARFoundation 对应 ARKit 的运动跟踪|
|[PicoFrameSource](../../../api/unity/easyar.PicoFrameSource.html)|否|是|6DoF|提供 Pico 设备的运动跟踪 [1](#fn:1)|
|[RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html)|否|是|6DoF|提供 Rokid 设备的运动跟踪 [1](#fn:1)|
## 运行时帧数据源选取
session 的场景层级结构中包含了一个或多个帧数据源组件。在 session 运行时，并非所有的帧数据源组件都会被使用。
下面的截图展示了一个只有单个帧数据源组件的场景层级结构：
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-image-tracking.png)
下面的截图展示了一个包含多个帧数据源组件的场景层级结构：
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-mega.png)
每个帧数据源的功能不同，这也同时决定了它们适用的使用场景和设备。在 session 组装时，会从这些组件中选取一个且只有一个作为 session 的帧数据源。
[AssembleOptions.FrameSourceSelection](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html) 属性定义了 session 运行时帧数据源的选取方法：
|名称|方法|
|[Auto](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_Auto)（默认）|自动选择，按 transform 顺序选择第一个可用且 active 的子节点。|
|[Manual](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_Manual)|手动指定。只能指定 session 子节点。|
|[FramePlayer](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_FramePlayer)|使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html)。|
> **提示**
Unity 物体的 transform 顺序可以使用 [Transform.GetSiblingIndex()](https://docs.unity3d.com/ScriptReference/Transform.GetSiblingIndex.html) 判断，也可以从 Hierarchy 视图中物体的排序判断，但是需要关闭以下选项（默认是关闭状态）： Edit > Preferences > General > Enable Alphanumeric Sorting。
session 组装过程中，帧数据源在经历如下步骤后被选定：
1. session 遍历其子节点，按 transform 顺序收集所有 active 的帧数据源组件。
2. 根据 [AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 中的选源策略（[AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource)）筛选候选列表：
* **Auto**（默认）：保留所有候选。
* **Manual**：仅保留手动指定的帧数据源。
* **FramePlayer**：更换候选列表为 [FramePlayer](../../../api/unity/easyar.FramePlayer.html)。
* 再次筛选候选列表，移除以下组件：
* 被组件自身禁用的组件。
* 关闭了自定义相机（[AssembleOptions.EnableCustomCamera](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_EnableCustomCamera) 为 false）时的所有自定义相机组件。
* （Android 平台）如果 [AssembleOptions.DeviceList](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_DeviceList) 的超时设置大于 0，且候选列表中包含 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)、[ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html) 或 [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)，会尝试下载对应的最新的设备支持列表。下载更新后，这些帧数据源的可用性可能会发生变化。下载完成或超时后，继续后续步骤。
* 按列表顺序依次检查剩余候选组件的可用性（调用 [FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 并访问 [FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable)）。
* 选取**第一个**检查结果为可用的帧数据源。
其中，组件自身的禁用条件由组件内部定义，常见有这些情况：
* 在不支持的系统中运行，比如非 Android 系统下 [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html) 会被禁用。
* 必要的第三方 SDK 未安装，比如 XREAL SDK 未安装时 [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html) 会被禁用。
* 配置的条件未满足，比如设备的 [MotionTrackerCameraDeviceQualityLevel](../../../api/unity/easyar.MotionTrackerCameraDeviceQualityLevel.html) 低于 [MotionTrackerFrameSource.DeviceQualityLevel](../../../api/unity/easyar.MotionTrackerFrameSource.html#u_easyar_MotionTrackerFrameSource_DeviceQualityLevel) 时 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 会被禁用。
如果最终没有任何一个帧数据源被选定，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，且 session 报告中 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 字段数值是 [NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource)。
> **注意**
设备列表完成更新后，如果设备列表发生变化，帧数据源的可用性可能也会发生改变，可以参考 [设备支持和 session 报告](../fundamentals/session-report.html) 了解这时 session 的行为。
## 后续步骤
* 尝试在场景中 [添加一组帧数据源](frame-source-group.html)
## 相关主题
* [设备支持和 session 报告](../fundamentals/session-report.html)
* [EasyAR 的头显支持](../../headsets/headsets.html)
* 创建 [外部帧数据源](external-frame-source.html) 以使用 [自定义相机](../../cameras/custom-camera.html)
1. 设备支持情况可以参考 [EasyAR 的头显支持](../../headsets/headsets.html) 。[↩](#fnref:1)[↩](#fnref:2)[↩](#fnref:3)[↩](#fnref:4)
