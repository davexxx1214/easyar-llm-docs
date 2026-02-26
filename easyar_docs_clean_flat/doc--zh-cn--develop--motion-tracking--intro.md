---
source: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/intro.html
original_file: doc--zh-cn--develop--motion-tracking--intro.md
normalized_at: 2026-02-27
---
# 什么是运动跟踪功能？
## 运动跟踪功能介绍
AR 的运动跟踪功能泛指通过计算机视觉和传感器融合算法，实时跟踪设备（手机、平板、智能眼镜）相对于环境的六自由度位置和朝向的功能。部分厂商或操作系统原生的混合现实 SDK 提供类似的运动跟踪功能，如苹果 [ARKit](https://developer.apple.com/augmented-reality/arkit/),谷歌的 [ARCore](https://developers.google.com/ar),华为的 [AR Engine](https://developer.huawei.com/consumer/en/hms/huawei-arengine/) 等。在部分智能眼镜上，厂商提供类似的运动跟踪功能。在微信小程序平台上，微信开放了功能与运动跟踪相似的[6DoF AR 能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)。
通过厂商或操作系统支持的设备占比相对较低，为了使得更多机型支持运动跟踪功能， EasyAR 的运动跟踪（Motion Tracker）利用计算机视觉、惯性同步定位和建图（VI-SLAM）技术，在更多的机型上实现六自由度的实时跟踪。
![Motion Tracking](https://doc-asset.easyar.com/develop/motion-tracking/media/motion-tracking.png)
## 后续步骤
* 了解 [EasyAR 运动跟踪支持的设备](devices.html)
* 了解 [EasyAR 运动跟踪与 EasyAR 其他模块的关系](motion-tracking-and-easyar.html)
* 了解 [EasyAR 运动跟踪与ARKit/ARCore/华为AR Engine的关系](comparison.html)
