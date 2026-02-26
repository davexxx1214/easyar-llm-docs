---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/headsets.html
original_file: doc--zh-cn--develop--unity--headsets--headsets.md
normalized_at: 2026-02-27
---
# Unity 中的 EasyAR 头显支持
本文档介绍了在 Unity 中 EasyAR 头显支持的整体架构和注意事项。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
## 头显支持概述
EasyAR 在 Unity 中支持头显的方式比较灵活，常见有两种方式：
* 内置支持：通常在 EasyAR Sense 库中直接对接设备 SDK，并在 Unity 中提供对应的接口 （比如 Apple Vision Pro）
* 扩展支持：通过 Unity 头显扩展包对接设备 SDK （比如 Pico）
```
block
columns 4
block:groupApp:4
block:groupAppWrapper
space
App1["EasyAR + Device A<br>App"]
space
App2["EasyAR<br>App"]
space
App3["EasyAR + Device B<br>App"]
end
end
block:groupSensePluginExtension
columns 1
SensePluginExtension["EasyAR Sense Unity Plugin<br>Extension for Device A"]
space
end
block:groupSensePlugin
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupDeviceAUnity
columns 1
DeviceAUnity["Device A<br>Unity SDK"]
space
end
block:groupSense
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
MDeviceB["Device B<br>CameraDevice"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:4
columns 1
System["Native Library"]
block:groupSystemWrapper
space
DeviceA["Device A<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
space
DeviceB["Device B<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePluginExtension --> App1
SensePlugin --> App1
SensePlugin --> App2
SensePlugin --> App3
ARF --> App3
XRI --> App1
XRI --> App3
groupSense --> SensePlugin
groupDeviceAUnity --> SensePluginExtension
SensePlugin --> SensePluginExtension
DeviceA --> groupDeviceAUnity
DeviceA --> XRSDK
XRSubsystem --> ARF
XRSubsystem --> XRI
DeviceB --> MDeviceB
DeviceB --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style DeviceAUnity fill:none,stroke:none,stroke-width:0px,color:#fff
style Sense fill:none,stroke:none,stroke-width:0px,color:#fff
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px,color
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePluginExtension fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class groupSense EasyAR
class SensePlugin EasyAR
class SensePluginExtension EasyAR
classDef Device fill:#636,stroke:#333,color:#fff
class groupDeviceAUnity Device
class DeviceB Device
class DeviceA Device
```
>
> 图中：
>
>
> 设备 A 属于扩展支持
>
> 实践中设备 A 通常会有对应的 Unity SDK，用于对接 Unity XR SDK 或者独立实现头显渲染能力。
>
> 设备 A 的头显扩展包负责将 EasyAR Sense Unity Plugin 和设备 A 的 Unity SDK 对接起来，从而实现 EasyAR 在设备 A 上的运行。这个支持包可能由 EasyAR 提供，也可能由设备厂商提供。
>
>
> 设备 B 属于内置支持
>
> 实践中设备 B 可能有也可能没有对应的 Unity SDK，取决于设备厂商的实现。比如 Apple Vision Pro 没有对应的 Unity SDK，XREAL 有对应的 Unity SDK。
>
>
>
内置支持和扩展支持的头显都支持使用了 [自定义相机](../../cameras/custom-camera.html)。
> **重要事项**
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
在 Unity 中，虚拟摄像机的渲染、投影矩阵 和 transform 等不受 EasyAR 控制，它们通常由设备 SDK 或 Unity XR SDK 控制。设备自身的功能，比如手势识别、眼动追踪等，仍然由设备及设备 SDK 提供。在使用时，通常需要同时使用 EasyAR 和设备 SDK。
## 后续步骤
* [使用头显样例](samples.html)
* [启用头显支持](enable-headset.html)
* 工程配置
* [Vision Pro 工程配置](setup-visionpro.html)
* [XREAL 工程配置](setup-xreal.html)
* [其它 Android 设备工程配置](../fundamentals/setup-player.html)
* [创建 EasyAR 头显扩展包](extension-imp.html)
