---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/enable-mega.html
original_file: doc--zh-cn--develop--unity--mega--enable-mega.md
normalized_at: 2026-02-27
---
# 导入最新版本的 EasyAR 插件以启用 Mega 功能
本文介绍了如何导入最新版本的 EasyAR Sense Unity Plugin (for Mega) 以启用 Mega 功能。
## 使用 Mega 应导入最新版本的 EasyAR 插件
>
> 需要使用 Unity 2021.3.30 或更高版本。
>
在[下载页面](https://www.easyar.cn/view/download.html)，您会看到 Unity 插件有两个版本：`EasyAR Sense Unity Plugin` 和 `EasyAR Sense Unity Plugin (for Mega)`。
这两个版本的主要差异为：
* **EasyAR Sense Unity Plugin**： 不含 Mega 支持文件，不能用于 Mega 开发。EasyAR 提供从 4.6 开始的历史版本下载。
* **EasyAR Sense Unity Plugin (for Mega)**：包含 Mega 支持文件，可以用于 Mega 开发。EasyAR 不提供历史版本下载。
在使用 4000 之后的版本时，只要版本号相同，两个压缩包内的 EasyAR Sense Unity Plugin（即 `com.easyar.sense`）文件是完全相同的，可以互相替换。因此，如果您已经下载并导入了最新版本的 EasyAR Sense Unity Plugin，可以直接从 EasyAR Sense Unity Plugin (for Mega) 压缩包中提取 `com.easyar.mega` 文件导入到 Unity 项目中，而不需要重新导入整个插件包。
> **注意**
在 4000 版本之后，导入不兼容的 `com.easyar.sense` 和 `com.easyar.mega` 时，脚本编译器会报错，提示版本不匹配。请确保 `com.easyar.sense` 和 `com.easyar.mega` 来自同一版本的插件包或互相兼容。
4.7 版本的 `com.easyar.sense` 和 `com.easyar.mega` 的版本号包含后面的所有数字和字母在内必须完全一致，才能保证兼容性。
在应用上线前，建议再次查看 EasyAR 网站，如果有更新版本的 EasyAR Sense Unity Plugin (for Mega)，请下载并导入最新版本以确保应用可以正常使用最新的 Mega 服务，以确保最长的兼容性和最佳的性能。
> **重要事项**
使用过时的 EasyAR Sense Unity Plugin (for Mega) 开发的应用，可能无法使用最新的 Mega 服务。
在线上服务没有变化时（即 Mega 定位库的版本没有更新时），使用旧版本的 EasyAR Sense Unity Plugin (for Mega) 打包的应用仍然可以正常使用。
## 导入 EasyAR 插件和 Mega 支持包
解压下载的 zip 包之后可以看到 `readme` 和两个 `tgz` 文件，`tgz` 文件可以直接导入 Unity 不要再解压。
导入方法：
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`
* 在弹出的对话框中选择下载并解压得到的 `.tgz` 文件
两个 `.tgz` 文件 导入顺序不限，可以先导入 `com.easyar.sense`，也可以先导入 `com.easyar.mega`。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/package-import.png)
> **提示**
`com.easyar.mega` 依赖一些第三方包，如 `com.unity.cloud.ktx` 和 `com.unity.cloud.gltfast`，导入时请确保网络连接正常，以便 Unity 可以自动下载和导入这些依赖包。
在部分网络环境下，Unity 导入这些依赖包的过程可能比较缓慢，建议修改网络环境或多次尝试导入，直到所有依赖包都成功导入。
导入成功后，在 Unity 的 `Console` 窗口中不应看到任何错误提示，同时打开 `Package Manager` 窗口，可以看到 `EasyAR Sense Unity Plugin` 和 `EasyAR Mega Studio` 均已导入且显示为刚刚导入的版本号。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/package-imported.png)
> **注意**
在导入插件包后， `tgz` 文件不能被删除或移动到另一个位置，因此通常需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 后续步骤
* [快速入门](quickstart.html) Unity Mega 开发
* 使用 Mega 开发应用
* [AR Session 最佳实践](session-best-practice.html)
* [添加跟踪目标](target.html)
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)
