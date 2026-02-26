---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/comp-CameraDeviceFrameSource.html
original_file: doc--zh-cn--develop--unity--cameras--comp-CameraDeviceFrameSource.md
normalized_at: 2026-02-27
---
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
