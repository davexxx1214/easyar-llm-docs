---
source: https://www.easyar.cn/doc/zh-cn/develop/mega/report.html
original_file: doc--zh-cn--develop--mega--report.md
normalized_at: 2026-02-27
---
# 问题报告与反馈
我们非常重视您的反馈，这是帮助我们改进 EasyAR Mega 产品和服务的关键。为了让我们能够快速、准确地定位并解决您遇到的问题，请在提交报告前，花几分钟时间阅读本篇指南。
## 我们的联系方式
您可以通过以下渠道向我们提交问题报告：
* **官方开发者社区/论坛** - 推荐用于一般性问题和社区交流。
* 中文用户点击 [这里](https://answers.easyar.cn)
* 其他用户点击 [这里](https://answers.easyar.com)
* **企业微信群** - 适用于需要保密或更正式支持的企业级用户。
* 扫描下方二维码进群
![](https://doc-asset.easyar.com/develop/mega/media/wechat.png)
* **更多联系方式** - 作为备选方案。
* 获取联系方式点击 [这里](https://www.easyar.cn/view/contactus.html)
## 提交一份高质量报告的核心要素
一份包含以下信息的报告，将极大地帮助我们复现和解决问题。**信息越完整，问题解决越快。**
### **通用报告清单（所有问题都需要）**
1. **问题清晰描述**：
* 您期望实现的效果是什么？
* 实际发生了什么？（例如：应用闪退、定位失败、内容飘移）
* 问题发生的频率（必现/偶现）？在什么条件下发生？
* **设备与环境信息**：
* **设备型号**：例如，`iPhone 14 Pro`, `Samsung Galaxy S23 Ultra`, `Apple Vision Pro`。
* **操作系统版本**：例如，`iOS 17.2`, `Android 14`, `visionOS 26`。
* **EasyAR SDK 版本**：例如，`EasyAR Sense Unity Plugin v4.6.0`。
* **测试环境**：室内/室外，光照条件，是否为动态环境。
* **EIF 数据（最重要的证据）**：
* **请务必提供能够复现问题的 EIF 录制文件**。
* EIF 数据包含了问题发生时的所有传感器和图像信息，是我们诊断问题的最有力工具。请参考 [采集模拟运行数据](input-recording.html) 了解如何录制。
* **日志文件 (Log)**：
* 请提供问题发生时的完整应用日志。
* **Android**: `Logcat` 输出。
* **iOS**: `Console.app` 日志或 Xcode 控制台输出。
* **Unity**: Unity Editor 的 `Console` 日志。
* **微信小程序**：`session.dumpLog()` 得到的日志文件。
* **录屏或截图**：
* 问题发生时的屏幕录像或高清截图，这能直观地展示您所描述的现象。
* 不同设备的操作指南可参考：[手机录屏](../diagnostics/recordings.html)、[头显录屏](../diagnostics/recordings-headsets.html)。
* **Mega 定位库信息**
* 在 Unity 中导出应用所使用的 Mega 定位库的服务信息。导出方法：
![Mega Service Export](https://doc-asset.easyar.com/develop/mega/media/mega-service-export.png)
## 特定问题类型的补充清单
为了让问题定位更精准，请根据您的问题类型，额外提供以下信息：
**A. 定位失败或不稳定**
* 已尝试使用 **Mega Toolbox** 或 PC 端工具在相同位置进行验证，并说明结果。
* 已确认定位库中加载的地图与当前物理空间一致。
* 说明问题发生的大概位置（例如，商场中庭、景区门口）。
**B. 内容不显示**
* 已提供使用外部工具验证定位的结果。
* 已明确内容摆放或代码逻辑没有问题。
* 如果是渲染问题，请提供所用模型、Shader 或特效的截图或描述。
**C. 内容跳动或飘移**
* 已说明设备的移动方式（平稳移动/快速移动）。
* 已描述环境的纹理和光照情况，以及是否存在极度相似的混淆区域。
* 已说明应用内部对姿态的处理逻辑以及内容摆放正确。
**D. 微信小程序问题**
* 已提供用户在微信内开启 Mega 服务权限的截图。
* 已说明用户手机型号是否在微信官方支持列表中。
* 已提供小程序的 AppID 和具体的业务场景描述。
**E. 性能问题 (卡顿、功耗高)**
* 已说明问题发生的设备型号。
* 已提供应用运行时的 CPU/GPU 占用率或设备温度信息（如果可能）。
* 已说明 3D 内容的复杂程度（模型面数、纹理大小）。
* 已说明是否使用了多图配置。
## 使用 EasyAR Sense Unity Plugin 导出 Unity 开发信息
特别地，针对 Unity 平台的 Mega 应用开发，我们准备了更便捷的反馈信息生成工具。详细的操作步骤如下：
1. 在菜单栏打开 `EasyAR > Sense > 提问`
![提问](https://doc-asset.easyar.com/develop/mega/media/unity-question.png)
2. 在 `提问` 中提供以下信息:
* 勾选运行环境（单选），如 Android。
* 复制设备信息。在 `ARSession` 中将 `DiagnosticsController.DumpSession` 设置为 `Log`，复制一帧的输出并填写结果到设备信息框中。
![Dump session](https://doc-asset.easyar.com/develop/mega/media/unity-device-info.png)
* 勾选您的应用在使用的所有 EasyAR 功能，支持多选。
* 确定已经完成页面中的四项检查并打勾，建议在提问时描述如何在 Sample 中复现问题。
* 点击右上角的复制功能，即完成了 Unity 开发信息的收集。
![导出 Unity 开发信息](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
## 报告提交流程建议
1. **准备材料**：根据上述清单，收集 EIF、日志、截图/录屏、服务信息、开发信息等。
2. **撰写报告**：清晰描述问题，并附上所有材料。
3. **提交**：通过您选择的渠道提交报告。
4. **跟进**：我们收到报告后，会通过商务或邮件与您联系。请保持关注。
感谢您的时间和对 EasyAR Mega 产品的支持！您的每一次反馈，都在帮助我们构建更好的空间计算未来。
