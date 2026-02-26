---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/comp-FrameRecorder.html
---

FrameRecorder 组件参考 | EasyAR 文档
**
##### Table of Contents
**
# FrameRecorder 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.FrameRecorder.html)
>
探索 FrameRecorder 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/comp-FrameRecorder.png)
默认条件下组件截图。
|属性|描述|
|**Auto Start**|session 启动后自动启动录制。|
|**Format**|录制的格式。选项：
* Auto：自动选择可用的格式。
* H264：H264。MacOS、iOS、Android上支持。
* Obsolete：原始 EIF 格式，在Windows上只支持该格式。|
|**Auto File Path**|自动生成文件路径。文件将被存储在 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|*Type*|Auto File Path 未选中时显示。
路径类型。选项：
* Absolute：绝对路径。
* PersistentDataPath：Unity 沙盒路径 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|*Folder Path*|Auto File Path 未选中时显示。
文件夹路径。|
|*File Name*|Auto File Path 未选中时显示。
文件名（不含扩展名）。|
|**Events**|可注册事件。|
|*OnReady*|可以开始录制的事件。|
|*OnRecording*|录制启动的事件。|
|*OnFinish*|录制结束的事件。|