---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/verify-pc-camera.html
original_file: doc--zh-cn--develop--unity--mega--verify-pc-camera.md
normalized_at: 2026-02-27
---
# 使用 PC 摄像头快速跑通 Mega （一种快捷但不推荐的远程调试方式）
本文档旨在指导开发者如何在没有 EIF 录制文件的情况下，利用 PC 摄像头配合现场图片，验证 Mega 云定位服务是否能跑通。
## 开始之前
* 完成[快速入门](quickstart.html)，了解如何运行包含 Mega 功能的 Unity 应用。
* PC 连接一个摄像头设备，并确保其功能正常。
* **功能预期**：
该方式**并非**我们推荐的远程调试方式，在有条件录制的情况[使用 EIF 文件进行调试](verify-session-tool.html)是我们推荐的最佳实践。
该方式仅用于**在没有 EIF 文件**情况下调试**与跟踪效果无关**的流程开发，比如用于验证 Mega 服务是否通畅。
PC 上使用相机看到的效果与实机的跟踪效果**完全无关**。
## 操作步骤
完成以下步骤即可快速跑通 Mega 服务验证。
### 获取现场照片
获取一张现场较为清晰的照片，可以现场拍摄也可以在编辑器中使用全景预览功能截取一张图片。
**如何使用全景预览功能截取图片**
>
> 点击场景
> Hierarchy
> 面板中的
> Mega Block Viewer(Dev)
> > 在
> Inspector
> 面板中点击
> 全景标记
> 右侧的
> 加载
> 。
>
![全景加载](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera02.png)
>
> 此时场景中会出现许多代表
> 全景标记
> 的黄色小球：
>
![全景标记](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera06.png)
>
> 点击
> 需要预览的位置的全景标记
> > 点击场景
> Hierarchy
> 面板中的
> Mega Block Viewer(Dev)
> > 在
> Inspector
> 面板中点击
> 全景标记
> 左侧的
> 隐藏
> 。
>
![全景标记隐藏](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera07.png)
>
> 即可在
> Mega Panorama
> 窗口中得到一张现场图片，将其截图保存：
>
![现场图片](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera05.png)
>
### 对照 Block 稠密模型或全景摆放一些 3D 内容
![摆放3D内容](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera03.png)
### 确认 Session 验证工具没有开启
点击场景中的 **AR Session (EasyAR)** > 确认其 **Inspector** 面板上的 **Frame Player** 被关闭。
![确认FramePlayer关闭](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera12.png)
点击场景中的 **EasyAR.Mega.BlockViewer(Dev)** > 确认其 **Inspector** 面板上的验证工具没有被 **Enable** (若不需要使用稠密模型，也可以直接删除或隐藏 **EasyAR.Mega.BlockViewer(Dev)**)。
![确认验证工具关闭](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera10.png)
### 点击运行，使用现场图片跑通 Mega
* **操作示范：**
> **重要事项**
Mega 定位服务对于用于定位的输入比较“宽容”，但这种调试方式的结果仅用于区分“通”与“不通”（即 0 或 1 的区别）。它能证明 Mega 定位服务已跑通，但完全不能代表真机上的实际跟踪体验。若要观察定位速度和跟踪稳定性，务必[使用 EIF 文件调试](verify-session-tool.html)或真机实测。
* **可以使用相机对着图片或视频运行**，如果定位成功，将会看到 3D 物体贴屏显示并跳跃更新。由于在场景中加载了 Block 模型，Block 模型也会显示出来。
* 如果将工具 `EasyAR.Mega.BlockViewer (Dev)` 关闭（`active` 设成 `false` 或删除节点），看到的就是在现实场景中叠加了虚拟物体的效果。
* **屏幕上的警告信息是无法关闭的**，因为这种使用方式并不能反映真实效果，我们限制这种方式只能在开发过程中使用，且开发人员应该清楚这样使用的影响。
![屏幕警告信息](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera11.png)
* 可以**通过诊断信息时间戳更新判断系统是否正常运行**：如果看到屏幕上显示的诊断信息中时间戳在不断更新，就说明系统已经正常在运行了。
![通过时间戳判断](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera12.gif)
> **重要事项**
在使用时，你一定会注意到运行时显示在屏幕上或目视前方的诊断信息文字，仔细阅读 [UI 消息输出](../diagnostics/ui-messages.html)，仔细斟酌在开发阶段、测试阶段、应用上线之后应该采取何种配置，以及保留何种控制开关。与 EasyAR 的沟通通常需要提供这些信息，建议多利用而不是立马关闭。
## 后续步骤
* 尽可能[使用 session 验证工具模拟运行](verify-session-tool.html)。
