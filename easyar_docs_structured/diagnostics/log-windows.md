---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-windows.html
original_file: doc--zh-cn--develop--diagnostics--log-windows.md
normalized_at: 2026-02-27
---
# Windows 上的日志分析
关于 原生(Windows) 和 Unity 编辑器(Windows)上的日志，可参考如下说明。
## 日志获取方法
如果程序带有控制台，可以从控制台获取日志。
![log Windows](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-windows.png)
否则，需要使用 `Log.setLogFunc` 进行日志重定向，并自己提供输出日志的方法。
## Unity 内置日志
在使用 Unity 开发应用时，除了平台自带的日志分析手段之外，Unity 编辑器还提供了额外的调试手段。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|Windows|%LOCALAPPDATA%\\Unity\\Editor\\Editor.log|
|播放器|Windows|%USERPROFILE%\\AppData\\LocalLow\\CompanyName\\ProductName\\Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
## 日志的理解
一般来说，输出级别为 `Error` 的错误（显示为红色），是比较重要的问题，需要检查。例如下面是找不到摄像头的错误。
![log Windows error](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-windows-error.png)
在分析错误时，经常需要弄清错误发生的条件，例如调用的函数、参数、相关的状态。
## 反馈时的注意事项
反馈时需要附带以下信息。
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台
Win32
* CPU 架构
x86\_64/x86
