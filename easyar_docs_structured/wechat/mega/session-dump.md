---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-dump.html
original_file: doc--zh-cn--develop--wechat--mega--session-dump.md
normalized_at: 2026-02-27
---
# 如何记录与转发 AR Session dump 文件
AR Session dump 文件是 EasyAR 团队排查定位、跟踪问题的核心依据。
## 开始之前
* 了解什么是 [AR Session](session.html)。
* 确保您的项目已经[启用 EasyAR Mega](integration.html)。
## 什么是 AR Session dump 文件
> **重要事项**
AR Session dump 文件是微信小程序上分析和解决 Mega 定位、跟踪问题**最重要的依据**。
AR Session dump 文件记录了小程序进行 Mega 定位请求时的关键时空上下文。
## 如何记录与转发
通过调用 `session.dumpSession(signal: boolean)` 接口控制记录流程：
* **传入 `true`**：启动记录。
* **传入 `false`**：停止记录，并返回生成的 **文件临时路径 (tempFilePath)**。
通常建议将记录逻辑与 UI 按钮绑定，在开始记录时通过 [wx.showToast()](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html) 方法提示记录开始，在记录结束时通过 [wx.shareFileMessage()](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareFileMessage.html) 方法将记录的文件通过微信聊天转发。
```
/\*\*
\* 处理 Session 记录逻辑
\* @param signal true 为开始记录，false 为结束记录并转发
\*/
dumpSession(signal: boolean): void {
// 调用接口获取路径
const recordPath = session.dumpSession(signal);
// signal 为 true 时，接口返回空字符串，表示正在记录
if (recordPath.length == 0) {
wx.showToast({
title: '开始记录数据',
icon: 'success',
duration: 2000
});
return;
}
// signal 为 false 时，处理返回的文件路径
wx.shareFileMessage({
filePath: recordPath,
success() {
wx.showToast({
title: '记录转发成功',
icon: 'success',
duration: 2000
});
},
fail() {
wx.showToast({
title: '记录转发失败',
icon: 'error',
duration: 2000
});
}
})
}
```
>
> 这个例子演示了如何在 xr-frame 组件中使用
`> session.dumpSession()
`> 方法记录并转发 AR Session dump 文件，并且给出相应的 Toast 提示。
>
> **注意**
由于小程序本地空间限制（通常为 200MB），建议单次录制时间不要过长，且最长录制时间不能超过 10 分钟。
## 相关主题
* [使用微信小程序 Mega Toolbox 记录与转发 session dump 数据](../../../mega/data-collection/wechat/toolbox-dump.html)
* [使用你的小程序录制 AR Session dump 文件](../../../mega/data-collection/wechat/wechat-dump.html)
* [微信小程序问题报告注意事项](../diagnostics/report.html)
