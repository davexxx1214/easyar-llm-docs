---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/report.html
---

问题报告 | EasyAR 文档
**
##### Table of Contents
**
# 问题报告
##### 注意
EasyAR Mega 用户请务必阅读 [Mega 常见问题](../../mega/faq.html) 和 [问题报告与反馈](../../mega/report.html) 。
##### 注意
在反馈问题之前，请务必使用最新版本的 SDK 并在 sample 中复现问题，很多问题可能会在新版本中得到修复，EasyAR 主要支持在最新版本上能够复现的问题。此外，Unity 本身也会存在一些问题，一些 Unity 的问题可以通过尝试删除 Unity Library 文件夹、Unity 生成的 XCode 工程来解决。
请使用插件内置的 `提问` 功能来辅助检查和收集反馈信息。
![diagnostics report ask dialog options](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
这个窗口可以从 `EasyAR &gt; Sense &gt; 提问` 菜单打开
![diagnostics report ask menu](https://doc-asset.easyar.com/develop/mega/media/unity-question.png)
打开后信息是不全的，需要选择使用的环境和功能
![diagnostics report ask dialog](https://doc-asset.easyar.com/mega/troubleshooting/media/localization_failure6.png)
如需反馈手机或头显上的问题，请复制Session Dump信息日志
![diagnostics report ask dialog session dump setting](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-report-3.png)
然后填写到文本框中
![diagnostics report ask dialog session dump filling](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-report-4.png)
最后根据窗口提示完成所有操作后，点击右上角的复制按钮复制所有信息
![diagnostics report ask dialog options](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
请注意，这个界面不只是用来获取报告的，同时它也会引导你进行初步的问题筛查，请务必认真使用。
如遇到崩溃，请参考 崩溃分析（[Android](../../diagnostics/crash-android.html) [iOS/macOS/visionOS](../../diagnostics/crash-ios.html) [Windows](../../diagnostics/crash-windows.html)） 获取相关信息，一般来说如果没有完整的信息问题报告将是无效的。