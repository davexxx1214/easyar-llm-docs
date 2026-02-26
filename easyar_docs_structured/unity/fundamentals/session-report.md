---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-report.html
original_file: doc--zh-cn--develop--unity--fundamentals--session-report.md
normalized_at: 2026-02-27
---
# 设备支持和 session 报告
由于设备硬件和性能差异，AR 功能很多时候并不能在所有设备上运行。所以在使用 AR 功能时准确判断当前设备的支持情况是非常重要的。本文介绍了在 Unity 中，设备可用性是如何表达的，以及如何通过 session 报告（[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report)）获取设备支持和 session 可用性的信息。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
## 设备支持、session 可用性与组装
每个 AR 功能可以支持的设备是不同的。比如运动跟踪对硬件元器件有一定要求且通常需要对设备进行标定，而图像跟踪功能则可以在几乎所有摄像头可用的设备上运行。所以判断一个 AR 应用是否可以在某个设备上运行，通常需要知道当前使用哪些 AR 功能，或者换个说法就是判断某个 session 是否可以在设备上运行。
在 Unity 中，上述判断过程是在 session 组装（[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble)）阶段完成的。组装过程会根据 session 中包含的组件和当前设备的支持情况，决定 session 启动前的最终状态。
如果组装成功，session 会进入 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态，并可以继续启动和运行；如果组装失败，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，并且可以通过 session 报告（[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report)）查询具体的失败原因。
## session 报告
[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 属性提供了 session 的运行报告，一份 session 报告包含以下字段：
|属性|描述|
|Availability|完整的可用性报告|
|BrokenReason|session 损坏原因，当 session 状态为 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 时有效|
|Exception|session 损坏具体异常，当 session 状态为 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 时有效|
在 session 报告中，可以通过 [Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 查询每个组件的可用性，或是通过 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 在 session 损坏时查询损坏的详细原因。
### 一份 session 报告示例
比如，在 Windows 上，如果 session 中包含 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html)、[CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 以及若干个其它 frame source 组件，那么组装过程会检查每个组件的可用性，并生成如下报告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-report-success.png)
可以看到图中虽然 [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html) 组件的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 是 [Unavailable](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Unavailable)，但是由于 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 和 [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 都是是 [Available](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Available)，所以整个 session 的组装是成功的，且 session 成功进入了 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态。
如果我们把 [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 从 session 中移除，那么组装过程会生成如下报告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-report-fail.png)
可以看到 [FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 列表数目从 9 变成了 8，并且虽然 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 组件的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 仍然是 [Available](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Available)，但是由于没有可用的 frame source 组件，所以整个 session 的组装失败，session 进入了 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态。此时报告中 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 字段数值是 [NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource)，表示没有可用的 frame source。
除了组装过程之外，session 运行过程中也可能出现损坏的情况，比如某个运行中的组件被意外移除等。此时同样可以通过 session 报告查询具体的损坏原因。
### 报告更新
session 报告会在以下时间点发生变化：
* 组装第一阶段完成
这时会生成一份完整的 session 报告，包含组件可用性报告。session 报告的 [Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 部分会在这时确定并不再变化。
可以通过 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告更新。
如果组装之后直接启动了 session，也可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告更新。需要关注的 session 的状态包括： [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 和 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。
* 组装第二阶段完成
这时会生成一份新的组件可用性报告。除非 session 重启，否则 session 报告不会更新。
可以通过 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告更新。
* session 启动或运行过程中 session 损坏时
session 报告的 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 和 [Exception](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Exception) 会更新。
可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告更新。需要关注的 session 的状态包括：[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。
### 报告内容：session 损坏的原因
[BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 表示 session 损坏的原因，有以下这些情况：
|原因|描述|
|Uninitialized|组装过程，EasyAR Sense 未成功初始化|
|LicenseInvalid|组装过程，EasyAR Sense license 验证失败或不适用于当前使用|
|SessionObjectIncomplete|组装过程，session 物体不完整。比如在 URP 中未正确配置 RendererFeature|
|NoAvailabileFrameSource|组装过程，无可用的 frame source。比如所有 frame source 都不可用或未添加任何 frame source。在且仅在默认 session 配置下，这种情况说明设备当前选择的 AR 功能的支持|
|FrameSourceIncomplete|组装过程，frame source 不完整。一般多出现在自定义 frame source 时未正确实现 frame source 接口|
|FrameFilterNotAvailabile|组装过程，存在不可用的 frame filter。这种情况只存在于部分组装选项下。|
|StartFailed|启动失败。比如启动过程中出现异常|
|RunningFailed|运行失败。比如运行中的组件被意外移除，或是 URP 中未正确配置 RendererFeature 等。|
### 报告内容：可用性信息
[Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 提供了 session 中每个组件的可用性信息。它包含以下字段：
|字段|描述|
|FrameFilters|组装过程检查过的 frame filter 可用性列表|
|FrameSources|组装过程检查过的 frame source 可用性列表|
|PendingDeviceList|未完成的设备列表下载任务|
|DeviceList|设备列表下载结果|
其中 [PendingDeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_PendingDeviceList) 和 [DeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_DeviceList) 字段用于表示设备支持列表的下载状态。组装第一阶段完成时，当且仅当 [PendingDeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_PendingDeviceList) 非空时，组装会进入第二阶段，可以使用这个条件来判断 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 是否会第二次执行。
## 后续步骤
* 尝试 [判断可用性和设备支持](session-assemble.html)
