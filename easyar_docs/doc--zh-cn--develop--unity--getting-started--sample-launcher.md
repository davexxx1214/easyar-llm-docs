---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/sample-launcher.html
---

使用 AllSamplesLauncher 快速体验 EasyAR 样例 | EasyAR 文档
**
##### Table of Contents
**
# 使用 AllSamplesLauncher 快速体验 EasyAR 样例
AllSamplesLauncher 是一个集成化的示例启动器，可以帮助您快速熟悉 EasyAR SDK 的各项功能。通过该启动器，您可以在单个 Unity 工程中一键切换并运行所有官方示例场景，无需手动配置多个独立项目。
## 准备工作
在开始之前，请确保您已经完成了以下准备工作：
1. 已安装 Unity Hub 和 Unity 编辑器
2. 创建一个新的 Unity 工程
3. 已导入 EasyAR Sense Unity Plugin 并且导入了所有 Samples
请参考 [快速入门](quickstart.html) 中的介绍按步骤进行操作。
## 详细步骤
1. 打开 Samples 中的所有场景。
![All Sample Scenes](https://doc-asset.easyar.com/develop/unity/getting-started/media/all-sample-scenes.png)
2. 点击菜单栏 `File` &gt; `Build Settings` 或 `Build Profiles` &gt; `Scene List` 。
3. 将所有场景都拖动到 `Scene List` 中。
4. 确保 AllSamplesLauncher 位于所有场景中的第一个。如不是，可以在窗口内拖动。
![Scene List Order](https://doc-asset.easyar.com/develop/unity/getting-started/media/scene-list-order.png)
5. 点击菜单栏 `File` &gt; `Build And Run` 进行打包、运行。
##### 注意
打包到手机运行时，不要添加头显类的场景：
* Combination\_BasedOn\_AppleVisionPro
* Combination\_BasedOn\_Xreal
![Donot Load Headset](https://doc-asset.easyar.com/develop/unity/getting-started/media/donot-load-headset.png)
## 打包中遇到问题
在您编译、打包过程中，可能遇到一些错误。常见的问题有：
|错误信息|原因|解决办法|
|*FileNotFoundException:EasyAR Settings Asset*|未填写 License|点击菜单栏 `EasyAR` &gt; `Sense` &gt; `Configuration`，在 **EasyAR Sense License** 中填入您的 License Key|
|*Missing Prefab Asset: 'XR Interaction Setup'*|头显相关文件缺失|打包场景列表中删除头显相关场景。如果您确认需要打包头显，请按照 [使用头显样例](../headsets/samples.html) 中的步骤进行|
## 启动器使用
运行后，您将看到一个简洁的启动器界面。
![Lanucher Homepage](https://doc-asset.easyar.com/develop/unity/getting-started/media/lanucher-homepage.png)
点击界面底部中间的 `Samples` 按钮，即可进入所有功能的样例。
![Lanucher Samplepage](https://doc-asset.easyar.com/develop/unity/getting-started/media/lanucher-samplepage.png)
在界面左侧是功能分类，右侧则是每个功能下的场景样例列表。点击不同的样例场景，即可体验 EasyAR 提供的所有不同功能。
同时，在界面的底部还提供了 `EasyAR Sense` 和 `EasyAR Mega` 的功能演示视频，可以帮助您更好的理解 EasyAR 能为您提供怎样的功能和效果。
## 运行样例前的必读事项
在运行特定样例之前，您**必须**完成以下关键配置，否则样例将无法正常工作：
1. **设置您的 API Key**
* 部分样例（特别是涉及云识别、Mega 云定位等）需要有效的 API Key。
* 在菜单栏 `EasyAR` &gt; `Sense` &gt; `Configuration` 中，找到对应样例需要填写的地方。
* 从中填入您从 EasyAR 开发者中心申请到的 **App ID**、 **API Key**、 **API Secret**。
![Key Configuration](https://doc-asset.easyar.com/develop/unity/getting-started/media/key-config.png)
* **重要提示**：如果您还没有 API Key，部分本地功能的样例（如图片跟踪）可能仍能运行，但云功能会失败。请务必前往 [EasyAR 开发者中心](https://www.easyar.cn/view/login.html) 创建应用并获取 Key。
* **配置 XR/平台支持**：
* 如果您运行的是 **头显相关** 的样例，您参照 [使用头显样例](../headsets/samples.html) 中的进行。
* 请确保您的设备（如手机或头显）已正确连接并处于开发者模式。
## 深入探索样例
示例启动器是您学习的最佳起点。我们强烈建议您：
* **先运行，再研究**：通过启动器快速体验每个样例的效果，对 EasyAR 的能力建立直观印象。
* **打开场景源文件**：每个样例都是一个独立的 Unity 场景文件，位于 `Assets/Samples/EasyAR Sense Unity Plugin/[版本号]/\_\_All Samples\_\_/[功能名称]/[样例名称]/Scenes` 目录下。
* **研究并阅读脚本代码**：在样例场景中，可以打开样例附带的 `\*.cs` 脚本，查看我们是如何调用 EasyAR API 来实现特定功能的。这是学习 API 使用方法的最佳途径。
通过示例启动器，您可以快速建立对 EasyAR SDK 的功能认知。祝您探索愉快！