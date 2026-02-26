---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/known-issues.html
original_file: doc--zh-cn--develop--wechat--mega--known-issues.md
normalized_at: 2026-02-27
---
# 微信小程序 Mega 插件已知问题与限制
这篇文章介绍了 Mega 小程序插件在使用过程中的已知问题和限制。
## 微信已知问题
当前微信 xr-frame 或 VisionKit 已确认的缺陷。发生时将导致 AR 功能失效，请在开发时留意相关触发场景。
### 微信平面检测异常
在特定情况下（如画面中出现大片白墙、相机长时间被遮挡等），微信提供的平面检测可能出现状态异常。在这种状态下，MegaTracker 无法正常工作。
处理方法参考 [平面 AR 追踪器异常处理](session-plane-detection-error.html)。
### Session 初始化时间较长
AR Session 需要等待微信平面检测初始化完成后才能完成初始化。在某些情况下，微信平面检测初始化时间较长。
AR Session 需要等待 xr-frame ARTracker 初始化完成的原因 请见 [MegaTracker 是如何在 xr-frame 上工作的](tracker.html)。
* **状态参考**：[微信小程序 AR 追踪器状态文档](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#获取追踪状态)。
* **监听示例**：
```
<xr-ar-tracker id="xrARTracker" mode="Plane" bind:ar-tracker-state="handleARTrackerState"></xr-ar-tracker>
```
```
handleARTrackerState({detail}) {
if (detail.value.state == xrFrameSystem.EARTrackerState.Detected) {
console.log('Plane is now detected by XR-Frame ARTracker.');
}
}
```
### 节点的 worldPosition 在当前帧不会被立刻更新
这个例子中 `trs.worldPosition` 未被及时更新：
```
public onTick(delta, data) {
const trs = this.el.getComponent(xrFrameSystem.Transform);
// 更新前该节点的 WorldPosition
console.log(`World Position before update: ${trs.worldPosition.x}, ${trs.worldPosition.y}, ${trs.worldPosition.z}`);
// 更新前该节点的 LocalPosition
console.log(`Local Position before update: ${trs.Position.x}, ${trs.Position.y}, ${trs.Position.z}`);
trs.position.x += 0.1;
trs.position.y += 0.1;
trs.position.z += 0.1;
// 该节点的 WorldPosition 未被更新
console.log(`World Position after update: ${trs.worldPosition.x}, ${trs.worldPosition.y}, ${trs.worldPosition.z}`);
// 该节点的 LocalPosition 被更新
console.log(`Local Position after update: ${trs.Position.x}, ${trs.Position.y}, ${trs.Position.z}`);
}
```
在开发中建议一直使用 LocalTransform ， 即 `el.getComponent(xrFrameSystem.Transform).position` 和 `el.getComponent(xrFrameSystem.Transform).rotation`。
### 屏幕方向切换异常
在微信小程序全局配置 `app.json` 中的 `window` 若填入 "auto"。
设备以横屏模式离开小程序后，若以竖屏模式重新进入，会出现 AR 画面异常的情况。
因此任何时候**不要**在 AR 小程序应用中使用 "auto"。
## 使用限制
功能运行的硬性要求。未满足时功能不可用，但可通过调整配置或环境予以避免。
### 机型限制
运行 Mega 小程序插件的设备需要至少支持 **微信 VisionKit V1 平面接口**。为获得理想效果，建议使用支持 **微信 VisionKit V2 平面接口** 的设备。
* **支持机型列表**：参考 [V2 平面 AR 接口支持列表](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)。
* **快速判断方法**：
1. 扫描微信小程序官方 Sample 二维码。
![微信小程序官方 Sample 二维码](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites01.png)
2. 进入小程序后，导航至 **接口** > **VisionKit 视觉能力** > **水平面 AR-v2**，即可快速判断当前设备是否支持。
如果需要在不支持 VisionKit 的设备上使用 Mega 服务，请参考[导航场景最佳实践](../../mega/navigation.html) 使用支持几乎所有设备的**视＋ AR 导航产品**。
### PlaneMode 强制配置
受部分微信接口支持限制，**planeMode** 必须设置为 **1** 。
```
<xr-scene ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
```
### GPS 功能限制
暂不支持通过 GPS 对齐 Block。
暂不支持通过 GPS 摆放标注数据。
## 相关主题
* [MegaTracker的概念与工作流](tracker.html)
* [平面 AR 追踪器异常处理](session-plane-detection-error.html)
* [AR Session 屏幕旋转适配](session-device-orientation.html)
