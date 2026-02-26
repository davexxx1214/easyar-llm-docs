---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/guide.html
---

图像云识别微信小程序开发者指南 | EasyAR 文档
**
##### Table of Contents
**
# 图像云识别微信小程序开发者指南
本章主要介绍 EasyAR 云识别和微信小程序结合的常用功能以及实现方法。
## 功能和使用
微信小程序 XR-FRAME 是微信官方推出的 XR/3D 应用开发解决方案，采用混合渲染技术实现接近原生的性能表现，兼具视觉效果与开发便捷性，可快速构建 AR 应用。该框架支持图像跟踪、3D 模型加载、动画控制、视频播放及粒子特效等核心功能，开发模式以 WXML 模板化编程为主，仅需少量逻辑代码即可实现高质量视觉效果。
EasyAR 云识别（CRS）服务专注于海量图像库的以图搜图场景，通过云端算法实现高效目标识别，具有高性价比和低接入门槛的特点，开发者可快速集成并完成功能开发。
### 数据流
```
`flowchart TB
B[API 或者 EasyAR Web] --&gt; A[云识别 CRS] &lt;--&gt; D[设备端 微信小程序]
C[虚拟内容] &lt;--&gt; D[设备端 微信小程序]
`
```
XR-FRAME 和云识别两者结合以后，本地设备将不再受目标图数量的限制，可以解决应用对超大范围的需求。
### 实现流程
1. 云识别服务调用‌
* 通过 EasyAR 云识别（CRS）API 发起图像识别请求
* 处理识别结果（识别成功/失败，处理 Meta 等）
* 跟踪图配置‌
* 根据识别结果中的 trackingImage，动态设置 xr-ar-tracker
‌
* 虚拟资源加载‌
* 解析 Meta 数据中的资源标识符
* 使用 xr-asset 下载 3D 模型或视频等虚拟资产
* 将虚拟资产加入到场景中，并配置资源属性（如缩放比例、初始位置等）
‌
* AR 内容呈现‌
* 将虚拟资产与识别标记进行空间绑定
* 实现虚实融合的渲染效果
* 处理用户交互事件（如点击、拖拽等）
## 常用功能
云识别获取结果以后，微信小程序中常用的 AR 功能包括以下几种：
* 仅识别并展示识别结果
* 仅识别并展示识别目标关联的视频、动画、模型、脚本
* 识别 + 跟踪叠加视频、动画、模型、脚本
## 相关主题
* [微信小程序开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)