---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-plane-detection-error.html
original_file: doc--zh-cn--develop--wechat--mega--session-plane-detection-error.md
normalized_at: 2026-02-27
---
# 平面 AR 追踪器异常处理
这篇文章介绍了如何通过注册回调处理微信平面 AR 追踪器的异常。
## 开始之前
* 通过[MegaTracker 工作流](tracker.html)了解：
* xr-frame 的[平面AR追踪器](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#Plane) 本质上是 [VisionKit 6DoF-平面能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)的封装。
* MegaTracker 是如何在 xr-frame 上工作的。
* 了解 [AR Session 的概念与流程](session-state.html)
## 为什么会出现平面检测异常
在特定情况下（如画面中出现大片白墙、摄像头长时间被遮挡等），微信平面 AR 追踪器可能出现状态异常。
此时平面 AR 追踪器无法正常输出每帧的相机位姿（即 6DoF 数据）这会导致 MegaTracker 无法工作。
当画面正常（纹理丰富，摄像头不被遮挡）一段时间后平面 AR 追踪器会恢复工作，同时 MegaTracker 也会恢复工作。
## 设置平面检测异常时的行为
通过 [setPlaneDetectionErrorBehavior(behavior)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setPlaneDetectionErrorBehavior_member_1_) 注册异常处理回调。当检测到异常时，该回调会被触发，开发者可在其中实现自定义提示，隐藏 3D 内容或其他处理逻辑。
```
session.setPlaneDetectionErrorBehavior(() => {
wx.showToast({
icon: 'none',
title: `微信平面检测结果异常，请将相机对着平面来回移动以恢复跟踪`,
duration: 2000,
});
});
```
>
> 这个例子中使用 session 的
[> setPlaneDetectionErrorBehavior(behavior)
](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setPlaneDetectionErrorBehavior_member_1_)> 接口注册了一个弹出 Toast 窗口的回调，当平面检测异常时触发。
>
