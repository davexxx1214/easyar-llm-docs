# EasyAR 专题包：plane-detection

适用于上下文长度有限时的分卷输入。

## 目录
- `plane-detection/devices.md`
- `plane-detection/intro.md`

---

## 平面检测支持的设备和平台
- 章节路径: `plane-detection/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/plane-detection/devices.html

# 平面检测支持的设备和平台
本章节介绍平面检测功能支持的设备硬件要求和支持的开发平台。
## 平面检测支持的设备
平面检测支持 Android，需要设备本身支持 6DoF 的 EasyAR Motion Tracker 开启时才生效。
如果要使用 ARKit 或 ARCore 等平面检测功能，无法通过 EasyAR 单独实现，在 Unity 上可以通过 [AR Foundation](../unity/fundamentals/arfoundation.html) 联合 EasyAR 实现，Native 开发上可以使用自定义相机同时使用 EasyAR 和 ARKit/ARCore。
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上的 Unity 或者原生上使用平面检测功能。需要注意的是是录制 EIF 的设备同样支持运动跟踪功能。
## 延伸阅读
* [运动跟踪与EasyAR其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker支持的设备](../motion-tracking/devices-easyar.html)

---

## EasyAR 平面检测
- 章节路径: `plane-detection/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/plane-detection/intro.html

# EasyAR 平面检测
EasyAR 平面检测是在运行 EasyAR 运动跟踪时，自动检测环境中的水平面或者竖直面，提供虚拟物体放置等功能。
## EasyAR 平面检测原理
EasyAR 平面检测（Plane Detection）是在 **运行 EasyAR 运动跟踪（Motion Tracker）过程中同步** 自动完成的一种简单的环境理解能力。系统基于设备摄像头和惯性传感器获取的时空信息，对真实环境进行连续建模，从而识别并跟踪环境中的水平面与竖直面，为虚拟物体放置、交互对齐和空间理解提供基础支持。
![planedetection](https://doc-asset.easyar.com/develop/plane-detection/media/plane-detection.png)
具体的流程为：
1. 运动跟踪
在运动跟踪运行期间，EasyAR 持续获取以下两类核心数据来自 RGB 摄像头的连续图像帧、加速度计和陀螺仪的数据。系统通过视觉–惯性融合算法估计设备在世界坐标系中的连续六自由度位置和姿态，为后续的空间建模与平面分析提供稳定、低漂移的相机轨迹。
2. 特征点检测和三角化
在位姿估计的基础上，EasyAR 从图像序列中提取并跟踪稳定的视觉特征点（如角点或纹理显著区域），并通过多视几何方法将这些特征点三角化，恢复其在三维空间中的位置，形成一个局部三维点云表示。
3. 平面候选区域生成
在获得三维点云后，系统对点云进行几何分析，以发现可能属于同一平面的点集。通过与重力方向的关系判断，系统可以区分不同类型的平面候选：
* 水平面：法向量与重力方向近似平行（如地面、桌面）；
* 竖直面：法向量与重力方向近似垂直（如墙面、立柱）。
* 平面跟踪与检测
EasyAR 会在连续帧中对已检测到的平面进行验证和更新：
* 判断新观测到的三维点是否支持已有平面模型；
* 根据观测一致性动态调整平面范围、边界和置信度；
* 剔除短暂出现或不稳定的平面候选。
只有在几何一致性和时间稳定性均满足要求时，结果才会被为“可用平面”。
* 平面坐标系与虚拟内容对齐
一旦平面被确认，您可基于平面检测结果实现更真实的 AR 效果：
* 在平面上放置虚拟物体，实现真实尺度和方向的对齐；
* 进行射线投射（Hit Test），将屏幕点击映射到真实平面位置；
* 实现基于平面的交互逻辑，如物体吸附、移动和遮挡判断。
由于平面与运动跟踪系统共享同一世界坐标系，虚拟物体在用户移动设备时能够保持稳定、连续的空间一致性。
平面检测依赖于运动跟踪提供的稳定位姿和空间结构，而平面检测结果反过来也可用于增强环境理解能力，例如辅助内容放置和交互设计。二者共同构成 EasyAR 空间感知能力的核心基础，但在系统架构上相互解耦，平面检测不会改变运动跟踪本身的位姿估计结果。
## 最佳实践
为了保证用户使用平面检测的效果，遵循以下实践能提升用户体验。
* 引导用户缓慢移动，避免静止不动、快速运动或者原地旋转。
* 避免无纹理、纯色、镜面等视觉难以识别的平面。
> **注意**
平面检测是 EasyAR 识别环境中水平或竖直平面的功能，表面跟踪并不检测或者识别场景中的平面结构，需要进行区分。
## 延伸阅读
* [平面检测支持的设备](devices.html)
