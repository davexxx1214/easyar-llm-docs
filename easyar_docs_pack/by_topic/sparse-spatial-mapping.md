# EasyAR 专题包：sparse-spatial-mapping

适用于上下文长度有限时的分卷输入。

## 目录
- `sparse-spatial-mapping/comparison.md`
- `sparse-spatial-mapping/devices.md`
- `sparse-spatial-mapping/intro.md`

---

## EasyAR 稀疏空间地图与 ARKit/ARCore 的区别
- 章节路径: `sparse-spatial-mapping/comparison.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/comparison.html

# EasyAR 稀疏空间地图与 ARKit/ARCore 的区别
EasyAR 稀疏空间地图用于扫描用户周围小范围环境（房间级别），建立视觉地图并导出，可用于多个设备间实时共享，实现多人互动、持久化等功能。类似的方案还包括 ARKit 提供的 ARWorldMap 和 ARCore 提供的 Cloud Anchors。
* ARWorldMap 支持将扫描场景序列化、持久化重定位，可以实现在 iOS 平台上的持久化、多人共享体验。
* Cloud Anchors 将用户扫描环境数据上传到 Google Cloud 上，通过重定位实现多人共享 AR 体验。
EasyAR 稀疏空间地图实现了离线、跨平台、高度自由的地图管理，更适合以下场合：
* 需要完全离线运行的场景（工厂小范围、地下室、展览馆无网环境）。
* 要跨 iOS/Android 等多平台共享同一套地图。
* 开发者希望自己完全掌控地图数据。
> **注意**
如果要扫描和重建的区域超过 100 平方米或者场景光照、季节等变化较大，建议升级至 [EasyAR Mega](../mega/intro.html) 功能。
## 延伸阅读
* [ARKit ARWorldMap](https://developer.apple.com/documentation/arkit/arworldmap)
* [ARCore Cloud Anchors](https://developers.google.com/ar/develop/cloud-anchors)

---

## 稀疏空间地图支持的设备和平台
- 章节路径: `sparse-spatial-mapping/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/devices.html

# 稀疏空间地图支持的设备和平台
本章节介绍稀疏空间地图功能 (Sparse Spatial Map) 支持的设备硬件要求和开发平台。
## 稀疏空间地图支持的设备
稀疏空间地图支持 iOS/Android/鸿蒙以及部分头显平台。硬件上，需要设备本身支持 6DoF 的[运动跟踪](../motion-tracking/intro.html)功能。
稀疏空间地图可用的运动跟踪类型包括：
* EasyAR 运动跟踪（Motion Tracker）
* 谷歌 ARCore
* 苹果 ARKit
* 华为 AR Engine
* 六自由度跟踪能力的头显或眼镜
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上通过 Unity 或者原生使用稀疏空间地图功能。需要注意的是录制 EIF 的设备必须支持运动跟踪功能。
如果您的设备支持运动跟踪功能，可以参照 [自定义相机](../cameras/custom-camera.html) 的方式接入 EasyAR 并使用稀疏空间地图功能。
## 延伸阅读
* [运动跟踪与 EasyAR 其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker支持的设备](../motion-tracking/devices-easyar.html)
* [华为 AR Engine支持的设备](../motion-tracking/devices-arengine.html)

---

## EasyAR 稀疏空间地图
- 章节路径: `sparse-spatial-mapping/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/intro.html

# EasyAR 稀疏空间地图
EasyAR 稀疏空间地图（Sparse Spatial Map）用于扫描用户周围小范围环境（房间级别），生成环境的三维视觉地图并提供视觉定位跟踪功能。适用于开发持久化 AR 应用或多人互动 AR 应用。
## EasyAR 稀疏空间地图原理
EasyAR 稀疏空间地图在运动跟踪的基础上，在设备端利用计算机视觉算法，分析摄像头数据的特征建立环境的空间三维地图。用户可以保存视觉地图或多个设备间实时共享。当其他设备加载相应地图，并在加载地图中通过定位确定设备相对于地图的位置和姿态，从而开发持久化 AR 应用或多人互动 AR 应用。
稀疏空间地图目前需要稳定的运动跟踪系统（例如 EasyAR Motion Tracker、ARCore、ARKit）提供六自由度的位置和姿态用于建图中及定位成功后的持续跟踪。在建图过程中，稀疏空间地图利用相机图像和对应位姿构建环境1:1的视觉地图。定位过程中，当视觉定位成功后，设备相对地图的位姿通过运动跟踪系统持续更新。
EasyAR 稀疏空间地图支持加载多个地图，在多个地图中定位并返回对应地图的 ID 和设备相对于该地图的位置和姿态。
![ssmintro](https://doc-asset.easyar.com/develop/sparse-spatial-mapping/media/sparsespatialmap-intro.png)
## 建图最佳实践
在创建稀疏空间地图时，你需要充分考虑用户会在什么地点、视角下进行定位，以此来优化建图的过程。建图时尽量覆盖到所有的可能定位所在视角，包括观察的角度和距离。
以下是提高建图效果的最佳实践：
* 尽量相对于被扫描区域、场景做平移运动或缓慢旋转。
* 尽可能充分移动扫描覆盖用户可能定位的位置。
* 尽量在具备丰富、稳定且静止的视觉特征区域进行建图。
* 单个地图范围不超过 1000 平方米。
* 建图设备到场景距离应小于 10 米。
在扫描建图时需要避免以下情况：
* 避免在大片的无视觉特征区域进行建图，如白墙。
* 避免在大片的反光材质区域进行建图，如玻璃、镜面物体。
* 避免在重复性的纹理区域建图。
建图完成后，可以在建立的稀疏空间地图中测试定位，检查定位的成功率和精度，若发现效果不理想，考虑重新建立更完整地图。
## 定位最佳实践
为了保证用户使用稀疏空间地图的定位效果，遵循以下实践能提高成功率并提升用户体验。
* 引导用户在地图对应的场景中进行定位，例如给出目标场景的预览图，帮助用户找到目标场景。
* 引导用户缓慢移动设备从多个角度尝试进行定位。
* 避免无视觉特征、镜面、含重复纹理的区域进行定位。
## 定位失败的常见原因
用户定位的环境与地图构建的环境存在较大差异时，可能将导致定位失败，如：
* 视角变化
确保建图尽可能覆盖潜在定位角度。如果定位的角度和最接近建图角度差别超过 45°，定位成功率会大幅下降。
* 光照差异
建图光照和定位光照相近情况下，定位成功率最高。例如尽量避免在白天建图后，在漆黑的夜晚尝试定位。
* 距离变化
建图时移动手机并覆盖不同距离的位置。例如距离目标 1 米附近的位置建图后，在距离 10 米的地方尝试定位容易失败。
## 延伸阅读
* [稀疏空间地图支持的设备](devices.html)
* [稀疏空间地图与 ARKit/ARCore 区别](comparison.html)
