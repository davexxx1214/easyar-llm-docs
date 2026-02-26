---
source: https://www.easyar.cn/doc/zh-cn/develop/fundamentals/fundamentals.html
---

AR 驱动的 3D 渲染 | EasyAR 文档
**
##### Table of Contents
**
# AR 驱动的 3D 渲染
AR 应用的开发需要解决一个基础问题，就是 AR 内容的渲染。本文会以平面图像跟踪为例，描述 AR 应用的基本模块、流程和渲染实现。
## 典型的 AR 应用流程
一个典型的 AR 应用，通常是从摄像机图像中识别特定的图像、物体或场景，跟踪其位置和姿态，并按照这个位置和姿态渲染显示虚拟内容（3D 模型）的过程。
![image tracking](https://doc-asset.easyar.com/develop/fundamentals/media/fundamentals-imagetracking.jpg)
*例如上图是一个平面图形跟踪的 AR 应用*
以下为应用流程示意图。
```
`flowchart TD
CameraDevice[Camera Device]
Tracker[Tracker]
Renderer[Renderer]
CameraDevice --&gt;|Image Frame| Tracker
Tracker --&gt;|Image Frame + Tracked Pose| Renderer
`
```
流程中有以下一些模块。
|模块|作用|
|物理相机|提供输入图像帧的序列。图像帧包括图像，图像生成的时间戳，有时候也可以带有摄像头在空间中的位置和姿态|
|跟踪器|从图像帧计算跟踪目标的位置和姿态。根据跟踪目标的不同，存在各种各样的跟踪器，例如平面图像跟踪器和 3D 对象跟踪器|
|渲染器|用于将相机图像和跟踪对象对应的 3D 模型渲染到屏幕上。在某些 AR 眼镜上，也可能不渲染相机图像，只渲染 3D 模型|
## 手机上的渲染
手机上的渲染分成相机画面的渲染和虚拟物体的渲染两部分。
### 相机画面的渲染
![camera image](https://doc-asset.easyar.com/develop/fundamentals/media/fundamentals-cameraimage.jpg)
相机画面渲染时，有一些需要注意的参数。
* 缩放模式
通常需要将相机画面填满整个屏幕，或者填满一个窗口，这时候会面临相机画面和屏幕/窗口的宽高比不一致的问题。
假设我们要求相机画面中心和屏幕/窗口中心对齐，保持宽高比不变，则有两种常见的缩放模式：等比缩放、等比填充。
|缩放模式|效果|
|等比缩放|在屏幕上显示所有内容，但会在左右或者上下留黑边|
|等比填充|不会有黑边，但会在左右或者上线裁掉部分画面|
* 相机图像旋转
在手机上，物理相机记录的图像通常相对于机身固定，不随屏幕显示方向变化而变化。但手机机身朝向的变化会影响到我们对于图像的上下左右方向的定义。渲染时，当前屏幕显示方向也会影响到显示的图像的方向。
通常在渲染时，需要确定一个相机图像相对于屏幕显示方向的旋转角。
* 相机图像翻转
有些情况下会用到前置摄像头，此时通常需要将画面左右翻转，以使得画面看起来像是一面镜子。
### 虚拟物体的渲染
![virtual object](https://doc-asset.easyar.com/develop/fundamentals/media/fundamentals-virtualobject.jpg)
在手机上渲染虚拟物体，需要将虚拟物体和相机画面对准。这要求我们将渲染相机和物体都放置在和真实空间完全对应的虚拟空间中，并使用物理相机相同的视场角、宽高比来进行渲染。相机画面和虚拟物体经过的透视投影变换一模一样，除了相机画面的透视投影变换大部分是发生在物理相机中，而虚拟物体的透视投影变换完全是一个计算过程。
## 头显上的渲染
头显上的渲染和手机上有一些差别，需要分两种情况。
* VST
Video See-Through，是指头显通过物理相机捕捉图像，然后在头显的屏幕上显示相机图像和虚拟内容的 AR 技术，典型代表是 Vision Pro。通常相机图像和虚拟内容的透视投影矩阵由头显提供的 SDK 进行设置，外部只需要设置虚拟内容的位置和姿态。用于跟踪的物理相机和屏幕上渲染的相机图像的相机可能在不同的位置，渲染时进行了坐标变换。
* OST
Optical See-Through，是指头显的屏幕透明，头显在屏幕上只显示虚拟内容的 AR 技术，典型代表是 HoloLens。通常虚拟内容的透视投影矩阵由头显提供的 SDK 进行设置，外部只需要设置虚拟内容的位置和姿态。用于跟踪的物理相机和屏幕上渲染的相机图像的相机可能在不同的位置，渲染时进行了坐标变换。
## 平台专用指南
AR 驱动的 3D 渲染与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [Unity 兼容性](../unity/fundamentals/unity-compatibility.html)
* [AR Session](../unity/fundamentals/session.html)
* [XR Origin](../unity/fundamentals/origin.html)
* [Target](../unity/fundamentals/target.html)
* [Camera](../unity/fundamentals/camera.html)
* [中心模式](../unity/fundamentals/center-mode.html)
* [使用Unity XR 框架](../unity/fundamentals/unity-xr.html)
* 工程配置
* [Player 工程配置](../unity/fundamentals/setup-player.html)
* [EasyAR 全局配置参考](../unity/fundamentals/setup-easyar.html)
* [示例说明](../unity/fundamentals/sample-arsession.html)
* [微信小程序](https://developers.weixin.qq.com/miniprogram/dev/framework/)
* [微信小程序 XR-Frame](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)
* [微信小程序 VisionKit](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/base.html)
* [EasyAR坐标系](../native/fundamentals/coordinates.html)
* [库加载和初始化](../native/fundamentals/initialization.html)
* [AR数据流](../native/fundamentals/dataflow.html)
* [3D空间内容展示](../native/fundamentals/contents.html)
* [在3D引擎中使用EasyAR](../native/fundamentals/3dengine.html)