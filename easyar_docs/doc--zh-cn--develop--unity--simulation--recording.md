---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/recording.html
original_file: doc--zh-cn--develop--unity--simulation--recording.md
normalized_at: 2026-02-27
---
# 在 Unity 中录制 EIF 文件
本文介绍了如何在 Unity 中录制 EIF 文件，以便用于模拟运行。
## 开始之前
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 通过 [访问 session 中的 AR 功能组件](../fundamentals/session-components.html) 了解如何访问录制组件
## 启动录制
使用 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `true` 来启动录制，例如：
```
if (Session.State >= ARSession.SessionState.Ready && Session.Assembly.FrameRecorder.OnSome)
{
var frameRecorder = Session.Assembly.FrameRecorder.Value;
frameRecorder.enabled = true;
}
```
需要注意的是，这里需要先判断 [ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 是否存在。
> **注意**
[ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 在少数情况下，比如使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html) 时是不能使用的。
[FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 默认值为 `false`，表示录制处于关闭状态，即使在编辑器中手动配置也是无效的。
录制在 session 运行过程中，[FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) >= [FrameRecorder.RecorderStatus.Ready](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Ready) 时才会开始。
如果 [FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) < [FrameRecorder.RecorderStatus.Ready](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Ready)，可以使用 [OnReady](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnReady) 事件来等待录制准备就绪。
```
Session.GetComponent<FrameRecorder>().OnReady.AddListener(() => {
// 可以开始录制
});
```
可以使用 [OnRecording](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnRecording) 事件来确认启动成功：
```
frameRecorder.OnRecording.AddListener((file) =>
{
Debug.Log($"Recording started: {file}");
});
```
启动失败没有事件触发，但可以通过检查 [FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) 是否为 [Error](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Error) 来确认。
> **重要事项**
场景内播放 EIF 时的运行效果与录制时使用的设备以及设备上当时选用的 frame source 有关，因此在录制 EIF 文件时，建议使用和目标设备相同或接近的设备进行录制，从而保证播放时的效果与目标设备上的效果一致。同时需要重点关注录制场景中的运动跟踪功能是否启用，如果录制时未启用运动跟踪功能，那么播放时也无法启用运动跟踪功能，依赖运动跟踪的 AR 功能（比如稠密空间地图、Mega等）也无法和设备上工作一致。
## 停止录制
使用 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `false` 来停止录制，例如：
```
frameRecorder.enabled = false;
```
该操作会立即停止录制，并阻塞直至文件写入完成。
> **重要事项**
必须调用停止录制，否则录制文件写入不完整，会导致部分功能或整个文件无法使用：
* 录制格式为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 时，EIF 文件无法跳转到指定的时间点进行播放（seek），只能从头播放
* 录制格式为 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 时，EIF 文件无法使用
## 文件存储和导出
可以使用 [OnRecording](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnRecording) 事件来获取录制文件的完整真实路径：
```
frameRecorder.OnRecording.AddListener((file) =>
{
Debug.Log($"Recording started: {file}");
});
```
默认配置下，录制文件会存储在应用的持久化数据路径下，可以通过 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) 来访问该路径。
可以通过 [FrameRecorder.Configuration](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Configuration).[FilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_FilePath) 来修改录制文件的存储路径。该路径必须在录制启动前设置，且需要关闭 [AutoFilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_AutoFilePath) 后才能生效。需要提前创建好目录。
> **重要事项**
必须保证录制文件的存储目录存在且应用可写入，否则录制启动时会失败。
例如，下面的代码展示了如何将录制文件存储在自定义目录下，并根据 session 使用的 FrameSource 类型和当前时间生成文件名：
```
if (!Directory.Exists(SavePath))
{
Directory.CreateDirectory(SavePath);
}
var frameRecorder = Session.Assembly.FrameRecorder.Value;
frameRecorder.Configuration.AutoFilePath = false;
frameRecorder.Configuration.FilePath.Type = WritablePathType.Absolute;
frameRecorder.Configuration.FilePath.FolderPath = SavePath;
frameRecorder.Configuration.FilePath.FileName = ARSessionFactory.DefaultName(Session.Assembly.FrameSource.GetType()).Replace(" ", "") + DateTime.Now.ToString("\_yyyy-MM-dd\_HH-mm-ss.fff");
frameRecorder.enabled = true;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中取消 Frame Recorder 的 `Auto File Path` 勾选之后配置：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-filepath.png)
> **提示**
通过 [FrameRecorder.RecordingConfiguration.FilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_FilePath) 可以修改文件的存储目录和文件名（不含扩展名），文件扩展名会根据录制格式自动添加。
* 录制格式为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 时，文件扩展名为 `.mkveif`
* 录制格式为 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 时，文件扩展名为 `.eif`
如果文件存储在应用的持久化数据路径或其他应用私有路径下，可以通过以下方式将文件导出到电脑上：
* Android 平台可以通过 USB 连接电脑后，使用 `adb pull` 或其他方式将文件导出到电脑上，文件通常在 `/sdcarad/Android/data/<app package name>/files` 下面。
* iOS 平台可以通过 Xcode 的 Devices 窗口将文件导出到电脑上，或者通过 iTunes 或 Finder 文件共享访问应用的私有目录。
* 通过代码将文件存储到公共目录下，比如 Android 的下载目录或 iOS 的相册等。
> **注意**
对于 iOS 应用，如果希望通过 iTunes 或 Finder 文件共享访问应用的私有目录，在打包前需要在 XCode 项目的 `Info.plist` 中添加 `UIFileSharingEnabled` 键，并将值设置为 `YES`：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/ios-plist-uifilesharingenabled.png)
添加之后显示的文字与添加的字符串不同，这是正常的。
## 更换录制格式
通过 [FrameRecorder.Configuration](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Configuration).[Format](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_Format) 改变录制格式，必须在录制启动前设置。
例如，下面的代码展示了如何将录制格式强制设置为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264)：
```
frameRecorder.Configuration.Format = FrameRecorder.InternalFormat.H264;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Format`：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-format.png)
> **注意**
[H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 在部分设备（比如 Windows）上无法使用，一般推荐使用 [Auto](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Auto)，这样会根据设备自动选择合适的格式。
> **注意**
在 XREAL 上，使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制数据无法用来模拟运行，用于且只用于反馈问题。
* 模拟运行时，应使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制数据。
* 反馈问题时，应使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制数据。
可以使用 [RecordingFormat](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_RecordingFormat) 来查看当前录制格式。
## 在 session 启动时自动录制
在 session 启动前设置 [AutoStart](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_AutoStart) 为 `true`，可以在 session 启动时启动录制，例如：
```
frameRecorder.AutoStart = true;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中勾选 Frame Recorder 的 `Auto Start`：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-autostart.png)
> **注意**
编辑器上修改 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 是无效的。
## Mega 可用的数据
在使用 Mega 时，对 EIF 及相关文件内容有一些特殊要求，在老版本的 Unity 插件中未集成相关功能，那些版本录制的数据不能用于 Mega。
以下这些情况录制的数据可以用于 Mega：
* 使用 Unity 插件 4000 或更高版本录制的数据
* 使用 Mega Toolbox 录制的数据
* 如果数据是使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制的，比如文件 `x.eif`，需要在文件相同目录同时存在 `x.eif.json` 文件才能使用
以下这些情况录制的数据不能用于 Mega：
* 使用 Unity 插件 4.6 或更低版本录制的数据
* 使用原生 EasyAR Sense，且未添加与 Unity 插件中相同内容的数据
另外，虽然 Mega 可以不使用运动跟踪进行工作，但运行效果是不一样的。建议在录制 EIF 文件时启用运动跟踪功能，从而保证播放时的效果能符合大部分使用场景。
## 后续步骤
* 尝试 [使用 EIF 文件模拟运行](playback.html)
* 尝试 [使用 session 验证工具](tool.html)
