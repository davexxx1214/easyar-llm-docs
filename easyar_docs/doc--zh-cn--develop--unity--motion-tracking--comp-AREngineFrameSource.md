---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-AREngineFrameSource.html
---

AREngineFrameSource 组件参考 | EasyAR 文档
**
##### Table of Contents
**
# AREngineFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.AREngineFrameSource.html)
>
探索 AREngineFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-AREngineFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|