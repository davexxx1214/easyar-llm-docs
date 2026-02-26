---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-creation.html
original_file: doc--zh-cn--develop--unity--fundamentals--session-creation.md
normalized_at: 2026-02-27
---
# 创建和配置 AR session
在 Unity 中使用 AR，需要首先在场景中创建并配置 AR session。本文介绍了创建和配置 AR session 的几种主要方法。一般在成功创建 session 之后，在 `Hierarchy` 视图中可以看到如下结构：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-result.png)
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
## 创建默认配置的 session
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `AR Session ([ 功能 ] Preset)` 可以创建一个预设好的 session。session 预先配置了适合该功能的 frame source 和 frame filter 组件。
在脚本中，可以使用 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 来创建 session。
比如，通过菜单 `EasyAR Sense` > `Image Tracking` > `AR Session (Image Tracking Preset)` 可以创建一个用于图像跟踪的 session。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation.png)
对应的脚本代码如下：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.ImageTracking);
```
需要注意的是，在使用 [ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapBuilder) 以及 [ARSessionFactory.ARSessionPreset.DenseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_DenseSpatialMapBuilder) 预设时，需要同时传入资源参数。例如，下面的代码创建了一个用于稀疏空间构建的 session，并指定了点云材质：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder, new ARSessionFactory.Resources { SparseSpatialMapPointCloudMaterial = PointCloudMaterial });
```
如果脚本只在编辑器中运行，也可以使用默认编辑器资源：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder, ARSessionFactory.Resources.EditorDefault());
```
菜单 `EasyAR Sense` > `AR Session (Preset)` > `\*\*` 中列出了所有可以使用的预设 session，可以参考使用。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-presets.png)
> **注意**
同一个场景中多个 session 同时运行会相互冲突，因此在场景中最多只能保留一个被启用（[GameObject.activeInHierarchy](https://docs.unity3d.com/ScriptReference/GameObject-activeInHierarchy.html) == `true`）的 session。
## 添加组件
session 的 frame source 和 frame filter 组件可以在 session 创建后根据需要添加和删除。
在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `\*\*` 可以添加适合该功能的 frame source 和 frame filter 组件。
在脚本中，可以使用 [ARSessionFactory.AddFrameSource<Source>(GameObject, bool)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameSource__1_UnityEngine_GameObject_System_Boolean_) 来添加 frame source 组件，或使用 [ARSessionFactory.AddFrameFilter<Filter>(GameObject, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameFilter__1_UnityEngine_GameObject_easyar_ARSessionFactory_Resources_) 来添加 frame filter 组件。
比如，通过菜单 `EasyAR Sense` > `Image Tracking` > `Frame Filter : Image Tracker` 可以给当前选中的 session 添加一个新的图像跟踪器。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-add.png)
对应的脚本代码如下：
```
ARSessionFactory.AddFrameFilter<ImageTrackerFrameFilter>(session);
```
> **小心**
添加组件必需在 assemble 前完成。session 开始执行 assemble 以及完成 assemble 后，任何对组件的增加和删除都会导致 session 进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并停止工作。
需要注意的是，在添加 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html) 以及 [DenseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.DenseSpatialMapBuilderFrameFilter.html) 时，需要同时传入资源参数。例如，下面的代码创建了一个用于稀疏空间构建的 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html)，并指定了点云材质：
```
ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, new ARSessionFactory.Resources { SparseSpatialMapPointCloudMaterial = PointCloudMaterial })
```
如果脚本只在编辑器中运行，也可以使用默认编辑器资源：
```
ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, ARSessionFactory.Resources.EditorDefault());
```
创建 frame filter 之后，可以使用 [ARSessionFactory.SetupFrameFilters(List<GameObject>, ARSessionFactory.ARSessionPreset)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_SetupFrameFilters_System_Collections_Generic_List_UnityEngine_GameObject__easyar_ARSessionFactory_ARSessionPreset_) 来根据预设配置调整 frame filter 的参数。
比如下面这段代码给 session 添加一个新的图像跟踪器，并配置成 [ARSessionFactory.ARSessionPreset.ImageTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTrackingMotionFusion) 的预设参数。
```
var filter = ARSessionFactory.AddFrameFilter<ImageTrackerFrameFilter>(session);
ARSessionFactory.SetupFrameFilters(new() { filter }, ARSessionFactory.ARSessionPreset.ImageTrackingMotionFusion);
```
使用菜单创建时无法按预设调整参数，需要在创建后根据具体的组件说明进行配置。
## 删除组件
要从 session 中删除组件，可以在 `Hierarchy` 视图中选中对应的组件并按 `Delete` 键，或者在脚本中销毁（`Destroy`）对应的物体。
> **注意**
禁用（`SetActive(false)`）组件的 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的效果与删除组件相同。
比如要从 session 中删除图像跟踪器，可以选中 `Image Tracker` 并按 `Delete` 键。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-del.png)
> **小心**
删除组件必需在 assemble 前完成。session 开始执行 assemble 以及完成 assemble 后，任何对组件的增加和删除都会导致 session 进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并停止工作。
## 组件排序的影响
session 的 frame filter 子节点的排列顺序对 session 执行没有任何影响。
session 的 frame source 子节点的排列顺序将影响 frame source 在 assemble 过程中的选择顺序。只有按 **transform 顺序** 排列的第一个可用的 frame source 会被选中作为 session 的实际 frame source。
> **注意**
frame source 节点的顺序只有在 assemble 之前修改是有效的。assemble 后，调整顺序不会影响运行结果。
## [可选] 自由创建 session
如果默认配置的 session 不能满足需求，还可用根据需要自由创建和配置 session。
可用使用菜单 `EasyAR Sense` > `AR Session (Preset)` > `AR Session (Empty)` 创建一个不包含任何 frame source 和 frame filter 组件的空 session。
在脚本中，可以使用 [ARSessionFactory.CreateSession()](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession) 来实现。
```
ARSessionFactory.CreateSession();
```
然后根据实际需要，添加合适的 frame source 和 frame filter 组件。
比如，如果需要创建一个包含稀疏空间构建和稠密空间构建功能的 session，可以使用下面的代码：
```
var session = ARSessionFactory.CreateSession();
var group = new GameObject("Frame Source Group");
group.transform.SetParent(session.transform, false);
ARSessionFactory.AddFrameSource<XREALFrameSource>(session);
ARSessionFactory.AddFrameSource<AREngineFrameSource>(session);
ARSessionFactory.AddFrameSource<ARCoreFrameSource>(session);
ARSessionFactory.AddFrameSource<ARCoreARFoundationFrameSource>(session);
ARSessionFactory.AddFrameSource<ARKitFrameSource>(session);
ARSessionFactory.AddFrameSource<ARKitARFoundationFrameSource>(session);
ARSessionFactory.AddFrameSource<VisionOSARKitFrameSource>(session);
ARSessionFactory.AddFrameSource<MotionTrackerFrameSource>(session);
List<GameObject> filters = new();
filters.Add(ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, resources));
filters.Add(ARSessionFactory.AddFrameFilter<DenseSpatialMapBuilderFrameFilter>(session, resources));
ARSessionFactory.SetupFrameFilters(filters, ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder);
ARSessionFactory.SetupFrameFilters(filters, ARSessionFactory.ARSessionPreset.DenseSpatialMapBuilder);
```
它将创建出这样的 session 结构：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-custom.png)
## 后续步骤
控制运行
* 了解 [初始化](initialization.html) 的方法和作用
* 了解如何 [判断可用性和设备支持](session-assemble.html)
* 了解 [控制 session 执行](session-ctrl.html) 的方法
访问组件和结果
* 尝试 [访问 AR 功能组件](session-components.html)
* 了解如何 [获取 session 的运行结果](session-output.html)
组件参考
* [ARSession](comp-ARSession.html) 组件参考
进一步了解 frame source 排序的影响和如何
* 了解 [帧数据源](../cameras/frame-source.html)
* 了解 [创建一组输入源](../cameras/frame-source-group.html) 的方法
根据应用功能创建最佳的 session
* [Mega](../mega/session-best-practice.html)
