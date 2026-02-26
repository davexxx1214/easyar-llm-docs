---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-access.html
original_file: doc--zh-cn--develop--wechat--mega--tracker-access.md
normalized_at: 2026-02-27
---
# MegaTracker 云服务鉴权
这篇文章介绍了如何指定 MegaTracker 使用云服务时的鉴权方式。
## 开始之前
* 了解[MegaTracker 的概念与工作流](tracker.html)
* [获取和使用 APIKey](../../apikey-auth.html)
## 使用 API Key 和 API Secret 鉴权
这种方式适用于传统的密钥对验证。你需要使用 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member) 来构造 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 中的 `access` 对象。
```
const apiKeyAccess = new mega.APIKeyAccessData(
settings.MegaTrackerAppID, // Mega 定位服务 AppID
settings.MegaTrackerServerAddress, // Mega 定位服务地址
settings.EasyARAPIKey, // APIKey 字符串
settings.EasyARAPISecret // APISecret 字符串
);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
>
> 这个例子中先使用配置中的云定位库
`> appId
`> ，云服务
`> serverAddress
`> ，云服务
`> apiKey
`> 和
`> apiSecret
`> 创建了
[> APIKeyAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)> 。
>
> 然后使用了创建的
[> APIKeyAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)> 创建
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> 。 这代表将使用 API Key 和 API Secret 鉴权
>
## 使用 API Token 鉴权
若能够使用服务器定时（每几分钟或几个小时）更新和下发 `APIToken`，使用这种方式避免了直接使用 APISecret 对定位请求进行签名，安全性更高。`APIToken` 的更新方式请参考 [Token的创建和使用方法](../../apikey-auth.html)。
可以根据 Token 的有效期，在前端设置定时器进行更新。
首先使用设置中的 Mega 定位库 AppID 和定位服务地址创建 [TokenAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member)。
然后使用创建的 [TokenAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member) 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
然后使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
当 Token 过期时，必须调用 [updateToken(apiToken)](../../../api/wechat/easyar.MegaTracker.html#w_easyar_MegaTracker_updateToken_member_1_) 进行更新，否则 Mega 服务将不可用，定位结果中的状态始终为 [ApiTokenExpired](../../../api/wechat/easyar.MegaLocalizationStatus.html#w_easyar_MegaLocalizationStatus_ApiTokenExpired_member)。
```
const tokenAccess = new mega.TokenAccessData(
settings.MegaTrackerAppID, // Mega 定位服务 AppID
settings.MegaTrackerServerAddress, // Mega 定位服务地址
"your\_api\_token" // APIToken 字符串
);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: tokenAccess
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
>
> 这个例子演示了如何使用
[> TokenAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member)> 创建
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> ，并且用这个
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> 创建 session 以使用
`> APIToken
`> 鉴权。
>
