---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-android.html
---

Android 上的崩溃分析 | EasyAR 文档
**
##### Table of Contents
**
# Android 上的崩溃分析
关于 原生(Android) 和 Unity(Android)上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在 Android Studio 中调试 Android 的 Native 程序时，需要在 Configuration 设置中将 Debugger - Debug type 改为Dual (Java + Native)。
![crash Android configuratio](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-configuration.png)
在 Android Studio 中调试时需要的信息如下图。
![crash Android stack](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-stack.png)
在 lldb 中输入 `bt` ，可以获得崩溃原因和代码运行栈，如下
```
`(lldb) bt
\* thread #16, name = 'samples.helloar', stop reason = signal SIGSEGV: invalid address (fault address: 0x9c40)
\* frame #0: 0x0000004922f3a1d8 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol3056$$libEasyAR.so + 6088
frame #1: 0x0000004922f38568 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol3054$$libEasyAR.so + 288
frame #2: 0x0000004922f347f8 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol2876$$libEasyAR.so + 332
frame #3: 0x00000049be2390c8 libc.so`\_\_pthread\_start(void\*) + 40
frame #4: 0x00000049be1f04f8 libc.so`\_\_start\_thread + 72
`
```
当代码运行栈中存在 `libEasyAR.so` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
在 lldb 中输入 `image dump sections libEasyAR.so`，可以获得动态库 `.text` 节加载地址，如下
```
`(lldb) image dump sections libEasyAR.so
...
SectID Type Load Address Perm File Off. File Size Flags Section Name
...
0x00000010 code [0x0000004922e30cfc-0x0000004923654558) r-x 0x00256cfc 0x0082385c 0x00000006 libEasyAR.so..text
...
`
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