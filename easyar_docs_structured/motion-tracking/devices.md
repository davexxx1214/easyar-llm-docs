---
source: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices.html
original_file: doc--zh-cn--develop--motion-tracking--devices.md
normalized_at: 2026-02-27
---
# 运动跟踪支持的设备
如果一个设备（手机、眼镜或头显）通过硬件或软件方案具有真实尺度的六自由度运动跟踪能力，我们称其为运动跟踪设备。这些设备包括但不限于可以运行 EasyAR 运动跟踪、 ARCore/ ARKit、华为 AR Engine 的设备，或具有六自由度跟踪能力的眼镜。
EasyAR 运动融合可以让图像和物体跟踪摆脱抖动困扰，跟踪稳定，并且可以在离开相机视野之后继续跟踪。
## 不同平台的运动跟踪方案的选择
部分操作系统或厂商通过系统原生的 AR SDK 提供类似的运动跟踪功能，如苹果 ARKit,谷歌 ARCore 和华为 AR Engine 等。
为保证最佳效果，在部分平台，EasyAR 自动选择当前可用的平台原生的运动跟踪方案而不需要额外配置。例如在 iOS 平台上，EasyAR 会优先调用 ARKit 的运动跟踪功能。需要进一步了解，请参阅[EasyAR运动跟踪与平台原生运动方案的关系](comparison.html)。
EasyAR 的运动跟踪解决方案，目前支持的设备包括主流的智能手机和平板电脑。EasyAR 的运动跟踪功能目前暂不支持 AR/MR 眼镜等可穿戴设备。如果这些设备本身支持六自由度的运动跟踪功能，开发者可以通过自定义相机接入 EasyAR 并与的其他功能联合使用。
对于微信小程序开发者，由于平台限制无法直接使用上述任何的运动跟踪方案，可以参阅微信小程序提供的类似[运动跟踪](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)功能。
## 延伸阅读
了解运动跟踪支持的具体机型
* [EasyAR 运动跟踪支持的设备](devices-easyar.html)
* [ARCore 运动跟踪支持的设备](devices-arcore.html)
* [AR Engine 运动跟踪支持的设备](devices-arengine.html)
* [微信小程序支持的设备](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)
