---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension.html
---

EasyAR Unity 头显扩展包 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR Unity 头显扩展包
本文档介绍了 EasyAR Unity 头显扩展包的概念、能力边界以及创建头显扩展包所需的背景知识。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
* 阅读 [Unity 中的 EasyAR 头显支持](headsets.html) 了解在 Unity 中 EasyAR 头显支持的整体架构。
## EasyAR Unity 头显扩展包是什么
EasyAR Unity 头显扩展包是一个 Unity package，包含一系列代码和示例，帮助您在您的头显设备上使用 EasyAR Sense 的功能。通过这个扩展包，您可以将 EasyAR Sense 的大部分功能（如图像跟踪、稠密空间地图等）集成到您的设备上，从而利用 EasyAR 提供的强大 AR 功能。
使用 EasyAR Unity 头显扩展包是 EasyAR 头显支持的其中一种方式。下图展示了 EasyAR 在 Unity 中的整体架构，以及头显扩展包在其中的位置。
```
`block
columns 4
block:groupApp:4
block:groupAppWrapper
space
App1["EasyAR + Device A&lt;br&gt;App"]
space
App2["EasyAR&lt;br&gt;App"]
space
App3["EasyAR + Device B&lt;br&gt;App"]
end
end
block:groupSensePluginExtension
columns 1
SensePluginExtension["EasyAR Sense Unity Plugin&lt;br&gt;Extension for Device A"]
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
DeviceAUnity["Device A&lt;br&gt;Unity SDK"]
space
end
block:groupSense
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
MDeviceB["Device B&lt;br&gt;CameraDevice"]
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
DeviceA["Device A&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;Library&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"]
space
space
DeviceB["Device B&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;Library&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"]
space
end
end
SensePluginExtension --&gt; App1
SensePlugin --&gt; App1
SensePlugin --&gt; App2
SensePlugin --&gt; App3
ARF --&gt; App3
XRI --&gt; App1
XRI --&gt; App3
groupSense --&gt; SensePlugin
groupDeviceAUnity --&gt; SensePluginExtension
SensePlugin --&gt; SensePluginExtension
DeviceA --&gt; groupDeviceAUnity
DeviceA --&gt; XRSDK
XRSubsystem --&gt; ARF
XRSubsystem --&gt; XRI
DeviceB --&gt; MDeviceB
DeviceB --&gt; XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style DeviceAUnity fill:none,stroke:none,stroke-width:0px
style Sense fill:none,stroke:none,stroke-width:0px,color
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePluginExtension fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class SensePluginExtension EasyAR
`
```
图中列出了两种典型的头显支持方式：通过 Unity 头显扩展包对接设备 SDK（Device A），以及在 EasyAR Sense 库中直接对接设备 SDK（Device B）。本文档主要介绍前者。
## 我可以创建自己的头显扩展包吗？
目前，AR/VR/MR/XR 行业内还没有形成非常统一的接口方案，虽然 OpenXR 是个很好的候选，但规范演化和行业实现还需要时间。所以通常来说市贩设备直接运行 EasyAR 并不那么容易，大概率存在数据接口缺失的情况。随着行业的发展，一些新兴设备也可能具备良好的接口支持，比如 2024 年苹果公司开放了 Vision Pro 的相关接口，这些接口已经足够用来支撑 EasyAR 运行，不过使用起来还是需要一些专业知识。
如果您无法做出判断，建议联系硬件制造商或 EasyAR 商务以获取相应的设备支持。
如果您是硬件制造商，并且希望在您的设备上支持 EasyAR 的功能，您可以参考接下来的文档内容来创建一个头显扩展包，从而让 EasyAR 的大部分功能可以在您的设备上运行。本文档在提供数据和接口规范的同时并不限定所有实现细节，任何实现方式或接口定义都可以讨论，欢迎通过商务渠道联系沟通。
本文档覆盖的硬件自身需要有运动跟踪或 SLAM 能力，EasyAR 的功能需要运行在良好的设备跟踪能力之上，通常不建议靠 EasyAR 的功能优化设备的跟踪，这会产生循环依赖进而理论上放大误差并导致整体系统趋于不稳。如果设备本身没有运动跟踪能力，那么支持方案并不在本文档覆盖范围之内，如有需要可通过商务渠道进行沟通。
## 头显扩展包的能力边界
头显扩展包的目标是让 EasyAR Sense 的大部分功能可以在您的设备上运行。为了实现这个目标，您需要了解头显扩展包的能力边界。
### 头显扩展包所包含的内容
您将实现的扩展是：
* 使用 [自定义相机功能](../../cameras/custom-camera.html)，从您的设备 API 抓取数据并发送进 `EasyAR Sense` 的一系列代码。
* 在 Unity 中，头显扩展会使用 [外部帧数据源](../cameras/external-frame-source.html) 和 `EasyAR Sense Unity Plugin` 定义的一套 `EasyAR Sense` 数据流来简化自定义相机开发。
* 在 Unity 中，头显扩展是一个 [Unity package](https://docs.unity3d.com/Manual/Packages.html)，包含运行时脚本，编辑器脚本和扩展的 sample，您或 EasyAR 可以将它分发给下游用户。
##### 提示
如果您不希望将对接细节暴露在外部系统中，可以联系 EasyAR 进行沟通。在 EasyAR Sense 内部使用 C 接口直接对接是可行且有先例的。
您在实现扩展的时候，可能会：
* 修改您 SDK 的**接口设计和内部实现**。
* 与您的**团队**一起讨论确认数据获取和使用方案。
* 花**大量**时间进行数据正确性验证而不是写代码。
完成扩展后，您将会看到：
* 大多数 `EasyAR Sense` 功能在您的设备上可以使用，这些功能会利用您设备的运动跟踪能力。
* `EasyAR Sense` 内支持的 EasyAR 云服务在您的设备上可以使用。
* 只能使用 EasyAR XR license。个人版、专业版以及经典版的 license 无法在您的设备上使用。
* 使用自定义相机时的所有 EasyAR license 的限制以相同方式适用于您的设备。
### 头显扩展包所不包含的内容
这个扩展不能脱离 `EasyAR Sense` 使用：
* 这个头显扩展不会独立运行，作为依赖，`EasyAR Sense` 也是需要的。在 Unity 中则必须使用 `EasyAR Sense Unity Plugin`。
* 它不会直接调用 EasyAR 云服务 API（比如 EasyAR Mega 定位服务），这些调用会在 `EasyAR Sense` 内部完成。
* 在 Unity 中，它不会直接调用 AR 功能（比如图像跟踪）的接口方法，它们在 `EasyAR Sense Unity Plugin` 内部完成。
* 在 Unity 中，它不会修改场景中物体或跟踪目标的 transform，它们在 `EasyAR Sense Unity Plugin` 内部完成。
这个扩展不能脱离您的设备 SDK 使用：
* 在 Unity 中，头显扩展或 `EasyAR Sense Unity Plugin` 不会修改场景中相机的 transform，这必须在您的设备 SDK 或其依赖路径中完成。
通过头显扩展有一些 EasyAR 功能仍是无法使用的：
* 表面跟踪功能将无法使用。
* EasyAR 自身的运动跟踪将无法使用。
* 平面检测（EasyAR 运动跟踪的一部分）将无法使用。
## 如何在我的设备上使用 Mega？
在设备上运行 Mega 是很多用户关心的问题。在 Unity 中，Mega 服务是运行在 `EasyAR Sense` 诸多基础功能之上的一个功能模块，所以只要您的设备完整支持 `EasyAR Sense`，那么 Mega 也会被支持。
一般来说，不建议在一开始就直接在设备上运行 Mega 示例来验证设备对 Mega 的支持情况，因为 Mega 会综合利用所有输入数据，并且其对这些数据的误差容忍度较大。直接运行 Mega 示例很可能会因为数据接口不匹配或数据质量不佳而导致无法获得合理的运行效果，并且无法判断问题出在哪里，这会为日后的调试带来很大困难。
##### 重要事项
Mega 服务对设备的运动跟踪能力有一定要求。如果设备的运动跟踪能力不佳，那么 Mega 的表现也会受到影响。在大范围 AR 场景中，还需要特别关注室内外的表现差异。
##### 重要事项
Mega 一般服务于大空间场景，因此需要格外关注远距离物体以及转动头部或移动时物体的 **显示** 效果。如果设备的显示系统误差较大，那么即使 Mega 本身运行正常，用户也会感觉虚拟物体无法正确贴合现实物体。
## 需要的背景知识和团队配置
创建头显扩展包不是一个简单的任务，需要您和您的团队在多个领域进行深入的工作。通常来说，要完成头显扩展，需要 Unity 开发参与的同时投入 Unity 开发之外的团队人员。由于缺少标准，只在 3D 引擎上面修改通常无法完成头显扩展，建议从第一天起就让系统工程师和 SDK 工程师等底层开发工程师参与进来。
打造 AR/VR 设备需要一些领域知识，相似地，在设备上运行和验证 EasyAR Sense 将需要您或您的团队是如下领域的专家：
* 您设备的物理结构和渲染系统
* 相机系统几何
* SDK 开发
* 常规 Android debug 技能，比如 adb（[中国大陆](https://developer.android.google.cn/tools/adb)，[国际](https://developer.android.com/tools/adb)）
如果您工作在 Unity 上，您还需要知道这些：
* [Unity 开发基础和 package 使用](https://docs.unity3d.com/Manual/Packages.html)
* [Unity package 开发](https://docs.unity3d.com/Manual/CustomPackages.html)
* C# 语言基础，包括 [IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable) 等
另外，有一点在这些领域的知识将帮助您更好地理解系统，尤其是如何发送正确的数据到 EasyAR：
* Android 开发（[中国大陆](https://developer.android.google.cn)，[国际](https://developer.android.com)）
* 几何视觉，尤其是图像匹配和 3D 重建
## 后续步骤
在接下来的文章中，您将了解创建头显扩展包的完整流程：
* [让头显支持 EasyAR](extension-imp.html) 介绍了如何使用模板来创建一个新的头显扩展包，并完成基本的输入扩展开发
* [运行验证（bring-up）](extension-bring-up.html) 介绍了如何在设备上验证输入扩展的正确性
* [发布扩展包](extension-dist.html) 介绍了如何将头显扩展包打包并分发给下游用户
## 相关主题
* [扩展包模板参考](extension-template.html)
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)