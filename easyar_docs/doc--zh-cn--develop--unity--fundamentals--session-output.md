---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-output.html
original_file: doc--zh-cn--develop--unity--fundamentals--session-output.md
normalized_at: 2026-02-27
---
# 获取 session 的运行结果
session 运行过程中会修改场景中部分物体的 transform，以及修改摄像机的画面等。有些时候，这些修改还不满足应用的使用需要，可能需要获取 session 每帧的运行结果，并对这些数据进行二次处理。本文介绍了如何获取和使用这些结果数据。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 了解如何 [创建 session](session-creation.html)
* 了解如何 [访问 AR 功能组件](session-components.html)
## 获取 [InputFrame](../../../api/unity/easyar.InputFrame.html) 更新
可以使用 [InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 事件获取 [InputFrame](../../../api/unity/easyar.InputFrame.html) 的更新。这个事件仅在 session 每帧输出数据中 [InputFrame](../../../api/unity/easyar.InputFrame.html) 产生变化时触发。
> **注意**
[InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 只在由 EasyAR 进行画面绘制的 session 中有效。一般来说，使用 AR Foundation 或头显时是无效的，这时需要使用这些第三方库提供的方法获取数据更新。
使用 [InputFrame](../../../api/unity/easyar.InputFrame.html) 可以获取物理相机图像、相机参数、时间戳、物理相机相对于世界坐标系的变换和跟踪状态等。不过由于相机变换已经被 session 应用到虚拟摄像机和其它物体上，所以通常不需要通过 [InputFrame](../../../api/unity/easyar.InputFrame.html) 获取相机变换。
### 获取当前帧的物理相机图像
可以使用 [InputFrame.image()](../../../api/unity/easyar.InputFrame.html#u_easyar_InputFrame_image) 方法获取 [Image](../../../api/unity/easyar.Image.html) 类型的物理相机图像数据。
例如，下面这段代码可以在 [InputFrame](../../../api/unity/easyar.InputFrame.html) 更新时获取物理相机图像：
```
Session.InputFrameUpdate += (inputFrame) => {
using (var image = inputFrame.image())
{
}
};
```
> **小心**
使用 [Image](../../../api/unity/easyar.Image.html) 类型数据以及从它获取的其它 class 类型数据时，必需保证 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 被正确调用（上面代码中的 using 语句保证了这一点），否则会出现内存泄漏甚至画面停止更新等问题。
如需保留 [InputFrame](../../../api/unity/easyar.InputFrame.html) 或 [Image](../../../api/unity/easyar.Image.html) 到下一帧使用，需要根据保留的数据量增加 [ARAssembly.ExtraBufferCapacity](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_ExtraBufferCapacity) 的数值，否则可能会因为缓冲区不足而导致数据获取失败。
如需保留 [InputFrame](../../../api/unity/easyar.InputFrame.html) ，还需要调用 [Clone()](../../../api/unity/easyar.InputFrame.html#u_easyar_InputFrame_Clone) 方法创建一个引用副本，然后在不需要时对副本调用 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose)。
由于物理相机的帧率通常低于渲染帧率，所以并不是每个渲染帧都能收到 [InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 事件，但同样的，物理相机画面渲染也并不是每个渲染帧都更新的。在 [InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 下次事件触发之前的所有渲染帧的画面内容都与当前 [InputFrame](../../../api/unity/easyar.InputFrame.html) 的图像一致。
> **注意**
[InputFrame](../../../api/unity/easyar.InputFrame.html) 中的图像一定是与当前帧虚拟摄像机背景画面一致的，但是背景画面渲染时可能经过缩放和裁切，所以获取的画面大小或比例与屏幕上显示的不一致是正常的。
另外需要注意的是，[InputFrame.image()](../../../api/unity/easyar.InputFrame.html#u_easyar_InputFrame_image) 返回的图像数据是 CPU 可读的，它不是 GPU 纹理。如果需要在 GPU 上使用图像数据，需要将图像数据上传到 GPU 纹理中，或者通过 [CameraImageRenderer.RequestTargetTexture(Action<Camera, RenderTexture>)](../../../api/unity/easyar.CameraImageRenderer.html#u_easyar_CameraImageRenderer_RequestTargetTexture_System_Action_UnityEngine_Camera_UnityEngine_RenderTexture__) 接口直接获取 GPU 纹理。
### [可选] 拦截物理相机图像渲染
可以使用 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 来控制物理相机图像的绘制。
下面这段代码可以停止物理相机图像的绘制：
```
if (Session.Assembly != null && Session.Assembly.CameraImageRenderer.OnSome)
{
Session.Assembly.CameraImageRenderer.Value.enabled = false;
}
```
需要注意的是，这里需要先判断 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 是否存在。
> **注意**
只在由 EasyAR 进行画面绘制的 session 中，才能通过上面的方法停止画面更新。一般来说，使用 AR Foundation 或头显时是无效的，这时需要使用这些第三方库提供的方法来实现相应的功能。
停止物理相机图像绘制后，应用可以通过 [InputFrame](../../../api/unity/easyar.InputFrame.html) 获取物理相机图像数据，并使用这些数据进行自定义的绘制。
## 获取 transform 更新
可以通过 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件获取 session 每帧更新后场景中物体的 transform 数据。
> **注意**
对于部分功能（比如 Mega），即使图像没有变化也没有显示地请求服务更新，AR 计算也是每个渲染帧都在运行的。因此如果需要获取所有的 transform 变化，则必需每帧获取 transform 数据，而不能只在某些帧获取。
### 获取虚拟摄像机的 transform
可以通过 [ARAssembly.Camera](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Camera) 获取场景中摄像机的 transform。
```
Session.PostSessionUpdate += () =>
{
var position = Session.Assembly.Camera.transform.position;
var rotation = Session.Assembly.Camera.transform.rotation;
};
```
### 获取 target 的 transform
可以通过在使用的具体 target 对象获取场景中 target 的 transform。比如，对于图像跟踪来说，这个 target 就是 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html) 组件所在的物体。
```
Session.PostSessionUpdate += () =>
{
var position = target.transform.position;
var rotation = target.transform.rotation;
};
```
### [可选] 获取 pose
pose 是一种描述物体位置和朝向的数据结构，通常由 position 和 rotation 两部分组成。在 AR 应用中，pose 通常用于描述物理相机或跟踪目标相对于某个参考系的位置和朝向。
Unity 中不提供原始的 pose 数据，因为pose 一般用于驱动场景中的物体运动，而这正是 session 自动完成的工作。对于内容计算和渲染来说，只需要 transform 就足够了。
> **重要事项**
在阅读下面的方法之前，请再思考一下，场景中摄像机、跟踪目标等物体的 transform 数据，是否已经满足需求？通常来说，额外的 pose 数据并不是必需的。
如果确实出于某种原因需要 pose 数据，可以在 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件中通过 transform 计算得到所需的 pose 数值。通常来说， [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 中获取到 target 与 camera 的相对 transform 就是 pose。
下面这段代码展示了如何获取 camera 和 target 的 transform，并计算它们之间的相对 pose：
```
Session.PostSessionUpdate += () =>
{
Pose cameraToWorld = new(Session.Assembly.Camera.transform.position, Session.Assembly.Camera.transform.rotation);
Pose targetToWorld = new(target.transform.position, target.transform.rotation);
Pose worldToTarget = new()
{
position = Quaternion.Inverse(targetToWorld.rotation) \* (-targetToWorld.position),
rotation = Quaternion.Inverse(targetToWorld.rotation)
};
Pose cameraToTarget = cameraToWorld.GetTransformedBy(worldToTarget);
};
```
> **小心**
如果您同时在使用 AR Foundation、头显或其它第三方库也在运行，这些库可能也会修改场景中摄像机的 transform。需要在确保这些库的更新逻辑完成之后再进行相关 pose 计算，否则计算结果可能不正确。在这样的场景下， [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 中 target 和 origin 的相对 pose 仍然是准确的。
### [可选] 拦截 transform 更新
AR 功能运行时，Unity 中的摄像机、跟踪目标等物体 transform 通常会被 session 自动更新。这些更新过程保证了 AR 渲染的正确性和一致性，所以没有任何方法可用拦截这些更新。
但是如果您需要自定义物体的 transform 更新逻辑，可以通过监听 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件来实现。这里需要使用一个比较繁琐的方法：
1. 虽然通常情况下，应该把渲染内容以子节点或附加组件的形式挂载在 session 控制的物体下，但是如果需要自定义更新物体的 transform，就需要把这些物体从 session 控制的物体层级中移除。也就是说，这些物体不应该是 session 控制物体的子节点。
2. 在 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件中，记录下想要自定义更新的物体的 transform。
3. 最后，在 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件中，根据 session 提供的数据，使用自定义逻辑更新这些物体的 transform。
> **注意**
使用 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件是必需的，因为只有在这个时间之后，session 才不会操作场景中的物体。
需要注意的是，这种方法不能用于修改 camera，需要更加复杂的逻辑来处理摄像机的自定义更新。
另外，这种方法只能用于自定义更新物体的 transform，不能用于修改 session 控制的物体的 transform。如果 session 控制的物体的 transform 被外部修改，session 仍然会在下一帧更新时覆盖这些修改，进而可能影响一些计算正确性。
> **小心**
使用这种方法需要您保证物体 transform 的正确性，否则可能会导致 AR 渲染错误。
如果您同时在使用 AR Foundation、头显或其它第三方库，这些库可能也会修改场景中物体的 transform。需要确保这些库的更新逻辑与自定义逻辑不会冲突，否则可能会导致不可预期的结果。
## 相关主题
* [中心模式](center-mode.html) 约束了 session 会驱动哪些物体的 transform 修改
* AR基础组件介绍
* [XR Origin](origin.html)
* [Target](target.html)
* [Camera](camera.html)
