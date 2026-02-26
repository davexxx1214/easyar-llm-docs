---
source: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/comparison.html
---

EasyAR 稀疏空间地图与 ARKit/ARCore 的区别 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR 稀疏空间地图与 ARKit/ARCore 的区别
EasyAR 稀疏空间地图用于扫描用户周围小范围环境（房间级别），建立视觉地图并导出，可用于多个设备间实时共享，实现多人互动、持久化等功能。类似的方案还包括 ARKit 提供的 ARWorldMap 和 ARCore 提供的 Cloud Anchors。
* ARWorldMap 支持将扫描场景序列化、持久化重定位，可以实现在 iOS 平台上的持久化、多人共享体验。
* Cloud Anchors 将用户扫描环境数据上传到 Google Cloud 上，通过重定位实现多人共享 AR 体验。
EasyAR 稀疏空间地图实现了离线、跨平台、高度自由的地图管理，更适合以下场合：
* 需要完全离线运行的场景（工厂小范围、地下室、展览馆无网环境）。
* 要跨 iOS/Android 等多平台共享同一套地图。
* 开发者希望自己完全掌控地图数据。
##### 注意
如果要扫描和重建的区域超过 100 平方米或者场景光照、季节等变化较大，建议升级至 [EasyAR Mega](../mega/intro.html) 功能。
## 延伸阅读
* [ARKit ARWorldMap](https://developer.apple.com/documentation/arkit/arworldmap)
* [ARCore Cloud Anchors](https://developers.google.com/ar/develop/cloud-anchors)