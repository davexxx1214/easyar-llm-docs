---
source: https://www.easyar.cn/doc/zh-cn/develop/dense-spatial-mapping/intro.html
---

EasyAR 稠密空间地图 | EasyAR 文档
**
##### Table of Contents
**
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