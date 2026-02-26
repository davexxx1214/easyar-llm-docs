---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/occlusion.html
---

在 Unity 中使用 EasyAR Mega 实现遮挡 | EasyAR 文档
**
##### Table of Contents
**
# 在 Unity 中使用 EasyAR Mega 实现遮挡
遮挡 （Occlusion） 是提升 AR 虚实融合沉浸感的关键技术。本文将介绍如何在 Unity 中通过 EasyAR Mega 实现遮挡效果。
## 开始之前
* 完成[使用 EasyAR Mega Unity 样例快速入门](quickstart.html)。
* 能够[创建与实景对齐的内容](content-realworld-alignment.html)。
## 遮挡的实现方式
* 离线建模：在 Block 坐标系下，针对现实世界中的实体（如墙体、立柱、大型设备）创建 1:1 匹配的几何体；或通过对 Block 稠密模型进行裁剪与减面处理得到优化后的模型。
* 运行时对齐：在运行时，通过云定位将 Block 坐标系与现实空间对齐，并加载对应的几何体。
* 材质替换：为这些几何体赋予特殊的遮挡材质。
* 视觉效果：当 GPU 渲染其他虚拟物体时，会因深度测试未通过而自动剔除被遮挡部分的像素，从而使虚拟物体遵循现实物理空间的遮挡逻辑。
## 如何使用几何体作为遮挡
根据以下步骤可以在场景中添加作为遮挡使用的几何体并验证效果。
### 摆放遮挡几何体
根据 Mega Block 的稠密模型使用内置几何体或自建几何体作为遮挡摆放在 Block 坐标系下的正确位置。
![摆放遮挡几何体](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion01.png)
### [可选]根据全景图微调几何体的位置
![根据全景图微调遮挡](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion02.png)
### 为几何体赋予遮挡材质
将几何体材质修改为遮挡材质，可以使用 Unity 自带的 `SpatialMappingOcculusion`。
![根据全景图微调遮挡](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion03.png)
### 使用 EIF 数据模拟运行或实机运行
可以根据运行效果微调遮挡模型的摆放。
## 如何使用裁剪并减面的稠密模型作为遮挡
根据以下步骤将导出后的 Mega Block 稠密模型裁剪并减面得到用于遮挡的白模，并导入场景作为遮挡。
### 在 **Mega Blocks** 中导出
在 **Inspector** 面板中的 **Mega Blocks** 工具选择导出
![选择导出](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion04.png)
### 修改导出选项
在导出时注意修改导出选项。
![导出选项](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion05.png)
图中 1 为 LOD 层级，层级越低模型越简单，面数越少，若需要最高的精度选择2，若能接受降低精度以减少面数选择 1 或者 0。
图中 2 为导出贴图选项，由于我们只需要白模作为遮挡，不需要贴图。
### 对模型进行裁剪并减面
将导出后的模型在数字内容创建软件（例如 Blender）中进行裁剪，减面，保存为 `Glb`。
##### 提示
例子中使用的是 Blender 的 Decimate Modifier。
![裁剪前](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion06.png)
裁剪并减面后：
![裁剪后](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion07.png)
### 将遮挡模型导入 Unity 并挂载到场景中 Block 节点下方
![导入遮挡模型](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion09.png)
### 修改模型的 Transform
修改模型的 **Transform** 使 **Position**，**Rotation** 均全部为 **0**。
此时用于遮挡的白模应该和稠密模型贴合，这是因为在数字内容创建软件中进行裁剪和减面操作时，并没有改变 Block 坐标系的定义。
![遮挡模型贴合](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion10.png)
### 为模型赋予遮挡材质
将模型材质修改为遮挡材质，可以使用 Unity 自带的 `SpatialMappingOcculusion`。
![遮挡模型更换材质](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion11.png)
### 使用 EIF 数据模拟运行或实机运行
使用 EIF 数据模拟运行或实机运行，查看效果。
## 遮挡的效果预期
遮挡的效果主要由以下几点影响：
* 定位跟踪本身的精度
* 模型摆放的准确程度
* 模型本身的精度（如果不是简单的几何体）
在定位漂移时出现数公分未对齐的情况是正常的。
遮挡用的模型面数太多容易影响性能，建议只在必要区域使用，并且尽量使用简单的几何体作为遮挡。
## 相关主题
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [使用 session 验证工具模拟运行](verify-session-tool.html)