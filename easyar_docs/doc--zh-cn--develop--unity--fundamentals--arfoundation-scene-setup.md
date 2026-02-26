---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/arfoundation-scene-setup.html
---

EasyAR 项目中的 AR Foundation 场景配置和用法 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR 项目中的 AR Foundation 场景配置和用法
在 Unity 中使用 AR Foundation 往往需要依靠 EasyAR 解决 AR Foundation 的设备局限性。以下内容介绍如何在 EasyAR 场景中正确配置和使用 AR Foundation，以及如何根据设备支持情况动态启用 AR Foundation。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
* 阅读 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html) 了解如何在 EasyAR 项目中安装和配置 AR Foundation。
## 添加 AR Foundation 组件
在 EasyAR 场景中添加 AR Foundation 的 AR Session 和 XR Origin。
### 添加 AR Session
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` &gt; `AR Session` 添加 Unity 的 [ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html) 到场景中。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session.png)
##### 注意
这个 AR Session 与 EasyAR 的 AR Session 不同，它们需要同时存在于场景中。
### 添加 XR Origin
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` &gt; `XR Origin (Mobile AR)` 添加 Unity 的 [XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 到场景中。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-origin.png)
##### 注意
这个 XR Origin 与 EasyAR 的 XR Origin 功能是重叠的，需要使用 Unity XR Origin 而非 EasyAR 的 XR Origin。
如果场景中之前存在 EasyAR 的 XR Origin，一般名称为 `XR Origin (EasyAR)`，需要将其下面的子物体移动到新创建的 XR Origin 下面，然后将 `XR Origin (EasyAR)` 删除。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-remove-origin.png)
这时候，如果新创建的 XR Origin 下面没有 XR Origin Child，需要手动添加。
在 `Hierarchy` 视图中，选中 **XR Origin** 并点击右键，通过菜单 `EasyAR Sense` &gt; `Origin` &gt; `Origin : XR Origin Child` 添加 XR Origin Child 到 XR Origin 下。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-child-creation.png)
### 配置 Camera
如果场景中之前存在 AR 用的 `Camera`，会发现场景中出现了多余的主摄像机，需要将原本的摄像机删除。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-remove-camera.png)
然后选中 XR Origin 下的 `Main Camera`，按照 [Camera 配置](camera-configs.html) 的说明对摄像机进行配置。
最后，一个完整的添加了 AR Foundation 的 EasyAR 场景结构应该类似下面这样：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/)
##### 小心
如果需要通过 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 修改 AR Foundation 的配置，需要注意部分手机自身（比如小米 10）存在问题，在修改配置之后无法获取图像，EasyAR 将无法使用（应用有图像背景但 EasyAR 功能没有任何反应），因此通常并不建议修改，如需修改需要做好 EasyAR 无法使用时的降级方案。
## 设备兼容与动态启用 AR Foundation
EasyAR 兼容的设备比 AR Foundation 多很多，因此需要配置以确保应用只在需要时启用 AR Foundation，其余情况需要完全关闭 AR Foundation。
### 检查 frame source 组件
一般来说，通过 EasyAR 菜单创建的 session 通常会自动添加 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 以及 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) （部分图像跟踪等不需要SLAM功能的除外）。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/.png)
##### 重要事项
[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 以及 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) 是 EasyAR 提供的 frame source，用于在支持 AR Foundation 的设备上启用 AR Foundation 功能。如果场景中的 session 不包含这些 frame source，则无法在启用 AR Foundation 功能。
如果场景中的 session 不包含这些 frame source，可以通过菜单手动添加。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-frame-source-creation.png)
为了在不支持 AR Foundation 的手机上运行，还需要确保 session 包含 AR Foundation 以外的 frame source。一个典型的ARSession 应该类似下面这样，
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-easyar.png)
##### 提示
可以根据实际需要对 frame source 进行排序，在应用运行时，session 会根据设备支持情况按 transform 顺序选择第一个可用的 frame source。
### 仅在需要时启用 AR Foundation
由于 AR Foundation 在手机上底层实现是 ARCore 和 ARKit，只能在有限的设备上使用，尤其是在很多国产 Android 手机上无法使用，所以通常建议仅在受支持的设备上启用 AR Foundation 及相关功能脚本。
EasyAR 可以自动完成这些操作，该功能可以通过 在 `Project Settings` &gt; `EasyAR` &gt; `Sense` 中的 `Unity XR` &gt; `Unity XR Auto Switch` 选项启用或关闭。详细说明可以参考 [自动切换 Unity XR 物体](unity-xr-switch.html) 。
## 保留 AR Foundation 兼容性的场景
正确添加了 AR Foundation 组件的场景可以在 AR Foundation 包安装或未安装时都正常工作。
未安装 AR Foundation 时 AR Foundation 的功能及对应 frame source 不可用，且场景中会有部分脚本缺失，属于正常情况。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-missing-scripts.png)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-missing-origin.png)
##### 提示
很多 sample 都可以在 AR Foundation 包安装或未安装时都正常工作。如果需要在这些 sample 中启用 AR Foundation 支持，仅需 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html) 即可。
## 后续步骤
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* 文中提到的相关 AR 组件：
* [ARSession](session.html)
* [XR Origin](origin.html)
* [Camera](camera.html)
* AR Foundation 提供了部分设备上的运动跟踪能力，关于运动跟踪和各个 EasyAR 功能的关系，可以参考以下内容：
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)
* 有关 AR Foundation 场景配置的更多信息可以阅读 AR Foundation 官方文档，阅读前注意选择对应的文档版本：
* [场景配置](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/project-setup/scene-setup.html)
* [XR Origin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin-setup.html)