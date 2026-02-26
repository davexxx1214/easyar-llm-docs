# EasyAR 专题包：dense-spatial-mapping

适用于上下文长度有限时的分卷输入。

## 目录
- `dense-spatial-mapping/devices.md`
- `dense-spatial-mapping/intro.md`

---

## 稠密空间地图支持的设备和平台
- 章节路径: `dense-spatial-mapping/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/dense-spatial-mapping/devices.html

# 稠密空间地图支持的设备和平台
本章介绍稠密空间地图（Dense Spatial Map）功能支持的设备硬件要求和开发平台。
## 稠密空间地图支持的设备
稠密空间地图支持 iOS、Android、鸿蒙平台以及部分头显平台。硬件上，需要设备支持六自由度的[运动跟踪](../motion-tracking/intro.html)功能。
稠密空间地图可用的运动跟踪类型包括：
* EasyAR 运动跟踪（Motion Tracker）
* 谷歌 ARCore
* 苹果 ARKit
* 华为 AR Engine
* 六自由度跟踪能力的头显或眼镜
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上通过 Unity 或者原生使用稠密空间地图功能。需要注意录制 EIF 的设备必须支持运动跟踪功能。
如果您的设备支持运动跟踪功能，可以参照 [自定义相机](../cameras/custom-camera.html) 的方式接入 EasyAR 并使用稠密空间地图功能。
## 延伸阅读
* [运动跟踪与 EasyAR 其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker 支持的设备](../motion-tracking/devices-easyar.html)
* [华为 AR Engine 支持的设备](../motion-tracking/devices-arengine.html)

---

## EasyAR 稠密空间地图
- 章节路径: `dense-spatial-mapping/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/dense-spatial-mapping/intro.html

# EasyAR 稠密空间地图
EasyAR 稠密空间地图利用设备的摄像头数据对周围环境进行三维重建，得到稠密的点云地图和网格地图。利用稠密空间地图让虚拟物体更好地融入真实环境之中，以实现真实物体和虚拟物体正确遮挡、碰撞等 AR 应用。
## 稠密空间地图功能简介
EasyAR 稠密空间地图在运动跟踪的基础上，分析设备的摄像头数据，建立环境的稠密点云信息并逐渐融合、构建网格（Mesh），得到环境的几何表示，可以用来实现虚拟物体和真实环境的遮挡关系等效果，从而提高 AR 的真实体验感。
EasyAR 稠密空间地图需要基于稳定的 [运动跟踪系统](../motion-tracking/intro.html) 提供六自由度的相机位置和姿态，可以从 EasyAR 运动跟踪模块或者 ARKit/ARCore 等获取。
![densespatialmap](https://doc-asset.easyar.com/develop/dense-spatial-mapping/media/densespatialmap-intro.png)
## 最佳实践
要想得到比较好的重建结果，建议用户按照如下方式进行操作：
* 尽量横移手机，避免原地旋转手机。
* 覆盖尽可能多的扫描角度。
* 不要在大片的纯色区域或对带有反光的物体重建。
* 避免快速的移动或遮挡摄像头。
## 延伸阅读
* [稠密空间地图支持的设备](devices.html)
* [运动跟踪与 EasyAR 其他模块的关系](../motion-tracking/motion-tracking-and-easyar.html)
