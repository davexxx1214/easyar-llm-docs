---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-device-frame-source.html
---

创建图像和设备运动数据输入扩展 | EasyAR 文档
**
##### Table of Contents
**
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
`public class MyFrameSource : ExternalDeviceMotionFrameSource
{
}
`
```
在创建头显扩展时，可以使用 `com.easyar.sense.ext.hmdtemplate` 模板，在模板基础上进行修改。这个模板在从 EasyAR 网站下载获得的 Unity 插件压缩包内。
## 设备定义
重写 [IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD) 来定义设备是否是头显。
例如，在头显上设为 true。
```
`public override bool IsHMD { get =&gt; true; }
`
```
重写 [Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display) 来定义设备的显示。
例如，在头显上默认的显示 [Display.DefaultHMDDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultHMDDisplay) 信息，这会定义显示旋转为 0。
```
`protected override IDisplay Display =&gt; easyar.Display.DefaultHMDDisplay;
`
```
## 可用性
重写 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 来定义设备是否可用。
例如，[RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`protected override Optional&lt;bool&gt; IsAvailable =&gt; Application.platform == RuntimePlatform.Android;
`
```
如果 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 在 session 组装时无法判断，可以重写 [CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程来阻塞组装过程，直到确定是否可用为止。
## session 原点
重写 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 来定义设备 SDK 定义的原点类型。
如果 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom)，还需要重写 [Origin](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_Origin) 。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`protected override DeviceOriginType OriginType =&gt;
#if EASYAR\_HAVE\_ROKID\_UXR
hasUXRComponents ? DeviceOriginType.None :
#endif
DeviceOriginType.XROrigin;
`
```
## 虚拟摄像机
如果 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom) 或 [None](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_None)，需要重写 [Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera) 来提供虚拟摄像机。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`protected override Camera Camera =&gt; hasUXRComponents ? (cameraCandidate ? cameraCandidate : Camera.main) : base.Camera;
`
```
## 物理相机
使用 [DeviceFrameSourceCamera](../../../api/unity/easyar.DeviceFrameSourceCamera.html) 类型重写 [DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 以提供设备物理相机信息。这个数据会在输入相机帧数据时使用。[CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须完成创建。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`private DeviceFrameSourceCamera deviceCamera;
protected override List&lt;FrameSourceCamera&gt; DeviceCameras =&gt; new List&lt;FrameSourceCamera&gt; { deviceCamera };
{
var imageDimensions = new int[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetImageDimensions(imageDimensions);
size = new Vector2Int(imageDimensions[0], imageDimensions[1]);
deviceCamera = new DeviceFrameSourceCamera(CameraDeviceType.Back, 0, size, new Vector2(50, 50), new DeviceFrameSourceCamera.CameraExtrinsics(Pose.identity, true), AxisSystemType.Unity);
started = true;
}
`
```
重写 [CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 来提供相机帧开始输入的标识。
例如：
```
`protected override bool CameraFrameStarted =&gt; started;
`
```
## session 启动和停止
重写 [OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_) 然后做 AR 独有的初始化工作。需要确保先调用 base.OnSessionStart。
例如：
```
`protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
StartCoroutine(InitializeCamera());
}
`
```
这里是适合打开设备相机（比如 RGB 相机或 VST 相机等）的位置，尤其是如果这些相机没有被设计成要一直打开时。同时这里也是适合获取整个生命周期内不会变化的标定数据的位置。有时在这些数据可以被获取前可能需要等待设备准备好或等待数据更新。
同时，这里也是一个适合启动数据输入循环的位置。也可以在 [Update()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) 或其它方法中写这个循环，尤其是当数据需要在 Unity 执行顺序的某个特殊时间点获取的时候。在 session 准备好（ready）之前不要输入数据。
如果需要，也可以忽略启动过程并在每次更新时做数据检查，这完全取决于具体需求。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`private IEnumerator InitializeCamera()
{
yield return new WaitUntil(() =&gt; (RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() &gt;= RokidTrackingStatus.Detecting &amp;&amp; (RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() &lt; RokidTrackingStatus.Tracking\_Paused);
var focalLength = new float[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetFocalLength(focalLength);
var principalPoint = new float[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetPrincipalPoint(principalPoint);
var distortion = new float[5];
RokidExtensionAPI.RokidOpenXR\_API\_GetDistortion(distortion);
var imageDimensions = new int[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetImageDimensions(imageDimensions);
size = new Vector2Int(imageDimensions[0], imageDimensions[1]);
var cameraParamList = new List&lt;float&gt; { focalLength[0], focalLength[1], principalPoint[0], principalPoint[1] }.Concat(distortion.ToList().GetRange(1, 4)).ToList();
cameraParameters = CameraParameters.tryCreateWithCustomIntrinsics(size.ToEasyARVector(), cameraParamList, CameraModelType.OpenCV\_Fisheye, CameraDeviceType.Back, 0).Value;
deviceCamera = new DeviceFrameSourceCamera(CameraDeviceType.Back, 0, size, new Vector2(50, 50), new DeviceFrameSourceCamera.CameraExtrinsics(Pose.identity, true), AxisSystemType.Unity);
RokidExtensionAPI.RokidOpenXR\_API\_OpenCameraPreview(OnCameraDataUpdate);
started = true;
}
`
```
重写 [OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop) 并释放资源，需要确保调用 base.OnSessionStop。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`protected override void OnSessionStop()
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
`
```
## 输入相机帧数据
在获取相机帧数据更新后，调用 [HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Pose_easyar_MotionTrackingStatus_) / [HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Quaternion_) 来输入相机帧数据。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`private static void OnCameraDataUpdate(IntPtr ptr, int dataSize, ushort width, ushort height, long timestamp)
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
`
```
##### 小心
不要忘记在使用后执行 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 或通过 `using` 等机制释放 [Image](../../../api/unity/easyar.Image.html) 、[Buffer](../../../api/unity/easyar.Buffer.html) 以及其它相关数据。否则会出现严重内存泄漏，buffer pool 获取 buffer 也可能会失败。
## 输入渲染帧数据
在设备数据准备好之后，每个渲染帧调用 [HandleRenderFrameData(double, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Pose_easyar_MotionTrackingStatus_) / [HandleRenderFrameData(double, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Quaternion_) 来输入渲染帧数据。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
`protected void LateUpdate()
{
if (!started) { return; }
if ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() &lt; RokidTrackingStatus.Detecting) { return; }
if ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() &gt;= RokidTrackingStatus.Tracking\_Paused) { return; }
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
`
```
## 后续步骤
* 创建 [头显扩展包](../headsets/extension.html)
## 相关主题
* [帧数据源和运行时选取过程](frame-source.html)
* [AR Session](../fundamentals/session.html)
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)