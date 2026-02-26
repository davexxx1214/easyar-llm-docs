---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/simulation.html
---

Unity AR 模拟运行 | EasyAR 文档
**
##### Table of Contents
**
# Unity AR 模拟运行
Unity 的 AR 开发有时受限于设备能力差异，经常需要打包到手机上进行测试。在使用一些与真实环境有关的功能时（比如稀疏空间地图或 Mega），AR 功能需要真实的环境才能使用，这往往需要在特定的环境驻场开发和测试。为了提高开发效率，EasyAR 提供了模拟运行的功能，可以在 Unity 编辑器中模拟 AR 设备的工作效果。
基于 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html)，Unity 中可以使用这些功能：
* [录制 EIF 文件](recording.html)
在 Unity 中录制 EIF 文件，以便用于模拟运行。
* [使用 EIF 文件模拟运行](playback.html)
在 Unity 中使用 EIF 文件进行模拟运行，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
* [使用 session 验证工具](tool.html)
使用 session 验证工具，在编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
相关功能组件包括：
* [FrameRecorder 组件](comp-FrameRecorder.html)
该组件提供了录制 EIF 的功能。
* [FramePlayer 组件](comp-FramePlayer.html)
该组件提供了使用 EIF 文件进行模拟运行的功能。
* [DiagnosticsController 组件](../diagnostics/comp-DiagnosticsController.html)
该组件是诊断系统的核心控制器，提供了 session 验证工具。