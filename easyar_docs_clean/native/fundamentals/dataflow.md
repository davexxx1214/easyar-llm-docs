---
source: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/dataflow.html
original_file: doc--zh-cn--develop--native--fundamentals--dataflow.md
normalized_at: 2026-02-27
---
# AR 数据流
本文介绍了 EasyAR Sense 中的数据流。EasyAR Sense 中使用组件化 API，组件之间通过数据流来连接。
## 输入输出数据
![fundamentals dataflow input output](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-input-output.png)
[InputFrame](../../../api/native/easyar.InputFrame.html)：输入帧。包含图像、camera 参数、时间戳、相机相对于世界坐标系的变换和跟踪状态。其中，camera 参数、时间戳、相机相对于世界坐标系的变换和跟踪状态均为可选，但特定的算法组件会对输入有特定的要求。
[OutputFrame](../../../api/native/easyar.OutputFrame.html)：输出帧。包含输入帧和同步处理组件的输出结果。
[FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html)：反馈帧。包含一个输入帧和一个历史输出帧，用于 [ImageTracker](../../../api/native/easyar.ImageTracker.html) 等反馈式同步处理组件。
## Camera组件
[CameraDevice](../../../api/native/easyar.CameraDevice.html)：Windows、Mac、iOS、Android 上的默认摄像头。
[ARKitCameraDevice](../../../api/native/easyar.ARKitCameraDevice.html)：iOS 上的 ARKit 默认实现。
[ARCoreCameraDevice](../../../api/native/easyar.ARCoreCameraDevice.html)：Android 上的 ARCore 默认实现。
[MotionTrackerCameraDevice](../../../api/native/easyar.MotionTrackerCameraDevice.html)：实现运动跟踪，通过多传感器融合解算设备的 6DoF 坐标。(只支持 Android )
[ThreeDofCameraDevice](../../../api/native/easyar.ThreeDofCameraDevice.html)：在默认摄像头的基础上，增加了 3DoF 的方向。
[InertialCameraDevice](../../../api/native/easyar.InertialCameraDevice.html)：在默认摄像头的基础上，增加了 3DoF 的方向和平面的基于惯性估计的平移。
custom camera device：自定义摄像头实现。
## 算法组件
反馈式同步处理组件：需要每帧跟着摄像机图像输出结果，并且需要上一帧处理结果用于避免相互干扰。
* [ImageTracker](../../../api/native/easyar.ImageTracker.html)：实现了平面图像的检测和跟踪。
* [ObjectTracker](../../../api/native/easyar.ObjectTracker.html)：实现了 3D 物体的检测和跟踪。
同步处理组件：需要每帧跟着摄像机图像输出结果。
* [SurfaceTracker](../../../api/native/easyar.SurfaceTracker.html)：实现了对环境表面的跟踪。
* [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html)：实现了稀疏空间地图，提供了扫描物理空间同时生成点云地图并进行实时定位的能力。
* [MegaTracker](../../../api/native/easyar.MegaTracker.html)：实现了 Mega 空间定位。
异步处理组件：不需要每帧跟着摄像机图像输出结果。
* [CloudRecognizer](../../../api/native/easyar.CloudRecognizer.html)：实现了云识别。
* [DenseSpatialMap](../../../api/native/easyar.DenseSpatialMap.html)：实现了稠密空间地图，可用于实现碰撞、遮挡等效果。
## 组件的可用性检查
所有的组件均有 isAvailable 函数，可用于判断该组件是否可用。
组件不可用的情况有
* 当前操作系统上没有实现。
* 组件所需要的依赖不存在，例如 ARKit、ARCore。
* 组件在当前版本（variant）上不存在，例如一些精简版本中某些功能不存在。
* 组件在当前 License 下不可用。
使用组件之前务必要判断组件是否可用，并进行相应的 fallback 或者提示。
## 数据流
组件的连接方式如下图所示。
![fundamentals dataflow](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow.png)
有一种特殊的输入为反馈式帧的用法，如下图所示。
![fundamentals dataflow feedback](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-feedback.png)
## 数据流辅助类
数据流的发出和接收端口，各组件需要包含这些端口
* [SignalSink](../../../api/native/easyar.SignalSink.html) / [SignalSource](../../../api/native/easyar.SignalSource.html)：接收/发出一个信号(无数据)。
* [InputFrameSink](../../../api/native/easyar.InputFrameSink.html) / [InputFrameSource](../../../api/native/easyar.InputFrameSource.html)：接收/发出一个 [InputFrame](../../../api/native/easyar.InputFrame.html)。
* [OutputFrameSink](../../../api/native/easyar.OutputFrameSink.html) / [OutputFrameSource](../../../api/native/easyar.OutputFrameSource.html)：接收/发出一个 [OutputFrame](../../../api/native/easyar.OutputFrame.html)。
* [FeedbackFrameSink](../../../api/native/easyar.FeedbackFrameSink.html) / [FeedbackFrameSource](../../../api/native/easyar.FeedbackFrameSource.html)：接收/发出一个 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html)。
数据流的分支和合并
* [InputFrameFork](../../../api/native/easyar.InputFrameFork.html)：将一个 [InputFrame](../../../api/native/easyar.InputFrame.html) 分成多个并行发出。
* [OutputFrameFork](../../../api/native/easyar.OutputFrameFork.html)：将一个 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 分成多个并行发出。
* [OutputFrameJoin](../../../api/native/easyar.OutputFrameJoin.html)：将多个 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 合并成一个，并将所有的结果合并到 Results 中。需要注意其多个输入的连接不应该在有数据流入的同时进行，否则可能会陷入不能输出的状态。（推荐在 Camera 启动之前完成数据流连接。）
* [FeedbackFrameFork](../../../api/native/easyar.FeedbackFrameFork.html)：将一个 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html) 分成多个并行发出。
数据流的限流和缓存
* [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html)：接收并发出 [InputFrame](../../../api/native/easyar.InputFrame.html)，但一次只发出一个，只有在接收到一个触发信号后才会发出下一个 [InputFrame](../../../api/native/easyar.InputFrame.html)，接收到多个 [InputFrame](../../../api/native/easyar.InputFrame.html) 时，后续的 [InputFrame](../../../api/native/easyar.InputFrame.html) 可能会覆盖前面的 [InputFrame](../../../api/native/easyar.InputFrame.html)。
* [OutputFrameBuffer](../../../api/native/easyar.OutputFrameBuffer.html)：接收 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 并缓存，等待用户轮询，接收到 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 的时候可以发出一个信号。
* 将 [OutputFrameBuffer](../../../api/native/easyar.OutputFrameBuffer.html) 发出的信号接到 [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html) 上，即可完成整个限流过程。
数据流的转换
* [InputFrameToOutputFrameAdapter](../../../api/native/easyar.InputFrameToOutputFrameAdapter.html)：可以将一个 [InputFrame](../../../api/native/easyar.InputFrame.html) 直接包装成 [OutputFrame](../../../api/native/easyar.OutputFrame.html)，用于渲染显示。
* [InputFrameToFeedbackFrameAdapter](../../../api/native/easyar.InputFrameToFeedbackFrameAdapter.html)：可以将一个 [InputFrame](../../../api/native/easyar.InputFrame.html) 和一个 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html) 包装成 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html)，用于反馈式同步处理组件。
## InputFrame数量的限制
[CameraDevice](../../../api/native/easyar.CameraDevice.html) 可以设置 bufferCapacity，即发出 [InputFrame](../../../api/native/easyar.InputFrame.html) 的最大数量，当前的默认值为8。
自定义摄像头可以使用 [BufferPool](../../../api/native/easyar.BufferPool.html) 实现。
各组件需要的 [InputFrame](../../../api/native/easyar.InputFrame.html) 数量，参考各组件的 API 文档。
如果 [InputFrame](../../../api/native/easyar.InputFrame.html) 数量不足，可能造成数据流卡住，导致渲染卡住。
如果 [InputFrame](../../../api/native/easyar.InputFrame.html) 数量不足，也可能出现第一次启动渲染不卡住但切换到后台或暂停/启动各组件后渲染卡住的情况，测试时需要注意覆盖。
## 连接和断开连接
不推荐在数据流运行过程中连接和断开连接。
如果需要在运行过程中进行连接和断开连接，需要注意只能在割边（去掉这条边后数据流会一分为二）上进行，不能在环的边（这里的环指的是将数据流看作无向图时边构成的环）上、 [OutputFrameJoin](../../../api/native/easyar.OutputFrameJoin.html) 的输入或者 [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html) 的 sideInput 上进行，否则可能会陷入数据流卡在 [OutputFrameJoin](../../../api/native/easyar.OutputFrameJoin.html) 和 [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html) 等结点无法输出的状态。
算法组件均有 start/stop 功能，在 stop 的时候，帧将不会被处理，但仍然会从组件中输出，只是不带有结果。
## 典型用法
以下为单个 [ImageTracker](../../../api/native/easyar.ImageTracker.html) 的用法，可用于识别、跟踪不重复的平面识别图。
![fundamentals dataflow single ImageTracker](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-single-ImageTracker.png)
以下为单个 [ImageTracker](../../../api/native/easyar.ImageTracker.html) 的用法，可用于识别、跟踪重复的平面识别图。
![fundamentals dataflow multiple ImageTracker](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-multiple-ImageTracker.png)
以下为 [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html) 的用法，可用于实现稀疏空间地图建图和定位、跟踪。
![fundamentals dataflow SparseSpatialMap](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-SparseSpatialMap.png)
以下为 [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html) 和 [DenseSpatialMap](../../../api/native/easyar.DenseSpatialMap.html) 同时使用的用法，可用于实现稀疏空间地图建图、定位、跟踪和稠密空间地图生成。
![fundamentals dataflow Sparse-DenseSpatialMap](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-Sparse-DenseSpatialMap.png)
