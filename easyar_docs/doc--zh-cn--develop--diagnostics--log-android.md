---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-android.html
---

Android 上的日志分析 | EasyAR 文档
**
##### Table of Contents
**
# Android 上的日志分析
关于 原生(Android) 和 Unity(Android) 上的日志，可参考如下说明。
## 日志获取方法
可以通过 Android Studio 或者 `adb logcat` 获得日志。推荐使用 `adb logcat` 以获得完整的日志。
使用时可能需要开启 Android 设备的开发者模式，开启 USB 调试或无线调试，连接 USB 线或通过 WLAN 进行配对和连接。请参考 Android 调试桥（[中文](https://android-docs.cn/tools/adb) [英文](https://developer.android.com/tools/adb)）。
以下为通过 WLAN 进行配对并连接，使用 `adb logcat` 的例子。
![log Android logcat](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-android-logcat.png)
连接 `adb` 后，首先使用 `adb logcat -c` 清空之前的日志，然后运行 `adb logcat &gt; log.txt` 即可将日志输出到 `log.txt` 。此时运行程序，直到出错，然后使用 `Ctrl + C` 结束日志输出。
以下为一个日志文件的例子。
![log Android](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-android.png)
## 日志的理解
以下 tag 是调试时需要特别关注的。
* EasyAR
EasyAR 输出的日志
* Unity
Unity 引擎在 C# 层输出的日志
* UnityPlayer
Unity 引擎在 Java/JNI 层输出的日志
* libunity
Unity 引擎在 C++ 或 IL2CPP 层输出的日志
* AndroidRuntime
Android 系统在 Java 异常未捕捉时输出的日志
* ActivityManager
Android 系统在 ANR 等情况下输出的日志
在分析错误时，经常需要弄清错误发生的条件，例如调用的函数、参数、相关的状态。
## 反馈时的注意事项
反馈时请提供未过滤 tag 的日志信息，因为有时候系统底层库会发出详细的出错原因，而这些库的 tag 在不同系统上是不同的。
此外，反馈时需要附带以下信息。
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* CPU 架构
aarch64/armeabi-v7a