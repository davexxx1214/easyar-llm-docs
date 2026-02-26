---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-image-stream-frame-source.html
---

创建图像输入扩展 | EasyAR 文档
**
##### Table of Contents
**
# 创建图像输入扩展
## 开始之前
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
* 阅读 [外部帧数据源](external-frame-source.html) 了解创建外部帧数据源所需详细接口说明。
* 阅读 [外部输入帧数据](external-input-frame.html) 了解相机帧数据和渲染帧数据。
## 创建外部帧数据源类
继承 [ExternalImageStreamFrameSource](../../../api/unity/easyar.ExternalImageStreamFrameSource.html) 来创建图像输入扩展。它是 [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html) 的子类，文件名应与类名相同。
例如：
```
`public class MyFrameSource : ExternalImageStreamFrameSource
{
}
`
```
示例 Workflow\_FrameSource\_ExternalImageStream 就是一个基于手机上使用 ARCore 录制的视频作为输入的图像输入扩展实现。该视频是使用 Pixel2 上的 ARCore 通过相机回调方式采集的（不是屏幕录制）。
## 设备定义
重写 [IsCameraUnderControl](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsCameraUnderControl) 并返回 true。
重写 [IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD) 来定义设备是否是头显。
例如，使用视频作为输入时设为 false。
```
`protected override bool IsHMD =&gt; false;
`
```
重写 [Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display) 来定义设备的显示。
例如，如果只在手机上运行，可以[Display.DefaultSystemDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultSystemDisplay)，它的旋转值根据操作系统当前显示状态而自动改变。
```
`protected override IDisplay Display =&gt; easyar.Display.DefaultSystemDisplay;
`
```
## 可用性
重写 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 来定义设备是否可用。
例如，使用视频作为输入时始终可用：
```
`protected override Optional&lt;bool&gt; IsAvailable =&gt; true;
`
```
如果 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 在 session 组装时无法判断，可以重写 [CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程来阻塞组装过程，直到确定是否可用为止。
## 虚拟摄像机
重写 [Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera) 来提供虚拟摄像机。
例如，有时可用使用 [Camera.main](https://docs.unity3d.com/ScriptReference/Camera-main.html) 作为 session 的虚拟摄像机：
```
`protected override Camera Camera =&gt; Camera.main;
`
```
## 物理相机
使用 [FrameSourceCamera](../../../api/unity/easyar.FrameSourceCamera.html) 类型重写 [DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 以提供设备物理相机信息。这个数据会在输入相机帧数据时使用。[CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须完成创建。
例如，使用示例 Workflow\_FrameSource\_ExternalImageStream 中所使用的视频：
```
`private FrameSourceCamera deviceCamera;
protected override List&lt;FrameSourceCamera&gt; DeviceCameras =&gt; new List&lt;FrameSourceCamera&gt; { deviceCamera };
{
var size = new Vector2Int(640, 360);
var cameraType = CameraDeviceType.Back;
var cameraOrientation = 90;
deviceCamera = new FrameSourceCamera(cameraType, cameraOrientation, size, new Vector2(30, 30));
started = true;
}
`
```
##### 小心
这里的几个输入参数需要根据实际使用的视频来设置。上面代码中的参数只适用于示例中的视频。
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
...
}
`
```
这里是适合打开设备相机的位置，尤其是如果这些相机没有被设计成要一直打开时。同时这里也是适合获取整个生命周期内不会变化的标定数据的位置。有时在这些数据可以被获取前可能需要等待设备准备好或等待数据更新。
同时，这里也是一个适合启动数据输入循环的位置。也可以在 [Update()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) 或其它方法中写这个循环，尤其是当数据需要在 Unity 执行顺序的某个特殊时间点获取的时候。在 session 准备好（ready）之前不要输入数据。
如果需要，也可以忽略启动过程并在每次更新时做数据检查，这完全取决于具体需求。
例如，使用视频作为输入时可以在这里开始播放视频并启动数据输入循环：
```
`protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
...
player.Play();
StartCoroutine(VideoDataToInputFrames());
}
`
```
重写 [OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop) 并释放资源，需要确保调用 base.OnSessionStop。
例如，使用视频作为输入时可以在这里停止视频播放并释放相关资源：
```
`protected override void OnSessionStop()
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
`
```
## 从设备或文件获取相机帧数据
可以从系统相机、USB 相机、视频文件、网络等任意来源获取图像。只要能将数据转换成 [Image](../../../api/unity/easyar.Image.html) 所需的格式即可。从这些设备或文件获取数据的方式各不相同，需要参考相关设备或文件的使用说明。
例如，使用视频作为输入时，可以使用 [Texture2D.ReadPixels(Rect, int, int, bool)](https://docs.unity3d.com/ScriptReference/Texture2D.ReadPixels.html) 从视频播放器的 RenderTexture 中获取相机帧数据，然后复制 [Texture2D.GetRawTextureData()](https://docs.unity3d.com/ScriptReference/Texture2D.GetRawTextureData.html) 的数据到 [Buffer](../../../api/unity/easyar.Buffer.html) 中：
```
`void VideoDataToInputFrames()
{
...
RenderTexture.active = renderTexture;
var pixelSize = new Vector2Int((int)player.width, (int)player.height);
var texture = new Texture2D(pixelSize.x, pixelSize.y, TextureFormat.RGB24, false);
texture.ReadPixels(new Rect(0, 0, pixelSize.x, pixelSize.y), 0, 0);
texture.Apply();
RenderTexture.active = null;
...
CopyRawTextureData(buffer, texture.GetRawTextureData&lt;byte&gt;(), pixelSize);
}
static unsafe void CopyRawTextureData(Buffer buffer, Unity.Collections.NativeArray&lt;byte&gt; data, Vector2Int size)
{
int oneLineLength = size.x \* 3;
int totalLength = oneLineLength \* size.y;
var ptr = new IntPtr(data.GetUnsafeReadOnlyPtr());
for (int i = 0; i &lt; size.y; i++)
{
buffer.tryCopyFrom(ptr, oneLineLength \* i, totalLength - oneLineLength \* (i + 1), oneLineLength);
}
}
`
```
##### 小心
如上面代码中一样，从 [Texture2D](https://docs.unity3d.com/ScriptReference/Texture2D.html) 的指针中复制的数据需要上下反转之后，数据的内存排列才是正常的图像。
在获取图像的同时，还需要获取相机或等效相机的标定数据并创建 [CameraParameters](../../../api/unity/easyar.CameraParameters.html) 实例。
如果数据的原始来源来自手机的相机回调，且数据没有人工裁剪，那么可以直接使用手机相机的标定数据。在使用 ARCore 或 ARKit 等接口获取相机回调数据时，可以参考相关文档获取相机内参。如果需要使用的 AR 功能是图像跟踪或物体跟踪，这种情况也可以使用 [CameraParameters.createWithDefaultIntrinsics(Vec2I, CameraDeviceType, int)](../../../api/unity/easyar.CameraParameters.html#u_easyar_CameraParameters_createWithDefaultIntrinsics_easyar_Vec2I_easyar_CameraDeviceType_System_Int32_) 来创建相机内参，这时算法效果会受到轻微影响，但一般影响不大。
如果数据来自 USB 相机或非相机回调生成的视频文件等其他来源，则需要对相机或视频帧进行标定以获取正确的内参。
##### 小心
相机回调数据不能裁剪，裁剪后需要重新计算内参。如果数据来自屏幕录制等方式获取的图像数据，通常无法使用手机相机的标定数据，这时也需要对相机或视频帧进行标定以获取正确的内参。
内参不正确会导致 AR 功能无法正常使用，常见虚拟内容与现实物体无法对齐，以及 AR 跟踪不容易成功或很容易丢失等。
例如，使用示例 Workflow\_FrameSource\_ExternalImageStream 中所使用的视频，其对应的相机内参及 [CameraParameters](../../../api/unity/easyar.CameraParameters.html) 创建过程如下：
```
`var size = new Vector2Int(640, 360);
var cameraType = CameraDeviceType.Back;
var cameraOrientation = 90;
cameraParameters = new CameraParameters(size.ToEasyARVector(), new Vec2F(506.085f, 505.3105f), new Vec2F(318.1032f, 177.6514f), cameraType, cameraOrientation);
`
```
##### 小心
上面代码中的参数只适用于示例中的视频，该相机内参与视频是在同一时间采集的。如果需要使用其他视频或设备的数据，务必同时获取设备内参或手动进行标定。
## 输入相机帧数据
在获取相机帧数据更新后，调用 [HandleCameraFrameData(double, Image, CameraParameters)](../../../api/unity/easyar.ExternalImageStreamFrameSource.html#u_easyar_ExternalImageStreamFrameSource_HandleCameraFrameData_System_Double_easyar_Image_easyar_CameraParameters_) 来输入相机帧数据。
例如，使用视频作为输入时实现如下：
```
`IEnumerator VideoDataToInputFrames()
{
yield return new WaitUntil(() =&gt; player.isPrepared);
var pixelSize = new Vector2Int((int)player.width, (int)player.height);
...
yield return new WaitUntil(() =&gt; player.isPlaying &amp;&amp; player.frame &gt;= 0);
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
CopyRawTextureData(buffer, texture.GetRawTextureData&lt;byte&gt;(), pixelSize);
using (buffer)
using (var image = Image.create(buffer, pixelFormat, pixelSize.x, pixelSize.y, pixelSize.x, pixelSize.y))
{
HandleCameraFrameData(player.time, image, cameraParameters);
}
}
}
`
```
##### 小心
不要忘记在使用后执行 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 或通过 `using` 等机制释放 [Image](../../../api/unity/easyar.Image.html) 、[Buffer](../../../api/unity/easyar.Buffer.html) 以及其它相关数据。否则会出现严重内存泄漏，buffer pool 获取 buffer 也可能会失败。
## 相关主题
* [帧数据源和运行时选取过程](frame-source.html)
* [AR Session](../fundamentals/session.html)
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)