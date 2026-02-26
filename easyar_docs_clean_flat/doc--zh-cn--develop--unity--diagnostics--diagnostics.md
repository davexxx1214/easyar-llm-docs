---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/diagnostics.html
original_file: doc--zh-cn--develop--unity--diagnostics--diagnostics.md
normalized_at: 2026-02-27
---
# Unity 开发中的问题诊断和报告
在开发基于 Unity 的插件或应用时，难免会遇到运行异常或逻辑错误。为了帮助开发者快速定位和解决问题，Unity Plugin 提供了一系列内置的诊断与调试工具。本章将介绍这些常用的调试手段和辅助功能，涵盖从实时日志查看、开发者模式启用，到问题数据采集与上报的完整流程。
* [UI 消息](ui-messages.html)
介绍运行时系统如何通过 UI 层面展示错误、警告和其他诊断信息，并说明这些消息的分类标准与含义，便于快速识别问题类型。
* [开发者模式](developer-mode.html)
说明如何在应用运行期间激活开发者模式，以及该模式下可使用的高级调试功能：可视化调试图层、EIF/EED 文件录制。
* [录制 EED dump 文件](event-dump.html)
详细讲解如何触发并录制 EED 文件，该文件包含关键事件、传感器数据、系统状态等上下文信息；同时说明如何从设备中导出和使用这些 dump 文件进行离线分析。
* [问题报告](report.html)
指导用户如何规范地提交问题反馈，包括应附带的日志、dump 文件、复现步骤等，以提高问题处理效率。
相关功能组件包括：
* [DiagnosticsController 组件](comp-DiagnosticsController.html)
该组件是诊断系统的核心控制器，负责协调日志记录、状态监控、dump 生成等功能。
