---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/getting-started/quickstart.html
original_file: doc--zh-cn--develop--wechat--getting-started--quickstart.md
normalized_at: 2026-02-27
---
# 在微信小程序中使用 AR
在微信小程序中开发 AR 应用，依赖微信提供的 VisionKit 和 xr-frame 组件。开发者可以实现图像跟踪、运动跟踪等功能。通过 EasyAR，在微信小程序上还支持 Mega 和图像云识别（CRS）功能。
为了实现小程序上的 AR 体验，需要多个组件共同工作：
* XR-Frame 负责小程序上相机控制和 3D 虚拟内容的渲染和叠加。
* VisionKit 负责提供图像跟踪、设备本地运动跟踪等。
* EasyAR CRS 提供图像云识别相对于已知平面目标的位置和姿态。
* Mega 提供设备相对于已知空间环境的六自由度位置和姿态。
## 后续步骤
为方便您快速开发微信小程序的应用，请参阅相关入门指南和示例代码。
* [图像云识别快速入门](../cloud-recognition/quickstart.html)
* [Mega 快速入门](../mega/quickstart.html)
