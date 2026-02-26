---
source: https://www.easyar.cn/doc/zh-cn/develop/mega/input-recording.html
original_file: doc--zh-cn--develop--mega--input-recording.md
normalized_at: 2026-02-27
---
# 采集模拟运行数据
在 Mega 应用的开发和调试过程中，直接在真实环境中反复测试不仅耗时，而且可能受限于场地、设备和网络条件。为了解决这个问题，EasyAR 提供了一套强大的模拟运行机制，其核心就是 EIF 数据文件。
本篇将指导您如何采集和回放 EIF 数据，以实现高效的功能验证、问题排查和效果预览。
## 核心概念：什么是 EIF 数据？
在开始之前，强烈建议您先阅读 [EIF 简介](../simulation/simulation.html)，以了解：
* **EIF 文件内容**：它是一个数据容器，不仅包含摄像头视频流，还同步记录了传感器数据、设备姿态、相机参数等。
* **录制与回放机制**：通过在真实环境中录制一次 EIF 文件，您就可以在开发环境中无限次地回放，完美复现当时的场景。
理解 EIF 是 “一次录制，随处回放” 的 “数字副本”，将极大提升您的开发效率。
## 采集 EIF 数据：方法与流程
采集高质量的 EIF 数据是成功模拟的第一步。请遵循 [采集 EIF 数据](../../mega/simulation-verification/recording.html) 中的基本原则，以确保数据的有效性。
根据您的目标设备，采集 EIF 的方法如下：
* 智能手机
工具：通过 Mega Toolbox App 完成。这是一个专为手机设计的辅助应用，简化了录制流程。
参考：详细的操作步骤请查阅 [手机录制 EIF 文件](../../mega/data-collection/simulation/toolbox.html)。
* XR 头显设备
工具：通过 Sample 程序完成。在头显的示例工程中集成了 EIF 录制功能。
参考：详细的操作步骤请查阅 [眼镜录制 EIF 文件](../../mega/data-collection/simulation/headsets.html)。
## 回放 EIF 数据：验证与调试
采集到 EIF 文件后，您就可以在开发环境中进行回放，无需连接真实设备，也无需亲临现场。
根据您的开发环境，回放 EIF 的方式如下：
* Unity 开发
工具：使用 `session` 验证工具。这是一个集成在 Mega `ARSession` 中的工具，可以直接加载 EIF 文件并模拟 Mega 定位会话。
参考：具体使用方法请查阅 [使用 session 验证工具模拟运行](../unity/mega/verify-session-tool.html)。
* 微信小程序开发
工具：借助 Unity 编辑器。由于微信小程序开发环境的限制，推荐您在 Unity 编辑器中回放 EIF 数据来验证内容和逻辑。
参考：具体使用方法请查阅 [在 Unity 编辑器中模拟运行](../wechat/mega/content-simulation.html)。
总之，掌握 EIF 数据的采集与回放，是高效开发 EasyAR Mega 应用的必备技能。它将开发流程从“现场调试”转变为“离线分析”，显著缩短开发周期，并使团队协作和问题复现变得更加简单。
