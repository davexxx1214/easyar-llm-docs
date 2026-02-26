---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/camera.html
---

AR 场景中的 Unity 摄像机 | EasyAR 文档
**
##### Table of Contents
**
# AR 场景中的 Unity 摄像机
Unity 中 AR 的效果呈现离不开摄像机。通过以下内容，您将了解 AR 场景中摄像机的作用，以及 session 如何控制摄像机的属性以确保正确的 AR 体验。
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
# AR 场景中摄像机的作用
Unity 中的摄像机用于向玩家展示游戏世界，而在 AR 场景中，摄像机的作用更加重要。它不仅负责渲染虚拟内容，还需要与现实世界进行对齐，以确保虚拟对象正确地叠加在现实场景中。
>
> 这段视频展示了一个简单的 AR 场景。视频左边是
`> Scene
`> 视图，右边是
`> Game
`> 视图。视频是使用模拟运行数据，在 Unity 编辑器的
`> Play
`> 模式录制的。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
> 可以看到，在这段视频里，代表用户的摄像机（摄像机图标）会根据用户在现实世界中的移动而移动。白色锥体截取了过去一段时间内摄像机的位置和朝向轨迹。可以看到在
`> Game
`> 视图中，摄像机不仅展示了
`> Scene
`> 视图里的虚拟内容，同时在虚拟内容底部还叠加了现实世界的图像，这就是 AR 场景中摄像机的典型工作方式。
>
为了确保虚拟对象正确地叠加在现实场景中，摄像机的部分属性需要根据 AR 运行的状态进行调整。这些属性包括：
* 摄像机的 transform（位置和朝向）
* 摄像机的视野（FOV）、宽高比（aspect ratio）和投影矩阵
* 摄像机的剔除设置（[GL.invertCulling](https://docs.unity3d.com/ScriptReference/GL-invertCulling.html)）
##### 警告
在开发应用时，修改 session 摄像机的这些属性是不受支持的，因为这可能会导致虚拟内容与现实世界对齐不正确，从而影响用户体验。即使通过某些手段修改了这些属性，AR 系统也会在运行过程中覆盖这些修改，或是因为渲染数据与计算数据的不一致导致不可预期的行为。
根据控制这些属性的对象的不同，session 所使用的摄像机可以分为两类：受 session 控制的摄像机和不受 session 控制的摄像机。
## 受 session 控制的摄像机
如果 session 的摄像机不属于任何外部系统，比如头显或 AR Foundation，那么 session 会自动控制摄像机的上述属性，以确保摄像机正确地与现实世界对齐。
### transform
摄像机的 transform（位置和朝向）是由 session 根据 AR 功能的运行状态进行调整的。一般来说，session 会根据运动跟踪数据和/或 target 的跟踪数据来更新摄像机的位置和朝向，从而确保用户看到的内容和现实世界中的内容一致。
在 Unity 中，所有 AR 跟踪的中心参考点被称为 session 中心，而 session 运行过程中决定这个中心的规则被称为中心模式。在不同的中心模式下，摄像机的 transform 行为有所不同：
* **在 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 中心模式下，摄像机是可以随意移动的。**
一般 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式很少被应用使用。
* **在其它中心模式（比如 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget)）下，摄像机是不能随意移动的。**
[FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 是大部分 AR 应用会采用的模式。
##### 警告
摄像机 transform 的 scale 数值应始终保持为 (1, 1, 1)。修改摄像机的 scale 可能会导致不可预期的行为。
### 投影矩阵
摄像机的投影矩阵会在 session 每帧更新时根据物理相机的内参进行更新，以确保虚拟内容正确地叠加在现实场景中。
### 剔除设置
摄像机的剔除设置（[GL.invertCulling](https://docs.unity3d.com/ScriptReference/GL-invertCulling.html)）会根据 session 的镜像设置进行调整，以确保虚拟内容正确地渲染在现实场景中。
在 [HorizontalFlip](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_HorizontalFlip) 中对应当前使用的摄像头的设置为 [World](../../../api/unity/easyar.ARSession.ARHorizontalFlipMode.html#u_easyar_ARSession_ARHorizontalFlipMode_World) 时，[GL.invertCulling](https://docs.unity3d.com/ScriptReference/GL-invertCulling.html) 会被设置为 `true`。这是前置摄像头的默认配置。
### AR 背景视频流
在 AR 场景中，摄像机通常会渲染来自物理相机的视频流作为背景，以增强用户的沉浸感。session 会自动处理视频流的获取和渲染，并确保视频流与虚拟内容正确地对齐。
## 不受 session 控制的摄像机
在使用头显和 AR Foundation 、以及实现中指定了 [IsCameraUnderControl](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsCameraUnderControl) 为 `false` 的 [FrameSource](../../../api/unity/easyar.FrameSource.html) 时，session 不会控制摄像机的上述属性，而是由外部系统负责控制。
##### 警告
虽然在这种情况下 session 不会控制摄像机的属性，但它们会由第三方系统（比如头显 SDK 或 AR Foundation）所控制，在开发应用时修改这些属性仍然是不受支持的。
## 复制摄像机时的注意事项
有时可能需要将 session 摄像机的参数复制到另一个摄像机上，这时需要额外关注以下两点：
* 属性获取时间：在使用受控摄像机时，需要参考 [获取 session 的运行结果](session-output.html) 在正确的时间获取这些参数；在使用不受控 session 控制的摄像机时，需要参考第三方系统的文档在正确的时间获取。
* 摄像机的视野（FOV）、宽高比（aspect ratio）和投影矩阵：需要使用 [Camera.projectionMatrix](https://docs.unity3d.com/ScriptReference/Camera-projectionMatrix.html) 获取摄像机投影矩阵，并复制到另外一个摄像机。[Camera.fieldOfView](https://docs.unity3d.com/ScriptReference/Camera-fieldOfView.html) 和 [Camera.aspect](https://docs.unity3d.com/ScriptReference/Camera-aspect.html) 在数学上是投影矩阵的一部分，使用 [Camera.fieldOfView](https://docs.unity3d.com/ScriptReference/Camera-fieldOfView.html) 和 [Camera.aspect](https://docs.unity3d.com/ScriptReference/Camera-aspect.html) 是不充分的。
## 后续步骤
* 阅读 [Camera 配置](camera-configs.html) 了解如何配置摄像机以获得最佳的 AR 体验
## 相关主题
* [中心模式](center-mode.html)