---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-input-frame.html
original_file: doc--zh-cn--develop--unity--cameras--external-input-frame.md
normalized_at: 2026-02-27
---
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
