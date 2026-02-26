---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_4.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-4_4.md
normalized_at: 2026-02-27
---
# EasyAR Sense 4.4 发行说明
## 4.4.0
2021-10-28
EasyAR Sense 4.4.0 增加了对 EasyAR Cloud SpatialMap 的支持，另外还增加了一些小功能，修复了一些问题。
[EasyAR Cloud SpatialMap](https://www.easyar.cn/cloudspatialmap.html) 提供城市级 AR 云方案，通过灵活的采集方案、稳定的建图定位能力及完善的工具链，为文旅、商圈、教育、工业等众多行业进行 AR 数字化赋能。
详细更新内容如下：
>
> ++ 增加 CloudLocalizer，用于支持 EasyAR Cloud SpatialMap
>
> + 增加 RealTimeCoordinateTransform，用于 EasyAR 运动融合
>
> + iOS 和 MacOS 中的 framework 改为以 xcframework 的形式组织
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ARKit/ARCore 对焦控制接口 ARCoreCameraDevice.setFocusMode、ARKitCameraDevice.setFocusMode
>
> + 增加加速度计接口 Accelerometer
>
> - 去除 iOS 上的 static framework，请改为使用 dynamic framework
>
> - 去除 MacOS 上的 bundle，请改为使用 framework 或者 dylib
>
> - C++03 接口已过时，会在将来删除，请改为使用 C++17 或者 C 接口，示例已删除
>
> * 将 Android 示例中的 jcenter 改为 mavenCentral，以应对 jcenter 关闭
>
> * 修复 MotionTracking 在反复进出时可能崩溃的问题
>
> * 修复 MotionTracking 在部分设备上卡死的问题
>
> * 优化 iOS 示例发布包大小
>
> * 修复 ImageTracking 有时候识别到后马上丢失的问题
>
> * 修复 ImageTracking 在 Android 上部分识别图加载失败无法用于跟踪的问题
>
> * 修复 ImageTarget.save 在 MacOS 上 Unicode 字符路径无法使用问题
>
> * 修复 CameraDevice 设置的回调在调用 open 之后会失效的问题
>
> * 修复 CameraDevice 在 Android 上调用 start 之后设置的回调无法被触发的问题
>
> * 修复了一些稳定性问题
>
