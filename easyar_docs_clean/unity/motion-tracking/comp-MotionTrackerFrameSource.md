---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-MotionTrackerFrameSource.html
original_file: doc--zh-cn--develop--unity--motion-tracking--comp-MotionTrackerFrameSource.md
normalized_at: 2026-02-27
---
# MotionTrackerFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.MotionTrackerFrameSource.html)
>
探索 MotionTrackerFrameSource 组件窗口中的各项属性以自定义相机和运动跟踪参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-MotionTrackerFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Default：使用默认值，实际选择与使用的 AR 功能有关。
* Input：使用指定值。选择 Input 时可选项：
* Continousauto：连续自动对焦模式，图像清晰度高，跟踪效果一般。实际对焦效果取决于设备能力。
* Medium：中等距离定焦模式，图像清晰度一般，跟踪效果较好，实际对焦效果取决于设备能力。|
|**Desired Resolution**|期望的分辨率。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Resolution\_1280：标准分辨率是 1280 x 960 或者 1280 x 720，实际分辨率取决于设备能力。
* Resolution\_640：标准分辨率是 640 x 480 或者 640 x 360，实际分辨率取决于设备能力。|
|**Desired Frame Rate**|期望的相机图像帧率。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Camera\_FPS\_30：设备图像帧率是 30fps，实际帧率取决于设备能力。
* Camera\_FPS\_60：设备图像帧率是 60fps 或者 30fps，实际帧率取决于设备能力。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Desired Min Quality Level*|期望的最低允许的质量级别。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* NotSupported：设备不支持运动跟踪，可能是适配不达标或者尚未适配。
* Bad：设备不完全达标，尺度不稳定，可用于桌面尺度内的小场景等。
* Limited：设备不完全达标，尺度接近准确，可用于房间尺度内的中等场景，类似 AR 游戏、AR 导航等。
* Good：设备达标，尺度准确，可用于建筑物尺度的大型场景，类似 AR 游戏、AR 导航、三维重建等。|
|*Desired Tracking Mode*|期望的跟踪模式。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* VIO：只有跟踪和点击碰撞点云，CPU 和内存占用少，但是不支持平面检测、重定位和锚点。
* SLAM：同时跟踪和建图，支持丢失后的重定位、点击碰撞点云和平面检测，但是没有锚点，不支持实时校正位姿，且 CPU 和内存占用稍高。
* Anchor：同时跟踪和建图，支持丢失后的重定位、点击碰撞点云、平面检测和锚点，但是 CPU 和内存占用最高。
* LargeScale：适用于大场景下，同时跟踪和建图，支持丢失后的重定位、点击碰撞点云、平面检测和锚点。大景深下跟踪更稳定。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|
