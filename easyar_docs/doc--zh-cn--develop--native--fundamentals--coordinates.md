---
source: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/coordinates.html
---

EasyAR 坐标系 | EasyAR 文档
**
##### Table of Contents
**
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
p\_{11} &amp; p\_{12} &amp; p\_{13} &amp; p\_{14} \\\\
p\_{21} &amp; p\_{22} &amp; p\_{23} &amp; p\_{24} \\\\
p\_{31} &amp; p\_{32} &amp; p\_{33} &amp; p\_{34} \\\\
0 &amp; 0 &amp; 0 &amp; 1 \\\\
\\end{array}
\\right)
\\]
如果 3D 引擎采用了其他的坐标轴定义，则在 3D 引擎中设置变换矩阵时需要考虑，例如 camera 坐标系和 target 坐标系的 z 方向均相反时，应设置 3D 引擎的 target 结点变换矩阵值为：
\\[
\\left(
\\begin{array}{cccc}
1 &amp; 0 &amp; 0 &amp; 0 \\\\
0 &amp; 1 &amp; 0 &amp; 0 \\\\
0 &amp; 0 &amp; -1 &amp; 0 \\\\
0 &amp; 0 &amp; 0 &amp; 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
p\_{11} &amp; p\_{12} &amp; p\_{13} &amp; p\_{14} \\\\
p\_{21} &amp; p\_{22} &amp; p\_{23} &amp; p\_{24} \\\\
p\_{31} &amp; p\_{32} &amp; p\_{33} &amp; p\_{34} \\\\
0 &amp; 0 &amp; 0 &amp; 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 &amp; 0 &amp; 0 &amp; 0 \\\\
0 &amp; 1 &amp; 0 &amp; 0 \\\\
0 &amp; 0 &amp; -1 &amp; 0 \\\\
0 &amp; 0 &amp; 0 &amp; 1 \\\\
\\end{array}
\\right)=\\left(
\\begin{array}{cccc}
p\_{11} &amp; p\_{12} &amp; -p\_{13} &amp; p\_{14} \\\\
p\_{21} &amp; p\_{22} &amp; -p\_{23} &amp; p\_{24} \\\\
-p\_{31} &amp; -p\_{32} &amp; p\_{33} &amp; -p\_{34} \\\\
0 &amp; 0 &amp; 0 &amp; 1 \\\\
\\end{array}
\\right)
\\]
## 运动跟踪的 transform
表面跟踪（[SurfaceTracker](../../../api/native/easyar.SurfaceTracker.html)） 的 [transform](../../../api/native/easyar.SurfaceTrackerResult.html#n_easyar_SurfaceTrackerResult_transform) 和运动跟踪（[MotionTrackerCameraDevice](../../../api/native/easyar.MotionTrackerCameraDevice.html)）、ARKit（[ARKitCameraDevice](../../../api/native/easyar.ARKitCameraDevice.html)）、ARCore（[ARCoreCameraDevice](../../../api/native/easyar.ARCoreCameraDevice.html)）的 [cameraTransform](../../../api/native/easyar.InputFrame.html#n_easyar_InputFrame_cameraTransform)，表示 camera 相对于世界坐标系的变换。其中 camera 坐标系与世界坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，在移动设备上指设备自然方向的右和上。）世界坐标系的 y 轴向上（与重力方向相反），原点由运动跟踪系统决定。数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。
## 稀疏空间地图和 Mega 中的 pose
稀疏空间地图 [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html) 的 [getMapPose](../../../api/native/easyar.SparseSpatialMapResult.html#n_easyar_SparseSpatialMapResult_getMapPose)和 Mega 中的 [pose](../../../api/native/easyar.MegaTrackerBlockInstance.html#n_easyar_MegaTrackerBlockInstance_pose)，表示地图 block 在 camera 坐标系中的位置和姿态。其中 camera 坐标系与世地图 block 坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，在移动设备上指设备自然方向的右和上。）地图 block 坐标系的 y 轴向上（与重力方向相反），原点由地图 block 数据决定。数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。