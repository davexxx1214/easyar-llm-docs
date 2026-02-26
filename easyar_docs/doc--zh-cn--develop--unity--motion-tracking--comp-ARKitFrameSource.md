---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-ARKitFrameSource.html
---

ARKitFrameSource 组件参考 | EasyAR 文档
**
##### Table of Contents
**
# ARKitFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ARKitFrameSource.html)
>
探索 ARKitFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-ARKitFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Desired Frame Rate**|期望的相机图像帧率。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|