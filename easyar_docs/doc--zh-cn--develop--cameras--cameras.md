---
source: https://www.easyar.cn/doc/zh-cn/develop/cameras/cameras.html
---

摄像头和输入扩展 | EasyAR 文档
**
##### Table of Contents
**
# 摄像头和输入扩展
本文介绍物理相机的相机模型、参数和一些其他使用上的注意点，以及使用自定义相机的方式进行输入扩展。
![camera](https://doc-asset.easyar.com/develop/cameras/media/cameras-camera.jpg)
## 输入帧
输入帧（Input Frame）是 AR 中的基本数据单元，它表示一次从摄像头或其他数据源捕获的帧的所有相关信息。一个输入帧通常包含：
* 原始图像数据（camera image）
* 相机参数（如内参）
* 时间戳
* 相机在世界坐标中的变换矩阵
* 跟踪状态（tracking status）
这些信息为 AR 算法提供定位、跟踪、渲染等所需的时空上下文数据。
## 物理相机
目前电子设备上使用的摄像头，通常由多片透镜和反射镜组成。但一般不使用实际的光学结构来构建相机模型，而是使用一些简化的模型。
### 针孔相机模型
![pinhole camera](https://doc-asset.easyar.com/develop/cameras/media/cameras-pinhole.png)
这是通常使用的最简单的模型，光通过一个小孔成一个旋转 180 度的像。但相机输出的数据中会将像正过来。需要六个参数来描述这个模型，像素宽高 \\(w, h\\) ，像素焦距 \\(f\_x, f\_y\\) ，主点像素位置 \\(c\_x, c\_y\\) 。可以注意到如果像素宽高缩放时，像素焦距和主点像素位置也对应缩放，可以保持像的位置不变。
### OpenCV 相机模型
有些相机会存在显著的径向畸变和切向畸变，[OpenCV 相机模型](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)在针孔相机模型上的基础上增加了高次参数来描述径向畸变和切向畸变。径向畸变使用 \\(k\_1, k\_2, k\_3, \\cdots\\) 来描述。切向畸变使用 \\(p\_1, p\_2\\) 来描述。
##### 注意
有一些跟踪器不支持 OpenCV 相机模型。
### OpenCV 鱼眼相机模型
鱼眼相机通过透视投影以将大视角内容压缩到较小的成像面积内。[OpenCV 鱼眼相机模型](https://docs.opencv.org/4.x/db/d58/group__calib3d__fisheye.html)不带畸变矫正，在针孔相机模型 6 个参数的基础上，使用 \\(k\_1, k\_2, k\_3, k\_4, \\cdots\\) 来描述。
##### 注意
有一些跟踪器不支持 OpenCV 鱼眼相机模型。
![fisheye camera](https://doc-asset.easyar.com/develop/cameras/media/cameras-fisheye.jpg)
### 相机朝向与图像朝向
在手机上，通常横向拿（从正常竖向拿逆时针旋转 90 度）且屏幕显示方向也是横向的时候，后置摄像头输出的图像在屏幕上显示时的方向和真实场景一致。不改变屏幕物理方向只改变屏幕显示方向不会改变物理相机输出的图像方向。当正常竖向拿且屏幕显示方向也是正常竖向的时候，后置摄像头输出的图像需要顺时针旋转 90 度后显示到屏幕上，才和真实场景一致。当屏幕显示方向旋转时，渲染相机图像需要进行反向的旋转补偿，才能和真实场景一致。
相机朝向和图像朝向，通常都是相对于设备的自然方向来定义的：
* 手机
* Android
Android 定义了一个自然方向，是指正常竖向拿手机的方向，惯性传感器单元(IMU)也是以这个方向为基准。相机输出图像相对于这个方向的旋转角度，作为相机的参数，可以获得。
* iOS
iOS 上，虽然未明确定义自然方向，但惯性传感器单元也是使用的和 Android 一样的基准。
* 平板
平板的自然方向，有一些是横向拿的方向，有些和手机一样是正常竖向拿的方向。
* 眼镜
眼镜的自然方向，通常是横向拿的方向。
渲染相机图像时，会综合相机朝向和屏幕朝向进行渲染。
### 相机类型与相机翻转
手机上一般有后置摄像头和前置摄像头。前置摄像头输出的图像，需要进行左右翻转后再显示到屏幕上，模拟一面镜子。如果不进行左右翻转，看起来会很不习惯。
## 输入扩展
EasyAR 支持使用自定义相机的方式进行输入扩展。自定义相机可以支持从外部获得输入帧传输到 AR 系统中，供跟踪器使用。自定义相机可以由您自行实现图像数据获取。
## 平台专用指南
摄像头和输入扩展的使用与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [帧数据源](../unity/cameras/frame-source.html)
* [创建一组输入源](../unity/cameras/frame-source-group.html)
* [自定义相机和外部帧输入](../unity/cameras/external-frame-source.html)
* [内置Frame Source参考](../unity/cameras/frame-source-builtin.html)
* [示例说明](../unity/cameras/sample-camera-device.html)