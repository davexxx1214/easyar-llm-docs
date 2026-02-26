---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/target.html
---

添加 Mega 跟踪目标 | EasyAR 文档
**
##### Table of Contents
**
# 添加 Mega 跟踪目标
本文介绍了如何添加 Mega 的跟踪目标以及如何在 Unity 编辑器中加载环境模型以辅助开发。
## 开始之前
* 检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
* [导入最新版本的 EasyAR 插件以启用 Mega 功能](enable-mega.html)
* 了解 [Unity AR 的跟踪目标](../fundamentals/target.html) 的基本概念和使用方法
##### 注意
以下内容及工具仅适用于使用 EasyAR Mega 开发 Unity 应用的过程。
如果您在开发小程序，请参考 [使用 Unity 编辑器创建并上传标注（小程序开发）](../../wechat/mega/content-annotation-creation.html)。
如果您只希望查看 Mega 建图结果，请参考 Mega 使用指南中的 [预览3D 实景网格](../../../mega/mapping/textured-mesh.html)。
如果您需要模拟运行查看定位效果，但您并没有一个可以使用的 Unity 应用工程，请参考 Mega 使用指南中的 [模拟运行效果预览](../../../mega/simulation-verification/intro.html)。
## Mega 的跟踪目标
Mega 的跟踪目标是包含 [BlockController](../../../api/unity/EasyAR.Mega.Scene.BlockController.html) 组件的空物体，称为 block。在场景中，block 会被组织在一个包含 [BlockRootController](../../../api/unity/EasyAR.Mega.Scene.BlockRootController.html) 组件的空物体下，这个物体的默认名称为 `MegaBlocks`。`MegaBlocks` 下所有的 block 物体代表了当前定位库中的所有跟踪目标。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/target-block.png)
开发中经常需要使用 block 模型来辅助查看和摆放 3D 内容。这个模型可以使用工具加载到场景中，方便查看和参考。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/target-block-model.png)
模型位置是与 block 跟踪目标对齐的，可以直接在模型上摆放 3D 内容。
##### 提示
模型存储于工具节点下，仅存在于编辑器模式下，不会被打包进最终应用。
## 在编辑器中添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [External](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_External)（默认） 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/block-root-source.png)
### 添加 Block Viewer for Unity Developer 工具
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Mega` &gt; `Tool` &gt; `Block Viewer for Unity Developer (Edit Mode)` 可以添加 Unity 开发用的 Block Viewer 工具。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer.png)
##### 重要事项
使用 Unity 开发 Mega 应用时，必须使用 `Block Viewer for Unity Developer` 工具。`EasyAR Mega` &gt; `Tool` 菜单下的其它工具不适合做 Unity 应用开发。
虽然 `Annotation Tool` 也有类似的功能，但这个工具的部分功能将在未来版本中被移除，因此不建议使用。
`Annotation Tool` 的标注功能（仅标注本身）即将迁移至 EasyAR 开发中心网页，block mesh 加载和模型摆放不受影响。
工具添加成功后，场景层级中会多出一个 `EasyAR.Mega.BlockViewer (Dev)` 节点和一个 `MegaBlocks` 节点。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer-result.png)
### 生成跟踪目标 —— block
选中 `EasyAR.Mega.BlockViewer (Dev)` 节点，在 **Inspector** 面板中填写 EasyAR 账号信息并登录；
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/login.png)
点击 Mega Cloud Service 右侧按钮；
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/click-cls.png)
选择需要使用的 `Mega定位服务`，点击**确定**。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/select-cls.png)
在选择服务之后，当前库中的 block 列表会显示在 `MegaBlocks` 节点下，并显示在工具面板上。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/load-block.png)
##### 提示
为什么我的 `MegaBlocks` 下面是空的？
建议检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
到这里已经生成了跟踪目标 block，`MegaBlocks` 节点下每个 `Block\_` 开头的子节点即代表一个 block 跟踪目标。
### 加载 block 模型
点击**加载**选择的Block：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/load-block-2.png)
加载完成后，Block 会显示在 `Scene` 窗口中。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/block-in-scene.png)
## 定位成功时自动添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [Internal](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Internal) 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)。
在这两个模式下，如果定位到一个新的 block 且 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下没有该 block，这个新的 block 会被自动添加到 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下。如果 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 不存在会被自动创建。
##### 提示
定位成功时自动添加跟踪目标时，无法加载 block 模型，仅能添加 block 跟踪目标。
## 在脚本中添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [Internal](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Internal) 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)，这时如果 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 不存在会被自动创建。或者也可以在 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [External](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_External) 时在编辑器中事先指定好 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 物体。
##### 注意
如果 block 不在定位库中，即使使用脚本添加到场景中，block 也无法被定位到。
可以使用 [BlockHolder.Hold](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_Hold_) 方法添加一个新的 block 到 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下。这个方法通常用在使用 ema 标注文件时，脚本读取到标注信息后添加 block。
比如，下面的代码片段展示了如何使用标注文件中的信息添加 block：
```
`foreach (var item in ema.blocks)
{
var info = new BlockController.BlockInfo { ID = item.id.ToString(), Timestamp = item.timestamp };
if (!item.keepTransform &amp;&amp; item.location.OnSome)
{
blockHolder.Hold(info, item.location.Value);
}
else
{
blockHolder.Hold(info, item.transform.ToUnity());
}
}
`
```
##### 提示
使用脚本在运行时添加跟踪目标时，无法加载 block 模型，仅能添加 block 跟踪目标。
## 后续步骤
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)
## 相关主题
* [Mega Studio（Unity）操作手册](../../../mega/reference/studio-unity/intro.html)