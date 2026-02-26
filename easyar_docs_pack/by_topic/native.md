# EasyAR 专题包：native

适用于上下文长度有限时的分卷输入。

## 目录
- `native/fundamentals/3dengine.md`
- `native/fundamentals/contents.md`
- `native/fundamentals/coordinates.md`
- `native/fundamentals/dataflow.md`
- `native/fundamentals/initialization.md`
- `native/getting-started/choosing-an-engine.md`
- `native/getting-started/enable-easyar-android.md`
- `native/getting-started/enable-easyar-ios.md`
- `native/getting-started/quickstart-android.md`
- `native/getting-started/quickstart-ios.md`
- `native/getting-started/quickstart-windows.md`
- `native/getting-started/variants.md`
- `native/release-notes/release-notes-1_0.md`
- `native/release-notes/release-notes-1_1.md`
- `native/release-notes/release-notes-1_2.md`
- `native/release-notes/release-notes-1_3.md`
- `native/release-notes/release-notes-2_0.md`
- `native/release-notes/release-notes-2_1.md`
- `native/release-notes/release-notes-2_2.md`
- `native/release-notes/release-notes-2_3.md`
- `native/release-notes/release-notes-3_0.md`
- `native/release-notes/release-notes-3_1.md`
- `native/release-notes/release-notes-4_0.md`
- `native/release-notes/release-notes-4_1.md`
- `native/release-notes/release-notes-4_2.md`
- `native/release-notes/release-notes-4_3.md`
- `native/release-notes/release-notes-4_4.md`
- `native/release-notes/release-notes-4_5.md`
- `native/release-notes/release-notes-4_6.md`
- `native/release-notes/release-notes-4_7.md`
- `native/release-notes/release-notes.md`

---

## 在 3D 引擎中使用 EasyAR
- 章节路径: `native/fundamentals/3dengine.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/3dengine.html

# 在 3D 引擎中使用 EasyAR
在 3D 引擎中使用 EasyAR，需要渲染相机画面和虚拟物体。渲染虚拟物体需要和相机画面对准。相机画面渲染时，图像生成时和显示时的一些参数可能不匹配，例如物理相机的位置、朝向、画幅、宽高比等和显示器画面可能不同，在渲染时需要考虑。如果需要将 EasyAR 接到没有支持的 3D 引擎上，需要特别注意以下细节。
## 相机画面边界填充的剪裁
图像的剪裁、转置和编码都需要较大的计算量，出于减少计算和降低延迟的考虑，一般会使用比较原始的格式。为了方便视频编码，物理相机输出的图像经常会对齐到 8x8、16x16、32x32、64x64 这样的方格上，例如有些手机上选择 1920x1080 的分辨率，输出的图像可能变成 1920x1088，就是由于 1080 不是 64 的倍数。
![image with padding](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-crop.png)
这就要求在渲染的时候去掉这些多余的填充部分。有多种可能的做法：一种是在将图像上传到显存时指定宽度，例如 OpenGL 中可以使用`glPixelStorei(GL\_PACK\_ROW\_LENGTH, ...)`实现；一种是在 fragment shader 中手动计算 UV 坐标，并在从图像采样时将超过的部分截断。
## 跟随屏幕旋转方向渲染
在手机上，物理相机记录的图像通常相对于机身固定，不随屏幕显示方向变化而变化。但手机机身朝向的变化会影响到我们对于图像的上下左右方向的定义。渲染时，当前屏幕显示方向也会影响到显示的图像的方向。
通常在渲染时，需要确定一个相机图像相对于屏幕显示方向的旋转角。
如果我们用 \\(\\theta\_{screen}\\) 表示屏幕图像相对于屏幕自然方向顺时针旋转的弧度，\\(\\theta\_{phycam}\\) 表示物理相机图像要正确显示在自然方向的屏幕上需要顺时针旋转的弧度，\\(\\theta\\) 表示物理相机图像显示在当前屏幕上需要顺时针旋转的弧度。
对于后置摄像头，有
\\[
\\theta = \\theta\_{phycam} - \\theta\_{screen}
\\]
例如，Android 手机上，在自然方向使用手机时，\\(\\theta\_{screen} = 0, \\theta\_{phycam} = \\frac{\\pi}{2}\\)，则 \\(\\theta = \\frac{\\pi}{2}\\)。
对于前置摄像头，如果在旋转完成后，进行左右方向翻转，则有
\\[
\\theta = \\theta\_{phycam} + \\theta\_{screen}
\\]
> **注意**
当屏幕图像旋转时，需要在旋转发生后的第一帧立刻重新计算 \\(\\theta\\)，否则可能出现瞬间的屏幕图像方向不正常。
## 相机背景和虚拟物体的渲染
在手机上渲染虚拟物体，需要将虚拟物体和相机画面对准。这要求我们将渲染相机和物体都放置在和真实空间完全对应的虚拟空间中，并使用物理相机相同的视场角、宽高比来进行渲染。相机画面和虚拟物体经过的透视投影变换几乎一模一样，只有一点区别，即相机画面的透视投影变换大部分是发生在物理相机中，而虚拟物体的透视投影变换完全是一个计算过程。
以下均采用 OpenGL 惯例，使用其他惯例，需要进行相应的坐标轴映射。假设相机坐标系的坐标轴定义如下：x 轴指向右，y 轴指向上，z 轴出屏幕向外。剪裁坐标系的坐标轴定义如下：x 轴指向右，y 轴指向上，z 轴出屏幕向外，w 轴为虚拟轴。
此时，渲染相机画面需要的透视投影变换矩阵如下：
\\[
P\_i=\\left(
\\begin{array}{cccc}
(-1)^{\\text{flip}} & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & 1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
\\cos (-\\theta ) & -\\sin (-\\theta ) & \\phantom{0} & \\phantom{0} \\\\
\\sin (-\\theta ) & \\cos (-\\theta ) & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
s\_x & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & s\_y & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)
\\]
其中：`flip`是指画面是否左右翻转，翻转时值为 1，不翻转时值为 0；\\(\\theta\\) 是图像沿顺时针旋转角，单位为弧度； \\(s\_x\\) 、 \\(s\_y\\) 是缩放系数，用于进行等比缩放或等比填充，它们随 \\(\\theta\\) 变化。此变换矩阵首先对相机图像进行缩放，然后进行旋转，最后进行翻转。渲染时应使用一个矩形铺满屏幕，例如在 OpenGL 中，可以将矩形的顶点放在 \\((-1, -1, 0)\\) 、 \\((1, -1, 0)\\) 、 \\((1, 1, 0)\\) 、 \\((-1, 1, 0)\\) ，UV 坐标设置在对应的四个角上，然后使用此透视投影矩阵渲染。
渲染虚拟物体需要的透视投影矩阵如下：
\\[
P=P\_i\\left(
\\begin{array}{cccc}
1 & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & 1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -\\frac{f+n}{f-n} & -\\frac{2 f n}{f-n} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
\\frac{2}{w} & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\frac{2}{h} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & -1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
f\_x & \\phantom{0} & c\_x & \\phantom{0} \\\\
\\phantom{0} & f\_y & c\_y & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & -1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)
\\]
其中： \\(n\\) 、 \\(f\\) 是通常 3D 渲染的透视投影矩阵中使用的近裁和远裁参数； \\(w\\) 、 \\(h\\) 是相机图像的像素宽高； \\(f\_x\\) 、 \\(f\_y\\) 、 \\(c\_x\\) 、 \\(c\_y\\) 为相机模型中常用的内参，其中 \\(f\_x\\) 、 \\(f\_y\\) 是像素焦距， \\(c\_x\\) 、 \\(c\_y\\) 为主点像素位置。此投影投影矩阵依次进行如下变换：相机内参的透视投影变换（由于 OpenCV 中图像坐标系 y、z 轴方向和 OpenGL 相机坐标系相反，进行了两次坐标系变换），从图像像素坐标系转换到图像矩形坐标系的变换，近裁和远裁的变换，渲染相机画面时的透视投影变换。
经过整理，可得
\\[
P=P\_i\\left(
\\begin{array}{cccc}
\\frac{2 f\_x}{w} & \\phantom{0} & 1-\\frac{2 c\_x}{w} & \\phantom{0} \\\\
\\phantom{0} & \\frac{2 f\_y}{h} & -1+\\frac{2 c\_y}{h} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -\\frac{f+n}{f-n} & -\\frac{2 f n}{f-n} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\end{array}
\\right)
\\]
从上述过程可知，渲染通常需要分两次进行，一次渲染相机画面，一次渲染虚拟物体，虚拟物体覆盖在相机画面之上。
有些 3D 引擎中将透视投影矩阵表示为横向视场角、宽高比等参数，如果不考虑旋转、翻转，忽略主点偏移，是可以计算的，其中横向视场角 \\(\\alpha=2 arctan{\\frac{w}{2 f\_x}}\\) ，宽高比 \\(r=\\frac{w}{h}\\) 。
需要注意这个过程中没有考虑相机畸变的情况，因为目前大部分手机的相机畸变非常轻微。

---

## 3D 空间内容展示
- 章节路径: `native/fundamentals/contents.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/contents.html

# 3D 空间内容展示
使用 AR 时，通常需要展示虚拟物体。在简单的测试示例中，可以使用简单的几何体，但要面向消费者开发时，一般需要显示高精度的3D 模型和动画，并可能会在点击模型结点时触发事件和交互。
## 模型
当前比较流行的 3D 模型，一般由三角形网格（triangle mesh）构成。为了让模型看起来真实，我们需要为每个三角形赋予材质 （material）。材质通常实现某种光照模型，其内容由贴图和光照模型参数构成。
* 贴图（texture）决定三角形中每个点的基础颜色，所有三角形的贴图会放在一张或多张漫反射贴图中。在一些进阶用法中，还可以使用贴图表示每个点的法线方向或者其他参数。
* 光照模型（lighting model）定义物体如何与光线交互，常见的有 PBR。光照模型通常使用 shader 来实现。PBR 光照模型的参数有颜色、金属度、粗糙度等。
在应用开发中，一般不会直接在 OpenGL / Metal / Vulkan / Direct3D 上加载 3D 模型，而是使用 3D 引擎来进行加载。3D 引擎会要求使用一些特定的 3D 模型格式，例如历史悠久、较为可读的obj / mtl 格式，以及目前比较流行的 glTF 格式。
## 动画
为了让模型运动，需要使用骨骼动画。骨骼是指的 3D 模型中做刚体运动时保持一致运动的大块模型结点。
显示动画，需要在运行时不断更新模型结点的位置和姿态（变换矩阵）。大部分 3D 引擎会提供动画功能，只需要在动画制作软件中编辑好动画，并以 3D 引擎支持的格式导出，即可在 3D 引擎中使用。上述 glTF 格式也包含动画的功能。
## 交互
用户点击模型结点时，有时候需要触发事件和交互。一般会对骨骼动画中的骨骼进行命名，并使用碰撞检测或射线检测，在点击时触发事件，返回被点击的骨骼名称。事件的处理，可以使用脚本或者应用代码来进行。
> **注意**
如果您缺少 3D 引擎的使用经验，强烈建议您考虑使用 Unity 来开发您的应用。EasyAR Sense Unity Plugin 对 Unity 有较好的支持，如果您使用其他的 3D 引擎，可能会面临支持和可用资源较少的问题。

---

## EasyAR 坐标系
- 章节路径: `native/fundamentals/coordinates.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/coordinates.html

# EasyAR 坐标系
3D 程序中，坐标系的定义非常重要。如果没有特别说明，则采用以下惯例。
* 向量均为列向量。
* 矩阵均采用 row-major。（OpenGL 为 column-major）
* 坐标系均采用右手坐标系。(与 OpenGL 一致)
* 坐标系如果存在物理标尺，则单位使用米。
* 世界坐标系的 Y 轴负方向为重力方向。
* 设备坐标系的 X 轴向右，Y 轴向上，Z 轴为屏幕向外；对于屏幕可以旋转的设备，右和上的定义以其默认方向为准，特别的，Android 的默认方向遵循系统定义。（眼镜和部分平板的横屏放置为默认方向，手机和部分平板竖屏放置为默认方向），iOS 的默认方向为竖屏放置。（与 Android 和 iOS 的 IMU 说明中的定义一致）
## 物体跟踪的 pose
平面图像跟踪（[ImageTracker](../../../api/native/easyar.ImageTracker.html)）和3D物体跟踪（[ObjectTracker](../../../api/native/easyar.ObjectTracker.html)）的物体 pose 存放在 [pose](../../../api/native/easyar.TargetInstance.html#n_easyar_TargetInstance_pose)，表示当前被跟踪的 target 相对于 camera 的位姿。其中 camera 坐标系与 target 坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，指的是相机图像中的右和上，可能和设备自然方向的可能不同。）数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。
pose 可写成：
\\[
P = \\left(
\\begin{array}{cccc}
p\_{11} & p\_{12} & p\_{13} & p\_{14} \\\\
p\_{21} & p\_{22} & p\_{23} & p\_{24} \\\\
p\_{31} & p\_{32} & p\_{33} & p\_{34} \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)
\\]
如果 3D 引擎采用了其他的坐标轴定义，则在 3D 引擎中设置变换矩阵时需要考虑，例如 camera 坐标系和 target 坐标系的 z 方向均相反时，应设置 3D 引擎的 target 结点变换矩阵值为：
\\[
\\left(
\\begin{array}{cccc}
1 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 \\\\
0 & 0 & -1 & 0 \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
p\_{11} & p\_{12} & p\_{13} & p\_{14} \\\\
p\_{21} & p\_{22} & p\_{23} & p\_{24} \\\\
p\_{31} & p\_{32} & p\_{33} & p\_{34} \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 \\\\
0 & 0 & -1 & 0 \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)=\\left(
\\begin{array}{cccc}
p\_{11} & p\_{12} & -p\_{13} & p\_{14} \\\\
p\_{21} & p\_{22} & -p\_{23} & p\_{24} \\\\
-p\_{31} & -p\_{32} & p\_{33} & -p\_{34} \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)
\\]
## 运动跟踪的 transform
表面跟踪（[SurfaceTracker](../../../api/native/easyar.SurfaceTracker.html)） 的 [transform](../../../api/native/easyar.SurfaceTrackerResult.html#n_easyar_SurfaceTrackerResult_transform) 和运动跟踪（[MotionTrackerCameraDevice](../../../api/native/easyar.MotionTrackerCameraDevice.html)）、ARKit（[ARKitCameraDevice](../../../api/native/easyar.ARKitCameraDevice.html)）、ARCore（[ARCoreCameraDevice](../../../api/native/easyar.ARCoreCameraDevice.html)）的 [cameraTransform](../../../api/native/easyar.InputFrame.html#n_easyar_InputFrame_cameraTransform)，表示 camera 相对于世界坐标系的变换。其中 camera 坐标系与世界坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，在移动设备上指设备自然方向的右和上。）世界坐标系的 y 轴向上（与重力方向相反），原点由运动跟踪系统决定。数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。
## 稀疏空间地图和 Mega 中的 pose
稀疏空间地图 [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html) 的 [getMapPose](../../../api/native/easyar.SparseSpatialMapResult.html#n_easyar_SparseSpatialMapResult_getMapPose)和 Mega 中的 [pose](../../../api/native/easyar.MegaTrackerBlockInstance.html#n_easyar_MegaTrackerBlockInstance_pose)，表示地图 block 在 camera 坐标系中的位置和姿态。其中 camera 坐标系与世地图 block 坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，在移动设备上指设备自然方向的右和上。）地图 block 坐标系的 y 轴向上（与重力方向相反），原点由地图 block 数据决定。数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。

---

## AR 数据流
- 章节路径: `native/fundamentals/dataflow.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/dataflow.html

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

---

## 库加载和初始化
- 章节路径: `native/fundamentals/initialization.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/initialization.html

# 库加载和初始化
在使用 EasyAR Sense 的功能之前，需要进行初始化。初始化时，EasyAR Sense 会建立一些必要的环境，并验证 License Key。
## 非 Android 平台
对于 iOS/macOS/visionOS/Windows 平台，一般通过编译时动态链接来实现库的加载，参考示例添加对 EasyAR 库的引用，并在需要时添加 EasyAR 库的头文件即可。
初始化只需要调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_System_String_) 并传入 license key 即可。
## Android 平台
对于 Android 平台，一般是通过 java.lang.System.loadLibrary 来进行动态库的加载。
初始化只需要调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_android_app_Activity_System_String_) 并传入当前 Activity 和 License Key 即可，其中会自动调用 java.lang.System.loadLibrary。
如果您需要将 libEasyAR.so 放在非默认位置（例如需要在运行过程中动态下载），则您需要改为调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_android_app_Activity_System_String_System_String_) 并传入当前 Activity、License Key 和 libEasyAR.so 存放路径。
如果您有更复杂的需求，可以将加载 libEasyAR.so，设置 Activity 和验证 License Key 三个步骤分开进行。您可以先调用 [loadLibraries](../../../api/native/easyar.Engine.html#n_easyar_Engine_loadLibraries_System_String_)，再调用[setupActivity](../../../api/native/easyar.Engine.html#n_easyar_Engine_setupActivity)，再调用 [initializeKey](../../../api/native/easyar.Engine.html#n_easyar_Engine_initializeKey)。

---

## 在进行增强现实开发前选择一款 3D 引擎
- 章节路径: `native/getting-started/choosing-an-engine.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/choosing-an-engine.html

# 在进行增强现实开发前选择一款 3D 引擎
AR 开发的第一步是选择合适的 3D 引擎，这一章介绍为什么需要 3D 引擎、AR 开发中常见的 3D 引擎及各自优缺点。
## 为什么 AR 需要 3D 引擎
增强现实并不是简单地在相机画面上叠加 2D 或 3D 图像，而是一个实时三维系统，其核心能力可能还包括：
* 真实相机建模
为了渲染的虚拟物体看起来在现实中更真实，需要根据实际相机画面使用的参数（例如内外参，畸变模型等）调整用于渲染的 3D 引擎中的摄像机的投影矩阵。
* 空间坐标系统管理
统一管理设备、环境、AR 内容等之间的位置和姿态，负责世界坐标、相机坐标、设备坐标之间的选择、设置和转换。
* 实时三维渲染
根据实时估计的场景深度或重建的网格实现虚拟物体和环境的真实遮挡效果，根据光照估计算法模拟阴影，实现逼真的虚实融合效果。
* 资源与生命周期管理
管理虚拟的 AR 资源、内容，覆盖其加载、展示、卸载等生命周期管理。
这些能力构成了典型 3D 引擎的核心职责。因此根据具体的项目需求，选择合适的 3D 引擎是快速实现 AR 效果的必要前提之一。
## 常见的 3D 引擎
EasyAR 支持多种 3D 引擎，包括常见的 3D 引擎如 Unity，Unreal 或者原生开发(Native)。 EasyAR 提供 Unity 和 Native 的样例及开发文档。
### Unity
Unity 定位通用实时 3D 引擎， 是当前大多数 AR 开发者的第一选择。Unity 原生支持 Windows/ macOS 以及 iOS / Android / visionOS 等跨平台开发。 Unity 生态成熟，文档与示例完善。
### Native
相较于使用 Unity 等高层封装引擎，直接基于原生图形 API（如 OpenGL、Vulkan、Metal）进行 AR 开发的优势可概括如下：系统依赖少，运行环境可极度精简，可深度定制相机模型及底层算法。原生 API 开发，工程成本和维护成本高，缺乏成熟编辑器与调试工具，迭代效率低，跨平台难度大，不利于产品级快速交付，通常用于一些简单功能的实现。
### Web
Web 无需安装，基于浏览器即可使用，分发和触达成本极低。 天然跨平台，适合快速上线与大规模用户访问。 开发门槛相对较低，前端生态成熟。
目前 Web 在 AR 应用中仍然较为受限，主要体现在性能受浏览器与安全沙箱限制对运动跟踪、遮挡、精确光照等 AR 核心能力支持不足，设备能力访问受限，稳定性和一致性难以保障。
因此 Web AR 适合“轻量展示与营销”，不适合高精度、强交互的复杂 AR 应用。
## 延伸阅读
* [Android Native 快速入门](quickstart-android.html)
* [iOS Native 快速入门](quickstart-ios.html)
* [Windows Native 快速入门](quickstart-windows.html)
* [Unity 快速入门](../../unity/getting-started/quickstart.html)

---

## 在 Android 应用中启用 EasyAR 功能
- 章节路径: `native/getting-started/enable-easyar-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/enable-easyar-android.html

# 在 Android 应用中启用 EasyAR 功能
本章介绍如何在 Android Studio 中配置 EasyAR 的 Android 工程，无需使用 Unity 等 3D 引擎。
## 准备工作
开始之前，您需要准备：
* 最新版本的 Android Studio
* JDK 8/11/17
* Android Gradle Plugin 4.0 或以上
* Android NDK r28 或以上
* 获取 EasyAR 授权许可证
* 选择 EasyAR Sense [发布版本并下载](variants.html)
> **注意**
并非所有安卓设备均支持 EasyAR Sense 的所有功能，部分功能依赖额外硬件或配置，具体可查阅对应功能支持的设备列表。
## 导入 EasyAR Sense for Android
本节介绍如何在**非 Unity 的 Android 工程**中导入 EasyAR Sense SDK。 EasyAR Sense 提供 Java 和 C++ API，并支持 Kotlin，您可以使用最习惯的语言进行开发。
由于不同 IDE 的配置方式可能存在差异，这里仅说明**基于 Android Studio + Gradle 的典型配置方式**。
### 选择 API 使用方式
EasyAR Sense for Android 提供两种 API 使用方式：
* 仅使用 Java API
* 使用 Java 和 C++ API
请根据项目需求选择其中一种进行配置。
#### 仅使用 Java API
当仅使用 EasyAR 的 Java API 时，**无需配置 NDK**。
将 `EasyAR.aar` 放入`app/libs/` 或 Gradle 指定目录。
#### 使用 Java 和 C++ API
当需要同时使用 EasyAR 的 C++ API 时，需要同时配置 Java 依赖与原生库。
* Java 层文件
将 `EasyAR.jar` 放入 `app/libs/` 或 Gradle 指定路径。
* 原生库（`.so`）
将 EasyAR 提供的原生库按 ABI 放入以下路径或 Gradle 指定路径。
```
app/src/main/jniLibs/
├── armeabi-v7a/
│ └── libEasyAR.so
└── arm64-v8a/
└── libEasyAR.so
```
* C++ 头文件
将 EasyAR SDK 中 `include` 目录下的 `easyar` 文件夹拷贝到以下路径或 `Android.mk`/`CMakeLists.txt` 指定路径。
```
app/src/main/jni/easyar/
```
头文件路径需在 `Android.mk` 或 `CMakeLists.txt` 中显式指定。
### Gradle 配置说明
当您使用 C++ API 时，需要在 Gradle 中启用 Native Build, **仅适用 Java API 无需配置**。 您可以使用 ndk-build（Android.mk）进行配置。
在 `app/build.gradle` 中添加：
```
android {
externalNativeBuild {
ndkBuild {
path "src/main/jni/Android.mk"
}
}
}
```
>
> 如果使用 CMake，请参考
[> Google 官方文档
](https://developer.android.google.cn/studio/projects/add-native-code.html)> 进行配置。
>
### NDK 配置
#### 声明 EasyAR 为预编译库
```
include $(CLEAR\_VARS)
# 确保该路径指向 jniLibs 中当前 ABI 目录
LOCAL\_PATH := $(LOCAL\_PATH\_TOP)/../jniLibs/$(TARGET\_ARCH\_ABI)
LOCAL\_MODULE := EasyAR
LOCAL\_SRC\_FILES := libEasyAR.so
include $(PREBUILT\_SHARED\_LIBRARY)
```
#### 链接 EasyAR 与系统库
```
LOCAL\_SHARED\_LIBRARIES += EasyAR
# OpenGL ES（必需）
LOCAL\_LDLIBS += -lGLESv3
```
>
> EasyAR 运行至少需要 OpenGL ES 2.0，推荐使用 OpenGL ES 3.0（GLESv3）。
>
### 指定 ABI 架构
在 `app/build.gradle` 中显式指定 ABI，避免无效架构被打包：
```
android {
defaultConfig {
ndk {
abiFilters "armeabi-v7a", "arm64-v8a"
}
}
}
```
如果只需要其中一种架构，可只保留对应项。
### AndroidManifest 权限配置
EasyAR Sense 需要以下权限，缺失将导致初始化失败或黑屏：
```
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
```
完整示例：
```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
package="cn.easyar.samples.helloar">
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
</manifest>
```
### 初始化 EasyAR
在应用启动时调用 `Engine.initialize` 进行初始化。
示例（Java）：
```
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
Engine.initialize(this, key);
}
```
> **注意**
初始化必须在使用 EasyAR 相关功能之前完成。
## 额外配置
在 Android 平台上，根据系统版本及所使用的功能不同，可能还需要注意以下配置和限制。
### 配置使用 ARCore
如果项目中使用 **ARCore**，请参考其官方文档完成 `AndroidManifest.xml` 和 `build.gradle` 的相关配置。
此外，在初始化 EasyAR 之前，必须显式加载 ARCore 的原生库：
```
System.loadLibrary("arcore\_sdk\_c");
```
> **注意**
使用 **ARCore v1.19.0 之前的版本**时，在 **Android 11** 上将无法被检测到。
这是由于 Android 11 开始引入了应用可见性限制，需要在 `AndroidManifest.xml` 中声明 ARCore 包名。
```
<queries>
<package android:name="com.google.ar.core" />
</queries>
```
### 配置混淆（ProGuard）
如果对 Java 代码启用混淆，需要 **排除 `cn.easyar` 命名空间**。
EasyAR Sense 在运行时会通过 JNI 使用 **类名反射获取 Java 类型**。
如果 `cn.easyar` 下的类被混淆或重命名，可能导致未定义行为。
#### 基本规则
```
-keep class cn.easyar.\*\* { \*; }
```
#### 推荐的精确规则
```
-dontwarn javax.annotation.Nonnull
-dontwarn javax.annotation.Nullable
-keepattributes \*Annotation\*
-keep class cn.easyar.RefBase { native <methods>; }
-keepclassmembers class cn.easyar.\* {
<fields>;
protected <init>(long, cn.easyar.RefBase);
}
-keep,allowobfuscation interface cn.easyar.FunctorOf\* { \*; }
-keep class cn.easyar.Buffer { native <methods>; }
-keep class cn.easyar.Engine { native <methods>; }
-keep class cn.easyar.JniUtility { native <methods>; }
-keep class cn.easyar.engine.\*\* { \*; }
-keep class cn.easyar.CameraParameters
-keep interface cn.easyar.FunctorOfVoidFromInputFrame
```
上述 ProGuard 规则 **已包含在 EasyAR 的 aar 库中**，通常无需重复配置。
### Scoped Storage
Android 10 开始引入的 **Scoped Storage（分区存储）** 机制，会对部分依赖文件路径的 API 造成影响。这是由于 /sdcard 下的非媒体路径（如自定义目录）在 Android 10 上无法直接访问所致。对 EasyAR 的影响体现在部分需要传入文件路径的 API（如录屏）在 Android 10 上，不支持直接读写媒体路径，但是在 Android 11 上可以正常工作。
**解决方式**：
* 简便方案（Android 10）
在 `AndroidManifest.xml` 中禁用 Scoped Storage：
```
<application
android:requestLegacyExternalStorage="true"
... >
</application>
```
* 推荐方案
* 仅使用应用内部存储
* 或通过 MediaStore 与媒体路径进行数据交换
### Android Gradle Plugin 与 NDK
自 NDK r22 起，默认使用 LLD 链接器，并需要配合 `llvm-strip` 使用；这与 Android Gradle Plugin 4.0 以下版本内置的 `strip` 工具不兼容。
**解决方式**:
* 升级至 **Android Gradle Plugin 4.0 或以上**
* 或在 `packagingOptions` 中使用 `doNotStrip` 禁用 stripping（不推荐）
### Windows 路径长度限制
在 Windows 系统上，如果工程中任意文件（包括构建过程中生成的临时文件）的**绝对路径长度超过 260 个字符**，
可能会导致 Android Studio 构建失败。
**解决方式**：
* 将工程放置在更短路径下（例如 `C:\\user\\project`）
* 避免过深的目录层级
## 延伸阅读
* [EasyAR Mega 支持的设备](../../mega/devices.html)
* [图像跟踪支持的设备](../../image-tracking/devices.html)
* [运动跟踪支持的设备](../../motion-tracking/devices.html)
* [稀疏空间地图支持的设备](../../sparse-spatial-mapping/devices.html)
* [稠密空间地图支持的设备](../../dense-spatial-mapping/devices.html)
* [运动跟踪与 EasyAR 其他模块的关系](../../motion-tracking/motion-tracking-and-easyar.html)

---

## 在 iOS 应用中启用 EasyAR 功能
- 章节路径: `native/getting-started/enable-easyar-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/enable-easyar-ios.html

# 在 iOS 应用中启用 EasyAR 功能
本章介绍如何在 Xcode 中配置 EasyAR 的 iOS 工程 ， 而不需使用 Unity 等 3D 引擎。
## 准备工作
开始之前，您需要准备：
* Xcode 16 或更新版本
* 获取 EasyAR 授权许可证
* 选择 EasyAR Sense [发布版本并下载](variants.html)
## 使用 Objective-C 启用 EasyAR
1. 添加 Frameworks
在 `Frameworks, Libraries, and Embedded Content` 中添加 `easyar.xcframework`。
![addxframework1](https://doc-asset.easyar.com/develop/native/getting-started/media/xfframework.png)
2. 禁用 Bitcode
EasyAR 不使用 bitcode 也不提供 bitcode 兼容性, 需要在配置中禁用 bitcode。
![disablebitcode2](https://doc-asset.easyar.com/develop/native/getting-started/media/disablebitcode.png)
3. 初始化 EasyAR
使用 `easyar\_Engine` 的 `initialize:` 方法来初始化 EasyAR 。您可以添加初始化代码如下
```
[easyar\_Engine initialize:key];
```
4. 隐私配置
由于 AR 要使用摄像头，隐私配置需要添加 `Privacy - Camera Usage Description`，
![campermission](https://doc-asset.easyar.com/develop/native/getting-started/media/camerapermission.png)
如果要使用录屏功能，隐私配置需要添加 `Privacy - Microphone Usage Description`，
![microphonepermission](https://doc-asset.easyar.com/develop/native/getting-started/media/mcpermission.png)
## 通过 Swift API 启用 EasyAR
EasyAR Sense Swift API 是以源代码形式提供的，这样可以提供最好的兼容性（苹果从 Swift 5 开始提供 ABI 兼容）。
使用 EasyAR Sense Swift API 需要首先创建一个 framework 工程，然后将 framework target 嵌入到你的工程中。
### 创建 EasyARSwift framework 工程
1. 创建一个 Cocoa Touch Framework 类型的新工程并命名为 `EasyARSwift`
你可以选择将 EasyARSwift 工程嵌入到你的 app 工程里面或创建独立的工程。
![embedprj](https://doc-asset.easyar.com/develop/native/getting-started/media/embedproject.png)
2. 导入EasyAR Swift 代码到 EasyARSwift 工程
![embedswiftcode2](https://doc-asset.easyar.com/develop/native/getting-started/media/embedproject.png)
XCode 自动生成的 EasyARSwift.h 文件并没有被使用，可以安全删除。
3. 在 build settings 中配置 `Objective-C Bridging Header`
![bridgeheader](https://doc-asset.easyar.com/develop/native/getting-started/media/bridgingheader.png)
> **注意**
这个选项在导入 swift 文件之前不会显示在 XCode 选项中，所以请一定先导入 Swift 代码再进行配置更改。
4. 导入 `easyar.xcframework` 到 EasyARSwift 工程中
![addxframework3](https://doc-asset.easyar.com/develop/native/getting-started/media/xfframework.png)
5. 关闭 Bitcode
EasyAR 不使用 bitcode 也不提供 bitcode 兼容性, 需要保证在配置中禁用 bitcode。
![disablebitcode](https://doc-asset.easyar.com/develop/native/getting-started/media/disablebitcode.png)
6. Deployment Target
根据您的 app 工程修改 `deployment target`，保证 EasyARSwift 工程的 `deployment target`比 app 工程的小或相等。
![setdeploytarget](https://doc-asset.easyar.com/develop/native/getting-started/media/setdeploytarget.png)
### 嵌入和使用 EasyARSwift framework
1. 在工程中嵌入 EasyARSwift framework
![embedswiftfw](https://doc-asset.easyar.com/develop/native/getting-started/media/embedsffw.png)
![embedswiftfw2](https://doc-asset.easyar.com/develop/native/getting-started/media/embedsffw2.png)
2. 在 Swift 源代码中 `import EasyARSwift`
![importeasyswift](https://doc-asset.easyar.com/develop/native/getting-started/media/importeasyswift.png)
代码书写方式可以参考 `HelloARSwift` 样例中的代码或 API Reference 。

---

## 运行 EasyAR Android 样例
- 章节路径: `native/getting-started/quickstart-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-android.html

# 运行 EasyAR Android 样例
本文介绍如何运行 EasyAR 提供的原生 Android 样例。这里以 HelloAR 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下环境：
* Android Studio 2025.1.2 或更高版本
* JDK 17
* Android NDK r28
* Android 手机
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key，注意包名与样例一致，如 HelloAR 应为 `cn.easyar.samples.helloar`
## 导入并编译样例
1. 在 Android Studio 菜单依次选择 `File -> New -> Import Project...`，选择样例所在目录导入，等待 Android Studio 完成下载和配置。
![importhelloar](https://doc-asset.easyar.com/develop/native/getting-started/media/android-studio-import-hello-ar.png)
2. 设置许可证（License Key）
根据路径找到 ARActivity.java，按照代码提示填入开发中心获取的 License Key。
![fillkey](https://doc-asset.easyar.com/develop/native/getting-started/media/android_hello_ar_fill_in_key.png)
1. 编译并运行
连接手机到电脑上，点击运行按钮，按提示在手机上运行。
![buildandrun](https://doc-asset.easyar.com/develop/native/getting-started/media/android-build-run.png)
HelloAR 实现了对平面图像的识别跟踪并叠加虚拟物体的功能。样例中识别图像在 `assets/sightplus` 路径下找到。
HelloAR 样例的运行效果如下。
![rungif](https://doc-asset.easyar.com/develop/native/getting-started/media/android-helloar.gif)
## 相关阅读
* [运行 EasyAR iOS 样例](quickstart-ios.html)
* [运行 EasyAR Windows 样例](quickstart-windows.html)

---

## 运行 EasyAR 的 iOS 样例
- 章节路径: `native/getting-started/quickstart-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-ios.html

# 运行 EasyAR 的 iOS 样例
本文介绍如何运行 EasyAR 提供的原生 iOS 样例。这里以 HelloAR 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下环境：
* Xcode 16 或更高版本
* ARM64 CPU 的 iPhone 或 iPad 真机
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key，注意包名与样例一致，如 HelloAR 为 `cn.easyar.samples.helloar`
## 导入并编译样例
1. 使用 Xcode 打开下载解压的样例，如 `helloar.xcodeproj`
![openiossample](https://doc-asset.easyar.com/develop/native/getting-started/media/openiossample.png)
2. 设置许可证（License Key）
根据路径找到 `ViewController.m`，按照代码提示填入开发中心获取的 License Key。
![xcodefillkey](https://doc-asset.easyar.com/develop/native/getting-started/media/ios-fill-key.png)
3. 编译并运行
连接手机到电脑上，点击运行按钮，按提示在 iPhone /iPad 上运行样例。
HelloAR 实现了对平面图像的识别跟踪并叠加虚拟物体的功能，摄像头对准识别图（在 `assets` 文件夹下也可以找到）即可体验效果。
![namecard](https://doc-asset.easyar.com/develop/unity/headsets/media/namecard.jpg)
## 相关阅读
* [运行 EasyAR 安卓样例](quickstart-android.html)
* [运行 EasyAR Windows 样例](quickstart-windows.html)

---

## 运行 EasyAR Windows 样例
- 章节路径: `native/getting-started/quickstart-windows.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-windows.html

# 运行 EasyAR Windows 样例
本文介绍如何运行 EasyAR 提供的原生 Windows 样例。这里以 HelloARQt 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下内容
* Visual Studio 2022 或更高版本 (有 `.vcxproj` 工程的样例)
* CMake 3.8 或更高版本 (有 `CMakeLists.txt` 的样例)
* Qt 5.4 或更高版本 (Qt 样例)
* (USB) 摄像头，插入状态并可以正常工作。
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key
> **注意**
请确保 Visual Studio 的 C++ 支持库已经安装，这些在 Visual Studio 的默认安装情况下不会自动安装。
## 编译运行 EasyAR 的 Windows 的样例
以下以 HelloARQt 为例介绍如何编译运行 EasyAR 官方 Windows 的样例。
1. 打开 CMake，指定 `where is the source code` 目录为下载解压的样例目录，设置 binary 文件的路径。
2. 点击 `Configure`, 在弹出的窗口中，选择系统的 Visual Studio 版本。如果某些路径（如 Qt）没有自动设置报错，需要手动修改，重新 `Configure`，直至没有错误。
![sample1](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample1.png)
3. 点击 `Generate`，生成工程文件。
![sample2](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample2.png)
4. 点击 `Open Project`，在 Visual Studio 中打开工程。
![sample3](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample3.png)
5. 在 Visual Studio 点击运行，在运行窗口的输入框里填写官网获取的 License Key，点击 `Start` 运行样例。
![sample4](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample4.png)
## 常见问题
1. 如果运行时提示找不到 Qt，解决方案是添加 Qt 路径到 PATH 环境变量，注销并重新登录计算机。
2. 上面介绍的 HelloARQt 是**运行时**输入 License Key ，但是也有样例需要在**运行前**填写许可证，通常在 `initialize` 代码处，如 HelloAR 样例的 License 在 `main.cc` 中填写。
![sample5](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample5.png)
## 相关阅读
* [运行 EasyAR 安卓样例](quickstart-android.html)
* [运行 EasyAR iOS 样例](quickstart-ios.html)

---

## 选择 EasyAR Sense 发布版本
- 章节路径: `native/getting-started/variants.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/variants.html

# 选择 EasyAR Sense 发布版本
在原生开发前，需要您在官网注册并获取授权许可证，然后选择[下载对应的发布版本](https://www.easyar.cn/view/download.html)。
EasyAR Sense 分为社区版和企业版，两者授权不同，下载时需要按照许可证选择对应的文件。
* **Sense 社区版**：支持个人版、专业版、经典版的许可证。
* **Sense 企业版**：支持企业版许可证。
您下载的社区版或企业版 EasyAR Sense 均有多个发布版本，主要区别是包含的功能差异，您可以根据实际需要选择相应的发布版本。
* 社区版发布版的不同
* 社区版（Community）
包含运动跟踪、稀疏空间地图、稠密重建地图、物体跟踪、表面跟踪、平面检测等基础 AR 功能。
* 社区 R 版（CommunityR）
在社区版的基础上，额外支持 Recorder 和 VideoPlayer 功能。
* 社区 Full 版（CommunityFull）
在社区版的基础上，支持安卓平台的惯性导航功能。
* 企业版发布版的不同
* 企业（Enterprise）
包含运动跟踪、稀疏空间地图、稠密重建地图、物体跟踪、表面跟踪、平面检测等基础 AR 功能，包含企业定制功能。
* 企业 Full 版（EnterpriseFull）
在企业版的基础上，支持 Android 平台的惯性导航功能。
> **注意**
Full 版本（社区版/企业版）加入惯性导航功能，主要用于 Mega 上一些不支持 6DoF 运动跟踪功能的设备。由于包体增加比较明显，如您的应用不依赖 Mega，通常不需要 Full 版本。
## 相关阅读
[EasyAR Sense 授权许可](../../license-sense.html)

---

## EasyAR Sense 1.0 发行说明
- 章节路径: `native/release-notes/release-notes-1_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_0.html

# EasyAR Sense 1.0 发行说明
## 1.0.1
2015-10-21
EasyAR 1.0.1 修复了一些 bug，增强了用户体验。
从这个版本开始 sample 代码和 SDK 将分开打包，在网站上通过不同链接下载 （sample code 也有部分更新）。
自 EasyAR 1.0.0 版本开始的详细更新内容如下。
>
> + 添加更明显的错误信息输出
>
> + 添加使用必读
>
> * 修正在某些情况下启动速度慢的问题
>
> * 修正跟踪很容易丢失的问题
>
> * 修正在某些情况下 unity 编辑器中初始化失败的情况（即使已经填写正确的 Key）
>
> * 提升运行效率
>
> * 将示例代码单独打包
>
> * 其它修正
>
## 1.0.0
2015-10-14
EasyAR SDK 正式版本开放下载！

---

## EasyAR Sense 1.1 发行说明
- 章节路径: `native/release-notes/release-notes-1_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_1.html

# EasyAR Sense 1.1 发行说明
## 1.1.0
2015-11-29
EasyAR 1.1.0 对视频播放功能和 Unity 的支持做了大量改进，完整支持 Unity 5，增强了用户体验。
同时，这个版本增加了包括 Unity 端和本地端的大量可直接运行的样例。这些样例演示了各种 target 的创建方式和包含流媒体和透明视频在内的视频播放，以及更加高级的实时 target 创建和 AR 涂涂乐。
从这个版本开始 Unity 的 sample 代码和 SDK 将分开打包，在网站上通过不同链接下载。
样例中大多数 marker 都可以使用“视+”通过云识别来玩。这里面许多是有趣的 AR 游戏。下载
视+（ [http://www.sightp.com](http://www.sightp.com) ），一起来玩吧！
自 EasyAR 1.0.1 版本开始的详细更新内容如下。
>
> + 添加更多完整实例（单独的压缩包）
>
> + 添加透明视频支持
>
> + 完整支持 Unity 5
>
> + Unity: 添加/改善许多接口
>
> + Unity: 添加获取同步 Frame 的接口
>
> + Unity: 添加设置 Target 或 Augmenter 为世界中心的选项（该选项可在 Augmenter 物体上找到）
>
> + Unity: 开放 ARBuilder 脚本，提供从头构建 EasyAR 的参考实现
>
> * 更加完善的视频播放支持（接口有变化）
>
> * 更加完善的前置摄像头和动态摄像头切换支持
>
> * Unity: 完善 ImageTarget 在 Inspector 面板中的设置
>
> * Unity: 完善错误信息显示和新手导引
>
> * Unity: 修正 Target transform 变化后的显示
>
> * Unity5: 修正 iOS 上白屏问题
>
> * 其它修正和完善
>
> * 将 Unity 示例单独打包
>

---

## EasyAR Sense 1.2 发行说明
- 章节路径: `native/release-notes/release-notes-1_2.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_2.html

# EasyAR Sense 1.2 发行说明
## 1.2.1
2016-02-19
EasyAR 1.2.1 主要修复了 1.2.0 的一个使用问题，同时对跟踪算法做了一部分优化。这个问题只有在不正确的设置了 target 的 size 的时候才会出现，这个版本将可以容许这样的输入。
自 EasyAR 1.2.0 版本开始的详细更新内容如下。
>
> * 修正当输入 size 比例不正确的时候的闪烁和难以识别问题
>
> * 优化跟踪算法
>
## 1.2.0
2016-02-05
EasyAR 1.2.0 有两个使用体验上的显著改进。
1. 跟踪稳定性大幅提升，跟踪过程更加准确和鲁棒。
2. Unity3D 用户将不再需要在 Windows 系统中安装 Visual C++ 2015 RedistributablePackage。很多 Windows8.1 的用户将从中受益。
自 EasyAR 1.1.0 版本开始的详细更新内容如下。
>
> + 大幅提升跟踪稳定性和准确性
>
> + Unity: 移除 Visual C++运行时库依赖
>
> + Unity: 添加对 Unity 5.3+ OpenGLCore 的支持
>
> + Unity: 添加更多针对首次使用的引导
>
> + Unity: 添加关闭显示视频不支持信息的选项
>
> * 修正某些情况下 iOS 视频播放黑屏
>
> * 修正某些 Android 设备视频播放不正常
>
> * Unity: 微调整某些接口
>
> * Unity: 修正 invalid aabb
>
> * Unity: 修正 Unity 5 使用 prefab 创建场景灰屏
>
> * Unity: 修正 postbuild 脚本对 Unity 4.7 的兼容性
>
> * 其它修正和完善
>
> * 在发布包中添加一个 Unity 样例
>

---

## EasyAR Sense 1.3 发行说明
- 章节路径: `native/release-notes/release-notes-1_3.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_3.html

# EasyAR Sense 1.3 发行说明
## 1.3.1
2016-07-29
EasyAR 1.3.1 主要修复了某些 Android 设备的兼容性问题，并增加了中文路径（json 文件和图像路径）支持。
自 EasyAR 1.3.0 版本开始的详细更新内容如下。
>
> + 添加中文路径支持
>
> + 添加 json 文件中对"meta"数据的支持
>
> * 修正 UTF-8-BOM 编码的 json 文件解析
>
> * 修正在某些 Android 设备（Nexus 5s/6）上的 camera 显示问题
>
## 1.3.0
2016-05-28
EasyAR 1.3.0 增加了一些新特性并有很多改进，主要集中在这几方面：
1. 支持多目标。
EasyAR 现在可以支持同时跟踪多个目标。可以使用一个 tracker 进行多目标同时跟踪，也可以在不同 tracker 中加载不同的 target 来同时跟踪。EasyAR 支持运行时动态修改最大跟踪目标个数。更多使用细节请参考 [EasyAR Multi-Target](../../image-tracking/intro.html) 。
2. 接口修改，使用更加灵活。
这个版本和之前版本相比，一部分接口有所调整，但整体框架没有太大的变动。你现在可以像搭积木一样使用 EasyAR 的 Unity 基础 prefab，这个版本中也添加了很多预先搭好的模块以供参考。
3. 优化检测和跟踪，减少抖动。
4. 性能优化和降低功耗。
详细更新内容如下：
>
> + 添加多目标支持
>
> + 添加多目标的典型样例
>
> + 添加同时跟踪目标和识别二维码的样例
>
> + 提升检测和跟踪效果，减少抖动
>
> + 优化算法降低功耗
>
> + 添加直接画到 texture 的接口
>
> + 添加显式水平翻转相机输入的接口
>
> + 添加禁止 Android 自动旋转检测的接口
>
> + 添加设置外部旋转的接口
>
> + Unity: 优化渲染效率
>
> + Unity: 添加多个组合了基础 prefab 的常用 prefab
>
> + Unity: 添加 EasyARBehaviour，用以输入 key 并进行初始化，并显式处理 pause/resume/quit 事件
>
> + Unity: 添加显示/隐藏 RealityPlane 的选项
>
> + Unity: 添加使用索引打开 camera 的接口
>
> + Unity: 添加对自定义硬件设置旋转偏移的接口
>
> + Unity: 修改 AugmentedTarget 接口，支持在 FrameUpdate 事件中进行自定义的姿态滤波
>
> + Unity: 修改 Target 事件处理接口
>
> * 调整部分接口
>
> * 修正切换场景时的内存泄漏
>
> * 修正在暂停并恢复之后找到虚假的目标
>
> * 修正使用透明 PNG 图像的 target 检测
>
> * 修正因 key 中的空格导致的初始化失败
>
> * 修正 iOS 和 mac 某些分辨率下 camera 显示错误
>
> * 修正 native iOS 样例在切换到后台时崩溃
>
> * Unity: 修正在图像高比宽大的时候 ImageTarget mesh 显示错误
>
> * Unity: 修正在 OnFound 事件中重置 target
>
> * Unity: 修正 camera 打开之后有可能出现的白色帧
>
> * Unity: 修正 Augmenter 中心模式下的 TargetOnTheFly 和 Coloring3D 样例
>
> * Unity: 修正 TargetOnTheFly 样例在某些情况下崩溃的问题
>

---

## EasyAR Sense 2.0 发行说明
- 章节路径: `native/release-notes/release-notes-2_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_0.html

# EasyAR Sense 2.0 发行说明
## 2.0.0
2017-05-29
从 SDK 2.0 版本开始，EasyAR 将有两个产品，EasyAR SDK 和 EasyAR CRS (云识别服务)。EasyAR SDK 将有两个子版本，EasyAR SDK Basic 和 EasyAR SDK Pro。
EasyAR SDK 2.0 Pro 是个全新版本的 SDK，除了拥有 EasyAR SDK Basic 所有功能之外，还有更多激动人心的特性。EasyAR SDK Pro 是收费的 SDK，关于费用定价、付款方式等详细信息可以在 EasyAR 网站上查看。EasyAR SDK Pro 同时提供免费试用，试用期间 APP 每天的启动次数将会受限。
EasyAR SDK Pro 有这些全新特性：
1. 3D 物体跟踪
对日常生活中的常见有纹理 3D 物体进行实时识别与跟踪。
2. SLAM
单目实时 6 自由度相机姿态跟踪。
3. 录屏
高效易用的录屏功能。
EasyAR CRS 是云端图像识别服务，现在已经开放使用，可以在云端动态管理识别图，在 SDK 中使用对应 API 可以使用云服务识别云端存储的识别图，并从云端获取和识别图相关联的数据信息。EasyAR CRS 是收费服务，关于费用定价、付款方式等详细信息可以在 EasyAR 网站上查看。EasyAR CRS 同时提供免费试用，可以零成本测试相关功能。
EasyAR SDK 2.0 Basic 是 EasyAR SDK 1.x 的升级版。这个版本可以免费商用。EasyAR 1.x 的所有功能仍旧可以在这个版本中找到，我们没有添加任何限制或水印。EasyAR SDK 2.0 Basic 有许多改进，主要集中在这几方面：
1. 工作流和 API 改变
EasyAR 处在演化过程中，新的工作流将有更多的灵活性。我们正在完善的 EasyAR 一站式解决方案也将带给 2.0 越来越多的灵活性。这个改变在 Unity API 中表现的并不很明显，不过有些组件的名字已经变化。
2. 全新的编程语言支持
EasyAR SDK 现在导出了纯 C 接口，赋予开发者更大的自由空间。同时我们添加了对很多编程语言的支持，包括 C/C++11/traditional C++/Java for Android/Objective-C for iOS。所有的语言都有一个样例来演示基本的使用方式。我们会在未来的小版本升级中添加更多的语言支持。
3. 云识别支持
EasyAR SDK 现在内置云识别支持。
4. 许多改进、bug 修复和兼容性提升
我们提升了二维码的检测效果，调整了很多 API 以达到更高的灵活度。这个版本修复了许多 bug，包括在部分 Android 机型上显示不正确的问题和一些内存相关的问题。同时我们还提升了 EasyAR SDK 与 AMD CPU 的兼容性以及与 Unity3D、Google VR SDK 等第三方 SDK 的兼容性。
详细更新内容如下：
>
> ++ 全新的编程语言支持：C/C++11/traditional C++/Java for Android/Objective-C for iOS
>
> ++ 所有编程语言和不同 IDE 的 sample
>
> ++ 工作流和 API 变化
>
> ++ 云识别
>
> ++ 3D 跟踪 (pro)
>
> ++ SLAM (pro)
>
> ++ 录屏 (pro)
>
> + SDK API 导出为 C 接口，更容易在所有平台上导入其他语言
>
> + 添加 camera 权限申请 API
>
> + 添加 camera 缩放 API
>
> + 提升二维码检测效果
>
> + 优化内存使用
>
> + Unity: 添加默认的 found/lost 行为
>
> + Windows: DLL 将不再依赖于 CRT
>
> + Windows: 添加两个样例：一个关于如何使用 API，另一个演示在 Qt5 中的集成
>
> + Android: 添加 native 库文件的自定义加载路径和选择性加载支持
>
> - Unity: 删除了大部分非 behaviour API（所有功能被移动到了 behaviour 中）
>
> * 修复对 AMD CPU 的兼容性
>
> * 修复某些情况下渲染 camera 图像导致的 GL 状态污染
>
> * 修复视频播放前的黑色块
>
> * Unity: 修复 Unity 4.x 中 target 加载状态总是返回 true
>
> * Unity: 修复 Unity 5.0.0 和部分其他版本中屏幕闪烁
>
> * Windows: 修复某些情况下窗口关闭时崩溃
>
> * Android: 修复某些情况下调用 close 之后 camera 延迟关闭
>
> * Android: 修复从 native 线程中调用 camera API 崩溃
>
> * Android: 修复内存抖动和频繁 GC
>
> * Android: 修复在某些设备上 camera 的显示
>
> * Android: 修复某些类型 PNG 图像的加载和跟踪问题
>
> * iOS: 修复某些情况下关闭 camera 随机崩溃
>
> * iOS: 修复由于不兼容的 RTTI 配置导致的在与某些 SDK（比如 Google VR SDK）一起使用时出现的未被处理的异常（通常是 domain error）
>
> * iOS: 修复视频播放位置的时间单位
>

---

## EasyAR Sense 2.1 发行说明
- 章节路径: `native/release-notes/release-notes-2_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_1.html

# EasyAR Sense 2.1 发行说明
## 2.1.0
2017-09-08
EasyAR SDK 2.1.0 增加了一些新特性，并针对使用稳定性做了增强，主要集中在这几方面：
1. 新的编程语言支持。
EasyAR 现在支持使用 iOS 的 Swift 和 Android 的 Kotlin 进行编程。我们同时添加了在 EasyAR SDK 中使用 Swift 和 Kotlin 的样例。
2. Android arm64 支持。
EasyAR SDK 将从 2.1 版本开始添加 Android arm64-v8a 架构的文件。
3. Bug 修复和稳定性增强。
我们修复了一些由 EasyAR SDK 2.0 版本引入的 bug，包括调用 ImageTarget.setupAll 时产生的 local reference table overflow 以及 iOS 11 视频播放失败。我们同时修复了 camera 图像在屏幕上显示色彩失真的一个长期存在的问题。
详细更新内容如下：
>
> + 添加新的编程语言支持：Swift for iOS
>
> + 添加 Android 使用的 arm64-v8a 库文件
>
> + 添加新接口（Buffer），实现在 Android Java API 中访问图像数据
>
> + 添加 Android Kotlin 样例
>
> + 添加 iOS dynamic framework 样例
>
> * All: 所有接口都不会抛出异常
>
> * All: 修复 camera 图像在屏幕显示的色彩失真
>
> * Unity: 修复 iOS Unity 录屏后的系统杂音
>
> * Unity: 如果 OnPreRender 中修改了 RevertBackfacing，会在 OnPostRender 中重置
>
> * Unity: 添加 ObjectTargetBaseBehaviour 中缺失的 LoadList*接口
>
> * Unity: 默认不在 AndroidManifest 中添加音频权限
>
> * Unity: 修改容易产生误导的错误信息，"EasyAR is running on an unsupported graphics device" 改为 "EasyAR is running with an unsupported graphics API"
>
> * Android: Engine API 已经可以替换 cn.easyar.engine.EasyAR。cn.easyar.engine.EasyAR 已经弃用并将在今后版本中移除
>
> * Android: 修复调用 ImageTarget.setupAll 配置大量 target 时可能产生的 local reference table overflow
>
> * Android: 修复在 Android 平板和眼镜上 SLAM 不正常的漂移
>
> * Android: 修复在某些罕见 Android 设备上拒绝 camera 权限导致的崩溃
>
> * Android: 改善在某些罕见 Android 设备上的 camera 分辨率选择策略
>
> * iOS: 修复 iOS 11 视频播放
>
> * iOS: framework 将不会再包含签名
>
> * iOS: 修复在某些设备上的某些分辨率下 camera 显示问题
>
> * iOS: 修复录屏内存泄漏
>
> * Sample: 重命名 Unity 样例代码的文件名和 namespace，划分样例代码和 SDK 的明确边界
>
> * Sample: 删除 HelloARCloud 样例中的本地目标
>
> * Sample: 改善 Android/iOS HelloARQRCode 样例中 QR Code 检测到之后的信息显示
>
> * Sample: 在 iOS Unity 上默认打开 IL2CPP
>
> * 其它修正和完善
>

---

## EasyAR Sense 2.2 发行说明
- 章节路径: `native/release-notes/release-notes-2_2.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_2.html

# EasyAR Sense 2.2 发行说明
## 2.2.1
2018-10-24
EasyAR SDK 2.2.1 修复了在 Android 8、iPhone XS/XS Max 以及 Unity 2018 上的一些兼容性问题。
详细更新内容如下：
>
> + 提升 EasyAR CRS 连接的安全性
>
> * 修复了在 Android 8 及新版本上 ARSceneTracker 停止时崩溃
>
> * 修复了在 Unity 2018 上使用 Android/iOS/Mac 发布黑屏
>
> * 修复了在 iPhone XS/XS Max 上的崩溃
>
## 2.2.0
2018-03-06
EasyAR SDK 2.2.0 对图像跟踪做了大幅改进。这个版本中 ImageTracker 变得更加稳定，跟踪不易丢失，同时姿态的抖动也有所减弱。算法默认将以最高质量模式运行，可以通过选择 ImageTracker 的不同模式来平衡跟踪运行效率和质量。
详细更新内容如下：
>
> + 优化图像跟踪算法
>
> + 添加 ImageTracker 模式选择的接口
>
> * 修复在 Java 接口中使用非 ASCII 字符造成的崩溃
>
> * 修复某些类型 PNG 图像在某些硬件下的加载和跟踪问题
>
> * 修复在使用多个 camera 实例的时候，某些情况下 camera 打开失败
>
> * 修复在经打开的 camera 在未关闭的情况下再次调用打开接口时崩溃
>
> * 修复录屏缩放模式无效
>
> * 修复在某些情况下录屏关闭时崩溃
>

---

## EasyAR Sense 2.3 发行说明
- 章节路径: `native/release-notes/release-notes-2_3.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_3.html

# EasyAR Sense 2.3 发行说明
## 2.3.0
2018-10-24
EasyAR SDK 2.3.0 对图像跟踪的抖动问题做了大幅改进。这个版本同时包含对 Android 8、iPhone XS/XS Max 以及 Unity 2018 的一些兼容性修复。
详细更新内容如下：
>
> + 优化图像跟踪算法
>
> + 提升 EasyAR CRS 连接的安全性
>
> * 修复了在 Android 8 及新版本上 ARSceneTracker 停止时崩溃
>
> * 修复了在 Unity 2018 上使用 Android/iOS/Mac 发布黑屏
>
> * 修复了在 iPhone XS/XS Max 上的崩溃
>

---

## EasyAR Sense 3.0 发行说明
- 章节路径: `native/release-notes/release-notes-3_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-3_0.html

# EasyAR Sense 3.0 发行说明
## 3.0.1
2019-07-26
EasyAR SDK 3.0.1 修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> * 增加 Windows 上对摄像头的 YUY2 和 I420 像素格式的支持，减少出现黑屏的情况
>
> * 修正 Objective-C 示例中的 Renderer 的多个实例状态不独立，导致第二次进入时会在 glDrawArrays 处崩溃的问题
>
> * 增加对每通道 16 位的 png 图片的支持
>
> * 修正 Unity HelloAR_Coloring3D 示例在非 OpenGLES 和屏幕旋转等情况下贴图坐标出错的问题
>
> * 修正 Unity 示例默认不自动调焦的问题
>
> * 修正 Unity 示例中运行的一瞬间模型仍然显示，之后才消失的问题
>
> * 去除 Unity 示例初始化成功界面提示
>
> * 在 Unity 示例中增加对第二摄像头的支持(例如：在 Windows/Mac 上内置摄像头之外的 USB 摄像头)
>
> * 将 ExternalCamera 改名为 CustomCamera 以减少歧义
>
## 3.0.0
2019-07-07
EasyAR SDK 3.0 是 EasyAR SDK 2.x 的升级版。EasyAR SDK 3.0 有许多改进，主要集中在这几方面：
1. 更灵活的基于数据流的组件化 API
EasyAR 的 API 在 3.0 版本中，对原有 API 按照数据流进行了组件化的组织，使得 EasyAR 可以更容易与其他系统进行对接，以满足更为灵活的需求。
在此基础上，实现了外部摄像头接入和外部算法接入。
扩展 Camera 接口支持接收图片帧用于 AR 识别和跟踪。AR 展示将不依赖于手机自带摄像头，只要设备能够检测到外部摄像头并获取到视频流，就可以通过将视频流转成图片帧的方式传入 EasyAR SDK 用于 AR 应用，从而帮助 EasyAR 开发者为 AR/VR/MR 眼镜、无人机以及 USB 设备开发应用。
新的 API 支持开发者接入 EasyAR SDK 自有算法（ImageTracker 等）以外的其他算法，提供更灵活的能力扩展。
2. 编程语言和平台支持
增加了 C# for .Net/Mono 支持。
将 C++11 接口升级到 C++17，采用 std::optional 来明确参数和返回值的可空性。
将 Kotlin 和 Swift 接口升级到最新版本，并改善对 Optional 的支持。
增加了 Android ARM64 支持。
非 OpenGLES2 的渲染 API 支持(除 VideoPlayer 和 Recorder 以外实现渲染 API 中立)。
3. 表面跟踪
针对小型 AR 交互游戏、AR 短视频拍摄以及产品放置展示等应用场景，EasyAR SDK 3.0 增加 Surface Tracking 功能，使用检测任意表面特征点计算跟踪，不需要消耗时间寻找平面，实现更快速的表面贴合及姿态跟踪。
4. Image Target Data 生成
支持在原生及 Unity 应用中将待识别的图片提前生成一个数据包，用于识别跟踪，提高识别图加载速度。
5. 降低包体大小
通过架构的结构性改进和功能裁剪，减小了 SDK 的包体大小。
当前版本中去除了二维码扫描等冗余功能，以换取更小的包体。
6. 许多改进、bug 修复和兼容性提升
详细更新内容如下：
>
> ++ 更灵活的基于数据流的组件化 API
>
> ++ 表面跟踪
>
> + Image Target Data 生成
>
> + 编程语言支持：C# for .Net/Mono 支持
>
> + 编程语言支持：C++11 升级到 C++17
>
> + 编程语言支持：Kotlin/Swift 升级并支持 Optional
>
> + Unity 插件重写并开源，底层 API 与非 Unity 统一
>
> + Unity 插件涂涂乐示例新增截取静态图像绘制小熊的功能
>
> + Unity 插件新增 key 填错等 UI 提示
>
> + Android ARM64 支持
>
> + 非 OpenGLES2 的渲染 API 支持(除 VideoPlayer 和 Recorder 以外实现渲染 API 中立)
>
> + 外部摄像头接入
>
> + 外部算法接入
>
> + 降低包体大小
>
> - 二维码识别功能移除
>
> - 渲染器移除，改为提供各平台示例渲染代码
>
> * 支持从内存加载识别图
>
> * CloudRecognizer 支持 https(Android 和 iOS 上)
>
> * Android CameraDevice 增加对 Camera2 的支持
>
> * 修正 Android 9.0 上录屏崩溃的问题
>
> * 支持 Unity 5.6, 2017.4, 2018.4, 2019.1，去除对 5.6 以下版本的支持
>
> * 去除对 iOS 7 及以下版本的支持
>
> * Unity 插件使用 CommandBuffer 绘制相机背景
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 3.1 发行说明
- 章节路径: `native/release-notes/release-notes-3_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-3_1.html

# EasyAR Sense 3.1 发行说明
## 3.1.0
2020-01-14
EasyAR Sense 3.1.0 从 4.0.0 中反向移植了许多设计优化和问题修复。
EasyAR Sense Unity 插件也更新到新版本，有了巨大提升。
详细更新内容如下：
EasyAR Sense
>
> + CameraDevice 增加了获得 camera 数量、索引，获得 camera 前后位置的功能（Mac 不支持）和以指定前后位置打开 camera 的功能
>
> + 增加了各组件汇报占用的 camera buffer 需求的功能，用于 CameraDevice.setBufferCapacity
>
> * 编程语言支持：Swift 升级到 Swift 5
>
> * 不再区分 Basic 和 Pro 二进制包
>
> * CloundRecognitionService 从使用 AppKey 改为使用 ApiKey
>
> * 修正 iOS 上只能使用有限种类分辨率的问题，使得 iPad 上能够使用最大视野
>
> * 修正部分 iPad 设备上 camera 分辨率较高时会崩溃的问题
>
> * 修正 Google Play Store Android App Bundle 支持
>
> * 修正 ImageTracker.unloadTarget 和 ObjectTracker.unloadTarget 无法卸载 target 的问题
>
> * 修复了一些稳定性问题
>
Unity Plugin for EasyAR Sense 3.1.0
>
> ++ 恢复类似 Sense 2.3 的接口设计和行为，并有非常多改进
>
> + 添加严重出错情况的弹出消息（可在 EasyARController 上关闭）
>
> + Components: 大多数组件可以使用 Unity 组件的 enabled 来控制 start/stop
>
> + Component ARSenssion: AR 入口，控制 center mode，具备支持外部设备的能力，比如自定义相机及 AR 眼镜
>
> + Component ARAssembly: 展示 EasyAR Sense 组件化 API 的组装过程，支持所有 EasyAR Sense 的组件
>
> + Component ImageTargetController: 改善对不同类型输入的支持，可以从本地文件系统或 web URL 加载图像和.etd 文件
>
> + Component CameraImageRenderer: camera 图像渲染可由 disable 该组件来关闭
>
> + Scene: 添加 target gizmo，可在 Unity 编辑器中显示 target 细节
>
> + Asset: 添加全局服务配置及 gizmo 控制选项
>
> + Window: 添加生成 image target data（.etd 文件）的窗口
>
> + Window: 添加菜单跳转到 license key 设置界面和其他全局配置
>
> * 修复目标跟踪存在一帧延迟的问题
>
> * 修复阻塞式 target 加载，减少 target 加载时间
>
> * 修复 target size 获取
>
> * 许多其他改进及 bug 修复
>
Samples of Unity Plugin for EasyAR Sense 3.1.0
>
> ++ 添加回所有 Sense 2.3 的 sample
>
> + 添加 sample 启动器，可以通过启动器加载所有 samples
>
> + 添加屏幕上显示的组件状态信息，覆盖所有 sample
>
> + 添加展示 AR 眼镜支持的 sample
>
> + 添加表面跟踪与图像跟踪同时使用的 sample
>
> + 添加获取 camera 图像贴图和控制 camera 显示的 sample
>
> + 添加修改视频 aspect ratio （Unity VideoPlayer 功能） 适配 image target 的 sample
>
> + 添加展示从图像扩展跟踪的 sample
>
> + 云识别 sample 现在使用本地缓存，并在跟踪状态下停止云端识别，以覆盖常见的使用场景
>
> + 优化 coloring3D sample，修复 bug
>

---

## EasyAR Sense 4.0 发行说明
- 章节路径: `native/release-notes/release-notes-4_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_0.html

# EasyAR Sense 4.0 发行说明
## 4.0.1
2020-05-13
EasyAR Sense 4.0.1 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + CloudRecognizer 状态回调增加“到达访问额度”状态
>
> + 增加输入帧录制和播放功能，用于调试
>
> + 增加 MotionTracking 适配机型
>
> * 修正 MotionTracking 中的内存泄露问题
>
> * MotionTracking 的相机对焦模式改为自动对焦
>
> * 修正 SparseSpatialMapManager.load 出错时会崩溃的问题
>
> * 修正 Android HelloARMotionTracking 示例摄像机图像不更新的问题
>
> * 修复了一些稳定性问题
>
## 4.0.0
2019-12-30
EasyAR 已经成长为一个大家族，从版本 4 开始，过去被大家熟知的 EasyAR SDK 将被赋予一个新的名字：EasyAR Sense。EasyAR Sense 提供感知真实世界的能力。这个版本包含了所有 3.0 的功能。
EasyAR Sense 是一个独立 SDK，它不依赖于非系统组件或是像 Unity3D 这样的工具，可以提供灵活的基于数据流的组件化 API。
而关于 Unity 的支持，EasyAR Sense Unity Plugin 是一个非常薄的封装，用于在 Unity 中暴露 EasyAR Sense 的功能。EasyAR Sense Unity Plugin 的所有代码经过良好的接口设计且都是开源的。你可以直接使用这个插件来快速创建 AR 体验，也可以参考插件代码来更加灵活和自定义的使用 EasyAR Sense 接口和功能，或是创建属于自己的 Unity 插件。
EasyAR Sense 4.0 带来了这些全新特性：
1. 稀疏空间地图 Sparse Spatial Map
稀疏空间地图提供了扫描物理空间同时生成点云地图并进行实时定位的能力，开发者可以快速基于现实空间创建应用，如 AR 说明书以及 AR 导航导览等。在点云地图上部署的虚拟内容，同时也会被持久化放置在现实空间中，实现虚拟世界和物理世界的连接。此外，多人 AR 互动也能在此基础上实现。
2. 稠密空间地图 Dense Spatial Map
虚拟内容与物理世界产生交互碰撞，AR 体验才更加逼真。EasyAR Sense 4.0 支持实时重建环境的稠密空间地图，可以实现碰撞、遮挡等效果，从而构建更真实的 AR 体验。
3. 运动跟踪 Motion Tracking
提供多传感融合的方式解算位置和姿态，降低了相机运动带来的漂移，让虚拟物体在空间更加稳定。同时提供重定位功能，在跟踪丢失后可以恢复定位。使用运动跟踪的应用，不依赖于 ARCore，也不需要最终用户通过 Google 服务框架安装 ARCore 服务。
4. ARKit/ARCore 支持
支持在 iOS 上使用 ARKit，在 Android 上使用 ARCore，并可以与 EasyAR Sense 的其他功能一起使用。
EasyAR Sense Unity 插件同样获得了巨大提升，主要集中在这几方面：
1. 连贯的设计演化
EasyAR Sense 1/2/3 的 Unity 插件的所有功能和优点都在这个版本中保留了下来。
这个版本的插件尽可能多的使用了 Unity 本身的功能，比如使用 OnEnable/OnDisable 来控制 start/stop。大多数 EasyAR Sense 功能都可以不需要写脚本直接工作。
所有 EasyAR Sense 4.0 的新功能都已经支持，许多 bug 也已经修复。
2. 编辑器体验优化
编辑器中可以显示 image target 的 gizmo，以更好的体验替代过去版本中编辑模式下自动生成的 mesh。
严重错误（比如 license key 验证失败）会通过弹出消息在屏幕上显示，用于帮助 debug。
除 API 外，提供了 Unity 工具窗口来生成 image target data。
3. 更多样例，覆盖更多细节 API
添加了展示所有新功能以及不同算法组合工作的样例。
添加了 AR 眼镜支持的样例，预先标定了两款 AR 眼镜：影创 Action One 及 EPSON BT-350。
社区中许多关于“如何使用”的问题在这些样例中都有解答。感谢大家的反馈！
EasyAR Sense 4.0 提供免费个人版、月付费专业版和定制化功能企业版三种订阅模式。
功能、定价、付款方式等的详细信息可以在 [产品页面](https://www.easyar.cn/view/sdk.html) 及 [价格页面](https://www.easyar.cn/price.html) 了解。

---

## EasyAR Sense 4.1 发行说明
- 章节路径: `native/release-notes/release-notes-4_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_1.html

# EasyAR Sense 4.1 发行说明
## 4.1.0
2020-07-16
EasyAR Sense 4.1.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + MotionTrackerCameraDevice 支持点击碰撞和获取局部点云功能
>
> + CloudRecognizer 支持单次扫描
>
> + API 文档支持交叉引用链接
>
> - 拆分 Unity Plugin 文档
>
> - 去除 ImageTarget.setupAll 和 ObjectTarget.setupAll，并增加了 Android 和 iOS 上使用 JSON 加载 ImageTarget 的示例代码
>
> * 修正 Android 上 CameraDevice(Camera1).setSize 中与 buffer 数量相关的多线程 race condition(造成摄像机画面显示不正常)
>
> * 修正 Android 上 CameraDevice(Camera2).supportedSize 返回数值错误的问题
>
> * 修正 Android 上 CameraDevice.supportedFrameRateRangeLower 和 CameraDevice.supportedFrameRateRangeUpper 崩溃的问题
>
> * 修正 SparseSpatialMap 上传和下载超过 1MB 地图时数据损坏的问题
>
> * CameraDevice.setSize 不再修改 CameraParameters，只在 InputFrame 生成时进行根据图像大小重新计算 CameraParameters
>
> * 修正 Swift binding 在 XCode 11.4 和之后版本上运行崩溃的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.2 发行说明
- 章节路径: `native/release-notes/release-notes-4_2.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_2.html

# EasyAR Sense 4.2 发行说明
## 4.2.0
2021-01-25
EasyAR Sense 4.2.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + 增加 iOS 不带录屏和视频播放器功能版本，以满足部分应用的 AppStore 隐私政策合规要求
>
> + 增加 MacOS 上的 framework 版本
>
> + FrameRecorder 播放时增加暂停/继续和获取总播放时间、当前播放时间、初始屏幕旋转方向、是否已完成的功能
>
> + 将 Android 的 CameraDevice 实现提取到了 HelloARCustomCamera 示例中，便于进行修改
>
> + 在 Android 的 aar 库中增加了 ProGuard 规则，不再需要手动指定
>
> + 在 MotionTracking 中优化了平面检测，提升了跟踪鲁棒性和重定位能力
>
> + 增加 MotionTracker 标定参数网络更新功能(CalibrationDownloader)
>
> + 增加 MotionTracking 适配机型
>
> + 增加 CameraDeviceSelector.getFocusMode 以在使用 SurfaceTracking 或 MotionTracking 时获得推荐的对焦模式
>
> + 增加 Storage.setAssetDirPath 以设置加载 image target 等文件时的根目录
>
> + 增加 Log.setLogFuncWithScheduler 以在无法或不便保证线程安全时使用自定义日志函数
>
> * Android 平台示例均升级到 Android 11 (API Level 30)目标
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.3 发行说明
- 章节路径: `native/release-notes/release-notes-4_3.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_3.html

# EasyAR Sense 4.3 发行说明
## 4.3.0
2021-04-07
EasyAR Sense 4.3.0 增加了一些小功能，修复了一些兼容性问题。
详细更新内容如下：
>
> + 增加 MotionTrackerCameraDevice.getQualityLevel，用于获取设备的 MotionTracking 适配质量
>
> + 增加 MotionTrackerCameraDevice.setTrackingMode，用于支持不同的跟踪模式
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ARCoreCameraDevice 在 Android 11 上的兼容性说明
>
> * 在 MotionTracking 中优化了 hittest
>
> * 在 MotionTracking 中提升了大场景下鲁棒性
>
> * 在 DenseSpatialMap 中减小了 block size，提升 incremental update 的性能
>
> * 升级 XCode 版本到 12，iOS 最低版本到 9.0
>
> * 升级 Android Gradle Plugin 版本到 4.1.0，NDK 到 r22
>
> * 修复 Android 平台上 HelloARRecording 示例对 Android 10 和 Android 11 的兼容性问题
>
> * 修复 Android 平台上 CameraDevice 使用 camera2 时有时候退出时会崩溃的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.4 发行说明
- 章节路径: `native/release-notes/release-notes-4_4.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_4.html

# EasyAR Sense 4.4 发行说明
## 4.4.0
2021-10-28
EasyAR Sense 4.4.0 增加了对 EasyAR Cloud SpatialMap 的支持，另外还增加了一些小功能，修复了一些问题。
[EasyAR Cloud SpatialMap](https://www.easyar.cn/cloudspatialmap.html) 提供城市级 AR 云方案，通过灵活的采集方案、稳定的建图定位能力及完善的工具链，为文旅、商圈、教育、工业等众多行业进行 AR 数字化赋能。
详细更新内容如下：
>
> ++ 增加 CloudLocalizer，用于支持 EasyAR Cloud SpatialMap
>
> + 增加 RealTimeCoordinateTransform，用于 EasyAR 运动融合
>
> + iOS 和 MacOS 中的 framework 改为以 xcframework 的形式组织
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ARKit/ARCore 对焦控制接口 ARCoreCameraDevice.setFocusMode、ARKitCameraDevice.setFocusMode
>
> + 增加加速度计接口 Accelerometer
>
> - 去除 iOS 上的 static framework，请改为使用 dynamic framework
>
> - 去除 MacOS 上的 bundle，请改为使用 framework 或者 dylib
>
> - C++03 接口已过时，会在将来删除，请改为使用 C++17 或者 C 接口，示例已删除
>
> * 将 Android 示例中的 jcenter 改为 mavenCentral，以应对 jcenter 关闭
>
> * 修复 MotionTracking 在反复进出时可能崩溃的问题
>
> * 修复 MotionTracking 在部分设备上卡死的问题
>
> * 优化 iOS 示例发布包大小
>
> * 修复 ImageTracking 有时候识别到后马上丢失的问题
>
> * 修复 ImageTracking 在 Android 上部分识别图加载失败无法用于跟踪的问题
>
> * 修复 ImageTarget.save 在 MacOS 上 Unicode 字符路径无法使用问题
>
> * 修复 CameraDevice 设置的回调在调用 open 之后会失效的问题
>
> * 修复 CameraDevice 在 Android 上调用 start 之后设置的回调无法被触发的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.5 发行说明
- 章节路径: `native/release-notes/release-notes-4_5.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_5.html

# EasyAR Sense 4.5 发行说明
## 4.5.0
2022-03-04
EasyAR Sense 4.5.0 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 网络相关功能增加超时时间参数(CalibrationDownloader.download、CloudLocalizer.resolve、CloudRecognizer.resolve、SparseSpatialMapManager.host、SparseSpatialMapManager.load)
>
> + Image 增加 pixelWidth 和 pixelHeight 用于支持摄像机图像的 padding
>
> + 增加 MotionTracking 适配机型
>
> - 结束 Android 4.x 支持，最低支持版本为 5.0
>
> - 移除 C++03 接口
>
> - 停止获取 Android Build Serial 以满足 PlayStore Families Policy Requirements
>
> * Recorder、VideoPlayer 和各示例的 OpenGLES 2.0 升级为 3.0
>
> * 升级编译 SDK 的工具版本：XCode 13
>
> * 升级编译 SDK 的工具版本：Android Gradle Plugin 7.0.0，NDK r23
>
> * 升级各示例依赖的工具版本
>
> * 修正 ARCoreCameraDevice 在部分机型上出现的花屏等问题
>
> * 修正 CameraDevice 在 iPhone 上前置摄像头使用 setFocusMode 时崩溃的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.6 发行说明
- 章节路径: `native/release-notes/release-notes-4_6.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_6.html

# EasyAR Sense 4.6 发行说明
## 4.6.1
2023-03-24
EasyAR Sense 4.6.1 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 增加 MotionTracking 适配机型
>
> * 修正 MotionTrackerCameraDevice 的 hitTestAgainstPointCloud、hitTestAgainstHorizontalPlane、getLocalPointsCloud 无返回结果的问题
>
## 4.6.0
2023-02-13
EasyAR Sense 4.6.0 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 增加 MegaTracker，集成 CloudLocalizer 和 RealTimeCoordinateTransform，下个版本将删除 RealTimeCoordinateTransform
>
> + 增加 CloudLocalizer.resolve 参数以支持辅助邻近位置和指南针读数输入
>
> + 增加 Accelerometer.output 以配合 MegaTracker 输入
>
> + 增加 MotionTrackerCameraDeviceTrackingMode.LargeScale 模式降低大空间跑飞概率
>
> + 增加 MotionTracking 跟踪稳定性
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ImageTracker.setResultPostProcessing、ObjectTracker.setResultPostProcessing、SparseSpatialMap.setResultPoseType 以集成 RealTimeCoordinateTransform 功能
>
> + 增加 ARCore 机型列表以判断设备是否支持 ARCore，HelloARMotionTracking 示例增加 ARCore 下载引导
>
> + 增加 MacOS arm64 的支持
>
> - 移除 iOS armv7 空库
>
> - 结束 iOS 9.x-10.x 支持，最低支持版本为 11.0
>
> - 停止获取 Android SSAID(ANDROID_ID)以满足中国大陆监管要求。请受到影响的用户尽快升级。同时，从 EasyAR Sense 4.6.0 开始，将无法连接按日活计费的 CRS 服务，请迁移到按调用次数计费模式
>
> * 优化 CloudLocalizer 接口，修正对相机旋转方向的处理
>
> * 修改 CloudLocalizerStatus 错误值定义
>
> * 简化 TargetInstance 和 TargetStatus
>
> * 修正 Java binding 中回调的参数没有自动释放的问题
>
> * 升级编译 SDK 的工具版本：Android Gradle Plugin 7.2.0，NDK r25
>
> * 升级编译 SDK 的工具版本：XCode 14
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.7 发行说明
- 章节路径: `native/release-notes/release-notes-4_7.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_7.html

# EasyAR Sense 4.7 发行说明
## 4.7.0
2025-10-20
EasyAR Sense 4.7.0 增加了一些功能，修复了一些问题。
版本
>
> + 增加 CommunityR 版本，支持视频播放、录屏功能，取消 NR 版本，其他版本不再支持视频播放、录屏功能
>
> + 增加 visionOS 支持
>
> + 增加 aar 的 C++ prefab 支持
>
> * 升级编译 SDK 的工具版本：Android build tools 36，NDK r28，兼容 Android 16KiB 内存页大小
>
> * 升级编译 SDK 的工具版本：XCode 16.1
>
> - 结束 iOS 11.x-14.x 支持，最低支持版本为 15.0
>
> - 结束 macOS 10.x 支持，最低支持版本为 11.0
>
MEGA
>
> + 增加 MegaLandmarkFilter 用于支持 EasyAR Mega Landmark 的 VPS 云定位
>
> + MegaTracker 支持新协议版本
>
> + MegaTracker 运行时支持切换定位库
>
> + 服务器唤醒中定义单独枚举项
>
> + MegaTracker 增加同步获得输出 pose 的功能
>
> + MegaTracker 增加 setResultAsyncMode 接口，适应 RTCT 的修改
>
> + 支持使用 API Token 访问 Mega 服务
>
算法
>
> + 支持使用 API Token 访问 CRS 服务
>
> + InputFrame 增加了一些不兼容的检查
>
> + InputFrame 增加 CameraTransformType 字段
>
> + CameraParameters 增加鱼眼等相机模型
>
> + ImageTracker ObjectTracker SparseSpatialMap 增加同步访问结果模式
>
> * 将 RealTimeCoordinateTransform 集成在各个 Tracker 中，改进其稳定性
>
> * 修正 MotionTrackerCameraDevice 在某些情况下会崩溃的问题
>
设备
>
> + 增加 ThreeDofCameraDevice 用于支持 3DoF 的相机
>
> + 增加 InertialCameraDevice 用于支持惯性导航
>
> + 增加 VisionOSARKitCameraDevice 用于支持 visionOS 上的 ARKit 相机
>
> + 增加 Gyroscope Magnetometer AttitudeSensor 用于获取传感器数据
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获取帧率的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice 获取摄像机图像大小的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获得摄像机类型和旋转方向 的功能
>
> + 增加 CameraDevice 获得旋转方向的功能
>
> + 增加 MotionTrackerCameraDevice 获得摄像机类型、旋转方向、大小、帧率的功能
>
> + 增加对一些 AR 眼镜的支持(请参考 EasyAR Sense Unity Plugin 文档)
>
> + ARKitCameraDevice 增加帧率设置
>
> + 各种 CameraDevice 删除获得 InputFrameSourceType 功能
>
> + 升级 ARCore 机型列表
>
> + 升级 MotionTrackerCameraDevice 机型列表
>
> + Android 上 camera2 获取系统内参
>
> + iOS 支持 CameraDevice 获取内参(可能部分老手机不支持)
>
杂项
>
> + 增加 VideoInputFrameRecorder 和 VideoInputFramePlayer 用于 EIF MKV 格式调试数据录制和播放(Windows 上只支持播放，Android 上只支持录制)
>
> + 增加 EventDumpRecorder 用于 EED 格式调试数据录制，EED(EasyARSense Event Dump)文件可用于记录日志、输出帧状态、定位请求、IMU、GPS 等数据
>
> + Log 增加 logMessage
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NORTTI
> 选项用于禁用 RTTI
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常
>
> + 在 C++导出接口实现中增加
> EASYAR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常 throw
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 发行说明
- 章节路径: `native/release-notes/release-notes.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes.html

# EasyAR Sense 发行说明
EasyAR 是灵活好用的增强现实引擎。
EasyAR Sense 提供感知真实世界的能力，支持平面图像跟踪、3D 物体跟踪、表面跟踪、运动跟踪和稀疏空间地图、稠密空间地图、Mega。
EasyAR Sense 是一个独立 SDK，它不依赖于非系统组件或是像 Unity3D 这样的工具，可以提供灵活的基于数据流的组件化 API。
EasyAR Sense 4.0 提供免费个人版、月付费专业版、一次性付费经典版和定制化功能企业版四种订阅模式。
## 历史版本
[4.7](release-notes-4_7.html)
[4.6](release-notes-4_6.html)
[4.5](release-notes-4_5.html)
[4.4](release-notes-4_4.html)
[4.3](release-notes-4_3.html)
[4.2](release-notes-4_2.html)
[4.1](release-notes-4_1.html)
[4.0](release-notes-4_0.html)
[3.1](release-notes-3_1.html)
[3.0](release-notes-3_0.html)
[2.3](release-notes-2_3.html)
[2.2](release-notes-2_2.html)
[2.1](release-notes-2_1.html)
[2.0](release-notes-2_0.html)
[1.3](release-notes-1_3.html)
[1.2](release-notes-1_2.html)
[1.1](release-notes-1_1.html)
[1.0](release-notes-1_0.html)
## 4.7.0
2025-10-20
版本
>
> + 增加 CommunityR 版本，支持视频播放、录屏功能，取消 NR 版本，其他版本不再支持视频播放、录屏功能
>
> + 增加 visionOS 支持
>
> + 增加 aar 的 C++ prefab 支持
>
> * 升级编译 SDK 的工具版本：Android build tools 36，NDK r28，兼容 Android 16KiB 内存页大小
>
> * 升级编译 SDK 的工具版本：XCode 16.1
>
> - 结束 iOS 11.x-14.x 支持，最低支持版本为 15.0
>
> - 结束 macOS 10.x 支持，最低支持版本为 11.0
>
MEGA
>
> + 增加 MegaLandmarkFilter 用于支持 EasyAR Mega Landmark 的 VPS 云定位
>
> + MegaTracker 支持新协议版本
>
> + MegaTracker 运行时支持切换定位库
>
> + 服务器唤醒中定义单独枚举项
>
> + MegaTracker 增加同步获得输出 pose 的功能
>
> + MegaTracker 增加 setResultAsyncMode 接口，适应 RTCT 的修改
>
> + 支持使用 API Token 访问 Mega 服务
>
算法
>
> + 支持使用 API Token 访问 CRS 服务
>
> + InputFrame 增加了一些不兼容的检查
>
> + InputFrame 增加 CameraTransformType 字段
>
> + CameraParameters 增加鱼眼等相机模型
>
> + ImageTracker ObjectTracker SparseSpatialMap 增加同步访问结果模式
>
> * 将 RealTimeCoordinateTransform 集成在各个 Tracker 中，改进其稳定性
>
> * 修正 MotionTrackerCameraDevice 在某些情况下会崩溃的问题
>
设备
>
> + 增加 ThreeDofCameraDevice 用于支持 3DoF 的相机
>
> + 增加 InertialCameraDevice 用于支持惯性导航
>
> + 增加 VisionOSARKitCameraDevice 用于支持 visionOS 上的 ARKit 相机
>
> + 增加 Gyroscope Magnetometer AttitudeSensor 用于获取传感器数据
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获取帧率的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice 获取摄像机图像大小的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获得摄像机类型和旋转方向 的功能
>
> + 增加 CameraDevice 获得旋转方向的功能
>
> + 增加 MotionTrackerCameraDevice 获得摄像机类型、旋转方向、大小、帧率的功能
>
> + 增加对一些 AR 眼镜的支持(请参考 EasyAR Sense Unity Plugin 文档)
>
> + ARKitCameraDevice 增加帧率设置
>
> + 各种 CameraDevice 删除获得 InputFrameSourceType 功能
>
> + 升级 ARCore 机型列表
>
> + 升级 MotionTrackerCameraDevice 机型列表
>
> + Android 上 camera2 获取系统内参
>
> + iOS 支持 CameraDevice 获取内参(可能部分老手机不支持)
>
杂项
>
> + 增加 VideoInputFrameRecorder 和 VideoInputFramePlayer 用于 EIF MKV 格式调试数据录制和播放(Windows 上只支持播放，Android 上只支持录制)
>
> + 增加 EventDumpRecorder 用于 EED 格式调试数据录制，EED(EasyARSense Event Dump)文件可用于记录日志、输出帧状态、定位请求、IMU、GPS 等数据
>
> + Log 增加 logMessage
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NORTTI
> 选项用于禁用 RTTI
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常
>
> + 在 C++导出接口实现中增加
> EASYAR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常 throw
>
> * 修复了一些稳定性问题
>
