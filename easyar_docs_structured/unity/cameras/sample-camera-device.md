---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/sample-camera-device.html
original_file: doc--zh-cn--develop--unity--cameras--sample-camera-device.md
normalized_at: 2026-02-27
---
# Workflow\_FrameSource\_CameraDevice 示例详解
`Workflow\_FrameSource\_CameraDevice` 是一个专注于 **帧输入源（Frame Source）底层控制** 的示例场景，展示了如何使用 `CameraDeviceFrameSource` 获取摄像头的原始图像流，并进行一些基础控制。
## 使用方法
### 1. 打开场景
在 Unity 编辑器中，打开 `Workflow\_FrameSource\_CameraDevice` 场景，位于 `Assets/` 目录中。
### 2. 构建运行
* 在编辑器中点击 **Play** 可查看 PC 上的效果画面（部分功能受限）。
* **必须构建到真机** 才能完整体验摄像头的基础控制能力。
应用启动后，将自动打开后置摄像头。
## 预期效果
当摄像头对准周围环境时：
1. 屏幕中会显示实时摄像头画面。
2. 此时会渲染一个 3D 动态熊猫模型。
3. UI 显示当前摄像头状态（如分辨率、FPS）。
4. 点击 `Loop Size` 按钮可以切换当前摄像头支持的输出帧分辨率。
5. 点击 `Flash Torch` 按钮可以 **关闭/打开** 闪光灯。
6. 点击 `HorizontalFlip` 可以切换当前画面的 **镜像显示**。
7. 点击 `CaptureIamge` 可以切换是否让模型捕获当前环境画面作为自身的贴图。
8. 点击 `CameraImage` 可以切换是否显示当前摄像头画面。
9. 点击 `Camera` 可以 **关闭/打开** 当前摄像头，关闭后画面将保持关闭前的状态不变。
10. 通过 `NextCamera` 按钮动态切换 **前置/后置摄像头**。
> **提示**
更多 FrameSource 详情，请参阅：
* [内置Frame Source参考](frame-source-builtin.html)
* [自定义相机和外部帧输入](external-frame-source.html)
通过 `Workflow\_FrameSource\_CameraDevice`，您可深入掌握 EasyAR 对底层摄像头资源的控制能力，为构建高性能、高定制化的 AR 应用奠定坚实基础。
