---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/target.html
original_file: doc--zh-cn--develop--unity--fundamentals--target.md
normalized_at: 2026-02-27
---
# Unity AR 的跟踪目标 —— target
target 在 Unity 中表达了各种可跟踪的物体。通过以下内容，您将了解 Unity AR 中的跟踪对象 target 的基本概念、状态和生命周期。
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
## target 是什么
target 是指那些被 AR 功能识别和跟踪的物体在 Unity 中的代表。真实世界中这些物体可以是图像、3D 物体、空间地图等。通过识别和跟踪这些物体，AR 应用可以在现实世界中叠加虚拟内容，实现丰富的交互体验。
有些 target 在现实世界中是静止的（比如墙上的海报）。
>
> 这段视频展示了一个简单的运行了图像跟踪的 AR 场景。视频左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图。视频是使用模拟运行数据，在 Unity 编辑器的
`> Play
`> 模式录制的。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。在这段视频里，target（
[> ImageTarget
](../../../api/unity/easyar.ImageTarget.html)> ）代表了现实世界中的名片。我们在其上方放置一个黄色球体标识便于观察它的运动。
>
> 可以看到，target 在现实世界和场景中的位置都是固定的，而代表用户的摄像机（蓝色锥体）会根据用户在现实世界中的移动而移动。白色锥体截取了过去一段时间内摄像机的位置和朝向轨迹。可以看到黄色球体是在 target （
[> ImageTarget
](../../../api/unity/easyar.ImageTarget.html)> ）节点下的，这也是这类场景中物体的典型组织结构。
>
有些 target 在现实世界中是可以移动的（比如公交车上的海报）。
>
> 这段视频展示了同样的场景，不过这次我们在现实世界中移动了 target（名片）。可以看到，target 移动后，黄色球体会跟随名片进行运动，而
`> Game
`> 视图中该球体标识仍然贴合在名片之上。
>
为了便于理解，上面两个视频中关闭了 [ImageTarget](../../../api/unity/easyar.ImageTarget.html) 的 gizmo 的显示，并且都采用了 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式，这两段视频中 `Scene` 视图中物体的运动与真实世界中相同。在实际的 AR 场景中，这种运动关系要更加复杂一些。
## target 在不同中心模式下的行为
在 Unity 中，所有 AR 跟踪的中心参考点被称为 session 中心，而 session 运行过程中决定这个中心的规则被称为中心模式。在不同的中心模式下，target 的行为有所不同：
* **在 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式下，target 是不能随意移动的。**
[SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式只能存在于有运动跟踪的场景中。
虽然这个模式在前面的简单场景中可以很好地展示 target 和摄像机在现实中的运动，但在实际的 AR 场景中并不常用，因为在这个模式下，session 会控制 target 的运动，且由于运动跟踪或是 AR 功能本身的计算误差，很难保证 target 是完全固定不动的。这时内容根节点就要跟随 target 进行运动，在 Unity 系统中会对内容行为（比如物理系统）产生一些影响。
* **在 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 中心模式下，如果 target 正好是被选作中心的物体，那它是可以随意移动的。**
一般 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 模式是比较常用的，它能保证第一个被跟踪的物体在场景中是不会被 session 控制的，如果没有移动 target 的需求，那它就是固定不动的，无论现实场景中对应的物体是否在运动。
* **在 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 中心模式下，如果 target 不是被选作中心的物体，以及在 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 中心模式下，target 是不能随意移动的。**
一般在同时跟踪多个物体时，即使在现实环境中这些物体是相对固定的，但是由于计算误差的存在，同一时间也只能有一个 target 是不受 session 控制的。这时根据配置不同，其它 target 的运动与否是不受保证的，即使现实中没有运动，场景中也可能会有微小的运动。应该充分考虑到多个物体同时跟踪时的这个行为，并合理调整内容策略。
关于中心模式以及场景内物体的运动方式可以详细参考： [中心模式](center-mode.html) 。
## target 的状态
target 的状态反映了 target 在当前 session 中的识别和跟踪情况。常见的状态包括：
* **被跟踪（Tracked）**：target 已被成功识别和跟踪，AR 应用可以在其上叠加虚拟内容，内容会贴合真实世界中的物体。
* **未被跟踪（Not Tracked）**：target 当前未被识别或跟踪，如果 AR 应用仍然在其上叠加虚拟内容，则内容不会贴合真实世界中的物体。
同时，在状态变化时，可以通过这些事件进行响应：
* **TargetFound**：当 target 被成功识别和跟踪时触发。
* **TargetLost**：当 target 失去跟踪状态时触发。
## target 的生命周期
在 Unity AR 场景中，target 通常由对应的 frame filter 组件进行管理。frame filter 会处理来自 frame source 的图像数据，并识别和跟踪其中的 target。而 frame filter 的生命周期则依托于 session。虽然不同 AR 功能实现上可能会有差异，但大部分情况下，在 session 启动时，target 会被加载，并在加载后受控于 session。在 session 停止时，target 会被卸载并留在原地直至被下一个 session 使用或被手动删除。
## 后续步骤
* 尝试 [获取 target 状态](target-state.html)
* 尝试在各种 AR 功能中使用对应的 target
* [Mega](../mega/target.html)
## 相关主题
* [中心模式](center-mode.html)
* [XR Origin](origin.html)
