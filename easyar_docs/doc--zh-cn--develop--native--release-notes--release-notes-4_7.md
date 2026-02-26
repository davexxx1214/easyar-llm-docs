---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_7.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-4_7.md
normalized_at: 2026-02-27
---
# EasyAR Sense 4.7 发行说明
## 4.7.0
2025-10-20
EasyAR Sense 4.7.0 增加了一些功能，修复了一些问题。
版本
>
> + 增加 CommunityR 版本，支持视频播放、录屏功能，取消 NR 版本，其他版本不再支持视频播放、录屏功能
>
> + 增加 visionOS 支持
>
> + 增加 aar 的 C++ prefab 支持
>
> * 升级编译 SDK 的工具版本：Android build tools 36，NDK r28，兼容 Android 16KiB 内存页大小
>
> * 升级编译 SDK 的工具版本：XCode 16.1
>
> - 结束 iOS 11.x-14.x 支持，最低支持版本为 15.0
>
> - 结束 macOS 10.x 支持，最低支持版本为 11.0
>
MEGA
>
> + 增加 MegaLandmarkFilter 用于支持 EasyAR Mega Landmark 的 VPS 云定位
>
> + MegaTracker 支持新协议版本
>
> + MegaTracker 运行时支持切换定位库
>
> + 服务器唤醒中定义单独枚举项
>
> + MegaTracker 增加同步获得输出 pose 的功能
>
> + MegaTracker 增加 setResultAsyncMode 接口，适应 RTCT 的修改
>
> + 支持使用 API Token 访问 Mega 服务
>
算法
>
> + 支持使用 API Token 访问 CRS 服务
>
> + InputFrame 增加了一些不兼容的检查
>
> + InputFrame 增加 CameraTransformType 字段
>
> + CameraParameters 增加鱼眼等相机模型
>
> + ImageTracker ObjectTracker SparseSpatialMap 增加同步访问结果模式
>
> * 将 RealTimeCoordinateTransform 集成在各个 Tracker 中，改进其稳定性
>
> * 修正 MotionTrackerCameraDevice 在某些情况下会崩溃的问题
>
设备
>
> + 增加 ThreeDofCameraDevice 用于支持 3DoF 的相机
>
> + 增加 InertialCameraDevice 用于支持惯性导航
>
> + 增加 VisionOSARKitCameraDevice 用于支持 visionOS 上的 ARKit 相机
>
> + 增加 Gyroscope Magnetometer AttitudeSensor 用于获取传感器数据
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获取帧率的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice 获取摄像机图像大小的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获得摄像机类型和旋转方向 的功能
>
> + 增加 CameraDevice 获得旋转方向的功能
>
> + 增加 MotionTrackerCameraDevice 获得摄像机类型、旋转方向、大小、帧率的功能
>
> + 增加对一些 AR 眼镜的支持(请参考 EasyAR Sense Unity Plugin 文档)
>
> + ARKitCameraDevice 增加帧率设置
>
> + 各种 CameraDevice 删除获得 InputFrameSourceType 功能
>
> + 升级 ARCore 机型列表
>
> + 升级 MotionTrackerCameraDevice 机型列表
>
> + Android 上 camera2 获取系统内参
>
> + iOS 支持 CameraDevice 获取内参(可能部分老手机不支持)
>
杂项
>
> + 增加 VideoInputFrameRecorder 和 VideoInputFramePlayer 用于 EIF MKV 格式调试数据录制和播放(Windows 上只支持播放，Android 上只支持录制)
>
> + 增加 EventDumpRecorder 用于 EED 格式调试数据录制，EED(EasyARSense Event Dump)文件可用于记录日志、输出帧状态、定位请求、IMU、GPS 等数据
>
> + Log 增加 logMessage
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NORTTI
> 选项用于禁用 RTTI
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常
>
> + 在 C++导出接口实现中增加
> EASYAR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常 throw
>
> * 修复了一些稳定性问题
>
