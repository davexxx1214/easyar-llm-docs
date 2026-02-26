---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-imp.html
---

让头显支持 EasyAR | EasyAR 文档
**
##### Table of Contents
**
# 让头显支持 EasyAR
本文介绍如何使用 EasyAR Sense Unity Plugin 的头显扩展包模板来开发一个支持头显设备的 EasyAR 扩展包。
## 开始之前
在进入开发之前，需要先了解如何使用 EasyAR Sense Unity Plugin。
* [快速入门](../getting-started/quickstart.html)
* 运行 [AR Session 示例](../fundamentals/sample-arsession.html)、图像跟踪示例 ImageTracking\_Targets 和稠密空间地图示例 SpatialMap\_Dense\_BallGame，它们的运行效果在手机上和头显上是相似的。
头显插件开发会涉及一些基础功能，需要先了解这些内容：
* 了解 [AR Session](../fundamentals/session.html)
* 了解 [帧数据源](../cameras/frame-source.html) 和 [外部帧数据源](../cameras/external-frame-source.html)
此外，还需要熟悉 [如何开发一个 Unity 的 package](https://docs.unity3d.com/Manual/CustomPackages.html)。
## 为 AR/MR 准备设备
* 准备运动跟踪/VIO 系统
确保设备跟踪误差受控。一些 EasyAR 功能比如 Mega 可以在某种程度上降低设备累积误差，但大的局部误差也会让 EasyAR 的算法变得不稳定。通常来讲，通常我们期望 VIO 漂移在 1‰ 以内。
* 准备显示系统
确保当一个与现实中某个物体大小和轮廓相同的虚拟物体被放置在虚拟世界中，且它与虚拟摄像机的相对变换关系与真实世界中对应物体与设备的变换关系相同时，虚拟物体可以贴合显示在真实物体上，且移动设备或转头不会打破显示效果。可以参考 Vision Pro 的效果。
* 准备设备 SDK
确保已经有 API 可以提供 [外部输入帧数据](../cameras/external-input-frame.html) 。这些数据应该由系统中的两个且只有两个时间点产生，需要确保不会出现数据无法对齐的情况。
## 使用头显扩展包模板
通过 Unity 的 [Package Manager window](https://docs.unity3d.com/Manual/upm-ui.html) 来 [使用本地 tarball 文件安装插件](https://docs.unity3d.com/Manual/upm-ui-tarball.html) 导入 `EasyAR Sense Unity Plugin` （package `com.easyar.sense`）。解压头显扩展模板 （package `com.easyar.sense.ext.hmdtemplate`）到 Unity 工程的 Packages 目录，并重命名 `Samples\~` 文件夹为 `Samples` 。
这时应看到这样的目录结构：
```
`.
├── Assets
└── Packages
└── com.easyar.sense.ext.hmdtemplate
├── CHANGELOG.md
├── Documentation\~
├── Editor
├── LICENSE.md
├── package.json
├── Runtime
└── Samples
└── Combination\_BasedOn\_HMD
`
```
##### 提示
如有需要，可以使用任何 Unity 允许的方式来导入 `EasyAR Sense Unity Plugin` 和存放头显扩展模板。
如果不使用模板，也可以参考 [Unity 创建自定义 package 的指南](https://docs.unity3d.com/Manual/CustomPackages.html) 来创建一个新的 package。
如果设备 SDK 未使用 Unity 的 package 来组织，需要解压头显扩展模板到 Unity 的 Assets 文件夹，然后从解压的文件中删除 package.json 以及任何以 .asmdef 为后缀名的文件。请注意在这种使用方式下，同时使用设备 SDK 与 EasyAR 的用户将无法获得合理的版本依赖。
## 完成运行时输入扩展
遵循 [创建图像和设备运动数据输入扩展](../cameras/external-device-frame-source.html) 方法，修改 `Runtime/HMDTemplateFrameSource.cs` 并完成适用于头显的输入扩展。这是扩展包最主要的开发工作。
## 完成编辑器菜单
修改 `MenuItems` 类中的 "HMD Template" 字符串为代表设备的名称。如果需要其它自定义编辑器功能，也可以添加其它脚本。
开发者在 `Hierarchy` 视图中选中 **AR Session (EasyAR)** 并点击右键时会出现这些菜单项：
* `EasyAR Sense` &gt; `Extensions` &gt; `Frame Source : [Device Name]`：在当前 session 中添加一个该设备的帧数据源。
* `EasyAR Sense` &gt; `Extensions` &gt; `Frame Source : [Device Name (keep it only)]`：在当前 session 中添加并仅保留一个该设备的帧数据源。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-context-menu.png)
## 完成应用示例
示例位于 `Samples/Combination\_BasedOn\_HMD`。简单起见，示例模板中没有代码，全部 AR 功能靠场景内容及配置即可完成。
1. 添加支持设备运行的内容到场景中。
##### 提示
如有需要，也可以反过来做，使用一个可以在设备上运行的场景，然后添加 EasyAR 组件和 sample 场景中的其它物体到场景中。
2. 修改设计用来放在 session 原点下的物体。
如果场景中定义了 session 原点，移动 `EasyARPanda` 和 `UI` 到原点节点下。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-ui.png)
`EasyARPanda` 会提供一个设备运动跟踪行为的参照，这会帮助判断跟踪不稳定时候的原因。
这些物体名称括号内的文字是给扩展开发者看的提示，可以删除：
* `(Move into Origin if there is any)`
* `(Move into Origin if there is any, set constraint source to your rendering camera)`
* 配置 `HUD` 按钮行为。
设置 `UI` 的 constraint source 为虚拟摄像机，以确保 `HUD` 按钮可以按预期工作。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-hud.png)
* 配置 `Canvas` 的 raycast 功能。
修改 `UI` 节点下的 `Canvas`，确保 raycast 可以工作，以保证所有 UI 按钮和开关可以按预期工作。
模板中已经在 `Canvas` 节点下预先添加了 [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/index.html) 的 [Tracked Device Graphic Raycaster](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/tracked-device-graphic-raycaster.html)，导入对应的 package 之后即可看到。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-raycaster.png)
如果在设备上运行时不使用 [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/index.html)，会看到类似下面的缺少脚本提示，可以将其删除，并添加设备所需的 raycaster 组件。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-raycaster-missing.png)
## 后续步骤
* 在进一步完成扩展包之前，需要先 [运行验证（bring-up）](extension-bring-up.html) 输入扩展
* 全部完成之后，可以准备 [发布扩展包](extension-dist.html)
## 相关主题
* [扩展包模板参考](extension-template.html)
* [外部输入帧数据](../cameras/external-input-frame.html)
* [创建图像和设备运动数据输入扩展](../cameras/external-device-frame-source.html)