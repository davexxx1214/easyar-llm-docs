---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-ios.html
original_file: doc--zh-cn--develop--diagnostics--crash-ios.md
normalized_at: 2026-02-27
---
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
