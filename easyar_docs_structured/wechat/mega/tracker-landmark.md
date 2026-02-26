---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-landmark.html
original_file: doc--zh-cn--develop--wechat--mega--tracker-landmark.md
normalized_at: 2026-02-27
---
# 使用 Mega Landmark 服务
这篇文章介绍了在微信小程序 Mega 插件接入后，如何使用 Mega Landmark 的定位服务。
## 开始之前
* [获取和使用 APIKey](../../apikey-auth.html)（必须包括**Mega Landmark**）。
* 了解 [MegaTracker 的概念与工作流](tracker.html)。
* 了解 [MegaTracker 云服务鉴权](tracker-access.html)。
## 启用 Mega Landmark
首先使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 作为 `apiType` 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
然后使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
```
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess,
apiType: mega.MegaApiType.Landmark
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
## 如何使用 LandmarkFilter
当使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 创建时，MegaTracker 会自动内部实例化 [MegaLandmarkFilter](../../../api/wechat/easyar.MegaLandmarkFilter.html)。
它的功能是 MegaTracker 在使用 Landmark 服务时通过 SpotId 或 GNSS 数据筛选当前最合适的 Mega 定位库。
筛选接口只能在 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 成功后调用。
当 MegaTracker 使用 Landmark 服务而**没有**筛选成功时，定位状态始终为 [MissingSpotVersionId](../../../api/wechat/easyar.MegaLocalizationStatus.html#w_easyar_MegaLocalizationStatus_MissingSpotVersionId_member)
* **使用提供的 SpotID 匹配定位库**：
使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 的 [filterBySpotId(spotId)](../../../api/wechat/easyar.MegaLandmarkFilter.html#w_easyar_MegaLandmarkFilter_filterBySpotId_member_1_) 方法通过 SpotID 匹配定位库：
```
async landmarkFilter() {
const res = await session.megaTracker.landmarkFilter.filterBySpotId(settings.LandmarkSpotId);
if (res.status != mega.MegaLandmarkFilterStatus.Found) {
console.error(`LandmarkFilter Failed, status: ${mega.MegaLandmarkFilterStatus[res.status]}, exceptionInfo : ${res.exceptionInfo}`)
}
}
```
* **使用当前的 GNSS 数据匹配定位库**：
使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 的 [filterByLocation()](../../../api/wechat/easyar.MegaLandmarkFilter.html#w_easyar_MegaLandmarkFilter_filterByLocation_member_1_) 方法通过使用当前的 GNSS 数据 匹配定位库：
```
async landmarkFilter() {
const res = await session.megaTracker.landmarkFilter.filterByLocation();
if (res.status != mega.MegaLandmarkFilterStatus.Found) {
console.error(`LandmarkFilter Failed, status: ${mega.MegaLandmarkFilterStatus[res.status]}, exceptionInfo : ${res.exceptionInfo}`)
}
}
```
