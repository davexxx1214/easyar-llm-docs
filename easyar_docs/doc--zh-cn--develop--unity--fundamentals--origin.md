---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/origin.html
original_file: doc--zh-cn--develop--unity--fundamentals--origin.md
normalized_at: 2026-02-27
---
# Unity AR 的运动跟踪中心 —— XR Origin
XR Origin 是 Unity 中运动跟踪功能的核心概念。在现代 AR 应用中，运动跟踪正在逐步成为必不可少的功能。通过运动跟踪，应用可以在不借助其它识别物的前提下了解用户在现实世界中的位置和朝向，从而实现沉浸式的 AR 体验。通过以下内容，您将了解 XR Origin 的基本概念、组成和生命周期，以及在什么情况下需要使用 XR Origin。
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
## XR Origin 是什么
运动跟踪功能初始化时会选择一个参考点作为跟踪的原点。这个参考点一般是用户启动应用时或是系统 AR 服务启动时设备所在的位置。这个参考点在 Unity 场景中的代表就是 XR Origin。在大多数情况下，XR Origin 在场景中的起始位置也是摄像机的默认起始位置。
>
> 这段视频展示了一个简单的只有运动跟踪在运行的 AR 场景。视频左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图。视频是使用模拟运行数据，在 Unity 编辑器的
`> Play
`> 模式录制的。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
> 可以看到，在这段视频里，XR Origin（蓝色球体）在场景中的位置是固定的，而代表用户的摄像机（摄像机图标）会根据用户在现实世界中的移动而移动。白色锥体截取了过去一段时间内摄像机的位置和朝向轨迹，可以更好地理解摄像机在场景中的运动情况。可以看到这些白色锥体是生成在 XR Origin 的节点下的，这也是这类场景中物体的典型组织结构。
>
在 Unity 的运动跟踪系统中，摄像机一般是跟随 XR Origin 进行运动的。虽然摄像机并不一定是 XR Origin 的子节点，但 AR Session 会根据 XR Origin 的位置来计算摄像机的位置，从而保证用户看到的内容和现实世界中的内容一致。
>
> 这段视频展示了同样的场景，不过这次我们在运行时移动了 XR Origin（蓝色球体）。可以看到，XR Origin 被移动后，摄像机会跟随 XR Origin 进行运动，而
`> Game
`> 视图中的内容并没有变化。
>
在实际的 AR 场景中，这种运动关系要更加复杂一些。
## XR Origin 在不同中心模式下的行为
在 Unity 中，所有 AR 跟踪的中心参考点被称为 session 中心，而 session 运行过程中决定这个中心的规则被称为中心模式。在不同的中心模式下，XR Origin 的行为有所不同：
* **在 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式下，XR Origin 是可以随意移动的。**
一般 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式会在只有运动跟踪在工作的场景中使用。在有其它功能同时运行时，通常不会使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式。
不过在使用头显时，如果厂商没有在 Unity 中正确实现运动跟踪的参考点，这时就必须使用 Unity 的世界中心从而强制使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式。这种情况要求内容根节点要跟随 AR 功能进行运动，这可能会影响内容效果，但在第三方厂商做出更改之前并没有其它办法。
* **在其它中心模式（比如 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget)）下，XR Origin 是不能随意移动的。**
一般 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 模式在非运动跟踪或有其它 AR 功能与运动跟踪同时运行的场景中使用。
在这种模式下，XR Origin 的位置是由 AR 功能决定的，因此不能随意移动 XR Origin。
关于中心模式以及场景内物体的运动方式可以详细参考： [中心模式](center-mode.html) 。
## XR Origin 的形式和组成
EasyAR 可以使用两种不同形式的 XR Origin：
* EasyAR 提供的 XR Origin
* Unity XR 框架提供的 XR Origin
### XR Origin (EasyAR)
典型的 XR Origin 结构如下所示：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin.png)
XR Origin 根节点是一个空的 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html)，它可以有一个或多个 XR Origin Child 子节点。XR Origin Child 包含了一个 [XROriginChildController](../../../api/unity/easyar.XROriginChildController.html) 组件，用于代理 XR Origin 的控制逻辑。
session 运行时，如果场景中没有正确的 XR Origin 结构，XR Origin 和一个 XR Origin Child 会被自动创建。运行过程中，XR Origin Child 会被约束在 XR Origin 相同的位置和朝向下。
由 session 生成的物体，比如稀疏空间地图建图的点云，或是稠密空间建图的网格，会被创建在 XR Origin Child 节点下。
>
> 这段视频展示相同场景下在运动跟踪同时运行了稠密空间建图的效果。可以看到生成的网格是被创建在 XR Origin Child 节点下的。
>
> 注：为了便于理解，视频中关闭了深度图生成，因此视频中
`> Scene
`> 视图的内容与实际运行时显示的内容会有差异。
`> Game
`> 视图的显示效果与关闭 mesh 透明时相同。
>
### [可选] XR Origin (Unity XR)
如果需要，可以选择使用 Unity XR 框架提供的 [XR Origin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin.html) 组件。
在使用 Unity XR 框架提供的 XR Origin 时，一个典型的结构如下所示：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-unityxr.png)
在头显场景中，一个典型的结构如下所示：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-unityxr-headset.png)
XR Origin 根节点是由 Unity XR 框架创建和维护的 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html)，它可以有一个或多个 XR Origin Child 子节点。XR Origin Child 包含了一个 [XROriginChildController](../../../api/unity/easyar.XROriginChildController.html) 组件，用于代理 XR Origin 的控制逻辑。
session 运行时，如果场景中没有正确的 XR Origin Child 结构，XR Origin Child 会被自动创建。运行过程中，XR Origin Child 会被约束在 XR Origin 相同的位置和朝向下。
Unity XR 框架提供的 XR Origin 主要为以下两种情况提供支持：
* 您已经在项目中使用了 AR Foundation，并希望与 EasyAR 同时工作或根据设备支持情况在两者之间切换。
* 您所使用的头显 SDK 使用了 Unity XR 框架提供的 XR Origin 组件。
> **注意**
当 Unity XR 的核心包 `com.unity.xr.core-utils` 未被导入到工程中时，如果场景中的摄像机处于与 Unity XR 框架提供的 XR Origin 相同的层级结构中（Camera 及名为 Camera Offset 父节点），session 会假定这个结构是 Unity XR 框架创建的并使用它。这样做是为了给场景提供最大限度的兼容性，即：使用 AR Foundation 创建的场景，在 AR Foundation 未被导入工程中时，AR Foundation 不会工作但剩余的 AR 功能仍能正常工作。除了只有 AR Foundation 能提供的功能之外，这甚至不影响整个 AR 应该的功能性和设备兼容性。
大多数的 EasyAR 的示例场景都使用了这种方式来保证在没有 AR Foundation 的情况下仍然可以运行，且在 AR Foundation 存在时可以展示与 AR Foundation 的协同工作能力。
在 AR Foundation 的定义中，它的 XR Origin 是 XR 场景中跟踪空间的中心。不过需要注意的是，在 AR Foundation 的概念中，运动跟踪被作为必选功能，它所描述的 XR 场景中的跟踪就是运动跟踪。
在 EasyAR 系统中，运动跟踪是一个可选的功能，因此 XR Origin 也是可选的。XR Origin 只在启用了运动跟踪功能时才会创建和使用。
## XR Origin 的生命周期
XR Origin 的生命周期依托于 session。在 session 启动时，XR Origin 会被选定或被创建（如果场景中没有正确的 XR Origin 结构）。在 session 停止时，XR Origin 会留在原地直至被下一个 session 使用或被手动删除。
## 后续步骤
创建
* 尝试在场景中 [创建 XR Origin](origin-creation.html)
控制运行
* 了解 XR Origin 的 [Active 控制策略](active-control.html)
## 相关主题
* [中心模式](center-mode.html)
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)
