---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/verify-session-tool.html
---

使用 session 验证工具模拟运行使用 Mega 能力的 AR 工程 | EasyAR 文档
**
##### Table of Contents
**
# 使用 session 验证工具模拟运行使用 Mega 能力的 AR 工程
本文旨在指导开发者如何在 Unity 编辑器上利用 session 验证工具加载录制的 EIF 数据，模拟运行使用 Mega 能力的 AR 工程。
## 开始之前
* 完成[快速入门](quickstart.html)，了解如何运行包含 Mega 功能的 Unity 应用。
* 了解什么是 [EIF](../../simulation/simulation.html)。
* 学习如何[采集模拟运行数据](../../mega/input-recording.html)。
## 为什么用 session 验证工具模拟运行是个好办法
**远程开发**：无需顶着烈日或严寒驻场，利用 EIF 数据，您在办公室就能开发基于大规模地理空间的 AR 应用。
**跨平台调试**：无需频繁连接各种移动设备，在 Windows PC 上即可模拟手机、头显等不同终端的定位和跟踪效果。
**问题反馈的“金标准”**：一个**能够复现异常的 EIF 文件**，是 EasyAR 团队为您解决定位与跟踪问题的**关键依据**。
##### 注意
尽管 EIF 数据记录得非常精确，模拟效果和实际使用效果可能依然存在差异。
并且模拟数据对现场的覆盖有限，在最终发布前务必进行实地测试。
## 操作步骤
通过以下步骤使用 session 验证工具模拟运行。
### 准备好现场录制的 EIF 文件
根据所选录制格式不同，录制好的EIF数据应为 `.mkveif` 文件（或 `.eif` 文件和 `.eif.json` 文件，这两个文件缺一不可）。
**`.eif` 和 `.eif.json`：**
![旧EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool05.png)
**`.mkveif`：**
![新EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool06.png)
### 对照 Block 稠密模型或全景摆放一些 3D 内容
![摆放3D内容](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera03.png)
### 开启 Session 验证工具
点击场景中的 **AR Session (EasyAR)** &gt; 确认其 **Inspector** 面板上的 **Frame Player** 已经**开启**。
![确认FramePlayer开启](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool03.png)
### 运行
点击工具栏按钮或点击 **Session Validation Tool** 上的运行按钮在 Unity 编辑器上开始运行这个工程。
![运行按钮](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool07.png)
运行后会弹出一个提示框，**这是正常的**，它只是提示现在正在使用 `Frame Player`。
![提示弹窗](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool08.png)
点击工具上的按钮打开 EIF 文件。
![打开EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool09.png)
正常打开后它会自动播放，可以使用工具栏进行暂停/继续等控制，有些新格式的 EIF 也支持进度条跳转。
![控制进度](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool10.png)
运行效果：
若在工具 `EasyAR.Mega.BlockViewer (Dev)` 中加载了 Block 稠密模型，Block 稠密模型也会保持显示。这在进行位置比对或未放置模型的地方查看定位效果的情况下还是有用的。
一般来说可以将工具 `EasyAR.Mega.BlockViewer (Dev)` 关闭（`active` 设成 `false` 或删除场景节点），然后运行看到的就是在现实场景中叠加了虚拟物体的效果。
##### 重要事项
在使用时，你一定会注意到运行时显示在屏幕上或目视前方的诊断信息文字，仔细阅读 [UI 消息输出](../diagnostics/ui-messages.html)，仔细斟酌在开发阶段、测试阶段、应用上线之后应该采取何种配置，以及保留何种控制开关。与 EasyAR 的沟通通常需要提供这些信息，建议多利用而不是立马关闭。
默认设置下，启动后，在第一次定位到 `Block` 之前，整个 `MegaBlocks` 及其子节点的 `active` 都是 `false`，内容不会显示。
![MegaBlock显示状态](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool13.png)
在定位到之后，上述节点的 `active` 会变成 `true`，内容会显示出来并不断更新位置。
![MegaBlock定位到后显示](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool14.png)
如果要改变相关行为，或是更加自由的控制 active 行为，可以参考 [BlockRootController 组件参考](comp-BlockRootController.html) 和 [BlockController 组件参考](comp-BlockController.html)。
## 相关主题
* [session 验证工具](../simulation/tool.html)