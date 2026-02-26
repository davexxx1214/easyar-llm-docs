---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/developer-mode.html
---

开发者模式 | EasyAR 文档
**
##### Table of Contents
**
# 开发者模式
开发者模式用于设定是否启用运行时诊断面板。诊断面板可用于切换调试信息是否显示以及录制 EIF、EED 文件。
![diagnostics developer mode 1](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode.png)
## 开发者模式诊断面板
开发者模式诊断面板默认通过快速点击屏幕 8 次打开（可通过修改 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 来更改）。打开后会在屏幕右侧显示诊断面板。
![diagnostics developer mode 2](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode-panel.png)
诊断面板功能如下：
* session: session 信息控制，该信息用于了解 session 的运行状态和问题
* Toggle: 切换 [SessionDump](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionDump) 消息显示
* copy: 复制当前帧 session dump 信息
* eif: eif 录制控制，eif 文件用于 [Unity AR 模拟运行](../simulation/simulation.html)
* Auto/Obsolete: 切换 eif 格式，其中 Obsolete 表示使用原始 EIF 格式，Auto 表示根据平台支持情况自动选择 EIF MKV 格式或者原始 EIF 格式
* rec: 启动/停止 eif 录制
* eed: eed 录制控制，eed 文件用于抓取一些运行时的关键数据提供给 EasyAR 技术支持进行问题分析
* rec: 启动/停止 eed 录制
## 修改开发者模式开关
可以通过 session 上的 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 组件在编辑器中配置，或是使用 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 接口在脚本中配置。
可以选择的模式如下：
* [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default)：手机上快速点击屏幕8次进入开发者模式并会在屏幕右边打开诊断面板。
* [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom)：可以通过 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 接口来自定义开启开发者模式切换条件，未定义时诊断面板将无法在运行时打开。
可以通过设置 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 为 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom) 并且不修改 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 来禁止开启开发者模式。
比如，下面的代码展示了如何在脚本中禁止开启开发者模式：
```
`Session.Diagnostics.DeveloperModeSwitch = DiagnosticsController.DeveloperModeSwitchType.Custom;
`
```
##### 提示
* 建议在开发和测试阶段使用默认配置 [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default)。
* 建议在发布上线阶段使用配置 [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default) 或 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom)。
* 建议在使用 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom) 模式时，修改 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 以提供其它方式启用诊断面板，或提供其他自定义的方式收集运行时数据。
## 相关主题
* [录制 EED dump 文件](event-dump.html)
* [UI 消息](ui-messages.html)
* [Unity AR 模拟运行](../simulation/simulation.html)