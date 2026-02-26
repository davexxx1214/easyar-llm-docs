---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/diagnostics.html
original_file: doc--zh-cn--develop--unity--getting-started--diagnostics.md
normalized_at: 2026-02-27
---
# 充分利用 UI 诊断信息和工具
本文介绍了如何快速配置和使用 UI 诊断信息和开发者模式工具，以便在开发和测试阶段更好地调试和优化应用。
## 阅读 UI 消息
默认配置下，运行 EasyAR Sense Unity Plugin 应用时，诊断信息会通过 UI 消息显示在屏幕偏上位置，方便开发者了解 session 的运行状态和问题。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message-ui.png)
> **提示**
这些文字不是水印，可以根据需要显示或隐藏。
这些信息可以帮助开发者了解 session 的运行状态和问题，建议在开发和测试阶段保持显示。
可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Message Output` 来配置 UI 消息的显示方式。其中 `Message Output` > `Session Dump` 可以控制 session 状态信息的显示，其它选项可以控制不同级别的诊断消息的显示方式。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message.png)
通常建议在开发和测试阶段，进行以下配置：
* Message Output > Session Dump： `UI`
* Message Output > Sense Error： `UIAndLog`
* Message Output > Session Error： `UIAndLog`
* Message Output > Error： `UIAndLog`
* Message Output > Warning： `UIAndLog`
在发布上线阶段，进行以下配置：
* Message Output > Session Dump： `None`
* Message Output > Sense Error： `Log`
* Message Output > Session Error： `Log`
* Message Output > Error： `Log`
* Message Output > Warning： `Log`
## 使用开发者模式工具
默认配置下，运行 EasyAR Sense Unity Plugin 应用时，快速点击屏幕 8 次会在靠屏幕右边中间位置弹出开发者模式面板，方便开发者查看和调试 session 的运行状态以及录制用于模拟运行的数据。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode-panel.png)
* 可以通过 `session` 右边的切换按钮来切换屏幕上方信息的显示与否。
* 可以通过 `eif` 右边的 `rec` 按钮来启动或停止 EIF 录制功能。录制的 EIF 文件会保存在应用的持久化数据路径中，可以通过 `Application.persistentDataPath` 来获取该路径。
如果要禁用开发者模式面板，可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Developer Mode Switch` 为 `Custom`。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode.png)
通常建议在开发和测试阶段，进行以下配置：
* Developer Mode Switch： `Default`
在发布上线阶段，进行以下配置：
* Developer Mode Switch： `Default` 或 `Custom`
如果选择 `Custom`，建议以其它方式保证线上应用可以使用诊断面板或自定义的方式收集运行时数据。
## 延伸阅读
* [诊断功能简介](../diagnostics/diagnostics.html)
* [UI 消息](../diagnostics/ui-messages.html) 介绍了如何使用 UI 消息来显示 session 状态
* [开发者模式](../diagnostics/developer-mode.html) 介绍了如何使用开发者模式进行调试
