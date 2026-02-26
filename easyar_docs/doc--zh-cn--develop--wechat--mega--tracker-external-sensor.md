---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-external-sensor.html
---

MegaTracker 传感器外部控制 | EasyAR 文档
**
##### Table of Contents
**
# MegaTracker 传感器外部控制
默认情况下，MegaTracker 会自动管理加速度计和 GNSS 数据的监听接口。但在某些复杂应用场景中，开发者可能需要手动控制这些接口的开启和关闭，以实现更精细的功耗管理或权限控制。
## 开始之前
* 了解[MegaTracker 的概念与工作流](tracker.html)
## 外部控制约束逻辑
在 session 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 时，可以通过 [MegaTrackerSensorOptions](../../../api/wechat/easyar.MegaTrackerSensorOptions.html) 配置传感器的监听接口。
|参数名|类型|默认值|说明|
|isAcceExternalControl|`boolean`|`false`|加速度计是否由外部（开发者）控制。|
|isGeoExternalControl|`boolean`|`false`|GNSS 数据是否由外部（开发者）控制。|
##### 提示
**适用场景**：如果您的应用除了 Mega 功能外，本身不直接订阅传感器数据，建议保持默认值 `false`，由 Mega 自动处理。
当上述参数设置为 `true` 时，开发者必须严格遵守以下调用顺序：
* **启动流程**
在调用 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) **之前**，必须确保已手动开启对应的传感器监听：
* **加速度计**：调用 [wx.startAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.startAccelerometer.html)。
* **GNSS**：调用 [wx.startLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)。
* **停止流程**
在调用 [stop()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_stop_member_1_) **之后**，方可关闭对应的传感器监听：
* **加速度计**：调用 [wx.stopAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.stopAccelerometer.html)。
* **GNSS**：调用 [wx.stopLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.stopLocationUpdate.html)。
##### 小心
**冲突警告**：若设置为 `false`（Mega 托管），不能在 Session 运行期间调用微信原生的停止传感器接口，否则会导致数据中断。
```
`const megaTrackerSensorOptions: easyar.MegaTrackerSensorOptions = {
isAcceExternalControl: false,
isGeoExternalControl: true
};
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess,
options: megaTrackerSensorOptions
};
session = megaComponent.createSession(megaTrackerConfigs);
`
```
>
> 这个例子演示了如何外部控制开启和关闭微信地理位置数据监听，在调用
[> start(options)
](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_)> 之前，需要调用
[> wx.startLocationUpdate
](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)> 以开启微信地理位置数据监听。
>