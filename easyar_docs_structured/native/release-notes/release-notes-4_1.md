---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_1.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-4_1.md
normalized_at: 2026-02-27
---
# EasyAR Sense 4.1 发行说明
## 4.1.0
2020-07-16
EasyAR Sense 4.1.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + MotionTrackerCameraDevice 支持点击碰撞和获取局部点云功能
>
> + CloudRecognizer 支持单次扫描
>
> + API 文档支持交叉引用链接
>
> - 拆分 Unity Plugin 文档
>
> - 去除 ImageTarget.setupAll 和 ObjectTarget.setupAll，并增加了 Android 和 iOS 上使用 JSON 加载 ImageTarget 的示例代码
>
> * 修正 Android 上 CameraDevice(Camera1).setSize 中与 buffer 数量相关的多线程 race condition(造成摄像机画面显示不正常)
>
> * 修正 Android 上 CameraDevice(Camera2).supportedSize 返回数值错误的问题
>
> * 修正 Android 上 CameraDevice.supportedFrameRateRangeLower 和 CameraDevice.supportedFrameRateRangeUpper 崩溃的问题
>
> * 修正 SparseSpatialMap 上传和下载超过 1MB 地图时数据损坏的问题
>
> * CameraDevice.setSize 不再修改 CameraParameters，只在 InputFrame 生成时进行根据图像大小重新计算 CameraParameters
>
> * 修正 Swift binding 在 XCode 11.4 和之后版本上运行崩溃的问题
>
> * 修复了一些稳定性问题
>
