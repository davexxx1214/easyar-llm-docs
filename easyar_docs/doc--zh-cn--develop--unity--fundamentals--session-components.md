---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-components.html
original_file: doc--zh-cn--develop--unity--fundamentals--session-components.md
normalized_at: 2026-02-27
---
# 访问 session 中的 AR 功能组件
在运行中的 session 里，可以通过 [Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性访问各个功能组件。本文介绍了如何访问这些组件，以及访问时需要注意的事项。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 了解如何 [创建 session](session-creation.html)
## 编辑时或启动前配置 AR 组件
有些时候，某些组件选项（比如 [DesiredFocusMode](../../../api/unity/easyar.CameraDeviceFrameSource.html#u_easyar_CameraDeviceFrameSource_DesiredFocusMode)）必需在组件启动前配置，如果不想在 session 启动后再手动配置并启动组件，一个简单的方法是在 session 组装前对所有可能使用的 frame source 组件进行配置。组装过程会保留这些组件中的一个或多个，并应用其配置。
这时可以使用 [FindAnyObjectByType<T>()](https://docs.unity3d.com/ScriptReference/Object.FindAnyObjectByType.html) 或 [GetComponent<T>()](https://docs.unity3d.com/ScriptReference/Component.GetComponent.html) 等任何 Unity 基本方法找到组件，然后对组件进行配置。
> **注意**
通过这种方法获取到的 AR 组件是否会在运行时被包含在 session 中是不确定的。因此必需对所有可能的情况进行配置。
例如，下面的代码展示了在 session 组装前修改所有 frame source 组件的对焦模式的过程：
```
void Awake()
{
var allFrameSources = Session.GetComponentsInChildren<FrameSource>();
foreach (var source in allFrameSources)
{
if (source is CameraDeviceFrameSource)
{
((CameraDeviceFrameSource)source).DesiredFocusMode = autoFocus ? CameraDeviceFocusMode.Continousauto : CameraDeviceFocusMode.Medium;
}
else if (source is MotionTrackerFrameSource)
{
((MotionTrackerFrameSource)source).DesiredFocusMode = autoFocus ? MotionTrackerCameraDeviceFocusMode.Continousauto : MotionTrackerCameraDeviceFocusMode.Medium;
}
else if (source is ARCoreFrameSource)
{
((ARCoreFrameSource)source).DesiredFocusMode = autoFocus ? ARCoreCameraDeviceFocusMode.Auto : ARCoreCameraDeviceFocusMode.Fixed;
}
else if (source is ARKitFrameSource)
{
((ARKitFrameSource)source).DesiredFocusMode = autoFocus ? ARKitCameraDeviceFocusMode.Auto : ARKitCameraDeviceFocusMode.Fixed;
}
else if (source is AREngineFrameSource)
{
((AREngineFrameSource)source).DesiredFocusMode = autoFocus ? AREngineCameraDeviceFocusMode.Auto : AREngineCameraDeviceFocusMode.Fixed;
}
else if (source is ThreeDofCameraDeviceFrameSource)
{
((ThreeDofCameraDeviceFrameSource)source).DesiredFocusMode = autoFocus ? ThreeDofCameraDeviceFocusMode.Auto : ThreeDofCameraDeviceFocusMode.Fixed;
}
else if (source is InertialCameraDeviceFrameSource)
{
((InertialCameraDeviceFrameSource)source).DesiredFocusMode = autoFocus ? InertialCameraDeviceFocusMode.Auto : InertialCameraDeviceFocusMode.Fixed;
}
else if (source is ARFoundationFrameSource)
{
cameraManager.autoFocusRequested = autoFocus;
}
}
}
```
上述过程也可以在编辑器中完成，同样需要对所有组件都进行配置：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-components-editor.png)
其中 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 和 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) 两个 frame source 对应的配置在 `Main Camera` 的组件上。
> **警告**
通过这种方法获取到的 AR 组件只能用于运行前的配置。
由于组装过程会对 AR 组件进行筛选，通过场景树获取的 AR 组件可能并没有被包含在 session 中，无法正常工作。
## 运行中使用组装好的 AR 组件
session 中运行的 AR 组件是在组装后才确定的。在组装完成之前，任何 AR 组件都不能使用。组装好的 AR 组件可以通过 [Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性访问。
[Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 在 session 的状态 >= [Assembled](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Assembled) 的条件下可以使用。详细来说，[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 方法执行完成后，[Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性才会被赋值，可以通过它访问 session 组件。在 session 停止或损坏后，[Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性会被清空，无法再访问组件。
可以在脚本中检测 session 的 [State](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_State) 来判断当时是否可以访问 AR 组件：
```
if (Session.State >= ARSession.SessionState.Ready)
{
// Assembly 可以使用
}
else
{
// Assembly 不能使用
}
```
也可以通过订阅 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件来获取 session 的状态变化，从而在合适的时间点访问 AR 组件。一般来说为了能捕获到 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态，需要在 session start 之前订阅 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件，通常在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 中完成订阅是安全的：
```
void Awake()
{
Session.StateChanged += (state) =>
{
if (Session.State == ARSession.SessionState.Ready)
{
// Assembly 可以使用，在这之后 Assembly 一直可以访问，直至 session 停止或损坏
}
else if (Session.State < ARSession.SessionState.Ready)
{
// Assembly 不能使用，在这之后 Assembly 一直不可访问，直至 session 重新启动
}
else
{
// Assembly 可以使用，通常不需要处理
}
};
}
```
> **小心**
如果通过 [FindAnyObjectByType<T>()](https://docs.unity3d.com/ScriptReference/Object.FindAnyObjectByType.html) 或 [GetComponent<T>()](https://docs.unity3d.com/ScriptReference/Component.GetComponent.html) 等方法获取到 AR 组件是一定会被包含到 session 中的，也可以在运行时中使用。
只是存储这些组件的引用是安全的，但在使用这些组件时必须确保 session 处于运行状态且这些组件被正确包含在 session 中，否则可能会引发异常或不可预期的行为。
session 启动前和停止后，这些组件是无法工作的。建议即使在这样的用法中，也要关注 session 的 [State](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_State) 和 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件。
### 访问 frame source 组件
可以使用 [ARAssembly.FrameSource](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameSource) 属性访问 frame source 组件。在一个正常运行的 session 中，[ARAssembly.FrameSource](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameSource) 有且只有一个。
在使用 session 时，通常需要通过访问 [ARAssembly.FrameSource](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameSource) 才能确定运行时实际使用的 frame source 组件类型，从而访问该组件特有的属性和方法。
例如，下面的代码展示了如何根据 frame source 的不同使用不同的平面检测方法：
```
void PlaceObject(Vector2 touchPosition)
{
if (Session.Assembly.FrameSource is MotionTrackerFrameSource)
{
Ray ray = Session.Assembly.Camera.ScreenPointToRay(touchPosition);
if (Physics.Raycast(ray, out var hitInfo))
{
TouchRoot.transform.position = hitInfo.point;
}
}
else if (Session.Assembly.FrameSource is ARFoundationFrameSource)
{
var raycastManager = Session.Assembly.Origin.Value.GetComponent<UnityEngine.XR.ARFoundation.ARRaycastManager>();
var hits = new List<UnityEngine.XR.ARFoundation.ARRaycastHit>();
if (raycastManager.Raycast(touchPosition, hits, UnityEngine.XR.ARSubsystems.TrackableType.PlaneWithinPolygon))
{
var hitPose = hits[0].pose;
TouchRoot.transform.position = hitPose.position;
}
}
}
```
### 访问 frame filter 组件
可以使用 [ARAssembly.FrameFilters](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameFilters) 属性访问 frame filter 组件。在一个正常运行的 session 中，[ARAssembly.FrameFilters](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameFilters) 列表中的任何一个类型的组件都有可能有多个。
例如，下面的代码展示了如何获取 session 中的一个 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 并注册对应的事件：
```
var megaTracker = session.Assembly.FrameFilters.Where(f => f is MegaTrackerFrameFilter).FirstOrDefault() as MegaTrackerFrameFilter;
if (megaTracker)
{
megaTracker.LocalizationRespond += (response) =>
{
};
}
```
### 访问 camera 组件
可以使用 [ARAssembly.Camera](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Camera) 属性访问 camera 组件。如果场景中有多个 camera，这时一个找到 AR 使用的摄像机的快捷方式。
例如，下面的代码展示了如何获取 session 中的 camera 并对场景中的物体进行射线检测：
```
var ray = Session.Assembly.Camera.ScreenPointToRay(screenPoint);
if (Physics.Raycast(ray, out var hitInfo))
{
TouchRoot.transform.position = hitInfo.point;
};
```
### 访问 origin 组件
可以使用 [ARAssembly.Origin](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Origin) 属性访问 origin 组件。
例如，下面的代码展示了如何获取 session 中的 origin 并将一个代表当前摄像机位置和朝向的锥体显示在场景中：
```
if (session.Assembly.Origin.OnSome)
{
GameObject frustum = Instantiate(CameraFrustumPrefab, session.Assembly.Camera.transform.position, session.Assembly.Camera.transform.rotation);
frustum.transform.SetParent(session.Assembly.Origin.Value.transform);
}
```
需要注意的是，这里需要先判断 [ARAssembly.Origin](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Origin) 是否存在。
> **注意**
[ARAssembly.Origin](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Origin) 只在启用了运动跟踪功能的 session 中存在。
### 访问 CameraImageRenderer 组件
可以使用 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 属性访问 [CameraImageRenderer](../../../api/unity/easyar.CameraImageRenderer.html) 组件。
例如，下面这段代码可以获取物理相机图像的 [RenderTexture](https://docs.unity3d.com/ScriptReference/RenderTexture.html)：
```
RenderTexture renderTexture;
void Awake()
{
Session.StateChanged += (state) =>
{
if (state == ARSession.SessionState.Ready && Session.Assembly.CameraImageRenderer.OnSome)
{
Session.Assembly.CameraImageRenderer.Value.RequestTargetTexture((\_, texture) => renderTexture = texture);
}
};
}
```
需要注意的是，这里需要先判断 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 是否存在。
> **注意**
[ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 只在由 EasyAR 进行画面绘制的 session 中有效。一般来说，使用 AR Foundation 或头显时是无效的，这时物理相机画面的绘制由 AR Foundation 或头显 SDK 完成。
### 访问 FrameRecorder 组件
可以使用 [ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 属性访问 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html) 组件。
例如，下面这段代码可以启动录制，文件存储位置取决于配置，默认会存储在应用内存储目录中：
```
if (session.Assembly.FrameRecorder.OnSome)
{
var frameRecorder = session.Assembly.FrameRecorder.Value;
frameRecorder.enabled = true;
}
```
需要注意的是，这里需要先判断 [ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 是否存在。
> **注意**
[ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 在少数情况下，比如使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html) 时是不能使用的。
## 后续步骤
* 了解如何 [获取 session 的运行结果](session-output.html)，这些结果中包含了 AR 组件的运行输出
* 另外，您还可以通过下面这些示例来了解组件的访问：
* [Workflow\_ARSession 示例](sample-arsession.html) 展示了各种组件的访问和使用方法
## 相关主题
* [帧数据源](../cameras/frame-source.html) 描述了 frame source 以及运行时的选取方式
* [XR Origin](origin.html) 描述了 AR 场景中 origin 组件的用途
* [Camera](camera.html) 描述了 AR 场景中 camera 组件的用途
* [录制EIF文件](../simulation/recording.html) 描述了 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html) 的详细使用方法
