---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-template.html
original_file: doc--zh-cn--develop--unity--headsets--extension-template.md
normalized_at: 2026-02-27
---
# 头显扩展包模板简介
`com.easyar.sense.ext.hmdtemplate` package 是为头显扩展开发提供的示例和模板。它是一个 SDK 的实现，并且包含了给应用开发者的示例。
## 模板内容
这个 package 的包结构遵循了 [Unity 推荐的文件布局](https://docs.unity3d.com/Manual/cus-layout.html)：
```
.
├── CHANGELOG.md
├── Documentation\~
├── Editor
├── LICENSE.md
├── package.json
├── Runtime
└── Samples\~
└── Combination\_BasedOn\_HMD
```
其中一些比较重要的内容如下：
* **Runtime**：存放运行时平台资产的文件夹。这是模板中最重要的文件夹。
* **Samples\~**：存放 package 中所有示例的文件夹。它包含给下游使用的示例，可以用作测试扩展的 demo。为了原地开发这个示例，需要修改文件夹名为 `Samples` 。使用 [Client.Pack](https://docs.unity3d.com/ScriptReference/PackageManager.Client.Pack.html) 方法会在打包一个新的发布时将其自动重命名为 `Samples\~` 。
* **Editor**：存放编辑时平台资产的文件夹。这个文件夹的脚本主要用于创建菜单项。
* **package.json**：package 的清单文件。
## 模板示例的创建过程
1. [添加 AR Session](../fundamentals/session-creation.html)
在 `Hierarchy` 视图中：
* 在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Mega` > `AR Session (Mega Block Default Preset)` 添加 [ARSession](../../../api/unity/easyar.ARSession.html)。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Frame Filter : Image Tracker` 添加一个 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `SpatialMap` > `Frame Filter : Dense SpatialMap Builder` 添加一个 [DenseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.DenseSpatialMapBuilderFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `SpatialMap` > `Frame Filter : Sparse SpatialMap Builder` 添加一个 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Extensions` > `Frame Source : HMD Template (keep it only)` 添加并仅保留 HMD Template 这一个 [FrameSource](../../../api/unity/easyar.FrameSource.html)。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-session.png)
* 添加 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html)
在 `Hierarchy` 视图中，在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Target : Image Target` 添加一个 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html) 到 session 中。
配置 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html)：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-image-target.png)
在完成上述配置之后，`Scene` 视图中显示的图像是 gizmo。这个示例中通过一个 quad 来显示同一图像的虚拟物体。
添加显示在 target 上面的虚拟物体：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-image-target-content.png)
* 添加一个模型作为运动跟踪原点参考
这个模型对开发者以及下游用户都很重要，它用于解耦设备运动跟踪和 EasyAR 算法。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-origin-content.png)
* 添加功能选择的 UI
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-ui.png)
* 关闭启动时启用的 EasyAR 功能，并通过 UI 开关来打开它们
例如，图像跟踪的功能在启动时可以关闭，只需要设置对应组件的 enable 为 false 即可：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-feature-off.png)
然后添加 UI 开关处理：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-ui-switch.png)
## 相关主题
* [让头显支持 EasyAR](extension-imp.html) 介绍了如何使用这个模板来创建一个新的头显扩展包
* [运行验证（bring-up）](extension-bring-up.html) 介绍了如何利用这个模板提供的示例验证输入扩展的正确性
* [发布扩展包](extension-dist.html) 介绍了如何基于这个模板完成最后的打包分发
