---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/ui-messages.html
---

UI 消息 | EasyAR 文档
**
##### Table of Contents
**
# UI 消息
EasyAR Sense Unity Plugin 运行时有三类消息。
* 运行异常，包含 Sense Error、Session Error、Error、Warning
* Session Dump
* EasyAR Mega 开发特殊异常
您可以根据需要调整前两类消息的输出方式。可以通过 session 上的 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 组件在编辑器中配置，或是使用 [DiagnosticsController.MessageOutput](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_MessageOutput) 接口在脚本中配置。
![diagnostics ui messages](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message.png)
##### 提示
在 4000 版本中，如果场景由老版本插件创建，打开场景时 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 会被自动添加到 session 中。部分 Unity 版本中可能不会自动添加，在这些 Unity 版本中，[DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 会在运行时自动以默认值创建。
## 运行异常
插件运行时有时会收到内部组件发现的一些问题，以消息形式出现在系统中。这些消息有些可能是无法继续使用的严重故障，有些可能是故意触发的，有些可能是设备不受支持等等，按严重级别从高到低分为如下几类：
* [SenseError](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SenseError)：EasyAR Sense 错误，通常与 EasyAR Sense license 有关。
* [SessionError](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionError)：ARSession 错误，通常与设备不支持一些功能或错误的配置有关。
* [Error](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_Error)：其它错误信息
* [Warning](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_Warning)：警告信息
由于 Unity 开发的特殊性，我们默认会将这些消息显示在 UI 上，以辅助开发。
可以在编辑器或脚本中控制这些消息如何展示，可以选择的输出模式如下：
* [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)：输出到UI和日志。在头显上显示在眼前5米处。
* [Log](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_Log)：输出到系统日志。
##### 提示
* 建议在开发测试阶段使用默认配置 [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)。
* 建议在发布时将选项改成 [Log](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_Log)， 也可以保留 [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)，但这些UI消息通常对终端用户是不友好的。
* 建议在运行前 [判断 session 可用性和设备支持](../fundamentals/session-assemble.html) 并对不支持的设备进行合理提示。
### Sense Error
Sense Error 是一类特殊的错误，出现错误时 EasyAR 功能无法继续使用。常见原因：
* License 未正确配置或校验失败。该错误可以通过使用正确的 license 重新初始化来恢复。
* 部分设备（包括 AR Foundation、AR Engine 等所有使用自定义相机的设备或各种头显）上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）超过固定的有限时间。该错误无法恢复。
### Session Error
Session Error 是当前 ARSession 无法继续工作的错误。修改配置并重新运行 ARSession 可能可以解决这些错误。这些错误一般是由于您的配置错误、启动流程中抛出了异常导致组装中断、设备不受当前 ARSession 配置支持或是运行过程中 ARSession 组件丢失等导致的。
常见情况有：
* Session 组装错误：比如设备不受支持或支持设备的 Frame Source 没有正确配置在 ARSession 中等。
* Session 启动错误：云服务配置信息错误导致创建云服务功能出错，或配置信息未填写（包括 Mega 服务、云识别服务、SpatialMap 服务）等。
* Session 运行中错误：ARSession 组件被外部销毁，URP 环境下未正确配置 RendererFeature 等。
通常来说，配置错误以及启动流程中的异常导致组装中断都应该在开发过程中避免。设备不支持的情况主要出现在需要运动跟踪能力的功能上，需要参考 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 了解哪些功能需要注意设备支持，并在开发阶段选择合适的设备进行调试。
## Session Dump
[SessionDump](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionDump) 消息展示的是插件运行时收集的 ARSession 的运行状态，包括各个组件的一些关键状态。这些状态信息对了解 EasyAR 的运行以及分析问题有很大帮助。
可以在编辑器或脚本中控制这些状态如何展示，可以选择的输出模式如下：
* [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI)：显示在 UI 并每帧更新。在头显上，显示在眼前5米处。
* [Log](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_Log)：输出到系统日志，由于每帧都输出，对运行性能是有影响的，建议在开发或测试时使用。
* [None](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_None)：不输出。
##### 提示
* 建议在开发测试阶段使用默认配置 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI)，上面显示的信息是与 EasyAR 工作人员进行沟通所必不可少的。
* 建议在正式上线后再修改为 [None](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_None)，并保留打开 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI) 的软件开关，或通过其它系统进行数据收集。在向 EasyAR 反馈问题时， EasyAR 会向您或您的用户索取这些信息，以判断应用运行状态。
* 在绝大多数情况下，应用上线后运行出问题，应用端还是需要首先进行问题排查和分析，在排除应用问题并获取足够信息后反馈的问题才能较好解决。日志收集和分析的第三方 SDK 和平台比较多，建议上线前使用。如果您没有使用这些平台的经验或资源，保留打开 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI) 的开关（比如使用隐藏开关）让用户反馈看到的信息将是比较简单的。
## EasyAR Mega 开发特殊异常
Mega 开发中，还有一类无法控制的警告信息，这类信息会在满足特定配置条件时显示在 UI 上，开发者无法直接关闭。
建议关注信息本身，文字上写明了出现的原因和配置方法。开发者需要了解不同配置对不同使用方式的要求并根据开发进展合理选择。
这类信息是故意展示的，因为在特定使用条件下，这些功能用来辅助内容流程开发，但同时无法获取合理的运行结果，注意不要带着信息上线。
## 相关主题
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)
* [开发者模式](developer-mode.html)