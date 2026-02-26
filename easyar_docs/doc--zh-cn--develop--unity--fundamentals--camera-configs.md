---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/camera-configs.html
---

配置 camera | EasyAR 文档
**
##### Table of Contents
**
# 配置 camera
通过以下内容，您将了解如何配置 Unity 中 AR 场景的 camera 以获得最佳的 AR 体验。
## 开始之前
* 通过 [Camera](camera.html) 了解 AR 场景中摄像机的作用，以及 session 如何控制摄像机的属性以确保正确的 AR 体验。
## 适用于手机和 PC 设备的 camera 配置
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/camera-config.png)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/camera-config-urp.png)
在手机和 PC 设备上使用 AR 时，建议按照以下方式进行配置：
* **Clear Flags**：需要设置为 `Solid Color` 以确保 camera 图像可以正常渲染。如果保留默认的 *Skybox* ，camera 图像将无法显示。
* **Background**：非必需。考虑到使用体验，建议将背景颜色设为黑色以便在 camera 设备打开前和切换时以黑色过度。
* **Clipping Planes**：除通常渲染及性能需求之外，需要综合考虑识别及交互的物体或现实场景的物理大小和距离。比如可以设置 `Near` 为 0.1（米）以避免摄像机离物体较近时无法显示，设置 `Far` 为 1000（米）以避免远处物体无法显示。
##### 注意
使用 AR Foundation 或其他 Unity XR Origin 下的 camera 时，Unity 通常会预设其剪裁平面为 (0.1, 20) ，这可能会导致距离真实世界中的设备超过 20 米的物体无法显示出来。请在使用前根据具体需求来修改。
## 适用于头显的 camera 配置
使用头显时，camera 通常由设备 SDK 进行配置和控制，因此建议保留设备 SDK 默认配置，或根据设备 SDK 的要求进行配置。另外可以根据需要修改 **Clipping Planes**。