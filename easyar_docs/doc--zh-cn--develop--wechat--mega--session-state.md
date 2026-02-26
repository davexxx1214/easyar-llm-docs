---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-state.html
original_file: doc--zh-cn--develop--wechat--mega--session-state.md
normalized_at: 2026-02-27
---
# AR Session 流程控制
这篇文档将介绍 AR Session 流程控制，包括如何创建、启动、停止并销毁 AR Session。
## 开始之前
* 了解 [AR Session 的概念与流程](session-state.html)
## 创建
使用配置中的云定位库 `appId`，云服务 `serverAddress`，云服务 `apiKey` 和 `apiSecret` 创建 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)。
然后使用创建的 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member) 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
再使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
```
createSession() {
// 获取场景中挂载的 megaComponent
const megaElement = scene.getElementById('easyar-mega');
const megaComponent = megaElement.getComponent("easyar-mega") as easyar.EasyARMegaComponent;
// MegaTracker 云服务鉴权配置
const apiKeyAccess = new mega.APIKeyAccessData(this.data.appId, this.data.serverAddress, this.data.apiKey, this.data.apiSecret);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess
}
// Session 配置
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
}
// 创建实例
session = megaComponent.createSession(sessionConfigs);
}
```
>
> 这段代码演示了如何从场景中获取
`> megaComponent
`> 之后使用配置创建 session 实例。
>
> **小心**
单实例限制：一个场景中仅允许存在一个 Session 实例。在创建新 Session 前，必须确保已调用 [closeSession()](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_closeSession_member_1_) 销毁旧实例，否则将导致创建失败。
## 启动
一般在 xr-frame 的 AR 系统准备就绪的回调中使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 方法启动 session。
> **警告**
MegaTracker 依赖于平面 AR 追踪器提供的数据，在平面追踪器初始化完成前无法工作。
在 WXML 中使用 `bind:ready="handleReady"` 注册 AR 系统准备就绪事件：
```
<xr-scene ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
```
在 xr-frame 组件中的回调函数 `handleReady` 中使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 方法启动 session。
```
handleReady: function(event) {
try {
//启动 Session，默认失败重试 5 次
await session.start();
} catch (err) {
console.error(`EasyAR Session initialization failed: ${err.message}`);
return;
}
}
```
## 停止并销毁
使用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [closeSession()](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_closeSession_member_1_) 方法销毁 session。
建议在 xr-frame 组件生命周期的 [detached](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) 中调用保证在离开页面时（即组件实例被从页面节点树移除时）销毁。
```
lifetimes: {
detached: function() {
const megaElement = scene.getElementById('easyar-mega');
const megaComponent = megaElement.getComponent("easyar-mega") as easyar.EasyARMegaComponent;
megaComponent.closeSession();
}
}
```
## 前后台切换
在页面退到后台时使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [pause()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_pause_member_1_) 方法暂停 session。
在页面回到前台时使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [resume()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_resume_member_1_) 方法恢复 session。
```
/\*\* 小程序页面的调用\*/
onHide() {
if (this.ar) {
this.ar.pauseSession();
}
},
onShow() {
if (this.ar) {
this.ar.resumeSession();
}
}
/\*\* xr-frame 组件中的函数\*/
pauseSession(): void {
if (!session) { console.error("EasyAR Session is not ready"); return;}
session.pause();
},
resumeSession(): void {
if (!session) { console.error("EasyAR Session is not ready"); return;}
session.resume();
}
```
>
> 这段代码中 xr-frame 组件暴露了
`> pauseSession()
`> 和
`> resumeSession()
`> 两个函数。
>
> 在小程序页面中在
[> onHide
](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onHide)> 即小程序从前台进入后台时调用
`> pauseSession()
`> 暂停 session。
>
> 在
[> onShow
](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppShow.html)> 即小程序从后台进入前台时调用
`> resumeSession()
`> 恢复 session。
>
