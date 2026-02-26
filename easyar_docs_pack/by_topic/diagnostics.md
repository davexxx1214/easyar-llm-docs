# EasyAR 专题包：diagnostics

适用于上下文长度有限时的分卷输入。

## 目录
- `diagnostics/crash-android.md`
- `diagnostics/crash-ios.md`
- `diagnostics/crash-windows.md`
- `diagnostics/diagnostics.md`
- `diagnostics/log-android.md`
- `diagnostics/log-ios.md`
- `diagnostics/log-wechat.md`
- `diagnostics/log-windows.md`
- `diagnostics/recordings-headsets.md`
- `diagnostics/recordings.md`
- `diagnostics/simulation.md`

---

## Android 上的崩溃分析
- 章节路径: `diagnostics/crash-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-android.html

# Android 上的崩溃分析
关于 原生(Android) 和 Unity(Android)上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在 Android Studio 中调试 Android 的 Native 程序时，需要在 Configuration 设置中将 Debugger - Debug type 改为Dual (Java + Native)。
![crash Android configuratio](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-configuration.png)
在 Android Studio 中调试时需要的信息如下图。
![crash Android stack](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-stack.png)
在 lldb 中输入 `bt` ，可以获得崩溃原因和代码运行栈，如下
```
(lldb) bt
\* thread #16, name = 'samples.helloar', stop reason = signal SIGSEGV: invalid address (fault address: 0x9c40)
\* frame #0: 0x0000004922f3a1d8 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol3056$$libEasyAR.so + 6088
frame #1: 0x0000004922f38568 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol3054$$libEasyAR.so + 288
frame #2: 0x0000004922f347f8 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol2876$$libEasyAR.so + 332
frame #3: 0x00000049be2390c8 libc.so`\_\_pthread\_start(void\*) + 40
frame #4: 0x00000049be1f04f8 libc.so`\_\_start\_thread + 72
```
当代码运行栈中存在 `libEasyAR.so` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
在 lldb 中输入 `image dump sections libEasyAR.so`，可以获得动态库 `.text` 节加载地址，如下
```
(lldb) image dump sections libEasyAR.so
...
SectID Type Load Address Perm File Off. File Size Flags Section Name
...
0x00000010 code [0x0000004922e30cfc-0x0000004923654558) r-x 0x00256cfc 0x0082385c 0x00000006 libEasyAR.so..text
...
```
## 发布后的崩溃位置获取
发布后，也有可能遇到崩溃的情况。
如果出现可以重现的崩溃，可以尝试使用 Android Studio 自带的 Profile/Debug 工具。然后按照开发中的做法即可获得崩溃位置。
![crash Android debug](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-debug.png)
如果出现难以重现的崩溃，可以使用一些 crash 报告库，拦截应用崩溃信息，并报告到服务器。但是需要注意，崩溃信息中一定要包含代码运行栈和模块加载地址两部分信息。由于 Android 从 4.0 开始引入 ASLR（地址空间布局随机化），动态库模块加载地址在每次运行时都可能不同，会导致代码地址也会动态变化，只有知道代码栈中的代码地址和动态库模块加载地址的相对值，才能知道程序在什么位置发生了崩溃。
当代码运行栈中存在 `libEasyAR.so` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
## 其他崩溃相关信息
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* CPU 架构
aarch64/armeabi-v7a

---

## iOS/macOS/visionOS 上的崩溃分析
- 章节路径: `diagnostics/crash-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-ios.html

# iOS/macOS/visionOS 上的崩溃分析
关于 原生(iOS/macOS) 、 Unity(iOS/macOS/visionOS) 和 Unity 编辑器(macOS) 上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在 XCode 中调试时需要的信息如下图。
![crash iOS](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-ios.png)
在 lldb 中输入bt，可以获得崩溃原因和代码运行栈，如下
```
(lldb) bt
\* thread #11, stop reason = EXC\_BAD\_ACCESS (code=1, address=0x9c40)
\* frame #0: 0x00000001057e7cb0 easyar`\_\_\_lldb\_unnamed\_symbol2693$$easyar + 6984
frame #1: 0x00000001057e5e14 easyar`\_\_\_lldb\_unnamed\_symbol2692$$easyar + 276
frame #2: 0x00000001057e2500 easyar`\_\_\_lldb\_unnamed\_symbol2532$$easyar + 360
frame #3: 0x00000001f3d60bfc libsystem\_pthread.dylib`\_pthread\_start + 320
```
当代码运行栈中存在 `easyar` 或 `libEasyAR.dylib` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
在 lldb 中输入 `image list easyar` 或者 `image list libEasyAR.dylib`，可以获得动态库加载地址，如下
```
(lldb) image list easyar
[ 0] DF06BDD8-A8AF-3982-897D-A906EE229A4F 0x0000000105730000 /Users/<user>/Library/Developer/Xcode/DerivedData/helloar-bpvpobshgxnnwwdiryfjufioysag/Build/Products/Debug-iphoneos/helloar.app/Frameworks/easyar.framework/easyar
```
## 开发中的崩溃位置获取（Unity）
在使用 Unity 开发应用时，还可以使用 Unity 的日志来分析崩溃。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|macOS|\~/Library/Logs/Unity/Editor.log|
|播放器|iOS|使用 XCode 的 lldb 控制台|
|播放器|macOS|\~/Library/Logs/Company Name/Product Name/Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
托管异常(C#)可以在 Unity 编辑器的 Console 窗口中查看（Unity 主菜单的 `Window -> General -> Console`）。
## 发布后的崩溃位置获取
发布后，也有可能遇到崩溃的情况。此时从设备的 Privacy - Analytics & Improvements - Analytic Data 查看或通过 TestFlight 和 App Store 来[收集崩溃日志](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs#Collect-crash-reports-from-TestFlight-and-the-App-Store)。
以下为一个崩溃的例子：
```
Incident Identifier: 5916E252-D8C2-43C3-B583-7E38399597C9
CrashReporter Key: 2075d595d8d96cf07913a12798d5e0aba79c5358
Hardware Model: iPhone9,2
Process: ARManualEditorDemo [2352]
Path: /private/var/containers/Bundle/Application/ED9F6959-612A-4595-A7B9-3F573B5097DD/ARManualEditorDemo.app/ARManualEditorDemo
Identifier: cn.easyar.demo.ARManualEditor
Version: 6 (2.0.1)
Code Type: ARM-64 (Native)
Role: Non UI
Parent Process: launchd [1]
Coalition: cn.easyar.demo.ARManualEditor [1831]
Date/Time: 2019-09-17 16:21:13.1246 +0800
Launch Time: 2019-09-17 16:08:08.3605 +0800
OS Version: iPhone OS 12.4 (16G77)
Baseband Version: 5.70.01
Report Version: 104
Exception Type: EXC\_BREAKPOINT (SIGTRAP)
Exception Codes: 0x0000000000000001, 0x000000019d7e86fc
Triggered by Thread: 0
Thread 0 name: Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0 JavaScriptCore 0x000000019d7e86fc WTFCrashWithInfo+ 2471676 (int, char const\*, char const\*, int) + 20
1 JavaScriptCore 0x000000019dd85da0 llint\_slow\_path\_get\_by\_val + 6032
2 JavaScriptCore 0x000000019d7a25cc llint\_entry + 34380
...
13 JavaScriptCore 0x000000019d799cec vmEntryToJavaScript + 268
14 JavaScriptCore 0x000000019dccb4d0 JSC::Interpreter::executeCall+ 7595216 (JSC::ExecState\*, JSC::JSObject\*, JSC::CallType, JSC::CallData const&, JSC::JSValue, JSC::ArgList const&) + 424
15 JavaScriptCore 0x000000019dead560 JSC::profiledCall+ 9569632 (JSC::ExecState\*, JSC::ProfilingReason, JSC::JSValue, JSC::CallType, JSC::CallData const&, JSC::JSValue, JSC::ArgList const&) + 188
16 JavaScriptCore 0x000000019d7df170 JSObjectCallAsFunction + 376
17 EasyARPlayer 0x000000010353d284 0x10326c000 + 2953860
18 EasyARPlayer 0x000000010363c880 0x10326c000 + 3999872
19 EasyARPlayer 0x000000010364ee1c 0x10326c000 + 4075036
20 EasyARPlayer 0x0000000103295388 0x10326c000 + 168840
21 GLKit 0x00000001a337b91c -[GLKView \_display:] + 256
...
33 libdyld.dylib 0x0000000195e468e0 start + 4
...
Thread 8:
0 libsystem\_kernel.dylib 0x0000000195f92ee4 \_\_psynch\_cvwait + 8
1 libsystem\_pthread.dylib 0x000000019600dcf8 \_pthread\_cond\_wait$VARIANT$mp + 636
2 easyar 0x0000000102fba7c0 0x1028b4000 + 7366592
3 easyar 0x0000000102e7627c 0x1028b4000 + 6038140
4 easyar 0x0000000102e452e8 0x1028b4000 + 5837544
5 libsystem\_pthread.dylib 0x00000001960152c0 \_pthread\_body + 128
6 libsystem\_pthread.dylib 0x0000000196015220 \_pthread\_start + 44
7 libsystem\_pthread.dylib 0x0000000196018cdc thread\_start + 4
...
Binary Images:
0x1023e4000 - 0x1024f3fff ARManualEditorDemo arm64 <0fb0d9b7d18c3e2ebf44e950a68af61f> /var/containers/Bundle/Application/ED9F6959-612A-4595-A7B9-3F573B5097DD/ARManualEditorDemo.app/ARManualEditorDemo
...
0x1028b4000 - 0x10310bfff easyar arm64 <cb52ccf821e33255a0c30ca2422d2862> /var/containers/Bundle/Application/ED9F6959-612A-4595-A7B9-3F573B5097DD/ARManualEditorDemo.app/Frameworks/easyar.framework/easyar
...
EOF
```
其中，包含 `easyar` 的代码栈有
```
2 easyar 0x0000000102fba7c0 0x1028b4000 + 7366592
3 easyar 0x0000000102e7627c 0x1028b4000 + 6038140
4 easyar 0x0000000102e452e8 0x1028b4000 + 5837544
```
这里的 0x0000000102fba7c0 为代码在内存中的虚拟地址，0x1028b4000 为 `easyar` 的模块加载地址，7366592 为偏移量。
从 `Binary Images` 的部分也能看出0x1028b4000 为 `easyar` 的模块加载地址。
需要注意，崩溃信息中一定要包含代码运行栈和模块加载地址两部分信息。由于 ASLR（地址空间布局随机化），动态库模块加载地址在每次运行时都可能不同，会导致代码地址也会动态变化，只有知道代码栈中的代码地址和动态库模块加载地址的相对值，才能知道程序在什么位置发生了崩溃。
当代码运行栈中存在 `easyar` 或 `libEasyAR.dylib` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
## 其他崩溃相关信息
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

---

## Windows 上的崩溃分析
- 章节路径: `diagnostics/crash-windows.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-windows.html

# Windows 上的崩溃分析
关于 原生(Windows) 和 Unity 编辑器(Windows)上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在Visual Studio中调试时需要的信息如下图。
![crash Windows](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-windows.png)
其中崩溃原因为
```
Exception thrown at 0x00007FFB7747317B (EasyAR.dll) in HelloAR.exe: 0xC0000005: Access violation writing location 0x0000000000009C40.
```
代码运行栈为
```
> EasyAR.dll!00007ffb7747317b() Unknown
EasyAR.dll!00007ffb774719cc() Unknown
EasyAR.dll!00007ffb77477db3() Unknown
EasyAR.dll!00007ffb77474eb3() Unknown
ucrtbase.dll!00007ffbfee910b2() Unknown
kernel32.dll!00007ffc009f7c24() Unknown
ntdll.dll!00007ffc0148d721() Unknown
```
动态库加载地址为
```
0x00007FFB75BC0000
```
当代码运行栈中存在 `EasyAR.dll` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
## 开发中的崩溃位置获取（Unity）
在使用 Unity 开发应用时，还可以使用 Unity 的日志来分析崩溃。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|Windows|%LOCALAPPDATA%\\Unity\\Editor\\Editor.log|
|播放器|Windows|%USERPROFILE%\\AppData\\LocalLow\\CompanyName\\ProductName\\Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
托管异常(C#)可以在 Unity 编辑器的 Console 窗口中查看（Unity 主菜单的 `Window -> General -> Console`）。
## 其他崩溃相关信息
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台
Win32
* CPU 架构
x86\_64/x86

---

## 问题诊断和报告
- 章节路径: `diagnostics/diagnostics.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/diagnostics.html

# 问题诊断和报告
本章主要描述构建AR应用时可能遇到的问题、主要的分析方法，以及报告问题所需要收集的信息和联系途径。
## AR 场景中问题分析的挑战
在 AR 场景中的问题分析，存在一些独特的挑战。
### 输入的不确定性
在传统应用中，输入通常是确定的点击或键盘事件。而在 AR 中，输入源自变动的物理环境，这带来了极大的分析难度。AR 应用需要结合物理环境来使用，但开发和测试时，在物理环境中无法每次获得相同的输入，即使按照同一条路线行进，取得的相机图像、加速度计、陀螺仪等传感器的数据都可能产生一些变化，而这对跟踪结果的影响可能是巨大的。
EasyAR 中提供了 EIF 文件的录制和回放功能，可以在一定程度上缓解输入的不确定性，但由于算法的不确定性，最终的跟踪结果本质上还是不确定的。同时，EIF 录制数据覆盖不全、光照变化、行人或车辆造成的动态遮挡等，也会影响实际使用时的跟踪质量。
### 算法的不确定性
AR 的核心算法是一些视觉算法，例如 SLAM（即时定位与地图构建）。这些算法本质上是概率性的而非确定性的。
当输入的相机图像缺乏显著的特征时，算法可能使用历史位置姿态和加速度计、陀螺仪等传感器数据进行预测，预测的位置和姿态的结果会随着时间推移而累积，产生飘移。而每次的预测结果和数据的传入时机、设备的温度、CPU 的频率、网络传输速度等外界因素有关，存在动态变化，累积下来即使是同样的输入，多次运行的结果也可能偏差很大。
## 不同问题的分析方法
对于不同的问题，可能需要不同的分析方法。
### 日志
对于一些程序运行不正常的情况，例如黑屏、无法正常定位、无法正常跟踪的情况，最基本的方法是查看日志，检查其中是否有错误信息。EasyAR 中产生的日志，均会使用特定的标签，便于识别。
### 崩溃
有时候程序会发生崩溃，崩溃的位置可能在库的代码中，也可能在程序自己的代码中。崩溃发生的原因有可能是由于程序本身的问题，也可能是库中存在问题。
### 抖动、跳动等视觉异常
由于传感器数据精度或者算法适配原因，可能会发生定位抖动或跳动。此时应尝试使用不同设备重现此问题，并截图、录屏和录制 EIF 文件。
## 平台专用指南
问题诊断和报告与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [日志分析 Android](log-android.html)
* [日志分析 iOS/macOS/visionOS](log-ios.html)
* [日志分析 Windows](log-windows.html)
* [崩溃分析 Android](crash-android.html)
* [崩溃分析 iOS/macOS/visionOS](crash-ios.html)
* [崩溃分析 Windows](crash-windows.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)
* [Unity 简介](../unity/diagnostics/diagnostics.html)
* [Unity UI消息](../unity/diagnostics/ui-messages.html)
* [Unity 开发者模式](../unity/diagnostics/developer-mode.html)
* [Unity 录制EED dump文件](../unity/diagnostics/event-dump.html)
* [Unity 问题报告](../unity/diagnostics/report.html)
* [Unity Diagnostics Controller 组件参考](../unity/diagnostics/comp-DiagnosticsController.html)
* [日志分析](log-wechat.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)
* [问题报告](../wechat/diagnostics/report.html)
* [日志分析 Android](log-android.html)
* [日志分析 iOS/macOS/visionOS](log-ios.html)
* [日志分析 Windows](log-windows.html)
* [崩溃分析 Android](crash-android.html)
* [崩溃分析 iOS/macOS/visionOS](crash-ios.html)
* [崩溃分析 Windows](crash-windows.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)

---

## Android 上的日志分析
- 章节路径: `diagnostics/log-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-android.html

# Android 上的日志分析
关于 原生(Android) 和 Unity(Android) 上的日志，可参考如下说明。
## 日志获取方法
可以通过 Android Studio 或者 `adb logcat` 获得日志。推荐使用 `adb logcat` 以获得完整的日志。
使用时可能需要开启 Android 设备的开发者模式，开启 USB 调试或无线调试，连接 USB 线或通过 WLAN 进行配对和连接。请参考 Android 调试桥（[中文](https://android-docs.cn/tools/adb) [英文](https://developer.android.com/tools/adb)）。
以下为通过 WLAN 进行配对并连接，使用 `adb logcat` 的例子。
![log Android logcat](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-android-logcat.png)
连接 `adb` 后，首先使用 `adb logcat -c` 清空之前的日志，然后运行 `adb logcat > log.txt` 即可将日志输出到 `log.txt` 。此时运行程序，直到出错，然后使用 `Ctrl + C` 结束日志输出。
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

---

## iOS/macOS/visionOS 上的日志分析
- 章节路径: `diagnostics/log-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-ios.html

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

---

## 微信小程序上的日志分析
- 章节路径: `diagnostics/log-wechat.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-wechat.html

# 微信小程序上的日志分析
本文介绍了在微信小程序 AR 环境下进行日志获取和分析的完整流程。
## 使用微信小程序 vConsole
由于微信小程序 AR 只能在实机运行和调试，使用 vConsole 观察实时输出是调试的关键，基础用法可参考[微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/usability/vConsole.html)。
### 实机调试中如何启用 vConsole
在 AR 界面点击右上角**第一个按钮** > 点击下方工具栏中的**开发调试** > 点击**打开调试** > 在弹出窗口中点击 **确定**以重启小程序。
![打开调试](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat01.png)
![重新打开后生效](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat02.png)
此后界面上会持续显示 **vConsole** 悬浮按钮。
![vConsole按钮](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat03.png)
点击 **vConsole** 按钮即可查看当前运行的所有日志：
![小程序日志](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat04.png)
### 如何区分日志来源
日志来源一般可以分为：
* **微信小程序系统日志**：通常在页面路由跳转、组件生命周期变化时触发，在 vConsole 中以蓝字显示。
* **xr-frame 日志**：由官方渲染框架打印，日志内容以 `[xr-frame]` 开头。
* **用户自定义日志**：由开发者通过 `console.log()` 等标准接口打印。
* **小程序框架错误日志**：由微信底层抛出，内容以 `MiniProgramError` 开头。
* **Mega 小程序插件日志**：由 Mega 小程序插件内部打印，日志内容以中括号包裹的类名开头（如 [MegaTracker]），目前主要在捕获异常时输出。
* **示例 1**：
![小程序日志举例1](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat05.png)
第一部分蓝字是系统日志，显示了页面路由及加载状态
第二部分以 `[xr-frame]` 开头，展示了渲染框架的生命周期信息。
第三部分是开发者自定义输出。
* **示例 2**：
![小程序日志举例2](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat06.png)
出现了 `[MegaTracker]`、`[EasyARSession(xrframe)]` 等类名开头的日志，这代表 Mega 插件捕获到了运行异常。
* **示例 3**：
![小程序日志举例3](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat07.png)
`MiniProgramError` 中出现了 `WAXRFrameRenderContext.js` 字样，说明使用 xr-frame 相关的接口或组件配置出现了问题。
* **示例 4**：
![小程序日志举例4](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat08.png)
该日志说明 mega 插件中的 `onCloudLocalization` 方法运行时出现了异常导致小程序框架抛出错误。
### Mega 小程序插件的日志格式
由 [dumpLog(signal)](../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_dumpLog_member_1_) 方法导出的日志以 `|` 分隔，内容依次是：
* **时间戳**：`ISO 8601` 标准格式，表示打印日志时的系统时间。
* **日志级别**：包括 `Info`、`Warning`、`Error`、`FatalError`。
* **类名**：以中括号包裹。
* **详细信息**：具体的日志描述。
* **调用者**：通常为 `Unspecified`（表示自然运行过程）；若为用户调用接口引发的异常则显示为 `User`。
* **运行阶段**：显示为 `Unspecified` 表示无需关注；显示其他字段则表示该异常发生在特定运行阶段。
![小程序日志](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat09.png)
## 如何记录和转发日志
介绍日志的获取和导出方案。
### vConsole 导出日志
在打印日志的位置点击右侧复制按钮导出。
### Mega 小程序插件 dump log 接口
通过调用 [dumpLog(signal)](../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_dumpLog_member_1_) 接口控制导出日志流程：
* **传入 `true`**：启动记录。
* **传入 `false`**：停止记录，并返回生成的 **文件临时路径 (tempFilePath)**。
通常建议将记录逻辑与 UI 按钮绑定，在开始记录时通过 [wx.showToast()](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html) 方法提示记录开始，在记录结束时通过 [wx.shareFileMessage()](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareFileMessage.html) 方法将记录的文件通过微信聊天转发。
```
/\*\*
\* 处理 Session 记录逻辑
\* @param signal true 为开始记录，false 为结束记录并转发
\*/
dumpLog(signal: boolean): void {
// 调用接口获取路径
const logPath = session.dumpLog(signal);
// signal 为 true 时，接口返回空字符串，表示正在记录
if (logPath.length == 0) {
wx.showToast({
title: '开始记录日志',
icon: 'success',
duration: 2000
});
return;
}
// signal 为 false 时，处理返回的文件路径
wx.shareFileMessage({
filePath: logPath,
success() {
wx.showToast({
title: '日志转发成功',
icon: 'success',
duration: 2000
});
},
fail() {
wx.showToast({
title: '日志转发失败',
icon: 'error',
duration: 2000
});
}
})
}
```
>
> 这个例子演示了如何在 xr-frame 组件中使用
`> session.dumpLog()
`> 方法记录并转发日志文件，并且给出相应的 Toast 提示。
>
> **重要事项**
如果使用 Mega 时遇到定位或跟踪相关的问题而不是程序异常，除了日志外，**请务必提供当时的录屏文件和 session dump 文件**。纯日志文件仅能提供侧面参考，录屏与 dump 数据才是排查问题的**核心依据**。
## 相关主题
* [如何记录与转发 Mega AR Session 的 dump 文件](../wechat/mega/session-dump.html)。

---

## Windows 上的日志分析
- 章节路径: `diagnostics/log-windows.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-windows.html

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

---

## 头显设备录屏：记录沉浸式 AR/MR 体验
- 章节路径: `diagnostics/recordings-headsets.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/recordings-headsets.html

# 头显设备录屏：记录沉浸式 AR/MR 体验
在使用增强现实（AR）或混合现实（MR）头显设备进行开发、测试或用户支持时，录屏是复现和分析问题的重要手段。然而，与移动设备不同，头显录屏涉及到透视（Passthrough）、注视点渲染（Foveated Rendering）等特殊技术，录屏画面通常并非完全等同于用户双眼直接所见的完整立体视图。因此，在解读录屏内容时，需特别注意其与实际人眼体验之间的差异。
## 为什么头显录屏存在视觉差异？
**用户必须特别注意**：头显设备的录屏画面并不完全等于您在镜片后看到的实际画面。如果在录屏中发现了异常，请务必结合实际感受进行描述，以免误导开发人员。
以下是主要差异点：
1. 分辨率与清晰度差异
* 录屏：通常是单眼（如左眼）1080p 或更低分辨率的视频流。
* 人眼：根据应用的不同，现代头显的单眼分辨率可达 2K 甚至更高。
* 影响：您在录屏中看到的文字、画面模糊，在头显内可能不存在；反之，您在头显内看到的微小边缘锯齿，录屏可能完全看不出来。
1. 视场角（FOV）差异
* 录屏：录制的画面通常是方形的。尤其在宽视场角设备中，边缘内容常被裁切。
* 人眼：人眼看到的画面是双眼显示的，视野更大。
* 影响：如果您的问题发生在视野边缘，录屏可能无法准确体现。
1. 注视点渲染（Foveated Rendering）影响
* 录屏：全屏视野中所有内容都会包含在内，包括低分辨率边缘区域。
* 人眼：人眼注视中心是高分辨率的，而非注视中心边缘是低分辨率的。
* 影响：您实际感觉画面很清晰，但回看录屏时发现部分区域是模糊的。这通常是正常现象，并非Bug。因此，在录屏时务必专注于要展示的部分，这将确保该区域是清晰的。
1. 帧率与刷新率影响
* 录屏：录制视频的帧率通常以 30FPS 或 60FPS 的帧率进行。
* 人眼：实际体验的屏幕刷新率可能达到 90Hz 或者 120Hz。
* 影响：非常轻微的帧率下降在录屏中可能无法察觉，但人眼会感受明显的“卡顿”或“眩晕感”。如果录屏看起来流畅但实际体验则不然，这通常是性能问题，在录屏后务必说明。
## OST 头显的特殊说明
**特别注意**：如果您使用的是 OST（Optical See-Through, 光学透视）头显，例如 Rokid、Xreal 等 AR 眼镜，使用录屏功能并不能录制到人眼看到的实景内容。
### 什么是 OST 设备？
OST 设备通过半透明的光学镜片直接将光线投射到您的眼中，虚拟内容则通过微型投影或波导叠加在视野中，让您同时看到真实世界和叠加的虚拟图像。它拍摄外部世界的摄像头仅用于空间定位，并不用于显示。由于这一机制，设备本身无法“录制”人眼所见的真实场景。
### OST 设备录屏的局限性
* 无法录制实景：OST 设备的录屏功能只录制虚拟内容层（GUI、3D 模型、UI 指针等）。
* 背景是黑的：您在电脑或手机上回放这段视频时，看到的将是纯黑色背景上的虚拟物体，完全丢失了真实环境的上下文。
* 遮挡关系丢失：如果虚拟物体应该被真实物体（如您的手、桌子）遮挡，在录屏中它们会悬浮在黑屏上，看起来像是错误的层级关系。
### 虚拟内容叠加的视觉误差问题
即使在理想环境下，OST 头显所呈现的虚拟内容与真实世界之间的对齐也不可避免地存在一定程度的视觉误差。这类误差并非总是由软件 bug 或跟踪失效引起，而往往源于设备物理特性与人类视觉系统的根本差异，部分误差在当前技术条件下无法完全消除。
在提交反馈时，注意区分以下情况：
* 光学对齐误差：
* 现象：当您移动头部时，虚拟物体似乎在“漂浮”或与真实物体的位置有微小偏差。
* 原因：用户透过光学镜片直视现实世界，而虚拟内容的渲染坐标系通常基于头部跟踪与环境理解系统（如 SLAM）构建。由于光学显示光路与用于空间定位的摄像头/IMU 之间存在物理偏移，且难以做到亚像素级联合标定，虚实对齐在边缘视野或近距离场景中尤为敏感。
* 人眼标定局限：
* 现象：虚拟物体看起来有重影（鬼影）、边缘模糊，或者感觉图像没有正确投射在空间中。
* 原因：OST 设备极度依赖精确的瞳距 (IPD) 和眼球位置标定。如果设备没有针对您的眼睛进行精确校准，或者您佩戴头盔的位置发生了偏移，光学引擎投射的光线就无法准确进入您的瞳孔。然而，即便设备存在校准，但校准过程基于有限采样点，难以精确匹配每位用户的眼球几何结构、角膜曲率及视觉感知习惯。微小的标定偏差会导致虚拟物体在深度或横向位置上出现系统性偏移。
* 个体视觉差异：
* 现象：不同用户对虚拟内容位置的主观判断可能不同。
* 原因：不同用户的视力(如近视、散光)、动态聚焦能力等都会影响观察虚拟内容叠加效果的主观判断，OST 设备可能缺乏实时眼动跟踪与个性化光学校正能力，因此无法针对每个用户动态补偿这些差异。
* 环境因素干扰：
* 现象：在明亮环境下虚拟内容变淡、看不清甚至不可见；在暗环境下虚拟内容过曝、甚至产生鬼影。
* 原因：OST 设备将微型投影或波导的虚拟光线与真实世界的环境光线直接叠加。如果真实环境过亮，会盖过微弱的虚拟光；反之亦然。这种光学伪影是 OST 设备的固有光学特性。
> **注意**
此类误差属于 OST AR 眼镜技术的固有特性，而非功能故障。在问题排查时，请区分“可修复的软件/跟踪问题”与“受硬件与生理限制的体验边界”。若用户反馈涉及轻微错位、边缘畸变或深度感知不一致，建议先确认是否处于设备标称的使用条件（如工作距离、光照范围、校准状态）内。
### 如何处理 OST 设备的反馈？
如果您在使用 OST 设备时遇到视觉问题，在排除以上设备局限带来的因素之后，您可以进行录屏进行反馈。但单纯提交录屏内容通常是不够的：
1. 配合照片：请使用手机拍摄一张您透过镜片看到的实际画面照片（称为“眼视角照片”）。这能展示虚拟物体与真实环境的相对位置。
2. 描述环境：详细描述您所处的环境（光照条件、背景颜色、是否存在动态如行人等），因为 OST 的显示效果极度依赖环境光。
## 常见头显设备的录屏方法
> **注意**
录屏过程中设备可能降低渲染帧率或分辨率，影响对流畅度和跟踪稳定性的判断。建议在复现问题后尽快录制，避免长时间运行影响结果。
### Apple Vision Pro
1. 抬头看屏幕顶部，直到看到控制中心点。专注于这一点并单击。
2. 注视并点击 控制中心 > “录制我的视野”按钮 ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-record-button.png) 开始录制。
3. 若要停止录制，打开控制中心，然后再次轻点“录制我的视野”。
4. 您的视野录制会存在“照片”App ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-photos.png) 中。
### PICO 4 Ultra Enterprise
1. 打开控制中心 > 设置 > 通用 > 投屏、录屏与截屏，在“录屏和截屏”中选择录屏模式为“空间”。
2. 短按手柄的 Home 键，在屏幕弹出的菜单中选中“录屏”按钮，扣动扳机键开始录屏。
3. 此时系统会有开始倒计时提示，立即退回至待录制应用的界面，在倒计时结束后自动开始录制。
4. 再次短按手柄的 Home 键，重复选择“录屏”按钮即可停止录制。
5. 您的录制文件默认保存在设备的“内部存储/DCIM/ScreenRecord”目录。
### Rokid AR Studio
1. 进入桌面，找到底部状态栏，点击用户头像旁边的“快捷设置”区域。
2. 在弹出的窗口中点击“录制”按钮，立即退回至待录制应用的界面。系统自动开始录制。
3. 点击 Station Pro 上 X 按钮退回桌面。再次点击“快捷设置”区域的“录制”按钮即可停止录制。
4. 您的录制文件默认保存在设备的“内部共享存储空间/ScreenRecorder”目录。
### XREAL Air2 Ultra
1. 在 Beam Pro 屏幕上下滑呼出眼镜的控制中心，点击上方的“录屏”按钮。
2. 此时系统会有倒计时提示，立即退回至待录制应用的界面。
3. 点击屏幕上方悬浮的红色“停止”按钮即可停止录制。
4. 您的录制文件默认保存在设备的“内部共享存储空间/Movies/Record”目录。
## 最佳实践建议
使用头显录屏反馈问题时，关注以下几点：
* 提交时明确标注设备型号、录屏方式及环境因素。
* 若问题涉及深度、遮挡或跟踪抖动，补充文字描述人眼实际观察到的现象，因为录屏可能无法准确呈现。
* 对于关键场景，可配合外部摄像机拍摄用户佩戴头显时的实景操作，以提供更全面的上下文。
头显录屏虽便捷，但始终是对体验的近似还原。最可靠的诊断仍需结合日志、传感器数据与用户主观反馈。有关日志采集方法，请参阅:
* [Android 日志记录](log-android.html)
* [iOS 日志记录](log-ios.html)
* [Unity 日志记录](log-windows.html)

---

## 截图与录屏：记录 AR 视觉异常的重要手段
- 章节路径: `diagnostics/recordings.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/recordings.html

# 截图与录屏：记录 AR 视觉异常的重要手段
在增强现实（AR）应用的使用过程中，您可能会遇到诸如模型错位、内容跳动、跟踪丢失、遮挡异常等视觉体验问题。由于 AR 内容的效果好坏高度依赖于设备、环境光照和算法表现，这些问题往往具有瞬时性和上下文依赖性，单纯的通过模糊的文字（如“模型飘走了”）难以准确传达问题的具体细节。因此，及时使用截图或录屏功能记录异常现象，对于后续的问题诊断、技术复现和用户体验优化至关重要。
## 为什么需要截图与录屏？
当 AR 应用的表现与预期不符时，使用截图和录屏功能具有以下关键作用：
* **精准还原问题场景**
截图能捕捉异常发生的精确瞬间（如特定的内容跳动或模型穿模），而录屏则能完整记录导致异常的整个过程和环境交互。
* **辅助开发团队技术诊断**
通过查看您捕获的视觉证据，技术支持团队或开发人员可以快速定位问题根源（例如：是设备性能问题、SLAM 跟踪丢失，还是渲染管线错误），从而避免了繁琐的猜测和反复询问。
* **保留设备环境信息**
录屏不仅包含应用内的画面，通常还会包含设备的系统状态栏（时间、电量、网络信号），这对于诊断设备过热降频或网络波动导致的加载问题至关重要。
## 常见移动设备上的操作方法
在截图或录屏前，请确保 AR 场景已经加载完毕，并且异常行为正在发生或即将发生。请尽量保持设备稳定，以便画面清晰可辨。
### 通用操作原则
* 截图：适用于捕捉静态的视觉错误（如内容穿模、模型错位）。建议连续拍摄多张，以覆盖异常变化的不同阶段。
* 录屏：适用于捕捉动态行为（如跟踪丢失导致的画面抖动、交互时的卡顿）。建议录制时长控制在 15-30 秒，聚焦于问题发生的核心过程。
### iOS 设备（iPhone/iPad）
#### 截图：
* 带 FaceID 的设备：快速同时按下和松开 电源键 + 音量上键。
* 带 Home 键的设备：快速同时按下和松开 电源键 + Home 键。
* 截图将自动保存至“照片”App ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-photos.png)。
#### 录屏：
1. 进入 设置 > 控制中心 > 更多控制，添加“录屏”。
2. 从屏幕右上角下滑打开控制中心。
3. 点击 录屏按钮 ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-record-button.png) 开始录制；点击 停止按钮 ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-record-stop-button.png) 停止录制。
4. 如需录制系统声音或麦克风音频，长按录屏按钮进行设置。
5. 录制视频保存在“照片”App ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-photos.png) 中。
> **注意**
* 录屏时确保 设置 > 控制中心 > App内访问 是打开状态。
* 在录屏时可能因性能限制导致效果下降，建议在复现问题后尽快录制，避免长时间运行影响结果。
### Android 设备（以主流品牌为例）
#### 截图：
* 通用方法：快速同时按下和松开 电源键 + 音量下键。
* 部分厂商支持手势截图（如三指下滑）或智能助手快捷方式。
* 截图将自动保存至“相册 > 截屏”中。
#### 录屏：
* 原生 Android（Android 11 及以上）：
1. 下拉通知栏，找到“屏幕录制”快捷图标（若无，可在“编辑”中添加）。
2. 点击开始录制，可选择是否包含麦克风音频。
3. 再次点击屏幕左上角的录制图标停止录制。
4. 录制视频保存在“相册 > Movies”。
* 厂商定制系统（如 Samsung One UI、HyperOS、ColorOS、OriginOS）：
1. 通常在快捷面板中提供录屏入口（若无，可点加号添加）。
2. 点击开始录制。
3. 点击屏幕上方（不同厂商可能有所不同）的停止按钮停止录制。
4. 录制视频保存在“相册 > 录屏”中。
> **提示**
具体路径示例：
* 三星：下滑手机顶帘 > 录屏工具
* 小米/Redmi：下拉通知栏 > 屏幕录制
* OPPO/Realme：滑动屏幕顶部通知栏或下拉菜单栏 > 屏幕录制
* VIVO/iQOO: 屏幕顶部右侧下滑（早期机型为底部上滑）> 超级截屏 > 录制屏幕
* 华为：屏幕顶部右侧下滑 > 屏幕录制
* 荣耀：状态栏向下滑出通知面板，继续向下滑动出整个通知面板 > 屏幕录制
> **注意**
* 部分 Android 设备在运行高负载 AR 应用时可能限制后台录屏权限，请确保录屏前关闭省电模式，并授予必要权限。
* 在录屏时可能因性能限制导致效果下降，建议在复现问题后尽快录制，避免长时间运行影响结果。
## 最佳实践建议
通过熟练掌握上述操作，您可在 AR 体验出现异常的第一时间捕获关键证据，显著提升问题沟通与解决效率。建议在提交技术支持请求时，同时提供截图/录屏、设备型号、操作系统版本、EasyAR SDK 版本及 AR 应用日志，以构建完整的故障上下文。
有关日志采集方法，请参阅:
* [Android 日志记录](log-android.html)
* [iOS 日志记录](log-ios.html)
* [Unity 日志记录](log-windows.html)

---

## 录制 EIF 数据：复现 AR 问题的高保真依据
- 章节路径: `diagnostics/simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/simulation.html

# 录制 EIF 数据：复现 AR 问题的高保真依据
在增强现实（AR）应用中，某些复杂的空间定位问题（如跟踪抖动、虚实错位、内容飘移等）往往难以仅通过录屏或日志完整还原。为此，我们提供了EIF数据录制功能———一种专有的高保真数据转储格式，可同步记录以下关键信息：
* 设备基本信息（型号、系统、SDK 版本等）
* 包含时间戳的摄像头图像帧
* 设备的相机内参矩阵、外参矩阵
* IMU 传感器数据
* 外部辅助输入的额外数据（如 GNSS）
## 为什么录制EIF数据至关重要？
> **重要事项**
**能够复现问题的 EIF 数据是无价的。**
EIF 数据能够完整重现问题发生时的详细上下文，使开发团队在离线环境中精确复现用户所遇场景，极大提升问题定位效率。相比录屏或日志，EIF 具备以下优势：
1. 精准复现：开发人员可在调试工具中直接回放EIF数据，重现您遇到的 Bug。
2. 底层诊断：通过全面的分析各类数据（图像、传感器、外部输入等），开发人员可以判断问题出在技术的哪个环节。
3. 节省时间：避免了漫长的沟通循环，大幅缩短从报告问题到解决问题的周期。
## 如何录制 EIF 数据
EasyAR 提供了两种 EIF 数据录制的方式。
1. 直接使用 SDK 提供的 API 接口，在您的应用中实现 EIF 数据录制的功能。
2. 使用官方提供的 Mega Toolbox App。通常适用于进行 EasyAR Mega 的开发和问题反馈。
具体操作步骤请参考我们的技术文档，获取针对您的使用方式以及设备的操作指南。
> **提示**
访问以下链接查看调用 API 接口实现应用内录制 EIF 的功能：[输入帧录制和模拟运行](../simulation/simulation.html)。
访问以下链接查看使用 Mega Toolbox App 的操作指南：[使用 Toolbox 录制手机 EIF 文件](../../mega/data-collection/simulation/toolbox.html)。
简要录制流程概览（以 Mega Toolbox App 为例）：
1. 打开 Mega Toolbox App，点击“现场定位测试&定位问题反馈数据录制”。
2. 登录您的账号，选择您的定位库，并开始测试。
3. **尝试复现您的问题**。找到一个可以稳定复现问题的操作模式（如设备朝向、浏览方式、拍摄点位等）。
4. 一切准备就绪后，点击红色“录制”按钮开始录制。
5. 问题出现后，点击红色“停止并保存”按钮。
6. 系统将自动生成一个 EIF 文件，将设备连接电脑导出至本地存储后提交。
> **注意**
EIF 文件可能较大（数百 MB 至数 GB），建议仅录制**包含问题的核心片段**（通常 10–30 秒足够）。
## 最佳实践建议
为确保您的反馈能被高效处理，请在提交时**同时包含以下四类信息**：
|信息类型|说明|
|**EIF 数据文件**|核心诊断依据，务必包含问题复现过程|
|**主观现象描述**|清晰说明您观察到的行为（如“导航箭头在向左转弯时突然跳到天花板”）|
|**录屏或截图**|辅助可视化问题，直观地展示“用户最终看到的画面是怎样的”|
|**辅助上下文信息**|包括：
• 您的设备型号与操作系统版本
• 您的应用所使用的 EasyAR SDK 的版本号
• 问题产生的环境描述（室内/室外、光照、空间大小）
• Mega 类应用需要额外提供定位库信息，可在 Unity 工具中导出
• CRS 云识别类应用需要额外提供云识别库的信息|
> **提示**
示例：“在 Apple Vision Pro（visionOS 26）上使用 EasyAR Sense Unity Plugin 4000.0.1，在室内商场进行导航，在某个位置导航路径突然发生错误。已录制 EIF 文件：`avp\_wrong\_path\_20251218.mkveif`，附录屏、环境照片及定位库信息：`MegaStudio\_ServiceInfo\_myaccount\_2025-12-18\_10-33-26.json`。”
通过提供上述完整信息包，您将显著加速问题分析与修复进程。感谢您的配合！
