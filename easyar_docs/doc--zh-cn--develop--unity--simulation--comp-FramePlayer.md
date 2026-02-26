---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/comp-FramePlayer.html
original_file: doc--zh-cn--develop--unity--simulation--comp-FramePlayer.md
normalized_at: 2026-02-27
---
# FramePlayer 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.FramePlayer.html)
>
探索 FramePlayer 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/comp-FramePlayer.png)
默认条件下组件截图。
|属性|描述|
|**File Path Type**|路径类型。选项：
* Absolute：绝对路径。
* PersistentDataPath：Unity 沙盒路径 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|**File Path**|文件路径。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|
