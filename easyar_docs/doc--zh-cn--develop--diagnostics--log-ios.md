---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-ios.html
original_file: doc--zh-cn--develop--diagnostics--log-ios.md
normalized_at: 2026-02-27
---
# iOS/macOS/visionOS 上的日志分析
关于 原生(iOS/macOS) 、 Unity(iOS/macOS/visionOS) 和 Unity 编辑器(macOS) 上的日志，可参考如下说明。
## 日志获取方法
如果需要分析 iOS/visionOS 设备上的应用，则使用USB线将设备与 macOS 开发设备连接。如果需要分析 macOS 设备上的应用或程序，则这一步无需操作。
在 macOS 开发设备上，打开 `Finder -> Applications -> Utilities -> Console`。在 Console 中点击 `Start streaming`，然后运行需要分析的程序。打开应用或程序，直到 Console 中出现日志，在该日志上点右键，选择 `Show Process "<应用名>"`，即可查看该应用或程序进程的所有日志。
以下为一个例子。
![log macOS](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-macos.png)
按 `Cmd + A` 选中所有日志，然后按 `Cmd + C`，可将日志复制到剪贴板。
对于 macOS 上的程序，如果是命令行程序，也可以从终端获得日志输出。
此外，也可以通过 XCode 调试应用或程序，并从 XCode 的日志窗口获得日志。
## Unity 内置日志
在使用 Unity 开发应用时，除了平台自带的日志分析手段之外，Unity 编辑器还提供了额外的调试手段。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|macOS|\~/Library/Logs/Unity/Editor.log|
|播放器|iOS|使用 XCode 的 lldb 控制台|
|播放器|macOS|\~/Library/Logs/Company Name/Product Name/Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
## 日志的理解
在分析错误时，经常需要弄清错误发生的条件，例如调用的函数、参数、相关的状态。
## 反馈时的注意事项
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台和 CPU 架构
* iOS
arm64
* macOS
x86\_64/arm64
* visionOS
arm64
