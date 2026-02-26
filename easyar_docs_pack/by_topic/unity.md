# EasyAR 专题包：unity

适用于上下文长度有限时的分卷输入。

## 目录
- `unity/cameras/comp-CameraDeviceFrameSource.md`
- `unity/cameras/comp-InertialCameraDeviceFrameSource.md`
- `unity/cameras/comp-ThreeDofCameraDeviceFrameSource.md`
- `unity/cameras/external-device-frame-source.md`
- `unity/cameras/external-frame-source.md`
- `unity/cameras/external-image-stream-frame-source.md`
- `unity/cameras/external-input-frame.md`
- `unity/cameras/frame-source-builtin.md`
- `unity/cameras/frame-source-group.md`
- `unity/cameras/frame-source.md`
- `unity/cameras/sample-camera-device.md`
- `unity/diagnostics/comp-DiagnosticsController.md`
- `unity/diagnostics/developer-mode.md`
- `unity/diagnostics/diagnostics.md`
- `unity/diagnostics/event-dump.md`
- `unity/diagnostics/report.md`
- `unity/diagnostics/ui-messages.md`
- `unity/fundamentals/active-control.md`
- `unity/fundamentals/arfoundation-scene-setup.md`
- `unity/fundamentals/arfoundation.md`
- `unity/fundamentals/camera-configs.md`
- `unity/fundamentals/camera.md`
- `unity/fundamentals/center-mode-choosing.md`
- `unity/fundamentals/center-mode.md`
- `unity/fundamentals/comp-ARSession.md`
- `unity/fundamentals/initialization.md`
- `unity/fundamentals/intro.md`
- `unity/fundamentals/origin-creation.md`
- `unity/fundamentals/origin.md`
- `unity/fundamentals/sample-arsession.md`
- `unity/fundamentals/session-assemble.md`
- `unity/fundamentals/session-components.md`
- `unity/fundamentals/session-creation.md`
- `unity/fundamentals/session-ctrl.md`
- `unity/fundamentals/session-output.md`
- `unity/fundamentals/session-report.md`
- `unity/fundamentals/session.md`
- `unity/fundamentals/setup-easyar.md`
- `unity/fundamentals/setup-player.md`
- `unity/fundamentals/target-state.md`
- `unity/fundamentals/target.md`
- `unity/fundamentals/unity-compatibility.md`
- `unity/fundamentals/unity-xr-switch.md`
- `unity/fundamentals/unity-xr.md`
- `unity/getting-started/diagnostics.md`
- `unity/getting-started/enable-easyar.md`
- `unity/getting-started/quickstart.md`
- `unity/getting-started/sample-launcher.md`
- `unity/getting-started/scene.md`
- `unity/getting-started/universal-render-pipeline.md`
- `unity/headsets/enable-headset.md`
- `unity/headsets/extension-bring-up.md`
- `unity/headsets/extension-dist.md`
- `unity/headsets/extension-imp.md`
- `unity/headsets/extension-template.md`
- `unity/headsets/extension.md`
- `unity/headsets/headsets.md`
- `unity/headsets/samples.md`
- `unity/headsets/setup-visionpro.md`
- `unity/headsets/setup-xreal.md`
- `unity/mega/comp-BlockController.md`
- `unity/mega/comp-BlockHolder.md`
- `unity/mega/comp-BlockRootController.md`
- `unity/mega/comp-MegaTrackerFrameFilter.md`
- `unity/mega/content-realworld-alignment.md`
- `unity/mega/enable-mega.md`
- `unity/mega/occlusion.md`
- `unity/mega/onsite-and-simulation.md`
- `unity/mega/quickstart.md`
- `unity/mega/session-best-practice.md`
- `unity/mega/target.md`
- `unity/mega/tracker.md`
- `unity/mega/verify-pc-camera.md`
- `unity/mega/verify-session-tool.md`
- `unity/motion-tracking/3rdparty-compatibility.md`
- `unity/motion-tracking/comp-ARCoreFrameSource.md`
- `unity/motion-tracking/comp-AREngineFrameSource.md`
- `unity/motion-tracking/comp-ARKitFrameSource.md`
- `unity/motion-tracking/comp-MotionTrackerFrameSource.md`
- `unity/release-notes/release-notes-v4.md`
- `unity/release-notes/release-notes.md`
- `unity/simulation/comp-FramePlayer.md`
- `unity/simulation/comp-FrameRecorder.md`
- `unity/simulation/playback.md`
- `unity/simulation/recording.md`
- `unity/simulation/simulation.md`
- `unity/simulation/tool.md`

---

## CameraDeviceFrameSource 组件参考
- 章节路径: `unity/cameras/comp-CameraDeviceFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/comp-CameraDeviceFrameSource.html

# CameraDeviceFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.CameraDeviceFrameSource.html)
>
探索 CameraDeviceFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/comp-CameraDeviceFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Camera Open Method**|打开物理相机时使用的方法。 选项：
* PreferredType（默认）：按照摄像头设备类型打开摄像头设备，如果没有匹配的类型则会尝试打开第一个摄像头设备。
* DeviceIndex：按照摄像头索引打开摄像头设备。
* SpecificType：按照精确的摄像头设备类型打开摄像头设备，如果没有匹配的类型则会失败。在 Mac 上，摄像头类型无法判别。|
|*Type*|Camera Open Method 是 PreferredType 或 SpecificType 时显示。
打开物理相机时使用的摄像头类型。选项：
* Back（默认）：后置摄像头。
* Front：前置摄像头。
* Unknown：未知位置。|
|*Index*|Camera Open Method 是 DeviceIndex 时显示。
打开物理相机时使用的设备索引。|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Default：使用默认值，实际选择与使用的 AR 功能有关。
* Input：使用指定值。选择 Input 时可选项：
* Normal：常规对焦模式，在这个模式下需要调用 [AutoFocus()](../../../api/unity/easyar.CameraDeviceFrameSource.html#u_easyar_CameraDeviceFrameSource_AutoFocus) 来触发对焦。
* Continousauto：连续自动对焦模式。
* Infinity：无穷远对焦模式。
* Macro：微距对焦模式。在这个模式下需要调用 [AutoFocus()](../../../api/unity/easyar.CameraDeviceFrameSource.html#u_easyar_CameraDeviceFrameSource_AutoFocus) 来触发对焦。
* Medium：中等距离对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Desired Camera Preference*|期望的 [CameraDevicePreference](../../../api/unity/easyar.CameraDevicePreference.html)。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* PreferObjectSensing：对图像跟踪和物体跟踪进行优化。
* PreferSurfaceTracking：对表面跟踪进行优化。
* PreferMotionTracking：对运动跟踪进行优化。|
|*Desired Android Camera Api*|期望的 Android Camera API。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Camera1：Android Camera1 API。
* Camera2：Android Camera2 API。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，如未设置会使用 Camera.main。|

---

## InertialCameraDeviceFrameSource 组件参考
- 章节路径: `unity/cameras/comp-InertialCameraDeviceFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/comp-InertialCameraDeviceFrameSource.html

# InertialCameraDeviceFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
>
探索 InertialCameraDeviceFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/comp-InertialCameraDeviceFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## ThreeDofCameraDeviceFrameSource 组件参考
- 章节路径: `unity/cameras/comp-ThreeDofCameraDeviceFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/comp-ThreeDofCameraDeviceFrameSource.html

# ThreeDofCameraDeviceFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
>
探索 ThreeDofCameraDeviceFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/comp-ThreeDofCameraDeviceFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## 创建图像和设备运动数据输入扩展
- 章节路径: `unity/cameras/external-device-frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-device-frame-source.html

# 创建图像和设备运动数据输入扩展
通过创建图像和设备运动数据输入扩展，开发者可以为 EasyAR Sense 扩展自定义的相机实现，从而支持特定的头显设备或其它输入设备。以下内容介绍了创建图像和设备运动数据输入扩展的步骤和注意事项。
## 开始之前
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
* 阅读 [外部帧数据源](external-frame-source.html) 了解创建外部帧数据源所需详细接口说明。
* 阅读 [外部输入帧数据](external-input-frame.html) 了解相机帧数据和渲染帧数据。
## 创建外部帧数据源类
* 如果需要创建 6DoF 设备输入扩展，继承 [ExternalDeviceMotionFrameSource](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html)
* 如果需要创建 3DoF 设备输入扩展，继承 [ExternalDeviceRotationFrameSource](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html)
它们都是 [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html) 的子类，文件名应与类名相同。
例如，创建一个 6DoF 设备输入扩展：
```
public class MyFrameSource : ExternalDeviceMotionFrameSource
{
}
```
在创建头显扩展时，可以使用 `com.easyar.sense.ext.hmdtemplate` 模板，在模板基础上进行修改。这个模板在从 EasyAR 网站下载获得的 Unity 插件压缩包内。
## 设备定义
重写 [IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD) 来定义设备是否是头显。
例如，在头显上设为 true。
```
public override bool IsHMD { get => true; }
```
重写 [Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display) 来定义设备的显示。
例如，在头显上默认的显示 [Display.DefaultHMDDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultHMDDisplay) 信息，这会定义显示旋转为 0。
```
protected override IDisplay Display => easyar.Display.DefaultHMDDisplay;
```
## 可用性
重写 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 来定义设备是否可用。
例如，[RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override Optional<bool> IsAvailable => Application.platform == RuntimePlatform.Android;
```
如果 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 在 session 组装时无法判断，可以重写 [CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程来阻塞组装过程，直到确定是否可用为止。
## session 原点
重写 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 来定义设备 SDK 定义的原点类型。
如果 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom)，还需要重写 [Origin](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_Origin) 。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override DeviceOriginType OriginType =>
#if EASYAR\_HAVE\_ROKID\_UXR
hasUXRComponents ? DeviceOriginType.None :
#endif
DeviceOriginType.XROrigin;
```
## 虚拟摄像机
如果 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom) 或 [None](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_None)，需要重写 [Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera) 来提供虚拟摄像机。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override Camera Camera => hasUXRComponents ? (cameraCandidate ? cameraCandidate : Camera.main) : base.Camera;
```
## 物理相机
使用 [DeviceFrameSourceCamera](../../../api/unity/easyar.DeviceFrameSourceCamera.html) 类型重写 [DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 以提供设备物理相机信息。这个数据会在输入相机帧数据时使用。[CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须完成创建。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
private DeviceFrameSourceCamera deviceCamera;
protected override List<FrameSourceCamera> DeviceCameras => new List<FrameSourceCamera> { deviceCamera };
{
var imageDimensions = new int[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetImageDimensions(imageDimensions);
size = new Vector2Int(imageDimensions[0], imageDimensions[1]);
deviceCamera = new DeviceFrameSourceCamera(CameraDeviceType.Back, 0, size, new Vector2(50, 50), new DeviceFrameSourceCamera.CameraExtrinsics(Pose.identity, true), AxisSystemType.Unity);
started = true;
}
```
重写 [CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 来提供相机帧开始输入的标识。
例如：
```
protected override bool CameraFrameStarted => started;
```
## session 启动和停止
重写 [OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_) 然后做 AR 独有的初始化工作。需要确保先调用 base.OnSessionStart。
例如：
```
protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
StartCoroutine(InitializeCamera());
}
```
这里是适合打开设备相机（比如 RGB 相机或 VST 相机等）的位置，尤其是如果这些相机没有被设计成要一直打开时。同时这里也是适合获取整个生命周期内不会变化的标定数据的位置。有时在这些数据可以被获取前可能需要等待设备准备好或等待数据更新。
同时，这里也是一个适合启动数据输入循环的位置。也可以在 [Update()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) 或其它方法中写这个循环，尤其是当数据需要在 Unity 执行顺序的某个特殊时间点获取的时候。在 session 准备好（ready）之前不要输入数据。
如果需要，也可以忽略启动过程并在每次更新时做数据检查，这完全取决于具体需求。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
private IEnumerator InitializeCamera()
{
yield return new WaitUntil(() => (RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() >= RokidTrackingStatus.Detecting && (RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() < RokidTrackingStatus.Tracking\_Paused);
var focalLength = new float[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetFocalLength(focalLength);
var principalPoint = new float[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetPrincipalPoint(principalPoint);
var distortion = new float[5];
RokidExtensionAPI.RokidOpenXR\_API\_GetDistortion(distortion);
var imageDimensions = new int[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetImageDimensions(imageDimensions);
size = new Vector2Int(imageDimensions[0], imageDimensions[1]);
var cameraParamList = new List<float> { focalLength[0], focalLength[1], principalPoint[0], principalPoint[1] }.Concat(distortion.ToList().GetRange(1, 4)).ToList();
cameraParameters = CameraParameters.tryCreateWithCustomIntrinsics(size.ToEasyARVector(), cameraParamList, CameraModelType.OpenCV\_Fisheye, CameraDeviceType.Back, 0).Value;
deviceCamera = new DeviceFrameSourceCamera(CameraDeviceType.Back, 0, size, new Vector2(50, 50), new DeviceFrameSourceCamera.CameraExtrinsics(Pose.identity, true), AxisSystemType.Unity);
RokidExtensionAPI.RokidOpenXR\_API\_OpenCameraPreview(OnCameraDataUpdate);
started = true;
}
```
重写 [OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop) 并释放资源，需要确保调用 base.OnSessionStop。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override void OnSessionStop()
{
base.OnSessionStop();
RokidExtensionAPI.RokidOpenXR\_API\_CloseCameraPreview();
started = false;
StopAllCoroutines();
cameraParameters?.Dispose();
cameraParameters = null;
deviceCamera?.Dispose();
deviceCamera = null;
}
```
## 输入相机帧数据
在获取相机帧数据更新后，调用 [HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Pose_easyar_MotionTrackingStatus_) / [HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Quaternion_) 来输入相机帧数据。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
private static void OnCameraDataUpdate(IntPtr ptr, int dataSize, ushort width, ushort height, long timestamp)
{
if (!instance) { return; }
if (ptr == IntPtr.Zero || dataSize == 0 || timestamp == 0) { return; }
if (timestamp == instance.curTimestamp) { return; }
instance.curTimestamp = timestamp;
RokidExtensionAPI.RokidOpenXR\_API\_GetHistoryCameraPhysicsPose(timestamp, positionCache, rotationCache);
var pose = new Pose
{
position = new Vector3(positionCache[0], positionCache[1], -positionCache[2]),
rotation = new Quaternion(-rotationCache[0], -rotationCache[1], rotationCache[2], rotationCache[3]),
};
// NOTE: Use real tracking status when camera exposure if possible when writing your own device frame source.
var trackingStatus = ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus()).ToEasyARStatus();
var size = instance.size;
var pixelSize = instance.size;
var pixelFormat = PixelFormat.Gray;
var yLen = pixelSize.x \* pixelSize.y;
var bufferBlockSize = yLen;
var bufferO = instance.TryAcquireBuffer(bufferBlockSize);
if (bufferO.OnNone) { return; }
var buffer = bufferO.Value;
buffer.tryCopyFrom(ptr, 0, 0, bufferBlockSize);
using (buffer)
using (var image = Image.create(buffer, pixelFormat, size.x, size.y, pixelSize.x, pixelSize.y))
{
instance.HandleCameraFrameData(instance.deviceCamera, timestamp \* 1e-9, image, instance.cameraParameters, pose, trackingStatus);
}
}
```
> **小心**
不要忘记在使用后执行 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 或通过 `using` 等机制释放 [Image](../../../api/unity/easyar.Image.html) 、[Buffer](../../../api/unity/easyar.Buffer.html) 以及其它相关数据。否则会出现严重内存泄漏，buffer pool 获取 buffer 也可能会失败。
## 输入渲染帧数据
在设备数据准备好之后，每个渲染帧调用 [HandleRenderFrameData(double, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Pose_easyar_MotionTrackingStatus_) / [HandleRenderFrameData(double, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Quaternion_) 来输入渲染帧数据。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected void LateUpdate()
{
if (!started) { return; }
if ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() < RokidTrackingStatus.Detecting) { return; }
if ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() >= RokidTrackingStatus.Tracking\_Paused) { return; }
InputRenderFrameMotionData();
}
private void InputRenderFrameMotionData()
{
var timestamp = RokidExtensionAPI.RokidOpenXR\_API\_GetCameraPhysicsPose(positionCache, rotationCache);
var pose = new Pose
{
position = new Vector3(positionCache[0], positionCache[1], -positionCache[2]),
rotation = new Quaternion(-rotationCache[0], -rotationCache[1], rotationCache[2], rotationCache[3]),
};
if (timestamp == 0) { return; }
HandleRenderFrameData(timestamp \* 1e-9, pose, ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus()).ToEasyARStatus());
}
```
## 后续步骤
* 创建 [头显扩展包](../headsets/extension.html)
## 相关主题
* [帧数据源和运行时选取过程](frame-source.html)
* [AR Session](../fundamentals/session.html)
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)

---

## Unity 中的自定义相机实现 —— 外部帧数据源
- 章节路径: `unity/cameras/external-frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-frame-source.html

# Unity 中的自定义相机实现 —— 外部帧数据源
通过外部帧数据源（[ExternalFrameSource](../../../api/unity/easyar.ExternalFrameSource.html)），开发者可以为 EasyAR Sense 扩展自定义的相机实现，从而支持特定的头显设备或其它输入设备。以下内容介绍了外部帧数据源的类型结构及接口定义。
## 开始之前
* 了解 [自定义相机](../../cameras/custom-camera.html) 的基本概念。
* 了解 [帧数据源](frame-source.html) 的基本概念、类型以及运行时的选取方法。
## 外部帧数据源类型
```
---
config:
class:
hideEmptyMembersBox: true
---
classDiagram
class FrameSource {
<<abstract>>
}
class ExternalFrameSource {
<<abstract>>
}
class ExternalDeviceFrameSource {
<<abstract>>
}
class ExternalDeviceMotionFrameSource:::EasyAR {
<<abstract>>
}
class ExternalDeviceRotationFrameSource:::EasyAR {
<<abstract>>
}
class ExternalImageStreamFrameSource:::EasyAR {
<<abstract>>
}
ExternalFrameSource --|> FrameSource
ExternalDeviceFrameSource --|> ExternalFrameSource
ExternalDeviceMotionFrameSource --|> ExternalDeviceFrameSource
ExternalDeviceRotationFrameSource --|> ExternalDeviceFrameSource
ExternalImageStreamFrameSource --|> ExternalFrameSource
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
```
上图展示了外部帧数据源的类型结构。
根据输入数据的不同，外部帧数据源可以分为两大类：
* 图像和设备运动数据输入扩展
* 通过继承 [ExternalDeviceMotionFrameSource](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html) 实现：设备及设备 SDK 提供 6DoF 运动跟踪功能。虚拟摄像机的 transform 及其它控制由设备 SDK 完成。
* 通过继承 [ExternalDeviceRotationFrameSource](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html) 实现：设备及设备 SDK 提供 3DoF 旋转跟踪功能。虚拟摄像机的 transform 及其它控制由设备 SDK 完成。
* 图像输入扩展
* 通过继承 [ExternalImageStreamFrameSource](../../../api/unity/easyar.ExternalImageStreamFrameSource.html) 实现：仅提供图像输入。虚拟摄像机的 transform 及其它控制由 EasyAR 完成。
接入这几种外部帧数据源时，可以使用的 AR 功能有所不同：
* 图像和设备运动数据输入扩展 [ExternalDeviceMotionFrameSource](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html)
* Mega
* 运动跟踪（由设备自身提供）
* 稀疏空间地图
* 稠密空间地图
* 图像跟踪（支持运动融合）
* 图像云识别
* 物体跟踪（支持运动融合）
* 图像和设备运动数据输入扩展 [ExternalDeviceRotationFrameSource](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html)
* Mega
* 图像跟踪（不支持运动融合）
* 图像云识别
* 物体跟踪（不支持运动融合）
* 图像输入扩展 [ExternalImageStreamFrameSource](../../../api/unity/easyar.ExternalImageStreamFrameSource.html)
* 图像跟踪（不支持运动融合）
* 图像云识别
* 物体跟踪（不支持运动融合）
## 外部帧数据源接口定义
创建外部帧数据源时，必须实现相关接口。下面介绍了这些接口的定义及使用方法。
### 设备定义
* [FrameSource.IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD)：`定义是否为头显`
在且仅在头显设备上设为 true。
如果设备是头显，诊断信息将显示在摄像机前的 3D 板子而非屏幕上。部分 AR 功能在头显设备上运行会有些许不同。
* [FrameSource.Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display)：`定义显示系统`
提供当前显示的旋转等信息。
可以使用 [Display.DefaultSystemDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultSystemDisplay) 或 [Display.DefaultHMDDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultHMDDisplay) 来获取默认的显示信息。
通常在头显上可以使用 [Display.DefaultHMDDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultHMDDisplay)。
无额外设置。
* [FrameSource.IsCameraUnderControl](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsCameraUnderControl)：必须设置为 true。
### 可用性
* [FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable)：`可用性（Availability）`
用于判断 frame source 是否可以使用。
如果一个 frame source 在当前运行设备或环境下不可用，该数值应为 false。
如果该数值等于 Optional<bool>.Empty，[FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程会被调用，应在协程结束前更新 [FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable)。
可用性接口会在 session 组装时使用，不可用的组件将不会被选择且它的方法在 session 运行时不会被调用。
* [FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability)（可选）：`检查 frame source 是否可用的协程`
[FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 等于 Optional<bool>.Empty 时会被调用。在该协程结束前，session 的组装过程会被阻塞。
### session 原点
* [ExternalDeviceFrameSource.OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType)：`原点类型`
* [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin)：设备 SDK 使用 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 作为原点。
* [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom)：设备 SDK 使用自定义的原点。
需指定 [ExternalDeviceFrameSource.Origin](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_Origin)。
* [None](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_None)：设备 SDK 未定义原点。
这时原点将会自动从场景中选择或创建，但不会移动。
session 将只支持 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式。应用开发者必须对于他们如何摆放虚拟物体十分小心，因为所有 target 及 target 下的内容永远都会在 Unity 坐标系中移动，用户的部分内容（比如物理系统）将无法正常工作。所有放在 Unity 世界坐标系下的物体在任何配置下都永远不可能显示在正确的位置。
* [ExternalDeviceFrameSource.Origin](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_Origin)：`原点物体`
在且仅在 [ExternalDeviceFrameSource.OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 为 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom) 时定义自己的原点，其它时候不需要重新定义。
无。
### 虚拟摄像机
* [FrameSource.Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera)：`虚拟摄像机`
摄像机不受 session 控制，摄像机的 transform 和投影矩阵以及图像背景渲染应由外部代码控制。
仅在头显上该摄像机会被使用，用于将一些诊断文字展示在眼前。
在 [ExternalDeviceFrameSource.OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin) 时不需要定义，EasyAR 会自动使用 Unity XR 框架中定义的相机。
* [FrameSource.Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera)：`虚拟摄像机`
摄像机会受 session 控制，外部代码不能修改摄像机的 transform 和投影矩阵。
在头显上，该摄像机会用于将一些诊断文字展示在眼前。
### 物理相机
* [FrameSource.DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras)：`物理相机参数`
提供相机帧数据的物理相机。如果相机帧数据由多个相机提供，列表中需要包含所有物理相机。
需要确保在 [FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时可以获取到正确的物理相机参数。
* [FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted)：`相机帧是否开始输入`
在物理相机准备好并可以输入数据到 EasyAR 之后返回 true，物理相机停止运行后返回 false。在 [FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 false 时，EasyAR 不会工作。[FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须保证 [FrameSource.DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 数据可以访问且不间断地向 EasyAR 输入相机帧数据。在 EasyAR 检查到相机帧连续长时间无输入后会弹出警告，辅助用户判断功能无响应时进行问题解耦。
物理相机参数需要与真实设备相机相同。
* [FrameSourceCamera.CameraType](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraType)：`物理相机类型`
一般非前置相机的情况，比如头显上，选择后置相机。
* [FrameSourceCamera.CameraOrientation](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraOrientation)：`物理相机图像在设备的自然方向上显示时需要顺时针旋转的角度`
范围为 [0, 360)。
* [FrameSourceCamera.FrameSize](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameSize)：`图像尺寸`
* [FrameSourceCamera.FrameRateRange](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameRateRange)：`帧率范围`
定义 x 为帧率范围下界 y 为帧率范围上界。
* [DeviceFrameSourceCamera.AxisSystem](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_AxisSystem)：`头/物理相机 pose 以及物理相机外参使用的坐标轴系统`
所有矩阵必须使用相同的坐标轴系统。如果使用的数据定义不符合已知的系统，需要在传给 EasyAR 之前进行坐标轴变换。
* [DeviceFrameSourceCamera.Extrinsics](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_Extrinsics)：`物理相机外参`
一般是标定的矩阵。其坐标轴应符合 [DeviceFrameSourceCamera.AxisSystem](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_AxisSystem) 定义。如果外参的坐标轴定义与实际 pose 的坐标轴定义不同或它们不符合 [DeviceFrameSourceCamera.AxisSystem](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_AxisSystem) 的定义，需要在设置这个数值之前进行坐标轴变换。
物理相机参数需要与真实设备相机相同。如果是通过视频文件等输入，需要与录制视频时的物理相机或等价相机模型参数相同。
* [FrameSourceCamera.CameraType](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraType)：`物理相机类型`
一般非前置相机的情况，比如头显上，选择后置相机。
* [FrameSourceCamera.CameraOrientation](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraOrientation)：`物理相机图像在设备的自然方向上显示时需要顺时针旋转的角度`
范围为 [0, 360)。
* [FrameSourceCamera.FrameSize](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameSize)：`图像尺寸`
* [FrameSourceCamera.FrameRateRange](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameRateRange)：`帧率范围`
定义 x 为帧率范围下界 y 为帧率范围上界。
### session 启动和停止
* [FrameSource.OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_)：`处理 session 启动事件`
在 session 组装时选择了这个 frame source 时有效。
可以用于延迟初始化，在这个方法中进行 AR 独有的初始化工作。
* [FrameSource.OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop)：`处理 session 停止事件`
在 session 组装时选择了这个 frame source 时有效。
可以在这个方法中销毁 [FrameSource.OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_) 以及 session 运行中创建的资源并恢复内部状态。在 session 销毁之前这个方法会被保证调用。如果 frame source 在 session 之前销毁，它将不会被调用，且 session 将进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态。
### 输入帧
* [ExternalDeviceMotionFrameSource.HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Pose_easyar_MotionTrackingStatus_)：`输入相机帧数据`
* [ExternalDeviceRotationFrameSource.HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Quaternion_)：`输入相机帧数据`
可以在任何线程调用，只要设备 SDK 的 API 都是线程安全的即可。
这些数据需要与物理相机传感器曝光时的数据一致。建议输入 30 或 60 fps 的数据。最小可接受帧率为 2，但部分算法响应时间会受影响。只要可以获取，建议输入彩色数据，这对 Mega 的效果是有帮助的。
为实现最佳效率，可以设计整个数据链条让原始 YUV 数据直接通过共享内存透传，并直接使用数据指针传入 EasyAR，并注意数据所有权。
* [ExternalDeviceMotionFrameSource.HandleRenderFrameData(double, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Pose_easyar_MotionTrackingStatus_)：`输入渲染帧数据`
* [ExternalDeviceRotationFrameSource.HandleRenderFrameData(double, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Quaternion_)：`输入渲染帧数据`
需要确保在设备数据准备好之后每个渲染帧调用，不能跳帧。这些数据需要与驱动同一帧内当前 Unity 虚拟摄像机的数据一致。
* [ExternalImageStreamFrameSource.HandleCameraFrameData(double, Image, CameraParameters)](../../../api/unity/easyar.ExternalImageStreamFrameSource.html#u_easyar_ExternalImageStreamFrameSource_HandleCameraFrameData_System_Double_easyar_Image_easyar_CameraParameters_)：`输入相机帧数据`
可以在任何线程调用，只要设备 SDK 的 API 都是线程安全的即可。
这些数据需要与物理相机传感器曝光时的数据一致。建议输入 30 或 60 fps 的数据。最小可接受帧率为 2，但部分算法响应时间会受影响。只要可以获取，建议输入彩色数据，这对 Mega 的效果是有帮助的。
为实现最佳效率，可以设计整个数据链条让原始 YUV 数据直接通过共享内存透传，并直接使用数据指针传入 EasyAR，并注意数据所有权。
* [ExternalFrameSource.TryAcquireBuffer(int)](../../../api/unity/easyar.ExternalFrameSource.html#u_easyar_ExternalFrameSource_TryAcquireBuffer_System_Int32_)：`尝试从内存池中获取内存块`
这个内存块通常用于存储相机帧的图像数据并输入 EasyAR。
* [ExternalFrameSource.ReceivedFrameCount](../../../api/unity/easyar.ExternalFrameSource.html#u_easyar_ExternalFrameSource_ReceivedFrameCount)：`EasyAR 获取到的相机帧计数`
EasyAR 会用它来检查设备相机帧输入的健康情况。可以在调试中使用，如果这个数值停止增长，通常说明设备停止向 EasyAR 输入数据。
### Unity 消息
在脚本中使用以下消息时，需要注意确保基类实现被调用：
* [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html)
* [OnApplicationPause(Boolean)](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnApplicationPause.html)
* [OnDestroy()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnDestroy.html)
## 后续步骤
* 阅读 [外部输入帧数据](external-input-frame.html) 了解相机帧数据和渲染帧数据
* 创建 [图像和设备运动数据输入扩展](external-device-frame-source.html)
* 创建 [图像输入扩展](external-image-stream-frame-source.html)
## 相关主题
* [AR Session](../fundamentals/session.html)
* [Camera](../fundamentals/camera.html)
* [XR Origin](../fundamentals/origin.html)
* [中心模式](../fundamentals/center-mode.html)
* [EasyAR 的头显支持](../../headsets/headsets.html)

---

## 创建图像输入扩展
- 章节路径: `unity/cameras/external-image-stream-frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-image-stream-frame-source.html

# 创建图像输入扩展
## 开始之前
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
* 阅读 [外部帧数据源](external-frame-source.html) 了解创建外部帧数据源所需详细接口说明。
* 阅读 [外部输入帧数据](external-input-frame.html) 了解相机帧数据和渲染帧数据。
## 创建外部帧数据源类
继承 [ExternalImageStreamFrameSource](../../../api/unity/easyar.ExternalImageStreamFrameSource.html) 来创建图像输入扩展。它是 [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html) 的子类，文件名应与类名相同。
例如：
```
public class MyFrameSource : ExternalImageStreamFrameSource
{
}
```
示例 Workflow\_FrameSource\_ExternalImageStream 就是一个基于手机上使用 ARCore 录制的视频作为输入的图像输入扩展实现。该视频是使用 Pixel2 上的 ARCore 通过相机回调方式采集的（不是屏幕录制）。
## 设备定义
重写 [IsCameraUnderControl](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsCameraUnderControl) 并返回 true。
重写 [IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD) 来定义设备是否是头显。
例如，使用视频作为输入时设为 false。
```
protected override bool IsHMD => false;
```
重写 [Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display) 来定义设备的显示。
例如，如果只在手机上运行，可以[Display.DefaultSystemDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultSystemDisplay)，它的旋转值根据操作系统当前显示状态而自动改变。
```
protected override IDisplay Display => easyar.Display.DefaultSystemDisplay;
```
## 可用性
重写 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 来定义设备是否可用。
例如，使用视频作为输入时始终可用：
```
protected override Optional<bool> IsAvailable => true;
```
如果 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 在 session 组装时无法判断，可以重写 [CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程来阻塞组装过程，直到确定是否可用为止。
## 虚拟摄像机
重写 [Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera) 来提供虚拟摄像机。
例如，有时可用使用 [Camera.main](https://docs.unity3d.com/ScriptReference/Camera-main.html) 作为 session 的虚拟摄像机：
```
protected override Camera Camera => Camera.main;
```
## 物理相机
使用 [FrameSourceCamera](../../../api/unity/easyar.FrameSourceCamera.html) 类型重写 [DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 以提供设备物理相机信息。这个数据会在输入相机帧数据时使用。[CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须完成创建。
例如，使用示例 Workflow\_FrameSource\_ExternalImageStream 中所使用的视频：
```
private FrameSourceCamera deviceCamera;
protected override List<FrameSourceCamera> DeviceCameras => new List<FrameSourceCamera> { deviceCamera };
{
var size = new Vector2Int(640, 360);
var cameraType = CameraDeviceType.Back;
var cameraOrientation = 90;
deviceCamera = new FrameSourceCamera(cameraType, cameraOrientation, size, new Vector2(30, 30));
started = true;
}
```
> **小心**
这里的几个输入参数需要根据实际使用的视频来设置。上面代码中的参数只适用于示例中的视频。
重写 [CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 来提供相机帧开始输入的标识。
例如：
```
protected override bool CameraFrameStarted => started;
```
## session 启动和停止
重写 [OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_) 然后做 AR 独有的初始化工作。需要确保先调用 base.OnSessionStart。
例如：
```
protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
...
}
```
这里是适合打开设备相机的位置，尤其是如果这些相机没有被设计成要一直打开时。同时这里也是适合获取整个生命周期内不会变化的标定数据的位置。有时在这些数据可以被获取前可能需要等待设备准备好或等待数据更新。
同时，这里也是一个适合启动数据输入循环的位置。也可以在 [Update()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) 或其它方法中写这个循环，尤其是当数据需要在 Unity 执行顺序的某个特殊时间点获取的时候。在 session 准备好（ready）之前不要输入数据。
如果需要，也可以忽略启动过程并在每次更新时做数据检查，这完全取决于具体需求。
例如，使用视频作为输入时可以在这里开始播放视频并启动数据输入循环：
```
protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
...
player.Play();
StartCoroutine(VideoDataToInputFrames());
}
```
重写 [OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop) 并释放资源，需要确保调用 base.OnSessionStop。
例如，使用视频作为输入时可以在这里停止视频播放并释放相关资源：
```
protected override void OnSessionStop()
{
base.OnSessionStop();
StopAllCoroutines();
player.Stop();
if (renderTexture) { Destroy(renderTexture); }
cameraParameters?.Dispose();
cameraParameters = null;
frameIndex = -1;
started = false;
deviceCamera?.Dispose();
deviceCamera = null;
}
```
## 从设备或文件获取相机帧数据
可以从系统相机、USB 相机、视频文件、网络等任意来源获取图像。只要能将数据转换成 [Image](../../../api/unity/easyar.Image.html) 所需的格式即可。从这些设备或文件获取数据的方式各不相同，需要参考相关设备或文件的使用说明。
例如，使用视频作为输入时，可以使用 [Texture2D.ReadPixels(Rect, int, int, bool)](https://docs.unity3d.com/ScriptReference/Texture2D.ReadPixels.html) 从视频播放器的 RenderTexture 中获取相机帧数据，然后复制 [Texture2D.GetRawTextureData()](https://docs.unity3d.com/ScriptReference/Texture2D.GetRawTextureData.html) 的数据到 [Buffer](../../../api/unity/easyar.Buffer.html) 中：
```
void VideoDataToInputFrames()
{
...
RenderTexture.active = renderTexture;
var pixelSize = new Vector2Int((int)player.width, (int)player.height);
var texture = new Texture2D(pixelSize.x, pixelSize.y, TextureFormat.RGB24, false);
texture.ReadPixels(new Rect(0, 0, pixelSize.x, pixelSize.y), 0, 0);
texture.Apply();
RenderTexture.active = null;
...
CopyRawTextureData(buffer, texture.GetRawTextureData<byte>(), pixelSize);
}
static unsafe void CopyRawTextureData(Buffer buffer, Unity.Collections.NativeArray<byte> data, Vector2Int size)
{
int oneLineLength = size.x \* 3;
int totalLength = oneLineLength \* size.y;
var ptr = new IntPtr(data.GetUnsafeReadOnlyPtr());
for (int i = 0; i < size.y; i++)
{
buffer.tryCopyFrom(ptr, oneLineLength \* i, totalLength - oneLineLength \* (i + 1), oneLineLength);
}
}
```
> **小心**
如上面代码中一样，从 [Texture2D](https://docs.unity3d.com/ScriptReference/Texture2D.html) 的指针中复制的数据需要上下反转之后，数据的内存排列才是正常的图像。
在获取图像的同时，还需要获取相机或等效相机的标定数据并创建 [CameraParameters](../../../api/unity/easyar.CameraParameters.html) 实例。
如果数据的原始来源来自手机的相机回调，且数据没有人工裁剪，那么可以直接使用手机相机的标定数据。在使用 ARCore 或 ARKit 等接口获取相机回调数据时，可以参考相关文档获取相机内参。如果需要使用的 AR 功能是图像跟踪或物体跟踪，这种情况也可以使用 [CameraParameters.createWithDefaultIntrinsics(Vec2I, CameraDeviceType, int)](../../../api/unity/easyar.CameraParameters.html#u_easyar_CameraParameters_createWithDefaultIntrinsics_easyar_Vec2I_easyar_CameraDeviceType_System_Int32_) 来创建相机内参，这时算法效果会受到轻微影响，但一般影响不大。
如果数据来自 USB 相机或非相机回调生成的视频文件等其他来源，则需要对相机或视频帧进行标定以获取正确的内参。
> **小心**
相机回调数据不能裁剪，裁剪后需要重新计算内参。如果数据来自屏幕录制等方式获取的图像数据，通常无法使用手机相机的标定数据，这时也需要对相机或视频帧进行标定以获取正确的内参。
内参不正确会导致 AR 功能无法正常使用，常见虚拟内容与现实物体无法对齐，以及 AR 跟踪不容易成功或很容易丢失等。
例如，使用示例 Workflow\_FrameSource\_ExternalImageStream 中所使用的视频，其对应的相机内参及 [CameraParameters](../../../api/unity/easyar.CameraParameters.html) 创建过程如下：
```
var size = new Vector2Int(640, 360);
var cameraType = CameraDeviceType.Back;
var cameraOrientation = 90;
cameraParameters = new CameraParameters(size.ToEasyARVector(), new Vec2F(506.085f, 505.3105f), new Vec2F(318.1032f, 177.6514f), cameraType, cameraOrientation);
```
> **小心**
上面代码中的参数只适用于示例中的视频，该相机内参与视频是在同一时间采集的。如果需要使用其他视频或设备的数据，务必同时获取设备内参或手动进行标定。
## 输入相机帧数据
在获取相机帧数据更新后，调用 [HandleCameraFrameData(double, Image, CameraParameters)](../../../api/unity/easyar.ExternalImageStreamFrameSource.html#u_easyar_ExternalImageStreamFrameSource_HandleCameraFrameData_System_Double_easyar_Image_easyar_CameraParameters_) 来输入相机帧数据。
例如，使用视频作为输入时实现如下：
```
IEnumerator VideoDataToInputFrames()
{
yield return new WaitUntil(() => player.isPrepared);
var pixelSize = new Vector2Int((int)player.width, (int)player.height);
...
yield return new WaitUntil(() => player.isPlaying && player.frame >= 0);
while (true)
{
yield return null;
if (frameIndex == player.frame) { continue; }
frameIndex = player.frame;
...
var pixelFormat = PixelFormat.RGB888;
var bufferO = TryAcquireBuffer(pixelSize.x \* pixelSize.y \* 3);
if (bufferO.OnNone) { continue; }
var buffer = bufferO.Value;
CopyRawTextureData(buffer, texture.GetRawTextureData<byte>(), pixelSize);
using (buffer)
using (var image = Image.create(buffer, pixelFormat, pixelSize.x, pixelSize.y, pixelSize.x, pixelSize.y))
{
HandleCameraFrameData(player.time, image, cameraParameters);
}
}
}
```
> **小心**
不要忘记在使用后执行 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 或通过 `using` 等机制释放 [Image](../../../api/unity/easyar.Image.html) 、[Buffer](../../../api/unity/easyar.Buffer.html) 以及其它相关数据。否则会出现严重内存泄漏，buffer pool 获取 buffer 也可能会失败。
## 相关主题
* [帧数据源和运行时选取过程](frame-source.html)
* [AR Session](../fundamentals/session.html)
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)

---

## 外部帧数据源的输入帧数据要求
- 章节路径: `unity/cameras/external-input-frame.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-input-frame.html

# 外部帧数据源的输入帧数据要求
为使外部帧数据源正常工作，最重要的工作同时也是最棘手的部分是确保数据正确性。本文介绍了外部帧数据源的输入帧数据要求。
## 开始之前
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
* 了解 [外部帧数据源](external-frame-source.html) 的基本概念和常见类型。
## 输入帧数据类型
在 Unity 中，外部帧数据源通常需要在两个不同时间接收不同的数据，根据外部数据输入时间和数据特征，我们将这两组数据称为：
1. 相机帧数据（camera frame data）
2. 渲染帧数据（rendering frame data）
不同类型的外部帧数据源对这两组数据的需求不同：
* 图像和设备运动数据输入扩展：同时需要相机帧数据及渲染帧数据
* 图像输入扩展：只需要相机帧数据
## 相机帧数据
数据需求：
1. 时间戳（timestamp）
2. 原始物理相机图像数据（raw camera image data）
3. 内参（intrinsics，包括图像大小、焦距、主点。如果有畸变还需要畸变模型和畸变参数）
4. 外参（extrinsics，Tcw 或 Twc，标定的矩阵，表达物理相机相对设备/头的 pose 原点的物理偏移）
5. 跟踪状态（tracking status）
6. 设备位姿（device pose）
1. 时间戳（timestamp）
2. 原始物理相机图像数据（raw camera image data）
3. 内参（intrinsics，包括图像大小、焦距、主点。如果有畸变还需要畸变模型和畸变参数）
数据时间：
* 物理相机曝光中点
数据使用：
* API 调用时间：可根据外部代码的设计改变。一个大多数设备使用的常规方法是在 3D 引擎的渲染更新中查询，然后根据设备数据的时间戳来判断是否进一步进行数据处理
* API 调用线程：3D 引擎的 game thread 或任何其它线程（如果使用到的所有外部 API 都是线程安全的）
Unity 中 API 调用示例如下：
```
void TryInputCameraFrameData()
{
double timestamp;
if (timestamp == curTimestamp) { return; }
curTimestamp = timestamp;
PixelFormat format;
Vector2Int size;
Vector2Int pixelSize;
int bufferSize;
var bufferO = TryAcquireBuffer(bufferSize);
if (bufferO.OnNone) { return; }
var buffer = bufferO.Value;
IntPtr imageData;
buffer.tryCopyFrom(imageData, 0, 0, bufferSize);
var historicalHeadPose = new Pose();
MotionTrackingStatus trackingStatus = (MotionTrackingStatus)(-1);
using (buffer)
using (var image = Image.create(buffer, format, size.x, size.y, pixelSize.x, pixelSize.y))
{
HandleCameraFrameData(deviceCamera, timestamp, image, cameraParameters, historicalHeadPose, trackingStatus);
}
}
```
```
void TryInputCameraFrameData()
{
double timestamp;
if (timestamp == curTimestamp) { return; }
curTimestamp = timestamp;
PixelFormat format;
Vector2Int size;
Vector2Int pixelSize;
int bufferSize;
var bufferO = TryAcquireBuffer(bufferSize);
if (bufferO.OnNone) { return; }
var buffer = bufferO.Value;
IntPtr imageData;
buffer.tryCopyFrom(imageData, 0, 0, bufferSize);
var historicalHeadPose = new Pose();
MotionTrackingStatus trackingStatus = (MotionTrackingStatus)(-1);
using (buffer)
using (var image = Image.create(buffer, format, size.x, size.y, pixelSize.x, pixelSize.y))
{
HandleCameraFrameData(timestamp, image, cameraParameters);
}
}
```
## 渲染帧数据
数据需求：
1. 时间戳（timestamp）
2. 跟踪状态（tracking status）
3. 设备位姿（device pose）
无。
数据时间：
* 上屏时刻。TimeWarp 不计算在内。相同时刻的 device pose 数据会由外部（比如设备 SDK）用来设置虚拟摄像机的 transform 以渲染当前帧。
> **注意**
TimeWarp（有时也称为 Reprojection 或 ATW/PTW）是 VR/AR 头显中常用的一种降低延迟的技术。它会在渲染完成后，根据最新的头部位姿对图像进行再次扭曲变换，以补偿渲染期间产生的头部运动。EasyAR 需要的是渲染开始时用于设置虚拟摄像机的位姿对应的时刻，而不是 TimeWarp 后实际上屏的时刻。
数据使用：
* API 调用时间：3D 引擎的每个渲染帧
* API 调用线程：3D 引擎的 game thread
Unity 中 API 调用示例如下：
```
private void InputRenderFrameMotionData()
{
double timestamp = 0e-9;
var headPose = new Pose();
MotionTrackingStatus trackingStatus = (MotionTrackingStatus)(-1);
HandleRenderFrameData(timestamp, headPose, trackingStatus);
}
```
## 数据要求细节
物理相机图像数据：
* 图像坐标系：在传感器水平时获取的数据也应是水平的。数据应该以左上角为原点，行优先存储。图像不应翻转或颠倒。
* 图像 FPS：正常 30 或 60 fps 的数据都可以。如果高 fps 有特殊影响，为达到合理的算法效果，最小可接受帧率为 2。建议使用高于 2 的 fps，通常情况下使用原始数据帧率即可。
* 图像尺寸：为获取更好的计算结果，最大边应为 960 或更大。正常不鼓励在数据链路中进行耗时的图像缩放，建议直接使用原始数据，除非完整大小的数据拷贝时间已经长得无法接受。图像分辨率不能小于 640\*480。
* 像素格式：优先跟踪效果并综合考虑性能，通常格式优先顺序为 YUV > RGB > RGBA > Gray （YUV中的Y分量）。在使用 YUV 数据时，需要完整的数据定义，包括数据封装和填充细节。相较单通道图像而言，使用彩色图像 Mega 的效果会更好，但其它功能影响不大。
* 数据访问：数据指针或等价实现。最好在数据链路中消除所有可能的非必须拷贝。HandleRenderFrameData 中 EasyAR 复制一份数据，之后异步使用，该同步调用完成后就不再使用图像数据。注意数据所有权。
时间戳：
* 所有时间戳都应时钟同步，最好是硬件同步。数据单位是秒，但精度要求达到纳秒或尽可能高。
跟踪状态：
* 跟踪状态由设备定义，需要包含跟踪丢失（VIO不可用）的状态。如有更多等级则更好。
设备位姿：
* 所有 pose（包括 3D 引擎中虚拟摄像机的 transform）都应使用同一个原点。
* 所有 pose 以及外参应该使用相同的坐标轴系统。
* 在 Unity 中，pose 数据的坐标轴系统类型应为 Unity 坐标轴系统或 EasyAR 坐标轴系统。如果输入扩展由 EasyAR 实现且使用了其它坐标轴系统定义方式，应提供清晰的坐标轴系统定义或给出转换到 Unity 坐标轴系统或 EasyAR 坐标轴系统的方法。
* 在 Unity 中，如果使用 Unity XR 框架，只需要兼容 [XROrigin.TrackingOriginMode.Device](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.TrackingOriginMode.html#Unity_XR_CoreUtils_XROrigin_TrackingOriginMode_Device) 模式即可。
内参：
* 所有数值都应与图像数据匹配。如有需要应在输入 EasyAR 之前对内参进行缩放。
* 如果输入扩展由 EasyAR 实现，应说明内参是否会在每一帧变化（区别是对应 API 应该调用一次还是每帧调用）。
外参：
* 在头显上必须提供真实数据。
* 它是一个标定矩阵，表达物理相机相对设备/头的 pose 原点的物理偏移。如果设备的 pose 和物理相机 pose 相等，它应该是单位阵。
* Apple Vision Pro 对应接口为： [CameraFrame.Sample.Parameters.extrinsics](https://developer.apple.com/documentation/arkit/cameraframe/sample/parameters/4443449-extrinsics)，需要注意其数据定义与接口所需数据有区别，EasyAR 内部是进行转换之后再使用的。
* 在 Unity 中，外参的坐标轴系统类型应为 Unity 坐标轴系统或 EasyAR 坐标轴系统。如果输入扩展由 EasyAR 实现且使用了其它坐标轴系统定义方式，应提供清晰的坐标轴系统定义或给出转换到 Unity 坐标轴系统或 EasyAR 标轴系统的方法。
* 在头显设备中，通常存在多个不同定义的坐标系，这个不同可能包括坐标轴原点、朝向、左右手表达等。外参应在同一坐标系下计算，该接口数据需要同一坐标系下的坐标变换，而非两个不同定义的坐标系的变换矩阵。
性能：
* 数据应以最优效率提供。在大多数实现中，API 调用会发生在渲染过程，所以建议即使在底层需要进行耗时操作的情况下，也不要阻塞 API 调用，或者以合理的方式来使用这些 API。
* 如果输入扩展由 EasyAR 实现，需要对所有耗时 API 调用进行说明。
多相机：
* 至少一个相机的数据是需要的。这个相机可以是 RGB 相机、VST 相机、定位相机等中的任意一个。在头显上如果只输入一个相机的数据，通常推荐使用在中央或在眼睛附近的 RGB 相机或 VST 相机。
* 使用多相机可提升 EasyAR 算法效果。所有可用相机某一时刻的相机帧数据应在在同一个时间点同时输入。
>
> 多相机目前尚未完全支持，可以联系 EasyAR 获取更多细节。
>
## 后续步骤
* 创建 [图像和设备运动数据输入扩展](external-device-frame-source.html)
* 创建 [图像输入扩展](external-image-stream-frame-source.html)
* 创建 [头显扩展包](../headsets/extension.html)
## 相关主题
* [EasyAR 坐标系](../../native/fundamentals/coordinates.html)
* 图像输入扩展示例 Workflow\_FrameSource\_ExternalImageStream

---

## 内置 Frame Source 组件
- 章节路径: `unity/cameras/frame-source-builtin.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source-builtin.html

# 内置 Frame Source 组件
探索内置 Frame Source 组件窗口中的各项属性以自定义相机参数。
|接口|组件参考|
|[CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|[CameraDeviceFrameSource 组件参考](comp-CameraDeviceFrameSource.html)|
|[EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|[CameraDeviceFrameSource 组件参考](comp-CameraDeviceFrameSource.html)|
|[FramePlayer](../../../api/unity/easyar.FramePlayer.html)|[FramePlayer 组件参考](../simulation/comp-FramePlayer.html)|
|[ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)|[ThreeDofCameraDeviceFrameSource 组件参考](comp-ThreeDofCameraDeviceFrameSource.html)|
|[InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)|[InertialCameraDeviceFrameSource 组件参考](comp-InertialCameraDeviceFrameSource.html)|
|[MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)|[MotionTrackerFrameSource 组件参考](../motion-tracking/comp-MotionTrackerFrameSource.html)|
|[ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)|[ARCoreFrameSource 组件参考](../motion-tracking/comp-ARCoreFrameSource.html)|
|[ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)|[ARKitFrameSource 组件参考](../motion-tracking/comp-ARKitFrameSource.html)|
|[AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)|[AREngineFrameSource 组件参考](../motion-tracking/comp-AREngineFrameSource.html)|
|[VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)||
|[XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)||
|[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)||
|[ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)||

---

## 添加一组帧数据源
- 章节路径: `unity/cameras/frame-source-group.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source-group.html

# 添加一组帧数据源
一个 AR Session 可以包含多个帧数据源组件，称为帧数据源组（frame source group）。在运行时，session 会根据当前设备和启用的 AR 功能，从帧数据源组中选取一个最合适的帧数据源进行使用。本文介绍了如何使用和管理帧数据源组。
## 开始之前
* 了解 [帧数据源](frame-source.html) 的基本概念、类型以及运行时的选取方法。
## 使用预设 AR Session 的帧数据源组
[使用默认配置创建的 session](../fundamentals/session-creation.html) 会自带一组帧数据源，在使用单一 AR 功能时，一般就足够了。
不同预设 session 中所包含的帧数据源不同。
>
> 使用
[> ARSessionFactory.ARSessionPreset.ImageTracking
](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTracking)> 预设或
`> AR Session (Image Tracking Preset)
`> 菜单创建的 session 中只有单个帧数据源：
>
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-image-tracking.png)
>
> 使用
[> ARSessionFactory.ARSessionPreset.MegaBlock_MotionTracking_Inertial
](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)> 预设或
`> AR Session (Mega Block Default Preset)
`> 菜单创建的 session 中包含多个帧数据源组件的场景层级结构：
>
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-mega.png)
>
如果场景中一开始使用了某个预设创建了 session，在迭代过程中增加其它功能时，不仅需要添加相应的 frame filter 组件，还需要根据需要添加合适的帧数据源组件。
> **重要事项**
从 4.7 或更低版本升级后，需要整个删除 session 后重新通过菜单或 [ARSessionFactory](../../../api/unity/easyar.ARSessionFactory.html) 创建 session，才能使用预设的帧数据源组。
以下列出了所有预设的 AR 功能默认配置的帧数据源组件，注意列表中的排序与场景中帧数据源的组件排序相同：
|预设|帧数据源组|
|
* [ImageTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTracking)
* [CloudRecognition](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_CloudRecognition)
* [ObjectTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ObjectTracking)
* [SurfaceTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SurfaceTracking)|
1. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
|
* [MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MotionTracking)
* [SparseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapBuilder)
* [SparseSpatialMapTracker](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapTracker)
* [DenseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_DenseSpatialMapBuilder)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)|
|
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* [MegaLandmark\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)
* [MegaLandmark\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* [MegaLandmark\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial_3DOF)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
11. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* [MegaLandmark\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial_3DOF_0DOF)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
11. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
|
* [ImageTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTrackingMotionFusion)
* [ObjectTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ObjectTrackingMotionFusion)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
> **注意**
使用预设创建的组件排序可以保证在所有受内置帧数据源支持的设备上使用最优的帧数据源。
## 使用默认帧数据源配置
在使用默认参数时，帧数据源的配置会根据设备和运行时启用的 AR 功能自动调整。
如果手动修改过帧数据源的参数，在 session 中的 AR 功能发生变化时（比如在原本只包含图像跟踪的 session 中新增了运动跟踪功能），可能需要手动调整帧数据源的参数以适应新的功能需求，这样所有 AR 功能才能以最佳效果运行。
> **重要事项**
从 4.7 或更低版本升级后，需要整个删除 session 后重新通过菜单或 [ARSessionFactory](../../../api/unity/easyar.ARSessionFactory.html) 创建 session，才能使用正确的默认参数。
## 添加帧数据源组
在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `Frame Source : \*` 可以添加适合该功能的 frame source 组件。也可以通过菜单 `EasyAR Sense` > `Frame Source by Transform Type` > `\* Dof` > `Frame Source : \*` 添加需要的 frame source 组件。
在脚本中，可以使用 [ARSessionFactory.AddFrameSource<Source>(GameObject, bool)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameSource__1_UnityEngine_GameObject_System_Boolean_) 来添加 frame source 组件。
比如，通过菜单 `EasyAR Sense` > `Frame Source by Transform Type` > `3 Dof Rot-Only` > `Frame Source : Three Dof Camera Device` 可以给当前选中的 session 添加一个 [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-add.png)
对应的脚本代码如下：
```
ARSessionFactory.AddFrameSource<ThreeDofCameraDeviceFrameSource>(session);
```
## 帧数据源排序
session 组装过程中，帧数据源组中最终只有一个帧数据源会被选中后组装到 session 中，选取的规则取决于 [AssembleOptions.FrameSourceSelection](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html) 属性的值。在默认配置下，可以通过调整帧数据源组中各个组件的排序来影响最终被选中的帧数据源。
一般可以使用在 `Hierarchy` 视图中 [对场景中的物体进行排序](https://docs.unity3d.com/Manual/Hierarchy.html) 的方法直接移动 frame source 物体进行排序。
在脚本中，可以使用 [Transform.SetSiblingIndex(int)](https://docs.unity3d.com/ScriptReference/Transform.SetSiblingIndex.html) 来调整物体的排序。
比如，要将 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 排在其它帧数据源前面，可以在 `Hierarchy` 视图中选中 `Motion Tracker` 物体并拖动到最上面的位置。
相同的效果也可以通过下面的脚本代码实现：
```
motionTrackerFrameSource.transform.SetSiblingIndex(0);
```
另外还有一些预定义的排序方法可以使用。在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Utility` > `Sort Frame Source : \* > \*` 对特定的若干帧数据源组件进行排序。
在脚本中，可以使用 [ARSessionFactory.SortFrameSource(GameObject, ARSessionFactory.FrameSourceSortMethod)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_SortFrameSource_UnityEngine_GameObject_easyar_ARSessionFactory_FrameSourceSortMethod_) 实现相同的效果。
比如，通过菜单 `EasyAR Sense` > `Utility` > `Sort Frame Source : Motion Tracker > System SLAM` 可以将 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 排在 [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)、[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)、[ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)、[ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)和 [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html) 前面。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-sort.png)
对应的脚本代码如下：
```
ARSessionFactory.SortFrameSource(session, new ARSessionFactory.FrameSourceSortMethod { MotionTracker = ARSessionFactory.FrameSourceSortMethod.MotionTrackerSortMethod.PreferEasyAR });
```
经过上面的排序之后，场景层级结构变为：
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-sorted.png)
## 相关主题
* 了解如何 [添加和配置头显用的帧数据源](../headsets/enable-headset.html)
* 尝试在运行时 [获取正在使用的帧数据源](../fundamentals/session-components.html)

---

## Unity 中的摄像头及输入帧数据来源 —— 帧数据源（Frame Source）
- 章节路径: `unity/cameras/frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source.html

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

---

## Workflow\_FrameSource\_CameraDevice 示例详解
- 章节路径: `unity/cameras/sample-camera-device.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/sample-camera-device.html

# Workflow\_FrameSource\_CameraDevice 示例详解
`Workflow\_FrameSource\_CameraDevice` 是一个专注于 **帧输入源（Frame Source）底层控制** 的示例场景，展示了如何使用 `CameraDeviceFrameSource` 获取摄像头的原始图像流，并进行一些基础控制。
## 使用方法
### 1. 打开场景
在 Unity 编辑器中，打开 `Workflow\_FrameSource\_CameraDevice` 场景，位于 `Assets/` 目录中。
### 2. 构建运行
* 在编辑器中点击 **Play** 可查看 PC 上的效果画面（部分功能受限）。
* **必须构建到真机** 才能完整体验摄像头的基础控制能力。
应用启动后，将自动打开后置摄像头。
## 预期效果
当摄像头对准周围环境时：
1. 屏幕中会显示实时摄像头画面。
2. 此时会渲染一个 3D 动态熊猫模型。
3. UI 显示当前摄像头状态（如分辨率、FPS）。
4. 点击 `Loop Size` 按钮可以切换当前摄像头支持的输出帧分辨率。
5. 点击 `Flash Torch` 按钮可以 **关闭/打开** 闪光灯。
6. 点击 `HorizontalFlip` 可以切换当前画面的 **镜像显示**。
7. 点击 `CaptureIamge` 可以切换是否让模型捕获当前环境画面作为自身的贴图。
8. 点击 `CameraImage` 可以切换是否显示当前摄像头画面。
9. 点击 `Camera` 可以 **关闭/打开** 当前摄像头，关闭后画面将保持关闭前的状态不变。
10. 通过 `NextCamera` 按钮动态切换 **前置/后置摄像头**。
> **提示**
更多 FrameSource 详情，请参阅：
* [内置Frame Source参考](frame-source-builtin.html)
* [自定义相机和外部帧输入](external-frame-source.html)
通过 `Workflow\_FrameSource\_CameraDevice`，您可深入掌握 EasyAR 对底层摄像头资源的控制能力，为构建高性能、高定制化的 AR 应用奠定坚实基础。

---

## Diagnostics Controller 组件参考
- 章节路径: `unity/diagnostics/comp-DiagnosticsController.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/comp-DiagnosticsController.html

# Diagnostics Controller 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.DiagnosticsController.html)
>
探索 DiagnosticsController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/diagnostics/media/comp-DiagnosticsController.png)
默认条件下组件截图。
DiagnosticsController 组件窗口由三个部分组成：组件配置、Assembly 预览和 session 验证工具。
## 组件配置
|属性|描述|
|**Developer Mode Switch**|开发者模式开关。可以使用默认的开关（点击屏幕 8 次触发）或自定义一个开关，或提供开发者模式的等价替代。|
|**Message Output**|消息输出选项。|
|*Session Dump*|会话状态转储输出方式。选项：
* UI：显示在UI并每帧更新。在头戴设备上，显示在眼前5米处。
* Log：输出到系统日志，由于每帧都输出，对运行性能是有影响的，建议在开发或测试时使用。
* None：不输出。|
|*Sense Error*|Sense Error 输出方式，通常与 EasyAR Sense license 有关。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Session Error*|Session Error 输出方式，通常与设备不支持一些功能或错误的配置有关。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Error*|Error 输出方式。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Warning*|Warning 输出方式。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Show Editor Dialog On Fatal*|编辑器中，Sense Error 或 Session Error 时显示对话框。|
## Assembly 预览
Assembly 预览只在编辑模式可见。根据 [AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 显示当前 session 在组装时会选择的组件，这个是一个参考，与 session 运行时最终组装的组件可能不同。
## session 验证工具
[session 验证工具](../simulation/tool.html)用于帮助开发者在 Unity 编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。

---

## 开发者模式
- 章节路径: `unity/diagnostics/developer-mode.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/developer-mode.html

# 开发者模式
开发者模式用于设定是否启用运行时诊断面板。诊断面板可用于切换调试信息是否显示以及录制 EIF、EED 文件。
![diagnostics developer mode 1](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode.png)
## 开发者模式诊断面板
开发者模式诊断面板默认通过快速点击屏幕 8 次打开（可通过修改 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 来更改）。打开后会在屏幕右侧显示诊断面板。
![diagnostics developer mode 2](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode-panel.png)
诊断面板功能如下：
* session: session 信息控制，该信息用于了解 session 的运行状态和问题
* Toggle: 切换 [SessionDump](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionDump) 消息显示
* copy: 复制当前帧 session dump 信息
* eif: eif 录制控制，eif 文件用于 [Unity AR 模拟运行](../simulation/simulation.html)
* Auto/Obsolete: 切换 eif 格式，其中 Obsolete 表示使用原始 EIF 格式，Auto 表示根据平台支持情况自动选择 EIF MKV 格式或者原始 EIF 格式
* rec: 启动/停止 eif 录制
* eed: eed 录制控制，eed 文件用于抓取一些运行时的关键数据提供给 EasyAR 技术支持进行问题分析
* rec: 启动/停止 eed 录制
## 修改开发者模式开关
可以通过 session 上的 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 组件在编辑器中配置，或是使用 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 接口在脚本中配置。
可以选择的模式如下：
* [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default)：手机上快速点击屏幕8次进入开发者模式并会在屏幕右边打开诊断面板。
* [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom)：可以通过 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 接口来自定义开启开发者模式切换条件，未定义时诊断面板将无法在运行时打开。
可以通过设置 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 为 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom) 并且不修改 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 来禁止开启开发者模式。
比如，下面的代码展示了如何在脚本中禁止开启开发者模式：
```
Session.Diagnostics.DeveloperModeSwitch = DiagnosticsController.DeveloperModeSwitchType.Custom;
```
> **提示**
* 建议在开发和测试阶段使用默认配置 [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default)。
* 建议在发布上线阶段使用配置 [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default) 或 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom)。
* 建议在使用 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom) 模式时，修改 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 以提供其它方式启用诊断面板，或提供其他自定义的方式收集运行时数据。
## 相关主题
* [录制 EED dump 文件](event-dump.html)
* [UI 消息](ui-messages.html)
* [Unity AR 模拟运行](../simulation/simulation.html)

---

## Unity 开发中的问题诊断和报告
- 章节路径: `unity/diagnostics/diagnostics.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/diagnostics.html

# Unity 开发中的问题诊断和报告
在开发基于 Unity 的插件或应用时，难免会遇到运行异常或逻辑错误。为了帮助开发者快速定位和解决问题，Unity Plugin 提供了一系列内置的诊断与调试工具。本章将介绍这些常用的调试手段和辅助功能，涵盖从实时日志查看、开发者模式启用，到问题数据采集与上报的完整流程。
* [UI 消息](ui-messages.html)
介绍运行时系统如何通过 UI 层面展示错误、警告和其他诊断信息，并说明这些消息的分类标准与含义，便于快速识别问题类型。
* [开发者模式](developer-mode.html)
说明如何在应用运行期间激活开发者模式，以及该模式下可使用的高级调试功能：可视化调试图层、EIF/EED 文件录制。
* [录制 EED dump 文件](event-dump.html)
详细讲解如何触发并录制 EED 文件，该文件包含关键事件、传感器数据、系统状态等上下文信息；同时说明如何从设备中导出和使用这些 dump 文件进行离线分析。
* [问题报告](report.html)
指导用户如何规范地提交问题反馈，包括应附带的日志、dump 文件、复现步骤等，以提高问题处理效率。
相关功能组件包括：
* [DiagnosticsController 组件](comp-DiagnosticsController.html)
该组件是诊断系统的核心控制器，负责协调日志记录、状态监控、dump 生成等功能。

---

## 录制 EED dump 文件
- 章节路径: `unity/diagnostics/event-dump.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/event-dump.html

# 录制 EED dump 文件
EED（EasyAR Event Dump）文件可用于抓取一些运行时的关键数据提供给 EasyAR 技术支持进行问题分析，例如一些跟踪器的跟踪结果、程序与 Mega 服务之间的网络请求等。通常在使用 [EIF 文件](../../simulation/simulation.html) 无法重现问题的时候使用。
## 使用开发者模式面板录制
运行程序，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。
![diagnostics eed windows](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-windows.png)
录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed windows 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-windows-2.png)
打开应用，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed android](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-android.png)
默认的 EED 文件路径位于 `/sdcard/Android/data` 中，在 Android 11 或更高版本的设备上，将无法通过文件管理器或 `adb pull` 来获得。建议使用 [Shizuku](https://shizuku.rikka.app/) 和 [MiXplorer](https://mixplorer.com/) 来获取文件。需要先在 WLAN 环境使用 Shizuku 与手机的无线调试配对并启动，然后在 Shizuku 中对 MiXplorer 授权，即可使用 MiXplorer 管理 `/sdcard/Android/data` 文件夹。
![diagnostics eed android 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-android-2.png)
打开应用，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed ios](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios.png)
使用示例时，可以将 iOS 设备连接到 Mac 设备，然后从 Mac 设备的 Finder 中找到 iOS 设备示例应用中录制完成的 EED 文件。
![diagnostics eed ios 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios-2.png)
如果无法在 Finder 中找到文件，可以在 Xcode 主菜单的 `Window -> Devices and Simulators` 中，选中应用，点击 `…`，选择 `Download Container…`，也可以获得 EED 文件。
![diagnostics eed ios 3](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios-3.png)
## 使用脚本录制
可以使用 [EventDumpRecorder.start(string, int)](../../../api/unity/easyar.EventDumpRecorder.html#u_easyar_EventDumpRecorder_start_System_String_System_Int32_) 开始录制 EED 文件，使用 [EventDumpRecorder.stop()](../../../api/unity/easyar.EventDumpRecorder.html#u_easyar_EventDumpRecorder_stop) 停止录制。
比如，下面的代码展示了如何在脚本中录制 EED 文件：
```
EventDumpRecorder eedRecorder;
bool RecordEED(bool on)
{
if (on)
{
if (session.Assembly == null || session.Assembly.Display == null) { return false; }
var path = Path.Combine(Application.persistentDataPath, DateTime.Now.ToString("yyyy-MM-dd\_HH-mm-ss.fff") + ".eed");
eedRecorder = EventDumpRecorder.create();
eedRecorder?.start(path, session.Assembly.Display.Rotation);
}
else
{
eedRecorder?.stop();
eedRecorder?.Dispose();
eedRecorder = null;
}
return true;
}
```
## 相关主题
* [开发者模式](developer-mode.html)

---

## 问题报告
- 章节路径: `unity/diagnostics/report.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/report.html

# 问题报告
> **注意**
EasyAR Mega 用户请务必阅读 [Mega 常见问题](../../mega/faq.html) 和 [问题报告与反馈](../../mega/report.html) 。
> **注意**
在反馈问题之前，请务必使用最新版本的 SDK 并在 sample 中复现问题，很多问题可能会在新版本中得到修复，EasyAR 主要支持在最新版本上能够复现的问题。此外，Unity 本身也会存在一些问题，一些 Unity 的问题可以通过尝试删除 Unity Library 文件夹、Unity 生成的 XCode 工程来解决。
请使用插件内置的 `提问` 功能来辅助检查和收集反馈信息。
![diagnostics report ask dialog options](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
这个窗口可以从 `EasyAR > Sense > 提问` 菜单打开
![diagnostics report ask menu](https://doc-asset.easyar.com/develop/mega/media/unity-question.png)
打开后信息是不全的，需要选择使用的环境和功能
![diagnostics report ask dialog](https://doc-asset.easyar.com/mega/troubleshooting/media/localization_failure6.png)
如需反馈手机或头显上的问题，请复制Session Dump信息日志
![diagnostics report ask dialog session dump setting](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-report-3.png)
然后填写到文本框中
![diagnostics report ask dialog session dump filling](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-report-4.png)
最后根据窗口提示完成所有操作后，点击右上角的复制按钮复制所有信息
![diagnostics report ask dialog options](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
请注意，这个界面不只是用来获取报告的，同时它也会引导你进行初步的问题筛查，请务必认真使用。
如遇到崩溃，请参考 崩溃分析（[Android](../../diagnostics/crash-android.html) [iOS/macOS/visionOS](../../diagnostics/crash-ios.html) [Windows](../../diagnostics/crash-windows.html)） 获取相关信息，一般来说如果没有完整的信息问题报告将是无效的。

---

## UI 消息
- 章节路径: `unity/diagnostics/ui-messages.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/ui-messages.html

# UI 消息
EasyAR Sense Unity Plugin 运行时有三类消息。
* 运行异常，包含 Sense Error、Session Error、Error、Warning
* Session Dump
* EasyAR Mega 开发特殊异常
您可以根据需要调整前两类消息的输出方式。可以通过 session 上的 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 组件在编辑器中配置，或是使用 [DiagnosticsController.MessageOutput](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_MessageOutput) 接口在脚本中配置。
![diagnostics ui messages](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message.png)
> **提示**
在 4000 版本中，如果场景由老版本插件创建，打开场景时 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 会被自动添加到 session 中。部分 Unity 版本中可能不会自动添加，在这些 Unity 版本中，[DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 会在运行时自动以默认值创建。
## 运行异常
插件运行时有时会收到内部组件发现的一些问题，以消息形式出现在系统中。这些消息有些可能是无法继续使用的严重故障，有些可能是故意触发的，有些可能是设备不受支持等等，按严重级别从高到低分为如下几类：
* [SenseError](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SenseError)：EasyAR Sense 错误，通常与 EasyAR Sense license 有关。
* [SessionError](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionError)：ARSession 错误，通常与设备不支持一些功能或错误的配置有关。
* [Error](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_Error)：其它错误信息
* [Warning](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_Warning)：警告信息
由于 Unity 开发的特殊性，我们默认会将这些消息显示在 UI 上，以辅助开发。
可以在编辑器或脚本中控制这些消息如何展示，可以选择的输出模式如下：
* [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)：输出到UI和日志。在头显上显示在眼前5米处。
* [Log](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_Log)：输出到系统日志。
> **提示**
* 建议在开发测试阶段使用默认配置 [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)。
* 建议在发布时将选项改成 [Log](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_Log)， 也可以保留 [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)，但这些UI消息通常对终端用户是不友好的。
* 建议在运行前 [判断 session 可用性和设备支持](../fundamentals/session-assemble.html) 并对不支持的设备进行合理提示。
### Sense Error
Sense Error 是一类特殊的错误，出现错误时 EasyAR 功能无法继续使用。常见原因：
* License 未正确配置或校验失败。该错误可以通过使用正确的 license 重新初始化来恢复。
* 部分设备（包括 AR Foundation、AR Engine 等所有使用自定义相机的设备或各种头显）上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）超过固定的有限时间。该错误无法恢复。
### Session Error
Session Error 是当前 ARSession 无法继续工作的错误。修改配置并重新运行 ARSession 可能可以解决这些错误。这些错误一般是由于您的配置错误、启动流程中抛出了异常导致组装中断、设备不受当前 ARSession 配置支持或是运行过程中 ARSession 组件丢失等导致的。
常见情况有：
* Session 组装错误：比如设备不受支持或支持设备的 Frame Source 没有正确配置在 ARSession 中等。
* Session 启动错误：云服务配置信息错误导致创建云服务功能出错，或配置信息未填写（包括 Mega 服务、云识别服务、SpatialMap 服务）等。
* Session 运行中错误：ARSession 组件被外部销毁，URP 环境下未正确配置 RendererFeature 等。
通常来说，配置错误以及启动流程中的异常导致组装中断都应该在开发过程中避免。设备不支持的情况主要出现在需要运动跟踪能力的功能上，需要参考 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 了解哪些功能需要注意设备支持，并在开发阶段选择合适的设备进行调试。
## Session Dump
[SessionDump](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionDump) 消息展示的是插件运行时收集的 ARSession 的运行状态，包括各个组件的一些关键状态。这些状态信息对了解 EasyAR 的运行以及分析问题有很大帮助。
可以在编辑器或脚本中控制这些状态如何展示，可以选择的输出模式如下：
* [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI)：显示在 UI 并每帧更新。在头显上，显示在眼前5米处。
* [Log](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_Log)：输出到系统日志，由于每帧都输出，对运行性能是有影响的，建议在开发或测试时使用。
* [None](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_None)：不输出。
> **提示**
* 建议在开发测试阶段使用默认配置 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI)，上面显示的信息是与 EasyAR 工作人员进行沟通所必不可少的。
* 建议在正式上线后再修改为 [None](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_None)，并保留打开 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI) 的软件开关，或通过其它系统进行数据收集。在向 EasyAR 反馈问题时， EasyAR 会向您或您的用户索取这些信息，以判断应用运行状态。
* 在绝大多数情况下，应用上线后运行出问题，应用端还是需要首先进行问题排查和分析，在排除应用问题并获取足够信息后反馈的问题才能较好解决。日志收集和分析的第三方 SDK 和平台比较多，建议上线前使用。如果您没有使用这些平台的经验或资源，保留打开 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI) 的开关（比如使用隐藏开关）让用户反馈看到的信息将是比较简单的。
## EasyAR Mega 开发特殊异常
Mega 开发中，还有一类无法控制的警告信息，这类信息会在满足特定配置条件时显示在 UI 上，开发者无法直接关闭。
建议关注信息本身，文字上写明了出现的原因和配置方法。开发者需要了解不同配置对不同使用方式的要求并根据开发进展合理选择。
这类信息是故意展示的，因为在特定使用条件下，这些功能用来辅助内容流程开发，但同时无法获取合理的运行结果，注意不要带着信息上线。
## 相关主题
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)
* [开发者模式](developer-mode.html)

---

## 适用于 target 和 origin 的 active 控制策略
- 章节路径: `unity/fundamentals/active-control.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/active-control.html

# 适用于 target 和 origin 的 active 控制策略
通过以下内容，您将了解 target 和 origin 下物体的默认显示和隐藏策略，以及如何根据需要进行调整。
## 开始之前
* 阅读 [Target](target.html) 了解 target 的基本概念、状态和生命周期。
* 阅读 [XR Origin](origin.html) 了解 XR Origin 的基本概念、组成和生命周期。
## active 控制和控制策略类型
session 运行过程中，target 和 origin 会经历跟踪和丢失等状态变化。通过 active 控制策略，可以自动管理 target 和 origin 下物体的显示和隐藏行为。
在 Unity 中，[ActiveController](../../../api/unity/easyar.ActiveController.html) 组件负责自动管理 target 和 orign 物体的 [GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 状态，以便在 target 被跟踪或运动跟踪开始跟踪后显示内容，在 target 丢失或运动跟踪成功初始化之前隐藏内容。
[ActiveController](../../../api/unity/easyar.ActiveController.html) 提供了两种不同的 active 控制策略：
* [ActiveWhileTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveWhileTracked)：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `true`）；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `false`）。
* [ActiveAfterFirstTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveAfterFirstTracked)：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `false`）；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `true`）。
默认情况下，[TargetController](../../../api/unity/easyar.TargetController.html) 使用 [ActiveWhileTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveWhileTracked) 策略，这意味着当 target 被跟踪时，target 以及其下的内容会被激活，而当跟踪丢失时，target 以及其内容会被停用。
默认情况下，[XROriginChildController](../../../api/unity/easyar.XROriginChildController.html) 使用 [ActiveAfterFirstTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveAfterFirstTracked) 策略，这意味着在运动跟踪成功初始化之前，origin 以及其下的内容会被停用，而一旦运动跟踪成功初始化，origin 以及其下的内容会被持续激活。
## 选择不同的 active 控制策略
打开 Inspector 面板，在 `Strategy` 下拉菜单中选择 `Input`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/active-select.png)
然后在右侧选择所需的 active 控制策略来覆盖默认策略。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/active-select2.png)
在脚本中，可以通过 [OverrideStrategy](../../../api/unity/easyar.ActiveController.html#u_easyar_ActiveController_OverrideStrategy) 属性来覆盖默认的 active 控制策略。
比如，下面的代码展示了如何将 target 的 active 控制策略设置为 [ActiveAfterFirstTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveAfterFirstTracked)：
```
target.ActiveController.OverrideStrategy = ActiveController.Strategy.ActiveAfterFirstTracked;
```
对 active 策略的修改会即时生效，并根据当前的跟踪状态更新 [GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html)。
## 关闭 active 控制
如果需要完全禁用 active 控制，比如需要根据需要进行控制，可以通过禁用 [ActiveController](../../../api/unity/easyar.ActiveController.html) 组件来关闭 active 控制。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/active-disable.png)
在脚本中，可以通过设置 [ActiveController](../../../api/unity/easyar.ActiveController.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 属性来关闭 active 控制。
```
target.ActiveController.enabled = false;
```
[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 属性的修改会即时生效，并且不会再根据跟踪状态更新 [GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html)。如果再次启用 [ActiveController](../../../api/unity/easyar.ActiveController.html) 组件，[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 会根据当前的跟踪状态进行更新。

---

## EasyAR 项目中的 AR Foundation 场景配置和用法
- 章节路径: `unity/fundamentals/arfoundation-scene-setup.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/arfoundation-scene-setup.html

# EasyAR 项目中的 AR Foundation 场景配置和用法
在 Unity 中使用 AR Foundation 往往需要依靠 EasyAR 解决 AR Foundation 的设备局限性。以下内容介绍如何在 EasyAR 场景中正确配置和使用 AR Foundation，以及如何根据设备支持情况动态启用 AR Foundation。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
* 阅读 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html) 了解如何在 EasyAR 项目中安装和配置 AR Foundation。
## 添加 AR Foundation 组件
在 EasyAR 场景中添加 AR Foundation 的 AR Session 和 XR Origin。
### 添加 AR Session
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` > `AR Session` 添加 Unity 的 [ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html) 到场景中。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session.png)
> **注意**
这个 AR Session 与 EasyAR 的 AR Session 不同，它们需要同时存在于场景中。
### 添加 XR Origin
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` > `XR Origin (Mobile AR)` 添加 Unity 的 [XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 到场景中。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-origin.png)
> **注意**
这个 XR Origin 与 EasyAR 的 XR Origin 功能是重叠的，需要使用 Unity XR Origin 而非 EasyAR 的 XR Origin。
如果场景中之前存在 EasyAR 的 XR Origin，一般名称为 `XR Origin (EasyAR)`，需要将其下面的子物体移动到新创建的 XR Origin 下面，然后将 `XR Origin (EasyAR)` 删除。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-remove-origin.png)
这时候，如果新创建的 XR Origin 下面没有 XR Origin Child，需要手动添加。
在 `Hierarchy` 视图中，选中 **XR Origin** 并点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin Child` 添加 XR Origin Child 到 XR Origin 下。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-child-creation.png)
### 配置 Camera
如果场景中之前存在 AR 用的 `Camera`，会发现场景中出现了多余的主摄像机，需要将原本的摄像机删除。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-remove-camera.png)
然后选中 XR Origin 下的 `Main Camera`，按照 [Camera 配置](camera-configs.html) 的说明对摄像机进行配置。
最后，一个完整的添加了 AR Foundation 的 EasyAR 场景结构应该类似下面这样：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/)
> **小心**
如果需要通过 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 修改 AR Foundation 的配置，需要注意部分手机自身（比如小米 10）存在问题，在修改配置之后无法获取图像，EasyAR 将无法使用（应用有图像背景但 EasyAR 功能没有任何反应），因此通常并不建议修改，如需修改需要做好 EasyAR 无法使用时的降级方案。
## 设备兼容与动态启用 AR Foundation
EasyAR 兼容的设备比 AR Foundation 多很多，因此需要配置以确保应用只在需要时启用 AR Foundation，其余情况需要完全关闭 AR Foundation。
### 检查 frame source 组件
一般来说，通过 EasyAR 菜单创建的 session 通常会自动添加 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 以及 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) （部分图像跟踪等不需要SLAM功能的除外）。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/.png)
> **重要事项**
[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 以及 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) 是 EasyAR 提供的 frame source，用于在支持 AR Foundation 的设备上启用 AR Foundation 功能。如果场景中的 session 不包含这些 frame source，则无法在启用 AR Foundation 功能。
如果场景中的 session 不包含这些 frame source，可以通过菜单手动添加。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-frame-source-creation.png)
为了在不支持 AR Foundation 的手机上运行，还需要确保 session 包含 AR Foundation 以外的 frame source。一个典型的ARSession 应该类似下面这样，
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-easyar.png)
> **提示**
可以根据实际需要对 frame source 进行排序，在应用运行时，session 会根据设备支持情况按 transform 顺序选择第一个可用的 frame source。
### 仅在需要时启用 AR Foundation
由于 AR Foundation 在手机上底层实现是 ARCore 和 ARKit，只能在有限的设备上使用，尤其是在很多国产 Android 手机上无法使用，所以通常建议仅在受支持的设备上启用 AR Foundation 及相关功能脚本。
EasyAR 可以自动完成这些操作，该功能可以通过 在 `Project Settings` > `EasyAR` > `Sense` 中的 `Unity XR` > `Unity XR Auto Switch` 选项启用或关闭。详细说明可以参考 [自动切换 Unity XR 物体](unity-xr-switch.html) 。
## 保留 AR Foundation 兼容性的场景
正确添加了 AR Foundation 组件的场景可以在 AR Foundation 包安装或未安装时都正常工作。
未安装 AR Foundation 时 AR Foundation 的功能及对应 frame source 不可用，且场景中会有部分脚本缺失，属于正常情况。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-missing-scripts.png)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-missing-origin.png)
> **提示**
很多 sample 都可以在 AR Foundation 包安装或未安装时都正常工作。如果需要在这些 sample 中启用 AR Foundation 支持，仅需 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html) 即可。
## 后续步骤
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* 文中提到的相关 AR 组件：
* [ARSession](session.html)
* [XR Origin](origin.html)
* [Camera](camera.html)
* AR Foundation 提供了部分设备上的运动跟踪能力，关于运动跟踪和各个 EasyAR 功能的关系，可以参考以下内容：
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)
* 有关 AR Foundation 场景配置的更多信息可以阅读 AR Foundation 官方文档，阅读前注意选择对应的文档版本：
* [场景配置](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/project-setup/scene-setup.html)
* [XR Origin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin-setup.html)

---

## 在 EasyAR 项目中启用 AR Foundation
- 章节路径: `unity/fundamentals/arfoundation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/arfoundation.html

# 在 EasyAR 项目中启用 AR Foundation
如果需要启用 EasyAR 的 AR Foundation 支持，或使用 AR Foundation 的其它功能，需要正确安装配置 AR Foundation。以下内容介绍如何完成这些操作。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
## AR Foundation 版本兼容性
EasyAR 支持 AR Foundation 5 或更新版本。
> **重要事项**
AR Foundation 的支持是通过自定义相机实现的。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
## 安装 AR Foundation
建议参考 [AR Foundation 官方文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest) 来安装 AR Foundation。阅读前注意选择对应的文档版本。
### Unity 2022 及更新版本
如果工程中未安装过 XR 相关插件，需要在 `Project Settings` > `XR Plug-in Management` 中，点击 `Install XR Plugin Management` 按钮来安装 XR Plug-in Management 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-managment.png)
如果需要在 Android 平台使用 AR Foundation，在 Android 标签下勾选 `Google ARCore` 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-arcore.png)
如果需要在 iOS 平台使用 AR Foundation，在 iOS 标签下勾选 `Apple ARKit` 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-arkit.png)
如果需要在 visionOS 平台使用 AR Foundation，需要阅读 [Vision Pro 工程配置](../headsets/setup-visionpro.html)。
> **提示**
建议保持 `Initialize XR On Startup` 处于勾选状态，以确保 AR Foundation 能够在默认时间点初始化。
安装完成后，打开 `Package Manager` 窗口，可以看到 `AR Foundation` 以及对应平台的插件会出现在已安装的包列表中。注意这些包的版本号应完全一致。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install.png)
> **重要事项**
在安装和更新 AR Foundation 时，需要确保 `Google ARCore XR Plugin` 和 `Apple ARKit XR Plugin` 版本与 `AR Foundation` 版本完全一致。版本不匹配可能会导致运行时错误或功能异常。
### Unity 2021
在 Unity 2021 版本中，需要手动编辑 `Packages/manifest.json` 文件来指定版本，参考 [官方文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.2/manual/project-setup/edit-your-project-manifest.html)。
比如，如果需要安装 AR Foundation 5.2.0 版本并在 Android 和 iOS 平台使用，要确保 `Packages/manifest.json` 文件中包含以下内容：
```
{
"dependencies": {
...
"com.unity.xr.arcore": "5.2.0",
"com.unity.xr.arfoundation": "5.2.0",
"com.unity.xr.arkit": "5.2.0",
...
}
}
```
## 配置 XR Plug-in
在使用 EasyAR 时，通常 ARCore 的存在并不是必需的。因此应配置 ARCore 为可选，以避免在不支持 ARCore 的设备上应用无法正常运行。
在 `Project Settings` > `XR Plug-in Management` > `ARCore` 中，将 `Requirement` 和 `Depth` 都设置为 `Optional`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-config-arcore.png)
> **小心**
如果把 `Requirement` 设置为 `Required`，并在不支持 ARCore 的设备上安装了打包后的应用，设备会错误地报告 ARCore 是可用的并以 ARCore 运行。这会造成一个假象，似乎这些设备正在运行 ARCore 并且运行不正常（黑屏或其它异常情况），但这是错误的。
出现这个现象的原因是由于 Google Play 商店阻止在不受支持的设备上安装标记 ARCore 为必需的应用，所以这些应用总是假设它们正在受支持的设备上运行。
正常配置下，这些设备会在 session 组装时判断 ARCore 不受支持并使用 EasyAR 的功能。
如有需要，也可以参考以下官方文档来进一步配置 ARCore 和 ARKit。阅读前注意选择对应的文档版本。
* [ARCore 插件配置](https://docs.unity3d.com/Packages/com.unity.xr.arcore@6.4/manual/project-configuration-arcore.html)
* [ARKit 插件配置](https://docs.unity3d.com/Packages/com.unity.xr.arkit@6.4/manual/project-configuration-arkit.html)
## 配置 Universal Render Pipeline
如果当前工程在使用 URP，需要配置 URP 资产。如未正确配置，AR Foundation 的摄像机背景图可能无法正确渲染。
首先确保已经正确配置 EasyAR 的 URP Renderer Feature，参考 [EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html)。
然后在Renderer Features 列表中添加 [ARBackgroundRendererFeature](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARBackgroundRendererFeature.html)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-config-urp.png)
与 EasyAR 的 URP Renderer Feature 配置一样，需要关注 `Project Settings` > `Quality` 中不同平台的配置，确保在所有需要使用 AR Foundation 的平台上都使用了正确配置了 [ARBackgroundRendererFeature](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARBackgroundRendererFeature.html) 的 URP 资产。
另外也可以参考 [AR Foundation 官方的 URP 配置文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/project-setup/universal-render-pipeline.html) 进行配置，阅读前注意选择对应的文档版本。
> **注意**
[EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html) 仍是需要的，这样才能确保在不支持 AR Foundation 的设备上使用 EasyAR 接口的相关功能渲染仍能正常。
## 启用 EasyAR AR Foundation 支持
在 `Project Settings` > `EasyAR` > `Sense` 中，确保 `Unity XR` > `AR Foundation Support` 选项被启用。**该选项是默认开启的。**
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-enable.png)
修改该选项会触发脚本重新编译，需要等待脚本编译完成修改才会生效。如果 Unity 因为某种原因未正常触发编译，可以关闭 Unity，删除 `Library/ScriptAssemblies` 文件夹来强制 Unity 重新编译脚本。
> **提示**
如果 EasyAR 与工程中的 AR Foundation 不兼容，且没有同时使用 EasyAR 和 AR Foundation 的需求，可以关闭该选项。
## 后续步骤
* 了解 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html)
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* [EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html)

---

## 配置 camera
- 章节路径: `unity/fundamentals/camera-configs.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/camera-configs.html

# 配置 camera
通过以下内容，您将了解如何配置 Unity 中 AR 场景的 camera 以获得最佳的 AR 体验。
## 开始之前
* 通过 [Camera](camera.html) 了解 AR 场景中摄像机的作用，以及 session 如何控制摄像机的属性以确保正确的 AR 体验。
## 适用于手机和 PC 设备的 camera 配置
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/camera-config.png)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/camera-config-urp.png)
在手机和 PC 设备上使用 AR 时，建议按照以下方式进行配置：
* **Clear Flags**：需要设置为 `Solid Color` 以确保 camera 图像可以正常渲染。如果保留默认的 *Skybox* ，camera 图像将无法显示。
* **Background**：非必需。考虑到使用体验，建议将背景颜色设为黑色以便在 camera 设备打开前和切换时以黑色过度。
* **Clipping Planes**：除通常渲染及性能需求之外，需要综合考虑识别及交互的物体或现实场景的物理大小和距离。比如可以设置 `Near` 为 0.1（米）以避免摄像机离物体较近时无法显示，设置 `Far` 为 1000（米）以避免远处物体无法显示。
> **注意**
使用 AR Foundation 或其他 Unity XR Origin 下的 camera 时，Unity 通常会预设其剪裁平面为 (0.1, 20) ，这可能会导致距离真实世界中的设备超过 20 米的物体无法显示出来。请在使用前根据具体需求来修改。
## 适用于头显的 camera 配置
使用头显时，camera 通常由设备 SDK 进行配置和控制，因此建议保留设备 SDK 默认配置，或根据设备 SDK 的要求进行配置。另外可以根据需要修改 **Clipping Planes**。

---

## AR 场景中的 Unity 摄像机
- 章节路径: `unity/fundamentals/camera.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/camera.html

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
> **警告**
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
> **警告**
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
> **警告**
虽然在这种情况下 session 不会控制摄像机的属性，但它们会由第三方系统（比如头显 SDK 或 AR Foundation）所控制，在开发应用时修改这些属性仍然是不受支持的。
## 复制摄像机时的注意事项
有时可能需要将 session 摄像机的参数复制到另一个摄像机上，这时需要额外关注以下两点：
* 属性获取时间：在使用受控摄像机时，需要参考 [获取 session 的运行结果](session-output.html) 在正确的时间获取这些参数；在使用不受控 session 控制的摄像机时，需要参考第三方系统的文档在正确的时间获取。
* 摄像机的视野（FOV）、宽高比（aspect ratio）和投影矩阵：需要使用 [Camera.projectionMatrix](https://docs.unity3d.com/ScriptReference/Camera-projectionMatrix.html) 获取摄像机投影矩阵，并复制到另外一个摄像机。[Camera.fieldOfView](https://docs.unity3d.com/ScriptReference/Camera-fieldOfView.html) 和 [Camera.aspect](https://docs.unity3d.com/ScriptReference/Camera-aspect.html) 在数学上是投影矩阵的一部分，使用 [Camera.fieldOfView](https://docs.unity3d.com/ScriptReference/Camera-fieldOfView.html) 和 [Camera.aspect](https://docs.unity3d.com/ScriptReference/Camera-aspect.html) 是不充分的。
## 后续步骤
* 阅读 [Camera 配置](camera-configs.html) 了解如何配置摄像机以获得最佳的 AR 体验
## 相关主题
* [中心模式](center-mode.html)

---

## 选择合适的中心模式
- 章节路径: `unity/fundamentals/center-mode-choosing.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/center-mode-choosing.html

# 选择合适的中心模式
选择合适的中心模式对于内容制作来说至关重要。通过以下内容，您将了解如何获取和修改中心模式，以及选择合适中心模式的建议。
## 开始之前
* 通过 [AR Session 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [AR Session 的中心模式](center-mode.html) 了解中心模式的基本概念及其对场景中物体运动行为的影响。
## 获取可用中心模式
在 session 运行时，只有当前 session 可用的中心模式会显示在 Inspector 面板的 `Center` 下拉菜单中。如果 session 未启动，则所有中心模式均会显示。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-available.png)
这张图中显示了在编辑器中使用 CameraDeviceFrameSource 时的 session 可用的中心模式。
在脚本中，可以在 session 成功组装后通过 [ARSession.AvailableCenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AvailableCenterMode) 属性来获取当前 session 中可用的中心模式列表。
比如，下面的代码展示了如何判断某个中心模式是否在当前 session 中可用：
```
if (Session.AvailableCenterMode.Contains(mode))
{
// mode 在当前 session 中可用
}
```
## 修改中心模式
打开 Inspector 面板，在 `Center` 下拉菜单中选择需要的中心模式。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-change.png)
在脚本中，可以通过 [ARSession.CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 属性来修改中心模式。
比如，下面的代码展示了如何在可用的中心模式之间循环切换：
```
while (true)
{
Session.CenterMode = (ARSession.ARCenterMode)(((int)Session.CenterMode + 1) % Enum.GetValues(typeof(ARSession.ARCenterMode)).Length);
if (Session.AvailableCenterMode.Contains(Session.CenterMode)) { break; }
}
```
session 每帧更新时会判断当前中心模式是否有效，如果有效，session 会立即尝试使用新的中心模式。
>
> 在上面这个视频中，session 一开始使用
[> FirstTarget
](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget)> 模式，中心物体是圣诞树（亮蓝色点云）。随后我们手动将中心模式修改为
[> Camera
](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera)> 模式，中心物体变为摄像机（蓝色锥体）。视频内容的详细描述请参考
[> AR Session 的中心模式
](center-mode.html)> 。
>
session 更新时，如果修改后的中心模式在当前 session 中无效，[CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 属性会被自动修改为第一个可用的中心模式（通常是 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)），并在日志中输出一行警告信息：
```
Center mode {Value} is unavailable in this session, reset to {NewValue}.
```
## 如何选择中心模式
与现实世界中的物体进行对齐是 AR 内容制作的核心需求，而中心模式决定了 session 以哪个物体作为参考点来计算场景中其它物体的位置和朝向。因此，选择合适的中心模式对于内容制作来说至关重要。
### 通用建议
很多时候使用 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 模式，以 `target` 作为中心对内容制作是更友好的，这样放在 `target` 下的内容参考点可以保持静止不动，不会因为 `XR Origin` 或 `camera` 的移动而产生不必要的影响（比如影响物理系统计算）。不过这并不绝对，具体来说：
* 在不知道怎么选择时，使用默认值，即 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 中心
由于绝大部分 AR 功能都是有误差的，而且运行中会不断修正这个误差，这就会导致看似在现实世界中相对不动的物体（比如稀疏空间地图的 `target` 和 运动跟踪的 `XR Origin`）实际在虚拟空间中是会有相对运动的，这时采用 `target` 作为中心就要比采用 `XR Origin` 要更符合内容制作的需要。
* 多个 `target` 同时被跟踪的情况
对于多个 `target` 同时被跟踪的情况，同样由于及计算误差，即使现实世界中的物体相对是静止的，这些 `target` 之间也可能存在相对运动。如何选择中心的物体则需要根据实际需要进行判断，通常 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 模式是更合适的选择。
* 什么时候使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式
[SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 适用于只有运动跟踪在运行的场景，这时 `XR Origin` 是唯一的参考点。它还适用于一些特殊情况，如果头显厂商没有正确实现运动跟踪的参考点，这时就必须使用 Unity 的世界中心从而强制使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式。
* [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式的使用场景
[Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式则更适用于物理相机不动的场景（比如使用固定摄像头的卡片对战类 AR），这时采用 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式会更便于内容创作。
### 不同 AR 功能的常用中心模式
在单独使用部分 AR 功能时，某些中心模式会更常用一些。下面的表格列出了这些 AR 功能对应的常用中心模式：
|功能|常用中心模式|
|Mega|FirstTarget 或 SpecificTarget|
|运动跟踪|SessionOrigin|
|平面检测|SessionOrigin|
|稀疏空间地图|FirstTarget 或 SpecificTarget|
|稠密空间地图|SessionOrigin|
|表面跟踪|FirstTarget 或 SpecificTarget|
|图像跟踪|FirstTarget、SpecificTarget 或 Camera|
|图像云识别|FirstTarget、SpecificTarget 或 Camera|
|物体跟踪|FirstTarget、SpecificTarget 或 Camera|
### 跨设备需要考虑的问题
在开发跨设备的 AR 应用时，需要考虑不同设备对中心模式的支持情况。
* 如果仅涉及手机和平板，通常不会有太大问题，如果需要使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)，要确保运动跟踪可以运行。
* 如果需要使用头显，则需要格外注意
* 查阅 [有效中心模式](center-mode.html#available-center-mode) 确定将要使用的设备都支持哪些中心模式。如果在使用第三方扩展，注意查看这些扩展使用的 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType)。
* 使用 Rokid 设备时，尽量不要使用 UXR。使用 XRI 可以确保大多数中心模式可用。
* 在不支持 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 和 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 模式的头显上，需要注意使用 Mega 或图像跟踪等绝大部分功能内容都是做不到相对 Unity 世界坐标系静止的。
## 每个中心模式都能正确显示的内容
> **警告**
在 Unity AR 中，任何存在于 Unity 世界坐标系下且未根据 session 组件调整 transform 的物体都可能无法正确显示。
如果世界坐标系下放置了一些模型，那这些模型的位置和朝向可能与现实世界中任何物体都没有对应关系，实际运行效果可能碰巧正常，也可能看上去像是浮在空中或者到处乱动。
要保证内容在任何中心模式下都能正确显示，正确的做法是：
* 始终把要显示的内容放在对应的 `target` 节点下，或者放在 `XR Origin` 节点下（如果内容需要跟随 XR Origin 运动）
* 或者通过手动方式对齐内容和 `target` 或 `XR Origin` 的位置和朝向，但需要在 [ARSession.PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件后操作
> **注意**
这么做并不能保证所有内容元素都工作正常，因为 Unity 的某些功能只能在世界坐标系下工作（比如物理系统），选择合适的中心模式仍然是重要的。
## 相关主题
* [获取 session 的运行结果](session-output.html)

---

## AR Session 的中心模式
- 章节路径: `unity/fundamentals/center-mode.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/center-mode.html

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
> **提示**
如果您有使用 AR Foundation 的使用经验，可能会注意到 AR Foundation 中并不存在类似的概念。实际上，AR Foundation 的行为模式与 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式是一致的。
在 session 中，`target` 和 `camera` 的相对运动关系由当前 session 控制。`XR Origin` 和 `camera` 的相对运动关系，由当前 session 控制或者第三方框架（比如 AR Foundation）控制。中心模式的存在保证了在不同的运行环境下，session 都能正确地控制场景中物体的运动行为。
比如，如果 AR Foundation 或基于 Unity XR 的头显 SDK 控制了 `XR Origin` 和 `camera` 的相对运动关系，`XR Origin` 作为 Unity XR 框架的设计，是可以由 session 控制移动的，而 `camera` 则不行。这时 session 会限制中心模式为 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 、 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 或 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)，这样对于 session 来说，中心会是 `XR Origin` 或某个 `target`，而对于 Unity XR 框架来说，中心仍然是 `XR Origin`，整个系统可以完美工作。
> **警告**
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
> 一个是
> 圣诞树
> ，它是静止不动的。它是通过稀疏空间地图功能进行跟踪的。
>
> 另一个是一张
> A4 纸
> ，纸上事先打印好了一张图片，它是可以移动的。它是通过图像跟踪功能进行跟踪的。
>
>
> 录制视频时，观察者（手机）从圣诞树的右后方开始，绕着圣诞树移动。A4 纸在观察者前方左右摆动。
>
> 为了便于观察，我们对场景中的不同物体添加了一些标识，
>
>
* **> 圣诞树
> ：处于跟踪状态时在其所占据的空间叠加了
> 亮蓝色点云
> 。跟踪丢失时这些标识会消失。
>
* **> A4 纸
> ：处于跟踪状态时在其正上方叠加了一个
> 熊猫
> 。
`> Game
`> 视图中还额外显示了一个与 A4 纸内容和大小完全相同的图片。跟踪丢失时这些标识会消失。
>
* **> XR Origin
> ：在其位置放置了一个
> 蓝色球体
>
* **> 摄像机
> ：在其位置放置了一个
> 蓝色锥体
> ，锥体的主轴与摄像机的视线方向一致。
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

---

## AR Session 组件参考
- 章节路径: `unity/fundamentals/comp-ARSession.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/comp-ARSession.html

# AR Session 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ARSession.html)
>
探索 AR Session 组件窗口中的各项属性以自定义 session 参数。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/comp-ARSession.png)
默认条件下组件截图。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/comp-ARSession-runtime.png)
运行时的组件截图。
|属性|描述|
|**Auto Start**|控制 session 是否自动启动。如果值为 `true`（默认值），则在 [MonoBehaviour.Start()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) 时 session 会自动启动。
参见：[session 的流程控制](session-ctrl.html)|
|**Assemble Options**|Session 的组装选项。|
|*Enable Custom Camera*|启用自定义相机（默认 `true`）。
自定义相机包括：AR Engine frame source、AR Foundation frame source、所有头显以及所有自定义的 frame source。
*在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。*|
|*Frame Source*|FrameSource 的选择策略：
* Auto（默认）：自动选择，选择第一个可用且 active 的子节点。
* Manual：手动指定。需要在展开的选项内选择 session 的一个 frame source。
* FramePlayer：选择 frame player。参见：[帧数据源](../cameras/frame-source.html)|
|*Frame Filter*|FrameFilter 的选择策略：
* Auto（默认）：自动选择。选择所有 active 的子节点。
* AutoAvailable：自动选择。选择所有 active 且可用的子节点。
* Manual：手动指定。需要在展开的选项内选择 session 的一组 frame filter。
* None：不选择。|
|*Device List Update Options*|设备列表更新选项。
参见：[判断可用性和设备支持](session-assemble.html)|
|*Timeout*|请求超时时间，单位：s。|
|*Wait Time*|等待时间，单位：s。
超过等待时间即使下载未完成也会继续，这时下载完成后会通过事件更新。|
|*Ignore Cache*|忽略缓存，无论当前进程近期是否下载过都强制下载。|
|**Center**|AR中心模式：
* FirstTarget（默认）：以第一个跟踪到的 target 为中心。
* Camera：以 [ARAssembly.Camera](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Camera) 为中心。
* SpecificTarget：以 手动指定的 *target* 为中心。
* SessionOrigin：以 [ARSession.Origin](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Origin) 为中心。在编辑器内运行时，随 session 状态随时更新且修改立即生效。
参见：[中心模式](center-mode.html)|
|*Target*|手动指定的中心物体。
在编辑器内运行时，随 session 状态随时更新且修改立即生效。|
|*Current*|运行时表示 session 当前正在使用的中心物体。|
|**Horizontal Flip**|水平镜像渲染模式。仅在使用图像或物体跟踪时可用。
在编辑器内运行时，随 session 状态随时更新且修改立即生效。|
|*Back Camera*|后置摄像头的水平镜像渲染模式：
* None（默认）：不翻转。
* World：水平镜像渲染，camera 图像会镜像显示，camera 投影矩阵会变化进行镜像渲染，target scale 不会改变。
* Target：水平镜像渲染，camera 图像会镜像显示，target scale 会改变进行镜像渲染，camera 投影矩阵不会改变。|
|*Front Camera*|前置摄像头的水平镜像渲染模式：
* None：不翻转。
* World（默认）：水平镜像渲染，camera 图像会镜像显示，camera 投影矩阵会变化进行镜像渲染，target scale 不会改变。
* Target：水平镜像渲染，camera 图像会镜像显示，target scale 会改变进行镜像渲染，camera 投影矩阵不会改变。|

---

## 使用 License Key 初始化 EasyAR Sense
- 章节路径: `unity/fundamentals/initialization.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/initialization.html

# 使用 License Key 初始化 EasyAR Sense
在 Unity 中使用 EasyAR，需要使用 license key 初始化 EasyAR Sense，以确保功能被激活。有两种初始化方式：自动初始化和手动初始化。
初始化成功后，可以通过 Unity 控制台或操作系统日志看到 EasyAR Sense 的版本号和运行平台信息，例如：
>
> EasyAR Sense (Android-arm64) Version 4.7.0.11800-cf8e24e30
>
## 开始之前
* [EasyAR Sense 许可证](../../license-sense.html) 描述了如何获取 EasyAR Sense 许可证（license key）。在初始化 EasyAR Sense 之前，需要根据实际使用的设备和开发阶段准备好合适的许可证。
## 自动初始化
自动初始化适用于大部分使用场景。
打开 `EasyAR 全局配置`，勾选 `Initialize On Startup` 选项，并填写 `EasyAR Sense License` > `LicenseKey`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-license-settings.png)
自动初始化会在 Unity 的 [BeforeSceneLoad](https://docs.unity3d.com/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) 时间点自动调用。
> **注意**
在编辑器下使用的 license 不会校验应用包名，所以编辑器中可以正常使用的 license，在打包到平台应用或 app 运行时仍有可能失败，这时候需要注意两种情况：
1. 填写的 license 的包名与 Unity Player Settings 中填写的 bundle id/package name 应该一致。
2. 如果 Unity 打包后，在 gradle 或 XCode 工程中修改了包名。这时需要在 Unity 中使用 gradle 或 XCode 里面的包名。
## [可选] 手动初始化
手动初始化主要用于自定义的初始化流程，比如在调用 EasyAR 接口之前弹出用户隐私说明（请参阅 [合规指南](../../compliance/guide.html) ）等。
打开 `EasyAR 全局配置` ，取消勾选 `Initialize On Startup` 选项。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-license-settings-manual.png)
然后使用 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 接口手动调用初始化。
可以通过参数传入 license，
```
EasyARController.Initialize("my-license");
```
也可以使用 `EasyAR 全局配置` 中填写的 license,
```
EasyARController.Initialize();
```
> **重要事项**
[EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 必须在 [ARSession](../../../api/unity/easyar.ARSession.html) 启动之前调用。
在一些特殊情况下，如果要多次调用 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize)，需要确保每次 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 执行后通过 [EasyARController.Deinitialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Deinitialize) 进行反初始化。
## 初始化失败的解决方法
在包含了 [ARSession](../../../api/unity/easyar.ARSession.html) 的场景运行后，如果日志中没有包含类似的信息，则说明初始化失败。
>
> EasyAR Sense (Android-arm64) Version 4.7.0.11800-cf8e24e30
>
在 Unity 编辑器中，可能还会看到类似这样的弹窗
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-fail.png)
> **注意**
需要注意阅读弹窗中显示的文字信息，并不是所有弹窗都是初始化失败。
常见的出错信息和原因如下：
* EasyARSettings is not found
* `EasyAR 全局配置` 资源文件未创建（常见于没有填写 license）
* License Key is empty
* `EasyAR 全局配置` 中未填写 license，或工程中存在多个 `EasyAR 全局配置` 资源文件
* EasyARController.Initialize is not called (InitializeOnStartup = false)
* 手动初始化未在正确的时机调用
* EasyAR stops after script change in play mode
* 编辑器中运行时，脚本发生了改动。这时需要重新运行即可
## 相关主题
* [ARSession](session.html)
* [EasyAR 全局配置](setup-easyar.html)
* [合规指南](../../compliance/guide.html)
* 日志查看方法： [Android](../../diagnostics/log-android.html)、[iOS](../../diagnostics/log-ios.html)、[Unity 编辑器](../../diagnostics/log-windows.html)

---

## AR 驱动的 Unity 应用基础
- 章节路径: `unity/fundamentals/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/intro.html

# AR 驱动的 Unity 应用基础
EasyAR Sense Unity 插件包提供了在 Unity 中开发 AR 应用的基础功能。本文介绍了在 Unity 中开发 AR 应用时需要了解的基础知识和组件。
## 开始之前
* 了解 [AR 驱动的 3D 渲染](../../fundamentals/fundamentals.html)。
## Unity AR 应用开发基础
首先，您需要通过以下内容了解 EasyAR 兼容哪些 Unity 版本及平台：
* [Unity 兼容性](unity-compatibility.html)
在 Unity 中，AR 应用的典型流程与 [一般 AR 应用](../../fundamentals/fundamentals.html) 类似，但通过 AR Session 组件来管理摄像头数据的获取、跟踪器的运行以及虚拟内容的渲染。
```
flowchart TD
subgraph AR
CameraDevice[Camera Device]
Tracker[Tracker]
Renderer[Renderer]
CameraDevice -->|Image Frame| Tracker
Tracker -->|Image Frame + Tracked Pose| Renderer
end
subgraph unity["Unity AR"]
B[Session]
C([Camera])
O([Origin])
T([Target])
B -- transform --> C
B -- transform --> O
B -- transform --> T
classDef Unity fill:#6e6ce6,stroke:#333,color:#fff
class B Unity
class C Unity
class O Unity
class T Unity
end
CameraDevice -..- B
Tracker -..- B
Renderer -..- C
Renderer -..- O
Renderer -..- T
```
您将从以下这些基础组件开始，逐步了解 Unity 中 AR 应用的基础知识：
* [AR Session](session.html)
* [Camera](camera.html)
* [XR Origin](origin.html)
* [Target](target.html)
然后，您需要了解**中心模式**，这是理解 EasyAR 对 Unity 组件行为控制的关键概念：
* [中心模式](center-mode.html)
如果您有 Unity XR 框架（比如 AR Foundation）的使用经验，您可能会希望了解怎样在开发 EasyAR 应用时使用这些功能：
* [Unity XR 框架](unity-xr.html)
* [AR Foundation](arfoundation.html)
如果您已经在 Unity 编辑器内完成了 AR 开发，您可能会希望在打包发布前了解如何配置 Unity 项目以便在目标设备上运行：
* [Player 配置](setup-player.html)
* [EasyAR 配置](setup-easyar.html)
结合上面这些基础知识，您可以参考以下工作流程示例，实践您所学到的内容：
* [Workflow\_ARSession 示例](sample-arsession.html)
## 后续步骤
在掌握了 Unity AR 应用开发的基础知识后，您仍需继续了解更多 AR 开发所需的功能和组件：
* 了解 [帧数据源（Frame Source）](../cameras/frame-source.html)
* 了解 [Unity AR 模拟运行](../simulation/simulation.html) 并在开发过程中多加利用
* 了解 [诊断功能](../diagnostics/diagnostics.html) 并在开发过程中多加利用
如果您需要在头显设备上运行 EasyAR 应用，您还需要：
* 了解 [XR 头显](../headsets/headsets.html) 的使用

---

## 创建 XR Origin
- 章节路径: `unity/fundamentals/origin-creation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/origin-creation.html

# 创建 XR Origin
通过以下内容，您将了解如何在 Unity 场景中创建和配置 XR Origin 以及 XR Origin Child。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [XR Origin](origin.html) 了解 XR Origin 的基本概念、组成和生命周期。
## 创建 XR Origin (EasyAR)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin (EasyAR)` 可以创建一个完整 origin 结构。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-creation.png)
在脚本中，可以使用 [ARSessionFactory.CreateOrigin()](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateOrigin) 创建：
```
ARSessionFactory.CreateOrigin();
```
> **注意**
session 运行时，如果场景中没有正确的 XR Origin 结构，XR Origin 和一个 XR Origin Child 会被自动创建。
## [可选] 创建 XR Origin (Unity XR)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` > `XR Origin (Mobile AR)` 可以创建适用于 AR Foundation 的 XR Origin。有关该 XR Origin 的详细信息和创建方法，请参考 Unity 官方文档：[添加 Unity XR 的 XR Origin 到场景](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin-setup.html)。
> **注意**
使用头显时，请务必参考对应头显 SDK 的文档进行操作。
在使用 Unity XR 框架提供的 XR Origin 时，需要手动添加 XR Origin Child。
## 添加 XR Origin Child 到 XR Origin
在 `Hierarchy` 视图中，选中 **XR Origin (EasyAR)** 或 **XR Origin** 并点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin Child` 可以添加 XR Origin Child 到 XR Origin 下。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-child-creation.png)
在脚本中，可以使用 [ARSessionFactory.AddOriginChild(GameObject)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddOriginChild_UnityEngine_GameObject_)：
```
ARSessionFactory.AddOriginChild(origin);
```
可以添加任意多个 XR Origin Child，它们都会正常工作。但是对于 session 内部生成的物体来说，只会使用第一个 XR Origin Child 作为父节点。
> **注意**
session 运行时，如果场景中没有正确的 XR Origin Child 结构，XR Origin Child 会被自动创建。
## 后续步骤
* 了解 XR Origin 的 [active 控制策略](active-control.html)

---

## Unity AR 的运动跟踪中心 —— XR Origin
- 章节路径: `unity/fundamentals/origin.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/origin.html

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

---

## Workflow\_ARSession 示例详解
- 章节路径: `unity/fundamentals/sample-arsession.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/sample-arsession.html

# Workflow\_ARSession 示例详解
`Workflow\_ARSession` 是一个**轻量级**的 AR 会话管理示例，旨在展示如何以最小依赖构建一个完整的 AR 应用流程。该示例同时支持 **AR Foundation 兼容模式** 和 **简易模式** ，您可以根据项目需求灵活选择。
## 使用方法
### 场景选择（二选一）
在 Unity 编辑器中，`Workflow\_ARSession` 场景包含两组互斥的配置根对象，请**仅启用其中一组**（确保另一组处于非激活状态）：
|配置名称|适用场景|依赖|
|`ARFoundationCompatibleSceneSetup`|已使用或计划集成 **AR Foundation** 的项目|需完成 [AR Foundation 配置](arfoundation.html)|
|`SimpleSceneSetup`|**不依赖 AR Foundation**，直接使用 EasyAR 原生能力|无额外依赖，适合轻量级 AR 应用|
### 构建与运行
1. 将 `Workflow\_ARSession` 添加至菜单栏 `File` > `Build Settings` 或 `Build Profiles` > `Scene List` 中。
2. 根据所选目标平台（如 Android 或 iOS），在 `Project Settings` > `Player` 中确认构建选项。
3. 构建到真机并运行。
应用启动后，将自动初始化摄像头并等待识别目标。
## 识别目标与获取方法
本示例默认演示 **图像识别（Image Tracking）** 功能，但其架构可轻松扩展至物体跟踪、云识别等其他模式。
### 默认目标：`namecard.jpg`
* **目标类型**：2D 图像（建议打印尺寸 ≥ 90mm × 54mm）
* **下载地址**：🔗 [namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
### 如何替换目标？
1. 将您的图像（JPG/PNG）放入 `Assets/Samples/EasyAR Sense Unity Plugin/[版本号]/\_\_All Samples\_\_/Workflow/Workflow\_ARSession/Targets`。
2. 选择场景中的 `ImageTarget-namecard` 组件，在 **Inspector** 的 `Image Target Controller (Script)` 中更改 `Texture` 为您的图像。
3. 修改 `Name` 和 `Scale`。 `Scale` 是您的目标的物理尺寸（单位：米），以图像的长边为准。
![Replace Image Target](https://doc-asset.easyar.com/develop/unity/fundamentals/media/image-target-config.png)
4. 保存并重新构建。
## 预期效果
当摄像头对准目标图像时，系统将：
1. 实时检测并跟踪图像；
2. 在图像平面上叠加一个 3D 熊猫；
熊猫的位置、朝向与缩放严格绑定于图像目标的位姿，即使图像运动、部分遮挡或光照变化，仍能稳定跟踪。
## 扩展建议
* **添加物体跟踪**：替换 `ImageTracker` 为 `ObjectTracker`，加载 `.obj` 模型文件；
* **接入云识别**：使用 `CloudRecognizer` 替代本地目标列表；
* **多目标支持**：从单个图像目标扩展为多个图像，系统将自动处理并发跟踪。
> **提示**
更多功能组件请 [访问AR功能组件](session-components.html)。
通过 `Workflow\_ARSession`，您可快速掌握 EasyAR 的核心工作流，并以此为基础构建生产级 AR 应用。

---

## 判断 session 可用性和设备支持
- 章节路径: `unity/fundamentals/session-assemble.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-assemble.html

# 判断 session 可用性和设备支持
在启动 AR 之前，通常需要先判断 session 是否可用以及当前设备是否支持所需的 AR 功能。本文介绍了如何进行这些检查。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 通过 [设备支持和报告](session-report.html) 了解 Unity 中设备支持和 session 报告的基础知识
* 了解如何 [创建 session](session-creation.html)
## 在启动流程中获取报告
如果组装之后直接启动了 session，可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告。
需要在 session start 之前订阅 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件，通常在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 中完成订阅是安全的：
```
void Awake()
{
Session.StateChanged += HandleSessionStateChange;
}
```
在事件处理中需要关注的 session 的状态包括：[Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 和 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。[Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态说明 session 已经成功启动，也即说明 session 在当前设备上可用。[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态说明 session 启动失败，也即说明 session 在当前设备上不可用。
[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并不总是在设备不受支持的时候出现。所以还需要使用 [SessionReport.BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 获取具体的失败原因。
```
void HandleSessionStateChange(ARSession.SessionState status)
{
if (status == ARSession.SessionState.Ready)
{
// session 在当前设备上可用
}
else if (status == ARSession.SessionState.Broken)
{
// session 在当前设备上不可用
if (Session.Report.BrokenReason == SessionReport.SessionBrokenReason.NoAvailabileFrameSource ||
Session.Report.BrokenReason == SessionReport.SessionBrokenReason.FrameFilterNotAvailabile)
{
// 所选组件不受当前设备支持
}
else
{
// 设备无关的原因
}
}
}
```
出现 [SessionReport.SessionBrokenReason.NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource) 和 [SessionReport.SessionBrokenReason.FrameFilterNotAvailabile](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_FrameFilterNotAvailabile) 这两种原因，说明 session 组件在当前设备上不可用；而其它原因通常是设备无关的。严格来说，出现这两种原因意味着当前配置（且仅该配置）下的 AR 功能无法在该设备上运行。配置指 session 物体中选择的功能和设置。可以从 [Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 中获得详细的可用性报告。
对于 [SessionReport.SessionBrokenReason.NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource) 的情况，如果在启动 session 时联网更新设备列表时发现设备已被支持，session 有可能自动恢复。
## 在启动前获取报告
如果希望在 session 启动前做出判断，并根据具体情况决定是否启动 session，可以手动调用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 并使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告。
需要在 session assemble 之前订阅 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件，
```
Session.AssembleUpdate += OnAssembleUpdate;
```
在组装第一阶段，仍然可用利用 [ARSession.SessionState](../../../api/unity/easyar.ARSession.SessionState.html) 和 [Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 来判断 session 受支持的情况。但是第二阶段的报告不会更新到 session 中。
因此一般手动调用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 时，需要在 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件中处理组件可用性报告，从而判断 session 在当前设备上是否可用。
需要重点关注 [SessionReport.AvailabilityReport.FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 列表中组件的可用性。如果有任何一个 frame source 组件是可用的，那么 [SessionReport.AvailabilityReport.FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 部分在当前设备上就是可用的。
同时还需要关注报告中的 [SessionReport.AvailabilityReport.FrameFilters](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameFilters) 列表中组件的可用性。但是判断标准根据组装选项不同，会要求所有 frame filter 可用，或是任意数量的 frame filter 可用。默认选项下，要求所有 frame filter 可用。
在默认配置下，可以使用如下代码判断 session 组件在当前设备上是否可用：
```
void OnAssembleUpdate(SessionReport.AvailabilityReport report)
{
if (report.FrameSources.Any(f => f.Availability == SessionReport.AvailabilityReport.AvailabilityStatus.Available) &&
report.FrameFilters.All(f => f.Availability == SessionReport.AvailabilityReport.AvailabilityStatus.Available))
{
Session.AssembleUpdate -= OnAssembleUpdate;
// session 组件在当前设备上可用，可以启动 session
Session.StartSession();
}
else
{
// session 组件在当前设备上不可用
}
if (report.PendingDeviceList.Count <= 0)
{
Session.AssembleUpdate -= OnAssembleUpdate;
}
}
```
注意 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件可能会触发两次。上面的代码示例中，会在确认组件可用后取消订阅事件。
这种判断方法没法判断 session 启动过程中可能出现的其它错误，但这些错误通常是设备无关的，如有需要可以在启动 session 后通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件进行补充判断。
## session 组件不可用时的选择
在应用开发中，一般都希望对尽量多的设备提供兼容支持。因此当 session 组件在当前设备上不可用时，可以考虑以下几种选择：
* 降级使用其它 AR 功能
通过修改 session 组件配置，选择当前设备支持的 AR 功能。可以参考 [创建 session](session-creation.html) 了解如何修改 session 组件配置。
* 提供非 AR 体验
在 session 组件不可用时，提供一个非 AR 的体验。比如在导航场景下，如果 AR 导航无法实现，提供传统2D导航是非常有用的。
* 提示用户更换设备
在某些应用场景下，用户可能会使用不支持 AR 功能的设备。此时可以提示用户更换设备以获得更好的体验。
在选择这些方案时，可以结合应用的具体需求和用户群体进行权衡。在 AR 应用中，如果部分设备确实无法提供 AR 或降级方案，仍然需要提供一个良好的用户提示信息，以便让用户了解当前设备的限制。
## 后续步骤
* 了解 [控制 session 执行](session-ctrl.html) 的方法
* 了解 [帧数据源及运行时选取](../cameras/frame-source.html)
* 另外，您还可以通过下面这些示例来了解获取报告之后的应用场景：
* [Workflow\_ARSession 示例](sample-arsession.html) 使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示，同时还使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件在 UI 上展示了每个组件的可用性
* SpatialMap\_Sparse\_AllInOne 示例使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件对设备支持进行了提前判断和不可用提示
* MotionTracking\_DeviceMotionAndPlaneDetection 示例使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示
* MegaBlock\_Basic 示例使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示

---

## 访问 session 中的 AR 功能组件
- 章节路径: `unity/fundamentals/session-components.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-components.html

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

---

## 创建和配置 AR session
- 章节路径: `unity/fundamentals/session-creation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-creation.html

# 创建和配置 AR session
在 Unity 中使用 AR，需要首先在场景中创建并配置 AR session。本文介绍了创建和配置 AR session 的几种主要方法。一般在成功创建 session 之后，在 `Hierarchy` 视图中可以看到如下结构：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-result.png)
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
## 创建默认配置的 session
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `AR Session ([ 功能 ] Preset)` 可以创建一个预设好的 session。session 预先配置了适合该功能的 frame source 和 frame filter 组件。
在脚本中，可以使用 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 来创建 session。
比如，通过菜单 `EasyAR Sense` > `Image Tracking` > `AR Session (Image Tracking Preset)` 可以创建一个用于图像跟踪的 session。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation.png)
对应的脚本代码如下：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.ImageTracking);
```
需要注意的是，在使用 [ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapBuilder) 以及 [ARSessionFactory.ARSessionPreset.DenseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_DenseSpatialMapBuilder) 预设时，需要同时传入资源参数。例如，下面的代码创建了一个用于稀疏空间构建的 session，并指定了点云材质：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder, new ARSessionFactory.Resources { SparseSpatialMapPointCloudMaterial = PointCloudMaterial });
```
如果脚本只在编辑器中运行，也可以使用默认编辑器资源：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder, ARSessionFactory.Resources.EditorDefault());
```
菜单 `EasyAR Sense` > `AR Session (Preset)` > `\*\*` 中列出了所有可以使用的预设 session，可以参考使用。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-presets.png)
> **注意**
同一个场景中多个 session 同时运行会相互冲突，因此在场景中最多只能保留一个被启用（[GameObject.activeInHierarchy](https://docs.unity3d.com/ScriptReference/GameObject-activeInHierarchy.html) == `true`）的 session。
## 添加组件
session 的 frame source 和 frame filter 组件可以在 session 创建后根据需要添加和删除。
在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `\*\*` 可以添加适合该功能的 frame source 和 frame filter 组件。
在脚本中，可以使用 [ARSessionFactory.AddFrameSource<Source>(GameObject, bool)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameSource__1_UnityEngine_GameObject_System_Boolean_) 来添加 frame source 组件，或使用 [ARSessionFactory.AddFrameFilter<Filter>(GameObject, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameFilter__1_UnityEngine_GameObject_easyar_ARSessionFactory_Resources_) 来添加 frame filter 组件。
比如，通过菜单 `EasyAR Sense` > `Image Tracking` > `Frame Filter : Image Tracker` 可以给当前选中的 session 添加一个新的图像跟踪器。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-add.png)
对应的脚本代码如下：
```
ARSessionFactory.AddFrameFilter<ImageTrackerFrameFilter>(session);
```
> **小心**
添加组件必需在 assemble 前完成。session 开始执行 assemble 以及完成 assemble 后，任何对组件的增加和删除都会导致 session 进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并停止工作。
需要注意的是，在添加 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html) 以及 [DenseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.DenseSpatialMapBuilderFrameFilter.html) 时，需要同时传入资源参数。例如，下面的代码创建了一个用于稀疏空间构建的 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html)，并指定了点云材质：
```
ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, new ARSessionFactory.Resources { SparseSpatialMapPointCloudMaterial = PointCloudMaterial })
```
如果脚本只在编辑器中运行，也可以使用默认编辑器资源：
```
ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, ARSessionFactory.Resources.EditorDefault());
```
创建 frame filter 之后，可以使用 [ARSessionFactory.SetupFrameFilters(List<GameObject>, ARSessionFactory.ARSessionPreset)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_SetupFrameFilters_System_Collections_Generic_List_UnityEngine_GameObject__easyar_ARSessionFactory_ARSessionPreset_) 来根据预设配置调整 frame filter 的参数。
比如下面这段代码给 session 添加一个新的图像跟踪器，并配置成 [ARSessionFactory.ARSessionPreset.ImageTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTrackingMotionFusion) 的预设参数。
```
var filter = ARSessionFactory.AddFrameFilter<ImageTrackerFrameFilter>(session);
ARSessionFactory.SetupFrameFilters(new() { filter }, ARSessionFactory.ARSessionPreset.ImageTrackingMotionFusion);
```
使用菜单创建时无法按预设调整参数，需要在创建后根据具体的组件说明进行配置。
## 删除组件
要从 session 中删除组件，可以在 `Hierarchy` 视图中选中对应的组件并按 `Delete` 键，或者在脚本中销毁（`Destroy`）对应的物体。
> **注意**
禁用（`SetActive(false)`）组件的 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的效果与删除组件相同。
比如要从 session 中删除图像跟踪器，可以选中 `Image Tracker` 并按 `Delete` 键。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-del.png)
> **小心**
删除组件必需在 assemble 前完成。session 开始执行 assemble 以及完成 assemble 后，任何对组件的增加和删除都会导致 session 进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并停止工作。
## 组件排序的影响
session 的 frame filter 子节点的排列顺序对 session 执行没有任何影响。
session 的 frame source 子节点的排列顺序将影响 frame source 在 assemble 过程中的选择顺序。只有按 **transform 顺序** 排列的第一个可用的 frame source 会被选中作为 session 的实际 frame source。
> **注意**
frame source 节点的顺序只有在 assemble 之前修改是有效的。assemble 后，调整顺序不会影响运行结果。
## [可选] 自由创建 session
如果默认配置的 session 不能满足需求，还可用根据需要自由创建和配置 session。
可用使用菜单 `EasyAR Sense` > `AR Session (Preset)` > `AR Session (Empty)` 创建一个不包含任何 frame source 和 frame filter 组件的空 session。
在脚本中，可以使用 [ARSessionFactory.CreateSession()](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession) 来实现。
```
ARSessionFactory.CreateSession();
```
然后根据实际需要，添加合适的 frame source 和 frame filter 组件。
比如，如果需要创建一个包含稀疏空间构建和稠密空间构建功能的 session，可以使用下面的代码：
```
var session = ARSessionFactory.CreateSession();
var group = new GameObject("Frame Source Group");
group.transform.SetParent(session.transform, false);
ARSessionFactory.AddFrameSource<XREALFrameSource>(session);
ARSessionFactory.AddFrameSource<AREngineFrameSource>(session);
ARSessionFactory.AddFrameSource<ARCoreFrameSource>(session);
ARSessionFactory.AddFrameSource<ARCoreARFoundationFrameSource>(session);
ARSessionFactory.AddFrameSource<ARKitFrameSource>(session);
ARSessionFactory.AddFrameSource<ARKitARFoundationFrameSource>(session);
ARSessionFactory.AddFrameSource<VisionOSARKitFrameSource>(session);
ARSessionFactory.AddFrameSource<MotionTrackerFrameSource>(session);
List<GameObject> filters = new();
filters.Add(ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, resources));
filters.Add(ARSessionFactory.AddFrameFilter<DenseSpatialMapBuilderFrameFilter>(session, resources));
ARSessionFactory.SetupFrameFilters(filters, ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder);
ARSessionFactory.SetupFrameFilters(filters, ARSessionFactory.ARSessionPreset.DenseSpatialMapBuilder);
```
它将创建出这样的 session 结构：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-custom.png)
## 后续步骤
控制运行
* 了解 [初始化](initialization.html) 的方法和作用
* 了解如何 [判断可用性和设备支持](session-assemble.html)
* 了解 [控制 session 执行](session-ctrl.html) 的方法
访问组件和结果
* 尝试 [访问 AR 功能组件](session-components.html)
* 了解如何 [获取 session 的运行结果](session-output.html)
组件参考
* [ARSession](comp-ARSession.html) 组件参考
进一步了解 frame source 排序的影响和如何
* 了解 [帧数据源](../cameras/frame-source.html)
* 了解 [创建一组输入源](../cameras/frame-source-group.html) 的方法
根据应用功能创建最佳的 session
* [Mega](../mega/session-best-practice.html)

---

## session 的流程控制
- 章节路径: `unity/fundamentals/session-ctrl.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-ctrl.html

# session 的流程控制
在 session 的运行过程中，有时需要对 session 组件进行修改，这时就需要停止再重新启动 session。有时还可能需要停止 session 的某些输出。本文介绍了如何控制 session 的运行流程。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 了解如何 [创建 session](session-creation.html)
## session 的组装
通常在启动 session 时会自动触发组装过程。
下面这段代码会隐式执行组装过程。
```
Session.StartSession();
```
有些时候，比如需要提前 [判断可用性和设备支持](session-assemble.html)，也可以使用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 手动触发 session 组装过程：
```
StartCoroutine(Session.Assemble());
```
> **注意**
[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 返回一个协程，需要通过 [StartCoroutine(IEnumerator)](https://docs.unity3d.com/ScriptReference/MonoBehaviour.StartCoroutine.html) 启动。
## 启动 session
[AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 控制 session 是否自动启动。如果 [AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 为 `true`（默认值），则在 [MonoBehaviour.Start()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) 时 session 会自动启动。
session 也可以手动启动，这需要提前修改 [AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 为 `false`。然后可以使用 [StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 来启动 session。
```
Session.StartSession();
```
## 停止 session
可以使用 [StopSession(bool)](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StopSession_System_Boolean_) 来停止 session。
```
Session.StopSession(keepLastFrame);
```
可以通过参数 `keepLastFrame` 来控制 session 停止后是否保留最后一帧的物理相机图像。这在需要切换不同 session 时比较有用，可以避免画面闪烁。
> **注意**
`keepLastFrame` 只能控制那些由 EasyAR 进行画面绘制的 session。一般来说，使用 AR Foundation 或头显时该参数无效。
## 停止 session 输出
session 运行时，可以通过 [enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 来控制 session 的输出。
下面这段代码可以停止 session 的所有输出，这时 session 仍然处于运行状态，但不会更新任何内容（包括由 EasyAR 绘制的物理相机画面和所有 EasyAR 控制的节点的 transform 等）。
```
Session.enabled = false;
```
## 停止 session 绘制物理相机图像
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
[ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 只在由 EasyAR 进行画面绘制的 session 中有效。一般来说，使用 AR Foundation 或头显时是无效的，这时物理相机画面的绘制由 AR Foundation 或头显 SDK 完成。
## 后续步骤
* 尝试 [访问 AR 功能组件](session-components.html)，了解更多 AR 功能的控制方法
* 了解如何 [获取 session 的运行结果](session-output.html)
* 了解如何 [判断可用性和设备支持](session-assemble.html)

---

## 获取 session 的运行结果
- 章节路径: `unity/fundamentals/session-output.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-output.html

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

---

## 设备支持和 session 报告
- 章节路径: `unity/fundamentals/session-report.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-report.html

# 设备支持和 session 报告
由于设备硬件和性能差异，AR 功能很多时候并不能在所有设备上运行。所以在使用 AR 功能时准确判断当前设备的支持情况是非常重要的。本文介绍了在 Unity 中，设备可用性是如何表达的，以及如何通过 session 报告（[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report)）获取设备支持和 session 可用性的信息。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
## 设备支持、session 可用性与组装
每个 AR 功能可以支持的设备是不同的。比如运动跟踪对硬件元器件有一定要求且通常需要对设备进行标定，而图像跟踪功能则可以在几乎所有摄像头可用的设备上运行。所以判断一个 AR 应用是否可以在某个设备上运行，通常需要知道当前使用哪些 AR 功能，或者换个说法就是判断某个 session 是否可以在设备上运行。
在 Unity 中，上述判断过程是在 session 组装（[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble)）阶段完成的。组装过程会根据 session 中包含的组件和当前设备的支持情况，决定 session 启动前的最终状态。
如果组装成功，session 会进入 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态，并可以继续启动和运行；如果组装失败，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，并且可以通过 session 报告（[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report)）查询具体的失败原因。
## session 报告
[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 属性提供了 session 的运行报告，一份 session 报告包含以下字段：
|属性|描述|
|Availability|完整的可用性报告|
|BrokenReason|session 损坏原因，当 session 状态为 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 时有效|
|Exception|session 损坏具体异常，当 session 状态为 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 时有效|
在 session 报告中，可以通过 [Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 查询每个组件的可用性，或是通过 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 在 session 损坏时查询损坏的详细原因。
### 一份 session 报告示例
比如，在 Windows 上，如果 session 中包含 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html)、[CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 以及若干个其它 frame source 组件，那么组装过程会检查每个组件的可用性，并生成如下报告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-report-success.png)
可以看到图中虽然 [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html) 组件的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 是 [Unavailable](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Unavailable)，但是由于 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 和 [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 都是是 [Available](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Available)，所以整个 session 的组装是成功的，且 session 成功进入了 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态。
如果我们把 [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 从 session 中移除，那么组装过程会生成如下报告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-report-fail.png)
可以看到 [FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 列表数目从 9 变成了 8，并且虽然 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 组件的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 仍然是 [Available](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Available)，但是由于没有可用的 frame source 组件，所以整个 session 的组装失败，session 进入了 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态。此时报告中 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 字段数值是 [NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource)，表示没有可用的 frame source。
除了组装过程之外，session 运行过程中也可能出现损坏的情况，比如某个运行中的组件被意外移除等。此时同样可以通过 session 报告查询具体的损坏原因。
### 报告更新
session 报告会在以下时间点发生变化：
* 组装第一阶段完成
这时会生成一份完整的 session 报告，包含组件可用性报告。session 报告的 [Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 部分会在这时确定并不再变化。
可以通过 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告更新。
如果组装之后直接启动了 session，也可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告更新。需要关注的 session 的状态包括： [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 和 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。
* 组装第二阶段完成
这时会生成一份新的组件可用性报告。除非 session 重启，否则 session 报告不会更新。
可以通过 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告更新。
* session 启动或运行过程中 session 损坏时
session 报告的 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 和 [Exception](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Exception) 会更新。
可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告更新。需要关注的 session 的状态包括：[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。
### 报告内容：session 损坏的原因
[BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 表示 session 损坏的原因，有以下这些情况：
|原因|描述|
|Uninitialized|组装过程，EasyAR Sense 未成功初始化|
|LicenseInvalid|组装过程，EasyAR Sense license 验证失败或不适用于当前使用|
|SessionObjectIncomplete|组装过程，session 物体不完整。比如在 URP 中未正确配置 RendererFeature|
|NoAvailabileFrameSource|组装过程，无可用的 frame source。比如所有 frame source 都不可用或未添加任何 frame source。在且仅在默认 session 配置下，这种情况说明设备当前选择的 AR 功能的支持|
|FrameSourceIncomplete|组装过程，frame source 不完整。一般多出现在自定义 frame source 时未正确实现 frame source 接口|
|FrameFilterNotAvailabile|组装过程，存在不可用的 frame filter。这种情况只存在于部分组装选项下。|
|StartFailed|启动失败。比如启动过程中出现异常|
|RunningFailed|运行失败。比如运行中的组件被意外移除，或是 URP 中未正确配置 RendererFeature 等。|
### 报告内容：可用性信息
[Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 提供了 session 中每个组件的可用性信息。它包含以下字段：
|字段|描述|
|FrameFilters|组装过程检查过的 frame filter 可用性列表|
|FrameSources|组装过程检查过的 frame source 可用性列表|
|PendingDeviceList|未完成的设备列表下载任务|
|DeviceList|设备列表下载结果|
其中 [PendingDeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_PendingDeviceList) 和 [DeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_DeviceList) 字段用于表示设备支持列表的下载状态。组装第一阶段完成时，当且仅当 [PendingDeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_PendingDeviceList) 非空时，组装会进入第二阶段，可以使用这个条件来判断 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 是否会第二次执行。
## 后续步骤
* 尝试 [判断可用性和设备支持](session-assemble.html)

---

## Unity AR 的入口 —— AR Session
- 章节路径: `unity/fundamentals/session.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session.html

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

---

## EasyAR 配置
- 章节路径: `unity/fundamentals/setup-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/setup-easyar.html

# EasyAR 配置
EasyAR 配置页面可以从 Unity 菜单 `EasyAR > Sense > Configuration` 或 `Edit > Project Settings > EasyAR` 进入。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
这里包含所有对 EasyAR Sense Unity Plugin 的全局配置
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/settings-easyar.png)
## Initialize On Startup
在启动时初始化 EasyAR。通常建议保持这个选项打开。
如果关闭该选项，需要手动初始化 EasyAR Sense，具体方法可以参考 [初始化 EasyAR Sense](initialization.html) 。
## EasyAR Sense License
EasyAR Sense License 相关配置。
### LicenseKey
EasyAR Sense License Key。使用 EasyAR 功能必须填写可用的 license。
仅当使用接口手动初始化 EasyAR Sense 时可留空。
> **注意**
在头显设备（Vision Pro、XREAL、Pico、Rokid 等）设备上使用时，需要使用 EasyAR XR License。
> **注意**
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
### Verify When Build
在构建 Unity 工程时验证 license Key。
当这个选项打开时，Unity 项目构建过程会验证 license Key，如果 license 在构建平台上无效或不包含 Unity Player Settings 中设置的包名，构建过程将会失败。如果需要使用其它地方配置的 license key 或者需要在 Unity 构建过程之后修改包名，可以关闭这个选项。
## Lib Variants
EasyAR Sense 库变种配置。
## EasyAR Sense License
EasyAR Sense License 相关配置。
### LicenseKey
EasyAR Sense License Key。使用 EasyAR 功能必须填写可用的 license。
仅当使用接口手动初始化 EasyAR Sense 时可留空。
> **注意**
在头显设备（Vision Pro、XREAL、Pico、Rokid 等）设备上使用时，需要使用 EasyAR XR License。
> **注意**
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
### Verify When Build
在构建 Unity 工程时验证 license Key。
当这个选项打开时，Unity 项目构建过程会验证 license Key，如果 license 在构建平台上无效或不包含 Unity Player Settings 中设置的包名，构建过程将会失败。如果需要使用其它地方配置的 license key 或者需要在 Unity 构建过程之后修改包名，可以关闭这个选项。
## Permissions
应用权限配置。通常建议保持默认。
除相机权限外，其它权限配置不可更改，由其它功能配置所决定。
|权限|是否可改|启用条件|权限说明|
|`Camera`|是||相机权限，使用相机设备需要的权限|
|`AndroidMicrophone`|否|Variant 为 VideoRecording|麦克风权限，使用录屏功能需要的权限|
|`Location`|否|导入 Mega 支持包|（fine）定位权限，使用 EasyAR Mega 需要的权限|
## Unity XR
Unity XR 框架（AR Foundation 等）相关配置。
### AR Foundation Support
AR Foundation 支持开关，建议保持打开。
在极个别情况下，比如需要使用 AR Foundation 4 或 AR Foundation 更新导致编译出错，可以关闭这个选项，但插件内所有与 AR Foundation 相关的功能将同时禁用。
> **注意**
修改此选项之后脚本会自动重新编译。
### Unity XR Auto Switch
自动切换 Unity XR（比如 AR Foundation）物体的功能配置。
* `Editor` ：编辑模式选项
* `Disable AR Session` ：存在 [ARSession](../../../api/unity/easyar.ARSession.html) 时，编辑时禁用 AR Foundation 的 ARSession。
* `Player` ：运行模式选项
* `Enable` ：启用运行时控制。注意：关闭该选项，编辑模式被禁用的组件在运行时不会被恢复。
* `Enable If Desktop` ：在 Windows/Mac 上启用。
* `Enable If Mobile AR On Startup` ：切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。通常这个选项需要 XR Plug-in Management 中的 `Initialize XR on Startup` 是选中的。
* `Disable If Non Mobile AR Post Startup` ：切换器启动时，如果存在移动 AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。通常这个选项会在 XR Plug-in Management 中的 `Initialize XR on Startup` 未选中时被使用。
* `Restore AR Session When Disabled` ：功能禁用时，恢复（启用）所有被禁用的 AR Foundation 的 ARSession（无论它是否由 EasyAR 所禁用）。这个选项通常用于恢复编辑时被禁用的组件。
详细功能说明可参考 [Unity XR 自动切换](unity-xr-switch.html) 。
## Mega
EasyAR Mega 功能配置。
### InertialCameraDevice Support
只读选项，显示当前配置下惯导功能是否可用以及 ONNX 运行时信息。
如果显示信息不符合需求，需要视情况修改 `Lib Variants` 以及 `ONNX Runtime (Bundled)` 选项。
### Mega Block > Localization Service Access [Global]
全局 Mega Block 定位服务器配置。
### Mega Landmark > Localization Service Access [Global]
全局 Mega Landmark 定位服务器配置。
## Spatial Map
EasyAR 空间地图功能配置。
### Service Access [Global]
全局稀疏地图服务器配置。
## Image Tracking
EasyAR 图像跟踪功能配置。
### Target Gizmo
编辑器下 ImageTarget 的 Gizmos 配置。
打开这些选项将会在 Unity Editor 中显示对应 gizmo，如果场景中该类 target 过多，可能会影响编辑器中的启动性能。在设备上运行时的性能不会受到影响。
* `Enable Image File` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.ImageFileSourceData](../../../api/unity/easyar.ImageTargetController.ImageFileSourceData.html) 的 target 的 Gizmos。
* `Enable Target Data File` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.TargetDataFileSourceData](../../../api/unity/easyar.ImageTargetController.TargetDataFileSourceData.html) 的 target 的 Gizmos。
* `Enable Target` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.TargetSourceData](../../../api/unity/easyar.ImageTargetController.TargetSourceData.html) 的 target 的 Gizmos。
* `Enable Texture 2D` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.Texture2DSourceData](../../../api/unity/easyar.ImageTargetController.Texture2DSourceData.html) 的 target 的 Gizmos。
### Cloud Recognition (CRS) > Service Access [Global]
全局云识别服务器配置。
## Object Tracking
EasyAR 物体跟踪功能配置。
### Target Gizmo
编辑器下 ObjectTarget 的 Gizmos 配置。
* `Enable`：开启 Gizmos。
## Third-Party Libraries
第三方库配置。
### ARCore SDK
ARCore SDK 配置。
ARCore 提供了在部分 Android 设备上的运动跟踪能力，可以阅读 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 来了解 EasyAR 功能与运动跟踪的关系，以及是否需要和什么时候需要使用 ARCore。
* `AR Foundation Or Optional`: 随 EasyAR 或 `AR Foundation` 一起分发的 ARCore SDK 将会被包含在应用中，根据 ARCore XR Plugin 的设置决定。一般情况下推荐使用这个选项，它会自动处理 `AR Foundation` 的情况。
* `Optional`: ARCore 功能在支持 ARCore 并安装了 Google Play Services for AR 的设备上可以使用。
* `Required`: 应用将只能在支持 ARCore 并安装了 Google Play Services for AR 的设备上运行。
* `External`: 如果在使用 `AR Foundation` 或其它 ARCore SDK 分发，可以使用这个选项。这样随 EasyAR 一起分发的 ARCore SDK 将不会使用。也可以使用这个选项来完全排除 ARCore SDK 在应用中的使用。
> **小心**
如果把 `ARCore SDK` 设置为 `Required`，或是在 AR Foundation 的 ARCore 配置中将 `Requirement` 设置为 `Required`，并在不支持 ARCore 的设备上安装了打包后的应用，设备会错误地报告 ARCore 是可用的并以 ARCore 运行。这会造成一个假象，似乎这些设备正在运行 ARCore 并且运行不正常（黑屏或其它异常情况），但这是错误的。
出现这个现象的原因是由于 Google Play 商店阻止在不受支持的设备上安装标记 ARCore 为必需的应用，所以这些应用总是假设它们正在受支持的设备上运行。
正常配置下，这些设备会在 session 组装时判断 ARCore 不受支持并使用 EasyAR 的功能。
关于 `Optional` 和 `Required` 的详细说明及上线 Google Play Store 应用需要做的其它配置可以参考 Google 的说明（[中国大陆](https://developers.google.cn/ar/develop/java/enable-arcore)，[国际](https://developers.google.com/ar/develop/java/enable-arcore)）。
> **注意**
在 EasyAR Sense Unity Plugin 中，ARCore 的支持所需的库文件和配置已经在插件包中，但要在手机上运行，仍需在手机上安装 [Google Play Services for AR](https://play.google.com/store/apps/details?id=com.google.ar.core) 。
有三种不同来源的 ARCore SDK 可以使用：
* 使用随插件分发的 ARCore SDK
插件内集成了一个 ARCore SDK 版本，详细信息可以参考 [ARCore、AR Engine 版本兼容性](../motion-tracking/3rdparty-compatibility.html)。在使用 EasyAR 的 ARCore 封装时，可以不另外导入 AR Foundation。
* 使用 AR Foundation 的 ARCore SDK
如果需要使用 AR Foundation 的 ARCore SDK，可以参考 Google 的说明（[中国大陆](https://developers.google.cn/ar/develop/java/enable-arcore)，[国际](https://developers.google.com/ar/develop/java/enable-arcore)）进行配置，这时 `ARCore SDK` 选项需要选择 `AR Foundation Or Optional` 或 `External` 。
* 使用其它 ARCore SDK
如果有其它第三方插件或项目内有 ARCore SDK 的分发，也可以使用这些 ARCore SDK。这时 `ARCore SDK` 选项需要选择 `External` ，并根据具体插件或项目的要求进行配置。
**Warn 32-bit-only ARCore-enabled build**
根据 Google 的说明，在 arm64 的设备上运行仅有 armv7 库文件的程序，ARCore 不会正常工作。在打包时如果未选择 ARM64 会弹出警告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/settings-arcore-warn.png)
这时需要修改项目配置，使用 IL2CPP 编译并选择 ARM64 支持。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/adnroid-64bit.png)
> **小心**
如确有需要，可以选择 `Continue and don't warn me again`，或者关闭该选项，这将关闭打包时的检查。关闭检查只是在打包时不弹出提示，但运行时在一些设备上将有可能出现异常，包括但不限于崩溃或黑屏等。
### AR Engine SDK
AR Engine SDK 配置。
AR Engine 提供了在部分 Android 设备上的运动跟踪能力，可以阅读 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 来了解 EasyAR 功能与运动跟踪的关系，以及是否需要和什么时候需要使用 AR Engine。
* `AREngineInterop` ：AREngineInterop 可用。随 EasyAR 一起分发的 AR Engine SDK 将会被包含在应用中。
* `External` ：AREngineInterop 可用。随 EasyAR 一起分发的 AR Engine SDK 将不会使用。
* `Disabled` ：AREngineInterop 不可用。随 EasyAR 一起分发的 AR Engine SDK 将不会使用。所有与 AR Engine 有关的功能将被禁用。
### ONNX Runtime (Bundled)
是否使用捆绑的 ONNX 运行时。仅在 `Lib Variant` 为 `Full` 时有效。
如需使用不同版本的 ONNX，可用从 ONNX 官方获取更新版本并关闭该选项。使用自己编译的二进制不兼容的 ONNX 将导致未知错误。
## Workaround For Unity
针对 Unity bug 或不合理行为的应对方案。
### GenerateXMLDoc
在脚本重新加载时生成 XML 文档，以使 API 文档的 intelliSense 可以工作。
### URP17RG\_DX11\_RuinedScene
Workaround URP 17 Render Graph DX11 场景渲染被毁损。Unity 6.2 及更新版本中该选项已关闭。
### URP17RG\_IOS\_Glitches\_Partial
部分规避 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture)。
问题简述：当从 EasyAR 获取相机纹理（类似 ImageTracking\_Coloring3D示例 及 [ARSession 工作流（CameraDevice）](../cameras/sample-camera-device.html) 示例中的使用），在 iOS/Mac 设备上可以观察到视觉故障和伪影。我们已经在纯 Unity 包中复现该问题并报告给了 Unity： [Glitches on iOS with AR Camera Image Rendering (URP 17 render graph)](https://discussions.unity.com/t/glitches-on-ios-with-ar-camera-image-rendering-urp-17-render-graph/1548048) 。问题进展可以关注 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 更新以及 Unity 未来版本的发布日志。

---

## Player 配置
- 章节路径: `unity/fundamentals/setup-player.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/setup-player.html

# Player 配置
本文介绍在 Unity 中使用 EasyAR Sense Unity Plugin 打包应用时需要注意的 Player 配置选项。
## 不同平台配置说明
在 Unity 打包时，需要检查并确认下列配置。
依次在 Unity 菜单 `File -> Build Settings-> Player Settings`，点击安卓图标，调出 Android平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
通常情况下需要设置以下选项。
* Package Name
设置 Android 应用的 `Package Name`, **注意 `Package Name` 要与创建 License Key 时填写的必须一致**。
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
* API Level
EasyAR 支持的 `API level` 与使用的版本有关， 使用 `Full` 变种时，需要 `Android API Level 24` 或以上; 使用其他变种时，EasyAR Sense 需要 `Android API Level 21` 或以上。
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* Target Architecture
如果需要使用 Google ARCore ，或其它情况需要编译支持 ARM64 ，需要使用 `IL2CPP` 编译并选择 `ARM64 支持`。在不需要支持 ARM64 架构的情况下无需配置。
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/adnroid-64bit.png)
* 视频录制功能的特殊配置
如果要使用视频录制功能，需设置 `Graphics API` 为 `OpenGLES3` 或 `OpenGLES2`，并去掉 `Multithreaded Rendering` 的勾选。另外还需要在 EasyAR 配置 中将 `Lib Variants > Android` 设为 `VideoRecording` 。
![androidvideorecord](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-video-recording.png)
依次在 Unity 菜单 `File -> Build Settings-> Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
通常情况下需要设置以下选项。
* Bundle ID
设置 iOS 应用的 `Bundle ID`, 注意 `Bundle ID` 与创建 License Key 时填写的**必须一致**。
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
* Target Architecture
在 `Player Settings` 中修改 `architecture` 为 `ARM64`, 不可使用 `Universal`。
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* Usage Description配置
根据 EasyAR 配置 中 Permissions 中的启用情况，需要配置不同的 Usage Description。
* 如果 `Camera` 权限开启，需要添加 `Camera Usage Description`，否则构建将失败。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-camera-permission.png)
* 如果 `Location` 权限开启，需要添加 `Location Usage Description`，否则构建将失败。
![ioslocationpermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-location-permission.png)
* 需要 EIF 录制的额外配置（XCode 工程，需要时）
若需要录制 EIF 到默认目录并通过 iOS 的文件应用投送到电脑或其他设备，需要在 `Info.plist` 中增加 `UIFileSharingEnabled` 并将值设置为 `true`。
![iosstore](https://doc-asset.easyar.com/develop/unity/fundamentals/media/ios-plist-uifilesharingenabled.png)
## 常见问题
下面是与Player 配置相关的一些常见错误和解决方案。
* License Key 异常的报错
如果 License Key 异常（比如 `Package Name` 不匹配），在打包应用时将会类似 `is not a valid EasyAR Sense license key or it does not match package name `。这时如果选择继续打包，打包出的应用将无法正常使用，请根据窗口提示仔细检查并修复问题后再继续打包。
* 关闭打包时的许可证检查
在一些特殊情况，如果你使用 EasyAR 的接口手动初始化，不使用 `Setttings` 文件中的 `License Key`，你可以选择 `Continue and don't warn me again` ，或者关闭 EasyAR 配置 中的 `EasyAR Sense License > Verify When Build` 选项，这将关闭打包时的检查。
* 非 ARM 架构的 Android 设备支持
EasyAR Sense 不直接支持 x86 及 x86-64 架构的 Android 系统，但是一般x86架构的设备芯片可以兼容 ARM 程序，因此需要配置取消选择 x86 架构，这样在一些 x86 设备上可以正常使用。

---

## 获取 target 的状态
- 章节路径: `unity/fundamentals/target-state.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/target-state.html

# 获取 target 的状态
session 运行过程中，target 会经历跟踪和丢失等状态变化。通过以下内容，您将了解如何获取和使用 target 的状态信息，以及如何使用 found 和 lost 事件来控制内容的显示。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [Target](target.html) 了解 target 的基本概念、状态和生命周期。
## 判断 target 是否被跟踪
可以使用 [TargetController.IsTracked](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_IsTracked) 属性判断 target 是否被跟踪。
## 使用 target 的 found 和 lost 事件
可以使用 [TargetController.TargetFound](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetFound) 和 [TargetController.TargetLost](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetLost) 事件来处理 target 被跟踪和丢失的情况。
比如，下面的代码展示了在 target 被跟踪时播放视频，并在 target 丢失时暂停视频播放的过程：
```
target.TargetFound += () =>
{
if (player && player.gameObject.activeInHierarchy)
{
player.Play();
}
};
target.TargetLost += () =>
{
if (player && player.gameObject.activeInHierarchy)
{
player.Pause();
}
};
```
> **小心**
如果没有手动卸载 target，[TargetController.TargetLost](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetLost) 有可能在 session 停止时被调用。如果没有手动停止 session，则它可能在 session 的 OnDestroy 过程中被调用，由于 Unity 的 OnDestroy 执行顺序是不受保证的，所以在事件中使用的对象需要进行有效性检查以避免在 OnDestroy 过程中访问已经被销毁的对象。
## 后续步骤
* [active 控制策略](active-control.html) 介绍了 target 下物体的默认显示和隐藏策略，以及如何根据需要进行调整。

---

## Unity AR 的跟踪目标 —— target
- 章节路径: `unity/fundamentals/target.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/target.html

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

---

## Unity 兼容性
- 章节路径: `unity/fundamentals/unity-compatibility.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-compatibility.html

# Unity 兼容性
本文介绍 EasyAR Sense Unity Plugin 所兼容的 Unity 版本和配置要求。
## Unity 版本
EasyAR Sense Unity Plugin 支持 **Unity 2021.3** 或更高版本。
开发 Mega 功能所需的 EasyAR Mega Studio 支持 **Unity 2021.3.30** 或更高版本。
> **提示**
通常来说, EasyAR 不依赖很多变化的 Unity API，所以如果 Unity 发布了新版本，EasyAR Sense Unity Plugin 一般都可以正常使用。
EasyAR Sense Unity Plugin 从版本 4.6.4 开始支持 Unity 6 的 URP 17+ Render Graph。
## 开发平台
|操作系统|操作系统版本|CPU 架构|补充说明|
|**Windows**|7 及以上版本（7/8.1/10/11）|x86, x86\_64|Windows N/KN 版本需要安装 Media Feature Pack 才能使用|
|**macOS**|10.15 及以上版本|x86\_64, arm64||
另外，需要满足对应版本的 [Unity 开发系统要求](https://docs.unity3d.com/Manual/system-requirements.html) 。
## 发布平台
|操作系统|操作系统版本|CPU 架构|补充说明|
|**Windows**|7 及以上版本（7/8.1/10/11）|x86, x86\_64|Windows N/KN 版本需要安装 Media Feature Pack 才能使用|
|**macOS**|10.15 及以上版本|x86\_64, arm64||
|**Android**|5.0 及以上版本|armv7a, arm64-v8a|arm64-v8a 支持需要开启 IL2CPP|
|**鸿蒙（手机端）**|1.0 – 4.x 原生支持
5 以上通过 Android 应用兼容层支持|arm64-v8a||
|**iOS**|12.0 及以上版本|arm64|Architecture 需配置为 ARM64，不支持配置为 Universal|
|**visionOS**|2.0 及以上版本|arm64||
另外，需要满足对应版本的 Unity 的发布平台要求：
* [Windows](https://docs.unity3d.com/Manual/windows-requirements-and-compatibility.html)
* [macOS](https://docs.unity3d.com/Manual/macos-requirements-and-compatibility.html)
* [Android](https://docs.unity3d.com/Manual/android-requirements-and-compatibility.html)
* [iOS](https://docs.unity3d.com/Manual/ios-requirements-and-compatibility.html)
* [visionOS](https://docs.unity3d.com/Manual/visionOS.html)
特殊说明：
* **关于 Mac Apple silicon：**
EasyAR Sense Unity Plugin 支持在 Apple silicon 设备上原生运行，且可以在 Unity 编辑器中正常使用。
由于 Unity 对原生插件支持的 bug，在部分 Unity 版本中，为 *"Apple silicon"* 或 *"Intel 64-bit + Apple silicon"* 构建的应用可能无法正常工作。如果发现应用在 Mac 上无法使用，且显示类似 "Fail to load EasyAR library" 或 "DllNotFoundException: EasyAR assembly" 的错误，建议使用新版本的 Unity 或向 Unity 和 Unity 社区寻求帮助。
* **关于 Android 16 KB 内存页面大小支持：**
EasyAR Sense Unity Plugin 从版本 4000 开始支持具有 16 KB 内存页面大小的设备。
这是 Android 15 中引入的功能。有关该功能的更多信息，请参阅 Android 文档中关于[支持 16 KB 页面大小](https://developer.android.com/guide/practices/page-sizes)的内容。
* **关于 WebGL：**
EasyAR Sense Unity Plugin 不支持 Unity 的 WebGL。
直接使用 EasyAR 云服务接口（比如 [CRS 服务接口](../../cloud-recognition/management.html)）开发的功能可以发布到 Web 平台。
* **关于录屏功能：**
录屏功能仅支持 Android 平台，且需配置 Graphics API 为 OpenGLES2 或 OpenGLES3。
## Graphics API
EasyAR Sense Unity Plugin 直接使用 Unity 的渲染管线，所有 Unity 中可以使用的图形 API 都可以支持。
## Scriptable Render Pipeline
EasyAR Sense Unity Plugin 支持 Universal Render Pipeline (URP) 7.0.0 或更新版本。
EasyAR Sense Unity Plugin 不支持 High Definition Render Pipeline (HDRP)。
> **注意**
**关于 Unity 6 URP 17+ render graph 支持的声明**
EasyAR 支持 Unity 6 URP 17+ render graph，但是 Unity 本身仍存在部分未解决的问题。在遇到异常情形时可以尝试使用 Unity 提供的 [URP 兼容模式](https://docs.unity3d.com/6000.2/Documentation/Manual/urp/compatibility-mode.html) 。
部分问题已经在最新版本的 Unity 中得到解决，建议使用 6.2 及以上版本。
非兼容模式下的已知问题包括：
1. [未解决] 当从 EasyAR 获取相机纹理（类似 ImageTracking\_Coloring3D 示例及 [ARSession 工作流（CameraDevice）](../cameras/sample-camera-device.html) 示例中的使用），在 iOS/Mac 设备上可以观察到视觉故障和伪影。我们已经在纯 Unity 包中复现该问题并报告给了 Unity： [Glitches on iOS with AR Camera Image Rendering (URP 17 render graph)](https://discussions.unity.com/t/glitches-on-ios-with-ar-camera-image-rendering-urp-17-render-graph/1548048) 。问题进展可以关注 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 更新以及 Unity 未来版本的发布日志。
对于所有版本的 Unity 6，可以使用 [部分缓解措施](../../../api/unity/easyar.EasyARSettings.Workaround.html#u_easyar_EasyARSettings_Workaround_URP17RG_IOS_Glitches_Partial)，默认开启。
对于 Unity 6.2 及更新版本，可以将 Universal Render Pipeline Asset 中的 Render Scale 设置为 0.96-1.05 以外的数值来规避这个问题。
2. [Unity 6.2 已修复] Windows DX11 上相机画面会让场景中的物体渲染效果不可预测。在 Unity 6.0 - 6.1 版本中，EasyAR 提供 [规避选项](../../../api/unity/easyar.EasyARSettings.Workaround.html#u_easyar_EasyARSettings_Workaround_URP17RG_DX11_RuinedScene)] 且默认开启。

---

## 在 Unity 场景中自动切换 Unity XR 物体
- 章节路径: `unity/fundamentals/unity-xr-switch.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-xr-switch.html

# 在 Unity 场景中自动切换 Unity XR 物体
Unity 的 XR 组件（包括 AR Foundation）所能支持的设备有限。为了在受支持的设备上使用 AR Foundation，同时又能在其它大量设备上使用 AR 功能，EasyAR 提供了自动切换 Unity XR 物体的功能。以下内容介绍该功能对场景物体的改动及使用方法。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
* 确保场景已按 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html) 所描述，添加了 AR Foundation 的 [ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html) 及 [XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html)。
## 功能介绍
由于 Unity 的 AR Foundation 在手机上底层实现是 ARCore 和 ARKit，只能在有限的设备上使用，尤其是在很多国产 Android 手机上无法使用，所以通常建议仅在受支持的设备上启用 AR Foundation 及相关功能脚本。自动切换 Unity XR 物体的功能实现了上述操作，主要为移动 AR 设计，头显上默认配置下功能会被禁用。
在完整功能启用时，
* 编辑器中，[easyar.ARSession](../../../api/unity/easyar.ARSession.html) 会禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)
* 运行时，[easyar.ARSession](../../../api/unity/easyar.ARSession.html) 会在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 时禁用所有 Unity XR Core 组件及 AR Foundation 的组件。
* 运行时，如果被选择的 [FrameSource](../../../api/unity/easyar.FrameSource.html) 继承自 [ARFoundationFrameSource](../../../api/unity/easyar.ARFoundationFrameSource.html) 或是实现了 [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin) 原点的 [ExternalDeviceFrameSource](../../../api/unity/easyar.ExternalDeviceFrameSource.html)，则被禁用的 Unity XR Core 组件及 AR Foundation 组件将在 [easyar.ARSession.StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 时启用（未被 EasyAR 禁用的不会启用）。如果其他 [FrameSource](../../../api/unity/easyar.FrameSource.html) 被选择，则在 [easyar.ARSession.StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 时会禁用所有 Unity XR Core 组件及 AR Foundation 的组件。
* 运行时，所有 Unity XR Core 组件及 AR Foundation 的组件会在 [easyar.ARSession.StopSession(bool)](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StopSession_System_Boolean_) 时禁用。
默认配置下，功能启用条件如下，
* 在 Windows/Mac 上启用。
* 切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。
* 切换器启动时，如果存在移动AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。
> **注意**
XR Interaction Toolkit 的组件不受该功能控制，但其在 EasyAR 中是否可用未经验证。理论上对于只使用 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) GameObject 及其 Camera 的功能应该可以正常使用。如果行为异常可以尝试设置 [ARSession.ARCenterMode](../../../api/unity/easyar.ARSession.ARCenterMode.html) 为 [ARSession.ARCenterMode.SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)。如果功能还是不正常，则需要实现自定义的 XR Interaction Toolkit 的组件控制，在 [FrameSource](../../../api/unity/easyar.FrameSource.html) 不是继承自 [ARFoundationFrameSource](../../../api/unity/easyar.ARFoundationFrameSource.html) 时禁用相关组件。
## 配置方法
这个功能可以通过 `Project Settings` > `EasyAR` > `Sense` 中的 `Unity XR` > `Unity XR Auto Switch` 中的选项启用或关闭。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/xr-auto-switch.png)
图中选项配置功能行为如下：
* **Editor**：编辑模式选项
* **Disable AR Session**：存在 [easyar.ARSession](../../../api/unity/easyar.ARSession.html) 时，编辑时禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)。
* **Player**：运行模式选项
* **Enable**：启用运行时控制。注意：关闭该选项时编辑模式被禁用的组件在运行时不会被恢复。
* **Enable If Desktop**：在 Windows/Mac 上启用。
* **Enable If Mobile AR On Startup**：切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。通常这个选项需要 `Project Settings` > `XR Plug-in Management` 中的 `Initialize XR on Startup` 是选中的。
* **Disable If Non Mobile AR Post Startup**：切换器启动时，如果存在移动AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。通常这个选项会在 `Project Settings` > `XR Plug-in Management` 中的 `Initialize XR on Startup` 未选中时被使用。
* **Restore AR Session When Disabled**：功能禁用时，恢复（启用）所有被禁用的 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)（无论它是否由 EasyAR 所禁用）。这个选项通常用于恢复编辑时被禁用的组件。
## 使用自定义的控制方法
如果需要自定义这些组件的切换，或是 EasyAR 的行为干扰了某些组件的正常工作，需要确保关闭这些选项，同时根据以下基本规则自定义组件切换：
1. 在编辑器中禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)（它在执行时序中早于所有其它脚本）
2. 在 AR Foundation 开始工作前禁用所有 Unity XR Core 组件及 AR Foundation 的组件以及需要控制的相关组件或功能
3. 如果 [easyar.ARSession.Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 过程中选择了 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 或 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)，启用之前禁用的所有组件或功能，需要在 [StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 完成前完成，通常建议在 [easyar.ARSession.AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件响应中完成
4. 如果 [easyar.ARSession.Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 过程中选择使用了其它 [FrameSource](../../../api/unity/easyar.FrameSource.html)，则保持不变
## 相关主题
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)

---

## EasyAR 对 Unity XR 框架的支持
- 章节路径: `unity/fundamentals/unity-xr.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-xr.html

# EasyAR 对 Unity XR 框架的支持
EasyAR 并不依赖 Unity XR 框架来提供 AR 功能，但可以支持 Unity XR 框架中的部分组件包，以便在 Unity 中使用 EasyAR 的 AR 功能时可以利用 Unity XR 框架提供的功能。以下内容介绍了 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
## Unity XR 支持
Unity 通过其 [插件框架及一系列功能包和工具包](https://docs.unity3d.com/Manual/xr-support-landing.html) 支持 XR 开发。EasyAR 也支持这些 Unity XR 组件包，以便在 Unity 中使用 EasyAR 的 AR 功能时可以利用 Unity XR 框架提供的功能。
EasyAR 支持以下 Unity XR 组件包：
|显示名称|包名|最低支持版本|是否必需|用途|
|**XR Core Utilities**|com.unity.xr.core-utils|2.0.0|否|提供 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 支持|
|**AR Foundation**|com.unity.xr.arfoundation|5.0.0|否|提供 AR Foundation 支持|
|**XR Plugin Management**|com.unity.xr.management|3.0.0|否|提供 ARCore SDK 管理兼容及获取运行时 XR Loader 类型|
|**XR Interaction Toolkit**|com.unity.xr.interaction.toolkit|2.0.0|否|未直接使用|
|**PolySpatial visionOS**|com.unity.polyspatial.visionos|2.0.4[1](#fn:1)|否|未直接使用|
|**Apple visionOS XR Plugin**|com.unity.xr.visionos|2.0.4[1](#fn:1)|否|未直接使用|
|**Apple ARKit XR Plugin**|com.unity.xr.arkit|5.0.0|否|未直接使用|
|**Google ARCore XR Plugin**|com.unity.xr.arcore|5.0.0|否|提供 ARCore SDK 管理兼容|
> **注意**
EasyAR 并不依赖 Unity XR 框架来提供 AR 功能。因此，在没有 AR Foundation 等 Unity XR 组件的使用需求时，可以不安装这些组件包，EasyAR 仍然可以在受支持的设备上正常工作。
## AR Foundation 支持
[AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest) 是 Unity 提供的 AR 开发框架，其 AR 功能通过底层系统或第三方实现，常用于支持 ARCore、ARKit 以及部分头显。
### EasyAR 与 AR Foundation 的关系
```
block
columns 6
block:groupApp:6
block:groupAppWrapper
space
App1["EasyAR<br>App"]
space
App2["EasyAR + AR Foundation<br>App"]
space
App3["AR Foundation<br>App"]
end
end
block:groupSensePlugin:4
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupAREngineInterop
columns 1
AREngineInterop["EasyAR<br>AR Engine Interop"]
space
end
block:groupSense:3
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
Image["Image<br>Tracker"]
Object["Sparse<br>SpatialMap"]
MotionTracker["Motion<br>Tracker"]
MARCore["ARCore"]
MARKit["ARKit"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:6
columns 1
System["System Library"]
block:groupSystemWrapper
space
AREngine["AR Engine<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
ARCore["ARCore<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
ARKit["ARKit<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePlugin --> App1
SensePlugin --> App2
ARF --> App2
ARF --> App3
groupSense --> SensePlugin
groupAREngineInterop --> SensePlugin
AREngine --> groupAREngineInterop
XRSubsystem --> ARF
XRSubsystem --> XRI
ARCore --> MARCore
ARKit --> MARKit
ARCore --> XRSDK
ARKit --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style AREngineInterop fill:none,stroke:none,stroke-width:0px,color:#fff
style Sense fill:none,stroke:none,stroke-width:0px,color:#fff
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px,color:#fff
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class groupAREngineInterop EasyAR
class groupSense EasyAR
class SensePlugin EasyAR
classDef Unity fill:#636,stroke:#333,color:#fff
class groupXRSubsystem Unity
class ARF Unity
class XRI Unity
```
EasyAR 与 AR Foundation 是两个独立的 AR 框架，EasyAR 并不依赖 AR Foundation 来实现其 AR 功能。EasyAR 也可以通过系统中的 ARKit、ARCore 等系统库来实现运动跟踪能力。同时，EasyAR 还提供了 AR Foundation 所不具备的两种运动跟踪实现：EasyAR 自身的运动跟踪实现以及通过 AR Engine 提供的运动跟踪实现，从而提供了相比 AR Foundation 更加广泛的设备支持。
同时，EasyAR 可以获取 AR Foundation 运行时的数据，在 AR Foundation 运行时利用它所提供的运动跟踪能力驱动其它 AR 功能运行，从而提供对 AR Foundation 的兼容性。这些功能包括：
* Mega
* 稀疏空间地图
* 稠密空间地图
* 使用运动融合的图像跟踪和物体跟踪
可以参考 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 了解更详细的运动跟踪与 EasyAR 功能的关系。
### 什么情况下需要使用 AR Foundation
多数情况下，可以不使用 AR Foundation，EasyAR 会在比 AR Foundation 所支持的更加广泛的设备上正常工作。通常在以下两种情况下可以考虑使用 AR Foundation：
1. 需要使用 EasyAR 未封装的 ARKit 及 ARCore 功能
如果需要使用的 ARCore 或 ARKit 提供的一些功能在 EasyAR 中未封装，可以使用 AR Foundation。比如 AR Foundation 提供了对 ARKit 人脸跟踪的支持 [ARFaceManager](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARFaceManager.html)，EasyAR 并没有封装这个功能。
2. 在部分系统存在问题的小米手机上使用 ARCore 而非 EasyAR 实现的运动跟踪
如果需要在所有支持 ARCore 的小米和红米手机上使用 ARCore，可以考虑启用 AR Foundation。由于部分小米和红米手机系统存在问题，EasyAR 的 ARCore 封装不支持这些设备，包括米 9、米 10、红米 K20、红米 K30、红米 K40 等系列（这里列出的不全，设备支持会持续更新）。在这些手机上，默认配置下将不会使用 ARCore，在支持 EasyAR 运动跟踪的手机上会使用EasyAR 运动跟踪。
使用 AR Foundation 时 EasyAR 的功能效果并不是最优的。存在两种情况：
1. 在 EasyAR 不直接支持的那部分小米和红米手机上，输入 EasyAR 的数据是灰度图而非彩色图，这会影响部分算法的效果。由于设备自身问题，这是无法通过配置解决的。
2. 在使用 Mega 时，AR Foundation 默认使用的配置并不是最优的。
> **小心**
可以通过修改 AR Foundation 的 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 来获取更优的数据输入，启用 [ARCoreARFoundationFrameSource.OptimizeConfigurationForTracking](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html#u_easyar_ARCoreARFoundationFrameSource_OptimizeConfigurationForTracking) 可以自动完成最佳 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 选择。但需要注意部分手机自身（比如小米 10）存在问题，在修改配置之后无法获取图像，EasyAR 将无法使用（应用有图像背景但 EasyAR 功能没有任何反应），因此通常并不建议启用，如需使用需要做好 EasyAR 无法使用时的降级方案。
## 头显支持
由于 Unity XR 框架未提供足够充分的数据接口，因此 EasyAR 并不通过 Unity XR 框架来支持头显。
在支持 Unity XR 框架的头显上，EasyAR 会通过 **XR Core Utilities** 支持 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 的使用，但并不使用 Unity XR 框架来实现头显的支持。EasyAR 不会影响 **XR Interaction Toolkit** 的功能，只要设备支持就可以正常使用。
一般来说，头显厂商各自提供了 SDK 或系统接口来提供这些数据，EasyAR 通过系统接口以及厂商的 SDK 来支持头显。有些时候这些 SDK 并不是完全公开的，EasyAR 会与厂商合作提供完整支持。[Unity 中的头显支持](../headsets/headsets.html) 介绍了 EasyAR 支持的头显及其使用方法。
## 后续步骤
* 了解如何 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html)
* 了解 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html)
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)
* [Unity 中的头显支持](../headsets/headsets.html)
1. Unity 6 及更新版本中，最低支持 2.0.4。Unity 2022.3 中，最低支持 1.2.3，不支持 1.3.x。[↩](#fnref:1)[↩](#fnref:2)

---

## 充分利用 UI 诊断信息和工具
- 章节路径: `unity/getting-started/diagnostics.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/diagnostics.html

# 充分利用 UI 诊断信息和工具
本文介绍了如何快速配置和使用 UI 诊断信息和开发者模式工具，以便在开发和测试阶段更好地调试和优化应用。
## 阅读 UI 消息
默认配置下，运行 EasyAR Sense Unity Plugin 应用时，诊断信息会通过 UI 消息显示在屏幕偏上位置，方便开发者了解 session 的运行状态和问题。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message-ui.png)
> **提示**
这些文字不是水印，可以根据需要显示或隐藏。
这些信息可以帮助开发者了解 session 的运行状态和问题，建议在开发和测试阶段保持显示。
可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Message Output` 来配置 UI 消息的显示方式。其中 `Message Output` > `Session Dump` 可以控制 session 状态信息的显示，其它选项可以控制不同级别的诊断消息的显示方式。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message.png)
通常建议在开发和测试阶段，进行以下配置：
* Message Output > Session Dump： `UI`
* Message Output > Sense Error： `UIAndLog`
* Message Output > Session Error： `UIAndLog`
* Message Output > Error： `UIAndLog`
* Message Output > Warning： `UIAndLog`
在发布上线阶段，进行以下配置：
* Message Output > Session Dump： `None`
* Message Output > Sense Error： `Log`
* Message Output > Session Error： `Log`
* Message Output > Error： `Log`
* Message Output > Warning： `Log`
## 使用开发者模式工具
默认配置下，运行 EasyAR Sense Unity Plugin 应用时，快速点击屏幕 8 次会在靠屏幕右边中间位置弹出开发者模式面板，方便开发者查看和调试 session 的运行状态以及录制用于模拟运行的数据。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode-panel.png)
* 可以通过 `session` 右边的切换按钮来切换屏幕上方信息的显示与否。
* 可以通过 `eif` 右边的 `rec` 按钮来启动或停止 EIF 录制功能。录制的 EIF 文件会保存在应用的持久化数据路径中，可以通过 `Application.persistentDataPath` 来获取该路径。
如果要禁用开发者模式面板，可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Developer Mode Switch` 为 `Custom`。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode.png)
通常建议在开发和测试阶段，进行以下配置：
* Developer Mode Switch： `Default`
在发布上线阶段，进行以下配置：
* Developer Mode Switch： `Default` 或 `Custom`
如果选择 `Custom`，建议以其它方式保证线上应用可以使用诊断面板或自定义的方式收集运行时数据。
## 延伸阅读
* [诊断功能简介](../diagnostics/diagnostics.html)
* [UI 消息](../diagnostics/ui-messages.html) 介绍了如何使用 UI 消息来显示 session 状态
* [开发者模式](../diagnostics/developer-mode.html) 介绍了如何使用开发者模式进行调试

---

## 导入 EasyAR 插件以启用 AR 功能
- 章节路径: `unity/getting-started/enable-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/enable-easyar.html

# 导入 EasyAR 插件以启用 AR 功能
本教程介绍如何在 Unity 中启用 EasyAR 插件。
## 使用兼容的 Unity 版本
确保已安装兼容的 Unity 版本（Unity 2021.3 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
## 导入 EasyAR Sense Unity Plugin
在[下载页面](https://www.easyar.cn/view/download.html)，您会看到 Unity 插件有两个版本：`EasyAR Sense Unity Plugin` 和 `EasyAR Sense Unity Plugin (for Mega)`。
这两个版本的主要差异为：
* **EasyAR Sense Unity Plugin**： 不含 Mega 支持文件，不能用于 Mega 开发。EasyAR 提供从 4.6 开始的历史版本下载。
* **EasyAR Sense Unity Plugin (for Mega)**：包含 Mega 支持文件，可以用于 Mega 开发。EasyAR 不提供历史版本下载。
在不需要开发 Mega 功能时，建议使用 `EasyAR Sense Unity Plugin`。
* 下载插件包
* 下载最新版本的 [EasyAR Sense Unity Plugin](https://www.easyar.cn/view/download.html)。
* 解压下载的 `zip` 包之后可以看到 `readme` 和 `.tgz` 文件，`.tgz` 文件可以直接导入 Unity， 不能解压。
* 将 `.tgz` 文件存放到 Unity 项目 `Packages` 文件夹内。
* 导入插件包
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`。
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`。
* 在弹出的对话框中选择前述 `.tgz` 文件。
![ImportUnityPlugin](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_easyar_unity_plugin.png)
> **注意**
`.tgz` 文件在导入 Unity 后不能被删除或移动到另一个位置，需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 填写许可证（License Key）
从 Unity 菜单中选择 `EasyAR` > `Sense` > `Configuration` 调出 EasyAR Sense 设置界面。
![FillInKey](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
在 `EasyAR Sense License` 下的输入框中填入 EasyAR Sense License。
![FillInKey2](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill-in-key2.png)
> **提示**
EasyAR Sense License 可以从 EasyAR 开发中心（[中文](https://portal.easyar.cn/sdk/list)，[英文](https://portal.easyar.cn/sdk/list)） 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `是`，名称随意填写
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
> **注意**
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
## 后续步骤
* 可以阅读 [配置 AR 场景](scene.html) 了解如何创建一个简单的 AR 场景。
## 相关主题
* 如果需要开发 Mega 功能，可以 [导入最新版本的 EasyAR 插件以启用 Mega 功能](../mega/enable-mega.html)。

---

## 使用示例快速入门 EasyAR Unity 开发
- 章节路径: `unity/getting-started/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/quickstart.html

# 使用示例快速入门 EasyAR Unity 开发
本教程介绍如何配置并运行 EasyAR Unity 示例，以快速入门 AR 开发。
## 准备空 Unity 工程
确保已安装兼容的 Unity 版本（Unity 2021.3 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
使用 `3D (Built-in Render Pipeline)` 模板创建空 Unity 工程：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/create-project.png)
> **注意**
初次使用不建议使用 URP。
如果您在使用 Unity 6，需要手动下载并使用 `3D (Built-In Render Pipeline) Template`，默认安装下它在模板列表靠后的位置。
> **重要事项**
若要使用 URP，必须按照 [Universal Render Pipeline (URP)](universal-render-pipeline.html) 进行额外配置，否则相机画面将无法显示。
## 导入 EasyAR Sense Unity Plugin
* 下载插件包
* 下载最新版本的 [EasyAR Sense Unity Plugin](https://www.easyar.cn/view/download.html)，其中包含示例（sample）。
* 解压下载的 `zip` 包之后可以看到 `readme` 和 `.tgz` 文件，`.tgz` 文件可以直接导入 Unity， 不能解压。
* 将 `.tgz` 文件存放到 Unity 项目 `Packages` 文件夹内。
* 导入插件包
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`。
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`。
* 在弹出的对话框中选择前述 `.tgz` 文件。
![ImportUnityPlugin](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_easyar_unity_plugin.png)
> **注意**
`.tgz` 文件在导入 Unity 后不能被删除或移动到另一个位置，需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 导入示例
使用菜单 `Window` > `Package Manager` 打开 Package Manager，选中 `EasyAR Sense Unity Plugin`, 在右侧选择 `\*\*All Samples\*\*` 一次性导入所有示例。
![ImportSample](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_samples.png)
> **小心**
`\*\*All Samples\*\*` 和其他示例不可同时导入，否则会出现重复资产进而导致部分场景资源丢失。如不小心导入了重复的文件，需删除后重新导入。
## 修改场景列表
打开 `Build Settings` （ 或 `Build Profiles` ），
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_4.png)
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_6.png)
将 Unity 工程中的示例场景添加到 `Build Settings` 或 `Build Profiles` 的 `Scene List` 中，并将示例启动器的场景（`AllSamplesLauncher`）移动到所有场景中的第一个。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_7.png)
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_8.png)
> **小心**
注意不要这些添加头显的场景，否则可能会打包失败：
* Combination\_BasedOn\_AppleVisionPro.rst
* Combination\_BasedOn\_Xreal.rst
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_14.png)
## 填写许可证（License Key）
从 Unity 菜单中选择 `EasyAR` > `Sense` > `Configuration` 调出 EasyAR Sense 设置界面。
![FillInKey](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
在 `EasyAR Sense License` 下的输入框中填入 EasyAR Sense License。
![FillInKey2](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill-in-key2.png)
> **提示**
EasyAR Sense License 可以从 EasyAR 开发中心（[中文](https://portal.easyar.cn/sdk/list)，[英文](https://portal.easyar.cn/sdk/list)） 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `是`，名称随意填写
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
> **注意**
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
## 编辑器中运行
在编辑器中运行需要您的电脑上连接一个摄像头。
### 确认系统相机正常
打开 `系统相机应用`：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/camera-windows-open.png)
确认相机可以正常使用：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/camera-windows.png)
最后注意关闭相机应用，避免运行示例时发生冲突。
> **注意**
EasyAR 仅使用系统提供的接口打开相机，需确保 `系统相机应用` 可以打开相机并正常显示。
### 运行示例
>
> 以下内容以图像跟踪示例
`> ImageTracking_Targets
`> 为例，其他示例运行方式类似。
>
打开示例启动器场景，并点击 Unity 编辑器顶部的 `Play` 按钮。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-editor.png)
进入 `ImageTracking\_Targets` 场景。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-editor-select.png)
> **提示**
也可以直接打开 `ImageTracking\_Targets` 场景并执行。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-editor.png)
将摄像头对准以下识别图：
>
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
> 下载地址
> ：🔗
[> namecard
](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
EasyAR 会识别跟踪这张图，并叠加虚拟物体。
> **注意**
部分功能无法在编辑器中连接摄像头运行，但可以在手机上运行。无法在编辑器中使用的示例在运行时会有启动失败的弹窗。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_15.png)
同时会有消息提示和错误log输出。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_13.png)
## 手机上运行
在手机上运行需要进行打包，打包前需要修改 Player 配置。
### 修改 Player 配置
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击安卓图标，调出 Android 平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
* 修改 Package Name 为 License Key 页面显示的 Package Name
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Package Name 是 `com.mycompany.myproject`，则必须填写这里 Package Name 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 Minimum API Level 为 `API Level 21` 或更高版本
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* 修改 Scripting Backend 为 `IL2CPP`，并在 `Target Architecture` 中勾选 `ARM64`
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-64bit.png)
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
* 修改 Bundle ID 为 License Key 页面显示的 Bundle ID
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Bundle ID 是 `com.mycompany.myproject`，则必须填写这里 Bundle ID 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 `Architecture` 为 `ARM64`
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* 添加 `Camera Usage Description`，字符串内容可以随意填写，但必须添加。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-camera-permission.png)
### 打包应用
选择 `File` > `Build Settings`，选择目标平台 (Android/iOS)，然后选择 `switch platform`。
![switchplatform](https://doc-asset.easyar.com/develop/unity/getting-started/media/switch-platform.png)
选择 `Build` 或 `Build And Run` 编译项目并在手机上安装，运行时需允许相应权限。
![buildandrun](https://doc-asset.easyar.com/develop/unity/getting-started/media/build-and-run.png)
### 运行示例
>
> 以下内容以图像跟踪示例
`> ImageTracking_Targets
`> 为例，其他示例运行方式类似。
>
运行后启动的应是示例启动器场景。
> **提示**
如果打开后没有进入示例启动器场景，需要检查是否正确设置了 `Build Settings` 或 `Build Profiles` 的场景列表，将 `AllSamplesLauncher` 移动到第一个。
进入 `ImageTracking\_Targets` 场景。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-phone-select.png)
将手机摄像头对准以下识别图：
>
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
> 下载地址
> ：🔗
[> namecard
](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
EasyAR 会识别跟踪这张图，并叠加虚拟物体。
## 后续步骤
您已经成功运行 Unity AR 示例，可能对示例所展示的 AR 场景是如何创建的感兴趣。可以按顺序阅读以下入门指南：
* [启用 EasyAR](enable-easyar.html)
* [配置 AR 场景](scene.html)
* [场景中的诊断信息](diagnostics.html)
关于示例启动器可以参考详细的使用说明：
* [示例启动器使用说明](sample-launcher.html)
如果您希望了解完整的工程配置，可以参考以下内容：
* [使用 Universal Render Pipeline（URP）](universal-render-pipeline.html)
* [Player 配置](../fundamentals/setup-player.html)
* [EasyAR 配置](../fundamentals/setup-easyar.html)
如果您希望进一步了解 EasyAR 的使用方法，可以从这里开始：
* [AR 驱动的 Unity 应用基础](../fundamentals/intro.html)

---

## 使用 AllSamplesLauncher 快速体验 EasyAR 样例
- 章节路径: `unity/getting-started/sample-launcher.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/sample-launcher.html

# 使用 AllSamplesLauncher 快速体验 EasyAR 样例
AllSamplesLauncher 是一个集成化的示例启动器，可以帮助您快速熟悉 EasyAR SDK 的各项功能。通过该启动器，您可以在单个 Unity 工程中一键切换并运行所有官方示例场景，无需手动配置多个独立项目。
## 准备工作
在开始之前，请确保您已经完成了以下准备工作：
1. 已安装 Unity Hub 和 Unity 编辑器
2. 创建一个新的 Unity 工程
3. 已导入 EasyAR Sense Unity Plugin 并且导入了所有 Samples
请参考 [快速入门](quickstart.html) 中的介绍按步骤进行操作。
## 详细步骤
1. 打开 Samples 中的所有场景。
![All Sample Scenes](https://doc-asset.easyar.com/develop/unity/getting-started/media/all-sample-scenes.png)
2. 点击菜单栏 `File` > `Build Settings` 或 `Build Profiles` > `Scene List` 。
3. 将所有场景都拖动到 `Scene List` 中。
4. 确保 AllSamplesLauncher 位于所有场景中的第一个。如不是，可以在窗口内拖动。
![Scene List Order](https://doc-asset.easyar.com/develop/unity/getting-started/media/scene-list-order.png)
5. 点击菜单栏 `File` > `Build And Run` 进行打包、运行。
> **注意**
打包到手机运行时，不要添加头显类的场景：
* Combination\_BasedOn\_AppleVisionPro
* Combination\_BasedOn\_Xreal
![Donot Load Headset](https://doc-asset.easyar.com/develop/unity/getting-started/media/donot-load-headset.png)
## 打包中遇到问题
在您编译、打包过程中，可能遇到一些错误。常见的问题有：
|错误信息|原因|解决办法|
|*FileNotFoundException:EasyAR Settings Asset*|未填写 License|点击菜单栏 `EasyAR` > `Sense` > `Configuration`，在 **EasyAR Sense License** 中填入您的 License Key|
|*Missing Prefab Asset: 'XR Interaction Setup'*|头显相关文件缺失|打包场景列表中删除头显相关场景。如果您确认需要打包头显，请按照 [使用头显样例](../headsets/samples.html) 中的步骤进行|
## 启动器使用
运行后，您将看到一个简洁的启动器界面。
![Lanucher Homepage](https://doc-asset.easyar.com/develop/unity/getting-started/media/lanucher-homepage.png)
点击界面底部中间的 `Samples` 按钮，即可进入所有功能的样例。
![Lanucher Samplepage](https://doc-asset.easyar.com/develop/unity/getting-started/media/lanucher-samplepage.png)
在界面左侧是功能分类，右侧则是每个功能下的场景样例列表。点击不同的样例场景，即可体验 EasyAR 提供的所有不同功能。
同时，在界面的底部还提供了 `EasyAR Sense` 和 `EasyAR Mega` 的功能演示视频，可以帮助您更好的理解 EasyAR 能为您提供怎样的功能和效果。
## 运行样例前的必读事项
在运行特定样例之前，您**必须**完成以下关键配置，否则样例将无法正常工作：
1. **设置您的 API Key**
* 部分样例（特别是涉及云识别、Mega 云定位等）需要有效的 API Key。
* 在菜单栏 `EasyAR` > `Sense` > `Configuration` 中，找到对应样例需要填写的地方。
* 从中填入您从 EasyAR 开发者中心申请到的 **App ID**、 **API Key**、 **API Secret**。
![Key Configuration](https://doc-asset.easyar.com/develop/unity/getting-started/media/key-config.png)
* **重要提示**：如果您还没有 API Key，部分本地功能的样例（如图片跟踪）可能仍能运行，但云功能会失败。请务必前往 [EasyAR 开发者中心](https://www.easyar.cn/view/login.html) 创建应用并获取 Key。
* **配置 XR/平台支持**：
* 如果您运行的是 **头显相关** 的样例，您参照 [使用头显样例](../headsets/samples.html) 中的进行。
* 请确保您的设备（如手机或头显）已正确连接并处于开发者模式。
## 深入探索样例
示例启动器是您学习的最佳起点。我们强烈建议您：
* **先运行，再研究**：通过启动器快速体验每个样例的效果，对 EasyAR 的能力建立直观印象。
* **打开场景源文件**：每个样例都是一个独立的 Unity 场景文件，位于 `Assets/Samples/EasyAR Sense Unity Plugin/[版本号]/\_\_All Samples\_\_/[功能名称]/[样例名称]/Scenes` 目录下。
* **研究并阅读脚本代码**：在样例场景中，可以打开样例附带的 `\*.cs` 脚本，查看我们是如何调用 EasyAR API 来实现特定功能的。这是学习 API 使用方法的最佳途径。
通过示例启动器，您可以快速建立对 EasyAR SDK 的功能认知。祝您探索愉快！

---

## 配置 AR 场景
- 章节路径: `unity/getting-started/scene.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/scene.html

# 配置 AR 场景
本文以图像跟踪为例，介绍如何配置一个最简单的 AR 场景。
## 开始之前
* 按 [启用 EasyAR](enable-easyar.html) 的内容导入 EasyAR Sense Unity 插件并填写许可证（License Key）。
> **注意**
如果您的工程使用了 URP (Universal Render Pipeline) ，还需要额外 [配置 URP](universal-render-pipeline.html) 。
## 添加 AR Session
在 `Hierarchy` 视图中，在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `AR Session (Image Tracking Preset)` 创建一个用于图像跟踪的 session。
![PresetImageTracking](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation.png)
## 配置摄像机
选中 `Main Camera`, 在 `Inspector` 设置以下参数。
* 设置 `Clear Flags` 为 `Solid Color`。
* 设置 `Background` 为黑色。
* 设置 `Clipping Planes` 的 `Near` 为 0.1（米），`Far` 为 1000（米）。
![mainCameraSetting](https://doc-asset.easyar.com/develop/unity/getting-started/media/main_camera_setting.png)
## 添加 Target
在 `Hierarchy` 视图中，在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Target : Image Target` 添加一个 Image Target，默认显示为问号图标。
![createimagetarget](https://doc-asset.easyar.com/develop/unity/getting-started/media/create_image_target.png)
选中需要跟踪的图像，设置以下参数，并点击 `Apply` 按钮应用设置：
* 设置 `Texture Type` 为 `Editor GUI and Legacy GUI`。
* Advanced 中启用 `Read/Write`。
* `Format` 设置为 `RGB 24 bit`。
![createimagetarget](https://doc-asset.easyar.com/develop/unity/getting-started/media/target-image.png)
配置 `ImageTargetController`：
* 设置 **Source Type**: 为 `Texture 2D`。
* 设置 **Texture** 为配置好的图片。
* 设置 **Name** 为 namecard。
* 设置 **Scale** 为 0.09（表示 0.09 米）。
* 设置 **Tracker** 为 ARSession 下的 `ImageTrackerFrameFilter`。
![addimagetargetcontroler](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_target_controller.png)
> **提示**
Source Type 不同时，部分配置内容会有所不同。
## 添加跟随 Target 的 3D 内容
在 Image Target 节点下添加的 3D 内容相对图片的位置保持不变，即图片移动之后，虚拟内容跟随显示。
在 `Hierarchy` 视图中，选中 `Image Target`，通过菜单 `3D Object` > `Cube` 添加一个 Cube。
![add3D-1](https://doc-asset.easyar.com/develop/unity/getting-started/media/add_3D_1.png)
选中刚才添加的 Cube，配置其属性：
* 设置 Transform 的 `Scale` 为 {0.5, 0.3, 0.3}。
* 设置 Transform 的 `Position` 的 `z` 值为 -0.15 （使 Cube 底面与识别图对齐）。
![add3D-2](https://doc-asset.easyar.com/develop/unity/getting-started/media/add_3D_2.png)
到这里，一个最简单的 AR 场景就配置完成了。运行场景并对准图片，即可看到 Cube 出现在图片上方。
## 后续步骤
* 运行中会注意到屏幕上会显示黄色文字，可以阅读 [场景中的诊断信息](diagnostics.html) 了解这些信息的含义以及常用配置方法。
## 相关主题
* 了解 [AR Session](../fundamentals/session.html)
* 了解 [AR 场景中的 Camera](../fundamentals/camera.html)
* 了解 [Target](../fundamentals/target.html)

---

## 配置 Universal Render Pipeline（URP）
- 章节路径: `unity/getting-started/universal-render-pipeline.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/universal-render-pipeline.html

# 配置 Universal Render Pipeline（URP）
这篇文档介绍了 Universal Render Pipeline（URP） 工程接入 EasyAR 功能时如何配置。
## 开始之前
* 了解[在 Unity 中使用 URP 的方法](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest?subfolder=/manual/InstallingAndConfiguringURP.html)。
* 参考[在 Unity 中启用 EasyAR](enable-easyar.html) 导入 EasyAR Unity 插件。
## 创建 Universal Render Pipeline 资产
> **注意**
如果 Unity 项目使用 URP 项目模板创建，或项目中已经存在 UniversalRenderPipelineAsset 和 Universal Renderer，可以直接跳到[确认项目已切换至 URP 渲染管线](#unity-gettingstarted-universal-render-pipeline-switch)。
在 **Project** 窗口通过右键菜单 **Create** > **Rendering** > **URP Asset(with Universal Renderer)** 创建所需资产：
![Unity6.2_URP_Create_Asset](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline06.png)
## 找到目标平台所使用的 Universal Render Pipeline 资产
1. 点击菜单栏 **Edit** > **Project Settings** > **Graphics**。
顶部的 **Default Render Pipeline** 槽位应当已分配了一个 `Universal Render Pipeline Asset`。
![Unity6.2_URP_Graphics](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline01.png)
> **提示**
该选项在旧版 Unity 中的名称为 **Scriptable Render Pipeline Settings**。
2. 点击菜单栏 **Project Settings** > **Quality**。
选择目标平台的质量级别，下方的 **Render Pipeline Asset** 即目标平台使用的 Universal Render Pipeline 资产。若为空，则目标平台使用的 Universal Render Pipeline 资产为 **Graphics** 窗口中配置的资产。
![Unity6.2_URP_Quality](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline02.png)
> **提示**
若 **Quality** 中的设置与 **Graphics** 不一致，系统将优先使用 **Quality** 中的 Asset。
## 配置 Universal Render Pipeline 资产
> **重要事项**
Unity 编辑器与 Android/iOS 等设备上使用的 Universal Render Pipeline 资产往往是不同的，在编辑器上使用和在设备上使用需要分别配置。
1. 选择目标平台使用的 `Universal Render Pipeline Asset`，然后选择它所使用的 `Universal Renderer Data`。
![Unity6.2_URP_Renderer](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline03.png)
> **提示**
如果项目中配置了多个 Renderer，确保选择的是 **AR 相机正在使用** 的那个渲染器。您可以在场景相机的 **Camera** 组件 > **Rendering** > **Renderer** 选项中确认当前的索引值。
2. 在 `Universal Renderer Data` 的 **Inspector** 面板下方点击 **Add Renderer Feature**，添加 [EasyARCameraImageRendererFeature](../../../api/unity/easyar.EasyARCameraImageRendererFeature.html)。
![Unity6.2_URP_Renderer_Add_Feature](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline04.png)
## 使用 EasyAR 示例的注意事项
EasyAR Unity 插件自带的示例场景默认使用 `Built-in` 渲染管线的材质和着色器。Unity 会自动将这些材质和着色器转换为 URP 兼容的版本，但有少部分资源可能会渲染异常，需要参考 [Convert assets using the Render Pipeline Converter](https://docs.unity3d.com/Documentation/Manual/urp/features/rp-converter.html) 手动转换。
![非 URP 渲染异常](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline08.png)
点击菜单 **Window** > **Rendering** > **Render Pipeline Converter**，选择 **Built-in to URP** 打开转换窗口。勾选 **Material Upgrade** 和 **Readonly Material Converter** > 点击下方的 **Convert Assets**。
![Render Pipeline Converter](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline09.png)
转换完成后，示例材质显示将恢复正常。
## 常见问题
若配置不正确，运行时将没有相机画面，常常为显示为黑屏，但是在跟踪上目标时，添加在跟踪目标下的内容会正常显示。
在 4000 及以上版本中，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，这时画面或日志中会显示 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 为 `URP RenderPipeLineAsset not properly setup`：
![Session_Broken_Caused_By_URP](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline07.png)
解决该问题需按本文描述正确配置 `Universal Render Pipeline Asset`。
## 相关主题
* [Unity 兼容性](../fundamentals/unity-compatibility.html)

---

## 在 EasyAR 项目中启用头显支持
- 章节路径: `unity/headsets/enable-headset.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/enable-headset.html

# 在 EasyAR 项目中启用头显支持
本文档介绍了如何在一个已有的 EasyAR Unity 场景中启用头显支持。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
* 阅读 [Unity 中的 EasyAR 头显支持](headsets.html) 了解在 Unity 中 EasyAR 头显支持的整体架构。
本文假设您有一个已经可以使用 EasyAR 的场景。如果需要创建这样的场景，或是在一个头显场景中添加 EasyAR 组件，可以参考以下文档：
* [添加 AR Session](../fundamentals/session-creation.html)
* [配置 Camera](../fundamentals/camera-configs.html)
* [添加 XR Origin](../fundamentals/origin-creation.html)
## 在场景中添加头显组件
在场景中添加头显组件之前，通常需要移除现有的 Camera 和 XR Origin。
### 移除 Camera 和 XR Origin
删除场景中现有的 Camera。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/del-camera.png)
如果场景里已经存在 `XR Origin`，无论它来自 EasyAR 还是 Unity XR 框架，大部分情况下需要将其删除。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/del-origin.png)
> **提示**
在一些高级的用法中，可以根据自己需要判断是否删除。
### 添加头显组件
遵循头显官方说明来添加头显的组件。这里以 Pico 头显为例，与官方说明冲突时以官方说明为准。
使用菜单添加一个 `XR Interaction Manager`：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-add-manager.png)
使用菜单添加一个 `XR Origin`：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-add-origin.png)
在运行之前，需要确保阅读头显官方说明来了解一个有头显 SDK 的场景应该如何进行配置和运行。
## 配置 frame source
### 内置支持的设备
选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Head Mounted Display (Built-in)` > `Frame Source : [Name] (keep it only)` 创建 [Name] 的 frame source 并仅保留它。
比如，为 Apple Vision Pro 配置 frame source：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/visionpro-frame-source-add.png)
操作之后 session 中的 frame source 会变成这样：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/visionpro-frame-source.png)
> **提示**
如果 session 中包含设备对应的 frame srouce 并且在设备上是第一个可用的 frame source（比如上图中，在 visionOS 系统中 VisionOS ARKit 就是第一个可用的 frame source），可以不修改。部分菜单创建的默认 session 就属于这种情况。
### 扩展支持的设备
选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Extensions` > `Frame Source : [Name] (keep it only)` 创建 [Name] 的 frame source 并仅保留它。
比如，为 Pico 头显配置 frame source：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-frame-source-add.png)
操作之后 session 中的 frame source 会变成这样：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-frame-source.png)
### 跨设备支持
如果需要场景可以在不同设备上运行，需要保留其它 frame source，并确保在设备当前 frame source 可以被选中。
使用不含 `(keep it only)` 的菜单项可以只添加 frame source 且不删除其它 frame source，比如 `EasyAR Sense` > `Extensions` > `Frame Source : Pico` 将在 session 所有 frame source 最后创建适用于 Pico 的 frame source。一般来说，通过这个方式添加完 frame source 之后，还需要将它移动到合适的位置。
> **提示**
在一些高级的用法中，可以根据自己需要调整 frame source 的位置，也可以在代码中修改。
## 后续步骤
* [Vision Pro 工程配置](setup-visionpro.html)
* [XREAL 工程配置](setup-xreal.html)
* [其它 Android 设备工程配置](../fundamentals/setup-player.html)
## 相关主题
* [帧数据源及运行时选取](../cameras/frame-source.html)

---

## 运行验证（bring-up）头显扩展
- 章节路径: `unity/headsets/extension-bring-up.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-bring-up.html

# 运行验证（bring-up）头显扩展
为使 EasyAR 在设备上工作，最重要的工作同时也是最棘手的部分是确保输入数据正确性。在一个新设备上首次运行 EasyAR 时，超过 90% 的问题都是由错误的数据造成的。
如果可能，建议在没有 EasyAR 存在的时候，仅通过设备及设备接口使用一些测试方法来直接验证数据的正确性。本文会介绍一些使用 EasyAR 功能来验证数据的经验方法，这个过程能帮助理解 [外部输入帧数据](../cameras/external-input-frame.html)，但由于 EasyAR 自身也存在误差，使用这个耦合在一起的系统验证数据正确性并不是最佳选择。
## 开始之前
* 完成 [让头显支持 EasyAR](extension-imp.html) 开发。
* 阅读 [快速入门](../getting-started/quickstart.html) 了解如何使用 EasyAR Sense Unity Plugin。
* 了解如何 [使用头显样例](samples.html)。
* 了解 [Android 工程配置](../fundamentals/setup-player.html)。
## 运行基础功能示例
第一次在设备上运行验证 EasyAR 时，需要确保顺序运行这些功能，尤其是不要急于运行 Mega，因为 Mega 有一些容错性，在短时间运行或单一现实场景中运行的时候难以发觉问题。
1. 观察眼前显示的 session 信息，确保没有意外情况发生，并确保 frame count 在持续增长。
2. 运行 `Image` ，即 [图像跟踪](../../image-tracking/intro.html) 功能，与手机运行效果对比一致（建议以 iPhone 为标准）。关注跟踪状态和目标覆盖显示。
在未开启运动融合时，图像跟踪的效果会有明显延迟感，这是符合预期的。运动过程正确、设备停下来的时候位置能对齐即可。
3. 运行 `Dense` ，即 [稠密空间地图](../../dense-spatial-mapping/intro.html) 功能，与手机运行效果对比一致（建议以 iPhone 为标准）。关注网格位置、生成速度和质量。
如果输入数据帧率较低，网格生成速度会变慢，但质量不会明显变差。
该功能无法在部分 Android 设备上运行，网格质量也会根据设备而变化。
> **重要事项**
头显扩展包所使用的输入扩展是一个 [自定义相机](../../cameras/custom-camera.html) 实现。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
如果 `Image` 以及 `Dense` 都和手机上的效果表现一致或更好，那么大部分 EasyAR 的功能就都可以在设备上正常工作，可以开始测试 Mega 了。
## 解决运行中的异常情况：问题分解
如果无法重现与手机上相同的结果，那接下来是一个详细的问题分解过程，可以参考它来寻找根因。建议始终关注系统日志输出。
### 步骤零：理解头显自身系统误差
还记得 [为 AR/MR 准备设备](extension-imp.html) 中所描述的运动跟踪和显示需求吗？
> **重要事项**
运动跟踪/VIO 误差会始终以不同方式影响 EasyAR 算法的稳定性。
> **重要事项**
显示系统误差可能会导致虚拟物体和现实物体无法完美对齐。
在一些误差比较大的情形下，虚拟物体会看起来悬浮于真实物体上面或下面，然后（看起来）一直在漂移。这个现象可以在 Pico 4E 上观察到，即使不使用 EasyAR 只打开它自己的 VST 也有同样的现象。
### 步骤一：查看 session 运行状态
>
[> UI 消息
](../diagnostics/ui-messages.html)> 中的 session 状态显示正常所必须正常的功能或数据：
>
>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 可用性
`>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 虚拟摄像机
`>
>
如果看不到 session 状态信息的显示，需要尝试修改选项为 [Log](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_Log) 然后在系统日志中阅读 session 的状态和正在使用的 frame source 的名字。
可以尝试删除 [ARSession](../../../api/unity/easyar.ARSession.html) 节点下所有其它 frame source，然后查看是否有什么变化。
### 步骤二：确认 EasyAR 接收到的相机帧计数
>
> 必须正常的功能或数据：
>
>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 相机帧数据
`> 在 Unity 代码层的通路（不包含数据正确性以及到原生层的数据通路）
>
>
这个数据应该随时间增长，否则会在几秒之后显示警告信息。
如果发现这个数值不增长，应该最先解决。
### 步骤三：在设备上录制 EIF，然后在 Unity 编辑器中回放
>
> 必须正常的功能或数据：
>
>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 相机帧数据
`> 输入原生层的通路（不包含数据正确性）
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> timestamp
`> （不包括时间点和数据同步）
>
>
点击 `EIF` 来启动录制，再次点击停止。
> **提示**
必须正常停止录制才能获取到可随机索引的 EIF 文件。
在 Unity 编辑器中运行 EIF 数据时最好使用纯净的 EasyAR 场景或使用 EasyAR 的示例以避免场景中存在不正确的配置。
可以在 Unity 编辑器中看到 `相机帧数据` 的回放。图像数据并不是字节相等的，整个流程中存在有损编解码。
EasyAR 会在计算中使用畸变参数但显示时不会对图像做反畸变。所以如果输入了这些数据，当在 Unity 中回放 EIF 文件时，会观察到没有反畸变的数据，这是符合预期的。
> **提示**
修改 Unity game 窗口的比例与输入相同，否则数据会被裁剪显示。
如果数据播放偏快或偏慢，需要检查 `timestamp` 输入。
> **注意**
使用 EIF 可以做很多事情，可以在 Unity 编辑器中使用 EIF 运行 [图像跟踪](../../image-tracking/intro.html) 和 [稠密空间地图](../../dense-spatial-mapping/intro.html) 。注意在设备上运行时显示效果有可能是不一样的。
### 步骤四：使用 EIF 运行图像跟踪
>
> 必须正常的功能或数据：
>
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> intrinsics
`> （数据正确性不能完全保证，因为算法对误差存在容忍度）
>
>
在 Unity 编辑器中使用 EIF 运行图像跟踪示例 ImageTracking\_Targets，需要录制一个图像可以被跟踪到的 EIF。
> **注意**
[图像跟踪](../../image-tracking/intro.html) 需要跟踪目标占据整个图像的一定比例，如果无法跟踪到图像，尝试移动头到更加接近图像的位置。
如果跟踪持续失败或虚拟物体显示在图像中远离目标的位置，则很有可能 `intrinsics` 存在问题。
如果图像数据有畸变，可能会看到虚拟物体不会完美的覆盖图像上的跟踪目标，这是符合预期的。当跟踪目标处于图像边缘时这个现象会更加明显。
### 步骤五：在设备上运行图像跟踪
>
> 必须正常的功能或数据：
>
>
> 设备自身的显示系统
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> intrinsics
`> （数据正确性不能完全保证，因为算法对误差存在容忍度）
>
* `> 相机帧数据
`> 中的
`> extrinsics
`>
* `> 相机帧数据
`> 和
`> 渲染帧数据
`> 中
`> device pose
`> 的坐标一致性
>
* `> 相机帧数据
`> 和
`> 渲染帧数据
`> 中
`> device pose
`> 的时间差
>
>
> **注意**
[图像跟踪](../../image-tracking/intro.html) 需要跟踪目标占据整个图像的一定比例，如果无法跟踪到图像，尝试移动头到更加接近图像的位置。
[图像跟踪](../../image-tracking/intro.html) 需要图像横向边长与真实世界中物体的大小一致，在示例中需要跟踪一个横向边长撑满水平摆放的 A4 纸长边的图像，因此不要跟踪显示在电脑屏幕上的图像，除非使用一把尺子并参照尺子将图像横向边长调整到 A4 大小。
如果在使用 EIF 时图像跟踪很完美但在设备上却不同，需要在继续其它测试前解决它。在后续步骤中解决问题要困难得多。
如果虚拟物体悬浮显示在某个远离真实物体的地方，而且即使人不动也是如此，那很有可能 `intrinsics` 或 `extrinsics` 不正确或 `相机帧数据` 和 `渲染帧数据` 中 `device pose` 不在同一个坐标系，或者显示系统产生了这个误差。
如果虚拟物体在移动头部的时候持续移动并且看起来就像是有延迟一样，那有很大可能性 `device pose` 不够健康。这经常发生于几种情况（不能排除有其他问题的可能性），
* `device pose` 与 `raw camera image data` 的数据时间不同步
* `相机帧数据` 和 `渲染帧数据` 中使用了相同的 pose
### 步骤六：使用 EIF 并在设备上运行稠密空间地图
>
> 必须正常的功能或数据：
>
>
> 设备自身的显示系统
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> intrinsics
`> （数据正确性不能完全保证，因为算法对误差存在容忍度）
>
* `> 相机帧数据
`> 中的
`> extrinsics
`>
* `> 相机帧数据
`> 中的
`> device pose
`>
>
如果网格生成速度非常慢和/或地面重建坑坑洼洼，那非常有可能 `device pose` 有问题。也有可能 pose 的坐标系不正确或 pose 的时间点不对。
> **提示**
如果输入数据帧率较低，网格生成速度也会变慢，但质量不会明显变差。这种情况是符合预期的。
通常分辨精确的网格位置不是非常容易，所以在使用 [稠密空间地图](../../dense-spatial-mapping/intro.html) 时显示系统误差不一定能观察出来。
## 运行 Mega 示例
阅读以下内容了解如何在 Unity 中使用 Mega。如果您还没有开通 Mega 服务，需联系 EasyAR 商务获取试用资格。
* [EasyAR Mega 简介](../../mega/intro.html)
* [我的定位库可以使用了吗？](../../mega/localization-verify.html)
* [使用 EasyAR Mega Unity 样例快速入门](../mega/quickstart.html)
然后在设备上运行 `Mega` ，与手机运行效果对比一致（建议以 iPhone 为标准）。关注
* 物体显示位置是否正确
* 远处（10M 及以外）物体显示位置和大小是否正确
* 视线中心以外物体显示位置和大小是否正确
* 转动头部时物体显示位置和大小是否正确
## 解决运行中的异常情况
>
> 必须正常的功能或数据：
>
>
> 设备自身的显示系统
>
* `> 相机帧数据
`> 和
`> 渲染帧数据
`> 中的所有数据
>
>
在完成 [图像跟踪](../../image-tracking/intro.html) 以及 [稠密空间地图](../../dense-spatial-mapping/intro.html) 两个功能的验证后，理论上 EasyAR Mega 应该已经被支持了。如果在头显上运行的表现明显比手机上差，需要关注以下内容，
* 关注 `相机帧数据` 和 `渲染帧数据` 中的 pose 数据和 timestamp
* 关注运动跟踪/VIO 系统输出。`XR Origin` 下面的熊猫会是一个好的参考
另外，还需要重点关注设备自身的显示系统，尤其是远处、视线中心以外以及转动头部时的物体显示效果。这类场景在设备自身测试时经常会被忽略，但通常问题依然是设备自身的显示系统导致的，您需要向 EasyAR 说明这些问题和可能的影响，并为开发者提供合理效果预期。
> **重要事项**
用户使用时会非常关注这些显示问题，而很多设备也确实无法在大空间场景提供非常完美的显示效果。EasyAR 无法解决设备自身的显示问题，这需要设备厂商迭代解决，与此同时，用户也需要理解这些问题。
## 后续步骤
* [发布扩展包](extension-dist.html)
## 相关主题
可以在手机上运行的示例：
* 图像跟踪示例 ImageTracking\_Targets，可以通过它了解 [图像跟踪](../../image-tracking/intro.html) 功能的预期执行效果功能
* 稠密空间地图示例 SpatialMap\_Dense\_BallGame，可以通过它了解 [稠密空间地图](../../dense-spatial-mapping/intro.html) 功能的预期执行效果
* 运动融合示例 ImageTracking\_MotionFusion，可以通过它了解 [运动融合](../../image-tracking/motion-fusion.html) 功能的预期执行效果
* Mega 示例 MegaBlock\_Basic，可以通过它了解 [Mega](../../mega/intro.html) 功能的预期执行效果

---

## 发布扩展包
- 章节路径: `unity/headsets/extension-dist.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-dist.html

# 发布扩展包
本文介绍完成开发和运行验证后，如何将为特定头显开发的 EasyAR Sense Unity Plugin 扩展打包发布，以便用户可以方便地使用该扩展。
## 开始之前
* 完成 [让头显支持 EasyAR](extension-imp.html) 开发。
* 完成 [运行验证（bring-up）](extension-bring-up.html)，确保设备上运行效果正常。
## 完成包定义
包本身的定义在 `package.json` 中，可以根据 [Unity 创建自定义 package 的指南](https://docs.unity3d.com/Manual/CustomPackages.html) 来修改这个文件或创建一个新的包。注意确保修改 package 的 `name` 和 `displayName`，注意不要与 EasyAR 提供的模板本身或其它供应商的扩展发生冲突。
## 重新生成 meta 文件
删除并重新生成 package 中所有文件的 .meta 文件。否则它们会与模板本身或其它供应商的扩展发生冲突。
> **注意**
Unity 可能会缓存 .meta 文件，建议在 Unity 关闭状态下，删除包内所有 .meta 文件，并整个删除 `Library` 目录，然后重新打开 Unity 工程以重新生成 .meta 文件。
注意场景和资源文件中的引用都会变化，有可能需要重新创建或修改场景中的部分物体。文本替换 .unity 以及其它资源文件中的 GUID 是一种可行的方法。
## 检查版本兼容性
检查扩展与设备 SDK 以及 EasyAR Sense Unity Plugin 的版本兼容性。
> **注意**
从版本 4000 开始，EasyAR Sense Unity Plugin 遵循 Unity 所要求的 semantic versioning。在这之前每个小版本都可能会包含不兼容的更改。
## 打包发布
您可能还希望修改 package 中的其它一些文件，确保在发布前仔细审查整个 package。
建议使用 Unity package 来打包文件。如果设备 SDK 并没有准备好以 Unity package 形式发布，也可以选择通过 asset package 来发布。
需要提醒用户，EasyAR license key 的所有限制（尤其是针对自定义相机的限制）都适用于您的扩展包。

---

## 让头显支持 EasyAR
- 章节路径: `unity/headsets/extension-imp.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-imp.html

# 让头显支持 EasyAR
本文介绍如何使用 EasyAR Sense Unity Plugin 的头显扩展包模板来开发一个支持头显设备的 EasyAR 扩展包。
## 开始之前
在进入开发之前，需要先了解如何使用 EasyAR Sense Unity Plugin。
* [快速入门](../getting-started/quickstart.html)
* 运行 [AR Session 示例](../fundamentals/sample-arsession.html)、图像跟踪示例 ImageTracking\_Targets 和稠密空间地图示例 SpatialMap\_Dense\_BallGame，它们的运行效果在手机上和头显上是相似的。
头显插件开发会涉及一些基础功能，需要先了解这些内容：
* 了解 [AR Session](../fundamentals/session.html)
* 了解 [帧数据源](../cameras/frame-source.html) 和 [外部帧数据源](../cameras/external-frame-source.html)
此外，还需要熟悉 [如何开发一个 Unity 的 package](https://docs.unity3d.com/Manual/CustomPackages.html)。
## 为 AR/MR 准备设备
* 准备运动跟踪/VIO 系统
确保设备跟踪误差受控。一些 EasyAR 功能比如 Mega 可以在某种程度上降低设备累积误差，但大的局部误差也会让 EasyAR 的算法变得不稳定。通常来讲，通常我们期望 VIO 漂移在 1‰ 以内。
* 准备显示系统
确保当一个与现实中某个物体大小和轮廓相同的虚拟物体被放置在虚拟世界中，且它与虚拟摄像机的相对变换关系与真实世界中对应物体与设备的变换关系相同时，虚拟物体可以贴合显示在真实物体上，且移动设备或转头不会打破显示效果。可以参考 Vision Pro 的效果。
* 准备设备 SDK
确保已经有 API 可以提供 [外部输入帧数据](../cameras/external-input-frame.html) 。这些数据应该由系统中的两个且只有两个时间点产生，需要确保不会出现数据无法对齐的情况。
## 使用头显扩展包模板
通过 Unity 的 [Package Manager window](https://docs.unity3d.com/Manual/upm-ui.html) 来 [使用本地 tarball 文件安装插件](https://docs.unity3d.com/Manual/upm-ui-tarball.html) 导入 `EasyAR Sense Unity Plugin` （package `com.easyar.sense`）。解压头显扩展模板 （package `com.easyar.sense.ext.hmdtemplate`）到 Unity 工程的 Packages 目录，并重命名 `Samples\~` 文件夹为 `Samples` 。
这时应看到这样的目录结构：
```
.
├── Assets
└── Packages
└── com.easyar.sense.ext.hmdtemplate
├── CHANGELOG.md
├── Documentation\~
├── Editor
├── LICENSE.md
├── package.json
├── Runtime
└── Samples
└── Combination\_BasedOn\_HMD
```
> **提示**
如有需要，可以使用任何 Unity 允许的方式来导入 `EasyAR Sense Unity Plugin` 和存放头显扩展模板。
如果不使用模板，也可以参考 [Unity 创建自定义 package 的指南](https://docs.unity3d.com/Manual/CustomPackages.html) 来创建一个新的 package。
如果设备 SDK 未使用 Unity 的 package 来组织，需要解压头显扩展模板到 Unity 的 Assets 文件夹，然后从解压的文件中删除 package.json 以及任何以 .asmdef 为后缀名的文件。请注意在这种使用方式下，同时使用设备 SDK 与 EasyAR 的用户将无法获得合理的版本依赖。
## 完成运行时输入扩展
遵循 [创建图像和设备运动数据输入扩展](../cameras/external-device-frame-source.html) 方法，修改 `Runtime/HMDTemplateFrameSource.cs` 并完成适用于头显的输入扩展。这是扩展包最主要的开发工作。
## 完成编辑器菜单
修改 `MenuItems` 类中的 "HMD Template" 字符串为代表设备的名称。如果需要其它自定义编辑器功能，也可以添加其它脚本。
开发者在 `Hierarchy` 视图中选中 **AR Session (EasyAR)** 并点击右键时会出现这些菜单项：
* `EasyAR Sense` > `Extensions` > `Frame Source : [Device Name]`：在当前 session 中添加一个该设备的帧数据源。
* `EasyAR Sense` > `Extensions` > `Frame Source : [Device Name (keep it only)]`：在当前 session 中添加并仅保留一个该设备的帧数据源。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-context-menu.png)
## 完成应用示例
示例位于 `Samples/Combination\_BasedOn\_HMD`。简单起见，示例模板中没有代码，全部 AR 功能靠场景内容及配置即可完成。
1. 添加支持设备运行的内容到场景中。
> **提示**
如有需要，也可以反过来做，使用一个可以在设备上运行的场景，然后添加 EasyAR 组件和 sample 场景中的其它物体到场景中。
2. 修改设计用来放在 session 原点下的物体。
如果场景中定义了 session 原点，移动 `EasyARPanda` 和 `UI` 到原点节点下。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-ui.png)
`EasyARPanda` 会提供一个设备运动跟踪行为的参照，这会帮助判断跟踪不稳定时候的原因。
这些物体名称括号内的文字是给扩展开发者看的提示，可以删除：
* `(Move into Origin if there is any)`
* `(Move into Origin if there is any, set constraint source to your rendering camera)`
* 配置 `HUD` 按钮行为。
设置 `UI` 的 constraint source 为虚拟摄像机，以确保 `HUD` 按钮可以按预期工作。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-hud.png)
* 配置 `Canvas` 的 raycast 功能。
修改 `UI` 节点下的 `Canvas`，确保 raycast 可以工作，以保证所有 UI 按钮和开关可以按预期工作。
模板中已经在 `Canvas` 节点下预先添加了 [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/index.html) 的 [Tracked Device Graphic Raycaster](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/tracked-device-graphic-raycaster.html)，导入对应的 package 之后即可看到。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-raycaster.png)
如果在设备上运行时不使用 [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/index.html)，会看到类似下面的缺少脚本提示，可以将其删除，并添加设备所需的 raycaster 组件。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-raycaster-missing.png)
## 后续步骤
* 在进一步完成扩展包之前，需要先 [运行验证（bring-up）](extension-bring-up.html) 输入扩展
* 全部完成之后，可以准备 [发布扩展包](extension-dist.html)
## 相关主题
* [扩展包模板参考](extension-template.html)
* [外部输入帧数据](../cameras/external-input-frame.html)
* [创建图像和设备运动数据输入扩展](../cameras/external-device-frame-source.html)

---

## 头显扩展包模板简介
- 章节路径: `unity/headsets/extension-template.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-template.html

# 头显扩展包模板简介
`com.easyar.sense.ext.hmdtemplate` package 是为头显扩展开发提供的示例和模板。它是一个 SDK 的实现，并且包含了给应用开发者的示例。
## 模板内容
这个 package 的包结构遵循了 [Unity 推荐的文件布局](https://docs.unity3d.com/Manual/cus-layout.html)：
```
.
├── CHANGELOG.md
├── Documentation\~
├── Editor
├── LICENSE.md
├── package.json
├── Runtime
└── Samples\~
└── Combination\_BasedOn\_HMD
```
其中一些比较重要的内容如下：
* **Runtime**：存放运行时平台资产的文件夹。这是模板中最重要的文件夹。
* **Samples\~**：存放 package 中所有示例的文件夹。它包含给下游使用的示例，可以用作测试扩展的 demo。为了原地开发这个示例，需要修改文件夹名为 `Samples` 。使用 [Client.Pack](https://docs.unity3d.com/ScriptReference/PackageManager.Client.Pack.html) 方法会在打包一个新的发布时将其自动重命名为 `Samples\~` 。
* **Editor**：存放编辑时平台资产的文件夹。这个文件夹的脚本主要用于创建菜单项。
* **package.json**：package 的清单文件。
## 模板示例的创建过程
1. [添加 AR Session](../fundamentals/session-creation.html)
在 `Hierarchy` 视图中：
* 在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Mega` > `AR Session (Mega Block Default Preset)` 添加 [ARSession](../../../api/unity/easyar.ARSession.html)。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Frame Filter : Image Tracker` 添加一个 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `SpatialMap` > `Frame Filter : Dense SpatialMap Builder` 添加一个 [DenseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.DenseSpatialMapBuilderFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `SpatialMap` > `Frame Filter : Sparse SpatialMap Builder` 添加一个 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Extensions` > `Frame Source : HMD Template (keep it only)` 添加并仅保留 HMD Template 这一个 [FrameSource](../../../api/unity/easyar.FrameSource.html)。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-session.png)
* 添加 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html)
在 `Hierarchy` 视图中，在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Target : Image Target` 添加一个 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html) 到 session 中。
配置 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html)：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-image-target.png)
在完成上述配置之后，`Scene` 视图中显示的图像是 gizmo。这个示例中通过一个 quad 来显示同一图像的虚拟物体。
添加显示在 target 上面的虚拟物体：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-image-target-content.png)
* 添加一个模型作为运动跟踪原点参考
这个模型对开发者以及下游用户都很重要，它用于解耦设备运动跟踪和 EasyAR 算法。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-origin-content.png)
* 添加功能选择的 UI
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-ui.png)
* 关闭启动时启用的 EasyAR 功能，并通过 UI 开关来打开它们
例如，图像跟踪的功能在启动时可以关闭，只需要设置对应组件的 enable 为 false 即可：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-feature-off.png)
然后添加 UI 开关处理：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-ui-switch.png)
## 相关主题
* [让头显支持 EasyAR](extension-imp.html) 介绍了如何使用这个模板来创建一个新的头显扩展包
* [运行验证（bring-up）](extension-bring-up.html) 介绍了如何利用这个模板提供的示例验证输入扩展的正确性
* [发布扩展包](extension-dist.html) 介绍了如何基于这个模板完成最后的打包分发

---

## EasyAR Unity 头显扩展包
- 章节路径: `unity/headsets/extension.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension.html

# EasyAR Unity 头显扩展包
本文档介绍了 EasyAR Unity 头显扩展包的概念、能力边界以及创建头显扩展包所需的背景知识。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
* 阅读 [Unity 中的 EasyAR 头显支持](headsets.html) 了解在 Unity 中 EasyAR 头显支持的整体架构。
## EasyAR Unity 头显扩展包是什么
EasyAR Unity 头显扩展包是一个 Unity package，包含一系列代码和示例，帮助您在您的头显设备上使用 EasyAR Sense 的功能。通过这个扩展包，您可以将 EasyAR Sense 的大部分功能（如图像跟踪、稠密空间地图等）集成到您的设备上，从而利用 EasyAR 提供的强大 AR 功能。
使用 EasyAR Unity 头显扩展包是 EasyAR 头显支持的其中一种方式。下图展示了 EasyAR 在 Unity 中的整体架构，以及头显扩展包在其中的位置。
```
block
columns 4
block:groupApp:4
block:groupAppWrapper
space
App1["EasyAR + Device A<br>App"]
space
App2["EasyAR<br>App"]
space
App3["EasyAR + Device B<br>App"]
end
end
block:groupSensePluginExtension
columns 1
SensePluginExtension["EasyAR Sense Unity Plugin<br>Extension for Device A"]
space
end
block:groupSensePlugin
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupDeviceAUnity
columns 1
DeviceAUnity["Device A<br>Unity SDK"]
space
end
block:groupSense
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
MDeviceB["Device B<br>CameraDevice"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:4
columns 1
System["Native Library"]
block:groupSystemWrapper
space
DeviceA["Device A<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
space
DeviceB["Device B<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePluginExtension --> App1
SensePlugin --> App1
SensePlugin --> App2
SensePlugin --> App3
ARF --> App3
XRI --> App1
XRI --> App3
groupSense --> SensePlugin
groupDeviceAUnity --> SensePluginExtension
SensePlugin --> SensePluginExtension
DeviceA --> groupDeviceAUnity
DeviceA --> XRSDK
XRSubsystem --> ARF
XRSubsystem --> XRI
DeviceB --> MDeviceB
DeviceB --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style DeviceAUnity fill:none,stroke:none,stroke-width:0px
style Sense fill:none,stroke:none,stroke-width:0px,color
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePluginExtension fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class SensePluginExtension EasyAR
```
图中列出了两种典型的头显支持方式：通过 Unity 头显扩展包对接设备 SDK（Device A），以及在 EasyAR Sense 库中直接对接设备 SDK（Device B）。本文档主要介绍前者。
## 我可以创建自己的头显扩展包吗？
目前，AR/VR/MR/XR 行业内还没有形成非常统一的接口方案，虽然 OpenXR 是个很好的候选，但规范演化和行业实现还需要时间。所以通常来说市贩设备直接运行 EasyAR 并不那么容易，大概率存在数据接口缺失的情况。随着行业的发展，一些新兴设备也可能具备良好的接口支持，比如 2024 年苹果公司开放了 Vision Pro 的相关接口，这些接口已经足够用来支撑 EasyAR 运行，不过使用起来还是需要一些专业知识。
如果您无法做出判断，建议联系硬件制造商或 EasyAR 商务以获取相应的设备支持。
如果您是硬件制造商，并且希望在您的设备上支持 EasyAR 的功能，您可以参考接下来的文档内容来创建一个头显扩展包，从而让 EasyAR 的大部分功能可以在您的设备上运行。本文档在提供数据和接口规范的同时并不限定所有实现细节，任何实现方式或接口定义都可以讨论，欢迎通过商务渠道联系沟通。
本文档覆盖的硬件自身需要有运动跟踪或 SLAM 能力，EasyAR 的功能需要运行在良好的设备跟踪能力之上，通常不建议靠 EasyAR 的功能优化设备的跟踪，这会产生循环依赖进而理论上放大误差并导致整体系统趋于不稳。如果设备本身没有运动跟踪能力，那么支持方案并不在本文档覆盖范围之内，如有需要可通过商务渠道进行沟通。
## 头显扩展包的能力边界
头显扩展包的目标是让 EasyAR Sense 的大部分功能可以在您的设备上运行。为了实现这个目标，您需要了解头显扩展包的能力边界。
### 头显扩展包所包含的内容
您将实现的扩展是：
* 使用 [自定义相机功能](../../cameras/custom-camera.html)，从您的设备 API 抓取数据并发送进 `EasyAR Sense` 的一系列代码。
* 在 Unity 中，头显扩展会使用 [外部帧数据源](../cameras/external-frame-source.html) 和 `EasyAR Sense Unity Plugin` 定义的一套 `EasyAR Sense` 数据流来简化自定义相机开发。
* 在 Unity 中，头显扩展是一个 [Unity package](https://docs.unity3d.com/Manual/Packages.html)，包含运行时脚本，编辑器脚本和扩展的 sample，您或 EasyAR 可以将它分发给下游用户。
> **提示**
如果您不希望将对接细节暴露在外部系统中，可以联系 EasyAR 进行沟通。在 EasyAR Sense 内部使用 C 接口直接对接是可行且有先例的。
您在实现扩展的时候，可能会：
* 修改您 SDK 的**接口设计和内部实现**。
* 与您的**团队**一起讨论确认数据获取和使用方案。
* 花**大量**时间进行数据正确性验证而不是写代码。
完成扩展后，您将会看到：
* 大多数 `EasyAR Sense` 功能在您的设备上可以使用，这些功能会利用您设备的运动跟踪能力。
* `EasyAR Sense` 内支持的 EasyAR 云服务在您的设备上可以使用。
* 只能使用 EasyAR XR license。个人版、专业版以及经典版的 license 无法在您的设备上使用。
* 使用自定义相机时的所有 EasyAR license 的限制以相同方式适用于您的设备。
### 头显扩展包所不包含的内容
这个扩展不能脱离 `EasyAR Sense` 使用：
* 这个头显扩展不会独立运行，作为依赖，`EasyAR Sense` 也是需要的。在 Unity 中则必须使用 `EasyAR Sense Unity Plugin`。
* 它不会直接调用 EasyAR 云服务 API（比如 EasyAR Mega 定位服务），这些调用会在 `EasyAR Sense` 内部完成。
* 在 Unity 中，它不会直接调用 AR 功能（比如图像跟踪）的接口方法，它们在 `EasyAR Sense Unity Plugin` 内部完成。
* 在 Unity 中，它不会修改场景中物体或跟踪目标的 transform，它们在 `EasyAR Sense Unity Plugin` 内部完成。
这个扩展不能脱离您的设备 SDK 使用：
* 在 Unity 中，头显扩展或 `EasyAR Sense Unity Plugin` 不会修改场景中相机的 transform，这必须在您的设备 SDK 或其依赖路径中完成。
通过头显扩展有一些 EasyAR 功能仍是无法使用的：
* 表面跟踪功能将无法使用。
* EasyAR 自身的运动跟踪将无法使用。
* 平面检测（EasyAR 运动跟踪的一部分）将无法使用。
## 如何在我的设备上使用 Mega？
在设备上运行 Mega 是很多用户关心的问题。在 Unity 中，Mega 服务是运行在 `EasyAR Sense` 诸多基础功能之上的一个功能模块，所以只要您的设备完整支持 `EasyAR Sense`，那么 Mega 也会被支持。
一般来说，不建议在一开始就直接在设备上运行 Mega 示例来验证设备对 Mega 的支持情况，因为 Mega 会综合利用所有输入数据，并且其对这些数据的误差容忍度较大。直接运行 Mega 示例很可能会因为数据接口不匹配或数据质量不佳而导致无法获得合理的运行效果，并且无法判断问题出在哪里，这会为日后的调试带来很大困难。
> **重要事项**
Mega 服务对设备的运动跟踪能力有一定要求。如果设备的运动跟踪能力不佳，那么 Mega 的表现也会受到影响。在大范围 AR 场景中，还需要特别关注室内外的表现差异。
> **重要事项**
Mega 一般服务于大空间场景，因此需要格外关注远距离物体以及转动头部或移动时物体的 **显示** 效果。如果设备的显示系统误差较大，那么即使 Mega 本身运行正常，用户也会感觉虚拟物体无法正确贴合现实物体。
## 需要的背景知识和团队配置
创建头显扩展包不是一个简单的任务，需要您和您的团队在多个领域进行深入的工作。通常来说，要完成头显扩展，需要 Unity 开发参与的同时投入 Unity 开发之外的团队人员。由于缺少标准，只在 3D 引擎上面修改通常无法完成头显扩展，建议从第一天起就让系统工程师和 SDK 工程师等底层开发工程师参与进来。
打造 AR/VR 设备需要一些领域知识，相似地，在设备上运行和验证 EasyAR Sense 将需要您或您的团队是如下领域的专家：
* 您设备的物理结构和渲染系统
* 相机系统几何
* SDK 开发
* 常规 Android debug 技能，比如 adb（[中国大陆](https://developer.android.google.cn/tools/adb)，[国际](https://developer.android.com/tools/adb)）
如果您工作在 Unity 上，您还需要知道这些：
* [Unity 开发基础和 package 使用](https://docs.unity3d.com/Manual/Packages.html)
* [Unity package 开发](https://docs.unity3d.com/Manual/CustomPackages.html)
* C# 语言基础，包括 [IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable) 等
另外，有一点在这些领域的知识将帮助您更好地理解系统，尤其是如何发送正确的数据到 EasyAR：
* Android 开发（[中国大陆](https://developer.android.google.cn)，[国际](https://developer.android.com)）
* 几何视觉，尤其是图像匹配和 3D 重建
## 后续步骤
在接下来的文章中，您将了解创建头显扩展包的完整流程：
* [让头显支持 EasyAR](extension-imp.html) 介绍了如何使用模板来创建一个新的头显扩展包，并完成基本的输入扩展开发
* [运行验证（bring-up）](extension-bring-up.html) 介绍了如何在设备上验证输入扩展的正确性
* [发布扩展包](extension-dist.html) 介绍了如何将头显扩展包打包并分发给下游用户
## 相关主题
* [扩展包模板参考](extension-template.html)
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)

---

## Unity 中的 EasyAR 头显支持
- 章节路径: `unity/headsets/headsets.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/headsets.html

# Unity 中的 EasyAR 头显支持
本文档介绍了在 Unity 中 EasyAR 头显支持的整体架构和注意事项。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
## 头显支持概述
EasyAR 在 Unity 中支持头显的方式比较灵活，常见有两种方式：
* 内置支持：通常在 EasyAR Sense 库中直接对接设备 SDK，并在 Unity 中提供对应的接口 （比如 Apple Vision Pro）
* 扩展支持：通过 Unity 头显扩展包对接设备 SDK （比如 Pico）
```
block
columns 4
block:groupApp:4
block:groupAppWrapper
space
App1["EasyAR + Device A<br>App"]
space
App2["EasyAR<br>App"]
space
App3["EasyAR + Device B<br>App"]
end
end
block:groupSensePluginExtension
columns 1
SensePluginExtension["EasyAR Sense Unity Plugin<br>Extension for Device A"]
space
end
block:groupSensePlugin
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupDeviceAUnity
columns 1
DeviceAUnity["Device A<br>Unity SDK"]
space
end
block:groupSense
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
MDeviceB["Device B<br>CameraDevice"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:4
columns 1
System["Native Library"]
block:groupSystemWrapper
space
DeviceA["Device A<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
space
DeviceB["Device B<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePluginExtension --> App1
SensePlugin --> App1
SensePlugin --> App2
SensePlugin --> App3
ARF --> App3
XRI --> App1
XRI --> App3
groupSense --> SensePlugin
groupDeviceAUnity --> SensePluginExtension
SensePlugin --> SensePluginExtension
DeviceA --> groupDeviceAUnity
DeviceA --> XRSDK
XRSubsystem --> ARF
XRSubsystem --> XRI
DeviceB --> MDeviceB
DeviceB --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style DeviceAUnity fill:none,stroke:none,stroke-width:0px,color:#fff
style Sense fill:none,stroke:none,stroke-width:0px,color:#fff
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px,color
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePluginExtension fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class groupSense EasyAR
class SensePlugin EasyAR
class SensePluginExtension EasyAR
classDef Device fill:#636,stroke:#333,color:#fff
class groupDeviceAUnity Device
class DeviceB Device
class DeviceA Device
```
>
> 图中：
>
>
> 设备 A 属于扩展支持
>
> 实践中设备 A 通常会有对应的 Unity SDK，用于对接 Unity XR SDK 或者独立实现头显渲染能力。
>
> 设备 A 的头显扩展包负责将 EasyAR Sense Unity Plugin 和设备 A 的 Unity SDK 对接起来，从而实现 EasyAR 在设备 A 上的运行。这个支持包可能由 EasyAR 提供，也可能由设备厂商提供。
>
>
> 设备 B 属于内置支持
>
> 实践中设备 B 可能有也可能没有对应的 Unity SDK，取决于设备厂商的实现。比如 Apple Vision Pro 没有对应的 Unity SDK，XREAL 有对应的 Unity SDK。
>
>
>
内置支持和扩展支持的头显都支持使用了 [自定义相机](../../cameras/custom-camera.html)。
> **重要事项**
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
在 Unity 中，虚拟摄像机的渲染、投影矩阵 和 transform 等不受 EasyAR 控制，它们通常由设备 SDK 或 Unity XR SDK 控制。设备自身的功能，比如手势识别、眼动追踪等，仍然由设备及设备 SDK 提供。在使用时，通常需要同时使用 EasyAR 和设备 SDK。
## 后续步骤
* [使用头显样例](samples.html)
* [启用头显支持](enable-headset.html)
* 工程配置
* [Vision Pro 工程配置](setup-visionpro.html)
* [XREAL 工程配置](setup-xreal.html)
* [其它 Android 设备工程配置](../fundamentals/setup-player.html)
* [创建 EasyAR 头显扩展包](extension-imp.html)

---

## 在 XR 头显或眼镜上使用 EasyAR 样例
- 章节路径: `unity/headsets/samples.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/samples.html

# 在 XR 头显或眼镜上使用 EasyAR 样例
EasyAR 对所有头显提供统一的样例，样例中没有任何代码，全部由场景中配置实现。功能本身的使用可以参考相关功能在 Android/iOS 手机上样例实现。
头显样例名称为 `Combination\_BasedOn\_\*` , 比如 Pico 的样例为 `Combination\_BasedOn\_Pico`。 该样例在一个场景中演示了大部分 EasyAR 功能，它们可以动态开关，可以单独使用，也可以同时打开。
## 准备工作
* 确定您的头显或眼镜当前在 EasyAR [支持列表](../../headsets/headsets.html)
* 下载并导入 [EasyAR Unity 插件包](https://www.easyar.cn/view/download.html)
* 下载并导入 [EasyAR Unity XR设备扩展包](https://www.easyar.cn/view/download.html)
* 获取适合 XR 头显或者眼镜的 EasyAR 许可证，头显或眼镜可用 License 类型包括
* EasyAR Sense 4.x **XR License** 试用版（试用，在 EasyAR 网站自主开通）
* EasyAR Sense 4.x **XR License** 正式版（付费后使用，请联系商务购买开通）
* EasyAR Sense 4.x **XR License** 企业版（企业版 SDK 使用）
> **小心**
头显和眼镜上**仅允许使用 XR License**，普通 License 无法使用 EasyAR 功能。
## 导入官方样例
1. 内建支持的设备的样例位于 EasyAR Unity 插件包中，根据设备单独导入需要的样例。
![xr-samples-location](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-samples-location.png)
2. 通过扩展支持的设备样例随对应的头显扩展一起分发。可以使用 Unity 将样例导入工程中。以Pico为例。
![xr-pico-extension](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-pico-extension.png)
## 样例打包并运行
分别完成头显工程配置和样例使用说明。
* 严格参照对应头显官方的文档和说明做好对应的配置，EasyAR 文档中不会覆盖相关内容。
* 按照 EasyAR 文档中各平台说明进行配置。
Android: 请参考 [Android 工程配置](../fundamentals/setup-player.html)
visionOS: 请参考 [visionOS 工程配置](setup-visionpro.html)
XREAL 除了按照 Android 平台设置外，额外需要 [XREAL 工程配置](setup-xreal.html)
* 样例打包
在 Unity 里打包样例使用，并部署到设备上运行。具体方法参见 [Unity上运行样例](../getting-started/quickstart.html)。
## 用法说明
样例内置多个按钮，其具体功能如下。
![xr-sample-usage-7](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-sample-usage-7.png)
* 按钮1 `HUD`：切换UI显示模式，初始状态UI会固定在现实世界中，打开HUD之后UI会始终显示在眼前。
* 按钮2 `Record`：开关EIF录制。打开之后必须关闭才能录制正常的EIF文件，否则录出来的文件将无法使用。
* 按钮3 `Image`：开关图像跟踪。
* 按钮4 `Image Fusion`：开关图像跟踪+运动融合模式。
* 按钮5 `Dense`：开关稠密空间建图。
* 按钮6 `Sparse`：开关稀疏空间建图。
* 按钮7 `Mega`：开关 Mega。
## 功能详解
* 默认功能开关
所有功能启动时默认都是**关闭**的，这是通过在编辑器上将对应脚本停用实现的，按钮操作操作的是对应脚本的启用/停用，可以根据实际要运行的样例设置默认启用的功能。
![hmd-default-disable](https://doc-asset.easyar.com/develop/unity/headsets/media/hmddefault-all.png)
* 坐标系原点参照
样例中在[运动跟踪](../../motion-tracking/intro.html)的坐标系原点都放置了一个静止的熊猫模型，用于检查运动跟踪状态。这个模型对于解耦问题是有帮助的，比如在运行 Mega 的时候，有些快速漂移就是设备运动跟踪（即设备自身缺陷）导致的，这时候这个模型也会跟着一起漂移/可以根据需要，调整或删除这个熊猫模型。
* 使用内嵌图像跟踪的识别图
* 样例中预设了平面图像跟踪使用的图像的大小，您需要使用 A4 纸打印 namecard.jpg，必须保持图像的比例不拉伸，不裁剪，尽量充满纸张（下图）。
![namecard](https://doc-asset.easyar.com/develop/unity/headsets/media/namecard.jpg)
* 测量打印完成纸张上名片图案的长度，根据测量的结果，需将 Unity 场景中 `Image Target` 的 `Scale` 设为**与真实物理大小一致**（单位是米）。
![set-the-actual-size](https://doc-asset.easyar.com/develop/unity/headsets/media/set-the-actual-size.png)
* 在 `EasyAR 运动融合` 打开时，只能跟踪固定位置（不能移动）的图像。如果运动融合关闭，图像超出视野的时候就无法跟踪。
* 有时候眼镜视角不能很好的反应相机图像大小，如果识别不到可以尝试让眼镜相机靠近图像。实际使用时建议跟踪更大的图像，比如 5米\*5米 大小。
> **注意**
在头显上无论 EasyAR 运动融合功能是开是关，`image target` 的 `Scale` 参数都必须设置为真实的物理大小，否则显示位置会是错误的。
* Mega 配置
如果你在使用 EasyAR Mega，你需要参考 [Mega Unity 快速入门](../mega/quickstart.html)。

---

## 如何在 Apple Vision Pro 上使用 EasyAR 能力
- 章节路径: `unity/headsets/setup-visionpro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/setup-visionpro.html

# 如何在 Apple Vision Pro 上使用 EasyAR 能力
本指南将引导您完成 Unity 与 Xcode 的工程配置，为 Apple Vision Pro 应用解锁包括 Mega 云定位在内的全部 EasyAR 核心能力。
## 开始之前
* 学习如何使用[头显样例](samples.html)
* 确保开发环境符合以下要求：
* visionOS 2.0 及以上
* 对应 visionOS 版本的 Xcode 16.0 及以上并安装 visionOS simulator
* 推荐的 Unity 版本 6000.0.23 以上的 LTS 版本
## 向 Apple Inc. 申请企业级 API 许可
由于在 Apple Vision Pro 上获取相机画面及参数是一个需要 **entitlement** 的 **企业级 API**，您需要向 **Apple Inc.** 申请包含该 **entitlement** 的 **license** 文件。该 license 的申请和使用方式请参考 [Building spatial experiences for business apps with enterprise APIs for visionOS](https://developer.apple.com/documentation/visionos/building-spatial-experiences-for-business-apps-with-enterprise-apis)。
> **重要事项**
向苹果公司申请得到的 **entitlement** 中的 **Bundle ID** 应与创建 **EasyAR Sense License Key** 时填写的完全一致。
## 如何选择 visionOS App Mode
运行在 visionOS 上的 App 仅在 **Immersive Space** 下能够获取 ARKit 数据。而 Unity 编辑器打包的 App 在 **Immersive Space** 下基于渲染流程及 API 不同需要选择使用 **RealityKit with PolySpatial** 或 **Metal Rendering with Compositor Services** 模式。
关于 **Immersive Space** 的定义,可以参考苹果[官方文档](https://developer.apple.com/documentation/swiftui/immersive-spaces)。
关于 Unity 的 App Mode 的详细介绍，可以参考 Unity PolySpatial 文档中的 [visionOS Platform Overview](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/visionOSPlatformOverview.html)。
> **提示**
**App Mode 选择建议**
* **首选推荐：RealityKit with PolySpatial**
如果您是首次接触 visionOS，建议优先选择此模式。其优势在于能深度集成 visionOS 的系统级渲染特性，稳定性高，渲染效果好。
此模式不支持自定义代码着色器（HLSL/ShaderLab），必须使用 **Shader Graph**，且仅支持经 PolySpatial 兼容性检查后的特性（会被转换为 MaterialX）。
Unity 内置的 `Standard (Built-in)` 和 `Lit (URP)` 着色器已由官方预先适配，可直接使用。
* **进阶/特定需求：Metal Rendering with Compositor Services**
适用于有大量现有 3D 资产迁移需求或必须使用自定义着色器的复杂项目。
由于该模式下 Unity 负责全部渲染逻辑，绕过了系统的 RealityKit 管线，渲染效果一般不如 RealityKit 并且可能会遇到不可预见的渲染问题。
**EasyAR 接入建议：**
在尝试接入 EasyAR 时，请务必先使用 **RealityKit with PolySpatial** 模式跑通基础流程。这样可以有效隔离变量，避免因 Metal 底层适配问题与 AR 相关问题交织，从而导致难以定位故障成因。
## Unity 工程中的配置
Unity 工程中需要进行以下配置：
### 为 Unity 工程导入必要的 Package
**Unity 6 （推荐）**：
* `com.unity.xr.visionos` (2.0.4+)
* `com.unity.polyspatial` (2.0.4+)
* `com.unity.polyspatial.visionos` (2.0.4+)
* `com.unity.xr.visionos` (2.0.4+)
> **重要事项**
所有 Package 的版本号必须保持严格一致。
建议优先使用 Unity 6，部分早期的 Unity 2023.x 版本对 visionOS 尚不支持。
**Unity 2022.3**：
* `com.unity.xr.visionos` (1.2.3)
* `com.unity.polyspatial` (1.2.3)
* `com.unity.polyspatial.visionos` (1.2.3)
* `com.unity.xr.visionos` (1.2.3)
> **重要事项**
所有 Package 版本号必须保持严格一致。
不支持 **1.3.x** 版本，请务必锁定在 **1.2.3**。
### 选择 Build Platform
点击菜单栏中的 **File** > **Build Profiles** 将 Platform 切换至 **visionOS**。
![切换Build_Platform](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro01.png)
### 配置 Input System
确保使用新版的 `Input System Package`：
点击菜单栏中的 **Edit** > **Project Settings** > **Player**，将 **Active Input Handling** 槽设置为 **Input System Package(New)**。
此后 Unity 可能会要求重启工程，点击 **Apply** 使改动生效。
![InputSystem改动生效](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro02.png)
### 配置 XR Plug-in Management
点击菜单栏中的 **Edit** > **Project Settings** > **XR Plug-in Management**，在 visionOS 选项卡中的 Plug-in Providers 勾选 **Apple visionOS**。
![选择visionOS插件](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro03.png)
### 配置 Apple visionOS 插件
点击菜单栏中的 **Edit** > **Project Settings** > **XR Plug-in Management** > **Apple visionOS**。
根据[前文介绍](#setup-visionpro-how-to-choose-app-mode)选择合适的 **App Mode**。
![选择AppMode](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro04.png)
> **注意**
**Windowed** 模式由于不是运行于 **Immersive Space**，无法使用 AR 能力。
**Hybrid** 模式指开发者需要手动在 **Metal** 和 **RealityKit** 模式间切换，由于使用方式比较复杂，不推荐使用，具体可以参考 [Unity 官方对该模式的说明](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/PolySpatialHybridApps.html)。
接下来在同页面中进行以下修改：
* 在 **World Sensing Usage Description** 槽中添加一段描述。
* 将 **Metal Immersion Style** 设置为 **Mixed**。
* 将 **Reality Kit Immersion Style** 设置为 **Mixed**。
* 勾选 **IL2CPP Large Exe Workaround**。
![修改visionOS插件配置](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro05.png)
### [仅 RealityKit 模式需要] 导入 TextMesh Pro Essentials
点击菜单栏中的 **Edit** > **Project Settings** > **TextMesh Pro** > 点击 **Import TMP Essentials**
![Import TMP Essentials](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro09.png)
> **注意**
目前 **RealityKit with PolySpatial** 模式仅支持 **TextMesh Pro** 文字，若不导入则无法渲染文字。
### [仅 RealityKit 模式需要] PolySpatial 相关设置
点击菜单栏中的 **Edit** > **Project Settings** > **PolySpatial**，在该页面中进行以下修改：
* 设置 **Default Volume Camera Window Config** 为 `Default Unbounded Configuration`。
* 勾选 **Auto-Create Volume Camera**
![设置 PolySpatial](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro06.png)
如果需要另外指定 **Default Volume Camera Window Config**，必须确保其 **Mode** 为 **Unbounded**。
![确认 Mode 是 Unbounded](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro07.png)
场景中如果存在 `Volume Camera`，将其删除。
![删除场景中的 Volume Camera](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro08.png)
> **警告**
* **不支持** `World Transform` 数值不是 `identity` 的 `Volume Camera`。
* 若因**特殊原因**需要在场景中添加一个**唯一**的自定义 `Volume Camera`，请务必：
* 将其 `World Transform` 设为 `identity`。
* 确保其 `Volume Camera Window Configuration` 的 `Mode` 设置为 `Unbounded`。
* 在完全清楚 [Unity 官方文档](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/VolumeCamera.html)中其含义和用途的前提下使用。
### [使用 Mega 时]添加 Location Usage Description
> **小心**
若在 EasyAR 配置中启用了 **Location** 权限（使用 Mega 功能时），必须添加权限描述信息，否则 Build 将失败。
由于目前 Unity 的 **Project Settings** > **Player** > **visionOS** 选项卡中未显示 **Location Usage Description** 字段，请按照以下步骤配置：
1. **切换平台标签**：将选项卡暂时切换至 **iOS**。
2. **填入描述**：在 **Location Usage Description** 槽位中填入必要的权限用途说明。
3. **切回 visionOS**：将选项卡切回 **visionOS**，刚才填写的配置会自动保留并生效。
![Location Description](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro10.png)
## Xcode 工程中的配置
通过 Unity 打包得到的 Xcode 工程中需要进行以下配置：
### 配置相机数据 entitlement
* 将申请得到的 `Enterprise.license` 文件复制到 Xcode 工程文件目录。
![Copy to Xcode project folder](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro11.png)
* 将 Xcode 工程文件目录中的 `Enterprise.license` 拖入 Xcode 工程中。
![Move into Xcode project](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro12.png)
### 修改 info.plist 使应用能够保存和投送文件
若需要在应用中录制 EIF 并通过 visionOS 的文件应用投送到电脑或其他设备，需要在 `Info.plist` 中增加以下字段并修改：
* 添加 `LSSupportsOpeningDocumentsInPlace` 并将值设置为 `true`。
* 添加 `UIFileSharingEnabled` 并将值设置为 `true`。
![Modify Info.plist](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro13.png)
> **提示**
添加字段后 Xcode 界面上显示的 `Key` 与手动添加的字符串不同（比如输入了 `LSSupportsOpeningDocumentsInPlace` 但显示 **Supports opening documents in place**，这是正常的）。

---

## XREAL 工程配置方法
- 章节路径: `unity/headsets/setup-xreal.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/setup-xreal.html

# XREAL 工程配置方法
本章介绍如何配置 Unity 工程使其在 XREAL 头显上使用 EasyAR 的相关功能。
## 准备工作
* 获取适合 XR 头显或者眼镜的 EasyAR 许可证，头显或眼镜可用 License 类型包括
* EasyAR Sense 4.x **XR License 试用版**（试用，在 EasyAR 网站自主开通）
* EasyAR Sense 4.x **XR License 正式版**（付费后使用，请联系商务购买开通）
* EasyAR Sense 4.x **XR License 企业版**（企业版 SDK 使用）
其他许可证均不支持。
* 请通过商务获取 **XREAL** 的企业 License （注意，这个 License 是 XREAL 公司分发的文件，与 EasyAR 的 License 不同）。
* 下载并导入 [XREAL 的 SDK](https://developer.xreal.com/download)
* 下载并导入[EasyAR Unity 插件包](https://www.easyar.cn/view/download.html)
* 下载并导入 [EasyAR Unity XR设备扩展包](https://www.easyar.cn/view/download.html)
* 参考 [Android 工程配置](../fundamentals/setup-player.html)
> **注意**
当前仅支持 XREAL SDK >= 3.1
## 启用 XREAL 插件
1. 在 `Project Settings > XR Plug-in Management > XREAL` 中勾选 `Enable Native Session Manager`
![enablenativesession](https://doc-asset.easyar.com/develop/unity/headsets/media/xreal-enable-sdk-manager.png)
2. 在 `Project Settings > XR Plug-in Management > XREAL` 中配置 `License Asset` 为 XREAL 的企业许可证
![addxreallicense](https://doc-asset.easyar.com/develop/unity/headsets/media/xreal-add-license.png)
> **注意**
在 XREAL 上， 如果 `Frame Recorder` 的 `Format` 为 `Auto` 或 `H264` ，录制的数据质量被有意降低，Mega 的成功率和准确度都有不同程度的降低，因此其在电脑上的运行效果仅作为参考。
> **注意**
如需向 EasyAR 反馈问题数据，请设置 ARSession 上的 `Frame Recorder` 的 `Format` 为 `Obsolete` 进行录制，注意录制完成必须调用停止（设置 `enabled` 为 `false`）否则无法使用。这样录制出来的数据在 Unity 中使用会显示数据加密无法播放，这是正常的。

---

## BlockController 组件参考
- 章节路径: `unity/mega/comp-BlockController.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockController.html

# BlockController 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockController.html)
>
探索 BlockController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockController.png)
默认条件下组件截图。
|属性|描述|
|**Active Control**|选项：
* Hide Before First Found（默认）：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活。
* Hide When Not Tracking：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用。
* None：不控制 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的激活与否。|
|**ID**|Block ID。
只读。|

---

## BlockHolder 组件参考
- 章节路径: `unity/mega/comp-BlockHolder.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockHolder.html

# BlockHolder 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html)
>
探索 BlockHolder 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockHolder.png)
默认条件下组件截图。
|属性|描述|
|**Multi Block**|定位到多个Block时的策略。选项：
* Disable（默认）：不允许多个 block。运行中检测到多个 block 时，会抛出致命错误。
* PlayMode：block 间的相对变换会在运行时计算，（通常）由 Mega Studio 在编辑模式下设置的数值将会保持到相关的两个 block 都被定位到为止。
* EditMode：block 间的相对变换在运行时不会发生变化，会保持（通常）由 Mega Studio 在编辑模式下设置的数值不变。|
|**Block Root Source**|Block root 的来源。
* External（默认）：外部，比如 Mega Studio 生成的节点或事先组装好的节点。
* Internal：内部，需要时由 [BlockHolder](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html) 自身创建。
* Mixed：混合，可以来自外部或内部。|
|**Block Root**|所有 Mega block 的父节点。它通常由 Mega 工具生成。如未设置，一个新的 root 节点会在第一个 block 被持有的时候自动生成。|

---

## BlockRootController 组件参考
- 章节路径: `unity/mega/comp-BlockRootController.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockRootController.html

# BlockRootController 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockRootController.html)
>
探索 BlockRootController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockRootController.png)
默认条件下组件截图。
|属性|描述|
|**Active Control**|选项：
* Hide Before First Found：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活。
* Hide When Not Tracking（默认）：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用。
* None：不控制 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的激活与否。|
|**Root Location**|Block Root 的 GNSS（GPS、北斗等）信息。
它只在如下两种情况下有值：
1. 在编辑时，它下面其中一个 block 模型由 Mega Studio 导入且 block 数据含有GPS信息；
2. 在运行时，主动调用 [BlockHolder.Hold(BlockController.BlockInfo, Location)](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_Hold_EasyAR_Mega_Scene_BlockController_BlockInfo_EasyAR_Mega_Scene_Location_) 持有了一个 block。|
|*Latitude*|纬度。|
|*Longitude*|经度。|
|*Altitude*|海拔高度。|
|**Studio Tool**|当前控制 block 的 Studio 工具，仅用来在编辑模式下指示工具。|

---

## MegaTrackerFrameFilter 组件参考
- 章节路径: `unity/mega/comp-MegaTrackerFrameFilter.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-MegaTrackerFrameFilter.html

# MegaTrackerFrameFilter 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.MegaTrackerFrameFilter.html)
>
探索 MegaTrackerFrameFilter 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter.png)
默认条件下组件截图。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter-nomega.png)
未导入 `com.easyar.mega` 包，组件不可时的截图。
MegaTrackerFrameFilter 组件窗口由两个部分组成：组件配置和测试区域。
## 组件配置
|属性|描述|
|**Service**|服务访问信息。|
|*Type*|EasyAR Mega 服务类型。选项：
* Block：Mega Block。
* Landmark：Mega Landmark。|
|*Access Source*|服务访问数据源类型。选项：
* Global Config：使用全局服务器配置。根据 Service Type 选择 [GlobalMegaBlockLocalizationServiceConfig](../../../api/unity/easyar.EasyARSettings.html#u_easyar_EasyARSettings_GlobalMegaBlockLocalizationServiceConfig) 或 [GlobalMegaLandmarkLocalizationServiceConfig](../../../api/unity/easyar.EasyARSettings.html#u_easyar_EasyARSettings_GlobalMegaLandmarkLocalizationServiceConfig)。全局配置可以点击 Unity 菜单 EasyAR > Sense > Configuration 后在属性面板里面进行填写。
* API Key：使用 [APIKeyAccessData](../../../api/unity/easyar.APIKeyAccessData.html) 类型的访问数据。
* Token：使用 [TokenAccessData](../../../api/unity/easyar.TokenAccessData.html) 类型的访问数据。|
|*App ID*|Access Source 是 API Key 或 Token 时显示。
服务AppID。|
|*Server Address*|Access Source 是 API Key 或 Token 时显示。
服务地址。|
|*API Key*|Access Source 是 API Key 时显示。
API Key。|
|*API Secret*|Access Source 是 API Key 时显示。
API Secret。|
|*Token*|Access Source 是 Token 时显示。
Token。|
|**Request Time Parameters**|请求时间参数。|
|*Timeout*|与服务器通信的超时时间（毫秒）。|
|*Request Interval*|期望的请求间隔时间（毫秒），值越大整体误差越大。|
|**Location Input Mode**|位置输入模式。选项：
* Onsite：在现场使用的情况的输入模式。GNSS 数据通常从设备获取并输入到 Mega，通常由 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 内部处理。
* Simulator：远程调试或电脑上运行必须使用的输入模式，GNSS 数据需要模拟成现场数据并通过对应接口输入 Mega。可选。
* FramePlayer：在使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html) 时的输入模式。这个模式是只读的。远程调试或电脑上运行必须设置成 Simulator 模式，否则将无法使用。现场使用要设置成 Onsite 以达到最佳效果。|
|**Min Input Frame Level**|输入帧最小允许的 [MegaInputFrameLevel](../../../api/unity/easyar.MegaInputFrameLevel.html)。如果 frame source 只能给出维度更低的 [CameraTransformType](../../../api/unity/easyar.CameraTransformType.html) 的数据，session 会启动失败。选项：
* ZeroDof：0DoF。
* ThreeDof：3DoF。
* FiveDof：5DoF。
* SixDof：6DoF。|
## 测试区域
测试功能在 Unity play 模式下可用。
服务类型是 Block 时，测试区域显示 Block 测试功能：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter-test-block.png)
可以模拟 GNSS 数据进行测试。
服务类型是 Landmark 时，测试区域显示 Landmark 测试功能：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter-test-landmark.png)
可以模拟 GNSS 数据进行测试。
可以模拟 [MegaLandmarkFilterWrapper.FilterBySpotId(string, Action<MegaLandmarkFilterResponse>)](../../../api/unity/easyar.MegaLandmarkFilterWrapper.html#u_easyar_MegaLandmarkFilterWrapper_FilterBySpotId_System_String_System_Action_easyar_MegaLandmarkFilterResponse__) 和 [MegaLandmarkFilterWrapper.FilterByLocation(Action<MegaLandmarkFilterResponse>)](../../../api/unity/easyar.MegaLandmarkFilterWrapper.html#u_easyar_MegaLandmarkFilterWrapper_FilterByLocation_System_Action_easyar_MegaLandmarkFilterResponse__) 执行。

---

## 如何使用 Mega Studio 创建与实景精确对齐的 3D 内容
- 章节路径: `unity/mega/content-realworld-alignment.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/content-realworld-alignment.html

# 如何使用 Mega Studio 创建与实景精确对齐的 3D 内容
这篇文档将介绍如何使用 Unity 上的 Mega Studio 将虚拟物体准确地摆放在现实空间的某个位置，在 AR 体验中与现实空间精确对齐。
## 开始之前
* 参考文档 [我的定位库可以使用了吗？](../../mega/localization-verify.html) 确认定位库已正确创建并添加 **Mega Block**。
* 准备好 Unity 项目中要使用的 3D 资产。
## 精确摆放 3D 内容
通过完成以下步骤可以将虚拟内容准确地摆放在现实空间中。
### 将 3D 内容挂载至 Block 节点下
加载 Block 稠密模型后，将 3D 内容挂载至场景中的 Block 节点下，作为其子节点。
![挂载模型](https://doc-asset.easyar.com/develop/unity/mega/media/content-realworld-alignment05.png)
### 精确调整模型位置
在场景中对着稠密模型调整 3D 内容的位置和旋转，将其调整至期望的位置和朝向。
### [可选] 根据全景图精确调整模型位置
点击 **Inspector** 面板中的全景标记右侧的加载按钮，场景中出现全景标记。
![加载全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation13.png)
![显示全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation14.png)
点击任意一个**全景标记**，就可以在其位置进行全景下的摆放。您可以通过点击不同的**全景标记**切换全景，以确认 3D 内容在不同视角下的位置都是准确的。
![全景编辑](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation15.png)
## 如果加载的 Block 模型不水平怎么办
在 **Hierarchy** 面板中选择 **Block Root** ，在 **Inspector** 面板中修改 **Rotation** 直到稠密模型的朝向朝向在 Unity 编辑器中看起来正确。
> **重要事项**
Block Root 是在 3D 引擎场景节点树上所有 Block 节点的父节点。
Block Root 在世界坐标系下的 Transform **不会**影响 Block 的**本地坐标系**，也因此**不会影响作为 Block 子节点 3D 内容的渲染结果**。它的 Transform 和最终的显示效果**无关**。
## 如果加载的 Block 模型有破碎，缺损的部分怎么办
在三维重建过程中，若受采集视角覆盖不全的影响，生成的密模型中可能会出现破碎或缺损的部分。
![破碎缺损](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment02.png)
面对不完整的模型，若破碎/缺损部分的 3D 内容对齐精度要并不高，可以通过点击**全景标记**对照**全景图**的方式来摆放 3D 内容。之后可以通过点击附近不同的**全景标记**位置来验证效果。
![通过全景图摆放](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment03.png)
若破碎/缺损部分的 3D 内容对齐精度要求非常高，则需要通过[补充更新](../../../mega/scene-update/incremental.html)或[无损全量更新](../../../mega/scene-update/full.html)进行地图的补充或更新。一般来说这样的区域意味着采图过程中没有覆盖，在这样的区域内部 Mega 定位效果会受到影响，仅在编辑器中对齐 3D 内容是不够的。
## 后续步骤
* 通过[使用 session 验证工具模拟运行](verify-session-tool.html)进一步验证摆放的准确性。
* 为场景添加准确的[环境遮挡](occlusion.html)以增强 AR 的真实感。

---

## 导入最新版本的 EasyAR 插件以启用 Mega 功能
- 章节路径: `unity/mega/enable-mega.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/enable-mega.html

# 导入最新版本的 EasyAR 插件以启用 Mega 功能
本文介绍了如何导入最新版本的 EasyAR Sense Unity Plugin (for Mega) 以启用 Mega 功能。
## 使用 Mega 应导入最新版本的 EasyAR 插件
>
> 需要使用 Unity 2021.3.30 或更高版本。
>
在[下载页面](https://www.easyar.cn/view/download.html)，您会看到 Unity 插件有两个版本：`EasyAR Sense Unity Plugin` 和 `EasyAR Sense Unity Plugin (for Mega)`。
这两个版本的主要差异为：
* **EasyAR Sense Unity Plugin**： 不含 Mega 支持文件，不能用于 Mega 开发。EasyAR 提供从 4.6 开始的历史版本下载。
* **EasyAR Sense Unity Plugin (for Mega)**：包含 Mega 支持文件，可以用于 Mega 开发。EasyAR 不提供历史版本下载。
在使用 4000 之后的版本时，只要版本号相同，两个压缩包内的 EasyAR Sense Unity Plugin（即 `com.easyar.sense`）文件是完全相同的，可以互相替换。因此，如果您已经下载并导入了最新版本的 EasyAR Sense Unity Plugin，可以直接从 EasyAR Sense Unity Plugin (for Mega) 压缩包中提取 `com.easyar.mega` 文件导入到 Unity 项目中，而不需要重新导入整个插件包。
> **注意**
在 4000 版本之后，导入不兼容的 `com.easyar.sense` 和 `com.easyar.mega` 时，脚本编译器会报错，提示版本不匹配。请确保 `com.easyar.sense` 和 `com.easyar.mega` 来自同一版本的插件包或互相兼容。
4.7 版本的 `com.easyar.sense` 和 `com.easyar.mega` 的版本号包含后面的所有数字和字母在内必须完全一致，才能保证兼容性。
在应用上线前，建议再次查看 EasyAR 网站，如果有更新版本的 EasyAR Sense Unity Plugin (for Mega)，请下载并导入最新版本以确保应用可以正常使用最新的 Mega 服务，以确保最长的兼容性和最佳的性能。
> **重要事项**
使用过时的 EasyAR Sense Unity Plugin (for Mega) 开发的应用，可能无法使用最新的 Mega 服务。
在线上服务没有变化时（即 Mega 定位库的版本没有更新时），使用旧版本的 EasyAR Sense Unity Plugin (for Mega) 打包的应用仍然可以正常使用。
## 导入 EasyAR 插件和 Mega 支持包
解压下载的 zip 包之后可以看到 `readme` 和两个 `tgz` 文件，`tgz` 文件可以直接导入 Unity 不要再解压。
导入方法：
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`
* 在弹出的对话框中选择下载并解压得到的 `.tgz` 文件
两个 `.tgz` 文件 导入顺序不限，可以先导入 `com.easyar.sense`，也可以先导入 `com.easyar.mega`。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/package-import.png)
> **提示**
`com.easyar.mega` 依赖一些第三方包，如 `com.unity.cloud.ktx` 和 `com.unity.cloud.gltfast`，导入时请确保网络连接正常，以便 Unity 可以自动下载和导入这些依赖包。
在部分网络环境下，Unity 导入这些依赖包的过程可能比较缓慢，建议修改网络环境或多次尝试导入，直到所有依赖包都成功导入。
导入成功后，在 Unity 的 `Console` 窗口中不应看到任何错误提示，同时打开 `Package Manager` 窗口，可以看到 `EasyAR Sense Unity Plugin` 和 `EasyAR Mega Studio` 均已导入且显示为刚刚导入的版本号。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/package-imported.png)
> **注意**
在导入插件包后， `tgz` 文件不能被删除或移动到另一个位置，因此通常需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 后续步骤
* [快速入门](quickstart.html) Unity Mega 开发
* 使用 Mega 开发应用
* [AR Session 最佳实践](session-best-practice.html)
* [添加跟踪目标](target.html)
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)

---

## 在 Unity 中使用 EasyAR Mega 实现遮挡
- 章节路径: `unity/mega/occlusion.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/occlusion.html

# 在 Unity 中使用 EasyAR Mega 实现遮挡
遮挡 （Occlusion） 是提升 AR 虚实融合沉浸感的关键技术。本文将介绍如何在 Unity 中通过 EasyAR Mega 实现遮挡效果。
## 开始之前
* 完成[使用 EasyAR Mega Unity 样例快速入门](quickstart.html)。
* 能够[创建与实景对齐的内容](content-realworld-alignment.html)。
## 遮挡的实现方式
* 离线建模：在 Block 坐标系下，针对现实世界中的实体（如墙体、立柱、大型设备）创建 1:1 匹配的几何体；或通过对 Block 稠密模型进行裁剪与减面处理得到优化后的模型。
* 运行时对齐：在运行时，通过云定位将 Block 坐标系与现实空间对齐，并加载对应的几何体。
* 材质替换：为这些几何体赋予特殊的遮挡材质。
* 视觉效果：当 GPU 渲染其他虚拟物体时，会因深度测试未通过而自动剔除被遮挡部分的像素，从而使虚拟物体遵循现实物理空间的遮挡逻辑。
## 如何使用几何体作为遮挡
根据以下步骤可以在场景中添加作为遮挡使用的几何体并验证效果。
### 摆放遮挡几何体
根据 Mega Block 的稠密模型使用内置几何体或自建几何体作为遮挡摆放在 Block 坐标系下的正确位置。
![摆放遮挡几何体](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion01.png)
### [可选]根据全景图微调几何体的位置
![根据全景图微调遮挡](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion02.png)
### 为几何体赋予遮挡材质
将几何体材质修改为遮挡材质，可以使用 Unity 自带的 `SpatialMappingOcculusion`。
![根据全景图微调遮挡](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion03.png)
### 使用 EIF 数据模拟运行或实机运行
可以根据运行效果微调遮挡模型的摆放。
## 如何使用裁剪并减面的稠密模型作为遮挡
根据以下步骤将导出后的 Mega Block 稠密模型裁剪并减面得到用于遮挡的白模，并导入场景作为遮挡。
### 在 **Mega Blocks** 中导出
在 **Inspector** 面板中的 **Mega Blocks** 工具选择导出
![选择导出](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion04.png)
### 修改导出选项
在导出时注意修改导出选项。
![导出选项](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion05.png)
图中 1 为 LOD 层级，层级越低模型越简单，面数越少，若需要最高的精度选择2，若能接受降低精度以减少面数选择 1 或者 0。
图中 2 为导出贴图选项，由于我们只需要白模作为遮挡，不需要贴图。
### 对模型进行裁剪并减面
将导出后的模型在数字内容创建软件（例如 Blender）中进行裁剪，减面，保存为 `Glb`。
> **提示**
例子中使用的是 Blender 的 Decimate Modifier。
![裁剪前](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion06.png)
裁剪并减面后：
![裁剪后](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion07.png)
### 将遮挡模型导入 Unity 并挂载到场景中 Block 节点下方
![导入遮挡模型](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion09.png)
### 修改模型的 Transform
修改模型的 **Transform** 使 **Position**，**Rotation** 均全部为 **0**。
此时用于遮挡的白模应该和稠密模型贴合，这是因为在数字内容创建软件中进行裁剪和减面操作时，并没有改变 Block 坐标系的定义。
![遮挡模型贴合](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion10.png)
### 为模型赋予遮挡材质
将模型材质修改为遮挡材质，可以使用 Unity 自带的 `SpatialMappingOcculusion`。
![遮挡模型更换材质](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion11.png)
### 使用 EIF 数据模拟运行或实机运行
使用 EIF 数据模拟运行或实机运行，查看效果。
## 遮挡的效果预期
遮挡的效果主要由以下几点影响：
* 定位跟踪本身的精度
* 模型摆放的准确程度
* 模型本身的精度（如果不是简单的几何体）
在定位漂移时出现数公分未对齐的情况是正常的。
遮挡用的模型面数太多容易影响性能，建议只在必要区域使用，并且尽量使用简单的几何体作为遮挡。
## 相关主题
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [使用 session 验证工具模拟运行](verify-session-tool.html)

---

## 现场使用和模拟运行
- 章节路径: `unity/mega/onsite-and-simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/onsite-and-simulation.html

# 现场使用和模拟运行
本文介绍了 Mega 在现场使用和非现场模拟运行时的配置差异，以及如何根据需求进行配置。
## 现场使用和模拟运行的差异
Mega 会使用 GNSS（GPS、北斗等）信息对定位过程进行辅助，以提升定位的精度和稳定性。在现场使用时，设备的 GNSS 信息是准确的可以用来辅助定位。而在非现场模拟运行时，设备的 GNSS 信息与环境是不匹配的，这个数据不能用来辅助定位，反而会影响定位效果。因此，Mega 提供了两种不同的配置以适应现场使用和非现场模拟运行的需求。
默认配置为模拟运行配置，以避免初次使用时因错误配置导致的定位失败的问题。
在模拟运行的配置下，屏幕上会始终显示警告信息，这段信息无法关闭，以确保应用不会以错误的配置发布到最终用户手中。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/warn-simulation.png)
> **提示**
如果要关闭警告信息，需要确保应用只会在现场使用，并使用现场配置。
## 配置以用于非现场模拟运行
选中 session 下的 `Mega Tracker` 物体，找到 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件，选择 `Location Input Mode` 为 `Simulator` 选项即可启用模拟运行配置。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-simulator.png)
在脚本中，可以设置 [MegaTrackerFrameFilter.LocationInputMode](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocationInputMode) 为 [Simulator](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_Simulator) 来达到同样的效果。
> **注意**
[使用 EIF 文件模拟运行](../simulation/playback.html) 时，该选项会被自动设置为 [FramePlayer](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_FramePlayer) 且不可更改，以确保 EIF 文件内记录的 GNSS 数据被正确使用。
## 配置以用于现场使用
选中 session 下的 `Mega Tracker` 物体，找到 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件，选择 `Location Input Mode` 为 `Onsite` 选项即可启用现场使用配置。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-onsite.png)
在脚本中，可以设置 [MegaTrackerFrameFilter.LocationInputMode](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocationInputMode) 为 [Onsite](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_Onsite) 来达到同样的效果。
> **小心**
如果在非现场模拟运行时错误地使用了现场配置，可能会导致定位失败进而影响内容的显示。

---

## 使用示例快速入门 EasyAR Mega Unity 开发
- 章节路径: `unity/mega/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/quickstart.html

# 使用示例快速入门 EasyAR Mega Unity 开发
本教程介绍如何配置并运行 EasyAR Mega Unity 示例，以快速入门 EasyAR Mega 开发。
## 开始之前
阅读本篇之前，需要确保您已完成：
* 有一个 [有效的云定位库](../../mega/localization-verify.html)。
* 安装 Unity（2021.3.30 LTS 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
* 按 [启用 Mega](enable-mega.html) 的方法导入 `com.easyar.sense-\*\*.tgz` 和 `com.easyar.mega-\*\*.tgz` 包。
## 示例使用方法（六步走）
下面将分六个步骤介绍如何配置并运行 EasyAR Mega 的核心示例 `MegaBlock\_Basic`。
### 第一步：导入示例
> **注意**
如果通过 `\*\*All Samples\*\*` 导入了全部示例，需要跳过此步骤。
1. 使用菜单 `Window` > `Package Manager` 打开 Package Manager，选中 `EasyAR Sense Unity Plugin`, 在右侧的 **Samples** 中展开所有示例。
2. 选择示例（如 `MegaBlock\_Basic`），点击 **Import**。
![Import Sample](https://doc-asset.easyar.com/develop/unity/mega/media/sample-import.png)
> **注意**
* 本教程不能直接适用于头显设备，但在开发头显设备之前，需要使用手机开发了解流程。
* 如果您先前已经导入过旧版 SDK 的示例，在升级 SDK 之后需先删除旧示例再重新导入。
### 第二步：填写 License Key 并配置 Mega 云定位服务
1. 菜单栏选择 `EasyAR` > `Sense` > `Configuration`；
![License Guide](https://doc-asset.easyar.com/develop/unity/mega/media/fill-license-where.png)
2. 在打开的 **Project Settings** 面板中粘贴您的 License Key；
![Fill License](https://doc-asset.easyar.com/develop/unity/mega/media/fill-license-text.png)
> **提示**
EasyAR Sense License 可以从 [EasyAR 开发中心](https://www.easyar.cn/view/login.html) 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/mega/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `否`
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
> **注意**
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
1. 将您的 Mega 云定位库的各项信息配置到 **Project Settings** 面板中的 `Mega Block` 项；
![Mega Config Guide](https://doc-asset.easyar.com/develop/unity/mega/media/fill-mega-config-where.png)
> **提示**
Mega 云定位库配置可以从EasyAR开发中心获取。
![Mega Config Detail](https://doc-asset.easyar.com/develop/unity/mega/media/mega-config-detail.png)
确保您的 `API Key` 具有 `Mega Block` 的权限，如果没有需要进行更改或重新创建。
![API Key Auth](https://doc-asset.easyar.com/develop/unity/mega/media/check-apikey-auth.png)
### 第三步：摆放 3D 内容
1. 在 `Hierachy` 面板空白处右键点击，添加 Block 浏览工具（Unity 开发）；
![Add Block Viewer](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer.png)
2. 访问 Mega 定位服务；
1. 选中 `EasyAR.Mega.BlockViewer (Dev)` 节点，在 **Inspector** 面板中填写您的 EasyAR 账号信息并登录；
![login](https://doc-asset.easyar.com/develop/unity/mega/media/login.png)
2. 点击 Mega Cloud Service 右侧按钮；
![Click Mega CLS](https://doc-asset.easyar.com/develop/unity/mega/media/click-cls.png)
3. 选择您所要使用的 `Mega定位服务`，点击**确定**。
![Select Mega CLS](https://doc-asset.easyar.com/develop/unity/mega/media/select-cls.png)
4. 加载 Block
在选择服务之后，当前库中的 Block 列表会显示在 `MegaBlocks` 节点下，并显示在工具面板上。点击**加载**选择的Block：
![Load Block](https://doc-asset.easyar.com/develop/unity/mega/media/load-block.png)
加载完成后，Block 会显示在 `Scene` 窗口中。您可以在 `Scene` 窗口中操作，调整查看的视角、位置。同时检查下 Block 文件是否可用（比如 Block 坐标系是否正常，是否存在分层，是否过于模糊、存在缺损而无法找到位置摆放 AR 资源等）。
![Display Block](https://doc-asset.easyar.com/develop/unity/mega/media/block-in-scene.png)
5. 摆放 3D 内容
此时，您可以参考 Block 摆放 3D 物体。
![Place 3D Object](https://doc-asset.easyar.com/develop/unity/mega/media/annotate-in-block.png)
> **注意**
* 3D 物体必需摆放在工具自动生成的 `MegaBlocks` > `Block\_\*` 节点之下，以确保在运行时虚拟内容的渲染位置是正确的。
* 请不要修改 `Block\_\*` 节点的名字和 `local transform`，它由工具自动管理。
### 第四步：配置 MegaTracker
1. 配置 **Block Root**；
展开 `AR Session` ，选择 `Mega Block Tracker` 并设置 `Block Root` 为工具生成的 `MegaBlocks` 节点。
![Set Block Root](https://doc-asset.easyar.com/develop/unity/mega/media/set-block-root.png)
### 第五步：修改 Player 配置
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击安卓图标，调出 Android 平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
* 修改 Package Name 为 License Key 页面显示的 Package Name
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Package Name 是 `com.mycompany.myproject`，则必须填写这里 Package Name 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 Minimum API Level 为 `API Level 21` 或更高版本
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* 修改 Scripting Backend 为 `IL2CPP`，并在 `Target Architecture` 中勾选 `ARM64`
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-64bit.png)
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
* 修改 Bundle ID 为 License Key 页面显示的 Bundle ID
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Bundle ID 是 `com.mycompany.myproject`，则必须填写这里 Bundle ID 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 `Architecture` 为 `ARM64`
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* 添加 `Camera Usage Description` 和 `Location Usage Description`，字符串内容可以随意填写，但必须添加。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/mega/media/ios-permissions.png)
### 第六步：构建并运行
1. 添加当前场景至 `File` > `Build Settings` 或 `Build Profiles` > `Scene List` 中；
2. 切换到目标平台（如Android / iOS），检查包名（Bundle ID）与 License Key 是否一致；
![Switch Platform](https://doc-asset.easyar.com/develop/unity/mega/media/build-switch-platform.png)
3. 点击 **Build And Run**。
![Build And Run](https://doc-asset.easyar.com/develop/unity/mega/media/build-and-run.png)
现场实拍的运行效果如下：
## 关于屏幕上的黄色文字
运行时，您可能会看到屏幕上显示了两处黄色文字。
1. 模拟运行的警告信息
它位于屏幕下方：
![](https://doc-asset.easyar.com/develop/unity/mega/media/warn-simulation.png)
出现这个警告的原因是因为在默认配置下，应用可以不在现场运行。它对应用的运行效果有些微影响，如果您正好在现场使用，可以在打包前 [修改 MegaTracker 配置](onsite-and-simulation.html)。
2. 诊断信息
它位于屏幕上方，用于了解 session 的运行状态和问题，建议在开发和测试阶段保持显示：
![](https://doc-asset.easyar.com/develop/unity/mega/media/ui-message.png)
可以参考 [场景中的诊断信息](../getting-started/diagnostics.html) 来快速了解如何配置和使用这些诊断信息。
## 下一步：从入门到精通
恭喜！通过以上步骤，您已成功在 **10 分钟内** 运行了 EasyAR Mega 的核心示例，亲身体验了空间定位与 AR 内容叠加的魅力。
现在，您已经掌握了基础。如果您希望：
* **构建更稳定、更高效的 AR 应用**
* **实现复杂的虚实遮挡、内容对齐等效果**
* **在没有设备或无法前往现场时进行调试**
请参考以下深入指南，它们将帮助您解决开发过程中的实际问题。
### 开发进阶
如果您希望了解完整的工程配置，可以参考以下内容：
* [使用 Universal Render Pipeline（URP）](../getting-started/universal-render-pipeline.html)
* [Player 配置](../fundamentals/setup-player.html)
* [EasyAR 配置](../fundamentals/setup-easyar.html)
如果您希望进一步了解 EasyAR 的使用方法，可以从这里开始：
* [AR 驱动的 Unity 应用基础](../fundamentals/intro.html)
同时，建议阅读以下内容来帮助您开发和调试：
* [Unity 开发中的问题诊断和报告](../diagnostics/diagnostics.html)
* [Unity AR 模拟运行](../simulation/simulation.html)
### 精细化控制 Mega 功能
下面的这些内容将帮助您更好地在您的应用中使用 Mega：
* [现场使用和模拟运行](onsite-and-simulation.html)
* [ARSession 最佳实践](session-best-practice.html)
* [添加跟踪目标](target.html)
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [环境遮挡 (Occlusion)](occlusion.html)
* [控制跟踪过程](tracker.html)
下面的这些内容将帮助您无需到达现场即可验证 Mega 功能：
* [使用 PC 相机进行快速验证](verify-pc-camera.html)
* [使用 Session 验证工具进行模拟运行](verify-session-tool.html)
### 高级主题
下面的这些内容更加适合在有一定 EasyAR 使用经验后阅读。
如果您希望在头显上运行 EasyAR Mega，可以参考以下内容：
* [Unity 中的 EasyAR 头显支持](../headsets/headsets.html)
* [在 XR 头显或眼镜上使用 EasyAR 样例](../headsets/samples.html)
如果您希望使用 AR Foundation，可以从这里开始：
* [EasyAR 对 Unity XR 框架的支持](../fundamentals/unity-xr.html)

---

## 适用于 Mega 的 AR Session 最佳实践
- 章节路径: `unity/mega/session-best-practice.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/session-best-practice.html

# 适用于 Mega 的 AR Session 最佳实践
本文介绍了如何创建和配置适用于 Mega 的 AR session，以便在不同类型的设备上获得最佳的运行效果。
## 开始之前
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 了解如何 [创建 session](../fundamentals/session-creation.html)
## 默认配置的 session
对于大部分应用，推荐使用默认的 Mega session 配置，这些配置已经过优化，适用于大部分常见的使用场景。
默认的 session 支持以下类型的设备：
* 支持 6DoF 运动跟踪的设备（部分现代手机和头显）
* 支持 5DoF 惯性导航功能的设备（大部分有陀螺仪和加速度计的 Android 手机）
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Mega` > `AR Session (Mega Block Default Preset)` 可以创建默认的 Mega session。
对应的脚本代码如下：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.MegaBlock\_MotionTracking\_Inertial)
```
该 session 使用 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设：
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Mega` > `AR Session (Mega Landmark Default Preset)` 可以创建默认的 Mega session。
对应的脚本代码如下：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.MegaLandmark\_MotionTracking\_Inertial)
```
该 session 使用 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设：
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组。
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Landmark](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Landmark)
## 选择不同的预设
除了默认配置的 Mega session 外，还可以根据具体需求选择不同的预设来创建 session，它们的主要差别在于支持设备类型不同。
使用菜单和 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 创建 session 时可选的预设包括：
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)（默认）
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ZeroDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ZeroDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
使用菜单和 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 创建 session 时可选的预设包括：
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)（默认）
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ZeroDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ZeroDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
> **注意**
Mega 在不同类型的设备上运行效果是不一样的，详情可以参考 [Mega 支持的设备和平台应用](../../mega/devices.html)。
## 后续步骤
* [添加跟踪目标](target.html)
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)
## 相关主题
* 阅读 [帧数据源](../cameras/frame-source.html) 了解帧数据源的基本概念及运行时帧数据源选取过程
* 阅读 [添加一组帧数据源](../cameras/frame-source-group.html) 了解数据源组的配置和使用方法
* 阅读 [Mega 支持的设备和平台应用](../../mega/devices.html) 了解 Mega 支持的设备以及在不同设备上的运行效果

---

## 添加 Mega 跟踪目标
- 章节路径: `unity/mega/target.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/target.html

# 添加 Mega 跟踪目标
本文介绍了如何添加 Mega 的跟踪目标以及如何在 Unity 编辑器中加载环境模型以辅助开发。
## 开始之前
* 检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
* [导入最新版本的 EasyAR 插件以启用 Mega 功能](enable-mega.html)
* 了解 [Unity AR 的跟踪目标](../fundamentals/target.html) 的基本概念和使用方法
> **注意**
以下内容及工具仅适用于使用 EasyAR Mega 开发 Unity 应用的过程。
如果您在开发小程序，请参考 [使用 Unity 编辑器创建并上传标注（小程序开发）](../../wechat/mega/content-annotation-creation.html)。
如果您只希望查看 Mega 建图结果，请参考 Mega 使用指南中的 [预览3D 实景网格](../../../mega/mapping/textured-mesh.html)。
如果您需要模拟运行查看定位效果，但您并没有一个可以使用的 Unity 应用工程，请参考 Mega 使用指南中的 [模拟运行效果预览](../../../mega/simulation-verification/intro.html)。
## Mega 的跟踪目标
Mega 的跟踪目标是包含 [BlockController](../../../api/unity/EasyAR.Mega.Scene.BlockController.html) 组件的空物体，称为 block。在场景中，block 会被组织在一个包含 [BlockRootController](../../../api/unity/EasyAR.Mega.Scene.BlockRootController.html) 组件的空物体下，这个物体的默认名称为 `MegaBlocks`。`MegaBlocks` 下所有的 block 物体代表了当前定位库中的所有跟踪目标。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/target-block.png)
开发中经常需要使用 block 模型来辅助查看和摆放 3D 内容。这个模型可以使用工具加载到场景中，方便查看和参考。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/target-block-model.png)
模型位置是与 block 跟踪目标对齐的，可以直接在模型上摆放 3D 内容。
> **提示**
模型存储于工具节点下，仅存在于编辑器模式下，不会被打包进最终应用。
## 在编辑器中添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [External](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_External)（默认） 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/block-root-source.png)
### 添加 Block Viewer for Unity Developer 工具
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Mega` > `Tool` > `Block Viewer for Unity Developer (Edit Mode)` 可以添加 Unity 开发用的 Block Viewer 工具。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer.png)
> **重要事项**
使用 Unity 开发 Mega 应用时，必须使用 `Block Viewer for Unity Developer` 工具。`EasyAR Mega` > `Tool` 菜单下的其它工具不适合做 Unity 应用开发。
虽然 `Annotation Tool` 也有类似的功能，但这个工具的部分功能将在未来版本中被移除，因此不建议使用。
`Annotation Tool` 的标注功能（仅标注本身）即将迁移至 EasyAR 开发中心网页，block mesh 加载和模型摆放不受影响。
工具添加成功后，场景层级中会多出一个 `EasyAR.Mega.BlockViewer (Dev)` 节点和一个 `MegaBlocks` 节点。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer-result.png)
### 生成跟踪目标 —— block
选中 `EasyAR.Mega.BlockViewer (Dev)` 节点，在 **Inspector** 面板中填写 EasyAR 账号信息并登录；
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/login.png)
点击 Mega Cloud Service 右侧按钮；
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/click-cls.png)
选择需要使用的 `Mega定位服务`，点击**确定**。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/select-cls.png)
在选择服务之后，当前库中的 block 列表会显示在 `MegaBlocks` 节点下，并显示在工具面板上。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/load-block.png)
> **提示**
为什么我的 `MegaBlocks` 下面是空的？
建议检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
到这里已经生成了跟踪目标 block，`MegaBlocks` 节点下每个 `Block\_` 开头的子节点即代表一个 block 跟踪目标。
### 加载 block 模型
点击**加载**选择的Block：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/load-block-2.png)
加载完成后，Block 会显示在 `Scene` 窗口中。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/block-in-scene.png)
## 定位成功时自动添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [Internal](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Internal) 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)。
在这两个模式下，如果定位到一个新的 block 且 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下没有该 block，这个新的 block 会被自动添加到 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下。如果 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 不存在会被自动创建。
> **提示**
定位成功时自动添加跟踪目标时，无法加载 block 模型，仅能添加 block 跟踪目标。
## 在脚本中添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [Internal](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Internal) 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)，这时如果 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 不存在会被自动创建。或者也可以在 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [External](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_External) 时在编辑器中事先指定好 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 物体。
> **注意**
如果 block 不在定位库中，即使使用脚本添加到场景中，block 也无法被定位到。
可以使用 [BlockHolder.Hold](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_Hold_) 方法添加一个新的 block 到 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下。这个方法通常用在使用 ema 标注文件时，脚本读取到标注信息后添加 block。
比如，下面的代码片段展示了如何使用标注文件中的信息添加 block：
```
foreach (var item in ema.blocks)
{
var info = new BlockController.BlockInfo { ID = item.id.ToString(), Timestamp = item.timestamp };
if (!item.keepTransform && item.location.OnSome)
{
blockHolder.Hold(info, item.location.Value);
}
else
{
blockHolder.Hold(info, item.transform.ToUnity());
}
}
```
> **提示**
使用脚本在运行时添加跟踪目标时，无法加载 block 模型，仅能添加 block 跟踪目标。
## 后续步骤
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)
## 相关主题
* [Mega Studio（Unity）操作手册](../../../mega/reference/studio-unity/intro.html)

---

## 控制 Mega 跟踪过程
- 章节路径: `unity/mega/tracker.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/tracker.html

# 控制 Mega 跟踪过程
本文介绍了如何控制 Mega 跟踪过程中的各项功能和参数，以满足不同应用场景的需求。
## 开始之前
* 检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
## 调整设备支持等级
[MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 的 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 属性用于指定 Mega 支持的最低设备等级。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-level.png)
Mega 可以在几乎所有类型的帧数据源上运行，但不同的帧数据源对跟踪效果有不同的影响。
默认情况下，Mega 会选择设备支持的最高等级的帧数据源进行跟踪。[默认配置下的支持 Mega 的 session](session-best-practice.html) 已经配置了支持 6DoF 和 5DoF 的帧数据源。
在 Mega 运行时要支持某个等级的帧数据源需要满足两个条件：
* 所需的帧数据源在 session 的可选帧数据源组中。
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 大于或等于所需的帧数据源的 [CameraTransformType](../../../api/unity/easyar.CameraTransformType.html) 等级。
比如，要在默认 session 中支持 3DoF 跟踪，需要：
* 添加 [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html) 到 session 的帧数据源组中。
* 修改 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)。
又比如，要在默认 session 中删除 5DoF 跟踪支持，需要：
* 从 session 的帧数据源组中删除 [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)。
* 修改 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)（即使不修改，由于没有 5DoF 帧数据源，5DoF 也不会被使用）。
在没有满足条件的帧数据源可用时，session 组装会失败。
## 跟踪目标管理
使用 Mega 时，需要指定 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 使用的 target 即 block。
### block 来源控制
大部分情况下，建议保持默认配置，即在编辑器中使用 Mega Studio 导入 block。
选中 session 下的 `Mega Tracker` 物体，`Block Root Source` 选项应该保持为 `External`（默认）。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-rootsource.png)
同时，需要指定 `Block Root` 为场景中的 `MegaBlocks` 物体。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-rootsource-external.png)
修改 `Block Root Source` 选项可以指定其它 block 来源方式，比如使用 ema 导入数据时，通常会选择 `Internal` 或 `Mixed` 选项。
在脚本中，可以修改 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 来达到同样的效果。
### 多目标跟踪控制
在大部分的 Mega 使用场景下，没有使用多目标的必要。在熟练掌握如何避免多个 block 互相影响之前，建议一个定位库中只放一个block。
> **提示**
原理上，Mega 会计算设备在所有 block 中的位置，而不是从定位库中抽选设备看到的 block。考虑不周的使用可能会因数据混淆等原因导致效果劣化。
选中 session 下的 `Mega Tracker` 物体，修改 `Multi Block` 选项可以启用或禁用多目标跟踪功能。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-multi-block.png)
在脚本中，可以修改 [BlockHolder.MultiBlock](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_MultiBlock) 来达到同样的效果。
> **警告**
一般情况下，一个定位库里只能同时有一个 block。
修改多目标配置会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中该配置被修改过，向 EasyAR 反馈问题时请务必说明这一点。
## 了解当前系统状态
在默认 session 配置下，[UI 消息](../diagnostics/ui-messages.html) 会显示在屏幕上，其中包含了 Mega 跟踪状态的信息。
在定位成功时，Mega Block 下会包含 `Found` 状态文字以及当前跟踪的 block 名称和 ID：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-status-found.png)
在定位失败时，Mega Block 下会包含 `NotFound` 状态文字：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-status-notfound.png)
> **提示**
`NotFound` 是正常状态，在 Mega 工作的整个过程中经常会出现该状态，出现该状态时跟踪仍然在继续。通常应用开发中不需要对 `NotFound` 状态进行特殊处理。
使用 [MegaTrackerFrameFilter.LocalizationRespond](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocalizationRespond) 事件可以获取当前的定位状态，从而了解系统当前是否找到了跟踪目标。
以下代码展示了如何使用该事件，以及常见的需要应用关注的异常状态的处理方法：
```
private void Awake()
{
megaTracker.LocalizationRespond += HandleLocalizationStatusChange;
}
private void HandleLocalizationStatusChange(MegaLocalizationResponse response)
{
var status = response.Status;
wakingUpCount = status == MegaTrackerLocalizationStatus.WakingUp ? wakingUpCount + 1 : 0;
if (wakingUpCount >= 5)
{
// 服务正在唤醒中，需要让终端用户等待
}
if (status == MegaTrackerLocalizationStatus.QpsLimitExceeded)
{
// QPS 超限，会随机有终端用户定位失败（总体跟踪质量下降）
// 这时一般需要付费提升 QPS 上限以保障当前用户量下的跟踪质量
}
if (status == MegaTrackerLocalizationStatus.ApiTokenExpired)
{
// Token过期，这只会出现在使用 Token 接口访问服务时
// 接近该问题需要应用请求自己的后台获取 Token，并调用 MegaTrackerFrameFilter.UpdateToken 进行更新
}
}
```
如果应用经常遇到 [MegaTrackerLocalizationStatus.RequestTimeout](../../../api/unity/easyar.MegaTrackerLocalizationStatus.html#u_easyar_MegaTrackerLocalizationStatus_RequestTimeout) 状态，通常说明设备连接服务的网络状况不佳，建议优化网络环境以提升跟踪质量。在网络状况无法改善的场景下，可以考虑增加请求超时时间。
> **注意**
无法通过该事件获取定位返回的 pose。
事实上，定位返回的 pose 在应用开发中是不需要的，EasyAR 会在定位返回后通过本地算法计算出更准确的 pose 并返回给开发者使用，而该 pose 已经体现在 block 的 transform 中，可以参考 [获取 session 的运行结果](../fundamentals/session-output.html)。
## 暂停和继续
Mega 的跟踪和定位功能可以分别暂停和继续。
### 暂停跟踪
设置 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 为 false 可以暂停跟踪。
默认在跟踪暂停后，所有 block 节点下的内容都会隐藏。
### 暂停定位
设置 [MegaTrackerFrameFilter.ResultPoseType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ResultPoseType).[EnableLocalization](../../../api/unity/easyar.MegaResultPoseTypeParameters.html#u_easyar_MegaResultPoseTypeParameters_EnableLocalization) 为 false 可以暂停定位。
> **警告**
暂停定位会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中定位被暂停过，向 EasyAR 反馈问题时请务必说明这一点。
## 服务和请求控制
可以通过修改 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件的参数来控制请求服务的行为。
### 请求间隔和超时
选中 session 下的 `Mega Tracker` 物体，修改 `Request Time Parameters` 下的选项可以调整请求服务的时间间隔和超时时间。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-timep.png)
在脚本中，可以修改 [MegaTrackerFrameFilter.RequestTimeParameters](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_RequestTimeParameters) 来达到同样的效果。
> **警告**
修改请求间隔会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中请求间隔被修改过，向 EasyAR 反馈问题时请务必说明这一点。
### 切换定位库
使用 [MegaTrackerFrameFilter.SwitchEndPoint(ExplicitAddressAccessData, BlockRootController)](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_SwitchEndPoint_easyar_ExplicitAddressAccessData_EasyAR_Mega_Scene_BlockRootController_) 可以在运行时切换定位库。使用这个接口时相机画面及 session 不会中断。
## 相关主题
* [适用于 Mega 的 AR Session 最佳实践](session-best-practice.html) 介绍了如何创建和配置适用于 Mega 的 AR Session
* [添加 Mega 跟踪目标](target.html) 介绍了如何添加 Mega 的跟踪目标 block 以及如何在 Unity 编辑器中加载 block 模型以辅助开发
* [添加一组帧数据源](../cameras/frame-source-group.html) 介绍了如何修改 session 的帧数据源组
* [获取 session 的运行结果](../fundamentals/session-output.html) 介绍了如何获取 session 组件的跟踪结果
* [UI 消息](../diagnostics/ui-messages.html) 介绍了如何使用 UI 消息来显示 session 状态

---

## 使用 PC 摄像头快速跑通 Mega （一种快捷但不推荐的远程调试方式）
- 章节路径: `unity/mega/verify-pc-camera.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/verify-pc-camera.html

# 使用 PC 摄像头快速跑通 Mega （一种快捷但不推荐的远程调试方式）
本文档旨在指导开发者如何在没有 EIF 录制文件的情况下，利用 PC 摄像头配合现场图片，验证 Mega 云定位服务是否能跑通。
## 开始之前
* 完成[快速入门](quickstart.html)，了解如何运行包含 Mega 功能的 Unity 应用。
* PC 连接一个摄像头设备，并确保其功能正常。
* **功能预期**：
该方式**并非**我们推荐的远程调试方式，在有条件录制的情况[使用 EIF 文件进行调试](verify-session-tool.html)是我们推荐的最佳实践。
该方式仅用于**在没有 EIF 文件**情况下调试**与跟踪效果无关**的流程开发，比如用于验证 Mega 服务是否通畅。
PC 上使用相机看到的效果与实机的跟踪效果**完全无关**。
## 操作步骤
完成以下步骤即可快速跑通 Mega 服务验证。
### 获取现场照片
获取一张现场较为清晰的照片，可以现场拍摄也可以在编辑器中使用全景预览功能截取一张图片。
**如何使用全景预览功能截取图片**
>
> 点击场景
> Hierarchy
> 面板中的
> Mega Block Viewer(Dev)
> > 在
> Inspector
> 面板中点击
> 全景标记
> 右侧的
> 加载
> 。
>
![全景加载](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera02.png)
>
> 此时场景中会出现许多代表
> 全景标记
> 的黄色小球：
>
![全景标记](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera06.png)
>
> 点击
> 需要预览的位置的全景标记
> > 点击场景
> Hierarchy
> 面板中的
> Mega Block Viewer(Dev)
> > 在
> Inspector
> 面板中点击
> 全景标记
> 左侧的
> 隐藏
> 。
>
![全景标记隐藏](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera07.png)
>
> 即可在
> Mega Panorama
> 窗口中得到一张现场图片，将其截图保存：
>
![现场图片](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera05.png)
>
### 对照 Block 稠密模型或全景摆放一些 3D 内容
![摆放3D内容](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera03.png)
### 确认 Session 验证工具没有开启
点击场景中的 **AR Session (EasyAR)** > 确认其 **Inspector** 面板上的 **Frame Player** 被关闭。
![确认FramePlayer关闭](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera12.png)
点击场景中的 **EasyAR.Mega.BlockViewer(Dev)** > 确认其 **Inspector** 面板上的验证工具没有被 **Enable** (若不需要使用稠密模型，也可以直接删除或隐藏 **EasyAR.Mega.BlockViewer(Dev)**)。
![确认验证工具关闭](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera10.png)
### 点击运行，使用现场图片跑通 Mega
* **操作示范：**
> **重要事项**
Mega 定位服务对于用于定位的输入比较“宽容”，但这种调试方式的结果仅用于区分“通”与“不通”（即 0 或 1 的区别）。它能证明 Mega 定位服务已跑通，但完全不能代表真机上的实际跟踪体验。若要观察定位速度和跟踪稳定性，务必[使用 EIF 文件调试](verify-session-tool.html)或真机实测。
* **可以使用相机对着图片或视频运行**，如果定位成功，将会看到 3D 物体贴屏显示并跳跃更新。由于在场景中加载了 Block 模型，Block 模型也会显示出来。
* 如果将工具 `EasyAR.Mega.BlockViewer (Dev)` 关闭（`active` 设成 `false` 或删除节点），看到的就是在现实场景中叠加了虚拟物体的效果。
* **屏幕上的警告信息是无法关闭的**，因为这种使用方式并不能反映真实效果，我们限制这种方式只能在开发过程中使用，且开发人员应该清楚这样使用的影响。
![屏幕警告信息](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera11.png)
* 可以**通过诊断信息时间戳更新判断系统是否正常运行**：如果看到屏幕上显示的诊断信息中时间戳在不断更新，就说明系统已经正常在运行了。
![通过时间戳判断](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera12.gif)
> **重要事项**
在使用时，你一定会注意到运行时显示在屏幕上或目视前方的诊断信息文字，仔细阅读 [UI 消息输出](../diagnostics/ui-messages.html)，仔细斟酌在开发阶段、测试阶段、应用上线之后应该采取何种配置，以及保留何种控制开关。与 EasyAR 的沟通通常需要提供这些信息，建议多利用而不是立马关闭。
## 后续步骤
* 尽可能[使用 session 验证工具模拟运行](verify-session-tool.html)。

---

## 使用 session 验证工具模拟运行使用 Mega 能力的 AR 工程
- 章节路径: `unity/mega/verify-session-tool.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/verify-session-tool.html

# 使用 session 验证工具模拟运行使用 Mega 能力的 AR 工程
本文旨在指导开发者如何在 Unity 编辑器上利用 session 验证工具加载录制的 EIF 数据，模拟运行使用 Mega 能力的 AR 工程。
## 开始之前
* 完成[快速入门](quickstart.html)，了解如何运行包含 Mega 功能的 Unity 应用。
* 了解什么是 [EIF](../../simulation/simulation.html)。
* 学习如何[采集模拟运行数据](../../mega/input-recording.html)。
## 为什么用 session 验证工具模拟运行是个好办法
**远程开发**：无需顶着烈日或严寒驻场，利用 EIF 数据，您在办公室就能开发基于大规模地理空间的 AR 应用。
**跨平台调试**：无需频繁连接各种移动设备，在 Windows PC 上即可模拟手机、头显等不同终端的定位和跟踪效果。
**问题反馈的“金标准”**：一个**能够复现异常的 EIF 文件**，是 EasyAR 团队为您解决定位与跟踪问题的**关键依据**。
> **注意**
尽管 EIF 数据记录得非常精确，模拟效果和实际使用效果可能依然存在差异。
并且模拟数据对现场的覆盖有限，在最终发布前务必进行实地测试。
## 操作步骤
通过以下步骤使用 session 验证工具模拟运行。
### 准备好现场录制的 EIF 文件
根据所选录制格式不同，录制好的EIF数据应为 `.mkveif` 文件（或 `.eif` 文件和 `.eif.json` 文件，这两个文件缺一不可）。
**`.eif` 和 `.eif.json`：**
![旧EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool05.png)
**`.mkveif`：**
![新EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool06.png)
### 对照 Block 稠密模型或全景摆放一些 3D 内容
![摆放3D内容](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera03.png)
### 开启 Session 验证工具
点击场景中的 **AR Session (EasyAR)** > 确认其 **Inspector** 面板上的 **Frame Player** 已经**开启**。
![确认FramePlayer开启](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool03.png)
### 运行
点击工具栏按钮或点击 **Session Validation Tool** 上的运行按钮在 Unity 编辑器上开始运行这个工程。
![运行按钮](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool07.png)
运行后会弹出一个提示框，**这是正常的**，它只是提示现在正在使用 `Frame Player`。
![提示弹窗](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool08.png)
点击工具上的按钮打开 EIF 文件。
![打开EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool09.png)
正常打开后它会自动播放，可以使用工具栏进行暂停/继续等控制，有些新格式的 EIF 也支持进度条跳转。
![控制进度](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool10.png)
运行效果：
若在工具 `EasyAR.Mega.BlockViewer (Dev)` 中加载了 Block 稠密模型，Block 稠密模型也会保持显示。这在进行位置比对或未放置模型的地方查看定位效果的情况下还是有用的。
一般来说可以将工具 `EasyAR.Mega.BlockViewer (Dev)` 关闭（`active` 设成 `false` 或删除场景节点），然后运行看到的就是在现实场景中叠加了虚拟物体的效果。
> **重要事项**
在使用时，你一定会注意到运行时显示在屏幕上或目视前方的诊断信息文字，仔细阅读 [UI 消息输出](../diagnostics/ui-messages.html)，仔细斟酌在开发阶段、测试阶段、应用上线之后应该采取何种配置，以及保留何种控制开关。与 EasyAR 的沟通通常需要提供这些信息，建议多利用而不是立马关闭。
默认设置下，启动后，在第一次定位到 `Block` 之前，整个 `MegaBlocks` 及其子节点的 `active` 都是 `false`，内容不会显示。
![MegaBlock显示状态](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool13.png)
在定位到之后，上述节点的 `active` 会变成 `true`，内容会显示出来并不断更新位置。
![MegaBlock定位到后显示](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool14.png)
如果要改变相关行为，或是更加自由的控制 active 行为，可以参考 [BlockRootController 组件参考](comp-BlockRootController.html) 和 [BlockController 组件参考](comp-BlockController.html)。
## 相关主题
* [session 验证工具](../simulation/tool.html)

---

## ARCore、AR Engine 版本兼容性
- 章节路径: `unity/motion-tracking/3rdparty-compatibility.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/3rdparty-compatibility.html

# ARCore、AR Engine 版本兼容性
本文介绍 EasyAR Sense Unity Plugin 对第三方运动跟踪 SDK 版本的兼容性。
## ARCore 版本兼容性
EasyAR Sense Unity Plugin 集成了 ARCore SDK 1.46.0。
* 使用集成的 ARCore SDK 时：支持至少 ARCore （Google Play Services for AR） 1.46.0 及以上版本。更早版本的 ARCore 服务是否支持需要看 Google 自身的兼容性。
* 使用 AR Foundation 或其它 ARCore SDK 的发布时，ARCore 兼容性将由这些框架决定。
## 华为 AR Engine 版本兼容性
EasyAR Sense Unity Plugin 集成了 AR Engine SDK 3.7.0.3。
* 支持至少 AR Engine 2.18 及以上版本。详细兼容信息建议查阅 AR Engine 官方说明。
EasyAR Sense Unity Plugin 不直接支持华为官方已不再维护的 `Huawei AR Engine Unity SDK` 或是其它第三方发布的类似 SDK。使用 AR Engine 也无需在 Unity 中另行导入这些 SDK。
> **重要事项**
AR Engine 的支持是通过自定义相机实现的。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
## 相关主题
* [运动跟踪简介](../../motion-tracking/intro.html)
* [支持 ARCore 运动跟踪的设备](../../motion-tracking/devices-arcore.html)
* [支持 AR Engine 运动跟踪的设备](../../motion-tracking/devices-arengine.html)
* [AR Foundation 版本兼容性](../fundamentals/arfoundation.html)
* [EasyAR 全局配置参考](../fundamentals/setup-player.html)

---

## ARCoreFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-ARCoreFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-ARCoreFrameSource.html

# ARCoreFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ARCoreFrameSource.html)
>
探索 ARCoreFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-ARCoreFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## AREngineFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-AREngineFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-AREngineFrameSource.html

# AREngineFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.AREngineFrameSource.html)
>
探索 AREngineFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-AREngineFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## ARKitFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-ARKitFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-ARKitFrameSource.html

# ARKitFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ARKitFrameSource.html)
>
探索 ARKitFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-ARKitFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Desired Frame Rate**|期望的相机图像帧率。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## MotionTrackerFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-MotionTrackerFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-MotionTrackerFrameSource.html

# MotionTrackerFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.MotionTrackerFrameSource.html)
>
探索 MotionTrackerFrameSource 组件窗口中的各项属性以自定义相机和运动跟踪参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-MotionTrackerFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Default：使用默认值，实际选择与使用的 AR 功能有关。
* Input：使用指定值。选择 Input 时可选项：
* Continousauto：连续自动对焦模式，图像清晰度高，跟踪效果一般。实际对焦效果取决于设备能力。
* Medium：中等距离定焦模式，图像清晰度一般，跟踪效果较好，实际对焦效果取决于设备能力。|
|**Desired Resolution**|期望的分辨率。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Resolution\_1280：标准分辨率是 1280 x 960 或者 1280 x 720，实际分辨率取决于设备能力。
* Resolution\_640：标准分辨率是 640 x 480 或者 640 x 360，实际分辨率取决于设备能力。|
|**Desired Frame Rate**|期望的相机图像帧率。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Camera\_FPS\_30：设备图像帧率是 30fps，实际帧率取决于设备能力。
* Camera\_FPS\_60：设备图像帧率是 60fps 或者 30fps，实际帧率取决于设备能力。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Desired Min Quality Level*|期望的最低允许的质量级别。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* NotSupported：设备不支持运动跟踪，可能是适配不达标或者尚未适配。
* Bad：设备不完全达标，尺度不稳定，可用于桌面尺度内的小场景等。
* Limited：设备不完全达标，尺度接近准确，可用于房间尺度内的中等场景，类似 AR 游戏、AR 导航等。
* Good：设备达标，尺度准确，可用于建筑物尺度的大型场景，类似 AR 游戏、AR 导航、三维重建等。|
|*Desired Tracking Mode*|期望的跟踪模式。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* VIO：只有跟踪和点击碰撞点云，CPU 和内存占用少，但是不支持平面检测、重定位和锚点。
* SLAM：同时跟踪和建图，支持丢失后的重定位、点击碰撞点云和平面检测，但是没有锚点，不支持实时校正位姿，且 CPU 和内存占用稍高。
* Anchor：同时跟踪和建图，支持丢失后的重定位、点击碰撞点云、平面检测和锚点，但是 CPU 和内存占用最高。
* LargeScale：适用于大场景下，同时跟踪和建图，支持丢失后的重定位、点击碰撞点云、平面检测和锚点。大景深下跟踪更稳定。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## EasyAR Sense Unity Plugin 版本 4 发行说明
- 章节路径: `unity/release-notes/release-notes-v4.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/release-notes/release-notes-v4.html

# EasyAR Sense Unity Plugin 版本 4 发行说明
> **注意**
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
* 🚚 拆分和优化 Nreal（>= 1.6）支持
* 🚚 拆分和优化 AR Foundation（>= 4.1.3）支持
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
* ⬆️ ARCore：在使用 ARCore 的构建中，Gradle 版本必需 >= 5.6.4
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
* ✨ 添加 `ARCoreFrameSource` & `ARKitFrameSource` & `MotionTrackerFrameSource` 以替换 `VIOCameraDeviceUnion`，运行时的策略选择由更灵活的 `ARComponentPicker` 替换
* ✨ 添加 `ARFoundationFrameSource` 以支持 Unity AR Foundation
* ✨ 添加 `HuaweiAREngineFrameSource` 以支持华为 AR Engine
* 🔥 `VIOCameraDeviceUnion` 已经标记为过时，并将在将来的发布中删除
* 🚚 `VideoCameraDevice` 重命名为 `CameraDeviceFrameSource`
* 🚚 `RenderCamera` 被移动到了 `FrameSource` GameObject 上
* 🔧 AR session 中的 `Camera` 会由 `FrameSource` 在运行时进行选择
* 🔧 `MotionTrackerFrameSource` 默认会尝试从服务器更新设备支持列表，超时时间为 2s
* ✨ `ARCoreFrameSource` & `ARKitFrameSource` 获得了可以控制自动对焦开关的能力
* ✨ 优化 AR session 工作量和接口
* ✨ 添加 `ARComponentPicker` 组件来在运行时挑选可用的 frame source 及其它组件
* ✨ 添加 `ARSession.AvailableCenterMode` 以查询在一个 session 中所有可用的中心模式
* ✨ 添加 `ARSession.Origin` 以获取在运动跟踪功能在运行时，相机运动的相对物体
* ✨ 添加 `ARSession.TrackingStatus` 以获取设备运动跟踪质量
* ✨ 添加 `ARSession.State` & `ARSession.StateChanged` 以查询 ARSession 的状态
* ✨ 优化中心模式处理
* 🔧 一个 session 中可用的中心模式将由运行时选择的 frame source 来决定
* 🔧 空间地图可用在所有中心模式下使用
* 🔥 删除 `ARCenterMode.ExternalControl`，其功能被 `FrameSource.IsCameraUnderControl` == `false` 所替代
* 🚚 重命名 `ARCenterMode.WorldRoot` 为 `ARCenterMode.SessionOrigin`
* ✨ 优化初始化过程，尤其是首次使用体验
* ✨ 添加 `EasyARController.Initialize` & `EasyARController.Deinitialize` 接口以在启动后支持手动初始化
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

---

## EasyAR Sense Unity Plugin 发行说明
- 章节路径: `unity/release-notes/release-notes.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/release-notes/release-notes.html

# EasyAR Sense Unity Plugin 发行说明
我们很高兴地宣布 EasyAR Sense Unity Plugin 4000 发布。此版本标志着 EasyAR 具备了完善的 API 和与时俱进的设备支持，同时新版本发布也将比以往更加频繁。
下载 [EasyAR Sense Unity Plugin 4000](https://www.easyar.cn/view/download.html) 以享受这些新功能和改进。
## 历史版本
* [EasyAR Sense Unity Plugin 版本 4 发行说明](release-notes-v4.html)
## 版本 4000.0.1
>
> 发布日期：2025-11-14
>
* 🐛 修复：解决了在启用 minify 打包的 Android 构建中，因缺少静态方法（ `loadLibraries` 、 `setupActivity` ）而可能触发的运行时 `AndroidJavaException` 异常，该错误会导致 EasyAR 无法运行。
## 版本 4000.0.0
>
> 发布日期：2025-10-20
>
从这个版本开始，EasyAR Sense Unity Plugin 将遵循 Unity 所要求的 [包版本控制（使用 Semantic Versioning）](https://docs.unity3d.com/Manual/upm-semver.html) ，因此版本号将与 EasyAR Sense 相异，发布频率也可能不同。该版本插件内包含 EasyAR Sense 4.7.0 正式版。
EasyAR Sense Unity Plugin 4000.0.0 迎来了大幅改变，主要集中在这几方面：
1. Unity 及 AR Foundation 兼容性变化
从这个版本开始，EasyAR Sense Unity Plugin 将只支持 Unity 2021.3 及更新版本，Unity 6 支持也已经完善。同时，AR Foundation 支持已经合并到插件包内，这个版本将只支持 AR Foundation 5 及更新版本，其使用经过大量简化。如果场景中添加了 AR Foundation 的组件，无论运行之后 AR Foundation 是否最终使用，场景配置和脚本代码都可以不变。
2. 与时俱进的头显支持，新增支持多款 OST/VST 头显
经过与行业内多家企业多年的打磨，EasyAR 对头显的支持已经标准化。现在您可以通过 EasyAR Sense Unity Plugin 扩展实现第三方头显设备的支持（可能需要头显厂商提供部分数据接口）。这个版本内置了 Apple Vision Pro 以及 XREAL Air2 Ultra 的支持，同时通过 EasyAR Sense Unity Plugin 扩展包支持 Pico 4 Ultra Enterprise 及 Rokid AR Studio。
同时您也可以从 EasyAR 的一些合作伙伴那里获取其它设备的支持扩展包（比如 Xrany 元霓）。
3. 完善 Unity 组件接口，大幅优化 ARSession 工作流
这个版本是第一个通过 Unity 组件完整封装 EasyAR Sense 功能的版本。ARSession 经过了大量优化和重写，现在您可以轻松实现设备或功能的支持判断，根据具体情况启动或停止 ARSession 以实现运行时切换 ARSession 或不同 AR 功能。同时，您也可以使用 ARSessionFactory 在运行时创建 ARSession 及相关组件。这个版本还添加了惯性导航和 3DoF 相机功能，这些功能主要为 EasyAR Mega 所设计，但也可以单独使用。
4. 新增多个开发及诊断工具
这个版本增加了提供了全新的 EIF 录制和播放功能，虽然 EIF 录制和播放在过去的版本中也能使用，但使用 EIF 从未如此简单。您现在可以在 Unity 编辑器中使用时诊断工具 Session Validaion Tool 直接播放 eif 并驱动您的场景，无论是图像跟踪、空间地图还是 EasyAR Mega，都可以在电脑上还原设备上的运行效果。现在您可以使用运行时诊断面板 EasyAR Diagnostics Panel 在 app 中轻松开启 eif 录制功能，或是随时开关 ARSession 及其组件的关键状态信息显示。同时，这个版本的 sample 已经全部重写，运行 sample 就可以直接看到 ARSession 状态以及录制 eif 的按钮以方便使用。
5. EasyAR Mega 工具全面公开
这个版本集成发布了 Mega Studio 2.12。今后插件的更新将更加频繁，Unity 侧 Mega 工具将逐步合并进插件内部并与插件常规更新合并发布。除了过去预发布版本中的更新之外，这个版本会默认开启惯导支持，进一步大幅拓展 EasyAR Mega 的设备支持。这个版本还包含对最新版本 EasyAR Mega Landmark 服务的支持。使用 EasyAR Mega 可以通过 [EasyAR 网站页面](https://www.easyar.cn/view/apply.html) 进行申请。
详细更新内容如下：
**Unity 及 AR Foundation 兼容性变化：**
* 🔧 Unity：支持 Unity 2021.3 及更新版本（包括 Unity 2022.x/Unity 6.x）
* 🔥 移除对 Unity 2019/Unity 2020 的支持
* 🔥 移除用于 Unity 2019 的 gradle 版本检测
* 🔥 移除用于 Unity 2019 的选项 DisableARCoreAREngine
* ✨ Unity 6：全面支持 Unity 6
* ✨ 支持 URP 17+ 及 Render Graph
* 🐛 已修复：Unity 6 上 ClassLoader 行为变化导致 ARCore 失效
* 🐛 已修复：Render Scale 非 1 时相机渲染失效
* 🐛 Unity 6 自身 BUG：在 iOS/Mac 设备上可以观察到视觉故障和伪影。该问题仅发生在需要获取相机纹理的情况，我们添加了部分缓解措施但无法完全消除。已反馈至 Unity，见 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 。Unity 6.2 以上可以通过设置 Universal Render Pipeline Asset 中的 Render Scale 为 0.96-1.05 以外的数值来规避这个问题。
* 🐛 Unity 6 自身 BUG：Windows DX11 上的渲染效果不正常。我们在 Unity 6.0-6.1 中已添加缓解措施。实测 Unity 6.2 已修复该问题。
* ✨ AR Foundation：支持 AR Foundation 5 及更新版本，大幅简化使用
* ✨ AR Foundation 支持已经合并到插件包内，不再需要单独导入包（特殊需要可以通过配置选项关闭）
* ✨ 支持复用 `Unity.XR.CoreUtils.XROrigin` 作为 ARSession 的原点，支持复用 XROrigin 的 Camera
* ✨ 添加 `Unity XR Auto Switch` 配置选项，默认处理 Unity XR（包含 AR Foundation）物体的切换
* ✨ 通过 EasyAR 菜单创建的 ARSession 自动包含并默认开启 AR Foundation 支持
* ✨ 绝大部分 sample 都已添加 AR Foundation 支持（AR Foundation 本身需要手动导入并正确配置）
* 🔧 ARCore 及 ARKit 可单独控制，且可控制 EasyAR 内置的 ARCore/ARKit 与 AR Foundation 的 ARCore/ARKit 的优先顺序
* 🔥 移除对 AR Foundation 4 的支持
* 🔥 移除对 ARSessionOrigin 的支持，仅支持 XROrigin
* 🔥 移除代理执行 AR Foundation 的 ARCore 安装流程
* ✨ 全面兼容 Input System Package
**与时俱进的头显支持，新增支持多款 OST/VST 头显：**
* 🚀 头戴显示设备接口已稳定，支持第三方接入
* ✨ 支持第三方设备接入（需要头显厂商提供特定数据接口）
* ✨ 支持 XROrigin 及 XR Interaction Toolkit
* ✨ 简化并统一所有头显样例，零代码，并支持功能切换
* ✨ 支持鱼眼相机输入
* ✨ 支持自定义相机输入 3DOF 数据
* ✨ 添加菜单功能：Extensions，整合所有扩展菜单项
* 🐛 修复部分头显运行 DenseSpatialMap 时出现渲染异常
* 🔥 移除 ActionOne 和 BT350 等古早眼镜 sample
* ✨ 内建支持 Apple Vision Pro
* ✨ 支持 Metal、RealityKit 及 Hybrid 模式
* ✨ 支持 visionOS >= 2.0，支持 visionOS 26
* ✨ 内建支持 XREAL Air2 Ultra（需要 XREAL SDK >= 3.1）
* ✨ 不再需要导入单独的支持包
* ⚡ 优化 XREAL 上的运行效果
* 🔥 移除 XREAL Light 支持
* ✨ 通过 EasyAR Sense Unity Plugin 扩展分发 Pico 及 Rokid 等其它设备支持
* ✨ 提供第三方设备接入的参考模板 `com.easyar.sense.ext.hmdtemplate`
* ✨ 支持 Pico 4 Ultra Enterprise（需要 PICO Unity Integration SDK >= 3.1）
* ✨ 支持 Rokid AR Studio（需要 Rokid Unity OpenXR Plugin >= 3.0.3）
* ✨ 这些扩展将支持今后多个版本的 EasyAR Sense Unity Plugin
* ✨ 支持 EasyAR XR License
* 🔧 头显上使用 EasyAR 需要 EasyAR XR License 并保证首次联网（试用需每次联网）
**完善 Unity 组件接口，大幅优化 ARSession 工作流：**
* 🚀 完善 Unity 组件层封装
* ✨ 完善场景组件，提供所有 EasyAR Sense 功能
* 🔥 移除所有通过组件封装的 EasyAR Sense 层接口
* 🔥 移除所有内部接口
* ✨ ARSession：重写并大幅优化工作流
* ✨ 支持在任意时刻启动和停止 session
* ✨ 支持 session 自动启动控制
* ✨ 支持不黑屏切换 session 功能和输入源
* ✨ 简化设备支持判断，以一致接口提供
* ✨ 启动时更新 MotionTracker、ARCore、AR Engine 的设备支持列表
* ✨ 支持设备列表更新后 session 自动重启
* ✨ 支持获取详细 session 损坏信息
* ✨ 添加 session 内部状态自检
* 🔥 移除 ARComponentPicker，其功能由其余 session 流程替代
* 🔥 禁止多个 ARSession 同时运行
* ✨ ARSessionFactory：提供运行时创建 ARSession 及相关组件的功能
* ✨ 支持通过 ARSessionFactory 运行时创建与编辑器菜单相同的 session
* ✨ 添加 Frame Source 排序功能（含菜单项）
* ✨ FrameSource：添加惯导和 3DoF 支持
* ✨ 添加 InertialCameraDeviceFrameSource 用于支持惯性导航
* ✨ 添加 ThreeDofCameraDeviceFrameSource 用于支持 3DoF 的相机
* ✨ 添加菜单功能：Frame Source by Transform Type，提供所有内置 FrameSource 的列表
* ⚡ 优化 Inspector 选项
* ✨ 其它接口调整及功能更新
* ✨ 添加使用 Texture2D 创建 ImageTarget 的功能
* ✨ 添加 ImageMaterial 用于渲染 Image 类型的数据（相机图像或 Target 图像等）
* ✨ 添加 ActiveController 用于控制 GameObject 的 active，统一相关控制逻辑
* ✨ 添加在桌面上模拟屏幕旋转的功能
* ✨ 添加 XROriginChildController，控制 Session 原点下物体的行为
* 🔥 移除 WorldRootController
* 🔧 稀疏空间地图接口拆分成 Builder 和 Tracker 两个不同功能组件
* 🔧 调整 EasyARController，提供应用/系统级静态功能
* 🔧 统一 Target 组件接口
* 🔧 统一服务访问数据的接口
**新增多个开发及诊断工具：**
* 🚀 添加编辑时诊断工具：Session Validaion Tool
* ✨ 简化在任意场景中播放 eif
* ✨ 支持控制 eif 播放流程
* ✨ 支持控制 session 流程
* 🚀 添加运行时诊断面板：EasyAR Diagnostics Panel
* ✨ 添加 Developer Mode 开关，默认点击屏幕 8 次开启和关闭 Diagnostics Panel，简化线上 app 录制 eif 和问题反馈
* ✨ 支持自定义 Developer Mode 开关，使用自定义交互开关 Diagnostics Panel
* ✨ 支持控制 eif 录制
* ✨ 支持控制 session 信息显示
* ✨ 支持控制 eed 录制
* ✨ 添加全新的 EIF 录制和播放功能
* ✨ FrameRecorder 会自动组装进 ARSession，不再需要手动选择
* ✨ FrameRecorder 会默认自动生成文件名以支持无脚本使用
* ✨ FramePlayer 使用新格式录制的数据支持播放跳转及速度调节，文件体积降低
* 🔧 支持在电脑上使用 eif 驱动场景和 AR 功能（非新功能）
* ✨ 添加 DiagnosticsController，统一和优化诊断功能
* ✨ 添加信息分级显示及控制，默认所有错误及警告信息都会通过 UI 展示
* ✨ 添加显示 ARSession 及其组件的关键状态信息的功能，默认会通过 UI 展示并每帧更新
* 🔧 使用诊断功能简化问题反馈信息的获取
* 🔥 删除 GUIPopup
* 🔧 优化异常状态行为及错误信息展示
* 🔧 优化无可用 frame source 时的错误信息
* 🔧 URP 环境使用 EasyAR 而非 AR Foundation 或头显渲染相机图像时，未正确配置 RendererFeature 会报错并中断 ARSession 执行
* 🔧 修改 Origin 默认的 Active 控制策略，在跟踪丢失时内容贴屏而非消失
* 🔧 自定义相机或头显上使用试用产品时，到达限制时间将隐藏所有内容以避免效果误判
* 🔧 优化配置页面内容和选项
* ✨ 支持选择 EasyAR Sense 库的变种
* 🔒 应用权限部分除相机权限外，其余权限不再可改，由 EasyAR Sense 库变种及 Mega 是否启用而决定
* 🔧 功能及服务器配置按 EasyAR 功能分组
* 🔧 集中管理第三方 AR SDK 配置
* 🔧 集中管理针对 Unity 的 Workaround 配置
**EasyAR Mega 工具全面公开：**
* 🚀 全面公开，同步更新
* ✨ 集成发布 Mega Studio 2.12
* 🔧 Unity 侧 Mega 工具将逐步合并进插件内部，今后仍将只提供最新版本的整合包，但将与 EasyAR Sense Unity Plugin 常规更新合并发布
* 🔧 EasyAR Mega 仍需通过 [EasyAR 网站页面](https://www.easyar.cn/view/apply.html) 申请并通过后才能使用
* ✨ 新增支持 EasyAR Mega Landmark
* ✨ 新增支持 5DOF 惯导并默认开启，进一步大幅拓展 EasyAR Mega 的设备支持
* ✨ 新增支持使用 API Token 访问 Mega 服务
* 🔧 优化 Mega 效果及开发体验（包含在过去更新的 4.7.x 版本内）
* ✨ 支持 3DOF 纯旋转模式和 0DOF 模式（默认未启用）
* ✨ 添加 EditorCameraDeviceFrameSource 用于编辑器诊断，避免由于不完整的复制 sample 导致手机上错误运行
* ✨ 使用 Mega时录制老版本 eif 数据，FrameRecorder 将自动生成 .eif.json 文件
* 🔧 使用 LocationInputMode 替代远程调试的退化选项
* 🔧 拆分无跟踪模式为独立组件，通常不再需要使用和关注
* 🔧 添加 BlockRootSource 选项，默认配置下忘记设置 BlockRoot 将报错
* 🔧 调整定位到多 block 时的默认行为，确保多 block 不会被默认使用
* 🔧 调整部分接口命名
* 🔧 在 Session 包含 Mega 但无法使用时抛出更明确的异常
* 🔧 调整 Mega 支持的 MotionTracker 最低 QualityLevel 为 Limited
* 🐛 修复 CloudLocalizerStatus.WakingUp 状态未正确转义导致运行报错
* 🔧 部分优化及修改见 EasyAR Sense 的更新日志
**Sample 重写及优化：**
* ✨ 重写所有 sample
* ✨ 兼容不同 Input System 配置
* ✨ 兼容 URP17+
* ✨ 兼容使用 AR Foundation
* 🔧 兼容不使用 AR Foundation
* 🔧 保留少量不含 AR Foundation 支持的 sample
* ⚡ 优化脚本及接口调用
* 🚚 部分 sample 已重命名
* 🔧 替换 sample 内模型和视频等资源
* ⚡ 减少 streaming assets的使用，仅在展示特定功能的 sample 中使用并导入
* ✨ 使用 Texture2D 创建 ImageTarget
* ✨ 增加新功能和接口演示
* ✨ 添加 Workflow\_ARSession sample，用于学习 session 基础流程和设备支持等
* ✨ 添加 Workflow\_FrameSource\_ExternalImageStream sample，以视频作为自定义相机（不能用于头显）
* ✨ 添加 Combination\_BasedOn\_MotionTracking sample，用于学习运动跟踪可用时各种功能的使用、切换以及 AR Foundation 切换
* ✨ 添加 Combination\_BasedOn\_AppleVisionPro sample，用于展示 Apple Visio Pro 上各种功能的使用和切换
* ✨ 添加 Combination\_BasedOn\_Xreal sample，用于展示 XREAL 设备上各种功能的使用和切换
* ✨ 添加多个 Mega sample（包含在过去更新的 4.7.x 版本内）
* ✨ 添加 Workflow\_FrameSource\_CameraDevice 中切换相机尺寸和 torch 模式的功能
* 🔥 移除单独的 AR Foundation sample，其功能已经包含在其它 sample 中
* 🔥 移除 FrameRecording sample，其功能已经包含在其它 sample 中
* 🔥 移除 MotionTracking\_Fusion sample，其功能已经包含在 Combination\_BasedOn\_MotionTracking 中
* 🔥 移除 SurfaceTracking\_ImageTarget sample，功能组合仍可用轻松实现
* 🔥 移除 Camera\_CustomCamera sample，如有需要仍可自行实现
* 🔥 移除 ActionOne 和 BT350 等古早眼镜 sample
* ✨ 简化 eif 录制和播放使用
* ✨ 所有 sample 均添加 eif 录制按钮，录制的 eif 文件可在编辑器内使用
* ✨ 重写 launcher，加入 sample 说明
* 🐛 修复通过 launcher 加载 sample 场景偏暗的问题
**EasyAR 及第三方 AR 功能集成：**
* ⬆️ 更新 EasyAR Sense 到 4.7.0 正式版
* ⬆️ 更新 EasyAR AR Engine Interop
* ⬆️ 更新 ARCore SDK 到 1.46.0
* 🔧 在部分无法合理运行 AR Engine 的手机上禁用 AR Engine
* 🐛 修复 Unity 6 上 ClassLoader 行为变化导致 ARCore 失效

---

## FramePlayer 组件参考
- 章节路径: `unity/simulation/comp-FramePlayer.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/comp-FramePlayer.html

# FramePlayer 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.FramePlayer.html)
>
探索 FramePlayer 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/comp-FramePlayer.png)
默认条件下组件截图。
|属性|描述|
|**File Path Type**|路径类型。选项：
* Absolute：绝对路径。
* PersistentDataPath：Unity 沙盒路径 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|**File Path**|文件路径。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## FrameRecorder 组件参考
- 章节路径: `unity/simulation/comp-FrameRecorder.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/comp-FrameRecorder.html

# FrameRecorder 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.FrameRecorder.html)
>
探索 FrameRecorder 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/comp-FrameRecorder.png)
默认条件下组件截图。
|属性|描述|
|**Auto Start**|session 启动后自动启动录制。|
|**Format**|录制的格式。选项：
* Auto：自动选择可用的格式。
* H264：H264。MacOS、iOS、Android上支持。
* Obsolete：原始 EIF 格式，在Windows上只支持该格式。|
|**Auto File Path**|自动生成文件路径。文件将被存储在 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|*Type*|Auto File Path 未选中时显示。
路径类型。选项：
* Absolute：绝对路径。
* PersistentDataPath：Unity 沙盒路径 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|*Folder Path*|Auto File Path 未选中时显示。
文件夹路径。|
|*File Name*|Auto File Path 未选中时显示。
文件名（不含扩展名）。|
|**Events**|可注册事件。|
|*OnReady*|可以开始录制的事件。|
|*OnRecording*|录制启动的事件。|
|*OnFinish*|录制结束的事件。|

---

## 在 Unity 中使用 EIF 文件模拟运行
- 章节路径: `unity/simulation/playback.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/playback.html

# 在 Unity 中使用 EIF 文件模拟运行
本文介绍了如何在 Unity 中使用 EIF 文件进行模拟运行，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
## 开始之前
模拟运行使用 EIF 文件作为输入，因此在开始之前需要先录制 EIF 文件：
* 参考 [录制 EIF 文件](recording.html) 录制 EIF 文件
另外还需要了解：
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 通过 [访问 session 中的 AR 功能组件](../fundamentals/session-components.html) 了解如何访问录制组件
## 启用 session 的 frame player
[ARSession.AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 提供了多种方式来配置 session 组件的组合方式，其中一种方式是设置 [AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource) 为 [FramePlayer](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_FramePlayer) 来启用 frame player 组件，从而可用使用 EIF 文件进行模拟运行。
例如：
```
Session.AssembleOptions.FrameSource = AssembleOptions.FrameSourceSelection.FramePlayer;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Assemble Options` 中对应的选项：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-assemble.png)
这样 session 启动时就会启用 frame player 组件，而不会选择其它 frame source 组件。
使用 frame player 播放 EIF 文件的效果如下面这个视频所示：
>
> 这段视频展示了使用 frame player 在电脑上运动稠密空间建图的效果。视频左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
在播放 EIF 文件的过程中，session 中的各个 AR 功能组件都可以正常工作，场景中的内容和交互逻辑也可以正常工作，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
> **提示**
在电脑上使用 frame player 播放 EIF 看到的效果，与录制 EIF 文件时手机上的效果是基本一致的。
> **重要事项**
场景内播放 EIF 时的运行效果与录制时使用的设备以及设备上当时选用的 frame source 有关，因此在录制 EIF 文件时，建议使用和目标设备相同或接近的设备进行录制，从而保证播放时的效果与目标设备上的效果一致。同时需要重点关注录制场景中的运动跟踪功能是否启用，如果录制时未启用运动跟踪功能，那么播放时也无法启用运动跟踪功能，依赖运动跟踪的 AR 功能（比如稠密空间地图、Mega等）也无法和设备上工作一致。
## 在 session 启动时播放
默认情况下，session 启动时 frame player 会自动开始播放 EIF 文件，但是在播放前需要指定 EIF 文件路径，可以通过 [FramePlayer.FilePathType](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_FilePathType) 和 [FramePlayer.FilePath](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_FilePath) 属性来设置。
例如：
```
var player = Session.GetComponent<FramePlayer>();
player.FilePathType = WritablePathType.Absolute;
player.FilePath = path;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Frame Player` 组件中的对应选项：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-file.png)
如果未指定文件，或文件路径无效，session 启动时 frame player 会启动失败，并输出错误日志：
>
> File not found:
>
## 手动播放
如果要手动控制播放时机，可以在 session 启动前将 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 设为 `false`，
```
Session.GetComponent<FramePlayer>().enabled = false;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中取消 `Frame Player` 组件的 `Enabled` 勾选：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-auto-disable.png)
在需要播放时，使用 [Play()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Play) 来启动播放。
例如：
```
if (Session.Assembly.FrameSource is FramePlayer player)
{
player.Play();
}
```
每次调用 [Play()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Play) 都会停止前一次播放后（如果之前播放过）从头开始播放。
> **小心**
播放新数据时，场景中原本的数据不会被清空。AR 组件的状态也不会被重置，它们会表现得像是摄像头数据突然从上一个数据停止的地方跳到新数据开始的地方一样。
虽然这对一部分功能没太大影响，但是对于依赖运动跟踪的功能（比如稠密空间地图、Mega等）来说，可能会导致功能状态异常，从而影响运行效果。因此建议在播放新数据前，重新启动 session 来重置所有 AR 组件的状态。
## 暂停和继续
使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 来控制播放的暂停和继续。
例如，设置 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `false` 来暂停播放：
```
player.enabled = false;
```
播放暂停后，所有 AR 功能组件都会暂停工作。场景中的内容和交互逻辑不一定会停止，与内容本身有关。继续播放后，AR 功能组件会从暂停的位置继续工作。
## 停止播放
使用 [Stop()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Stop) 来停止播放。
```
player.Stop();
```
播放停止后，所有 AR 功能组件都会停止工作。场景中的内容和交互逻辑不一定会停止，与内容本身有关。
## 跳转到指定时间点播放（seek）
使用 [Seek(double)](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Seek_System_Double_) 来跳转到指定时间点播放。
例如，跳转到 5 秒后播放：
```
player.Seek(player.Time + 5);
```
> **注意**
跳转之后可能不是从精确的时间点开始播放，具体取决于 EIF 文件的编码方式和关键帧间隔。
并不是所有 EIF 文件都支持跳转播放，可以使用 [IsSeekable](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_IsSeekable) 属性来检查当前播放的 EIF 文件是否支持跳转播放。
> **注意**
只有使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制且正常调用停止录制的 EIF 文件才支持跳转播放。如果 EIF 文件不支持跳转播放，调用 [Seek(double)](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Seek_System_Double_) 不会有任何效果。
## 播放速度控制
使用 [Speed](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Speed) 属性来控制播放速度。
例如，设置播放速度在原来的基础上增加 0.1 倍：
```
player.Speed += 0.1;
```
并不是所有 EIF 文件都支持播放速度控制，可以使用 [IsSpeedChangeable](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_IsSpeedChangeable) 属性来检查当前播放的 EIF 文件是否支持播放速度控制。
> **注意**
只有使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制且正常调用停止录制的 EIF 文件才支持播放速度控制。如果 EIF 文件不支持播放速度控制，设置 [Speed](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Speed) 不会有任何效果。
## 相关主题
* 尝试 [使用 session 验证工具](tool.html)，这个工具包含了一个简单的 EIF 播放器，可以更加快速地使用 EIF 文件进行模拟运行

---

## 在 Unity 中录制 EIF 文件
- 章节路径: `unity/simulation/recording.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/recording.html

# 在 Unity 中录制 EIF 文件
本文介绍了如何在 Unity 中录制 EIF 文件，以便用于模拟运行。
## 开始之前
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 通过 [访问 session 中的 AR 功能组件](../fundamentals/session-components.html) 了解如何访问录制组件
## 启动录制
使用 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `true` 来启动录制，例如：
```
if (Session.State >= ARSession.SessionState.Ready && Session.Assembly.FrameRecorder.OnSome)
{
var frameRecorder = Session.Assembly.FrameRecorder.Value;
frameRecorder.enabled = true;
}
```
需要注意的是，这里需要先判断 [ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 是否存在。
> **注意**
[ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 在少数情况下，比如使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html) 时是不能使用的。
[FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 默认值为 `false`，表示录制处于关闭状态，即使在编辑器中手动配置也是无效的。
录制在 session 运行过程中，[FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) >= [FrameRecorder.RecorderStatus.Ready](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Ready) 时才会开始。
如果 [FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) < [FrameRecorder.RecorderStatus.Ready](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Ready)，可以使用 [OnReady](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnReady) 事件来等待录制准备就绪。
```
Session.GetComponent<FrameRecorder>().OnReady.AddListener(() => {
// 可以开始录制
});
```
可以使用 [OnRecording](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnRecording) 事件来确认启动成功：
```
frameRecorder.OnRecording.AddListener((file) =>
{
Debug.Log($"Recording started: {file}");
});
```
启动失败没有事件触发，但可以通过检查 [FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) 是否为 [Error](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Error) 来确认。
> **重要事项**
场景内播放 EIF 时的运行效果与录制时使用的设备以及设备上当时选用的 frame source 有关，因此在录制 EIF 文件时，建议使用和目标设备相同或接近的设备进行录制，从而保证播放时的效果与目标设备上的效果一致。同时需要重点关注录制场景中的运动跟踪功能是否启用，如果录制时未启用运动跟踪功能，那么播放时也无法启用运动跟踪功能，依赖运动跟踪的 AR 功能（比如稠密空间地图、Mega等）也无法和设备上工作一致。
## 停止录制
使用 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `false` 来停止录制，例如：
```
frameRecorder.enabled = false;
```
该操作会立即停止录制，并阻塞直至文件写入完成。
> **重要事项**
必须调用停止录制，否则录制文件写入不完整，会导致部分功能或整个文件无法使用：
* 录制格式为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 时，EIF 文件无法跳转到指定的时间点进行播放（seek），只能从头播放
* 录制格式为 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 时，EIF 文件无法使用
## 文件存储和导出
可以使用 [OnRecording](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnRecording) 事件来获取录制文件的完整真实路径：
```
frameRecorder.OnRecording.AddListener((file) =>
{
Debug.Log($"Recording started: {file}");
});
```
默认配置下，录制文件会存储在应用的持久化数据路径下，可以通过 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) 来访问该路径。
可以通过 [FrameRecorder.Configuration](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Configuration).[FilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_FilePath) 来修改录制文件的存储路径。该路径必须在录制启动前设置，且需要关闭 [AutoFilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_AutoFilePath) 后才能生效。需要提前创建好目录。
> **重要事项**
必须保证录制文件的存储目录存在且应用可写入，否则录制启动时会失败。
例如，下面的代码展示了如何将录制文件存储在自定义目录下，并根据 session 使用的 FrameSource 类型和当前时间生成文件名：
```
if (!Directory.Exists(SavePath))
{
Directory.CreateDirectory(SavePath);
}
var frameRecorder = Session.Assembly.FrameRecorder.Value;
frameRecorder.Configuration.AutoFilePath = false;
frameRecorder.Configuration.FilePath.Type = WritablePathType.Absolute;
frameRecorder.Configuration.FilePath.FolderPath = SavePath;
frameRecorder.Configuration.FilePath.FileName = ARSessionFactory.DefaultName(Session.Assembly.FrameSource.GetType()).Replace(" ", "") + DateTime.Now.ToString("\_yyyy-MM-dd\_HH-mm-ss.fff");
frameRecorder.enabled = true;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中取消 Frame Recorder 的 `Auto File Path` 勾选之后配置：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-filepath.png)
> **提示**
通过 [FrameRecorder.RecordingConfiguration.FilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_FilePath) 可以修改文件的存储目录和文件名（不含扩展名），文件扩展名会根据录制格式自动添加。
* 录制格式为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 时，文件扩展名为 `.mkveif`
* 录制格式为 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 时，文件扩展名为 `.eif`
如果文件存储在应用的持久化数据路径或其他应用私有路径下，可以通过以下方式将文件导出到电脑上：
* Android 平台可以通过 USB 连接电脑后，使用 `adb pull` 或其他方式将文件导出到电脑上，文件通常在 `/sdcarad/Android/data/<app package name>/files` 下面。
* iOS 平台可以通过 Xcode 的 Devices 窗口将文件导出到电脑上，或者通过 iTunes 或 Finder 文件共享访问应用的私有目录。
* 通过代码将文件存储到公共目录下，比如 Android 的下载目录或 iOS 的相册等。
> **注意**
对于 iOS 应用，如果希望通过 iTunes 或 Finder 文件共享访问应用的私有目录，在打包前需要在 XCode 项目的 `Info.plist` 中添加 `UIFileSharingEnabled` 键，并将值设置为 `YES`：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/ios-plist-uifilesharingenabled.png)
添加之后显示的文字与添加的字符串不同，这是正常的。
## 更换录制格式
通过 [FrameRecorder.Configuration](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Configuration).[Format](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_Format) 改变录制格式，必须在录制启动前设置。
例如，下面的代码展示了如何将录制格式强制设置为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264)：
```
frameRecorder.Configuration.Format = FrameRecorder.InternalFormat.H264;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Format`：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-format.png)
> **注意**
[H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 在部分设备（比如 Windows）上无法使用，一般推荐使用 [Auto](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Auto)，这样会根据设备自动选择合适的格式。
> **注意**
在 XREAL 上，使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制数据无法用来模拟运行，用于且只用于反馈问题。
* 模拟运行时，应使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制数据。
* 反馈问题时，应使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制数据。
可以使用 [RecordingFormat](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_RecordingFormat) 来查看当前录制格式。
## 在 session 启动时自动录制
在 session 启动前设置 [AutoStart](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_AutoStart) 为 `true`，可以在 session 启动时启动录制，例如：
```
frameRecorder.AutoStart = true;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中勾选 Frame Recorder 的 `Auto Start`：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-autostart.png)
> **注意**
编辑器上修改 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 是无效的。
## Mega 可用的数据
在使用 Mega 时，对 EIF 及相关文件内容有一些特殊要求，在老版本的 Unity 插件中未集成相关功能，那些版本录制的数据不能用于 Mega。
以下这些情况录制的数据可以用于 Mega：
* 使用 Unity 插件 4000 或更高版本录制的数据
* 使用 Mega Toolbox 录制的数据
* 如果数据是使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制的，比如文件 `x.eif`，需要在文件相同目录同时存在 `x.eif.json` 文件才能使用
以下这些情况录制的数据不能用于 Mega：
* 使用 Unity 插件 4.6 或更低版本录制的数据
* 使用原生 EasyAR Sense，且未添加与 Unity 插件中相同内容的数据
另外，虽然 Mega 可以不使用运动跟踪进行工作，但运行效果是不一样的。建议在录制 EIF 文件时启用运动跟踪功能，从而保证播放时的效果能符合大部分使用场景。
## 后续步骤
* 尝试 [使用 EIF 文件模拟运行](playback.html)
* 尝试 [使用 session 验证工具](tool.html)

---

## Unity AR 模拟运行
- 章节路径: `unity/simulation/simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/simulation.html

# Unity AR 模拟运行
Unity 的 AR 开发有时受限于设备能力差异，经常需要打包到手机上进行测试。在使用一些与真实环境有关的功能时（比如稀疏空间地图或 Mega），AR 功能需要真实的环境才能使用，这往往需要在特定的环境驻场开发和测试。为了提高开发效率，EasyAR 提供了模拟运行的功能，可以在 Unity 编辑器中模拟 AR 设备的工作效果。
基于 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html)，Unity 中可以使用这些功能：
* [录制 EIF 文件](recording.html)
在 Unity 中录制 EIF 文件，以便用于模拟运行。
* [使用 EIF 文件模拟运行](playback.html)
在 Unity 中使用 EIF 文件进行模拟运行，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
* [使用 session 验证工具](tool.html)
使用 session 验证工具，在编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
相关功能组件包括：
* [FrameRecorder 组件](comp-FrameRecorder.html)
该组件提供了录制 EIF 的功能。
* [FramePlayer 组件](comp-FramePlayer.html)
该组件提供了使用 EIF 文件进行模拟运行的功能。
* [DiagnosticsController 组件](../diagnostics/comp-DiagnosticsController.html)
该组件是诊断系统的核心控制器，提供了 session 验证工具。

---

## 使用 session 验证工具
- 章节路径: `unity/simulation/tool.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/tool.html

# 使用 session 验证工具
本文介绍了如何使用 session 验证工具，在编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
## 开始之前
模拟运行使用 EIF 文件作为输入，因此在开始之前需要先录制 EIF 文件：
* 参考 [录制 EIF 文件](recording.html) 录制 EIF 文件
另外还需要了解：
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
## session 验证工具
session 验证工具用于帮助开发者在 Unity 编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
默认情况下可以在 `AR Session (EasyAR)` 物体的 `Inspector` 窗口中看到 session 验证工具，它是 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 编辑器的一部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool.png)
点击工具右上角 `↗` 按钮可以将工具弹出为独立窗口，方便查看和操作，在窗口关闭或按下 `↘` 按钮后，工具会重新在 `Inspector` 窗口中显示。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-window.png)
工具运行时的效果如下面这个视频所示：
>
> 这段视频展示了 session 验证工具的使用效果，录制于 Unity 的 play 模式。视频上半部分左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图，视频下半部分是 session 验证工具。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
> 工具左边偏上部分展示了 EIF 播放的进度条，可以看到它在随着播放进度不断变化。工具左边偏下部分展示了当前 session 的状态。工具右边展示了 session 的组件和可用中心模式。
>
> 在场景中，可以看到同时工作的 3 个 AR 功能：
>
>
> 运动跟踪：它是由 frame player 提供的，蓝色球体是 XR Origin，蓝色锥体代表用户位置。
>
> 稠密空间建图：可用看到随着视角的移动，半透明的网格模型在不断生成。
>
> 稀疏空间跟踪：视频中在被跟踪的是一棵圣诞树，叠加的虚拟物体是浅蓝色点云。
>
>
## 启动工具
点击工具顶部的 `▶` 按钮即可启动工具。按下这个按钮的效果与直接按下 [Unity 工具栏](https://docs.unity3d.com/Manual/Toolbar.html) 的 `▶` 按钮是一样的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-run.png)
如果工具已经启动，则按钮会变为 `■`，点击即可停止工具。
当工具以独立窗口展示时，`▶` 按钮右边的选择框可以选择工具使用的 session 物体，如果窗口被重置导致 session 丢失，可以从这里重新选择。
## 控制 EIF 播放
要使用工具的 EIF 播放功能，需要在运行前勾选工具的 `Frame Player` 选项，这时工具会托管 session 组装过程中 frame source 的选择，无论 [AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource) 设置为何种值，都会启用 frame player 组件。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-player-enable.png)
因此，运行时会有弹窗提示，说明当前 session 所使用的 frame source 已被工具托管：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-notice.png)
> **注意**
工具只会在 Unity 编辑器上托管组装过程中 frame source 的选择，在应用打包运行时该选项没有任何影响。
正常运行时，EIF 播放控制功能会显示在工具的上方图中框出的部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-player.png)
可以通过这些按钮控制 EIF 文件的播放：
* `▶`：播放，从暂停或停止状态恢复播放
* `▮▮`：暂停
* `■`：停止
* `▮◀`：跳到 5 秒之前（文件支持时）
* `◀◀`：降低播放速度（文件支持时）
* `▶▶`：提高播放速度（文件支持时）
* `▶▮`：跳到 5 秒之后（文件支持时）
* `▲`：打开文件
* 进度条：点击可以跳转播放位置（文件支持时）
可以在播放的同时调整优化场景中的内容和交互逻辑，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
> **注意**
播放新数据和跳转播放时，场景中原本的数据不会被清空。AR 组件的状态也不会被重置，它们会表现得像是摄像头数据突然从上一帧数据跳到新数据一样。
虽然这对一部分功能没太大影响，但是对于依赖运动跟踪的功能（比如稠密空间地图、Mega等）来说，可能会导致功能状态异常，从而影响运行效果。
## 控制 session 工作流
使用工具的 session 工作流控制功能，需要在运行前勾选工具的 `Session Workflow` 选项，该选项是默认勾选的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-enable.png)
正常运行时，session 工作流控制功能会显示在工具的播放控制下方图中框出的部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-workflow.png)
在整块区域的上方，展示了 [EasyARController.IsReady](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_IsReady) 和 [ARSession.State](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_State) 两个状态信息。
在整块区域的下方，提供了这些按钮来控制 session 的工作流：
* `Initialize`：初始化 session，可以选择使用 `Project Settings` 中配置的 license key 或手动输入 license key
* `Assemble`：组装但不启动 session
* `StartSession (Assembled)`：启动已组装的 session
* `StartSession`： 组装并启动 session
* `StopSession`：停止 session
* `StopSession (keep image)`：停止 session，但保留图像背景
* `Deinitialize`：反初始化 session
> **注意**
由于这些控制功能直接调用了 [ARSession](../../../api/unity/easyar.ARSession.html) 和 [EasyARController](../../../api/unity/easyar.EasyARController.html) 的相关方法，因此可以通过这些按钮来验证 session 状态变化对内容的影响，但同时需要注意如果在应用脚本中也调用了类似方法，应用的运行流程可能超出应用本身的预期。
## 控制 session 组件
使用工具的 session 组件控制功能，需要在运行前勾选工具的 `Session Workflow` 选项，该选项是默认勾选的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-enable.png)
正常运行时，session 组件控制会显示在工具的下方或右方图中框出的部分，具体位置视窗体宽度而变：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-assembly.png)
这块区域显示的内容与具体的 session 有关，比如上图使用的 session 中包含了图像跟踪、稠密空间建图和稀疏空间跟踪三种功能组件，因此工具中显示了这三种功能的控制选框。
一般来说，这块区域会显示 session 中所有可用的 AR 功能组件，并提供这些组件的启用/禁用（[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html)）控制，包括：
* AR Session：控制 session 本身的启用/禁用
* Image Renderer：控制物理相机图像渲染的启用/禁用
* Camera：控制虚拟摄像机的启用/禁用
* Frame Source：控制 frame source 的启用/禁用，只有未启用 frame player 时才可控制，启用 frame player 时，功能控制由 EIF 播放控制部分替代
* Frame Filter：控制具体 AR 功能的启用/禁用
* Frame Recorder：控制录制 EIF 组件的启用/禁用，只有未启用 frame player 时才可见，启用 frame player 时，该组件不会被组装进 session
同时区域内还会显示 session 可用的中心模式和 [session 报告](../fundamentals/session-report.html)。
> **注意**
工具中展示的可用中心模式和 session 报告是编辑器下运行的结果，实际设备上运行时会不同。
## 相关主题
* 尝试 [使用 EIF 文件模拟运行](tool.html)，通过脚本控制 EIF 文件的播放
* 尝试在脚本中 [控制 session 执行](../fundamentals/session-ctrl.html)
* 尝试在脚本中 [访问 AR 功能组件](../fundamentals/session-components.html)
* 尝试在脚本中 [获取 session 的运行结果](../fundamentals/session-output.html)
* 尝试在脚本中 [初始化](../fundamentals/initialization.html)
* 尝试在脚本中 [获取 session 报告并判断设备支持](../fundamentals/session-assemble.html)
