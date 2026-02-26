---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source-group.html
---

添加一组帧数据源 | EasyAR 文档
**
##### Table of Contents
**
# 添加一组帧数据源
一个 AR Session 可以包含多个帧数据源组件，称为帧数据源组（frame source group）。在运行时，session 会根据当前设备和启用的 AR 功能，从帧数据源组中选取一个最合适的帧数据源进行使用。本文介绍了如何使用和管理帧数据源组。
## 开始之前
* 了解 [帧数据源](frame-source.html) 的基本概念、类型以及运行时的选取方法。
## 使用预设 AR Session 的帧数据源组
[使用默认配置创建的 session](../fundamentals/session-creation.html) 会自带一组帧数据源，在使用单一 AR 功能时，一般就足够了。
不同预设 session 中所包含的帧数据源不同。
>
> 使用
[> ARSessionFactory.ARSessionPreset.ImageTracking
](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTracking)> 预设或
`> AR Session (Image Tracking Preset)
`> 菜单创建的 session 中只有单个帧数据源：
>
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-image-tracking.png)
>
> 使用
[> ARSessionFactory.ARSessionPreset.MegaBlock_MotionTracking_Inertial
](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)> 预设或
`> AR Session (Mega Block Default Preset)
`> 菜单创建的 session 中包含多个帧数据源组件的场景层级结构：
>
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-mega.png)
>
如果场景中一开始使用了某个预设创建了 session，在迭代过程中增加其它功能时，不仅需要添加相应的 frame filter 组件，还需要根据需要添加合适的帧数据源组件。
##### 重要事项
从 4.7 或更低版本升级后，需要整个删除 session 后重新通过菜单或 [ARSessionFactory](../../../api/unity/easyar.ARSessionFactory.html) 创建 session，才能使用预设的帧数据源组。
以下列出了所有预设的 AR 功能默认配置的帧数据源组件，注意列表中的排序与场景中帧数据源的组件排序相同：
|预设|帧数据源组|
|
* [ImageTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTracking)
* [CloudRecognition](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_CloudRecognition)
* [ObjectTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ObjectTracking)
* [SurfaceTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SurfaceTracking)|
1. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
|
* [MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MotionTracking)
* [SparseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapBuilder)
* [SparseSpatialMapTracker](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapTracker)
* [DenseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_DenseSpatialMapBuilder)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)|
|
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* [MegaLandmark\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)
* [MegaLandmark\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* [MegaLandmark\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial_3DOF)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
11. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* [MegaLandmark\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial_3DOF_0DOF)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
11. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
|
* [ImageTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTrackingMotionFusion)
* [ObjectTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ObjectTrackingMotionFusion)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
##### 注意
使用预设创建的组件排序可以保证在所有受内置帧数据源支持的设备上使用最优的帧数据源。
## 使用默认帧数据源配置
在使用默认参数时，帧数据源的配置会根据设备和运行时启用的 AR 功能自动调整。
如果手动修改过帧数据源的参数，在 session 中的 AR 功能发生变化时（比如在原本只包含图像跟踪的 session 中新增了运动跟踪功能），可能需要手动调整帧数据源的参数以适应新的功能需求，这样所有 AR 功能才能以最佳效果运行。
##### 重要事项
从 4.7 或更低版本升级后，需要整个删除 session 后重新通过菜单或 [ARSessionFactory](../../../api/unity/easyar.ARSessionFactory.html) 创建 session，才能使用正确的默认参数。
## 添加帧数据源组
在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` &gt; `[ AR 功能 ]` &gt; `Frame Source : \*` 可以添加适合该功能的 frame source 组件。也可以通过菜单 `EasyAR Sense` &gt; `Frame Source by Transform Type` &gt; `\* Dof` &gt; `Frame Source : \*` 添加需要的 frame source 组件。
在脚本中，可以使用 [ARSessionFactory.AddFrameSource&lt;Source&gt;(GameObject, bool)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameSource__1_UnityEngine_GameObject_System_Boolean_) 来添加 frame source 组件。
比如，通过菜单 `EasyAR Sense` &gt; `Frame Source by Transform Type` &gt; `3 Dof Rot-Only` &gt; `Frame Source : Three Dof Camera Device` 可以给当前选中的 session 添加一个 [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-add.png)
对应的脚本代码如下：
```
`ARSessionFactory.AddFrameSource&lt;ThreeDofCameraDeviceFrameSource&gt;(session);
`
```
## 帧数据源排序
session 组装过程中，帧数据源组中最终只有一个帧数据源会被选中后组装到 session 中，选取的规则取决于 [AssembleOptions.FrameSourceSelection](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html) 属性的值。在默认配置下，可以通过调整帧数据源组中各个组件的排序来影响最终被选中的帧数据源。
一般可以使用在 `Hierarchy` 视图中 [对场景中的物体进行排序](https://docs.unity3d.com/Manual/Hierarchy.html) 的方法直接移动 frame source 物体进行排序。
在脚本中，可以使用 [Transform.SetSiblingIndex(int)](https://docs.unity3d.com/ScriptReference/Transform.SetSiblingIndex.html) 来调整物体的排序。
比如，要将 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 排在其它帧数据源前面，可以在 `Hierarchy` 视图中选中 `Motion Tracker` 物体并拖动到最上面的位置。
相同的效果也可以通过下面的脚本代码实现：
```
`motionTrackerFrameSource.transform.SetSiblingIndex(0);
`
```
另外还有一些预定义的排序方法可以使用。在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` &gt; `Utility` &gt; `Sort Frame Source : \* &gt; \*` 对特定的若干帧数据源组件进行排序。
在脚本中，可以使用 [ARSessionFactory.SortFrameSource(GameObject, ARSessionFactory.FrameSourceSortMethod)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_SortFrameSource_UnityEngine_GameObject_easyar_ARSessionFactory_FrameSourceSortMethod_) 实现相同的效果。
比如，通过菜单 `EasyAR Sense` &gt; `Utility` &gt; `Sort Frame Source : Motion Tracker &gt; System SLAM` 可以将 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 排在 [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)、[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)、[ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)、[ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)和 [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html) 前面。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-sort.png)
对应的脚本代码如下：
```
`ARSessionFactory.SortFrameSource(session, new ARSessionFactory.FrameSourceSortMethod { MotionTracker = ARSessionFactory.FrameSourceSortMethod.MotionTrackerSortMethod.PreferEasyAR });
`
```
经过上面的排序之后，场景层级结构变为：
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-sorted.png)
## 相关主题
* 了解如何 [添加和配置头显用的帧数据源](../headsets/enable-headset.html)
* 尝试在运行时 [获取正在使用的帧数据源](../fundamentals/session-components.html)