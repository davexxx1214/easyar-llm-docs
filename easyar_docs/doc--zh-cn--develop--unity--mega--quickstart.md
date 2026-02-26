---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/quickstart.html
---

使用示例快速入门 EasyAR Mega Unity 开发 | EasyAR 文档
**
##### Table of Contents
**
# 使用示例快速入门 EasyAR Mega Unity 开发
本教程介绍如何配置并运行 EasyAR Mega Unity 示例，以快速入门 EasyAR Mega 开发。
## 开始之前
阅读本篇之前，需要确保您已完成：
* 有一个 [有效的云定位库](../../mega/localization-verify.html)。
* 安装 Unity（2021.3.30 LTS 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
* 按 [启用 Mega](enable-mega.html) 的方法导入 `com.easyar.sense-\*\*.tgz` 和 `com.easyar.mega-\*\*.tgz` 包。
## 示例使用方法（六步走）
下面将分六个步骤介绍如何配置并运行 EasyAR Mega 的核心示例 `MegaBlock\_Basic`。
### 第一步：导入示例
##### 注意
如果通过 `\*\*All Samples\*\*` 导入了全部示例，需要跳过此步骤。
1. 使用菜单 `Window` &gt; `Package Manager` 打开 Package Manager，选中 `EasyAR Sense Unity Plugin`, 在右侧的 **Samples** 中展开所有示例。
2. 选择示例（如 `MegaBlock\_Basic`），点击 **Import**。
![Import Sample](https://doc-asset.easyar.com/develop/unity/mega/media/sample-import.png)
##### 注意
* 本教程不能直接适用于头显设备，但在开发头显设备之前，需要使用手机开发了解流程。
* 如果您先前已经导入过旧版 SDK 的示例，在升级 SDK 之后需先删除旧示例再重新导入。
### 第二步：填写 License Key 并配置 Mega 云定位服务
1. 菜单栏选择 `EasyAR` &gt; `Sense` &gt; `Configuration`；
![License Guide](https://doc-asset.easyar.com/develop/unity/mega/media/fill-license-where.png)
2. 在打开的 **Project Settings** 面板中粘贴您的 License Key；
![Fill License](https://doc-asset.easyar.com/develop/unity/mega/media/fill-license-text.png)
##### 提示
EasyAR Sense License 可以从 [EasyAR 开发中心](https://www.easyar.cn/view/login.html) 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/mega/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `否`
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
##### 注意
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
1. 将您的 Mega 云定位库的各项信息配置到 **Project Settings** 面板中的 `Mega Block` 项；
![Mega Config Guide](https://doc-asset.easyar.com/develop/unity/mega/media/fill-mega-config-where.png)
##### 提示
Mega 云定位库配置可以从EasyAR开发中心获取。
![Mega Config Detail](https://doc-asset.easyar.com/develop/unity/mega/media/mega-config-detail.png)
确保您的 `API Key` 具有 `Mega Block` 的权限，如果没有需要进行更改或重新创建。
![API Key Auth](https://doc-asset.easyar.com/develop/unity/mega/media/check-apikey-auth.png)
### 第三步：摆放 3D 内容
1. 在 `Hierachy` 面板空白处右键点击，添加 Block 浏览工具（Unity 开发）；
![Add Block Viewer](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer.png)
2. 访问 Mega 定位服务；
1. 选中 `EasyAR.Mega.BlockViewer (Dev)` 节点，在 **Inspector** 面板中填写您的 EasyAR 账号信息并登录；
![login](https://doc-asset.easyar.com/develop/unity/mega/media/login.png)
2. 点击 Mega Cloud Service 右侧按钮；
![Click Mega CLS](https://doc-asset.easyar.com/develop/unity/mega/media/click-cls.png)
3. 选择您所要使用的 `Mega定位服务`，点击**确定**。
![Select Mega CLS](https://doc-asset.easyar.com/develop/unity/mega/media/select-cls.png)
4. 加载 Block
在选择服务之后，当前库中的 Block 列表会显示在 `MegaBlocks` 节点下，并显示在工具面板上。点击**加载**选择的Block：
![Load Block](https://doc-asset.easyar.com/develop/unity/mega/media/load-block.png)
加载完成后，Block 会显示在 `Scene` 窗口中。您可以在 `Scene` 窗口中操作，调整查看的视角、位置。同时检查下 Block 文件是否可用（比如 Block 坐标系是否正常，是否存在分层，是否过于模糊、存在缺损而无法找到位置摆放 AR 资源等）。
![Display Block](https://doc-asset.easyar.com/develop/unity/mega/media/block-in-scene.png)
5. 摆放 3D 内容
此时，您可以参考 Block 摆放 3D 物体。
![Place 3D Object](https://doc-asset.easyar.com/develop/unity/mega/media/annotate-in-block.png)
##### 注意
* 3D 物体必需摆放在工具自动生成的 `MegaBlocks` &gt; `Block\_\*` 节点之下，以确保在运行时虚拟内容的渲染位置是正确的。
* 请不要修改 `Block\_\*` 节点的名字和 `local transform`，它由工具自动管理。
### 第四步：配置 MegaTracker
1. 配置 **Block Root**；
展开 `AR Session` ，选择 `Mega Block Tracker` 并设置 `Block Root` 为工具生成的 `MegaBlocks` 节点。
![Set Block Root](https://doc-asset.easyar.com/develop/unity/mega/media/set-block-root.png)
### 第五步：修改 Player 配置
依次在 Unity 菜单 `File` &gt; `Build Settings` &gt; `Player Settings`，点击安卓图标，调出 Android 平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
* 修改 Package Name 为 License Key 页面显示的 Package Name
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
##### 提示
比如，如果您在创建 License Key 时填写的 Package Name 是 `com.mycompany.myproject`，则必须填写这里 Package Name 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 Minimum API Level 为 `API Level 21` 或更高版本
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* 修改 Scripting Backend 为 `IL2CPP`，并在 `Target Architecture` 中勾选 `ARM64`
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-64bit.png)
依次在 Unity 菜单 `File` &gt; `Build Settings` &gt; `Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
* 修改 Bundle ID 为 License Key 页面显示的 Bundle ID
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
##### 提示
比如，如果您在创建 License Key 时填写的 Bundle ID 是 `com.mycompany.myproject`，则必须填写这里 Bundle ID 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 `Architecture` 为 `ARM64`
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* 添加 `Camera Usage Description` 和 `Location Usage Description`，字符串内容可以随意填写，但必须添加。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/mega/media/ios-permissions.png)
### 第六步：构建并运行
1. 添加当前场景至 `File` &gt; `Build Settings` 或 `Build Profiles` &gt; `Scene List` 中；
2. 切换到目标平台（如Android / iOS），检查包名（Bundle ID）与 License Key 是否一致；
![Switch Platform](https://doc-asset.easyar.com/develop/unity/mega/media/build-switch-platform.png)
3. 点击 **Build And Run**。
![Build And Run](https://doc-asset.easyar.com/develop/unity/mega/media/build-and-run.png)
现场实拍的运行效果如下：
## 关于屏幕上的黄色文字
运行时，您可能会看到屏幕上显示了两处黄色文字。
1. 模拟运行的警告信息
它位于屏幕下方：
![](https://doc-asset.easyar.com/develop/unity/mega/media/warn-simulation.png)
出现这个警告的原因是因为在默认配置下，应用可以不在现场运行。它对应用的运行效果有些微影响，如果您正好在现场使用，可以在打包前 [修改 MegaTracker 配置](onsite-and-simulation.html)。
2. 诊断信息
它位于屏幕上方，用于了解 session 的运行状态和问题，建议在开发和测试阶段保持显示：
![](https://doc-asset.easyar.com/develop/unity/mega/media/ui-message.png)
可以参考 [场景中的诊断信息](../getting-started/diagnostics.html) 来快速了解如何配置和使用这些诊断信息。
## 下一步：从入门到精通
恭喜！通过以上步骤，您已成功在 **10 分钟内** 运行了 EasyAR Mega 的核心示例，亲身体验了空间定位与 AR 内容叠加的魅力。
现在，您已经掌握了基础。如果您希望：
* **构建更稳定、更高效的 AR 应用**
* **实现复杂的虚实遮挡、内容对齐等效果**
* **在没有设备或无法前往现场时进行调试**
请参考以下深入指南，它们将帮助您解决开发过程中的实际问题。
### 开发进阶
如果您希望了解完整的工程配置，可以参考以下内容：
* [使用 Universal Render Pipeline（URP）](../getting-started/universal-render-pipeline.html)
* [Player 配置](../fundamentals/setup-player.html)
* [EasyAR 配置](../fundamentals/setup-easyar.html)
如果您希望进一步了解 EasyAR 的使用方法，可以从这里开始：
* [AR 驱动的 Unity 应用基础](../fundamentals/intro.html)
同时，建议阅读以下内容来帮助您开发和调试：
* [Unity 开发中的问题诊断和报告](../diagnostics/diagnostics.html)
* [Unity AR 模拟运行](../simulation/simulation.html)
### 精细化控制 Mega 功能
下面的这些内容将帮助您更好地在您的应用中使用 Mega：
* [现场使用和模拟运行](onsite-and-simulation.html)
* [ARSession 最佳实践](session-best-practice.html)
* [添加跟踪目标](target.html)
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [环境遮挡 (Occlusion)](occlusion.html)
* [控制跟踪过程](tracker.html)
下面的这些内容将帮助您无需到达现场即可验证 Mega 功能：
* [使用 PC 相机进行快速验证](verify-pc-camera.html)
* [使用 Session 验证工具进行模拟运行](verify-session-tool.html)
### 高级主题
下面的这些内容更加适合在有一定 EasyAR 使用经验后阅读。
如果您希望在头显上运行 EasyAR Mega，可以参考以下内容：
* [Unity 中的 EasyAR 头显支持](../headsets/headsets.html)
* [在 XR 头显或眼镜上使用 EasyAR 样例](../headsets/samples.html)
如果您希望使用 AR Foundation，可以从这里开始：
* [EasyAR 对 Unity XR 框架的支持](../fundamentals/unity-xr.html)