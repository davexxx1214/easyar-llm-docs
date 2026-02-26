---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockHolder.html
original_file: doc--zh-cn--develop--unity--mega--comp-BlockHolder.md
normalized_at: 2026-02-27
---
# BlockHolder 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html)
>
探索 BlockHolder 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockHolder.png)
默认条件下组件截图。
|属性|描述|
|**Multi Block**|定位到多个Block时的策略。选项：
* Disable（默认）：不允许多个 block。运行中检测到多个 block 时，会抛出致命错误。
* PlayMode：block 间的相对变换会在运行时计算，（通常）由 Mega Studio 在编辑模式下设置的数值将会保持到相关的两个 block 都被定位到为止。
* EditMode：block 间的相对变换在运行时不会发生变化，会保持（通常）由 Mega Studio 在编辑模式下设置的数值不变。|
|**Block Root Source**|Block root 的来源。
* External（默认）：外部，比如 Mega Studio 生成的节点或事先组装好的节点。
* Internal：内部，需要时由 [BlockHolder](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html) 自身创建。
* Mixed：混合，可以来自外部或内部。|
|**Block Root**|所有 Mega block 的父节点。它通常由 Mega 工具生成。如未设置，一个新的 root 节点会在第一个 block 被持有的时候自动生成。|
