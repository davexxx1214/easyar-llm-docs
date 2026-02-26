---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-frame-source.html
---

Unity 中的自定义相机实现 —— 外部帧数据源 | EasyAR 文档
**
##### Table of Contents
**
# Unity 中的自定义相机实现 —— 外部帧数据源
通过外部帧数据源（[ExternalFrameSource](../../../api/unity/easyar.ExternalFrameSource.html)），开发者可以为 EasyAR Sense 扩展自定义的相机实现，从而支持特定的头显设备或其它输入设备。以下内容介绍了外部帧数据源的类型结构及接口定义。
## 开始之前
* 了解 [自定义相机](../../cameras/custom-camera.html) 的基本概念。
* 了解 [帧数据源](frame-source.html) 的基本概念、类型以及运行时的选取方法。
## 外部帧数据源类型
```
`---
config:
class:
hideEmptyMembersBox: true
---
classDiagram
class FrameSource {
&lt;&lt;abstract&gt;&gt;
}
class ExternalFrameSource {
&lt;&lt;abstract&gt;&gt;
}
class ExternalDeviceFrameSource {
&lt;&lt;abstract&gt;&gt;
}
class ExternalDeviceMotionFrameSource:::EasyAR {
&lt;&lt;abstract&gt;&gt;
}
class ExternalDeviceRotationFrameSource:::EasyAR {
&lt;&lt;abstract&gt;&gt;
}
class ExternalImageStreamFrameSource:::EasyAR {
&lt;&lt;abstract&gt;&gt;
}
ExternalFrameSource --|&gt; FrameSource
ExternalDeviceFrameSource --|&gt; ExternalFrameSource
ExternalDeviceMotionFrameSource --|&gt; ExternalDeviceFrameSource
ExternalDeviceRotationFrameSource --|&gt; ExternalDeviceFrameSource
ExternalImageStreamFrameSource --|&gt; ExternalFrameSource
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
`
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
如果该数值等于 Optional&lt;bool&gt;.Empty，[FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程会被调用，应在协程结束前更新 [FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable)。
可用性接口会在 session 组装时使用，不可用的组件将不会被选择且它的方法在 session 运行时不会被调用。
* [FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability)（可选）：`检查 frame source 是否可用的协程`
[FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 等于 Optional&lt;bool&gt;.Empty 时会被调用。在该协程结束前，session 的组装过程会被阻塞。
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