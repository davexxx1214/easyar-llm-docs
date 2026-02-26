---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-realworld-alignment.html
---

如何使用 Unity 上的 Mega Studio 创建与实景精确对齐的 3D 内容 | EasyAR 文档
**
##### Table of Contents
**
# 如何使用 Unity 上的 Mega Studio 创建与实景精确对齐的 3D 内容
尽管 xr-frame 没有提供 3D 编辑器功能，您还是可以借助 Mega Studio 将虚拟物体准确地摆放在现实空间的某个位置，在 AR 体验中与现实空间精确对齐。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* 准备模型： 使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[XRFame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)，准备符合 xr-frame 要求的模型文件。
* 将模型的文件导入 Unity 。
##### 提示
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
## 将 3D 内容作为标注的子节点
将导入的模型拖到场景节点，作为标注的子节点。
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0**， Scale 可以根据需要自行调整。
##### 注意
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![修改模型Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
## 精确调整模型位置
选择 **标注节点** 在场景中对着稠密模型调整模型的位置和旋转。
##### 注意
模型相对于标注的 Position 和 Rotation 必须始终全部为 **0** ，否则您无法在 xr-frame 上得到正确的渲染结果。
## [可选] 根据全景图精确调整模型位置
点击 **Inspector** 面板中的全景标记右侧的加载按钮，场景中出现全景标记。
![加载全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation13.png)
![显示全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation14.png)
点击任意一个全景标记，就可以在其位置进行全景下的摆放，您可以切换全景的位置以确认模型在不同视角下的位置都是准确的。
![全景编辑](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation15.png)
## 如果加载的 Block 模型不水平怎么办
在 **Hierarchy** 面板中选择 **Block Root** ，在 **Inspector** 面板中修改 **Rotation** 直到稠密模型的朝向在 Unity 编辑器中看起来正确。
##### 重要事项
Block Root 是在 3D 引擎场景节点树上所有 Block 节点的父节点。
Block Root 在世界坐标系下的 Transform **不会**影响 Block 的**本地坐标系**，也因此**不会影响标注和标注下模型的渲染结果**。它的 Transform 和最终的显示效果**无关**。
## 如果加载的 Block 模型有破碎，缺损的部分怎么办
在三维重建过程中，若受采集视角覆盖不全的影响，生成的密模型中可能会出现破碎或缺损的部分。
![破碎缺损](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment02.png)
面对不完整的模型，若破碎/缺损部分的 3D 内容对齐精度要并不高，可以通过点击**全景标记**对照**全景图**的方式来摆放 3D 内容。之后可以通过点击附近不同的**全景标记**位置来验证效果。
![通过全景图摆放](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment03.png)
得到摆放结果。
![摆放结果](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment04.png)
若破碎/缺损部分的 3D 内容对齐精度要求非常高，则需要通过[补充更新](../../../mega/scene-update/incremental.html)或[无损全量更新](../../../mega/scene-update/full.html)进行地图的补充或更新。一般来说这样的区域意味着采图过程中没有覆盖，在这样的区域内部 Mega 定位效果会受到影响，仅在编辑器中对齐 3D 内容是不够的。
## 后续步骤
* 尝试[在 Unity 编辑器中模拟运行](content-simulation.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
**微信小程序 Mega 插件**：
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
**Mega Studio**：
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)