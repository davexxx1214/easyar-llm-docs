---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-device-orientation.html
---

AR Session 屏幕旋转适配 | EasyAR 文档
**
##### Table of Contents
**
# AR Session 屏幕旋转适配
这篇文章介绍了当需要横屏运行微信小程序时如何配置 AR Session。
## 开始之前
* 通过 [AR 驱动的 3D 渲染](../../fundamentals/fundamentals.html)了解相机图像相对于屏幕方向的旋转角是什么。
* 了解 [AR Session 的概念与流程](session-state.html)。
## Mega 小程序插件的屏幕朝向枚举
##### 注意
手机屏幕的朝向定义请参考 IOS, Android 等系统的官方定义。
Mega 小程序插件的屏幕朝向枚举 [DeviceOrientation](../../../api/wechat/easyar.DeviceOrientation.html):
|Constant|Value|Description|
|`Portrait`|0|Portrait|
|`LandscapeLeft`|90|LandscapeLeft|
|`PortraitUpsideDown`|180|PortraitUpsideDown|
|`LandscapeRight`|270|LandscapeRight|
## 在微信小程序全局配置中修改屏幕朝向
在 `app.json` 中添加 `window` 配置，具体定义见 [响应显示区域变化](https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html) 。
```
`"window": {
"pageOrientation": "landscape"
}
`
```
根据实际情况填入 "portrait"（竖屏） 或者 "landscape"（横屏）。
##### 小心
任何时候**不要**在 AR 小程序应用中使用 "auto"，在某些情况下会导致 AR 画面严重异常。
## 设置屏幕朝向
调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_) 传入屏幕旋转的方向，可随时调用，立即生效。
比如需要在屏幕相对自然竖直位置逆时针旋转 90 度的横屏模式下使用：
```
`let deviceOrientation = mega.DeviceOrientation.LandscapeLeft;
session.setDeviceOrientation(deviceOrientation);
`
```
mega 插件提供的屏幕朝向设置是为了**弥补微信小程序屏幕朝向监听缺失**。微信在 `pageOrientation` 设置中仅提供了 `portrait` 和 `landscape` 两个选项，而对于 AR 应用来说仅这两个选项是不够的。例如自然朝向逆时针旋转90度的横屏和自然朝向逆时针旋转270度的横屏完全不同。
因此当 `app.json` 中 `pageOrientation` 设置为 `portrait` 时，可以不调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_)，因为一般手机的自然竖直方向是 session 的默认朝向。
当 `app.json` 中 `pageOrientation` 设置为 `landscape` 时，必须调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_) 将屏幕朝向固定为 [LandscapeLeft](../../../api/wechat/easyar.DeviceOrientation.html#w_easyar_DeviceOrientation_LandscapeLeft_member) 或 [LandscapeRight](../../../api/wechat/easyar.DeviceOrientation.html#w_easyar_DeviceOrientation_LandscapeRight_member)