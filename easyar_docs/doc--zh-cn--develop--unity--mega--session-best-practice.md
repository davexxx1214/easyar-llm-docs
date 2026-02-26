---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/session-best-practice.html
---

适用于 Mega 的 AR Session 最佳实践 | EasyAR 文档
**
##### Table of Contents
**
# 适用于 Mega 的 AR Session 最佳实践
本文介绍了如何创建和配置适用于 Mega 的 AR session，以便在不同类型的设备上获得最佳的运行效果。
## 开始之前
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 了解如何 [创建 session](../fundamentals/session-creation.html)
## 默认配置的 session
对于大部分应用，推荐使用默认的 Mega session 配置，这些配置已经过优化，适用于大部分常见的使用场景。
默认的 session 支持以下类型的设备：
* 支持 6DoF 运动跟踪的设备（部分现代手机和头显）
* 支持 5DoF 惯性导航功能的设备（大部分有陀螺仪和加速度计的 Android 手机）
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` &gt; `Mega` &gt; `AR Session (Mega Block Default Preset)` 可以创建默认的 Mega session。
对应的脚本代码如下：
```
`ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.MegaBlock\_MotionTracking\_Inertial)
`
```
该 session 使用 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设：
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` &gt; `Mega` &gt; `AR Session (Mega Landmark Default Preset)` 可以创建默认的 Mega session。
对应的脚本代码如下：
```
`ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.MegaLandmark\_MotionTracking\_Inertial)
`
```
该 session 使用 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设：
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组。
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Landmark](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Landmark)
## 选择不同的预设
除了默认配置的 Mega session 外，还可以根据具体需求选择不同的预设来创建 session，它们的主要差别在于支持设备类型不同。
使用菜单和 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 创建 session 时可选的预设包括：
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)（默认）
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ZeroDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ZeroDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
使用菜单和 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 创建 session 时可选的预设包括：
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)（默认）
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ZeroDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ZeroDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
##### 注意
Mega 在不同类型的设备上运行效果是不一样的，详情可以参考 [Mega 支持的设备和平台应用](../../mega/devices.html)。
## 后续步骤
* [添加跟踪目标](target.html)
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)
## 相关主题
* 阅读 [帧数据源](../cameras/frame-source.html) 了解帧数据源的基本概念及运行时帧数据源选取过程
* 阅读 [添加一组帧数据源](../cameras/frame-source-group.html) 了解数据源组的配置和使用方法
* 阅读 [Mega 支持的设备和平台应用](../../mega/devices.html) 了解 Mega 支持的设备以及在不同设备上的运行效果