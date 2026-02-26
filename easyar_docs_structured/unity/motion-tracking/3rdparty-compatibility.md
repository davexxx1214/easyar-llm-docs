---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/3rdparty-compatibility.html
original_file: doc--zh-cn--develop--unity--motion-tracking--3rdparty-compatibility.md
normalized_at: 2026-02-27
---
# ARCore、AR Engine 版本兼容性
本文介绍 EasyAR Sense Unity Plugin 对第三方运动跟踪 SDK 版本的兼容性。
## ARCore 版本兼容性
EasyAR Sense Unity Plugin 集成了 ARCore SDK 1.46.0。
* 使用集成的 ARCore SDK 时：支持至少 ARCore （Google Play Services for AR） 1.46.0 及以上版本。更早版本的 ARCore 服务是否支持需要看 Google 自身的兼容性。
* 使用 AR Foundation 或其它 ARCore SDK 的发布时，ARCore 兼容性将由这些框架决定。
## 华为 AR Engine 版本兼容性
EasyAR Sense Unity Plugin 集成了 AR Engine SDK 3.7.0.3。
* 支持至少 AR Engine 2.18 及以上版本。详细兼容信息建议查阅 AR Engine 官方说明。
EasyAR Sense Unity Plugin 不直接支持华为官方已不再维护的 `Huawei AR Engine Unity SDK` 或是其它第三方发布的类似 SDK。使用 AR Engine 也无需在 Unity 中另行导入这些 SDK。
> **重要事项**
AR Engine 的支持是通过自定义相机实现的。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
## 相关主题
* [运动跟踪简介](../../motion-tracking/intro.html)
* [支持 ARCore 运动跟踪的设备](../../motion-tracking/devices-arcore.html)
* [支持 AR Engine 运动跟踪的设备](../../motion-tracking/devices-arengine.html)
* [AR Foundation 版本兼容性](../fundamentals/arfoundation.html)
* [EasyAR 全局配置参考](../fundamentals/setup-player.html)
