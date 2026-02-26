---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/setup-visionpro.html
---

如何在 Apple Vision Pro 上使用 EasyAR 能力 | EasyAR 文档
**
##### Table of Contents
**
# 如何在 Apple Vision Pro 上使用 EasyAR 能力
本指南将引导您完成 Unity 与 Xcode 的工程配置，为 Apple Vision Pro 应用解锁包括 Mega 云定位在内的全部 EasyAR 核心能力。
## 开始之前
* 学习如何使用[头显样例](samples.html)
* 确保开发环境符合以下要求：
* visionOS 2.0 及以上
* 对应 visionOS 版本的 Xcode 16.0 及以上并安装 visionOS simulator
* 推荐的 Unity 版本 6000.0.23 以上的 LTS 版本
## 向 Apple Inc. 申请企业级 API 许可
由于在 Apple Vision Pro 上获取相机画面及参数是一个需要 **entitlement** 的 **企业级 API**，您需要向 **Apple Inc.** 申请包含该 **entitlement** 的 **license** 文件。该 license 的申请和使用方式请参考 [Building spatial experiences for business apps with enterprise APIs for visionOS](https://developer.apple.com/documentation/visionos/building-spatial-experiences-for-business-apps-with-enterprise-apis)。
##### 重要事项
向苹果公司申请得到的 **entitlement** 中的 **Bundle ID** 应与创建 **EasyAR Sense License Key** 时填写的完全一致。
## 如何选择 visionOS App Mode
运行在 visionOS 上的 App 仅在 **Immersive Space** 下能够获取 ARKit 数据。而 Unity 编辑器打包的 App 在 **Immersive Space** 下基于渲染流程及 API 不同需要选择使用 **RealityKit with PolySpatial** 或 **Metal Rendering with Compositor Services** 模式。
关于 **Immersive Space** 的定义,可以参考苹果[官方文档](https://developer.apple.com/documentation/swiftui/immersive-spaces)。
关于 Unity 的 App Mode 的详细介绍，可以参考 Unity PolySpatial 文档中的 [visionOS Platform Overview](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/visionOSPlatformOverview.html)。
##### 提示
**App Mode 选择建议**
* **首选推荐：RealityKit with PolySpatial**
如果您是首次接触 visionOS，建议优先选择此模式。其优势在于能深度集成 visionOS 的系统级渲染特性，稳定性高，渲染效果好。
此模式不支持自定义代码着色器（HLSL/ShaderLab），必须使用 **Shader Graph**，且仅支持经 PolySpatial 兼容性检查后的特性（会被转换为 MaterialX）。
Unity 内置的 `Standard (Built-in)` 和 `Lit (URP)` 着色器已由官方预先适配，可直接使用。
* **进阶/特定需求：Metal Rendering with Compositor Services**
适用于有大量现有 3D 资产迁移需求或必须使用自定义着色器的复杂项目。
由于该模式下 Unity 负责全部渲染逻辑，绕过了系统的 RealityKit 管线，渲染效果一般不如 RealityKit 并且可能会遇到不可预见的渲染问题。
**EasyAR 接入建议：**
在尝试接入 EasyAR 时，请务必先使用 **RealityKit with PolySpatial** 模式跑通基础流程。这样可以有效隔离变量，避免因 Metal 底层适配问题与 AR 相关问题交织，从而导致难以定位故障成因。
## Unity 工程中的配置
Unity 工程中需要进行以下配置：
### 为 Unity 工程导入必要的 Package
**Unity 6 （推荐）**：
* `com.unity.xr.visionos` (2.0.4+)
* `com.unity.polyspatial` (2.0.4+)
* `com.unity.polyspatial.visionos` (2.0.4+)
* `com.unity.xr.visionos` (2.0.4+)
##### 重要事项
所有 Package 的版本号必须保持严格一致。
建议优先使用 Unity 6，部分早期的 Unity 2023.x 版本对 visionOS 尚不支持。
**Unity 2022.3**：
* `com.unity.xr.visionos` (1.2.3)
* `com.unity.polyspatial` (1.2.3)
* `com.unity.polyspatial.visionos` (1.2.3)
* `com.unity.xr.visionos` (1.2.3)
##### 重要事项
所有 Package 版本号必须保持严格一致。
不支持 **1.3.x** 版本，请务必锁定在 **1.2.3**。
### 选择 Build Platform
点击菜单栏中的 **File** &gt; **Build Profiles** 将 Platform 切换至 **visionOS**。
![切换Build_Platform](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro01.png)
### 配置 Input System
确保使用新版的 `Input System Package`：
点击菜单栏中的 **Edit** &gt; **Project Settings** &gt; **Player**，将 **Active Input Handling** 槽设置为 **Input System Package(New)**。
此后 Unity 可能会要求重启工程，点击 **Apply** 使改动生效。
![InputSystem改动生效](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro02.png)
### 配置 XR Plug-in Management
点击菜单栏中的 **Edit** &gt; **Project Settings** &gt; **XR Plug-in Management**，在 visionOS 选项卡中的 Plug-in Providers 勾选 **Apple visionOS**。
![选择visionOS插件](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro03.png)
### 配置 Apple visionOS 插件
点击菜单栏中的 **Edit** &gt; **Project Settings** &gt; **XR Plug-in Management** &gt; **Apple visionOS**。
根据[前文介绍](#setup-visionpro-how-to-choose-app-mode)选择合适的 **App Mode**。
![选择AppMode](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro04.png)
##### 注意
**Windowed** 模式由于不是运行于 **Immersive Space**，无法使用 AR 能力。
**Hybrid** 模式指开发者需要手动在 **Metal** 和 **RealityKit** 模式间切换，由于使用方式比较复杂，不推荐使用，具体可以参考 [Unity 官方对该模式的说明](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/PolySpatialHybridApps.html)。
接下来在同页面中进行以下修改：
* 在 **World Sensing Usage Description** 槽中添加一段描述。
* 将 **Metal Immersion Style** 设置为 **Mixed**。
* 将 **Reality Kit Immersion Style** 设置为 **Mixed**。
* 勾选 **IL2CPP Large Exe Workaround**。
![修改visionOS插件配置](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro05.png)
### [仅 RealityKit 模式需要] 导入 TextMesh Pro Essentials
点击菜单栏中的 **Edit** &gt; **Project Settings** &gt; **TextMesh Pro** &gt; 点击 **Import TMP Essentials**
![Import TMP Essentials](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro09.png)
##### 注意
目前 **RealityKit with PolySpatial** 模式仅支持 **TextMesh Pro** 文字，若不导入则无法渲染文字。
### [仅 RealityKit 模式需要] PolySpatial 相关设置
点击菜单栏中的 **Edit** &gt; **Project Settings** &gt; **PolySpatial**，在该页面中进行以下修改：
* 设置 **Default Volume Camera Window Config** 为 `Default Unbounded Configuration`。
* 勾选 **Auto-Create Volume Camera**
![设置 PolySpatial](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro06.png)
如果需要另外指定 **Default Volume Camera Window Config**，必须确保其 **Mode** 为 **Unbounded**。
![确认 Mode 是 Unbounded](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro07.png)
场景中如果存在 `Volume Camera`，将其删除。
![删除场景中的 Volume Camera](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro08.png)
##### 警告
* **不支持** `World Transform` 数值不是 `identity` 的 `Volume Camera`。
* 若因**特殊原因**需要在场景中添加一个**唯一**的自定义 `Volume Camera`，请务必：
* 将其 `World Transform` 设为 `identity`。
* 确保其 `Volume Camera Window Configuration` 的 `Mode` 设置为 `Unbounded`。
* 在完全清楚 [Unity 官方文档](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/VolumeCamera.html)中其含义和用途的前提下使用。
### [使用 Mega 时]添加 Location Usage Description
##### 小心
若在 EasyAR 配置中启用了 **Location** 权限（使用 Mega 功能时），必须添加权限描述信息，否则 Build 将失败。
由于目前 Unity 的 **Project Settings** &gt; **Player** &gt; **visionOS** 选项卡中未显示 **Location Usage Description** 字段，请按照以下步骤配置：
1. **切换平台标签**：将选项卡暂时切换至 **iOS**。
2. **填入描述**：在 **Location Usage Description** 槽位中填入必要的权限用途说明。
3. **切回 visionOS**：将选项卡切回 **visionOS**，刚才填写的配置会自动保留并生效。
![Location Description](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro10.png)
## Xcode 工程中的配置
通过 Unity 打包得到的 Xcode 工程中需要进行以下配置：
### 配置相机数据 entitlement
* 将申请得到的 `Enterprise.license` 文件复制到 Xcode 工程文件目录。
![Copy to Xcode project folder](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro11.png)
* 将 Xcode 工程文件目录中的 `Enterprise.license` 拖入 Xcode 工程中。
![Move into Xcode project](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro12.png)
### 修改 info.plist 使应用能够保存和投送文件
若需要在应用中录制 EIF 并通过 visionOS 的文件应用投送到电脑或其他设备，需要在 `Info.plist` 中增加以下字段并修改：
* 添加 `LSSupportsOpeningDocumentsInPlace` 并将值设置为 `true`。
* 添加 `UIFileSharingEnabled` 并将值设置为 `true`。
![Modify Info.plist](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro13.png)
##### 提示
添加字段后 Xcode 界面上显示的 `Key` 与手动添加的字符串不同（比如输入了 `LSSupportsOpeningDocumentsInPlace` 但显示 **Supports opening documents in place**，这是正常的）。