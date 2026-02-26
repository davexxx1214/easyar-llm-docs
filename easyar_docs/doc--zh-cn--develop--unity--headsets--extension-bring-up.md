---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-bring-up.html
---

运行验证（bring-up）头显扩展 | EasyAR 文档
**
##### Table of Contents
**
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
##### 重要事项
头显扩展包所使用的输入扩展是一个 [自定义相机](../../cameras/custom-camera.html) 实现。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
如果 `Image` 以及 `Dense` 都和手机上的效果表现一致或更好，那么大部分 EasyAR 的功能就都可以在设备上正常工作，可以开始测试 Mega 了。
## 解决运行中的异常情况：问题分解
如果无法重现与手机上相同的结果，那接下来是一个详细的问题分解过程，可以参考它来寻找根因。建议始终关注系统日志输出。
### 步骤零：理解头显自身系统误差
还记得 [为 AR/MR 准备设备](extension-imp.html) 中所描述的运动跟踪和显示需求吗？
##### 重要事项
运动跟踪/VIO 误差会始终以不同方式影响 EasyAR 算法的稳定性。
##### 重要事项
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
##### 提示
必须正常停止录制才能获取到可随机索引的 EIF 文件。
在 Unity 编辑器中运行 EIF 数据时最好使用纯净的 EasyAR 场景或使用 EasyAR 的示例以避免场景中存在不正确的配置。
可以在 Unity 编辑器中看到 `相机帧数据` 的回放。图像数据并不是字节相等的，整个流程中存在有损编解码。
EasyAR 会在计算中使用畸变参数但显示时不会对图像做反畸变。所以如果输入了这些数据，当在 Unity 中回放 EIF 文件时，会观察到没有反畸变的数据，这是符合预期的。
##### 提示
修改 Unity game 窗口的比例与输入相同，否则数据会被裁剪显示。
如果数据播放偏快或偏慢，需要检查 `timestamp` 输入。
##### 注意
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
##### 注意
[图像跟踪](../../image-tracking/intro.html) 需要跟踪目标占据整个图像的一定比例，如果无法跟踪到图像，尝试移动头到更加接近图像的位置。
如果跟踪持续失败或虚拟物体显示在图像中远离目标的位置，则很有可能 `intrinsics` 存在问题。
如果图像数据有畸变，可能会看到虚拟物体不会完美的覆盖图像上的跟踪目标，这是符合预期的。当跟踪目标处于图像边缘时这个现象会更加明显。
### 步骤五：在设备上运行图像跟踪
>
> 必须正常的功能或数据：
>
>
* > 设备自身的显示系统
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
##### 注意
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
* > 设备自身的显示系统
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
##### 提示
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
* > 设备自身的显示系统
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
##### 重要事项
用户使用时会非常关注这些显示问题，而很多设备也确实无法在大空间场景提供非常完美的显示效果。EasyAR 无法解决设备自身的显示问题，这需要设备厂商迭代解决，与此同时，用户也需要理解这些问题。
## 后续步骤
* [发布扩展包](extension-dist.html)
## 相关主题
可以在手机上运行的示例：
* 图像跟踪示例 ImageTracking\_Targets，可以通过它了解 [图像跟踪](../../image-tracking/intro.html) 功能的预期执行效果功能
* 稠密空间地图示例 SpatialMap\_Dense\_BallGame，可以通过它了解 [稠密空间地图](../../dense-spatial-mapping/intro.html) 功能的预期执行效果
* 运动融合示例 ImageTracking\_MotionFusion，可以通过它了解 [运动融合](../../image-tracking/motion-fusion.html) 功能的预期执行效果
* Mega 示例 MegaBlock\_Basic，可以通过它了解 [Mega](../../mega/intro.html) 功能的预期执行效果