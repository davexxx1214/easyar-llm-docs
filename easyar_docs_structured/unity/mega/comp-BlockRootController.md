---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockRootController.html
original_file: doc--zh-cn--develop--unity--mega--comp-BlockRootController.md
normalized_at: 2026-02-27
---
# BlockRootController 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockRootController.html)
>
探索 BlockRootController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockRootController.png)
默认条件下组件截图。
|属性|描述|
|**Active Control**|选项：
* Hide Before First Found：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活。
* Hide When Not Tracking（默认）：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用。
* None：不控制 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的激活与否。|
|**Root Location**|Block Root 的 GNSS（GPS、北斗等）信息。
它只在如下两种情况下有值：
1. 在编辑时，它下面其中一个 block 模型由 Mega Studio 导入且 block 数据含有GPS信息；
2. 在运行时，主动调用 [BlockHolder.Hold(BlockController.BlockInfo, Location)](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_Hold_EasyAR_Mega_Scene_BlockController_BlockInfo_EasyAR_Mega_Scene_Location_) 持有了一个 block。|
|*Latitude*|纬度。|
|*Longitude*|经度。|
|*Altitude*|海拔高度。|
|**Studio Tool**|当前控制 block 的 Studio 工具，仅用来在编辑模式下指示工具。|
