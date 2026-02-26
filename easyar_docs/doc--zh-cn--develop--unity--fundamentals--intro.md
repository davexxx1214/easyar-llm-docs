---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/intro.html
---

AR 驱动的 Unity 应用基础 | EasyAR 文档
**
##### Table of Contents
**
# AR 驱动的 Unity 应用基础
EasyAR Sense Unity 插件包提供了在 Unity 中开发 AR 应用的基础功能。本文介绍了在 Unity 中开发 AR 应用时需要了解的基础知识和组件。
## 开始之前
* 了解 [AR 驱动的 3D 渲染](../../fundamentals/fundamentals.html)。
## Unity AR 应用开发基础
首先，您需要通过以下内容了解 EasyAR 兼容哪些 Unity 版本及平台：
* [Unity 兼容性](unity-compatibility.html)
在 Unity 中，AR 应用的典型流程与 [一般 AR 应用](../../fundamentals/fundamentals.html) 类似，但通过 AR Session 组件来管理摄像头数据的获取、跟踪器的运行以及虚拟内容的渲染。
```
`flowchart TD
subgraph AR
CameraDevice[Camera Device]
Tracker[Tracker]
Renderer[Renderer]
CameraDevice --&gt;|Image Frame| Tracker
Tracker --&gt;|Image Frame + Tracked Pose| Renderer
end
subgraph unity["Unity AR"]
B[Session]
C([Camera])
O([Origin])
T([Target])
B -- transform --&gt; C
B -- transform --&gt; O
B -- transform --&gt; T
classDef Unity fill:#6e6ce6,stroke:#333,color:#fff
class B Unity
class C Unity
class O Unity
class T Unity
end
CameraDevice -..- B
Tracker -..- B
Renderer -..- C
Renderer -..- O
Renderer -..- T
`
```
您将从以下这些基础组件开始，逐步了解 Unity 中 AR 应用的基础知识：
* [AR Session](session.html)
* [Camera](camera.html)
* [XR Origin](origin.html)
* [Target](target.html)
然后，您需要了解**中心模式**，这是理解 EasyAR 对 Unity 组件行为控制的关键概念：
* [中心模式](center-mode.html)
如果您有 Unity XR 框架（比如 AR Foundation）的使用经验，您可能会希望了解怎样在开发 EasyAR 应用时使用这些功能：
* [Unity XR 框架](unity-xr.html)
* [AR Foundation](arfoundation.html)
如果您已经在 Unity 编辑器内完成了 AR 开发，您可能会希望在打包发布前了解如何配置 Unity 项目以便在目标设备上运行：
* [Player 配置](setup-player.html)
* [EasyAR 配置](setup-easyar.html)
结合上面这些基础知识，您可以参考以下工作流程示例，实践您所学到的内容：
* [Workflow\_ARSession 示例](sample-arsession.html)
## 后续步骤
在掌握了 Unity AR 应用开发的基础知识后，您仍需继续了解更多 AR 开发所需的功能和组件：
* 了解 [帧数据源（Frame Source）](../cameras/frame-source.html)
* 了解 [Unity AR 模拟运行](../simulation/simulation.html) 并在开发过程中多加利用
* 了解 [诊断功能](../diagnostics/diagnostics.html) 并在开发过程中多加利用
如果您需要在头显设备上运行 EasyAR 应用，您还需要：
* 了解 [XR 头显](../headsets/headsets.html) 的使用