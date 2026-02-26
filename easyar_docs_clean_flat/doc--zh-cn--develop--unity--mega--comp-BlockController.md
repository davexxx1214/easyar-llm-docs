---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockController.html
original_file: doc--zh-cn--develop--unity--mega--comp-BlockController.md
normalized_at: 2026-02-27
---
# BlockController 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockController.html)
>
探索 BlockController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockController.png)
默认条件下组件截图。
|属性|描述|
|**Active Control**|选项：
* Hide Before First Found（默认）：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活。
* Hide When Not Tracking：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用。
* None：不控制 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的激活与否。|
|**ID**|Block ID。
只读。|
