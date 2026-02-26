---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/playback.html
---

在 Unity 中使用 EIF 文件模拟运行 | EasyAR 文档
**
##### Table of Contents
**
# 在 Unity 中使用 EIF 文件模拟运行
本文介绍了如何在 Unity 中使用 EIF 文件进行模拟运行，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
## 开始之前
模拟运行使用 EIF 文件作为输入，因此在开始之前需要先录制 EIF 文件：
* 参考 [录制 EIF 文件](recording.html) 录制 EIF 文件
另外还需要了解：
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 通过 [访问 session 中的 AR 功能组件](../fundamentals/session-components.html) 了解如何访问录制组件
## 启用 session 的 frame player
[ARSession.AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 提供了多种方式来配置 session 组件的组合方式，其中一种方式是设置 [AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource) 为 [FramePlayer](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_FramePlayer) 来启用 frame player 组件，从而可用使用 EIF 文件进行模拟运行。
例如：
```
`Session.AssembleOptions.FrameSource = AssembleOptions.FrameSourceSelection.FramePlayer;
`
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Assemble Options` 中对应的选项：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-assemble.png)
这样 session 启动时就会启用 frame player 组件，而不会选择其它 frame source 组件。
使用 frame player 播放 EIF 文件的效果如下面这个视频所示：
>
> 这段视频展示了使用 frame player 在电脑上运动稠密空间建图的效果。视频左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
在播放 EIF 文件的过程中，session 中的各个 AR 功能组件都可以正常工作，场景中的内容和交互逻辑也可以正常工作，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
##### 提示
在电脑上使用 frame player 播放 EIF 看到的效果，与录制 EIF 文件时手机上的效果是基本一致的。
##### 重要事项
场景内播放 EIF 时的运行效果与录制时使用的设备以及设备上当时选用的 frame source 有关，因此在录制 EIF 文件时，建议使用和目标设备相同或接近的设备进行录制，从而保证播放时的效果与目标设备上的效果一致。同时需要重点关注录制场景中的运动跟踪功能是否启用，如果录制时未启用运动跟踪功能，那么播放时也无法启用运动跟踪功能，依赖运动跟踪的 AR 功能（比如稠密空间地图、Mega等）也无法和设备上工作一致。
## 在 session 启动时播放
默认情况下，session 启动时 frame player 会自动开始播放 EIF 文件，但是在播放前需要指定 EIF 文件路径，可以通过 [FramePlayer.FilePathType](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_FilePathType) 和 [FramePlayer.FilePath](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_FilePath) 属性来设置。
例如：
```
`var player = Session.GetComponent&lt;FramePlayer&gt;();
player.FilePathType = WritablePathType.Absolute;
player.FilePath = path;
`
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Frame Player` 组件中的对应选项：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-file.png)
如果未指定文件，或文件路径无效，session 启动时 frame player 会启动失败，并输出错误日志：
>
> File not found:
>
## 手动播放
如果要手动控制播放时机，可以在 session 启动前将 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 设为 `false`，
```
`Session.GetComponent&lt;FramePlayer&gt;().enabled = false;
`
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中取消 `Frame Player` 组件的 `Enabled` 勾选：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-auto-disable.png)
在需要播放时，使用 [Play()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Play) 来启动播放。
例如：
```
`if (Session.Assembly.FrameSource is FramePlayer player)
{
player.Play();
}
`
```
每次调用 [Play()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Play) 都会停止前一次播放后（如果之前播放过）从头开始播放。
##### 小心
播放新数据时，场景中原本的数据不会被清空。AR 组件的状态也不会被重置，它们会表现得像是摄像头数据突然从上一个数据停止的地方跳到新数据开始的地方一样。
虽然这对一部分功能没太大影响，但是对于依赖运动跟踪的功能（比如稠密空间地图、Mega等）来说，可能会导致功能状态异常，从而影响运行效果。因此建议在播放新数据前，重新启动 session 来重置所有 AR 组件的状态。
## 暂停和继续
使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 来控制播放的暂停和继续。
例如，设置 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `false` 来暂停播放：
```
`player.enabled = false;
`
```
播放暂停后，所有 AR 功能组件都会暂停工作。场景中的内容和交互逻辑不一定会停止，与内容本身有关。继续播放后，AR 功能组件会从暂停的位置继续工作。
## 停止播放
使用 [Stop()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Stop) 来停止播放。
```
`player.Stop();
`
```
播放停止后，所有 AR 功能组件都会停止工作。场景中的内容和交互逻辑不一定会停止，与内容本身有关。
## 跳转到指定时间点播放（seek）
使用 [Seek(double)](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Seek_System_Double_) 来跳转到指定时间点播放。
例如，跳转到 5 秒后播放：
```
`player.Seek(player.Time + 5);
`
```
##### 注意
跳转之后可能不是从精确的时间点开始播放，具体取决于 EIF 文件的编码方式和关键帧间隔。
并不是所有 EIF 文件都支持跳转播放，可以使用 [IsSeekable](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_IsSeekable) 属性来检查当前播放的 EIF 文件是否支持跳转播放。
##### 注意
只有使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制且正常调用停止录制的 EIF 文件才支持跳转播放。如果 EIF 文件不支持跳转播放，调用 [Seek(double)](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Seek_System_Double_) 不会有任何效果。
## 播放速度控制
使用 [Speed](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Speed) 属性来控制播放速度。
例如，设置播放速度在原来的基础上增加 0.1 倍：
```
`player.Speed += 0.1;
`
```
并不是所有 EIF 文件都支持播放速度控制，可以使用 [IsSpeedChangeable](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_IsSpeedChangeable) 属性来检查当前播放的 EIF 文件是否支持播放速度控制。
##### 注意
只有使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制且正常调用停止录制的 EIF 文件才支持播放速度控制。如果 EIF 文件不支持播放速度控制，设置 [Speed](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Speed) 不会有任何效果。
## 相关主题
* 尝试 [使用 session 验证工具](tool.html)，这个工具包含了一个简单的 EIF 播放器，可以更加快速地使用 EIF 文件进行模拟运行