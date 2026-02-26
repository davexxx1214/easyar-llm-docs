---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/tracker.html
---

控制 Mega 跟踪过程 | EasyAR 文档
**
##### Table of Contents
**
# 控制 Mega 跟踪过程
本文介绍了如何控制 Mega 跟踪过程中的各项功能和参数，以满足不同应用场景的需求。
## 开始之前
* 检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
## 调整设备支持等级
[MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 的 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 属性用于指定 Mega 支持的最低设备等级。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-level.png)
Mega 可以在几乎所有类型的帧数据源上运行，但不同的帧数据源对跟踪效果有不同的影响。
默认情况下，Mega 会选择设备支持的最高等级的帧数据源进行跟踪。[默认配置下的支持 Mega 的 session](session-best-practice.html) 已经配置了支持 6DoF 和 5DoF 的帧数据源。
在 Mega 运行时要支持某个等级的帧数据源需要满足两个条件：
* 所需的帧数据源在 session 的可选帧数据源组中。
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 大于或等于所需的帧数据源的 [CameraTransformType](../../../api/unity/easyar.CameraTransformType.html) 等级。
比如，要在默认 session 中支持 3DoF 跟踪，需要：
* 添加 [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html) 到 session 的帧数据源组中。
* 修改 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)。
又比如，要在默认 session 中删除 5DoF 跟踪支持，需要：
* 从 session 的帧数据源组中删除 [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)。
* 修改 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)（即使不修改，由于没有 5DoF 帧数据源，5DoF 也不会被使用）。
在没有满足条件的帧数据源可用时，session 组装会失败。
## 跟踪目标管理
使用 Mega 时，需要指定 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 使用的 target 即 block。
### block 来源控制
大部分情况下，建议保持默认配置，即在编辑器中使用 Mega Studio 导入 block。
选中 session 下的 `Mega Tracker` 物体，`Block Root Source` 选项应该保持为 `External`（默认）。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-rootsource.png)
同时，需要指定 `Block Root` 为场景中的 `MegaBlocks` 物体。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-rootsource-external.png)
修改 `Block Root Source` 选项可以指定其它 block 来源方式，比如使用 ema 导入数据时，通常会选择 `Internal` 或 `Mixed` 选项。
在脚本中，可以修改 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 来达到同样的效果。
### 多目标跟踪控制
在大部分的 Mega 使用场景下，没有使用多目标的必要。在熟练掌握如何避免多个 block 互相影响之前，建议一个定位库中只放一个block。
##### 提示
原理上，Mega 会计算设备在所有 block 中的位置，而不是从定位库中抽选设备看到的 block。考虑不周的使用可能会因数据混淆等原因导致效果劣化。
选中 session 下的 `Mega Tracker` 物体，修改 `Multi Block` 选项可以启用或禁用多目标跟踪功能。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-multi-block.png)
在脚本中，可以修改 [BlockHolder.MultiBlock](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_MultiBlock) 来达到同样的效果。
##### 警告
一般情况下，一个定位库里只能同时有一个 block。
修改多目标配置会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中该配置被修改过，向 EasyAR 反馈问题时请务必说明这一点。
## 了解当前系统状态
在默认 session 配置下，[UI 消息](../diagnostics/ui-messages.html) 会显示在屏幕上，其中包含了 Mega 跟踪状态的信息。
在定位成功时，Mega Block 下会包含 `Found` 状态文字以及当前跟踪的 block 名称和 ID：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-status-found.png)
在定位失败时，Mega Block 下会包含 `NotFound` 状态文字：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-status-notfound.png)
##### 提示
`NotFound` 是正常状态，在 Mega 工作的整个过程中经常会出现该状态，出现该状态时跟踪仍然在继续。通常应用开发中不需要对 `NotFound` 状态进行特殊处理。
使用 [MegaTrackerFrameFilter.LocalizationRespond](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocalizationRespond) 事件可以获取当前的定位状态，从而了解系统当前是否找到了跟踪目标。
以下代码展示了如何使用该事件，以及常见的需要应用关注的异常状态的处理方法：
```
`private void Awake()
{
megaTracker.LocalizationRespond += HandleLocalizationStatusChange;
}
private void HandleLocalizationStatusChange(MegaLocalizationResponse response)
{
var status = response.Status;
wakingUpCount = status == MegaTrackerLocalizationStatus.WakingUp ? wakingUpCount + 1 : 0;
if (wakingUpCount &gt;= 5)
{
// 服务正在唤醒中，需要让终端用户等待
}
if (status == MegaTrackerLocalizationStatus.QpsLimitExceeded)
{
// QPS 超限，会随机有终端用户定位失败（总体跟踪质量下降）
// 这时一般需要付费提升 QPS 上限以保障当前用户量下的跟踪质量
}
if (status == MegaTrackerLocalizationStatus.ApiTokenExpired)
{
// Token过期，这只会出现在使用 Token 接口访问服务时
// 接近该问题需要应用请求自己的后台获取 Token，并调用 MegaTrackerFrameFilter.UpdateToken 进行更新
}
}
`
```
如果应用经常遇到 [MegaTrackerLocalizationStatus.RequestTimeout](../../../api/unity/easyar.MegaTrackerLocalizationStatus.html#u_easyar_MegaTrackerLocalizationStatus_RequestTimeout) 状态，通常说明设备连接服务的网络状况不佳，建议优化网络环境以提升跟踪质量。在网络状况无法改善的场景下，可以考虑增加请求超时时间。
##### 注意
无法通过该事件获取定位返回的 pose。
事实上，定位返回的 pose 在应用开发中是不需要的，EasyAR 会在定位返回后通过本地算法计算出更准确的 pose 并返回给开发者使用，而该 pose 已经体现在 block 的 transform 中，可以参考 [获取 session 的运行结果](../fundamentals/session-output.html)。
## 暂停和继续
Mega 的跟踪和定位功能可以分别暂停和继续。
### 暂停跟踪
设置 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 为 false 可以暂停跟踪。
默认在跟踪暂停后，所有 block 节点下的内容都会隐藏。
### 暂停定位
设置 [MegaTrackerFrameFilter.ResultPoseType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ResultPoseType).[EnableLocalization](../../../api/unity/easyar.MegaResultPoseTypeParameters.html#u_easyar_MegaResultPoseTypeParameters_EnableLocalization) 为 false 可以暂停定位。
##### 警告
暂停定位会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中定位被暂停过，向 EasyAR 反馈问题时请务必说明这一点。
## 服务和请求控制
可以通过修改 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件的参数来控制请求服务的行为。
### 请求间隔和超时
选中 session 下的 `Mega Tracker` 物体，修改 `Request Time Parameters` 下的选项可以调整请求服务的时间间隔和超时时间。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-timep.png)
在脚本中，可以修改 [MegaTrackerFrameFilter.RequestTimeParameters](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_RequestTimeParameters) 来达到同样的效果。
##### 警告
修改请求间隔会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中请求间隔被修改过，向 EasyAR 反馈问题时请务必说明这一点。
### 切换定位库
使用 [MegaTrackerFrameFilter.SwitchEndPoint(ExplicitAddressAccessData, BlockRootController)](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_SwitchEndPoint_easyar_ExplicitAddressAccessData_EasyAR_Mega_Scene_BlockRootController_) 可以在运行时切换定位库。使用这个接口时相机画面及 session 不会中断。
## 相关主题
* [适用于 Mega 的 AR Session 最佳实践](session-best-practice.html) 介绍了如何创建和配置适用于 Mega 的 AR Session
* [添加 Mega 跟踪目标](target.html) 介绍了如何添加 Mega 的跟踪目标 block 以及如何在 Unity 编辑器中加载 block 模型以辅助开发
* [添加一组帧数据源](../cameras/frame-source-group.html) 介绍了如何修改 session 的帧数据源组
* [获取 session 的运行结果](../fundamentals/session-output.html) 介绍了如何获取 session 组件的跟踪结果
* [UI 消息](../diagnostics/ui-messages.html) 介绍了如何使用 UI 消息来显示 session 状态