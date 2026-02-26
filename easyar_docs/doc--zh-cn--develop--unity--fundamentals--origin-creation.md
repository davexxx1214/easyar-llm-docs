---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/origin-creation.html
original_file: doc--zh-cn--develop--unity--fundamentals--origin-creation.md
normalized_at: 2026-02-27
---
# 创建 XR Origin
通过以下内容，您将了解如何在 Unity 场景中创建和配置 XR Origin 以及 XR Origin Child。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [XR Origin](origin.html) 了解 XR Origin 的基本概念、组成和生命周期。
## 创建 XR Origin (EasyAR)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin (EasyAR)` 可以创建一个完整 origin 结构。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-creation.png)
在脚本中，可以使用 [ARSessionFactory.CreateOrigin()](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateOrigin) 创建：
```
ARSessionFactory.CreateOrigin();
```
> **注意**
session 运行时，如果场景中没有正确的 XR Origin 结构，XR Origin 和一个 XR Origin Child 会被自动创建。
## [可选] 创建 XR Origin (Unity XR)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` > `XR Origin (Mobile AR)` 可以创建适用于 AR Foundation 的 XR Origin。有关该 XR Origin 的详细信息和创建方法，请参考 Unity 官方文档：[添加 Unity XR 的 XR Origin 到场景](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin-setup.html)。
> **注意**
使用头显时，请务必参考对应头显 SDK 的文档进行操作。
在使用 Unity XR 框架提供的 XR Origin 时，需要手动添加 XR Origin Child。
## 添加 XR Origin Child 到 XR Origin
在 `Hierarchy` 视图中，选中 **XR Origin (EasyAR)** 或 **XR Origin** 并点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin Child` 可以添加 XR Origin Child 到 XR Origin 下。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-child-creation.png)
在脚本中，可以使用 [ARSessionFactory.AddOriginChild(GameObject)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddOriginChild_UnityEngine_GameObject_)：
```
ARSessionFactory.AddOriginChild(origin);
```
可以添加任意多个 XR Origin Child，它们都会正常工作。但是对于 session 内部生成的物体来说，只会使用第一个 XR Origin Child 作为父节点。
> **注意**
session 运行时，如果场景中没有正确的 XR Origin Child 结构，XR Origin Child 会被自动创建。
## 后续步骤
* 了解 XR Origin 的 [active 控制策略](active-control.html)
