---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/enable-headset.html
original_file: doc--zh-cn--develop--unity--headsets--enable-headset.md
normalized_at: 2026-02-27
---
# 在 EasyAR 项目中启用头显支持
本文档介绍了如何在一个已有的 EasyAR Unity 场景中启用头显支持。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
* 阅读 [Unity 中的 EasyAR 头显支持](headsets.html) 了解在 Unity 中 EasyAR 头显支持的整体架构。
本文假设您有一个已经可以使用 EasyAR 的场景。如果需要创建这样的场景，或是在一个头显场景中添加 EasyAR 组件，可以参考以下文档：
* [添加 AR Session](../fundamentals/session-creation.html)
* [配置 Camera](../fundamentals/camera-configs.html)
* [添加 XR Origin](../fundamentals/origin-creation.html)
## 在场景中添加头显组件
在场景中添加头显组件之前，通常需要移除现有的 Camera 和 XR Origin。
### 移除 Camera 和 XR Origin
删除场景中现有的 Camera。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/del-camera.png)
如果场景里已经存在 `XR Origin`，无论它来自 EasyAR 还是 Unity XR 框架，大部分情况下需要将其删除。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/del-origin.png)
> **提示**
在一些高级的用法中，可以根据自己需要判断是否删除。
### 添加头显组件
遵循头显官方说明来添加头显的组件。这里以 Pico 头显为例，与官方说明冲突时以官方说明为准。
使用菜单添加一个 `XR Interaction Manager`：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-add-manager.png)
使用菜单添加一个 `XR Origin`：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-add-origin.png)
在运行之前，需要确保阅读头显官方说明来了解一个有头显 SDK 的场景应该如何进行配置和运行。
## 配置 frame source
### 内置支持的设备
选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Head Mounted Display (Built-in)` > `Frame Source : [Name] (keep it only)` 创建 [Name] 的 frame source 并仅保留它。
比如，为 Apple Vision Pro 配置 frame source：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/visionpro-frame-source-add.png)
操作之后 session 中的 frame source 会变成这样：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/visionpro-frame-source.png)
> **提示**
如果 session 中包含设备对应的 frame srouce 并且在设备上是第一个可用的 frame source（比如上图中，在 visionOS 系统中 VisionOS ARKit 就是第一个可用的 frame source），可以不修改。部分菜单创建的默认 session 就属于这种情况。
### 扩展支持的设备
选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Extensions` > `Frame Source : [Name] (keep it only)` 创建 [Name] 的 frame source 并仅保留它。
比如，为 Pico 头显配置 frame source：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-frame-source-add.png)
操作之后 session 中的 frame source 会变成这样：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-frame-source.png)
### 跨设备支持
如果需要场景可以在不同设备上运行，需要保留其它 frame source，并确保在设备当前 frame source 可以被选中。
使用不含 `(keep it only)` 的菜单项可以只添加 frame source 且不删除其它 frame source，比如 `EasyAR Sense` > `Extensions` > `Frame Source : Pico` 将在 session 所有 frame source 最后创建适用于 Pico 的 frame source。一般来说，通过这个方式添加完 frame source 之后，还需要将它移动到合适的位置。
> **提示**
在一些高级的用法中，可以根据自己需要调整 frame source 的位置，也可以在代码中修改。
## 后续步骤
* [Vision Pro 工程配置](setup-visionpro.html)
* [XREAL 工程配置](setup-xreal.html)
* [其它 Android 设备工程配置](../fundamentals/setup-player.html)
## 相关主题
* [帧数据源及运行时选取](../cameras/frame-source.html)
