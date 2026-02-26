---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-windows.html
---

Windows 上的崩溃分析 | EasyAR 文档
**
##### Table of Contents
**
# Windows 上的崩溃分析
关于 原生(Windows) 和 Unity 编辑器(Windows)上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在Visual Studio中调试时需要的信息如下图。
![crash Windows](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-windows.png)
其中崩溃原因为
```
`Exception thrown at 0x00007FFB7747317B (EasyAR.dll) in HelloAR.exe: 0xC0000005: Access violation writing location 0x0000000000009C40.
`
```
代码运行栈为
```
`&gt; EasyAR.dll!00007ffb7747317b() Unknown
EasyAR.dll!00007ffb774719cc() Unknown
EasyAR.dll!00007ffb77477db3() Unknown
EasyAR.dll!00007ffb77474eb3() Unknown
ucrtbase.dll!00007ffbfee910b2() Unknown
kernel32.dll!00007ffc009f7c24() Unknown
ntdll.dll!00007ffc0148d721() Unknown
`
```
动态库加载地址为
```
`0x00007FFB75BC0000
`
```
当代码运行栈中存在 `EasyAR.dll` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
## 开发中的崩溃位置获取（Unity）
在使用 Unity 开发应用时，还可以使用 Unity 的日志来分析崩溃。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|Windows|%LOCALAPPDATA%\\Unity\\Editor\\Editor.log|
|播放器|Windows|%USERPROFILE%\\AppData\\LocalLow\\CompanyName\\ProductName\\Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
托管异常(C#)可以在 Unity 编辑器的 Console 窗口中查看（Unity 主菜单的 `Window -&gt; General -&gt; Console`）。
## 其他崩溃相关信息
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台
Win32
* CPU 架构
x86\_64/x86