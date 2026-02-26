---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/diagnostics/report.html
---

微信小程序问题报告 | EasyAR 文档
**
##### Table of Contents
**
# 微信小程序问题报告
为了能够快速、准确地定位您在开发或使用使用 EasyAR 提供的能力（Mega 或 CRS）的微信小程序时遇到的问题，在提交反馈前参考本指南提供必要的信息和数据以显著减少排查问题的往返沟通时间。
## 问题预检
在报告问题前，可以先尝试通过一些基本手段或阅读文档快速解决问题。
**使用 Mega 插件：**
* 确认使用 2.x 版本的小程序插件（1.x 版本的 Mega 小程序插件已不再维护）
* 阅读 [Mega 插件已知问题和限制](../mega/known-issues.html)确认是否为已知问题。
* 参考修改为 [Mega Sample](../mega/sample.html) 或 [CRS Sample](../cloud-recognition/sample.html) 中的实现方式，确认问题依然存在。
## 反馈问题时需要的数据
一份完整的问题报告通常需要包含以下数据，使 EasyAR 开发团队能够进行准确的分析。
### 运行环境数据
* **设备型号**：可以尝试通过 `wx.getDeviceInfo().model` 获取。
* **微信客户端平台**：通过 `wx.getDeviceInfo().system` 获取。
* **微信版本号**: 通过 `wx.getAppBaseInfo().version` 获取。
* **微信小程序客户端基础库版本**：通过 `wx.getAppBaseInfo().SDKVersion` 获取。
* **（若使用 Mega 插件）使用的 Mega 插件版本**：可以通过工程 `app.json` 文件中的 `plugins` 字段中的 `version` 获取。
### [Mega] AR Session dump 文件（至关重要）
能够复现问题的 AR Session dump 文件是分析微信小程序上定位、跟踪问题最重要的数据。
参考 [如何使用你的小程序录制 AR Session dump 文件](../../../mega/data-collection/wechat/wechat-dump.html)实现 dump 文件的记录与转发。
此外若定位问题可以稳定复现，您也可以通过 Mega toolbox 来录制这段数据并转发，参考[使用微信小程序 Mega Toolbox 记录与转发 session dump 数据](../../../mega/data-collection/wechat/toolbox-dump.html)。
### 屏幕录制（建议）
若使用 Mega 插件，请务必在录制屏幕的同时进行 AR Session dump。这能让我们将视频中的视觉现象与底层算法数据对齐。
### 运行日志
若在 vConsole 中出现了报错，您需要提交详细的错误信息，详细方法参考 [微信小程序上的日志分析](../../diagnostics/log-wechat.html)
##### 重要事项
如果使用 Mega 时遇到定位或跟踪相关的问题而不是程序异常，请务必提供当时的 **session dump 文件和录屏文件**。纯日志文件仅能提供侧面参考，dump 数据与录屏才是排查问题的**核心依据**。