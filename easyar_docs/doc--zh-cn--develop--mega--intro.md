---
source: https://www.easyar.cn/doc/zh-cn/develop/mega/intro.html
---

EasyAR Mega 简介 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR Mega 简介
EasyAR Mega 是一项端云协同的空间计算技术，旨在为整个物理世界（例如一个城市、一个园区或一个大型商场）创建持久化的、高精度的数字孪生空间。通过 EasyAR Mega，您的应用可以实现大规模、高精度的室内外定位与虚实遮挡，为用户带来前所未有的空间交互体验。
本章将从开发者的角度，简要介绍 EasyAR Mega 的核心工作原理、预期效果及平台适配指引。
##### 重要事项
非开发者用户（如产品经理、运营、测试人员等）直接前往 [Mega 使用指南](../../mega/overview.html) 了解 Mega 服务。
## 开始之前：确保定位服务就绪
在您的应用中集成 EasyAR Mega 功能前，**必须确保一个核心前提：Mega 云定位服务已准备完成**。
* **已完成现场数据采集**
* 使用指定设备采集目标区域的数据
* 使用 Mega Toolbox 采集 EIF 数据用于效果验证
* **已完成 Mega Block 建图**
* **定位服务已启用并绑定应用**
* 在开发中心将 Block 添加至 Mega 定位库中
* 获取有效的 App ID、API Key 并正确配置到您的项目中
##### 重要事项
若未完成上述步骤，应用将无法获取定位结果，表现为“始终无法触发 AR 内容”。开发前务必 [验证服务可用性](../../mega/localization/verification.html)。
## Mega 定位基本原理
与依赖卫星信号的传统 GNSS 定位不同，EasyAR Mega 基于先进的视觉定位技术。通过将用户设备实时拍摄的图像数据与预先构建的高精度三维数据进行匹配，确定出用户在物理世界中的 6DoF 位姿。根据该位姿，应用端可以在正确的物理位置上渲染叠加出虚拟内容。
**工作流程如下：**
1. **地图构建**：
* 使用专业设备（如全景相机）在目标区域进行数据采集。
![Data Capture](https://doc-asset.easyar.com/develop/mega/media/data-acquire.jpg)
* 通过 EasyAR 的建图管理后台，将采集到的数据（如 **.360** 文件）上传。
* 云端处理平台将对采集数据中的图像进行计算，使用先进的 AI 算法提取目标区域的视觉特征；并将图像与 IMU 传感器等信息融合，恢复采集时的运动轨迹（即每个时刻的相机位姿）；进而生成整个场景的三维点云、构建带纹理贴图的稠密网格。
* 最终建图系统将输出一个由 EasyAR 自定义的高精度、包含三维几何信息和视觉特征的“Mega Block 地图”。这个地图是 Mega 定位的基石。
![Mapping Process](https://doc-asset.easyar.com/develop/mega/media/mapping-procedure.jpg)
* **实时定位**：
* 用户打开应用，设备摄像头实时捕捉用户视野中的图像，并与相机内参、外参（若有）、辅助信息（若有，如 GNSS ）等一并发送给 Mega 云定位服务。
![User case](https://doc-asset.easyar.com/develop/mega/media/user-experience.jpg)
* Mega 云定位服务会提取上传图像的视觉特征，并与定位库中的 Mega Block 地图进行快速比对和匹配。
* 一旦匹配成功，系统就能以厘米级的精度计算出用户当前在地图中的确切位姿（即位置和朝向）。
* 此时，Mega 云定位会将解算好的位姿下发到应用端，并在应用端与设备本身的 SLAM 系统进行融合跟踪。
* 最终，应用端将获得一个实时定位并持续跟踪的位姿，从而让虚拟内容可以显示在物理世界中预先锚定的位置上，并跟随人的移动而持续更新。
![Localize Process](https://doc-asset.easyar.com/develop/mega/media/localization-procedure.jpg)
## 效果与预期结果
成功集成 EasyAR Mega 后，您的应用可以实现以下令人惊叹的效果：
* **厘米级精度**：相比 GNSS 的数米甚至数十米误差，Mega 定位可以提供亚米级乃至厘米级的定位精度，让虚拟内容稳定地“钉”在真实世界的特定位置上。
* **持久化空间**：虚拟内容可以被放置在物理世界的任何地方，并且所有用户在相同位置看到的内容都是一致的。
* **真实遮挡**：通过 Mega 的空间理解能力，虚拟物体可以被真实的建筑物或障碍物遮挡，极大地增强了沉浸感。
* **无 GNSS 区域工作**：在室内、地下停车场、高楼林立的城市街道或者树木茂盛的山川森林等 GNSS 信号弱或无效的区域，Mega 依然能提供稳定可靠的定位服务。
>
> 视频中是一个典型的使用 EasyAR Mega 的效果示例：
>
>
* > 高精度、持久化的空间定位让虚拟内容完美的贴合在建筑表面，呈现美轮美奂的动态视频和精心设计的巨幅 3D 海报。
>
* > 空间理解带来的真实遮挡，让天空中绽放的烟花、数字特效与周围环境相得益彰，没有违和感。
>
* > 在先进的视觉算法加持下，整个体验无惧周围复杂、密集的人员环境，即便是在夜间也能稳定工作。
>
>
### 可能遇到的不理想情况
* **定位识别速度较慢**
>
> 在人流密集区域如大型活动的现场，由于网络延时、并发请求等情况，Mega 云定位的延时可能会比较大，用户可能会需要等待一定时间才能看到虚拟内容。
>
* **环境变化导致误差**
>
> 如果物理环境发生了剧烈变化（例如，施工围挡、季节性植被变化），可能会导致定位精度下降或丢失。Mega 地图需要定期更新以适应环境变化。
>
* **持续体验出现飘移**
>
> Mega 定位在应用端会与设备本身的 SLAM 系统进行融合跟踪，并持续开启摄像头。长时间运行可能导致设备 CPU 降频，从而引发画面卡顿或掉帧，跟踪尺度飘移等现象。
>
##### 提示
更多详细的效果异常或故障，请参考 **故障排查** 章节：
* [Mega 常见问题](faq.html)
* [内容不显示](content-nodisplay.html)
* [内容跳动和飘移](content-drift.html)
* [问题报告](report.html)
## 扩展建议
如果您在集成 EasyAR Mega 过程中遇到诸如服务故障、场景变化、业务扩容等诸多**非程序开发**的相关问题，请访问我们的 [Mega 使用指南](../../mega/overview.html)。
在该指南中，您可以找到：
* **服务创建**：查看如何创建 Mega 服务以及简单的故障排查。
* **效果优化**：学会如何预览运行效果以及收集异常数据，冷启动监测等。
* **持久运营**：了解如何应对场景变化、业务扩容以及迁移/升级等持久化运营需求。
* **业务对接**：熟悉导航路网等实用业务数据的使用。
* **参考资源**：Mega Studio、Mega Toolbox 等实用工具的操作手册。
通过本篇，希望您对 EasyAR Mega 的工作原理和效果有了清晰的认识。接下来，您可以开始着手准备您的第一个 Mega 项目了！
## 平台专用指南
EasyAR Mega 的集成方式与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [快速入门](../unity/mega/quickstart.html)
* [启用 Mega](../unity/mega/enable-mega.html)
* [AR Session 最佳实践](../unity/mega/session-best-practice.html)
* [添加跟踪目标](../unity/mega/target.html)
* [添加与实景对齐的 3D 内容](../unity/mega/content-realworld-alignment.html)
* [控制跟踪过程](../unity/mega/tracker.html)
* [使用 PC 相机的快速验证](../unity/mega/verify-pc-camera.html)
* [使用 session 验证工具模拟运行](../unity/mega/verify-session-tool.html)
* [环境遮挡](../unity/mega/occlusion.html)
* 组件参考
* [MegaTrackerFrameFilter 组件参考](../unity/mega/comp-MegaTrackerFrameFilter.html)
* [BlockHolder 组件参考](../unity/mega/comp-BlockHolder.html)
* [BlockRootController 组件参考](../unity/mega/comp-BlockRootController.html)
* [BlockController 组件参考](../unity/mega/comp-BlockController.html)
* 快速入门
* [快速运行](../wechat/mega/quickstart.html)
* [在 Unity 里使用 Mega Studio](../wechat/mega/content-unity-setup.html)
* [摆放 3D 内容](../wechat/mega/content-simple.html)
* [完整运行](../wechat/mega/fullstart.html)
* [启用 Mega](../wechat/mega/integration.html)
* 基础组件
* AR Session
* [简介](../wechat/mega/session.html)
* [流程控制](../wechat/mega/session-state.html)
* [屏幕旋转适配](../wechat/mega/session-device-orientation.html)
* [使用非现场模式](../wechat/mega/session-gnss-simulation.html)
* [平面检测异常处理](../wechat/mega/session-plane-detection-error.html)
* MegaTracker
* [简介](../wechat/mega/tracker.html)
* [服务鉴权方式](../wechat/mega/tracker-access.html)
* [传感器外部控制](../wechat/mega/tracker-external-sensor.html)
* [使用 Landmark 服务](../wechat/mega/tracker-landmark.html)
* 内容展示
* 跨越微信XR-Frame编辑器缺失
* [创建并上传标注](../wechat/mega/content-annotation-creation.html)
* [创建与实景对齐的 3D 内容](../wechat/mega/content-simulation.html)
* [模拟运行](../wechat/mega/content-simulation.html)
* [运行时3D内容加载](../wechat/mega/content-load.html)
* [环境遮挡](../wechat/mega/occlusion.html)
* [透明视频](../wechat/mega/transparent-video.html)
* 问题诊断和报告
* [已知问题与限制](../wechat/mega/known-issues.html)
* [录制 ARSession dump 文件](../wechat/mega/session-dump.html)
* [示例说明](../wechat/mega/sample.html)