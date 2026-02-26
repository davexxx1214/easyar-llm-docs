---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-wechat.html
---

微信小程序上的日志分析 | EasyAR 文档
**
##### Table of Contents
**
# 微信小程序上的日志分析
本文介绍了在微信小程序 AR 环境下进行日志获取和分析的完整流程。
## 使用微信小程序 vConsole
由于微信小程序 AR 只能在实机运行和调试，使用 vConsole 观察实时输出是调试的关键，基础用法可参考[微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/usability/vConsole.html)。
### 实机调试中如何启用 vConsole
在 AR 界面点击右上角**第一个按钮** &gt; 点击下方工具栏中的**开发调试** &gt; 点击**打开调试** &gt; 在弹出窗口中点击 **确定**以重启小程序。
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
`/\*\*
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
`
```
>
> 这个例子演示了如何在 xr-frame 组件中使用
`> session.dumpLog()
`> 方法记录并转发日志文件，并且给出相应的 Toast 提示。
>
##### 重要事项
如果使用 Mega 时遇到定位或跟踪相关的问题而不是程序异常，除了日志外，**请务必提供当时的录屏文件和 session dump 文件**。纯日志文件仅能提供侧面参考，录屏与 dump 数据才是排查问题的**核心依据**。
## 相关主题
* [如何记录与转发 Mega AR Session 的 dump 文件](../wechat/mega/session-dump.html)。