---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/comp-DiagnosticsController.html
original_file: doc--zh-cn--develop--unity--diagnostics--comp-DiagnosticsController.md
normalized_at: 2026-02-27
---
# Diagnostics Controller 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.DiagnosticsController.html)
>
探索 DiagnosticsController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/diagnostics/media/comp-DiagnosticsController.png)
默认条件下组件截图。
DiagnosticsController 组件窗口由三个部分组成：组件配置、Assembly 预览和 session 验证工具。
## 组件配置
|属性|描述|
|**Developer Mode Switch**|开发者模式开关。可以使用默认的开关（点击屏幕 8 次触发）或自定义一个开关，或提供开发者模式的等价替代。|
|**Message Output**|消息输出选项。|
|*Session Dump*|会话状态转储输出方式。选项：
* UI：显示在UI并每帧更新。在头戴设备上，显示在眼前5米处。
* Log：输出到系统日志，由于每帧都输出，对运行性能是有影响的，建议在开发或测试时使用。
* None：不输出。|
|*Sense Error*|Sense Error 输出方式，通常与 EasyAR Sense license 有关。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Session Error*|Session Error 输出方式，通常与设备不支持一些功能或错误的配置有关。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Error*|Error 输出方式。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Warning*|Warning 输出方式。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Show Editor Dialog On Fatal*|编辑器中，Sense Error 或 Session Error 时显示对话框。|
## Assembly 预览
Assembly 预览只在编辑模式可见。根据 [AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 显示当前 session 在组装时会选择的组件，这个是一个参考，与 session 运行时最终组装的组件可能不同。
## session 验证工具
[session 验证工具](../simulation/tool.html)用于帮助开发者在 Unity 编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
