---
source: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/diagnostics.html
---

问题诊断和报告 | EasyAR 文档
**
##### Table of Contents
**
# 问题诊断和报告
本章主要描述构建AR应用时可能遇到的问题、主要的分析方法，以及报告问题所需要收集的信息和联系途径。
## AR 场景中问题分析的挑战
在 AR 场景中的问题分析，存在一些独特的挑战。
### 输入的不确定性
在传统应用中，输入通常是确定的点击或键盘事件。而在 AR 中，输入源自变动的物理环境，这带来了极大的分析难度。AR 应用需要结合物理环境来使用，但开发和测试时，在物理环境中无法每次获得相同的输入，即使按照同一条路线行进，取得的相机图像、加速度计、陀螺仪等传感器的数据都可能产生一些变化，而这对跟踪结果的影响可能是巨大的。
EasyAR 中提供了 EIF 文件的录制和回放功能，可以在一定程度上缓解输入的不确定性，但由于算法的不确定性，最终的跟踪结果本质上还是不确定的。同时，EIF 录制数据覆盖不全、光照变化、行人或车辆造成的动态遮挡等，也会影响实际使用时的跟踪质量。
### 算法的不确定性
AR 的核心算法是一些视觉算法，例如 SLAM（即时定位与地图构建）。这些算法本质上是概率性的而非确定性的。
当输入的相机图像缺乏显著的特征时，算法可能使用历史位置姿态和加速度计、陀螺仪等传感器数据进行预测，预测的位置和姿态的结果会随着时间推移而累积，产生飘移。而每次的预测结果和数据的传入时机、设备的温度、CPU 的频率、网络传输速度等外界因素有关，存在动态变化，累积下来即使是同样的输入，多次运行的结果也可能偏差很大。
## 不同问题的分析方法
对于不同的问题，可能需要不同的分析方法。
### 日志
对于一些程序运行不正常的情况，例如黑屏、无法正常定位、无法正常跟踪的情况，最基本的方法是查看日志，检查其中是否有错误信息。EasyAR 中产生的日志，均会使用特定的标签，便于识别。
### 崩溃
有时候程序会发生崩溃，崩溃的位置可能在库的代码中，也可能在程序自己的代码中。崩溃发生的原因有可能是由于程序本身的问题，也可能是库中存在问题。
### 抖动、跳动等视觉异常
由于传感器数据精度或者算法适配原因，可能会发生定位抖动或跳动。此时应尝试使用不同设备重现此问题，并截图、录屏和录制 EIF 文件。
## 平台专用指南
问题诊断和报告与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [日志分析 Android](log-android.html)
* [日志分析 iOS/macOS/visionOS](log-ios.html)
* [日志分析 Windows](log-windows.html)
* [崩溃分析 Android](crash-android.html)
* [崩溃分析 iOS/macOS/visionOS](crash-ios.html)
* [崩溃分析 Windows](crash-windows.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)
* [Unity 简介](../unity/diagnostics/diagnostics.html)
* [Unity UI消息](../unity/diagnostics/ui-messages.html)
* [Unity 开发者模式](../unity/diagnostics/developer-mode.html)
* [Unity 录制EED dump文件](../unity/diagnostics/event-dump.html)
* [Unity 问题报告](../unity/diagnostics/report.html)
* [Unity Diagnostics Controller 组件参考](../unity/diagnostics/comp-DiagnosticsController.html)
* [日志分析](log-wechat.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)
* [问题报告](../wechat/diagnostics/report.html)
* [日志分析 Android](log-android.html)
* [日志分析 iOS/macOS/visionOS](log-ios.html)
* [日志分析 Windows](log-windows.html)
* [崩溃分析 Android](crash-android.html)
* [崩溃分析 iOS/macOS/visionOS](crash-ios.html)
* [崩溃分析 Windows](crash-windows.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)