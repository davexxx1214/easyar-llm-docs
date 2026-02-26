---
source: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/comparison.html
---

EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系
EasyAR 的运动跟踪（Motion Tracker）利用计算机视觉和惯性同步定位和建图（VI-SLAM）技术，在更多的手机和平板上实现六自由度（6 Degrees of Freedom, 6DoF）的实时跟踪功能。
## 为什么选择使用 EasyAR 运动跟踪
EasyAR 运动跟踪功能相较系统级的运动跟踪方案(如 ARKit、ARCore、华为 AR Engine 等)有以下优点：
* 提供更广泛的设备支持能力。覆盖了约70%的主流设备，相较于其他方案机型覆盖率高出 30-60%。
* 对中低端机型专门算法优化，保证算力有限的平台也有较好的效果。
* 无需安装其他应用，而 ARCore 等其他平台都需要用户手动下载安装对应算法的应用。
## EasyAR 运动跟踪功能的特点
EasyAR 通过先进的计算机视觉识别相机图像中显著特征点并跟踪其位置变化，结合设备的惯性测量单元(IMU)数据信息，实时计算当前设备相对于真实世界的六自由度位置和姿态。渲染引擎根据返回的姿态和朝向同步渲染虚拟场景就可以保证虚拟的物体与现实环境进行贴合。
* 真实尺度
利用设备的惯导传感器和相机图像数据融合，恢复轨迹和场景真实物理尺度。
* 鲁棒准确的运动跟踪
多传感器融合算法能降低长时间跟踪的漂移，且对于光照变化、弱纹理区域和动态物体等更鲁棒。
* 快速初始化
通常仅需要设备对着应用场景平移即可实现初始化。
* 视觉重定位
在设备跟踪丢失后/跟踪不佳后快速准确地恢复设备相对于世界坐标系的位姿。
## EasyAR 运动跟踪最佳实践
虽然 EasyAR 运动跟踪针对各种挑战性场景进行优化，为了保证最佳的效果，可以引导用户遵循下列最佳实践。
* 避免快速运动，包括平移或者旋转
* 减少纹理不丰富的区域
* 保证良好的光照条件
## 在 EasyAR Motion Tracker 与平台原生的运动跟踪功能之间切换
为保证最佳效果，在部分平台，EasyAR 可能默认选择可用的平台原生的运动跟踪方案而不需要额外配置。例如在 iOS 平台上，EasyAR SDK 会优先使用ARKit的运动跟踪功能。类似的，在部分 ARCore/AR Engine 支持的安卓/鸿蒙设备上，EasyAR SDK 可能会默认使用其提供的运动功能。
## 后续步骤
* 了解 EasyAR MotionTracker 支持的机型，请查看 [Motion Tracker 支持的设备](devices-easyar.html)
* 在 EasyAR 中使用 AR Engine 的运动跟踪，请查看 [AR Engine支持的机型](devices-arengine.html)