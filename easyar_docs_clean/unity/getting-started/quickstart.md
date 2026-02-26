---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/quickstart.html
original_file: doc--zh-cn--develop--unity--getting-started--quickstart.md
normalized_at: 2026-02-27
---
# 使用示例快速入门 EasyAR Unity 开发
本教程介绍如何配置并运行 EasyAR Unity 示例，以快速入门 AR 开发。
## 准备空 Unity 工程
确保已安装兼容的 Unity 版本（Unity 2021.3 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
使用 `3D (Built-in Render Pipeline)` 模板创建空 Unity 工程：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/create-project.png)
> **注意**
初次使用不建议使用 URP。
如果您在使用 Unity 6，需要手动下载并使用 `3D (Built-In Render Pipeline) Template`，默认安装下它在模板列表靠后的位置。
> **重要事项**
若要使用 URP，必须按照 [Universal Render Pipeline (URP)](universal-render-pipeline.html) 进行额外配置，否则相机画面将无法显示。
## 导入 EasyAR Sense Unity Plugin
* 下载插件包
* 下载最新版本的 [EasyAR Sense Unity Plugin](https://www.easyar.cn/view/download.html)，其中包含示例（sample）。
* 解压下载的 `zip` 包之后可以看到 `readme` 和 `.tgz` 文件，`.tgz` 文件可以直接导入 Unity， 不能解压。
* 将 `.tgz` 文件存放到 Unity 项目 `Packages` 文件夹内。
* 导入插件包
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`。
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`。
* 在弹出的对话框中选择前述 `.tgz` 文件。
![ImportUnityPlugin](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_easyar_unity_plugin.png)
> **注意**
`.tgz` 文件在导入 Unity 后不能被删除或移动到另一个位置，需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 导入示例
使用菜单 `Window` > `Package Manager` 打开 Package Manager，选中 `EasyAR Sense Unity Plugin`, 在右侧选择 `\*\*All Samples\*\*` 一次性导入所有示例。
![ImportSample](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_samples.png)
> **小心**
`\*\*All Samples\*\*` 和其他示例不可同时导入，否则会出现重复资产进而导致部分场景资源丢失。如不小心导入了重复的文件，需删除后重新导入。
## 修改场景列表
打开 `Build Settings` （ 或 `Build Profiles` ），
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_4.png)
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_6.png)
将 Unity 工程中的示例场景添加到 `Build Settings` 或 `Build Profiles` 的 `Scene List` 中，并将示例启动器的场景（`AllSamplesLauncher`）移动到所有场景中的第一个。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_7.png)
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_8.png)
> **小心**
注意不要这些添加头显的场景，否则可能会打包失败：
* Combination\_BasedOn\_AppleVisionPro.rst
* Combination\_BasedOn\_Xreal.rst
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_14.png)
## 填写许可证（License Key）
从 Unity 菜单中选择 `EasyAR` > `Sense` > `Configuration` 调出 EasyAR Sense 设置界面。
![FillInKey](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
在 `EasyAR Sense License` 下的输入框中填入 EasyAR Sense License。
![FillInKey2](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill-in-key2.png)
> **提示**
EasyAR Sense License 可以从 EasyAR 开发中心（[中文](https://portal.easyar.cn/sdk/list)，[英文](https://portal.easyar.cn/sdk/list)） 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `是`，名称随意填写
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
> **注意**
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
## 编辑器中运行
在编辑器中运行需要您的电脑上连接一个摄像头。
### 确认系统相机正常
打开 `系统相机应用`：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/camera-windows-open.png)
确认相机可以正常使用：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/camera-windows.png)
最后注意关闭相机应用，避免运行示例时发生冲突。
> **注意**
EasyAR 仅使用系统提供的接口打开相机，需确保 `系统相机应用` 可以打开相机并正常显示。
### 运行示例
>
> 以下内容以图像跟踪示例
`> ImageTracking_Targets
`> 为例，其他示例运行方式类似。
>
打开示例启动器场景，并点击 Unity 编辑器顶部的 `Play` 按钮。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-editor.png)
进入 `ImageTracking\_Targets` 场景。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-editor-select.png)
> **提示**
也可以直接打开 `ImageTracking\_Targets` 场景并执行。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-editor.png)
将摄像头对准以下识别图：
>
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
> 下载地址
> ：🔗
[> namecard
](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
EasyAR 会识别跟踪这张图，并叠加虚拟物体。
> **注意**
部分功能无法在编辑器中连接摄像头运行，但可以在手机上运行。无法在编辑器中使用的示例在运行时会有启动失败的弹窗。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_15.png)
同时会有消息提示和错误log输出。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_13.png)
## 手机上运行
在手机上运行需要进行打包，打包前需要修改 Player 配置。
### 修改 Player 配置
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击安卓图标，调出 Android 平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
* 修改 Package Name 为 License Key 页面显示的 Package Name
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Package Name 是 `com.mycompany.myproject`，则必须填写这里 Package Name 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 Minimum API Level 为 `API Level 21` 或更高版本
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* 修改 Scripting Backend 为 `IL2CPP`，并在 `Target Architecture` 中勾选 `ARM64`
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-64bit.png)
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
* 修改 Bundle ID 为 License Key 页面显示的 Bundle ID
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Bundle ID 是 `com.mycompany.myproject`，则必须填写这里 Bundle ID 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 `Architecture` 为 `ARM64`
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* 添加 `Camera Usage Description`，字符串内容可以随意填写，但必须添加。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-camera-permission.png)
### 打包应用
选择 `File` > `Build Settings`，选择目标平台 (Android/iOS)，然后选择 `switch platform`。
![switchplatform](https://doc-asset.easyar.com/develop/unity/getting-started/media/switch-platform.png)
选择 `Build` 或 `Build And Run` 编译项目并在手机上安装，运行时需允许相应权限。
![buildandrun](https://doc-asset.easyar.com/develop/unity/getting-started/media/build-and-run.png)
### 运行示例
>
> 以下内容以图像跟踪示例
`> ImageTracking_Targets
`> 为例，其他示例运行方式类似。
>
运行后启动的应是示例启动器场景。
> **提示**
如果打开后没有进入示例启动器场景，需要检查是否正确设置了 `Build Settings` 或 `Build Profiles` 的场景列表，将 `AllSamplesLauncher` 移动到第一个。
进入 `ImageTracking\_Targets` 场景。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-phone-select.png)
将手机摄像头对准以下识别图：
>
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
> 下载地址
> ：🔗
[> namecard
](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
EasyAR 会识别跟踪这张图，并叠加虚拟物体。
## 后续步骤
您已经成功运行 Unity AR 示例，可能对示例所展示的 AR 场景是如何创建的感兴趣。可以按顺序阅读以下入门指南：
* [启用 EasyAR](enable-easyar.html)
* [配置 AR 场景](scene.html)
* [场景中的诊断信息](diagnostics.html)
关于示例启动器可以参考详细的使用说明：
* [示例启动器使用说明](sample-launcher.html)
如果您希望了解完整的工程配置，可以参考以下内容：
* [使用 Universal Render Pipeline（URP）](universal-render-pipeline.html)
* [Player 配置](../fundamentals/setup-player.html)
* [EasyAR 配置](../fundamentals/setup-easyar.html)
如果您希望进一步了解 EasyAR 的使用方法，可以从这里开始：
* [AR 驱动的 Unity 应用基础](../fundamentals/intro.html)
