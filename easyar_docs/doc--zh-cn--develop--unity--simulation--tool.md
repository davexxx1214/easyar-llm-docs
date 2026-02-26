---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/tool.html
---

使用 session 验证工具 | EasyAR 文档
**
##### Table of Contents
**
# 使用 session 验证工具
本文介绍了如何使用 session 验证工具，在编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
## 开始之前
模拟运行使用 EIF 文件作为输入，因此在开始之前需要先录制 EIF 文件：
* 参考 [录制 EIF 文件](recording.html) 录制 EIF 文件
另外还需要了解：
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
## session 验证工具
session 验证工具用于帮助开发者在 Unity 编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
默认情况下可以在 `AR Session (EasyAR)` 物体的 `Inspector` 窗口中看到 session 验证工具，它是 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 编辑器的一部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool.png)
点击工具右上角 `↗` 按钮可以将工具弹出为独立窗口，方便查看和操作，在窗口关闭或按下 `↘` 按钮后，工具会重新在 `Inspector` 窗口中显示。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-window.png)
工具运行时的效果如下面这个视频所示：
>
> 这段视频展示了 session 验证工具的使用效果，录制于 Unity 的 play 模式。视频上半部分左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图，视频下半部分是 session 验证工具。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
> 工具左边偏上部分展示了 EIF 播放的进度条，可以看到它在随着播放进度不断变化。工具左边偏下部分展示了当前 session 的状态。工具右边展示了 session 的组件和可用中心模式。
>
> 在场景中，可以看到同时工作的 3 个 AR 功能：
>
>
* > 运动跟踪：它是由 frame player 提供的，蓝色球体是 XR Origin，蓝色锥体代表用户位置。
>
* > 稠密空间建图：可用看到随着视角的移动，半透明的网格模型在不断生成。
>
* > 稀疏空间跟踪：视频中在被跟踪的是一棵圣诞树，叠加的虚拟物体是浅蓝色点云。
>
>
## 启动工具
点击工具顶部的 `▶` 按钮即可启动工具。按下这个按钮的效果与直接按下 [Unity 工具栏](https://docs.unity3d.com/Manual/Toolbar.html) 的 `▶` 按钮是一样的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-run.png)
如果工具已经启动，则按钮会变为 `■`，点击即可停止工具。
当工具以独立窗口展示时，`▶` 按钮右边的选择框可以选择工具使用的 session 物体，如果窗口被重置导致 session 丢失，可以从这里重新选择。
## 控制 EIF 播放
要使用工具的 EIF 播放功能，需要在运行前勾选工具的 `Frame Player` 选项，这时工具会托管 session 组装过程中 frame source 的选择，无论 [AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource) 设置为何种值，都会启用 frame player 组件。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-player-enable.png)
因此，运行时会有弹窗提示，说明当前 session 所使用的 frame source 已被工具托管：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-notice.png)
##### 注意
工具只会在 Unity 编辑器上托管组装过程中 frame source 的选择，在应用打包运行时该选项没有任何影响。
正常运行时，EIF 播放控制功能会显示在工具的上方图中框出的部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-player.png)
可以通过这些按钮控制 EIF 文件的播放：
* `▶`：播放，从暂停或停止状态恢复播放
* `▮▮`：暂停
* `■`：停止
* `▮◀`：跳到 5 秒之前（文件支持时）
* `◀◀`：降低播放速度（文件支持时）
* `▶▶`：提高播放速度（文件支持时）
* `▶▮`：跳到 5 秒之后（文件支持时）
* `▲`：打开文件
* 进度条：点击可以跳转播放位置（文件支持时）
可以在播放的同时调整优化场景中的内容和交互逻辑，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
##### 注意
播放新数据和跳转播放时，场景中原本的数据不会被清空。AR 组件的状态也不会被重置，它们会表现得像是摄像头数据突然从上一帧数据跳到新数据一样。
虽然这对一部分功能没太大影响，但是对于依赖运动跟踪的功能（比如稠密空间地图、Mega等）来说，可能会导致功能状态异常，从而影响运行效果。
## 控制 session 工作流
使用工具的 session 工作流控制功能，需要在运行前勾选工具的 `Session Workflow` 选项，该选项是默认勾选的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-enable.png)
正常运行时，session 工作流控制功能会显示在工具的播放控制下方图中框出的部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-workflow.png)
在整块区域的上方，展示了 [EasyARController.IsReady](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_IsReady) 和 [ARSession.State](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_State) 两个状态信息。
在整块区域的下方，提供了这些按钮来控制 session 的工作流：
* `Initialize`：初始化 session，可以选择使用 `Project Settings` 中配置的 license key 或手动输入 license key
* `Assemble`：组装但不启动 session
* `StartSession (Assembled)`：启动已组装的 session
* `StartSession`： 组装并启动 session
* `StopSession`：停止 session
* `StopSession (keep image)`：停止 session，但保留图像背景
* `Deinitialize`：反初始化 session
##### 注意
由于这些控制功能直接调用了 [ARSession](../../../api/unity/easyar.ARSession.html) 和 [EasyARController](../../../api/unity/easyar.EasyARController.html) 的相关方法，因此可以通过这些按钮来验证 session 状态变化对内容的影响，但同时需要注意如果在应用脚本中也调用了类似方法，应用的运行流程可能超出应用本身的预期。
## 控制 session 组件
使用工具的 session 组件控制功能，需要在运行前勾选工具的 `Session Workflow` 选项，该选项是默认勾选的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-enable.png)
正常运行时，session 组件控制会显示在工具的下方或右方图中框出的部分，具体位置视窗体宽度而变：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-assembly.png)
这块区域显示的内容与具体的 session 有关，比如上图使用的 session 中包含了图像跟踪、稠密空间建图和稀疏空间跟踪三种功能组件，因此工具中显示了这三种功能的控制选框。
一般来说，这块区域会显示 session 中所有可用的 AR 功能组件，并提供这些组件的启用/禁用（[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html)）控制，包括：
* AR Session：控制 session 本身的启用/禁用
* Image Renderer：控制物理相机图像渲染的启用/禁用
* Camera：控制虚拟摄像机的启用/禁用
* Frame Source：控制 frame source 的启用/禁用，只有未启用 frame player 时才可控制，启用 frame player 时，功能控制由 EIF 播放控制部分替代
* Frame Filter：控制具体 AR 功能的启用/禁用
* Frame Recorder：控制录制 EIF 组件的启用/禁用，只有未启用 frame player 时才可见，启用 frame player 时，该组件不会被组装进 session
同时区域内还会显示 session 可用的中心模式和 [session 报告](../fundamentals/session-report.html)。
##### 注意
工具中展示的可用中心模式和 session 报告是编辑器下运行的结果，实际设备上运行时会不同。
## 相关主题
* 尝试 [使用 EIF 文件模拟运行](tool.html)，通过脚本控制 EIF 文件的播放
* 尝试在脚本中 [控制 session 执行](../fundamentals/session-ctrl.html)
* 尝试在脚本中 [访问 AR 功能组件](../fundamentals/session-components.html)
* 尝试在脚本中 [获取 session 的运行结果](../fundamentals/session-output.html)
* 尝试在脚本中 [初始化](../fundamentals/initialization.html)
* 尝试在脚本中 [获取 session 报告并判断设备支持](../fundamentals/session-assemble.html)