---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/enable-easyar.html
original_file: doc--zh-cn--develop--unity--getting-started--enable-easyar.md
normalized_at: 2026-02-27
---
# 导入 EasyAR 插件以启用 AR 功能
本教程介绍如何在 Unity 中启用 EasyAR 插件。
## 使用兼容的 Unity 版本
确保已安装兼容的 Unity 版本（Unity 2021.3 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
## 导入 EasyAR Sense Unity Plugin
在[下载页面](https://www.easyar.cn/view/download.html)，您会看到 Unity 插件有两个版本：`EasyAR Sense Unity Plugin` 和 `EasyAR Sense Unity Plugin (for Mega)`。
这两个版本的主要差异为：
* **EasyAR Sense Unity Plugin**： 不含 Mega 支持文件，不能用于 Mega 开发。EasyAR 提供从 4.6 开始的历史版本下载。
* **EasyAR Sense Unity Plugin (for Mega)**：包含 Mega 支持文件，可以用于 Mega 开发。EasyAR 不提供历史版本下载。
在不需要开发 Mega 功能时，建议使用 `EasyAR Sense Unity Plugin`。
* 下载插件包
* 下载最新版本的 [EasyAR Sense Unity Plugin](https://www.easyar.cn/view/download.html)。
* 解压下载的 `zip` 包之后可以看到 `readme` 和 `.tgz` 文件，`.tgz` 文件可以直接导入 Unity， 不能解压。
* 将 `.tgz` 文件存放到 Unity 项目 `Packages` 文件夹内。
* 导入插件包
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`。
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`。
* 在弹出的对话框中选择前述 `.tgz` 文件。
![ImportUnityPlugin](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_easyar_unity_plugin.png)
> **注意**
`.tgz` 文件在导入 Unity 后不能被删除或移动到另一个位置，需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
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
## 后续步骤
* 可以阅读 [配置 AR 场景](scene.html) 了解如何创建一个简单的 AR 场景。
## 相关主题
* 如果需要开发 Mega 功能，可以 [导入最新版本的 EasyAR 插件以启用 Mega 功能](../mega/enable-mega.html)。
