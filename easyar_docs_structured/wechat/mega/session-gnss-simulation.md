---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-gnss-simulation.html
original_file: doc--zh-cn--develop--wechat--mega--session-gnss-simulation.md
normalized_at: 2026-02-27
---
# AR Session 非现场使用
这篇文章介绍了如何不在现场时使用 AR Session。
## 开始之前
* 了解 [AR Session 的概念与流程](session-state.html)
## 启用 Simulator 模式
使用 **Simulator** 模式可以避免开发 AR 应用过程中开发者必须长期驻场的情况。
在该模式下，session 不使用 GNSS 数据或使用虚假的 GNSS 数据输入。
> **警告**
启用 Simulator 模式后，画面会出现特定水印。
小程序正式发布时，AR Session 不允许使用 Simulator 模式。请务必在上线前移除相关配置。
### 不使用 GNSS 数据
使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [setGeoLocationInput(inputMode, geoLocation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setGeoLocationInput_member_1_) 方法 仅传入 "Simulator" 字符串。此后 session 不进行任何经纬度相关的定位。
```
session.setGeoLocationInput("Simulator");
```
### 使用模拟的 GNSS 数据
若需模拟用户处于特定位置，使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [setGeoLocationInput(inputMode, geoLocation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setGeoLocationInput_member_1_) 方法传入 "Simulator" 字符串和指定的经纬度。此后 session 使用模拟的经纬度数据进行定位。
```
const targetLongitude = 123.45; // 经度
const targetLatitude = 32.1; // 纬度
session.setGeoLocationInput("Simulator", { longitude: targetLongitude, latitude: targetLatitude });
```
> **警告**
模拟输入必须使用 WGS-84 坐标系的经纬度数据。
使用错误的经纬度数据可能会导致定位失败或错乱。
