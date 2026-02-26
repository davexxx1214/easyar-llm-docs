---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker.html
original_file: doc--zh-cn--develop--wechat--mega--tracker.md
normalized_at: 2026-02-27
---
# MegaTracker 的概念与工作流
这篇文档将介绍 MegaTracker 的基本概念及 MegaTracker 与微信原生的 AR 系统 VisionKit 和渲染框架 xr-frame 的关系。
## 开始之前
通过 [Mega 简介](../../mega/intro.html) 了解：
* Mega 定位与跟踪的基本原理。
* 什么是 Mega Block。
* 集成 Mega 后的预期结果。
## 平面 AR 追踪器 是什么
xr-frame 的[平面AR追踪器](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#Plane) 本质上是 [VisionKit 6DoF-平面能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)的封装。
在 xr-frame 的摄像机组件开启 `isARCamera` 后，摄像机的三维变换**每帧**都会与 AR 系统 （VisionKit） 同步。
由 xr-frame 提供 3D 渲染能力，由 VisionKit 提供在现实空间坐标系下的**运动跟踪能力**。
平面 AR 跟踪器不能和其他 AR 跟踪器一起使用。
## MegaTracker 是什么
MegaTracker 是连接微信 AR 系统 （VisionKit） 与 Mega 空间计算服务的核心算法组件，由它提供云定位功能。
* **输入**：每一帧 VisionKit 计算出的**在 VisionKit 坐标系下的相机位姿**（即 6DoF 数据） 及 进行 Mega 定位那一帧时的**相机图片**。
* **输出**：当前定位和跟踪的 **Mega Block** 下的相机位姿 。
## MegaTracker 是如何在 xr-frame 上工作的
```
flowchart BT
subgraph Using xr-frame Only
direction BT
PlaneARTracker\_1[PlaneARTracker] -->|MotionData & Image| XRFrame\_1[xr-frame]
end
subgraph Using Mega Plugin
direction BT
PlaneARTracker\_2[PlaneARTracker] -->|MotionData & Image| MegaTracker
MegaTracker -->|CameraTransform| XRFrame\_2[xr-frame]
end
```
* 在微信原生提供的数据流中 xr-frame 的摄像机组件每帧由**平面 AR 追踪器**的结果直接更新。
* 在 Mega 小程序提供的数据流中 **在 VisionKit 坐标系下的相机位姿**（即 6DoF 数据）及定位帧的图片数据会输入给 **MegaTracker**，在云定位和本地计算之后输出当前定位和跟踪的 **Mega Block** 下的相机位姿 ，最终更新 xr-frame 场景中摄像机在 **Mega Block** 节点下的 LocalTransform，此时 **MegaTracker** 接管了摄像机的控制权， xr-frame **不再**根据 AR 追踪器更新摄像机。
**MegaTracker 的运行深度依赖于平面追踪器提供的 6DoF 运动数据**。 因此，在平面追踪器完成初始化并建立稳定的追踪状态前，MegaTracker 无法介入工作。此外，AR 追踪的稳定性受限于环境特征；在遇到大面积无纹理区域（如白墙）、相机长时间遮挡等极端场景时，若微信底层平面追踪发生漂移或丢失，MegaTracker 将因失去可靠的输入源而同步进入失效状态。
## 后续步骤
* [指定 MegaTracker 云服务鉴权方式](tracker-access.html)
