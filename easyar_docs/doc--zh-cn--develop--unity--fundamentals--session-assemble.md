---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-assemble.html
original_file: doc--zh-cn--develop--unity--fundamentals--session-assemble.md
normalized_at: 2026-02-27
---
# 判断 session 可用性和设备支持
在启动 AR 之前，通常需要先判断 session 是否可用以及当前设备是否支持所需的 AR 功能。本文介绍了如何进行这些检查。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 通过 [设备支持和报告](session-report.html) 了解 Unity 中设备支持和 session 报告的基础知识
* 了解如何 [创建 session](session-creation.html)
## 在启动流程中获取报告
如果组装之后直接启动了 session，可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告。
需要在 session start 之前订阅 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件，通常在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 中完成订阅是安全的：
```
void Awake()
{
Session.StateChanged += HandleSessionStateChange;
}
```
在事件处理中需要关注的 session 的状态包括：[Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 和 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。[Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态说明 session 已经成功启动，也即说明 session 在当前设备上可用。[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态说明 session 启动失败，也即说明 session 在当前设备上不可用。
[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并不总是在设备不受支持的时候出现。所以还需要使用 [SessionReport.BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 获取具体的失败原因。
```
void HandleSessionStateChange(ARSession.SessionState status)
{
if (status == ARSession.SessionState.Ready)
{
// session 在当前设备上可用
}
else if (status == ARSession.SessionState.Broken)
{
// session 在当前设备上不可用
if (Session.Report.BrokenReason == SessionReport.SessionBrokenReason.NoAvailabileFrameSource ||
Session.Report.BrokenReason == SessionReport.SessionBrokenReason.FrameFilterNotAvailabile)
{
// 所选组件不受当前设备支持
}
else
{
// 设备无关的原因
}
}
}
```
出现 [SessionReport.SessionBrokenReason.NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource) 和 [SessionReport.SessionBrokenReason.FrameFilterNotAvailabile](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_FrameFilterNotAvailabile) 这两种原因，说明 session 组件在当前设备上不可用；而其它原因通常是设备无关的。严格来说，出现这两种原因意味着当前配置（且仅该配置）下的 AR 功能无法在该设备上运行。配置指 session 物体中选择的功能和设置。可以从 [Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 中获得详细的可用性报告。
对于 [SessionReport.SessionBrokenReason.NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource) 的情况，如果在启动 session 时联网更新设备列表时发现设备已被支持，session 有可能自动恢复。
## 在启动前获取报告
如果希望在 session 启动前做出判断，并根据具体情况决定是否启动 session，可以手动调用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 并使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告。
需要在 session assemble 之前订阅 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件，
```
Session.AssembleUpdate += OnAssembleUpdate;
```
在组装第一阶段，仍然可用利用 [ARSession.SessionState](../../../api/unity/easyar.ARSession.SessionState.html) 和 [Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 来判断 session 受支持的情况。但是第二阶段的报告不会更新到 session 中。
因此一般手动调用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 时，需要在 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件中处理组件可用性报告，从而判断 session 在当前设备上是否可用。
需要重点关注 [SessionReport.AvailabilityReport.FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 列表中组件的可用性。如果有任何一个 frame source 组件是可用的，那么 [SessionReport.AvailabilityReport.FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 部分在当前设备上就是可用的。
同时还需要关注报告中的 [SessionReport.AvailabilityReport.FrameFilters](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameFilters) 列表中组件的可用性。但是判断标准根据组装选项不同，会要求所有 frame filter 可用，或是任意数量的 frame filter 可用。默认选项下，要求所有 frame filter 可用。
在默认配置下，可以使用如下代码判断 session 组件在当前设备上是否可用：
```
void OnAssembleUpdate(SessionReport.AvailabilityReport report)
{
if (report.FrameSources.Any(f => f.Availability == SessionReport.AvailabilityReport.AvailabilityStatus.Available) &&
report.FrameFilters.All(f => f.Availability == SessionReport.AvailabilityReport.AvailabilityStatus.Available))
{
Session.AssembleUpdate -= OnAssembleUpdate;
// session 组件在当前设备上可用，可以启动 session
Session.StartSession();
}
else
{
// session 组件在当前设备上不可用
}
if (report.PendingDeviceList.Count <= 0)
{
Session.AssembleUpdate -= OnAssembleUpdate;
}
}
```
注意 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件可能会触发两次。上面的代码示例中，会在确认组件可用后取消订阅事件。
这种判断方法没法判断 session 启动过程中可能出现的其它错误，但这些错误通常是设备无关的，如有需要可以在启动 session 后通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件进行补充判断。
## session 组件不可用时的选择
在应用开发中，一般都希望对尽量多的设备提供兼容支持。因此当 session 组件在当前设备上不可用时，可以考虑以下几种选择：
* 降级使用其它 AR 功能
通过修改 session 组件配置，选择当前设备支持的 AR 功能。可以参考 [创建 session](session-creation.html) 了解如何修改 session 组件配置。
* 提供非 AR 体验
在 session 组件不可用时，提供一个非 AR 的体验。比如在导航场景下，如果 AR 导航无法实现，提供传统2D导航是非常有用的。
* 提示用户更换设备
在某些应用场景下，用户可能会使用不支持 AR 功能的设备。此时可以提示用户更换设备以获得更好的体验。
在选择这些方案时，可以结合应用的具体需求和用户群体进行权衡。在 AR 应用中，如果部分设备确实无法提供 AR 或降级方案，仍然需要提供一个良好的用户提示信息，以便让用户了解当前设备的限制。
## 后续步骤
* 了解 [控制 session 执行](session-ctrl.html) 的方法
* 了解 [帧数据源及运行时选取](../cameras/frame-source.html)
* 另外，您还可以通过下面这些示例来了解获取报告之后的应用场景：
* [Workflow\_ARSession 示例](sample-arsession.html) 使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示，同时还使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件在 UI 上展示了每个组件的可用性
* SpatialMap\_Sparse\_AllInOne 示例使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件对设备支持进行了提前判断和不可用提示
* MotionTracking\_DeviceMotionAndPlaneDetection 示例使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示
* MegaBlock\_Basic 示例使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示
