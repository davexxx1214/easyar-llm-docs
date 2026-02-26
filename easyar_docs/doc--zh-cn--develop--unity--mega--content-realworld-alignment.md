---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/content-realworld-alignment.html
---

如何使用 Mega Studio 创建与实景精确对齐的 3D 内容 | EasyAR 文档
**
##### Table of Contents
**
# 如何使用 Mega Studio 创建与实景精确对齐的 3D 内容
这篇文档将介绍如何使用 Unity 上的 Mega Studio 将虚拟物体准确地摆放在现实空间的某个位置，在 AR 体验中与现实空间精确对齐。
## 开始之前
* 参考文档 [我的定位库可以使用了吗？](../../mega/localization-verify.html) 确认定位库已正确创建并添加 **Mega Block**。
* 准备好 Unity 项目中要使用的 3D 资产。
## 精确摆放 3D 内容
通过完成以下步骤可以将虚拟内容准确地摆放在现实空间中。
### 将 3D 内容挂载至 Block 节点下
加载 Block 稠密模型后，将 3D 内容挂载至场景中的 Block 节点下，作为其子节点。
![挂载模型](https://doc-asset.easyar.com/develop/unity/mega/media/content-realworld-alignment05.png)
### 精确调整模型位置
在场景中对着稠密模型调整 3D 内容的位置和旋转，将其调整至期望的位置和朝向。
### [可选] 根据全景图精确调整模型位置
点击 **Inspector** 面板中的全景标记右侧的加载按钮，场景中出现全景标记。
![加载全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation13.png)
![显示全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation14.png)
点击任意一个**全景标记**，就可以在其位置进行全景下的摆放。您可以通过点击不同的**全景标记**切换全景，以确认 3D 内容在不同视角下的位置都是准确的。
![全景编辑](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation15.png)
## 如果加载的 Block 模型不水平怎么办
在 **Hierarchy** 面板中选择 **Block Root** ，在 **Inspector** 面板中修改 **Rotation** 直到稠密模型的朝向朝向在 Unity 编辑器中看起来正确。
##### 重要事项
Block Root 是在 3D 引擎场景节点树上所有 Block 节点的父节点。
Block Root 在世界坐标系下的 Transform **不会**影响 Block 的**本地坐标系**，也因此**不会影响作为 Block 子节点 3D 内容的渲染结果**。它的 Transform 和最终的显示效果**无关**。
## 如果加载的 Block 模型有破碎，缺损的部分怎么办
在三维重建过程中，若受采集视角覆盖不全的影响，生成的密模型中可能会出现破碎或缺损的部分。
![破碎缺损](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment02.png)
面对不完整的模型，若破碎/缺损部分的 3D 内容对齐精度要并不高，可以通过点击**全景标记**对照**全景图**的方式来摆放 3D 内容。之后可以通过点击附近不同的**全景标记**位置来验证效果。
![通过全景图摆放](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment03.png)
若破碎/缺损部分的 3D 内容对齐精度要求非常高，则需要通过[补充更新](../../../mega/scene-update/incremental.html)或[无损全量更新](../../../mega/scene-update/full.html)进行地图的补充或更新。一般来说这样的区域意味着采图过程中没有覆盖，在这样的区域内部 Mega 定位效果会受到影响，仅在编辑器中对齐 3D 内容是不够的。
## 后续步骤
* 通过[使用 session 验证工具模拟运行](verify-session-tool.html)进一步验证摆放的准确性。
* 为场景添加准确的[环境遮挡](occlusion.html)以增强 AR 的真实感。