---
source: https://www.easyar.cn/doc/zh-cn/develop/simulation/simulation.html
original_file: doc--zh-cn--develop--simulation--simulation.md
normalized_at: 2026-02-27
---
# 录制 EIF 文件并用于模拟运行
**EIF 文件（EasyAR Input Frame file）** 是 EasyAR Sense 用来存储一系列输入帧数据的文件格式。本文主要描述如何录制 EIF 文件并用于模拟运行。
## EIF 文件和内容
EIF 文件根据不同的录制方式，存在两个实现：
* 原始 EIF 格式（通常扩展名为.eif）
原始的 EIF 文件以 EasyAR 内部定义的数据结构逐帧存储输入帧数据，包括图像和附加信息（如 camera 参数和跟踪状态等）。这种格式不做视频压缩，而是逐帧编码（例如 JPEG 图像数据），适合精确回放。
* EIF MKV 格式（通常扩展名为.mkveif）
基于 MKV 封装的视频格式，在此基础上将输入帧的信息编码进 MKV 容器。视频编码使用 H.264 来压缩图像数据，同时保留输入帧其他元数据（如 IMU 传感器数据、定位数据等）作为流或附加轨道。这样可以显著减少文件体积，并便于标准视频流处理。
> **注意**
EIF MKV 格式目前只支持 Android/iOS/macOS/visionOS 上的录制和 Windows/macOS 上的回放，传统 EIF 格式无此限制。
## EIF 录制和回放
EasyAR 提供了录制和回放的一整套机制，主要通过以下组件控制：
* InputFrameRecorder / InputFramePlayer
* 用途
对应于原始 EIF 格式的录制和回放组件。
* 特点
录制过程中，所有传入的输入帧都会被序列化保存，包括图像、参数、跟踪状态等。
* VideoInputFrameRecorder / VideoInputFramePlayer
* 用途
对应于 EIF MKV 格式的录制和回放组件。
* 特点
录制时支持更多传感器数据流（如陀螺仪、加速度计、定位数据等），并将其一起封装入 EIF MKV 文件。播放端可选择输出这些数据，方便在 PC 端完整模拟录制时的各种输入。
## 使用 EIF 模拟运行的原理和可达到的效果
将录制好的 EIF 文件作为输入数据源，相当于把物理摄像头及其相关传感器在运行时的完整数据流“重播”给 AR 引擎。通过模拟输入帧序列：
* AR 引擎认为它仍然在获取物理摄像头的数据
回放输出的每一帧都具有原始时间戳、相机参数和跟踪状态，驱动算法像运行实时数据一样处理这些帧。
* 可以在非设备环境（如 PC 或 Unity 编辑器）复现真实运行时行为
这样你无需实机即可调试视觉跟踪、空间地图等功能，可以在 Windows/Mac 上模拟运行 Mega 等功能。
使用 EIF 模拟运行可达到的效果：
* 重现真实的数据流转过程
即便在没有摄像头的情况下，也可以像真实运行一样驱动 AR 功能，如平面图像跟踪、空间定位、稠密地图生成等。
* 便于开发调试与诊断
录制的 EIF 文件可用于分析跟踪失败原因、验证 AR 算法在特定输入上的行为或性能波动。
* 跨平台回放
在不同平台之间传输 EIF 文件，在 PC 上复现手机上录制的 AR Session 行为，无需设备即可调试。
## 后续步骤
* [录制EIF数据：复现AR问题的高保真依据](../diagnostics/simulation.html)
## 平台专用指南
录制 EIF 文件并用于模拟运行与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [Unity AR 模拟运行](../unity/simulation/simulation.html)
* [录制 EIF 文件](../unity/simulation/recording.html)
* [使用 EIF 文件模拟运行](../unity/simulation/playback.html)
* [使用 Session 验证工具播放 EIF 文件](../unity/simulation/tool.html)
