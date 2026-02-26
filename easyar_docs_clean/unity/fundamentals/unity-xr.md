---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-xr.html
original_file: doc--zh-cn--develop--unity--fundamentals--unity-xr.md
normalized_at: 2026-02-27
---
# EasyAR 对 Unity XR 框架的支持
EasyAR 并不依赖 Unity XR 框架来提供 AR 功能，但可以支持 Unity XR 框架中的部分组件包，以便在 Unity 中使用 EasyAR 的 AR 功能时可以利用 Unity XR 框架提供的功能。以下内容介绍了 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
## Unity XR 支持
Unity 通过其 [插件框架及一系列功能包和工具包](https://docs.unity3d.com/Manual/xr-support-landing.html) 支持 XR 开发。EasyAR 也支持这些 Unity XR 组件包，以便在 Unity 中使用 EasyAR 的 AR 功能时可以利用 Unity XR 框架提供的功能。
EasyAR 支持以下 Unity XR 组件包：
|显示名称|包名|最低支持版本|是否必需|用途|
|**XR Core Utilities**|com.unity.xr.core-utils|2.0.0|否|提供 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 支持|
|**AR Foundation**|com.unity.xr.arfoundation|5.0.0|否|提供 AR Foundation 支持|
|**XR Plugin Management**|com.unity.xr.management|3.0.0|否|提供 ARCore SDK 管理兼容及获取运行时 XR Loader 类型|
|**XR Interaction Toolkit**|com.unity.xr.interaction.toolkit|2.0.0|否|未直接使用|
|**PolySpatial visionOS**|com.unity.polyspatial.visionos|2.0.4[1](#fn:1)|否|未直接使用|
|**Apple visionOS XR Plugin**|com.unity.xr.visionos|2.0.4[1](#fn:1)|否|未直接使用|
|**Apple ARKit XR Plugin**|com.unity.xr.arkit|5.0.0|否|未直接使用|
|**Google ARCore XR Plugin**|com.unity.xr.arcore|5.0.0|否|提供 ARCore SDK 管理兼容|
> **注意**
EasyAR 并不依赖 Unity XR 框架来提供 AR 功能。因此，在没有 AR Foundation 等 Unity XR 组件的使用需求时，可以不安装这些组件包，EasyAR 仍然可以在受支持的设备上正常工作。
## AR Foundation 支持
[AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest) 是 Unity 提供的 AR 开发框架，其 AR 功能通过底层系统或第三方实现，常用于支持 ARCore、ARKit 以及部分头显。
### EasyAR 与 AR Foundation 的关系
```
block
columns 6
block:groupApp:6
block:groupAppWrapper
space
App1["EasyAR<br>App"]
space
App2["EasyAR + AR Foundation<br>App"]
space
App3["AR Foundation<br>App"]
end
end
block:groupSensePlugin:4
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupAREngineInterop
columns 1
AREngineInterop["EasyAR<br>AR Engine Interop"]
space
end
block:groupSense:3
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
Image["Image<br>Tracker"]
Object["Sparse<br>SpatialMap"]
MotionTracker["Motion<br>Tracker"]
MARCore["ARCore"]
MARKit["ARKit"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:6
columns 1
System["System Library"]
block:groupSystemWrapper
space
AREngine["AR Engine<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
ARCore["ARCore<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
ARKit["ARKit<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePlugin --> App1
SensePlugin --> App2
ARF --> App2
ARF --> App3
groupSense --> SensePlugin
groupAREngineInterop --> SensePlugin
AREngine --> groupAREngineInterop
XRSubsystem --> ARF
XRSubsystem --> XRI
ARCore --> MARCore
ARKit --> MARKit
ARCore --> XRSDK
ARKit --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style AREngineInterop fill:none,stroke:none,stroke-width:0px,color:#fff
style Sense fill:none,stroke:none,stroke-width:0px,color:#fff
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px,color:#fff
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class groupAREngineInterop EasyAR
class groupSense EasyAR
class SensePlugin EasyAR
classDef Unity fill:#636,stroke:#333,color:#fff
class groupXRSubsystem Unity
class ARF Unity
class XRI Unity
```
EasyAR 与 AR Foundation 是两个独立的 AR 框架，EasyAR 并不依赖 AR Foundation 来实现其 AR 功能。EasyAR 也可以通过系统中的 ARKit、ARCore 等系统库来实现运动跟踪能力。同时，EasyAR 还提供了 AR Foundation 所不具备的两种运动跟踪实现：EasyAR 自身的运动跟踪实现以及通过 AR Engine 提供的运动跟踪实现，从而提供了相比 AR Foundation 更加广泛的设备支持。
同时，EasyAR 可以获取 AR Foundation 运行时的数据，在 AR Foundation 运行时利用它所提供的运动跟踪能力驱动其它 AR 功能运行，从而提供对 AR Foundation 的兼容性。这些功能包括：
* Mega
* 稀疏空间地图
* 稠密空间地图
* 使用运动融合的图像跟踪和物体跟踪
可以参考 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 了解更详细的运动跟踪与 EasyAR 功能的关系。
### 什么情况下需要使用 AR Foundation
多数情况下，可以不使用 AR Foundation，EasyAR 会在比 AR Foundation 所支持的更加广泛的设备上正常工作。通常在以下两种情况下可以考虑使用 AR Foundation：
1. 需要使用 EasyAR 未封装的 ARKit 及 ARCore 功能
如果需要使用的 ARCore 或 ARKit 提供的一些功能在 EasyAR 中未封装，可以使用 AR Foundation。比如 AR Foundation 提供了对 ARKit 人脸跟踪的支持 [ARFaceManager](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARFaceManager.html)，EasyAR 并没有封装这个功能。
2. 在部分系统存在问题的小米手机上使用 ARCore 而非 EasyAR 实现的运动跟踪
如果需要在所有支持 ARCore 的小米和红米手机上使用 ARCore，可以考虑启用 AR Foundation。由于部分小米和红米手机系统存在问题，EasyAR 的 ARCore 封装不支持这些设备，包括米 9、米 10、红米 K20、红米 K30、红米 K40 等系列（这里列出的不全，设备支持会持续更新）。在这些手机上，默认配置下将不会使用 ARCore，在支持 EasyAR 运动跟踪的手机上会使用EasyAR 运动跟踪。
使用 AR Foundation 时 EasyAR 的功能效果并不是最优的。存在两种情况：
1. 在 EasyAR 不直接支持的那部分小米和红米手机上，输入 EasyAR 的数据是灰度图而非彩色图，这会影响部分算法的效果。由于设备自身问题，这是无法通过配置解决的。
2. 在使用 Mega 时，AR Foundation 默认使用的配置并不是最优的。
> **小心**
可以通过修改 AR Foundation 的 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 来获取更优的数据输入，启用 [ARCoreARFoundationFrameSource.OptimizeConfigurationForTracking](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html#u_easyar_ARCoreARFoundationFrameSource_OptimizeConfigurationForTracking) 可以自动完成最佳 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 选择。但需要注意部分手机自身（比如小米 10）存在问题，在修改配置之后无法获取图像，EasyAR 将无法使用（应用有图像背景但 EasyAR 功能没有任何反应），因此通常并不建议启用，如需使用需要做好 EasyAR 无法使用时的降级方案。
## 头显支持
由于 Unity XR 框架未提供足够充分的数据接口，因此 EasyAR 并不通过 Unity XR 框架来支持头显。
在支持 Unity XR 框架的头显上，EasyAR 会通过 **XR Core Utilities** 支持 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 的使用，但并不使用 Unity XR 框架来实现头显的支持。EasyAR 不会影响 **XR Interaction Toolkit** 的功能，只要设备支持就可以正常使用。
一般来说，头显厂商各自提供了 SDK 或系统接口来提供这些数据，EasyAR 通过系统接口以及厂商的 SDK 来支持头显。有些时候这些 SDK 并不是完全公开的，EasyAR 会与厂商合作提供完整支持。[Unity 中的头显支持](../headsets/headsets.html) 介绍了 EasyAR 支持的头显及其使用方法。
## 后续步骤
* 了解如何 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html)
* 了解 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html)
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)
* [Unity 中的头显支持](../headsets/headsets.html)
1. Unity 6 及更新版本中，最低支持 2.0.4。Unity 2022.3 中，最低支持 1.2.3，不支持 1.3.x。[↩](#fnref:1)[↩](#fnref:2)
