---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/center-mode.html
---

AR Session 的中心模式 | EasyAR 文档
**
##### Table of Contents
**
# AR Session 的中心模式
中心模式是 Unity AR 的核心概念，它决定了 session 在运行过程中选择哪个物体作为所有 AR 跟踪的参考点（中心物体），以及 session 中哪些物体可以随意移动。通过以下内容，您将了解中心模式的基本概念及其对场景中物体运动行为的影响。
## 开始之前
* 通过 [AR Session 简介](session.html)了解 session 的基本概念、组成和工作流程。
* 通过 [Camera](camera.html) 了解 AR 场景中摄像机的作用，以及 session 如何控制摄像机的属性以确保正确的 AR 体验。
* 通过 [XR Origin](origin.html) 了解 XR Origin 的基本概念、组成和生命周期。
* 通过 [Target](target.html) 了解 target 的基本概念、状态和生命周期。
## 中心物体和中心模式
在一个 session 中，可能同时运行着一个或多个不同的 AR 功能。这些 AR 功能可能会跟踪不同的物体，并且可能会同时使用运动跟踪功能来跟踪设备自身的位置和朝向。
为了确保场景中物体的运动行为符合预期，session 需要选择一个参考点作为所有 AR 跟踪的中心，这个参考点在 Unity 场景中的代表就是中心物体（[CenterObject](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterObject)）。中心模式（[CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode)）是 session 运行过程中决定这个中心物体到底是哪一个物体的规则。
一个 session 的中心可以是以下几种物体之一：
* 某个被跟踪的 target
* XR Origin
* 摄像机
中心模式决定了 session 选择哪一个物体作为中心物体，以及这个物体是否可以随意移动。而这个物体以外的物体（包括非中心的摄像机、XR Origin 和 target）都是受 session 控制，以中心物体为参考点进行运动的。
在 Unity 中，session 支持以下四种中心模式：
|名称|示意图|描述|
|**FirstTarget**
**SpecificTarget**|![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-target.png)|以 target 作为中心，该 target 可以随意移动。其中，
* FirstTarget 以第一个被跟踪的 target 作为中心。
* SpecificTarget 以指定的 target 作为中心。session 中的 camera 和 XR Origin 以及其他 target 都受 session 控制，以中心 target 为参考点进行运动。|
|**SessionOrigin**|![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-origin.png)|以 XR Origin 作为中心，XR Origin 可以随意移动。
session 中的 camera 和 target 都受 session 控制，以中心 XR Origin 为参考点进行运动。|
|**Camera**|![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-camera.png)|以摄像机作为中心，摄像机可以随意移动。
session 中的 XR Origin 和 target 都受 session 控制，以中心摄像机为参考点进行运动。|
>
> 示意图中有三个物体，蓝色球体代表 XR Origin，蓝色锥体标代表摄像机，黄色图片代表 target。在不同的中心模式下，session 会选择不同的物体作为中心物体，图中显示了对应物体的局部坐标系。
>
##### 提示
如果您有使用 AR Foundation 的使用经验，可能会注意到 AR Foundation 中并不存在类似的概念。实际上，AR Foundation 的行为模式与 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式是一致的。
在 session 中，`target` 和 `camera` 的相对运动关系由当前 session 控制。`XR Origin` 和 `camera` 的相对运动关系，由当前 session 控制或者第三方框架（比如 AR Foundation）控制。中心模式的存在保证了在不同的运行环境下，session 都能正确地控制场景中物体的运动行为。
比如，如果 AR Foundation 或基于 Unity XR 的头显 SDK 控制了 `XR Origin` 和 `camera` 的相对运动关系，`XR Origin` 作为 Unity XR 框架的设计，是可以由 session 控制移动的，而 `camera` 则不行。这时 session 会限制中心模式为 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 、 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 或 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)，这样对于 session 来说，中心会是 `XR Origin` 或某个 `target`，而对于 Unity XR 框架来说，中心仍然是 `XR Origin`，整个系统可以完美工作。
##### 警告
在 Unity AR 中，任何存在于 Unity 世界坐标系下且未根据 session 组件调整 transform 的物体都可能无法正确显示。因为 session 会根据中心物体的位置和朝向来调整场景中其它物体的位置和朝向，如果有物体不受 session 控制，它们的位置和朝向就可能与 session 计算出来的位置和朝向不一致，从而导致不可预期的行为。
比如，如果世界坐标系下放置了一个熊猫模型，这个熊猫模型的位置和朝向就可能与现实世界中任何物体都没有对应关系，看上去像是浮在空中或者到处乱动。
正确的做法是始终把要显示的内容放在某个 `target` 节点下，或者放在 `XR Origin` 节点下（如果内容需要跟随 XR Origin 运动）。这样内容的位置和朝向就会根据 session 的计算结果进行调整，从而确保内容能够正确地叠加在现实世界中。
通过手动方式对齐内容和 `target` 或 `XR Origin` 的位置和朝向是可以的，但需要在正确的时间操作，可以参考 [选择合适的中心模式](center-mode-choosing.html) 。
## 有效中心模式
并不是所有的中心模式在任何情况下都是有效的。session 会根据当前运行环境和选用的 frame source 来决定哪些中心模式是有效的，从而保证能够正确地控制场景中物体的运动行为。[ARSession.AvailableCenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AvailableCenterMode) 属性可以用来获取当前 session 的有效中心模式列表。
根据最终选用的 frame source 的不同，session 的有效中心模式有以下这几种不同情况：
|frame source|摄像机受控|有运动数据|有原点设计|有效中心模式|
|
* CameraDeviceFrameSource
* FramePlayer 且录制时使用的 frame source 无运动数据
* ExternalImageStreamFrameSource|是|否|-|
* FirstTarget
* SpecificTarget
* Camera|
|
* ARCoreFrameSource
* AREngineFrameSource
* ARKitFrameSource
* InertialCameraDeviceFrameSource
* MotionTrackerFrameSource
* ThreeDofCameraDeviceFrameSource
* FramePlayer 且录制时使用的 frame source 有运动数据|是|是|是|
* FirstTarget
* SpecificTarget
* SessionOrigin
* Camera (\*)\* *仅在 `camera` 不是
`XR Origin` 子节点时有效*|
|
* ARCoreARFoundationFrameSource
* ARKitARFoundationFrameSource
* VisionOSARKitFrameSource
* XREALFrameSource
* ExternalDeviceFrameSource 且 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin) 或 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom)
* PicoFrameSource
* RokidFrameSource 且不使用 UXR|否|是|是|
* FirstTarget
* SpecificTarget
* SessionOrigin|
|
* ExternalDeviceFrameSource 且 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [None](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_None)
* RokidFrameSource 且使用 UXR|否|是|否|
* SessionOrigin|
除了使用 FramePlayer 时之外，有效中心模式都是在 session 组装时确定的。使用 FramePlayer 时，有效中心模式是在 session 运行过程中每帧数据输出时根据数据中是否包含运动信息动态决定的。
## 不同中心模式的特性
接下来，我们将通过一系列示例视频来展示不同中心模式下物体的运动行为。
视频内容如下：
>
> 在现实世界中，有两个不同类型的可跟踪物体：
>
>
* > 一个是
**> 圣诞树
**> ，它是静止不动的。它是通过稀疏空间地图功能进行跟踪的。
>
* > 另一个是一张
**> A4 纸
**> ，纸上事先打印好了一张图片，它是可以移动的。它是通过图像跟踪功能进行跟踪的。
>
>
> 录制视频时，观察者（手机）从圣诞树的右后方开始，绕着圣诞树移动。A4 纸在观察者前方左右摆动。
>
> 为了便于观察，我们对场景中的不同物体添加了一些标识，
>
>
* **> 圣诞树
**> ：处于跟踪状态时在其所占据的空间叠加了
**> 亮蓝色点云
**> 。跟踪丢失时这些标识会消失。
>
* **> A4 纸
**> ：处于跟踪状态时在其正上方叠加了一个
**> 熊猫
**> 。
`> Game
`> 视图中还额外显示了一个与 A4 纸内容和大小完全相同的图片。跟踪丢失时这些标识会消失。
>
* **> XR Origin
**> ：在其位置放置了一个
**> 蓝色球体
**>
* **> 摄像机
**> ：在其位置放置了一个
**> 蓝色锥体
**> ，锥体的主轴与摄像机的视线方向一致。
>
>
这些视频均是使用模拟运行数据，在 Unity 编辑器的 `Play` 模式录制的。视频左边是 `Scene` 视图，右边是 `Game` 视图。`Game` 视图的内容与用户在现实世界中手机看到的内容是一样的。
### FirstTarget 和 SpecificTarget 中心模式
FirstTarget 和 SpecificTarget 中心模式是以某个 `target` 作为中心物体的模式。在这两个模式下，除了中心的 `target` 之外，session 中的 `camera` 和 `XR Origin` 以及其他 `target` 都是受 session 控制，以中心 `target` 为参考点进行运动的。
有些 target 在现实世界中是可以移动的，比如视频中的 A4 纸。
>
> 在上面这个视频中，中心物体是通过图像跟踪功能跟踪到的 A4 纸。可以看到，由于没有外部操作，A4 纸（熊猫）是静止不动的，而摄像机（蓝色锥体）、XR Origin（蓝色球体）和 圣诞树（亮蓝色点云）都在移动。
>
有些 target 在现实世界中是静止的，比如视频中的圣诞树。
>
> 在上面这个视频中，中心物体是通过稀疏空间地图功能跟踪到的圣诞树。可以看到，由于没有外部操作，圣诞树（亮蓝色点云）是静止不动的，而摄像机（蓝色锥体）和 A4 纸（熊猫）都在移动。XR Origin（蓝色球体）也没有移动，但这是因为它相对圣诞树是静止的。
>
在这两个模式下，作为参考点的中心 `target` 可以自由移动，这时 session 中的 `camera` 和 `XR Origin` 以及其他 `target` 都会跟着动，它们的 transform 不能被外部控制。
>
> 在上面这个视频中，中心物体是通过图像跟踪功能跟踪到的 A4 纸。可以看到，由于我们手动移动了 A4 纸（熊猫），摄像机（蓝色锥体）、XR Origin（蓝色球体）和 圣诞树（亮蓝色点云）都跟着动了。需要注意的是，这时
`> Game
`> 视图显示的内容并没有变化，因为摄像机的位置和朝向相对于 A4 纸和其它物体是没有变化的。
>
FirstTarget 和 SpecificTarget 模式的区别在于在运行过程中，中心 `target` 可能产生变化，但变化时中心的选择方式不同。要说明这个问题，我们要把跟踪成功和丢失的过程考虑在内。
在 session 中心物体发生变化时， [ARSession.CenterObject](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterObject) 会始终反映当前的中心物体，但 [ARSession.CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 不会发生改变。
#### FirstTarget 中心模式的中心变化
FirstTarget 中心模式下，session 始终是以第一个跟踪到的 `target` 为中心的。如果这个 `target` 跟踪丢失了，session 会重新选择中心，当 session 跟踪着或新跟踪上了另一个 `target`，另一个 `target` 就会被选作新的中心物体。
重新选择中心会出现在以下这些情况：
* 当前帧没有任何一个 `target` 在跟踪状态
这时如果 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式有效，session 会退化到 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式选择 `XR Origin` 作为中心物体；否则 session 会退化到 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式选择 `camera` 作为中心物体。
* 当前帧有 `target` 在跟踪状态，且上一帧没有任何一个 `target` 在跟踪状态
这时 session 会选择其中一个被跟踪的 `target` 作为中心物体。
* 当前帧有 `target` 在跟踪状态，且上一帧的中心 `target` 在当前帧跟踪丢失
这时 session 会选择其中一个被跟踪的 `target` 作为新的中心物体。
>
> 在上面这个视频中，一开始中心物体是通过图像跟踪功能跟踪到的 A4 纸。可以看到，当 A4 纸（熊猫）跟踪丢失时，session 重新选择了中心物体，这时圣诞树（亮蓝色点云）成为了新的中心物体，在视频结尾时，A4 纸重新被跟踪上了，但它并没有成为中心物体，因为圣诞树已经是中心物体了。
>
#### SpecificTarget 中心模式的中心变化
SpecificTarget 中心模式下，session 始终是以指定的 `target` 为中心的。如果这个 `target` 跟踪丢失了，session 会重新选择中心，但它不会选择其它 `target` 作为新的中心物体，当 session 重新跟踪上了这个指定的 `target`，它仍然会被选作中心物体。
重新选择中心会出现在以下这些情况：
* 当前帧指定的 `target` 未被跟踪
这时如果 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式有效，session 会退化到 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式选择 `XR Origin` 作为中心物体；否则 session 会退化到 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式选择 `camera` 作为中心物体。
* 当前帧指定的 `target` 在跟踪状态，且上一帧指定的 `target` 未被跟踪
这时 session 会选择指定的 `target` 作为中心物体。
>
> 在上面这个视频中，中心物体被指定为通过图像跟踪功能跟踪到的 A4 纸。可以看到，当 A4 纸（熊猫）跟踪丢失时，session 并没有选择其它
`> target
`> 作为新的中心物体，这时圣诞树（亮蓝色点云）并没有成为中心物体。在视频结尾时，A4 纸重新被跟踪上了，它恢复成为了中心物体。
>
### SessionOrigin 中心模式
SessionOrigin 中心模式是以 `XR Origin` 作为中心物体的模式。在这个模式下，session 中的 `camera` 和 `target` 都是受 session 控制，以中心 `XR Origin` 为参考点进行运动的。
>
> 在上面这个视频中，中心物体是 XR Origin。可以看到，由于没有外部操作，XR Origin（蓝色球体）是静止不动的，而摄像机（蓝色锥体）和 A4 纸（熊猫）都在移动。圣诞树（亮蓝色点云）也没有移动，但这是因为它相对 XR Origin 是静止的。
>
在这个模式下，作为参考点的中心 `XR Origin` 可以自由移动，这时 session 中的 `camera` 和 `target` 都会跟着动，它们的 transform 不能被外部控制。
>
> 在上面这个视频中，中心物体是 XR Origin。可以看到，由于我们手动移动了 XR Origin（蓝色球体），摄像机（蓝色锥体）、圣诞树（亮蓝色点云）和 A4 纸（熊猫）都跟着动了。需要注意的是，这时
`> Game
`> 视图显示的内容并没有变化，因为摄像机的位置和朝向相对于 XR Origin 和其它物体是没有变化的。
>
在 SessionOrigin 模式下，`XR Origin` 是必须有效的，因此这种模式下中心物体不会发生变化。
### Camera 中心模式
camera 中心模式是以 `camera` 作为中心物体的模式。在这个模式下，session 中的 `XR Origin` 和 `target` 都是受 session 控制，以中心 `camera` 为参考点进行运动的。
>
> 在上面这个视频中，中心物体是摄像机。可以看到，由于没有外部操作，摄像机（蓝色锥体）是静止不动的，而 XR Origin（蓝色球体）、圣诞树（亮蓝色点云）和 A4 纸（熊猫）都在移动。
>
在这个模式下，作为参考点的中心 `camera` 可以自由移动，这时session 中的 `XR Origin` 和 `target` 都会跟着动，它们的 transform 不能被外部控制。
>
> 在上面这个视频中，中心物体是摄像机。可以看到，由于我们手动移动了摄像机（蓝色锥体），XR Origin（蓝色球体）、圣诞树（亮蓝色点云）和 A4 纸（熊猫）都跟着动了。需要注意的是，这时
`> Game
`> 视图显示的内容并没有变化，因为摄像机的位置和朝向相对于 XR Origin 和其它物体是没有变化的。
>
在 Camera 模式下 `camera` 是必须有效的，因此这种模式下中心物体不会发生变化。
## 后续步骤
* 尝试 [选择合适的中心模式](center-mode-choosing.html)
## 相关主题
* [运动跟踪简介](../../motion-tracking/intro.html)
* [图像跟踪简介](../../image-tracking/intro.html)
* [稀疏空间地图简介](../../sparse-spatial-mapping/intro.html)