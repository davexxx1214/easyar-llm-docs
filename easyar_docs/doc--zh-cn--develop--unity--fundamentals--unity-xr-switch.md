---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-xr-switch.html
---

在 Unity 场景中自动切换 Unity XR 物体 | EasyAR 文档
**
##### Table of Contents
**
# 在 Unity 场景中自动切换 Unity XR 物体
Unity 的 XR 组件（包括 AR Foundation）所能支持的设备有限。为了在受支持的设备上使用 AR Foundation，同时又能在其它大量设备上使用 AR 功能，EasyAR 提供了自动切换 Unity XR 物体的功能。以下内容介绍该功能对场景物体的改动及使用方法。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
* 确保场景已按 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html) 所描述，添加了 AR Foundation 的 [ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html) 及 [XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html)。
## 功能介绍
由于 Unity 的 AR Foundation 在手机上底层实现是 ARCore 和 ARKit，只能在有限的设备上使用，尤其是在很多国产 Android 手机上无法使用，所以通常建议仅在受支持的设备上启用 AR Foundation 及相关功能脚本。自动切换 Unity XR 物体的功能实现了上述操作，主要为移动 AR 设计，头显上默认配置下功能会被禁用。
在完整功能启用时，
* 编辑器中，[easyar.ARSession](../../../api/unity/easyar.ARSession.html) 会禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)
* 运行时，[easyar.ARSession](../../../api/unity/easyar.ARSession.html) 会在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 时禁用所有 Unity XR Core 组件及 AR Foundation 的组件。
* 运行时，如果被选择的 [FrameSource](../../../api/unity/easyar.FrameSource.html) 继承自 [ARFoundationFrameSource](../../../api/unity/easyar.ARFoundationFrameSource.html) 或是实现了 [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin) 原点的 [ExternalDeviceFrameSource](../../../api/unity/easyar.ExternalDeviceFrameSource.html)，则被禁用的 Unity XR Core 组件及 AR Foundation 组件将在 [easyar.ARSession.StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 时启用（未被 EasyAR 禁用的不会启用）。如果其他 [FrameSource](../../../api/unity/easyar.FrameSource.html) 被选择，则在 [easyar.ARSession.StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 时会禁用所有 Unity XR Core 组件及 AR Foundation 的组件。
* 运行时，所有 Unity XR Core 组件及 AR Foundation 的组件会在 [easyar.ARSession.StopSession(bool)](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StopSession_System_Boolean_) 时禁用。
默认配置下，功能启用条件如下，
* 在 Windows/Mac 上启用。
* 切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。
* 切换器启动时，如果存在移动AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。
##### 注意
XR Interaction Toolkit 的组件不受该功能控制，但其在 EasyAR 中是否可用未经验证。理论上对于只使用 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) GameObject 及其 Camera 的功能应该可以正常使用。如果行为异常可以尝试设置 [ARSession.ARCenterMode](../../../api/unity/easyar.ARSession.ARCenterMode.html) 为 [ARSession.ARCenterMode.SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)。如果功能还是不正常，则需要实现自定义的 XR Interaction Toolkit 的组件控制，在 [FrameSource](../../../api/unity/easyar.FrameSource.html) 不是继承自 [ARFoundationFrameSource](../../../api/unity/easyar.ARFoundationFrameSource.html) 时禁用相关组件。
## 配置方法
这个功能可以通过 `Project Settings` &gt; `EasyAR` &gt; `Sense` 中的 `Unity XR` &gt; `Unity XR Auto Switch` 中的选项启用或关闭。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/xr-auto-switch.png)
图中选项配置功能行为如下：
* **Editor**：编辑模式选项
* **Disable AR Session**：存在 [easyar.ARSession](../../../api/unity/easyar.ARSession.html) 时，编辑时禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)。
* **Player**：运行模式选项
* **Enable**：启用运行时控制。注意：关闭该选项时编辑模式被禁用的组件在运行时不会被恢复。
* **Enable If Desktop**：在 Windows/Mac 上启用。
* **Enable If Mobile AR On Startup**：切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。通常这个选项需要 `Project Settings` &gt; `XR Plug-in Management` 中的 `Initialize XR on Startup` 是选中的。
* **Disable If Non Mobile AR Post Startup**：切换器启动时，如果存在移动AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。通常这个选项会在 `Project Settings` &gt; `XR Plug-in Management` 中的 `Initialize XR on Startup` 未选中时被使用。
* **Restore AR Session When Disabled**：功能禁用时，恢复（启用）所有被禁用的 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)（无论它是否由 EasyAR 所禁用）。这个选项通常用于恢复编辑时被禁用的组件。
## 使用自定义的控制方法
如果需要自定义这些组件的切换，或是 EasyAR 的行为干扰了某些组件的正常工作，需要确保关闭这些选项，同时根据以下基本规则自定义组件切换：
1. 在编辑器中禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)（它在执行时序中早于所有其它脚本）
2. 在 AR Foundation 开始工作前禁用所有 Unity XR Core 组件及 AR Foundation 的组件以及需要控制的相关组件或功能
3. 如果 [easyar.ARSession.Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 过程中选择了 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 或 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)，启用之前禁用的所有组件或功能，需要在 [StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 完成前完成，通常建议在 [easyar.ARSession.AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件响应中完成
4. 如果 [easyar.ARSession.Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 过程中选择使用了其它 [FrameSource](../../../api/unity/easyar.FrameSource.html)，则保持不变
## 相关主题
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)