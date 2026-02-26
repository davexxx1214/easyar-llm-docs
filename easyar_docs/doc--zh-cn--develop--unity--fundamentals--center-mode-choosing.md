---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/center-mode-choosing.html
---

选择合适的中心模式 | EasyAR 文档
**
##### Table of Contents
**
# 选择合适的中心模式
选择合适的中心模式对于内容制作来说至关重要。通过以下内容，您将了解如何获取和修改中心模式，以及选择合适中心模式的建议。
## 开始之前
* 通过 [AR Session 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [AR Session 的中心模式](center-mode.html) 了解中心模式的基本概念及其对场景中物体运动行为的影响。
## 获取可用中心模式
在 session 运行时，只有当前 session 可用的中心模式会显示在 Inspector 面板的 `Center` 下拉菜单中。如果 session 未启动，则所有中心模式均会显示。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-available.png)
这张图中显示了在编辑器中使用 CameraDeviceFrameSource 时的 session 可用的中心模式。
在脚本中，可以在 session 成功组装后通过 [ARSession.AvailableCenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AvailableCenterMode) 属性来获取当前 session 中可用的中心模式列表。
比如，下面的代码展示了如何判断某个中心模式是否在当前 session 中可用：
```
`if (Session.AvailableCenterMode.Contains(mode))
{
// mode 在当前 session 中可用
}
`
```
## 修改中心模式
打开 Inspector 面板，在 `Center` 下拉菜单中选择需要的中心模式。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-change.png)
在脚本中，可以通过 [ARSession.CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 属性来修改中心模式。
比如，下面的代码展示了如何在可用的中心模式之间循环切换：
```
`while (true)
{
Session.CenterMode = (ARSession.ARCenterMode)(((int)Session.CenterMode + 1) % Enum.GetValues(typeof(ARSession.ARCenterMode)).Length);
if (Session.AvailableCenterMode.Contains(Session.CenterMode)) { break; }
}
`
```
session 每帧更新时会判断当前中心模式是否有效，如果有效，session 会立即尝试使用新的中心模式。
>
> 在上面这个视频中，session 一开始使用
[> FirstTarget
](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget)> 模式，中心物体是圣诞树（亮蓝色点云）。随后我们手动将中心模式修改为
[> Camera
](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera)> 模式，中心物体变为摄像机（蓝色锥体）。视频内容的详细描述请参考
[> AR Session 的中心模式
](center-mode.html)> 。
>
session 更新时，如果修改后的中心模式在当前 session 中无效，[CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 属性会被自动修改为第一个可用的中心模式（通常是 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)），并在日志中输出一行警告信息：
```
`Center mode {Value} is unavailable in this session, reset to {NewValue}.
`
```
## 如何选择中心模式
与现实世界中的物体进行对齐是 AR 内容制作的核心需求，而中心模式决定了 session 以哪个物体作为参考点来计算场景中其它物体的位置和朝向。因此，选择合适的中心模式对于内容制作来说至关重要。
### 通用建议
很多时候使用 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 模式，以 `target` 作为中心对内容制作是更友好的，这样放在 `target` 下的内容参考点可以保持静止不动，不会因为 `XR Origin` 或 `camera` 的移动而产生不必要的影响（比如影响物理系统计算）。不过这并不绝对，具体来说：
* 在不知道怎么选择时，使用默认值，即 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 中心
由于绝大部分 AR 功能都是有误差的，而且运行中会不断修正这个误差，这就会导致看似在现实世界中相对不动的物体（比如稀疏空间地图的 `target` 和 运动跟踪的 `XR Origin`）实际在虚拟空间中是会有相对运动的，这时采用 `target` 作为中心就要比采用 `XR Origin` 要更符合内容制作的需要。
* 多个 `target` 同时被跟踪的情况
对于多个 `target` 同时被跟踪的情况，同样由于及计算误差，即使现实世界中的物体相对是静止的，这些 `target` 之间也可能存在相对运动。如何选择中心的物体则需要根据实际需要进行判断，通常 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 模式是更合适的选择。
* 什么时候使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式
[SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 适用于只有运动跟踪在运行的场景，这时 `XR Origin` 是唯一的参考点。它还适用于一些特殊情况，如果头显厂商没有正确实现运动跟踪的参考点，这时就必须使用 Unity 的世界中心从而强制使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式。
* [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式的使用场景
[Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式则更适用于物理相机不动的场景（比如使用固定摄像头的卡片对战类 AR），这时采用 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式会更便于内容创作。
### 不同 AR 功能的常用中心模式
在单独使用部分 AR 功能时，某些中心模式会更常用一些。下面的表格列出了这些 AR 功能对应的常用中心模式：
|功能|常用中心模式|
|Mega|FirstTarget 或 SpecificTarget|
|运动跟踪|SessionOrigin|
|平面检测|SessionOrigin|
|稀疏空间地图|FirstTarget 或 SpecificTarget|
|稠密空间地图|SessionOrigin|
|表面跟踪|FirstTarget 或 SpecificTarget|
|图像跟踪|FirstTarget、SpecificTarget 或 Camera|
|图像云识别|FirstTarget、SpecificTarget 或 Camera|
|物体跟踪|FirstTarget、SpecificTarget 或 Camera|
### 跨设备需要考虑的问题
在开发跨设备的 AR 应用时，需要考虑不同设备对中心模式的支持情况。
* 如果仅涉及手机和平板，通常不会有太大问题，如果需要使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)，要确保运动跟踪可以运行。
* 如果需要使用头显，则需要格外注意
* 查阅 [有效中心模式](center-mode.html#available-center-mode) 确定将要使用的设备都支持哪些中心模式。如果在使用第三方扩展，注意查看这些扩展使用的 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType)。
* 使用 Rokid 设备时，尽量不要使用 UXR。使用 XRI 可以确保大多数中心模式可用。
* 在不支持 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 和 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 模式的头显上，需要注意使用 Mega 或图像跟踪等绝大部分功能内容都是做不到相对 Unity 世界坐标系静止的。
## 每个中心模式都能正确显示的内容
##### 警告
在 Unity AR 中，任何存在于 Unity 世界坐标系下且未根据 session 组件调整 transform 的物体都可能无法正确显示。
如果世界坐标系下放置了一些模型，那这些模型的位置和朝向可能与现实世界中任何物体都没有对应关系，实际运行效果可能碰巧正常，也可能看上去像是浮在空中或者到处乱动。
要保证内容在任何中心模式下都能正确显示，正确的做法是：
* 始终把要显示的内容放在对应的 `target` 节点下，或者放在 `XR Origin` 节点下（如果内容需要跟随 XR Origin 运动）
* 或者通过手动方式对齐内容和 `target` 或 `XR Origin` 的位置和朝向，但需要在 [ARSession.PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件后操作
##### 注意
这么做并不能保证所有内容元素都工作正常，因为 Unity 的某些功能只能在世界坐标系下工作（比如物理系统），选择合适的中心模式仍然是重要的。
## 相关主题
* [获取 session 的运行结果](session-output.html)