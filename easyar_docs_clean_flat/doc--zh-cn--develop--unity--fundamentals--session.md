---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session.html
original_file: doc--zh-cn--develop--unity--fundamentals--session.md
normalized_at: 2026-02-27
---
# Unity AR 的入口 —— AR Session
AR 会话（session）是所有 AR 功能的入口，通过以下内容您将了解 AR Session 的基本概念、组成、运行流程以及它与 Unity AR Foundation 的 AR Session 有什么关系。您还会了解到在 Unity 中，EasyAR Sense 的数据流到底是如何工作的。
## AR Session 是什么
所有 AR 流程（例如物体跟踪）都是在原生库，即 EasyAR Sense 内部执行的。session 是 Unity 中 AR 功能的主要入口点。它管理 AR 系统的运行过程和状态，包括从物理相机和传感器中读取数据、分析真实世界、驱动场景中虚拟摄像机等其它部分物体的移动和渲染等。
```
flowchart LR
A((图像<br>和其它数据))
B[Session]
C([Camera])
O([Origin])
T([Target])
A --> B
B -. transform .-> C
B -. transform .-> O
B -. transform .-> T
```
### [可选] EasyAR 的 session 与 AR Foundation 的 session
EasyAR 的 session 是 Unity 中使用 EasyAR 的核心组件，可以独立于任何第三方或系统 AR 功能运行。而 [AR Foundation 的 session](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/features/session.html) 是 Unity XR 框架的一部分，只能使用 Unity XR 插件（如 ARKit 或 ARCore）提供的功能。
```
flowchart TD
A1[EasyAR<br>AR Session]
A2[EasyAR Sense]
A1 --> A2
B1[AR Foundation<br>AR Session]
B2[ARKit Plugin]
B3[ARCore Plugin]
B1 --> B2
B1 --> B3
```
使用 EasyAR 时，通常并不需要同时安装和使用 AR Foundation。比如图像跟踪功能，运动跟踪功能等等，都是由 EasyAR Sense 独立提供的。
在某些情况下，可能需要将 EasyAR Sense 与 AR Foundation 结合使用，以利用 AR Foundation 提供的额外功能（比如在部分设备上的平面检测）和接口。在这种情况下，EasyAR Sense 通过 AR Foundation 提供的接口与 Unity 引擎进行交互。
但是，由于 EasyAR 提供了比系统 AR 更多的功能和更完善的设备适配，独立使用 AR Foundation 通常无法达到与 EasyAR 相同的效果。
## session 的组成
一个典型的 session 主要由以下部分组成：
* frame source：提供物理相机图像和传感器数据的组件，有时这些组件也会提供运动跟踪数据。比如 *CameraDeviceFrameSource* 和 *MotionTrackerFrameSource*
* frame filter(s)：提供特定AR功能的组件，比如 *ImageTrackerFrameFilter*
* camera：场景中的虚拟摄像机对象
* origin：运动跟踪的原点对象
> **注意**
在 AR Foundation 的概念中，运动跟踪被作为必选功能，因此它始终会提供一个 origin。
而在 EasyAR 系统中，运动跟踪是一个可选的功能，因此 origin 也是可选的。
### [可选] session 的数据流
[数据流](../../native/fundamentals/dataflow.html) 是 EasyAR Sense 的核心概念之一。它不影响您在 Unity 中开发 AR 应用。如果您想要更加深入地理解 session 的工作原理，可以阅读本节内容。
在 Unity 中，一个 session 通常表达了一个 EasyAR Sense 的数据流。
```
flowchart LR
S[Frame Source]
R[Input Frame Recorder<br>Video Input Frame Recorder]
ift[iFrameThrottler]
iff[iFrameFork]
i2f[i2FAdapter]
fb[fbFrameFork]
i2o[i2OAdapter]
FOT[Object Tracker]
FIT[Image Tracker]
FMT[Mega Tracker]
FSSM[Sparse Spatial Map]
FST[Surface Tracker]
FDS[Dense Spatial Map]
FCR[Cloud Recognizer]
ofj[oFrameJoin]
off[oFrameFork]
ofb[oFrameBuffer]
O(( ))
ODS(( ))
OCR(( ))
S ==> R ==> ift ==> iff
iff --> i2f
i2f --> fb
fb -.-> FOT -.-> ofj
fb -.-> FIT -.-> ofj
iff ==> i2o ==> ofj ==> off ==> ofb ==> O
iff -.-> FMT -.-> ofj
iff -.-> FSSM -.-> ofj
iff -.-> FST -.-> ofj
iff -.-> FDS -.-> ODS
iff -.-> FCR -.-> OCR
off --> i2f
ofb --> ift
```
这个数据流是在 session 启动过程中创建的，图中除加粗数据通路外，其它部分是否连接取决于启动过程中启用的 AR 组件。
因此，通过修改 session 中启用的组件，可以灵活改变数据流的结构和功能，也可以很方便地同时启用多个 AR 功能。而这个方法将在接下来的段落中详细介绍。
## session 的流程
```
flowchart LR
i[初始化<br>Initialize]
a[组装<br>Assemble]
starta["启动（已组装的）<br>StartSession(Assembled)"]
start[启动<br>StartSession]
update((更新<br>update))
stop[停止<br>StopSession]
di[反初始化<br>Deinitialize]
i --> a --> starta --> update --> stop --> di
i --> start --> update
```
* 初始化
初始化是使用使用 license key 启动 EasyAR Sense 的过程，在初始化之前，只有极少部分 EasyAR Sense 的接口可以使用。初始化之后，AR 功能才会被激活。
* 组装（Assembling）
组装过程会根据组装选项的配置，从场景中挑选合适的组件，并将它们连接成一个整体工作单元。这个过程通常是在启动时自动完成的，但也可以在启动之前手动调用组装接口来完成这个过程。组装完成后，可以通过启动已组装的 session 来跳过组装过程，从而加快启动速度。
组装过程还有一个重要的用途就是判断AR组件以及输入源的可用性，并在所有候选输入中选择最合适的输入源。这一步骤也可以用来判断当前 session 是否可以在当前设备上运行。
组装过程分成两个阶段
1. 第一阶段会启动设备支持列表更新并根据配置等待固定时间后开始组装。如果在第一阶段等待后设备支持列表已经更新完成，那么组装过程就结束了；
2. 否则组装过程会进入第二阶段，第二阶段会在设备支持列表更新完成后执行。在这一阶段中，如果可用 frame source 从第一阶段的没有可用 frame source 变成了存在可用 frame source，且 session 在第一阶段之后启动失败，则会尝试重新启动 session。
无论第一阶段设备列表是否完成更新，session 都会在第一阶段完成后继续执行后续步骤。
3. 启动
启动是开始 AR 功能运行的过程。在启动之前，AR 功能组件不会处理任何数据。正常启动之后，session 会开始控制场景中的部分物体移动，并在使用部分输入源时控制物理相机图像的渲染。
4. 更新
更新过程在 Unity 的渲染循环的每帧执行。更新过程会根据当前使用的AR功能的运行结果，每帧修改虚拟摄像机（部分输入源）、原点以及跟踪目标的 transform。不同设备上更新过程的执行时间点并不是相同的，但一定会在渲染之前执行。
5. 停止
停止会终止 AR 功能的运行，场景中的物体将不再被 session 控制，输入源的数据也不会被处理。
6. 反初始化
反初始化会释放部分全局资源（不会卸载动态库）。反初始化之后，AR 功能组件将无法使用。
> **注意**
所有 AR 功能只能在 ARSession.StartSession 之后使用。
## session 的默认生命周期
```
flowchart LR
uload("BeforeSceneLoad")
ustart("MonoBehaviour.Start")
udestroy("MonoBehaviour.OnDestroy")
oi{Initialize<br>OnStartup}
ostart{AutoStart}
i[初始化<br>Initialize]
start[启动<br>StartSession]
update((更新<br>update))
stop[停止<br>StopSession]
uload -.-> ustart -.-> udestroy
uload --> oi -. true .-> i
ustart --> ostart -. true .-> start
udestroy --> stop
i --> start --> update --> stop
```
session 的生命周期一般由接口调用的时间决定。采用默认设置时，session 会在以下时间点自动执行：
* 初始化（[EasyARSettings.InitializeOnStartup](../../../api/unity/easyar.EasyARSettings.html#u_easyar_EasyARSettings_InitializeOnStartup) == `true`）
自动初始化会在 Unity 的 [BeforeSceneLoad](https://docs.unity3d.com/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) 时间点执行。
* 启动（[ARSession.AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) == `true`）
自动启动会在 session 的 [MonoBehaviour.Start()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) 时间点执行。
* 停止
自动停止会在 session 的 [MonoBehaviour.OnDestroy()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnDestroy.html) 时间点执行。
## session 状态
ARSession.State 描述了 session 的状态。一个 session 有以下几种状态：
|状态|描述|
|None|初始状态，session 未启动或组装|
|Broken|组装失败等原因 session 被破坏|
|Assembling|在组装过程中，组装过程通常可能持续几帧|
|Assembled|成功完成组装，但尚未启动|
|Ready|session 成功启动，这个状态只会持续一帧|
|Running|session 在运行中|
|Paused|session 暂停运行|
通常 session 的状态会在调用启动和停止等接口时发生变化。运行过程中，如果出现严重错误，session 也可能进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态。进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态的 session 无法恢复运行，必需调用停止后重新启动。
可以通过 session 的状态了解当前 session 是否出于可用状态。绝大多数功能只有在 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 或 [Running](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Running) 状态下才能使用。
## 运动跟踪状态
ARSession.TrackingStatus 描述了 session 的运动跟踪跟踪状态，它表示设备运动跟踪的质量，有这几种状态：
|状态|描述|
|Optional<MotionTrackingStatus>.Empty|运动跟踪功能未启用或 session 未运行|
|NotTracking|运动跟踪结果不可用，原因可能是正在初始化，跟踪丢失或者正在重定位|
|Limited|运动跟踪是有效的，但是结果不太好，原因可能是当前区域纹理太弱或运动过快|
|Tracking|运动跟踪质量好|
> **注意**
在 AR Foundation 的概念中，运动跟踪被作为必选功能，因此它的跟踪状态与 session 状态合并在了一起。
而在 EasyAR 系统中，运动跟踪是一个可选的功能，因此跟踪状态是独立存在且可能为空的。
## 其它 AR 功能的跟踪状态在哪
由于 AR 功能可能同时跟踪复数个对象，因此图像跟踪状态和其它 AR 功能的跟踪状态并不在 session 中，而是在跟踪目标组件中。
可以使用 TargetController.IsTracked 了解跟踪目标是否出于跟踪状态，或使用 TargetController.TargetFound 和TargetController.TargetLost 事件在跟踪状态变化时调整应用内容逻辑。
## 后续步骤
创建
* 尝试在场景中 [创建 session](session-creation.html)
控制运行
* 了解 [初始化](initialization.html) 的方法和作用
* 了解如何 [判断可用性和设备支持](session-assemble.html)
* 了解 [控制 session 执行](session-ctrl.html) 的方法
访问组件和结果
* 尝试 [访问 AR 功能组件](session-components.html)
* 了解如何 [获取 session 的运行结果](session-output.html)
组件参考
* [ARSession](comp-ARSession.html) 组件参考
在动手开发之前，您可以通过这些方法快速尝试修改 session 的工作流程并观察产生的变化：
* 尝试 [session 验证工具](../simulation/tool.html)，在编辑器上测试 session 的工作流程
* 尝试在不同平台上运行 [Workflow\_ARSession 示例](sample-arsession.html) ，了解组件可用性以及 session 组成和流程的差异
了解更多AR基础组件
* [XR Origin](origin.html)
* [Target](target.html)
* [Camera](camera.html)
了解 session 在场景中修改了哪些物体的属性
* 了解 [设备支持和报告](session-report.html)
* 了解 [中心模式](center-mode.html) 以及不同模式下物体的运动差异
了解 session 启动过程中做了什么
* 了解 [帧数据源及运行时选取](../cameras/frame-source.html)
了解如何在 EasyAR 场景中使用 Unity XR 框架和 AR Foundation
* 查看 [Unity XR 框架和 AR Foundation](unity-xr.html) 的使用方法和注意事项
如果您想了解更多关于 EasyAR Sense 的数据流，可以参考以下资源：
* [数据流](../../native/fundamentals/dataflow.html)
