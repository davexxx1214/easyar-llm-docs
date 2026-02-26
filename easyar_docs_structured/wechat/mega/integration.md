---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/integration.html
original_file: doc--zh-cn--develop--wechat--mega--integration.md
normalized_at: 2026-02-27
---
# 将 Mega 插件接入您的微信小程序
本文档将带您完成 Mega 插件在 xr-frame 小程序环境下的接入。
## 开始之前
* 参考 [xr-frame 开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)及 [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)学习如何使用微信官方提供的 XR-3D 引擎，内容包括：
* 常规微信小程序页面中引入 xr-frame 组件的方式。
* xr-frame 组件与小程序传统组件的通信方式。
* 如何从场景中获取或创建一个元素并修改部分属性比如 `Transform`。
* 加载和释放资源，例如 GLTF 模型。
## 全局配置
在小程序根目录下的 `app.json` 全局配置文件中添加对 Mega 小程序插件的依赖，并将[依赖加载](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/lazyload.html)改为**按需注入**。
```
{
"lazyCodeLoading": "requiredComponents",
"plugins": {
"easyar-wechat-miniprogram": {
"version": "2.0.2", //使用最新的插件版本
"provider": "wx27fa3b52b5462e8f" // Mega 小程序插件固定 id
}
}
}
```
## 加载插件
您可以通过[插件接口](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/using.html#js-接口)引入插件，直接使用插件的部分方法以验证插件是否已经被正确加载。
例如使用通过微信提供的 `requirePlugin(string path)` 接口拿到 [EasyARWechatMiniprogramPlugin](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html) 后，使用它的 [isMegaTrackerSupported](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_isMegaTrackerSupported_member) 方法判断设备是否支持。
```
//如果已经引入了 typings 文件
//const easyarPlugin: easyar.EasyARWechatMiniprogramPlugin = requirePlugin("easyar-wechat-miniprogram") as easyar.EasyARWechatMiniprogramPlugin;
const easyarPlugin = requirePlugin("easyar-wechat-miniprogram") as any;
//调用 isMegaTrackerSupported 判断当前设备是否支持，若不支持则弹窗提示
if (!easyarPlugin.isMegaTrackerSupported()) {
const message = `当前设备不支持 VK v1 和 v2，请参考微信官方文档：https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html`;
wx.showModal({
title: "设备不支持",
content: message,
showCancel: false,
});
console.error(message);
return;
}
```
>
> 这个例子中首先通过微信提供的
`> requirePlugin(string path)
`> 接口拿到了
`> easyarPlugin
`> 即插件暴露的接口对象，之后调用了其提供的
[> isMegaTrackerSupported
](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_isMegaTrackerSupported_member)> 方法判断当前运行环境下是否可用。若不可用则弹窗提示。
>
## 引入类型
建议使用 **Typescript** 进行开发。
样例工程中的路径：`/typings/types/easyar/lib.easyar.d.ts` 。
拷贝到工程相同目录，并在 `/typings/types/index.d.ts` 中以**三斜杠指令**引用：
```
/// <reference path="./easyar/lib.easyar.d.ts" />
```
当需要使用类型对象时，可以通过 [getMegaSystem](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_getMegaSystem_member) 获取 EasyAR Mega 微信小程序插件的类型系统 [IMegaSystem](../../../api/wechat/easyar.IMegaSystem.html)。
```
const mega: easyar.IMegaSystem = easyarPlugin.getMegaSystem();
```
之后可以使用 [IMegaSystem](../../../api/wechat/easyar.IMegaSystem.html) 中暴露的类型进行类型比较，例如可以用 `state` 比较与 `mega.SessionState.Running` 是否相等判断 session 是否初始化成功：
```
const newState: easyar.SessionState = event.detail.value;
if (newState === mega.SessionState.Running) {
console.log("EasyAR Session initialized succeeded. Start running.");
}
```
## xr-frame 场景搭建（WXML）
在页面的 WXML 文件中，`xr-easyar-mega` 组件必须作为 `xr-scene` 的子节点，并正确绑定相机与追踪器的 `id` ，若不填写 `id` 则组件会使用在场景中第一个查找到的 `xr-camera` 和 `xr-ar-tracker` 组件。
```
<xr-scene id="xr-scene" ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
<xr-easyar-mega
id="easyar-mega"
camera-id="xrCamera"
ar-tracker-id="xrARTracker"
></xr-easyar-mega>
<xr-node>
<xr-ar-tracker id="xrARTracker" mode="Plane"></xr-ar-tracker>
<xr-camera id="xrCamera" node-id="xrCamera" clear-color="0.925 0.925 0.925 1" background="ar" is-ar-camera></xr-camera>
</xr-node>
<xr-shadow id="shadow-root" node-id="xrShadow"></xr-shadow>
</xr-scene>
```
> **小心**
`ar-system` 的 `planeMode` 必须设置为 `1`
## 注册 Mega 插件的事件回调
```
<xr-easyar-mega
id="easyar-mega"
camera-id="xrCamera"
ar-tracker-id="xrARTracker"
bind:sessionStateChange="onSessionStateChange"
bind:megaLocalizationResult="onMegaLocalizationResult"
bind:postSessionUpdate="onPostSessionUpdate"
></xr-easyar-mega>
```
在 WXML 中绑定 xr-frame Element 代理分发的事件，xr-frame 的事件分发机制请参考 [xr-frame 事件机制](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/event.html)
插件分发的事件有：
|事件名称|参数类型|说明|
|`SessionStateChange`|[SessionState](../../../api/wechat/easyar.SessionState.html)|Session 状态改变时立即触发。参数为 Session 新的状态，用于处理 Session 初始化开始与成功的回调。|
|`MegaLocalizationResult`|[MegaLocalizationResult](../../../api/wechat/easyar.MegaLocalizationResult.html)|收到 Mega 定位结果的渲染帧完成更新后触发。事件触发时，该渲染帧内所有受 EasyAR 控制的 Transform 变化已经完成。|
|`PostSessionUpdate`|无参数|Session 在该渲染帧完成更新后立即触发。此时该帧内所有受 EasyAR 控制的 Transform 变化已经完成。|
## AR Session
session 的创建，启动及销毁请见 [AR Session 流程控制](session-state.html)
通过 `sessionStateChange` 事件回调确认初始化是否成功。当状态变为 [Running](../../../api/wechat/easyar.SessionState.html#w_easyar_SessionState_Running_member) 时，即可认为 ARSession 已就绪。
在 WXML 中通过 `bind:sessionStateChange="onSessionStateChange"` 将 xr-frame 组件中的 `onSessionStateChange()` 函数注册为 `sessionStateChange` 事件的回调：
```
<xr-easyar-mega
bind:sessionStateChange="onSessionStateChange"
></xr-easyar-mega>
```
在 xr-frame 组件中的回调函数 `onSessionStateChange()` 中将 session 状态与 [SessionState](../../../api/wechat/easyar.SessionState.html) 的各个枚举进行比较可判断 session 当前状态。
```
onSessionStateChange(event) {
const newState: easyar.SessionState = event.detail.value;
console.log(`EasyAR Session state changed to: ${mega.SessionState[newState]}`);
let displayInfoStr: string = "";
if (newState === mega.SessionState.None) {
displayInfoStr = "EasyAR Session is inactive.";
} else if (newState === mega.SessionState.Initializing) {
displayInfoStr = "EasyAR Session is initializing...";
} else if (newState === mega.SessionState.Running) {
displayInfoStr = "EasyAR Session initialized succeeded. Start running.";
}
this.triggerEvent("sessionDisplayInfoEvent", displayInfoStr);
}
```
>
> 上述代码中，初始化完成后控制台应打印 "EasyAR Session initialized succeeded. Start running."
>
## 相关主题
* [完整运行示例工程](fullstart.html)
* [AR Session 流程控制](session-state.html)
* [示例工程说明](sample.html)
