# EasyAR 专题包：motion-tracking

适用于上下文长度有限时的分卷输入。

## 目录
- `motion-tracking/comparison.md`
- `motion-tracking/devices-arcore.md`
- `motion-tracking/devices-arengine.md`
- `motion-tracking/devices-easyar.md`
- `motion-tracking/devices.md`
- `motion-tracking/intro.md`
- `motion-tracking/motion-tracking-and-easyar.md`

---

## EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系
- 章节路径: `motion-tracking/comparison.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/comparison.html

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

---

## 谷歌 ARCore 与运动跟踪
- 章节路径: `motion-tracking/devices-arcore.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices-arcore.html

# 谷歌 ARCore 与运动跟踪
谷歌的 ARCore 是用于在 Android 上的增强现实引擎。其为部分 Android 机型提供包括运动跟踪在内的多项能力。在 Unity 上为保证最佳效果，在 ARCore 支持的机型上，EasyAR Sense 默认选择 ARCore 的运动跟踪功能而不是 EasyAR 内置的 `Motion Tracker` 功能。
## ARCore 支持的机型和功能
与其他的 [运动跟踪](intro.html) 功能类似，ARCore 需要设备至少具备摄像头、陀螺仪和加速度计，而且经过谷歌标定并认证才可运行。
ARCore 官方支持的机型列表需要查阅 ARCore 官方文档（[中文](https://developers.google.cn/ar/devices?hl=zh-cn) / [English](https://developers.google.com/ar/devices)）。
> **注意**
需要注意的是，在支持机型上，需要安装额外的 `Google Play Services for AR` App 才可以运行 ARCore 功能，在部分机型可能已经预装，部分机型需要用户自行安装。
## 在 EasyAR 中调用 ARCore
在 EasyAR 使用 ARCore，支持的机型并不与官方机型一致, 主要体现在部分官方支持列表内的机型 ARCore 实测效果异常。可以通过 `ARCoreCameraDevice` 的 `isAvailable` 方法判断这些有问题的机型，然后禁用 ARCore。
ARCore 除了运动跟踪之外还支持环境理解、光照估计等功能，使用 EasyAR 运动跟踪仅调用 ARCore 的运动跟踪功能，不支持其他功能。
以下是 ARCore 效果测试异常禁用的机型列表，这些设备通过 `isAvailable` 检查 ARCore 可用性均返回 `False`。
|Brand|Model Name|
|Redmi|Redmi K40|
|Redmi|Redmi K30S Ultra|
|Redmi|Redmi K40 Gaming|
|Redmi|Redmi K40 Pro|
|Redmi|Redmi K50G|
|Redmi|K30 PRO|
|Redmi|Redmi K30 Pro Zoom Edition|
|Redmi|Redmi K40S|
|Redmi|Redmi K30|
|Xiaomi|Mi 10T|
|Xiaomi|Mi 10 Ultra|
|Xiaomi|MI 9|
|Xiaomi|Mi 10 Pro|
|Redmi|Redmi K20|
|Redmi|Redmi K20|
|Xiaomi|Mi 10T Lite|
|Xiaomi|Mi 10i|
|Xiaomi|MI 9 SE|
|Xiaomi|Mi 10 lite 5G|
|Xiaomi|Xiaomi 12X|
|Xiaomi|Mi 9 Lite|
|Redmi|Redmi K20 Pro|
|Redmi|Mi 9T Pro|
|Xiaomi|Mi 10|
|Xiaomi|Mi 10 Lite zoom|
## 延伸阅读
* [运动跟踪 支持的设备](devices.html)
* [EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系](comparison.html)

---

## 华为 AR Engine 与运动跟踪
- 章节路径: `motion-tracking/devices-arengine.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices-arengine.html

# 华为 AR Engine 与运动跟踪
华为的 AR Engine 是用于在 HarmonyOS/Android 上的增强现实应用的引擎。其为部分华为机型提供包括运动跟踪在内的多项能力。在 Unity 上，为保证最佳效果，在 AR Engine 支持的机型上，EasyAR Sense 默认选择 AR Engine 的运动跟踪功能而不是 EasyAR 内置的运动跟踪（Motion Tracker）。
> **重要事项**
这里所列的列表，是 EasyAR 实际测试并验证可用的，其他型号均不支持，注意与 AR Engine 官方支持的机型列表进行区分。
经过 EasyAR 验证通过可以正常使用 AR Engine 运动跟踪功能的机型如下:(截止 2026年 1月)
|设备型号|代号|
|Mate X5|HWALT-B|
|Mate 60 RS 非凡大师|HWALN|
|Mate 60|HWBRA|
|Mate 60 Pro|HWALN|
|Mate 60 Pro+|HWALN|
|Pura 70|HWADY|
|Pura 70 Pro+|HWHBN|
|Pura 70 Pro|HWHBN|
|Pura 70 Ultra|HWHBP|
|P50 Pocket|HWBAL|
|P50 Pro|HWJAD-Q|
|P50 Pro|HWJAD|
|P40|HWANA|
|P40 Pro|HWELS|
|P40 Pro|HWELS-P|
|P30|HWELE|
|P30 Pro|HWVOG|
|P20|HWEML|
|P20 Pro|HWCLT|
|Mate 40|HWOCE-L|
|Mate 40 Pro|HWNOH|
|Mate 40E Pro|HWNOH|
|Mate 40 Pro+|HWNOP|
|Mate 40 RS|HWNOP|
|Mate 30|HWTAS|
|Mate 30-5G版|HWTAS|
|Mate 30 Pro|HWLIO|
|Mate 30 RS 保时捷设计|HWLIO|
|Mate 30 Pro-5G版|HWLIO|
|Mate 30E Pro-5G版|HWLIO-L|
|Mate X2|HWTET|
|Mate 20|HWHMA|
|Mate 20 X|HWEVR|
|Mate 20 X-5G版|HWEVR|
|Mate X|HWTAH|
|MateXS|HWTAH|
|MateXS|HWTAH-C|
|Mate RS保时捷版|HWNEO|
|nova 8|HWANG|
|nova 8|HWANG-DL|
|nova 8 Pro|HWBRQ|
|nova 7|HWJEF|
|nova 7 Pro|HWJER|
|nova 6|HWWLZ|
|nova 6-5G版|HWWLZ|
|nova 5|HWYAL|
|nova 5|HWSPN|
|nova 5 Pro|HWSEA-A|
|nova 4|HWVCE|
|荣耀30|HWBMH|
|荣耀30S|HWCDY-H|
|荣耀30S|HWCDY|
|荣耀30 Pro|HWEBG|
|荣耀30 Pro+|HWEBG|
|荣耀V30|HWOXF|
|荣耀V30 Pro|HWOXF|
|荣耀20|HWYAL|
|荣耀20 Pro|HWYAL|
|荣耀V20|HWPCT|
|荣耀9x|HWSTK-HF|
|荣耀9x|HWHLK-H|
|MatePad Pro(MRX)|HWMRX|
|MatePad Pro 5G|HWMRX|
|MatePad Pro|HWMRX|
|MatePad Pro(WGR)|HWWGR|
|M6|HWSCM|
|M6|HWVRD|

---

## EasyAR 运动跟踪支持的设备
- 章节路径: `motion-tracking/devices-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices-easyar.html

# EasyAR 运动跟踪支持的设备
## EasyAR 运动跟踪的最低设备要求
要运行 EasyAR 运动跟踪需要满足以下必要（非充分）的要求
* 包含摄像机，加速度计和陀螺仪。
* Android 7.0 (API Level 24) 及以上。
> **注意**
如果设备缺少陀螺仪和加速度计，则无法使用运动跟踪功能，这种情况常在低端机型中相对常见(仅具备虚拟陀螺仪的机型不支持运动跟踪)。
## 保持最新的设备支持
为保持您的应用获取最新的设备支持，推荐下列方式：
* 集成最新发布的 EasyAR Sense SDK, 其内置最新的支持列表。
* SDK 在设备联网自动查询。可使用 CalibrationDownloader 联网并下载最新适配文件。
## EasyAR 运动跟踪的质量
EasyAR 根据设备本身的性能通过 Quality Level 进行分级，不同 Quality Level 的含义见下表。
|等级|说明|适用场景|
|NotSupported|设备不支持运动跟踪，可能是适配不达标或尚未适配|不可用于 AR 运动跟踪相关功能|
|Bad|设备不完全达标，尺度不稳定|有限的桌面尺度小场景|
|Limited|设备不完全达标，尺度接近准确|房间尺度中等场景，如 AR 游戏、AR 渲染、AR 导航|
|Good|设备达标，尺度准确|建筑物尺度大型场景，如 AR 游戏、AR 渲染、AR 导航、三维重建|
## 为什么设备不支持运动跟踪
新的机器设备默认并不支持运动跟踪，且列表里的手机可能存在个别机型不被支持的情况，可能的原因包括：
* 未完整适配，新机型发布，待适配。
* 硬件问题，例如部分机型并不包含陀螺仪。
* 效果验证不佳，EasyAR 通过标定确认机型运动跟踪效果不佳。
* 未联网下载最新的标定文件。
* 软件问题，例如系统升级后传感器同步出现异常被剔除。
如果您的机型不支持运动跟踪且硬件满足最低设备要求，请反馈您的设备具体型号，以便我们及时增加对您的设备的支持。
## EasyAR 运动跟踪支持的设备型号列表
EasyAR 会定期标定新发布的机型，不断增加运动跟踪支持的设备数量，更新频率正常是1次/季度。
当前 EasyAR 运动跟踪支持的机型见下表。
|设备型号|代号|Quality Level|
|Huawei Mate30 pro, HUAWEI MATE 30 PRO 5G,HUAWEI MATE 30 RS PORSCHE DESIGN|HWLIO|Good|
|Huawei Mate30 pro, HUAWEI MATE 30 PRO 5G,HUAWEI MATE 30 RS PORSCHE DESIGN|HWLIO-L|Good|
|hauwei Mate30e pro||Good|
|Huawei Mate30,HUAWEI MATE 30 5G|HWTAS|Good|
|Huawei P20|HWEML|Good|
|Huawei P30 pro|HWVOG|Good|
|Huawei P30|HWELE|Good|
|Huawei P30 lite / nova 4e|HWMAR|Good|
|Huawei P40|HWANA|Good|
|Huawei P40 4G||Good|
|honor Magic V Flip||Good|
|honor Magic V|HNMGI|Good|
|Honor Magic V||Good|
|Honor Magic V2||Good|
|Honor Magic VS||Good|
|Honor Magic VS2||Good|
|Honor Magic V3||Good|
|Honor Magic VS3||Good|
|Huawei P40 pro|HWELS|Good|
|Huawei P40 pro+|HWELS-P|Good|
|Huawei Mate40E||Good|
|Huawei Mate40|HWOCE-L|Good|
|Huawei Mate40 Pro|HWNOH|Good|
|Huawei Mate40 Pro+ / Huawei Mate 40 RS Porsche Design|HWNOP|Good|
|Mate50.Legacy data|HWCET|Good|
|Mate 50E. Legacy data|HWCET-QL|Good|
|TD Tech M40||Good|
|Mate 50 Pro. Legacy data|HWDCO|Good|
|Mate 60. Legacy data|HWBRA|Good|
|Mate 60 Pro|HWALN|Good|
|Mate 70||Good|
|Mate 70 Pro||Good|
|Mate 70 Pro+||Good|
|Huawei P50|HWABR-Q|Good|
|Huawei P50E|HWABR-QL|Good|
|TD Tech P50||Good|
|Huawei P50 Pocket|HWBAL|Good|
|Huawei P50 Pro|HWJAD|Good|
|Huawei P50 Pro|HWJAD-Q|Good|
|Huawei P60|HWLNA|Good|
|Huawei P60 Art||Good|
|Huawei P60 Pro|HWMNA|Good|
|Huawei Pura70||Good|
|Huawei Pura 70||Good|
|Huawei Pura 70Pro||Good|
|Huawei Pura 70 Pro||Good|
|Huawei Pura 70 Pro+||Good|
|Huawei Pura 70 Ultra||Good|
|Huawei Pura 80|hedy|Good|
|Huawei Pura 80 Pro|Lamarr|Good|
|Huawei Pura 80 Ultra|LamarrU|Good|
|Huawei Pura X||Good|
|Huawei Pocket||Good|
|Huawei Pocket 2||Good|
|Huawei nova9 SE|HWJLN-Q|Good|
|Huawei nova9 Pro|HWRTE|Good|
|Huawei nova9|HWNAM|Limited|
|Huawei nova10 pro|HWGLA-Q|Limited|
|Huawei nova10|HWNCO-Q|Limited|
|Huawei nova10 se|HWBNE-Q|Limited|
|Huawei nova 10Z|HWCHA-H|Limited|
|Huawei nova11|HWFOA|Limited|
|Huawei nova11SE||Good|
|Huawei nova11 Pro ultra|HWGOA|Limited|
|Huawei nova12||Good|
|Huawei nova12 Pro||Good|
|Huawei nova12 Ultra||Good|
|Huawei nova13||Good|
|Huawei nova13 Pro||Good|
|Huawei nova14||Good|
|Huawei nova14 Pro||Good|
|Huawei nova14 Ultra||Good|
|Huawei nova4|HWVCE|Good|
|Huawei Honor V20 / HONOR View20|HWPCT|Good|
|Huawei Honor 20 /Honor 20 pro /nova 5T|HWYAL|Good|
|Huawei Honor 20s||Good|
|Huawei Honor 10i||Good|
|Huawei Honor 20i||Good|
|Honor 30 pro / Honor 30 pro+|HWEBG|Good|
|Honor 30 pro+||Good|
|Honor 30|HWBMH-N|Good|
|Honor 30|HWBMH|Good|
|Honor 30|HWBMH-L|Good|
|Honor 30s|HWCDY|Good|
|Honor 30s|HWCDY-H|Good|
|Honor 30 lite|HWMXW|Bad|
|Honor V40|HWYOK|Bad|
|Honor V40|HWALA|Bad|
|Honor 50||Good|
|Honor 50E|HNJLH|Good|
|Honor 60||Good|
|Honor 60 SE||Good|
|Honor 60 Pro||Good|
|Honor 70||Good|
|Honor 70 Pro||Good|
|Honor 80||Good|
|Honor 80 Pro||Good|
|Honor 80 Pro zhipingban||Good|
|Honor 80 SE||Good|
|Honor 80 GT||Good|
|Honor 90||Good|
|Honor 90Pro||Good|
|Honor 90GT||Good|
|Honor 100||Good|
|Honor 100 Pro||Good|
|Honor 200||Good|
|Honor 200 Pro||Good|
|Honor GT||Good|
|Honor GT Power||Good|
|Honor 300||Good|
|Honor 300 Pro||Good|
|Honor 300 Ultra||Good|
|Honor 400||Good|
|Honor 400 Pro||Good|
|Honor play|HWCOR|Good|
|Huawei NZONE S7||Good|
|Huawei NZONE S7 Pro||Good|
|Huawei NZONE S7 Pro+||Good|
|Honor 8A 2020|HWJAT-M|Good|
|Honor note 10|HWRVL|Good|
|honor 50 Lite|HNNTN|Good|
|honor 60 SE|HNGIA|Good|
|honor X30|HNANY|Good|
|honor X30 Max|HNKKG|Good|
|honor X40||Good|
|honor X40 GT||Good|
|honor X50|Ali|Good|
|honor X50 GT||Good|
|honor X60||Good|
|honor X60 Pro||Good|
|honor X60 GT||Good|
|honor X70||Good|
|honor Play 30Plus|HNCMA|Bad|
|honor Play 40||Good|
|honor Play 40 Plus||Good|
|honor Play 50 Plus||Good|
|honor Play 60 Plus||Good|
|honor Play 70 Plus||Good|
|Huawei Y9a||Good|
|Honor Play 4 Pro 5G|HWOXP|Bad|
|Honor Play 5||Good|
|Honor Play 5T||Good|
|Honor Play 5T Pro||Good|
|Honor Play 6T||Good|
|Honor Play 6T Pro||Good|
|Honor Play 6C||Good|
|Honor Play 7T||Good|
|Honor Play 9C|Nick|Bad|
|Honor Play 9T Pro||Good|
|Honor Play 10C||Good|
|Huawei Mate Xs|HWTAH|Good|
|Huawei Mate Xs|HWTAH-C|Good|
|Huawei Mate XT||Good|
|Huawei Mate Xs2|HWPAL|Good|
|Huawei Mate X2|HWTET|Good|
|Huawei Mate X3|HWALT|Good|
|Huawei Mate X5|HWALT-B|Good|
|Huawei Mate X6||Good|
|Honor X10 5G|HWTEL|Good|
|Honor X10 5G|HWTEL-H|Good|
|Honor X10 Max 5G|HWKKG|Bad|
|Huawei MatePad Pro / MatePad Pro 5G /MatePad Pro wifi|HWMRX|Good|
|Huawei MatePad 11 (2021)|HWDBY|Limited|
|Huawei MatePad Pro 12.6 (2021)|HWWGR|Good|
|Huawei MatePad Pro 11 (2022)|HWGOT|Good|
|Huawei MatePad 10.8|HWSCMR|Good|
|Huawei MatePad Pro 10.8 (2021)|HWMRR|Good|
|Huawei MatePad 10.4|HWBAH|Good|
|Huawei MatePad 10.4|HWBAH3|Good|
|Huawei MediaPad M6 10.8|HWSCM|Good|
|Huawei MediaPad M6 8.4|HWVRD|Good|
|nova 5z / nova 5i pro|HWSPN|Good|
|vivo 5i||Good|
|Huawei nova 5|HWSEA-A|Good|
|nova 5 pro||Good|
|Huawei nova 6 / nova 6 5G|HWWLZ|Good|
|Huawei nova 7 5G|HWJEF-N|Good|
|Huawei nova 7 5G|HWJEF|Good|
|Huawei nova 7 pro 5G|HWJER|Good|
|Huawei nova 8 Pro|HWBRQ|Good|
|Huawei nova 8|HWANG|Good|
|Huawei nova 8|HWANG-DL|Good|
|Huawei Y Max/ Enjoy max|HWARS|Good|
|Huawei Y Max/ Enjoy max|HWARS-Q|Good|
|Huawei MediaPad M5 Lite 8|HWJDN2|Good|
|Huawei MediaPad M5 10 / pro|HWCMR|Good|
|Huawei MediaPad M5 8|HWSHT|Good|
|honor 50|HNNTH|Good|
|honor 50 Pro|HNRNA|Good|
|honor 60|HNLSA|Good|
|honor 60 Pro|HNTNA|Good|
|honor 70|HNFNE|Good|
|honor 70 pro|HNSDY|Good|
|honor 70 pro+|HNHPB|Good|
|honor X20|HNNTN|Bad|
|honor X20 SE|HNCHL|Bad|
|honor Magic 3|HNELZ|Bad|
|honor Magic 3 Pro||Good|
|honor Magic 3 Pro+||Good|
|honor Magic 4 lite / X9 5G|HNANY-Q|Good|
|honor Magic 4|HNLGE|Good|
|honor Magic 4 Pro||Good|
|honor Magic 4 ultimate||Good|
|Honor Magic 5|HWPGT|Good|
|Honor Magic 5 Pro||Good|
|Honor Magic V5|Maybach|Good|
|Mi Pad 6S Pro|sheng|Good|
|Honor Magic 6|HNBVL|Good|
|Honor Magic 6 Pro||Good|
|Honor Magic 6 Lite||Good|
|Honor Magic 7||Good|
|Honor Magic 7 Pro||Good|
|Honor Magic 7 Pro RSR||Good|
|Huawei honor V30 / V30 Pro / HONOR View30 / View30 Pro|HWOXF|Good|
|Huawei honor V40||Good|
|Huawei honor V purse||Good|
|Huawei Enjoy 50||Good|
|Huawei Enjoy 50 Pro||Good|
|Huawei Enjoy 50Z||Good|
|Huawei Enjoy 60X|HWSTG|Limited|
|Huawei Enjoy 60||Good|
|Huawei Enjoy 60 Pro||Good|
|Huawei Enjoy 70||Good|
|Huawei Enjoy 70 Pro||Good|
|Huawei Enjoy 70Z||Good|
|Huawei Enjoy 70S||Good|
|Huawei Enjoy 80||Good|
|Huawei Enjoy 20 5G|HWWKG|Bad|
|Huawei Enjoy 20 5G|HNKOZ-S|Bad|
|Huawei Enjoy 20 Plus 5G||Good|
|Huawei Enjoy Z 5G / Enjoy 20 Pro|HWDVC|Bad|
|Huawei Enjoy Z 5G / Enjoy 20 Pro|HWDVC-M|Bad|
|Honor Play 4T||Good|
|Honor Play 4T Pro||Good|
|Honor Play 4||Good|
|Honor Play 4 Pro||Good|
|Honor 9X / Huawei Enjoy 10 Plus / Huawei P Smart Z|HWSTK-HF|Good|
|Honor 9X Pro|HWHLK-H|Good|
|Huawei Mate 20|HWHMA|Good|
|Huawei Mate 20 X / Huawei Mate 20 X 5G|HWEVR|Good|
|Huawei HonorV10 / Honor View 10|HWBKL|Good|
|Huawei Enjoy 9 plus|HWJKM-H|Good|
|Huawei Enjoy 9 plus|HWJKM-HM|Good|
|Huawei honor 7A|HWAUM-Q|Good|
|Huawei Honor 9|HWSTF|Good|
|Huawei Mate 10 / Huawei Mate 10 Porsche Design|HWALP|Limited|
|Huawei Mate 10 pro|HWBLA|Good|
|Huawei nova 2s|HWHWI|Limited|
|Huawei nova 2 plus|HWBAC|Limited|
|Huawei nova 2s|HWHWI|Limited|
|Huawei nova 2|HWPIC|Limited|
|Huawei Mate9|HWMHA|Limited|
|Huawei Mate9 Pro|HWLON|Limited|
|Huawei P10|HWVTR|Limited|
|Huawei P10 plus|HWVKY|Limited|
|honor magic|HWNTS|Limited|
|honor V9|HWDUK|Limited|
|Huawei P9 Plus|HWVIE|Limited|
|Huawei P9|HWEVA|Limited|
|Huawei P20 lite|HWANE|Limited|
|Huawei HonorV10 / Honor View 10|HWBKL|Bad|
|Huawei Enjoy 9 plus|HWJKM-H|Bad|
|Huawei Enjoy 9 plus|HWJKM-HM|Bad|
|Huawei Honor 9|HWSTF|Bad|
|Huawei honor 7A|HWAUM-Q|Bad|
|Huawei Mate 10 / Huawei Mate 10 Porsche Design|HWALP|Bad|
|Huawei Mate 10 pro|HWBLA|Bad|
|Huawei nova 2s|HWHWI|Bad|
|Huawei nova 2 plus|HWBAC|Bad|
|Huawei nova 2s|HWHWI|Bad|
|Huawei nova 2|HWPIC|Bad|
|Huawei Mate9|HWMHA|Bad|
|Huawei Mate9 Pro|HWLON|Bad|
|Huawei P10|HWVTR|Bad|
|Huawei P10 plus|HWVKY|Bad|
|honor magic|HWNTS|Bad|
|honor V9|HWDUK|Bad|
|Huawei P9 Plus|HWVIE|Bad|
|Huawei P9|HWEVA|Bad|
|Huawei P20 lite|HWANE|Bad|
|Huawei nova|HWCAN|Bad|
|Huawei nova|HWCAZ|Bad|
|Huawei nova plus|HWMLA|Bad|
|Huawei P10 lite /Nova Youth|HWWAS-H|Bad|
|Honor V8|HWKNT|Bad|
|Honor 8|HWFRD|Bad|
|Honor V8 max / Honor note8|HWEDI|Bad|
|Honor 8X|HWJSN-HM|Limited|
|Huawei Honor 7|HWPLK|Bad|
|Huawei Mate 8|HWNXT|Bad|
|Huawei P20 Pro|HW-01K|Good|
|Huawei P20 Pro|HWCLT|Good|
|Huawei Honor 10|HWCOL|Good|
|Huawei nova 3i|HWINE|Good|
|HUAWEI Y9 2019 /enjoy 8Plus|HWJKM-H|Good|
|HUAWEI Y9 2019 /enjoy 8Plus|HWFLA-H|Good|
|enjoy 9 Plus||Good|
|enjoy 9S||Good|
|HUAWEI Y9s / Y9 2019 Prime 2019 / enjoy 10 Plus|HWSTK-HF|Good|
|HUAWEI enjoy 10 Enjoy 10||Good|
|Huawei Enjoy 10E enjoy 10E|HWMED|Bad|
|Huawei Enjoy 10S enjoy 10S|HWAQM|Bad|
|Huawei Enjoy 10S enjoy 10S|HWAQM-HF|Bad|
|Huawei Enjoy 10S enjoy 10S|HWJSN-H|Good|
|Huawei honor 8X max|HWARE-QC|Good|
|Huawei honor 8X max|HWARE-Q|Good|
|Huawei Mate 20 Pro /Huawei Mate 20 RS|HWLYA|Good|
|Huawei PORSCHE DESIGN HUAWEI Mate RS|HWNEO|Good|
|Huawei nova 3|HWPAR|Good|
|Huawei Mate 20 lite / MAIMANG 7|HWSNE|Good|
|Huawei MAIMANG 9|HWTNN|Bad|
|Huawei MAIMANG 10|TYH612M|Bad|
|Huawei Honor Magic 2|HWTNY|Good|
|Galaxy S8|SC-02J|Good|
|Galaxy S8|SCV36|Good|
|Galaxy S8|dreamqltecan|Good|
|Galaxy S8|dreamqltechn|Good|
|Galaxy S8|dreamqltecmcc|Good|
|Galaxy S8|dreamqltesq|Good|
|Galaxy S8|dreamqlteue|Good|
|Galaxy S8|dreamlte|Good|
|Galaxy S8|dreamlteks|Good|
|Galaxy S8|dreamlteskt|Good|
|Galaxy S8|dreamqlteue|Good|
|Galaxy S8 Lite|dreamliteqltechn|Good|
|Galaxy Note8|SC-01K|Good|
|Galaxy Note8|SCV37|Good|
|Galaxy Note8|greatqlte|Good|
|Galaxy Note8|greatqltechn|Good|
|Galaxy Note8|greatqltecmcc|Good|
|Galaxy Note8|greatqltecs|Good|
|Galaxy Note8|greatqlteue|Good|
|Galaxy Note8|greatlte|Good|
|Galaxy Note8|greatlte|Good|
|Galaxy Note8|greatlteks|Good|
|Galaxy Note8|greatlteks|Good|
|Galaxy Note9|crownqltecmcc|Good|
|Galaxy S8+|SCV35|Good|
|Galaxy S8+|SC-03J|Good|
|Galaxy S8+|dream2qltecan|Good|
|Galaxy S8+|dream2qltechn|Good|
|Galaxy S8+|dream2qltecmcc|Good|
|Galaxy S8+|dream2qltesq|Good|
|Galaxy S8+|dream2qlteue|Good|
|Galaxy S8+|dream2lte|Good|
|Galaxy S8+|dream2lteks|Good|
|Galaxy S8+|dream2lteskt|Good|
|Galaxy S8+|dream2qlteue|Good|
|Galaxy Note10+ 5G|d2xq|Good|
|Galaxy Note10+ 5G|d2xq2|Good|
|Galaxy Note10+ 5G|d2x|Good|
|Galaxy Note10+ 5G|d2xq|Good|
|Galaxy Note10+|d2s|Good|
|Galaxy Note10+|SCV45|Good|
|Galaxy Note10+|SC-01M|Good|
|Galaxy Note10+|d2xq|Good|
|Galaxy Note10 5G|d1x|Good|
|Galaxy Note10|d1q|Good|
|Galaxy Note10|d1|Good|
|Galaxy Note10 Lite|r7|Good|
|Samsung Galaxy Z Flip 5G|bloomxq|Good|
|Samsung Galaxy Z Flip 5G|bloomq|Good|
|Samsung Galaxy Z Flip 3||Good|
|Samsung Galaxy Z Flip 4||Good|
|Samsung Galaxy Z Flip 5||Good|
|Samsung W20 5G|zodiac|Good|
|Samsung W21 5G||Good|
|Samsung W22 5G||Good|
|Samsung W23 5G||Good|
|Samsung W23 Flip||Good|
|Samsung W24 5G||Good|
|Samsung W24 Flip||Good|
|Samsung W25 5G||Good|
|Samsung W25 Flip||Good|
|Samsung Galaxy Tab S6|gts6l|Good|
|Samsung Galaxy Tab S6|gts6lwifi|Good|
|Samsung Galaxy Tab S6 5G|gts6x|Good|
|Samsung Galaxy Tab S6 lite|gta4xl|Good|
|Samsung Galaxy Tab S6 lite|gta4xlwifi|Good|
|Samsung Galaxy F62|f62|Good|
|Samsung Galaxy F22|f22|Good|
|Galaxy S10 5G|beyondxq|Good|
|Galaxy S10 5G|beyondx|Good|
|Galaxy S10|beyond1|Good|
|Galaxy S10|beyond1q|Good|
|Galaxy S10|SCV41|Good|
|Galaxy S10|SC-03L|Good|
|Galaxy S10 lite|r5q|Good|
|Galaxy S10+ Olympic Games Edition|SC-05L|Good|
|Galaxy S10+|beyond2|Good|
|Galaxy S10+|beyond2q|Good|
|Galaxy S10+|SCV42|Good|
|Galaxy S10+|SC-04L|Good|
|Galaxy S10e|beyond0|Good|
|Galaxy S10e|beyond0q|Good|
|Galaxy S20+ / S20+ 5G|y2s|Good|
|Galaxy S20+ / S20+ 5G|y2q|Good|
|Galaxy S20+ / S20+ 5G|SCG02|Good|
|Galaxy S20+ / S20+ 5G|SC-52A|Good|
|Galaxy S20 Ultra / S20 Ultra 5G|z3q|Good|
|Galaxy S20 Ultra / S20 Ultra 5G|SCG03|Good|
|Galaxy S20 Ultra / S20 Ultra 5G|z3s|Good|
|Samsung Galaxy Xcover 5|xcover5|Good|
|Samsung Galaxy Xcover 6 pro|xcoverpro2|Good|
|Samsung Galaxy Z Fold2 5G|f2q|Good|
|Samsung Galaxy S20 FE|r8s|Good|
|Samsung Galaxy S20 FE 2022||Good|
|Samsung Galaxy S20 FE 5G|r8q|Good|
|zhifubao cloud XR|cic\_cloud|Good|
|Galaxy Fold /Fold 5G|winner|Good|
|Galaxy Z Flip3 5G|b2q|Good|
|Galaxy Z Fold2 5G||Good|
|Galaxy Z Flip3 5G|b2q|Good|
|Galaxy Z Fold3 5G|q2q|Good|
|Galaxy Z Flip4 5G|b4q|Good|
|Galaxy Z Fold4 5G|q4q|Good|
|Galaxy Z Fold5 5G|q5q|Good|
|Galaxy Z Fold6 5G|q6q|Good|
|Galaxy Z Fold7 5G|q7q|Good|
|Galaxy Z Flip5 5G|b5q|Good|
|Galaxy Z Flip6 5G|b6q|Good|
|Galaxy Z Flip7 5G|b7q|Good|
|Galaxy Z Flip7 5G|b7s|Good|
|Galaxy Z Flip7 5G|b7r|Good|
|Samsung Galaxy Tab A8 10.5|gta8|Good|
|Samsung Galaxy Tab A8 10.5|gta8wifi|Good|
|Samsung Galaxy Tab A7 10.4 (2020)|gta4l|Good|
|Samsung Galaxy Tab A7 10.4 (2020)|gta4lwifi|Good|
|Samsung Galaxy Tab Active3|gtactive3|Good|
|Samsung Galaxy Tab Active3|gtactive3wifi|Good|
|Galaxy S20 / S20 5G|x1s|Good|
|Galaxy S20 / S20 5G|SC-51A|Good|
|Galaxy S20 / S20 5G|SC51Aa|Good|
|Galaxy S20 / S20 5G|SCG01|Good|
|Galaxy S20 / S20 5G|x1q|Good|
|Galaxy S20 / S20 5G|SCG01|Good|
|Samsung Galaxy Note20|c1s|Good|
|Samsung Galaxy Note20 5G|c1q|Good|
|Samsung Galaxy Note20 Ultra 5G|c2s|Good|
|Samsung Galaxy Note20 Ultra 5G|c2q|Good|
|Samsung Galaxy Note20 Ultra 5G|SCG06|Good|
|Samsung Galaxy S21 5G|o1q|Good|
|Samsung Galaxy S21 5G|o1s|Good|
|Samsung Galaxy S21 5G|SCG09|Good|
|Samsung Galaxy S21 5G|SC-51B|Good|
|Samsung Galaxy S21 Ultra 5G|p3q|Good|
|Samsung Galaxy S21 Ultra 5G|p3s|Good|
|Samsung Galaxy S21 Ultra 5G|SC-52B|Good|
|Samsung Galaxy S21+ 5G|t2q|Good|
|Samsung Galaxy S21+ 5G|t2s|Good|
|Samsung Galaxy S21+ 5G|SCG10|Good|
|Samsung Galaxy S21 FE 5G|r9q|Good|
|Samsung Galaxy S21 FE 5G|r9s|Good|
|Samsung Galaxy S22 5G|r0q|Good|
|Samsung Galaxy S22 5G|r0s|Good|
|Samsung Galaxy S22+ 5G|g0q|Good|
|Samsung Galaxy S22+ 5G|t2s|Good|
|Samsung Galaxy S22+ 5G|g0s|Good|
|Samsung Galaxy S22 Ultra 5G|b0q|Good|
|Samsung Galaxy S22 Ultra 5G|b0s|Good|
|Samsung Galaxy S23|dm1q|Good|
|Samsung Galaxy S23|dm2q|Good|
|Samsung Galaxy S23|dm3q|Good|
|Samsung Galaxy S23|r11q|Good|
|Samsung Galaxy S23 Plus||Good|
|Samsung Galaxy S23 Ultra||Good|
|Samsung Galaxy S23 FE||Good|
|Samsung Galaxy S24|e1q|Good|
|Samsung Galaxy S24 Plus|e2q|Good|
|Samsung Galaxy S24 pro|e3q|Good|
|Samsung Galaxy S25|pa1q|Good|
|Samsung Galaxy S25 Plus|pa2q|Good|
|Samsung Galaxy S25 Edge|psq|Good|
|Samsung Galaxy S25 Ultra|pa3q|Good|
|Samsung Galaxy A6s|Phoenix|Good|
|Samsung Galaxy M62|m62|Good|
|Samsung Galaxy M51|m51|Good|
|Samsung Galaxy A13 5G|a13x|Good|
|Samsung Galaxy A73 5G|a73xq|Good|
|Samsung Galaxy A42 5G|a42xq|Good|
|Samsung Galaxy A42 5G|a42xuq|Good|
|Samsung Galaxy F41 / Galaxy M21s|f41|Good|
|Samsung Galaxy M31 Prime|m31|Good|
|Galaxy A52s 5G||Good|
|Samsung Galaxy A71 /A71 5G|a71|Good|
|Samsung Galaxy A71 /A71 5G|a7x|Good|
|Galaxy A Quantum|a71x|Good|
|Samsung Galaxy A51 /A51 5G|a51|Good|
|Samsung Galaxy A51 /A51 5G|a5x|Good|
|Samsung Galaxy A31|a31|Good|
|Samsung Galaxy A23|a23|Good|
|Samsung Galaxy A41|a41|Good|
|Samsung Galaxy M23|m23xq|Good|
|Samsung Galaxy M21|m21|Good|
|Samsung Galaxy M33|m33x|Good|
|Samsung Galaxy M31|m31|Good|
|Samsung Galaxy M31 5G|a32x|Good|
|Samsung Galaxy M13 5G|a13x|Good|
|Samsung Galaxy Z Flip|SCV47|Good|
|Samsung Galaxy Z Flip|bloomq|Good|
|Samsung Galaxy Xcover Pro|xcoverpro|Good|
|Samsung Galaxy M10s|m10s|Good|
|Samsung Galaxy Tab Active Pro|gtactivexl|Good|
|Samsung Galaxy Tab Active Pro|gtactivexlwifi|Good|
|Samsung Galaxy A33|a33x|Good|
|Samsung Galaxy A30s|a30s|Good|
|Samsung Galaxy M40|m40|Good|
|Samsung Galaxy M42|a42xq|Good|
|Samsung Galaxy M52|m52xq|Good|
|Samsung Galaxy M53|m53xq|Good|
|Samsung Galaxy M53|m53x|Good|
|Samsung Galaxy F42 5G|f42x|Good|
|Samsung Galaxy M30|m30|Good|
|Samsung Galaxy M30s|m30s|Good|
|Samsung Galaxy M31s|m31s|Good|
|Samsung Galaxy M32|m32|Good|
|Samsung Galaxy M32 5G|a32x|Good|
|Galaxy A9s|a9y18qltechn|Good|
|Galaxy A8(2018)|jackpotlte|Good|
|Galaxy A8(2018)|jackpotltecan|Good|
|Galaxy A8(2018)|jackpotlteks|Good|
|Galaxy A8+(2018)|jackpot2lte|Good|
|Samsung Galaxy Tab S7 FE|gts7xllitewifi|Good|
|Samsung Galaxy Tab S7 FE|gts7xllite|Good|
|Samsung Galaxy Tab S7 / Samsung Galaxy Tab S7 5G|gts7l|Good|
|Samsung Galaxy Tab S7 / Samsung Galaxy Tab S7 5G|gts7lwifi|Good|
|Samsung Galaxy Tab S7+ / Galaxy Tab S7+ 5G|gts7xl|Good|
|Samsung Galaxy Tab S7+ / Galaxy Tab S7+ 5G|gts7xlwifi|Good|
|Samsung Galaxy Tab S8|gts8wifi|Good|
|Samsung Galaxy Tab S8|gts8|Good|
|Samsung Galaxy Tab S8+|gts8pwifi|Good|
|Samsung Galaxy Tab S8+|gts8p|Good|
|Samsung Galaxy Tab S8 Ultra|gts8uwifi|Good|
|Samsung Galaxy Tab S8 Ultra|gts8u|Good|
|Samsung Galaxy M20|m20|Good|
|Samsung Galaxy M20|m20lte|Good|
|Samsung Galaxy A80|r1q|Good|
|Samsung Galaxy A42 5G|a42xq|Good|
|Samsung Galaxy A52 5G|a52xq|Good|
|Samsung Galaxy A52||Good|
|Samsung Galaxy A72|a72q|Good|
|Samsung Galaxy A60|a60q|Good|
|Samsung Galaxy A50|a50|Good|
|Samsung Galaxy A40|a40|Good|
|Samsung Galaxy A40s|a30c|Good|
|Samsung Galaxy A30|a30|Good|
|Samsung Galaxy A20e|a20e|Good|
|Samsung Galaxy A20|a20p|Good|
|Samsung Galaxy A20|a20|Good|
|Samsung Galaxy A22|a22|Good|
|Samsung Galaxy A22|a22x|Good|
|Samsung Galaxy A22s|a22x|Good|
|Samsung Galaxy A21s|a21s|Good|
|Samsung Galaxy A21|a21|Good|
|Samsung Galaxy A23 5G|a23xq|Good|
|Samsung Galaxy Tab S5e|gts4lv|Good|
|Samsung Galaxy Tab S5e|gts4lvwifi|Good|
|Samsung Galaxy Tab S5e|gts4lvwifichn|Good|
|Samsung Galaxy A8s|a8sqlte|Good|
|Samsung Galaxy A8s|a8sqltechn|Good|
|Samsung Galaxy A9 (2018)|a9y18qlte|Good|
|Samsung Galaxy A9 (2018)|a9y18qltekx|Good|
|Samsung Galaxy A9 (2018)|a9y18qltechn|Good|
|Samsung Galaxy A8+ (2018)|jackpot2lte|Good|
|Samsung Galaxy C7|c7ltechn|Good|
|Samsung Galaxy C7|c7proltechn|Good|
|Samsung Galaxy C7 Pro|c7prolte|Good|
|Samsung Galaxy C7 Pro|c7proltechn|Good|
|Samsung Galaxy C8|jadeltechn|Good|
|Samsung Galaxy C8|jadeltecmcc|Good|
|Samsung Galaxy C9 Pro|c9lte|Good|
|Samsung Galaxy C9 Pro|c9ltechn|Good|
|Samsung Galaxy C7 Pro|c7prolte|Good|
|Samsung Galaxy C7 Pro|c7proltechn|Good|
|Samsung Galaxy C55|m55xq|Good|
|Samsung Galaxy A51 5G UW|a51xq|Limited|
|Samsung Galaxy A51 5G UW|a51x|Limited|
|Samsung Galaxy A53 5G|a53x|Good|
|Samsung Galaxy A55 5G||Good|
|Samsung Galaxy A56 5G||Good|
|Samsung Galaxy A54 5G||Good|
|Samsung Galaxy F52 5G|f52x|Good|
|Samsung Galaxy A20s|a20s|Good|
|Samsung Galaxy A50s|a50s|Limited|
|Galaxy A90 5G|r3q|Good|
|Samsung Galaxy A8s|a8sqlte|Good|
|Samsung Galaxy A8s|a8sqltechn|Good|
|Samsung Galaxy A70|a70q|Limited|
|Samsung Galaxy A70s|a70s|Limited|
|Samsung Galaxy Quantum2|a82xq|Limited|
|Samsung Galaxy A9 star|astarqltechn|Bad|
|Samsung Galaxy A9 star|astarqltecmcc|Bad|
|Samsung Galaxy A9 star Lite|a6pltechn|Bad|
|Samsung Galaxy A9 star Lite|a6pltecmcc|Bad|
|Samsung Galaxy A7 (2018)|a7y18lte|Bad|
|Samsung Galaxy A7 (2018)|a7y18lteks|Bad|
|Galaxy S7|herolte|Good|
|Galaxy S7|heroltebmc|Good|
|Galaxy S7|heroltektt|Good|
|Galaxy S7|heroltelgt|Good|
|Galaxy S7|herolteskt|Good|
|Galaxy S7|heroqlteacg|Good|
|Galaxy S7|heroqlteaio|Good|
|Galaxy S7|heroqlteatt|Good|
|Galaxy S7|heroqltecctvzw|Good|
|Galaxy S7|heroqltechn|Good|
|Galaxy S7|heroqltelra|Good|
|Galaxy S7|heroqltemtr|Good|
|Galaxy S7|heroqltechn|Good|
|Galaxy S7|heroqltespr|Good|
|Galaxy S7|heroqltetfnvzw|Good|
|Galaxy S7|heroqltetmo|Good|
|Galaxy S7|heroqlteue|Good|
|Galaxy S7|heroqlteusc|Good|
|Galaxy S7|heroqltevzw|Good|
|Galaxy S7 Edge|SC-02H|Good|
|Galaxy S7 Edge|SCV33|Good|
|Galaxy S7 Edge|hero2qlteatt|Good|
|Galaxy S7 Edge|hero2qltecctvzw|Good|
|Galaxy S7 Edge|hero2qltechn|Good|
|Galaxy S7 Edge|hero2qltespr|Good|
|Galaxy S7 Edge|hero2qltetmo|Good|
|Galaxy S7 Edge|hero2qlteue|Good|
|Galaxy S7 Edge|hero2qlteusc|Good|
|Galaxy S7 Edge|hero2qltevzw|Good|
|Galaxy S7 Edge|hero2lte|Good|
|Galaxy S7 Edge|hero2ltebmc|Good|
|Galaxy S7 Edge|hero2ltektt|Good|
|Galaxy S7 Edge|hero2ltelgt|Good|
|Galaxy S7 Edge|hero2lteskt|Good|
|Galaxy S7 Edge|herolte|Good|
|Galaxy S7 Edge|heroltebmc|Good|
|Galaxy S7 Edge|heroltektt|Good|
|Galaxy S7 Edge|herolteskt|Good|
|Galaxy S7 Edge|heroqlteacg|Good|
|Galaxy S7 Edge|heroqlteaio|Good|
|Galaxy S7 Edge|heroqlteatt|Good|
|Galaxy S7 Edge|heroqltecctvzw|Good|
|Galaxy S7 Edge|heroqltechn|Good|
|Galaxy S7 Edge|heroqltelra|Good|
|Galaxy S7 Edge|heroqltemtr|Good|
|Galaxy S7 Edge|heroqltespr|Good|
|Galaxy S7 Edge|heroqltetfnvzw|Good|
|Galaxy S7 Edge|heroqltetmo|Good|
|Galaxy S7 Edge|heroqlteue|Good|
|Galaxy S7 Edge|heroqlteusc|Good|
|Galaxy S7 Edge|heroqltevzw|Good|
|Galaxy Note9|SC-01L|Good|
|Galaxy Note9|SCV40|Good|
|Galaxy Note9|SCV40\_jp\_kdi|Good|
|Galaxy Note9|SM-N960D|Good|
|Galaxy Note9|SM-N960J|Good|
|Galaxy Note9|crownqltechn|Good|
|Galaxy Note9|crownqltecmcc|Good|
|Galaxy Note9|crownqltecs|Good|
|Galaxy Note9|crownqltesq|Good|
|Galaxy Note9|crownqlteue|Good|
|Galaxy Note9|crownlte|Good|
|Galaxy Note9|crownlteks|Good|
|Galaxy S9|SC-02K|Good|
|Galaxy S9|SCV38|Good|
|Galaxy S9|starqltechn|Good|
|Galaxy S9|starqltecmcc|Good|
|Galaxy S9|starqltecs|Good|
|Galaxy S9|starqltesq|Good|
|Galaxy S9|starqlteue|Good|
|Galaxy S9 +|SC-03K|Good|
|Galaxy S9 +|SCV39|Good|
|Galaxy S9 +|star2qltechn|Good|
|Galaxy S9 +|star2qltecs|Good|
|Galaxy S9 +|star2qltesq|Good|
|Galaxy S9 +|star2qlteue|Good|
|Galaxy S9 +|star2lte|Good|
|Galaxy S9 +|star2lteks|Good|
|Galaxy S9 +|starlte|Good|
|Galaxy S9 +|starlteks|Good|
|Galaxy A5(2017)|a5y17lte|Good|
|Galaxy A5(2017)|a5y17ltecan|Good|
|Galaxy A5(2017)|a5y17ltektt|Good|
|Galaxy A5(2017)|a5y17ltelgt|Good|
|Galaxy A5(2017)|a5y17lteskt|Good|
|Galaxy A7(2017)|a7y17lte|Good|
|Galaxy A7(2017)|a7y17lteskt|Good|
|Galaxy Tab S4|gts4llte|Good|
|Galaxy Tab S4|gts4llteatt|Good|
|Galaxy Tab S4|gts4lltechn|Good|
|Galaxy Tab S4|gts4lltekx|Good|
|Galaxy Tab S4|gts4lltespr|Good|
|Galaxy Tab S4|gts4lltetmo|Good|
|Galaxy Tab S4|gts4llteusc|Good|
|Galaxy Tab S4|gts4lltevzw|Good|
|Galaxy Tab S4|gts4lwifi|Good|
|Galaxy Tab S4|gts4lwifichn|Good|
|Galaxy J5|j5y17lte|Good|
|Galaxy J5|j5y17ltedx|Good|
|Galaxy J5|j5y17ltektt|Good|
|Galaxy J5|j5y17ltelgt|Good|
|Galaxy J5|j5y17lteskt|Good|
|Galaxy J5|j5y17ltextc|Good|
|ZTE Axon 10 pro 5G|P855A21|Good|
|ZTE Axon 10 pro|P855A01|Good|
|ZTE Axon 10 pro|P855A02|Good|
|ZTE Axon 10 pro|P855A03|Good|
|ZTE Axon 10 pro|P855A03\_NA|Good|
|ZTE Axon 10s pro 5G|P865A02|Good|
|ZTE nubia Play|NX651J|Good|
|ZTE Axon 11|P671A13|Good|
|ZTE Axon 11|P671A11|Good|
|ZTE Axon 11 5G|P725A12|Good|
|ZTE Axon 11 5G|P725A11|Good|
|ZTE Axon 9 Pro|P845A01|Good|
|ZTE Axon 9 Pro|P845A02|Good|
|ZTE Axon 20 5G / Axon 20 5G Extreme|P725A02|Good|
|ZTE Axon 40||Good|
|ZTE Axon 40 Ultra||Good|
|ZTE Axon 40 Pro||Good|
|ZTE S30 SE|P633S01|Good|
|ZTE S30|P653S07|Good|
|ZTE S30 Pro|P768A02|Good|
|ZTE nubia Z20|NX627J|Good|
|ZTE nubia Z20|NX627J-EEA|Good|
|ZTE nubia Z30 Pro||Good|
|ZTE nubia Z40 Pro||Good|
|ZTE nubia||Good|
|ZTE nubia X|NX616J|Good|
|ZTE Blade X1 5G|Z6750|Good|
|ZTE Blade 11 Prime||Good|
|ZTE Red Magic 6 Pro||Good|
|ZTE Red Magic 6||Good|
|ZTE Red Magic 6s / Red Magic 6s Pro|NX669J-S|Good|
|ZTE Red Magic 6s / Red Magic 6s Pro|NX669J-EEA|Good|
|ZTE Red Magic 6s / Red Magic 6s Pro|NX669J-UN|Good|
|ZTE Red Magic 7|NX679J-EEA|Good|
|ZTE Red Magic 7 pro|NX709J-EEA|Good|
|ZTE Red Magic 7s||Good|
|ZTE Red Magic 7s pro||Good|
|ZTE Red Magic 9s pro||Good|
|ZTE Voyage 20 Pro|P653S11|Good|
|ZTE Red Magic 6R||Good|
|ZTE Blade V40||Good|
|ZTE Blade V30|P618F05|Good|
|ZTE Blade V30 vita|P963F06|Good|
|ZTE Blade V30 vita|P963F06\_A|Good|
|ZTE Blade 20 5G|P653S06|Good|
|ZTE Blade V10|P671F20|Good|
|ZTE Blade V10 Vita|P963F01|Good|
|ZTE Blade V10 Vita RU|P963F01D|Good|
|ZTE Axon 30 / 30 Pro 5G|P875A02|Good|
|ZTE Axon 30 / 30 Pro 5G|P875A12|Good|
|ZTE Axon 30 / 30 Pro 5G|P870A01|Good|
|ZTE Axon 30 Ultra|P875A11|Good|
|ZTE nubia Red Magic 5G|NX659J-EEA|Good|
|ZTE nubia Red Magic 5G|NX659J-RU|Good|
|ZTE nubia Red Magic 5G|NX659J-UN|Good|
|ZTE nubia Red Magic 5s|NX659J|Good|
|ZTE Red Magic 5G lite|NX651J-EEA|Good|
|ZTE nubia Red Magic mars rng /Red Magic mars|NX619J|Good|
|ZTE nubia Red Magic mars rng /Red Magic mars|NX619J-EEA|Good|
|ZTE nubia Red Magic 3s|NX629J\_V1S|Good|
|ZTE nubia Red Magic 3|NX629J|Good|
|ZTE nubia Red Magic 3|NX629J-EEA|Good|
|ZTE Blade V9|P450L10|Bad|
|ZTE Blade V9|P840F03|Bad|
|ZTE Blade V9|P450F10|Bad|
|ZTE Axon 7|ailsa\_ii|Bad|
|ZTE nubia Z17 mini|NX569J|Bad|
|ZTE nubia Z17|NX563J|Bad|
|ZTE nubia Z17s|NX595J|Bad|
|ZTE nubia Z17 lite|NX591J|Bad|
|ZTE nubia Z17 miniS|NX589J|Bad|
|ZTE nubia Z11 mini|NX529J|Bad|
|ZTE nubia M2|NX551J|Bad|
|ZTE nubia Z9 Max|NX510J|Bad|
|ZTE nubia Z9 Max|NX518J|Bad|
|ZTE nubia Z18 mini|NX611J|Bad|
|ZTE nubia Z11 mini S|NX549J|Bad|
|ZTE Blade V8|ZTE\_BLADE\_V0800|Bad|
|ZTE Blade V8 mini|ZTE\_BLADE\_V0850|Bad|
|ZTE Blade V8 Lite / Blade V8 SE|ZTE\_BLADE\_V0820|Bad|
|ZTE nubia Z50|PQ82A01|Good|
|ZTE nubia z50 ultra||Good|
|ZTE nubia z60||Good|
|ZTE nubia z60 pro||Good|
|ZTE nubia Hongmo9||Good|
|OPPO Reno|OP47DD|Good|
|OPPO Reno|OP47DDL1|Good|
|OPPO Reno|OP46B1|Good|
|OPPO Reno 10X|OP4847L1|Good|
|OPPO Reno 10X|OP4845|Good|
|OPPO Reno 10X|OP4845L1|Good|
|OPPO Reno 10X|OP4847|Good|
|OPPO Reno 10X|OP46C3|Good|
|OPPO Reno A|OP47CFL1|Good|
|OPPO realme X|RMX1901CN|Good|
|OPPO realme Pad||Good|
|OPPO realme X3|RMX2081L1|Good|
|OPPO realme X3|RMX2083L1|Good|
|OPPO realme X3|RMX2085L1|Good|
|OPPO realme X3 SuperZoom|RMX2086L1|Good|
|OPPO realme X2 pro|RMX1931CN|Good|
|OPPO realme X2 pro|RMX1931L1|Good|
|OPPO realme XT|RMX1921|Good|
|OPPO realme XT|RMX1921L1|Good|
|OPPO realme XT|RMX1922|Good|
|oppo Realme 6|RMX2001L1|Good|
|oppo Realme 6|RMX2003L1|Good|
|oppo Realme 6s / Realme Narzo|RMX2002L1|Good|
|oppo Realme 7 Pro|RMX2170L1|Good|
|oppo Realme 7|RMX2151|Good|
|oppo Realme 7 5G|RMX2111L1|Good|
|oppo Realme 7i / Realme Narzo 20|RE50C1|Good|
|oppo Realme 6 pro|RMX2061L1|Good|
|oppo Realme 6 pro|RMX2063L1|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2040|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2030|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2041|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2042|Good|
|oppo Realme 3 pro|RMX1851|Good|
|oppo Realme Narzo 10A|RMX2020|Good|
|oppo Realme Narzo 20A|RMX2050|Good|
|oppo Realme Narzo 20 Pro||Good|
|oppo Realme Narzo 30|RMX2156L1|Good|
|oppo Realme Narzo 30A|RMX3171|Good|
|oppo Realme Narzo 30 5G|RE513CL1|Good|
|oppo Realme Narzo 30 Pro 5G / Realme Q2|RMX2117L1|Good|
|oppo Realme Narzo 50|RMX3286|Good|
|oppo Realme Narzo 50A|RMX3430|Good|
|oppo Realme Narzo 50i|RMX3235|Good|
|oppo Realme GT 5G|RMX2202L1|Good|
|oppo Realme 9||Good|
|oppo Realme 9 speed||Good|
|oppo Realme GT Neo Flash|RE5469|Good|
|oppo Realme GT Master||Good|
|oppo Realme GT Master Explorer||Good|
|oppo Realme GT Neo2||Good|
|oppo Realme GT Neo2T||Good|
|oppo Realme GT 2||Good|
|oppo Realme 10||Good|
|oppo Realme 10s||Good|
|oppo Realme 10 Pro||Good|
|oppo Realme 10 Pro Plus||Good|
|oppo Realme 11||Good|
|oppo Realme 11 Pro||Good|
|oppo Realme 11 Pro Plus||Good|
|oppo Realme 12 Pro||Good|
|oppo Realme 12 Pro Plus||Good|
|oppo Realme 12||Good|
|oppo Realme 12X||Good|
|oppo Realme 13||Good|
|oppo Realme 13 Pro||Good|
|oppo Realme 13 Pro+||Good|
|oppo Realme 14||Good|
|oppo Realme 14 Pro||Good|
|oppo Realme 14 Pro Plus||Good|
|oppo Realme 15||Good|
|oppo Realme 15 Pro||Good|
|oppo Realme 15T||Good|
|OPPO realme V3||Good|
|OPPO realme V5||Good|
|OPPO realme V11||Good|
|OPPO realme V15||Good|
|OPPO realme V20||Good|
|OPPO realme V23i||Good|
|OPPO realme V30||Good|
|OPPO realme V30T||Good|
|OPPO realme V50||Good|
|OPPO realme V50S||Good|
|OPPO realme V60||Good|
|OPPO realme V60S||Good|
|OPPO realme V60 Pro||Good|
|OPPO realme V70||Good|
|OPPO realme V70S||Good|
|OPPO Reno ACE|OP4A89|Good|
|OPPO Reno ACE2|OP4AD9|Good|
|OPPO Reno Z|OP48A1|Good|
|OPPO Reno Z|OP48A1L1|Good|
|OPPO Reno Z|OP4699|Good|
|OPPO Reno 5G|OP46C7|Good|
|oppo Find X /Find X Lamborghini||Good|
|OPPO Reno 2|OP4B83L1|Good|
|OPPO Reno 2|OP4A57|Good|
|OPPO Reno 2 F||Good|
|OPPO Reno 2 Z|OP4B65L1|Good|
|OPPO Reno 2 Z|OP4A43|Good|
|OPPO Reno 3|OP4B9EL1|Good|
|OPPO Reno 3 5G china|OP4ADD|Good|
|OPPO Reno 3 A|OP4BAFL1|Good|
|OPPO F21 Pro||Good|
|OPPO F19||Good|
|OPPO F19 pro|OP4F43L1|Good|
|OPPO F19 pro+||Good|
|OPPO F19s||Good|
|OPPO F17 pro|OP4C51L1|Good|
|OPPO F17||Good|
|OPPO Reno 3 Youth 5G|OP4AB5|Good|
|OPPO Reno 3 Pro 5G china|OP4A9D|Good|
|OPPO Reno 3 Pro|OP4C5FL1|Good|
|OPPO Reno 3 Pro|OP4C2DL1|Good|
|OPPO Reno 4||Good|
|OPPO Reno 4F||Good|
|OPPO Reno 4Z||Good|
|OPPO Reno 4Lite||Good|
|OPPO Reno 4SE||Good|
|OPPO Reno 4 pro||Good|
|OPPO Reno 5 pro||Good|
|OPPO Reno 5 pro+|OP4EA7|Good|
|OPPO Reno 5 4G & 5G|OP4EA3|Good|
|OPPO Reno 5 4G & 5G|OP4F0BL1|Good|
|OPPO Reno 5 4G & 5G|OP4F1FL1|Good|
|OPPO Reno 5 4G & 5G|OP4F25L1|Good|
|OPPO Reno 5|OP4F1BL1|Good|
|OPPO Reno 5|OP4E8F|Good|
|OPPO Reno 5A|OP4F2BL1|Good|
|OPPO Reno 5F/5Lite|OP4F43L1|Good|
|OPPO Reno 5Z|OP4F4DL1|Good|
|OPPO Reno 5Z|OP4EB7|Good|
|OPPO Reno 5K|OP4E59|Good|
|OPPO Reno 6||Good|
|OPPO Reno 6 Pro||Good|
|OPPO Reno 6 Pro+|OP4EC1|Limited|
|OPPO Reno 6Z||Good|
|OPPO pad||Good|
|OPPO Reno 7SE||Good|
|OPPO Reno 7||Good|
|OPPO Reno 7 Pro|OP52E1L1|Good|
|OPPO Reno 7 Z 5G||Good|
|OPPO Pad Air||Good|
|OPPO Reno 8||Good|
|OPPO Reno 8 Pro||Good|
|OPPO Reno 8 Pro+||Good|
|OPPO Reno 9||Good|
|OPPO Reno 9 Pro||Good|
|OPPO Reno 9 Pro Plus||Good|
|OPPO Reno 10||Good|
|OPPO Reno 11||Good|
|OPPO Reno 11 Pro||Good|
|OPPO Reno 12||Good|
|OPPO Reno 12 Pro||Good|
|OPPO Reno 13||Good|
|OPPO Reno 13 Pro||Good|
|OPPO Reno 14||Good|
|OPPO Reno 14 Pro||Good|
|OPPO A72 5G||Good|
|OPPO A72|OP4C72L1|Good|
|OPPO A12 /A11k||Good|
|OPPO A53 5G|OP4F53L1|Good|
|OPPO A1 Pro|OP5613|Limited|
|OPPO A5 Pro||Good|
|OPPO A93s||Good|
|OPPO A93|OP4C51L1|Good|
|OPPO A95 5G||Good|
|OPPO A95/Reno 6Lite||Good|
|OPPO A96||Good|
|OPPO A97||Good|
|OPPO A56/A56s||Good|
|OPPO A55/A55s||Good|
|OPPO A52|OP4C77L1|Good|
|OPPO A52|OP4C7BL1|Good|
|OPPO A52|OP4AE7|Good|
|OPPO A58|OP526D|Good|
|OPPO A92s|OP4ABB|Good|
|OPPO A91|OP4ACF|Good|
|OPPO A74 5G||Good|
|OPPO A74||Good|
|OPPO A12||Good|
|OPPO A31||Good|
|OPPO A35|OP4E7B|Good|
|OPPO A9X|PCEM00|Good|
|OPPO K5|OP4AA7|Good|
|OPPO K3|OP4679|Good|
|OPPO K3|OP486B|Good|
|OPPO K1|PBCM30|Good|
|OPPO realme X youth|RMX1851CN|Good|
|OPPO realme Q|RMX1971CN|Good|
|OPPO realme C11 2021|RMX3231|Good|
|OPPO realme V5 5G|RMX2111CN|Good|
|OPPO realme V5 5G|RMX2112CN|Good|
|OPPO realme V23|RE5487|Good|
|OPPO realme U1|RMX1831|Good|
|OPPO realme U1|RMX1833|Good|
|OPPO realme V25|RE547D|Good|
|OPPO realme V25 Pro ??|RMX3143|Good|
|OPPO realme Q3???|RMX3142|Good|
|oppo Realme V13|RE5081|Good|
|oppo Realme Q3i||Good|
|oppo Realme Q3 Pro Carnival Edition|RE811C|Good|
|oppo Realme C35|RMX3511|Good|
|OPPO A5 2020||Good|
|OPPO A9 2020|OP4B80L1|Good|
|OPPO A9 2020|OP46F1|Good|
|OPPO A7X|PBBM00|Good|
|OPPO A7X|PBBT00|Good|
|OPPO A8|PDBM00|Bad|
|OPPO A8|PDBT00|Bad|
|OPPO K7X||Good|
|OPPO K9x|OPD2A0|Good|
|OPPO K9 5G|OP4E9F|Good|
|OPPO K9s||Good|
|OPPO K9 Pro|OP5245|Limited|
|OPPO K9 Pro|PEYM00|Limited|
|OPPO K10||Good|
|OPPO K10 Pro||Good|
|OPPO K11x||Good|
|OPPO K12X||Good|
|OPPO K12||Good|
|OPPO K12 Plus||Good|
|OPPO K12S||Good|
|OPPO K13||Good|
|OPPO K13 Turbo||Good|
|OPPO A11|A11|Bad|
|OPPO A11|OP4A4D|Bad|
|OPPO A11|A11w|Bad|
|OPPO A11|OP4A4D|Bad|
|OPPO A11X|A11|Good|
|OPPO A11X|OP4A54|Good|
|OPPO A3|PADM00|Good|
|OPPO A2||Good|
|OPPO A2 Pro||Good|
|OPPO A2m||Good|
|OPPO A2x||Good|
|OPPO A3|CPH1837|Good|
|OPPO A3m||Good|
|OPPO A3x||Good|
|OPPO A3i||Good|
|OPPO A3 Pro||Good|
|OPPO A3s|CPH1803|Good|
|OPPO A3s|CPH1853|Good|
|OPPO A5x||Good|
|OPPO A5||Good|
|OPPO A1||Good|
|oppo Find X2|OP4BA1L1|Good|
|oppo Find X2|OP4A77|Good|
|oppo Find X2 lite|OP4C41L1|Good|
|oppo Find X2 Neo|OP4C2DL1|Good|
|oppo Find X2 pro / X2 pro Lamborghini|OP4BA2L1|Good|
|oppo Find X2 pro / X2 pro Lamborghini|OP4A7A|Good|
|OPPO Find X3 lite||Good|
|OPPO Find X3 neo||Good|
|OPPO Find X3|OP4E5D|Good|
|OPPO Find N||Good|
|OPPO Find N2||Good|
|OPPO Find N3||Good|
|OPPO Find N5||Good|
|OPPO F11 pro|OP4863|Good|
|OPPO F15||Good|
|OPPO Find X3 pro|OP4F57L1|Good|
|OPPO Find X3 pro|OP4E3F|Good|
|OPPO Find X5|PFFM10|Good|
|OPPO Find X5 lite||Good|
|OPPO Find X5 pro||Good|
|OPPO Find X6||Good|
|OPPO Find X6 Pro||Good|
|OPPO Find X7|OP5661FL1|Good|
|OPPO Find X7 Ultra|OP565FL1|Good|
|OPPO Find X8||Good|
|OPPO Find X8S||Good|
|OPPO Find X8S plus||Good|
|OPPO Find X8 Ultra||Good|
|OPPO realme X2|RMX1991CN|Good|
|OPPO realme X2|RMX1992L1|Good|
|OPPO realme X2|RMX1993L1|Good|
|realme V3|RMX2200CN|Good|
|OPPO realme X50 5G|RMX2025CN|Good|
|OPPO realme X50 5G|RMX2051CN|Good|
|OPPO realme X50 5G|RMX2144L1|Good|
|OPPO realme X50 5G|RE5477|Good|
|OPPO realme X50m 5G|RE508C|Good|
|OPPO realme X50m 5G|RMX2141CN|Good|
|OPPO realme X50m 5G|RMX2142CN|Good|
|OPPO realme X50t 5G|RE508C|Good|
|OPPO realme X50t 5G|RMX2142CN|Good|
|OPPO realme 8 pro|RMX3081L1|Good|
|OPPO realme 8|RMX3085L1|Good|
|OPPO realme 8i||Good|
|OPPO realme 8S||Good|
|OPPO realme 8 5G||Good|
|OPPO realme 9 pro|RMX3471|Good|
|OPPO realme 9 pro+|RMX3392|Good|
|OPPO realme X7 5G|RMX3092L1|Limited|
|OPPO realme X7 5G|RMX2176CN|Limited|
|OPPO realme X7 pro|RMX2121CN|Limited|
|OPPO realme X7 pro|RMX3115|Limited|
|OPPO realme X7 pro|RMX3115|Good|
|OPPO realme X7 Max 5G|RMX3031L1|Good|
|OPPO realme X7 pro Ultra|RMX3116CN|Good|
|OPPO realme X7 pro Ultra|RMX3115CN|Good|
|OPPO realme gt neo5|RMX3706|Good|
|OPPO realme gt neo5|RMX3708|Good|
|OPPO realme gt neo5|RMX3700|Limited|
|OPPO realme neo7||Good|
|OPPO realme neo7 Turbo||Good|
|OPPO realme neo7x||Good|
|OPPO realme X50 pro 5G|RMX2076L1|Good|
|OPPO realme X50 pro 5G|RMX2071CN|Good|
|OPPO realme X50 pro 5G|RMX2075L1|Good|
|OPPO realme X50 pro Play|RMX2072CN|Good|
|OPPO realme 5 / 5s|RMX1911L1|Good|
|OPPO realme 5 / 5s|RMX1911|Good|
|OPPO realme 5 / 5s|RMX1915|Good|
|OPPO realme 5 / 5s|RMX1919|Good|
|OPPO realme 5 / 5s|RMX1925|Good|
|OPPO realme 5 / 5s|RMX1926|Good|
|OPPO realme 5i|RMX2030|Good|
|OPPO realme 5 Pro|RMX1971|Good|
|OPPO realme 5 Pro|RMX1973|Good|
|OPPO realme 5 Pro|RMX1971L1|Good|
|OPPO realme V11 5G|RMX3121CN|Good|
|OPPO realme V11 5G|RMX3122CN|Good|
|OPPO realme V15 5G|RMX3092CN|Good|
|OPPO realme V15 5G|RMX3093CN|Good|
|oppo Realme Narzo 30 Pro|RMX3161|Good|
|oppo Realme GT Neo|RMX3031CN|Limited|
|oppo Realme Q2||Good|
|oppo Realme Q2 Pro||Good|
|oppo Realme Q3 5G|RMX3161CN|Good|
|oppo Realme Q3s|RE548B|Good|
|oppo Realme Q3s|RE548BL1|Good|
|oppo Realme Q3 Pro 5G|RMX2205CN|Good|
|oppo Realme Q5||Good|
|oppo Realme Q5 Pro 5G/Realme GT Neo 3T||Good|
|oppo Realme GT2|RE5471|Good|
|oppo Realme GT2|RE58B2L1|Good|
|oppo Realme GT2|RE5465|Good|
|oppo Realme GT2 Pro||Good|
|oppo Realme GT Neo3||Good|
|oppo Realme GT Neo5||Good|
|oppo Realme GT Neo5SE||Good|
|oppo Realme GT Neo6||Good|
|oppo Realme GT Neo6SE||Good|
|oppo Realme GT 5||Good|
|oppo Realme GT 5 Pro||Good|
|oppo Realme GT 6||Good|
|oppo Realme GT 7 Pro||Good|
|oppo Realme GT 7 SE||Good|
|oppo Realme GT 7||Good|
|OPPO R17 Pro / RX17 Pro|PBDM00|Good|
|OPPO R17 Pro / RX17 Pro|PBDT00|Good|
|OPPO R17 Pro / RX17 Pro|CPH1877|Good|
|OPPO R17|CPH1879|Good|
|OPPO R17|PBEM00|Good|
|OPPO R17|PBET00|Good|
|OPPO R17 NEO / OPPO AX7 pro|CPH1893|Good|
|OPPO R15|PACT00|Bad|
|OPPO R15|PACM00|Bad|
|OPPO R15|PAAM00|Bad|
|OPPO R15|PAAT00|Bad|
|OPPO R15|CPH1835|Bad|
|OPPO R15X|PBCM10|Bad|
|OPPO R15X|PBCT10|Bad|
|OPPO R15 pro|CPH1831|Bad|
|OPPO R15 pro|CPH1833|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11Plus|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11sPlus|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11Plusk|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11s|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|R9|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|R9Plus|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|R9PlusA|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|X9079|Bad|
|OPPO R9s/R9sPlus/R9sk|R9s|Bad|
|OPPO R9s/R9sPlus/R9sk|R9sPlus|Bad|
|OPPO R9s/R9sPlus/R9sk|CPH1611|Bad|
|OPPO R9s/R9sPlus/R9sk|R9sk|Bad|
|OPPO R9s/R9sPlus/R9sk|CPH1607|Bad|
|OPPO A59s|A59|Bad|
|vivo IQOO Pro 5G|PD1916|Good|
|vivo IQOO Pro 5G|PD1916F|Good|
|vivo IQOO|PD1824|Good|
|vivo IQOO|PD1824BA|Good|
|vivo IQOO|V1824BA|Good|
|vivo IQOO|V1824A|Good|
|vivo IQOO Neo|PD1936|Good|
|vivo IQOO Neo|PD1936F|Good|
|vivo IQOO Neo|PD1914|Good|
|vivo IQOO Neo|PD1914F|Good|
|vivo IQOO Pro|PD1922|Good|
|vivo IQOO Pro|PD1922F|Good|
|vivo IQOO 3|PD1955F|Good|
|vivo iQOO Neo3|PD1981|Good|
|vivo iQOO Neo3|PD1981F|Good|
|vivo IQOO 3 5G|I1928|Good|
|vivo IQOO 3 5G|I1927|Good|
|vivo IQOO 3 5G|PD1955|Good|
|vivo IQOO 3 PRO 5G|PD2024|Good|
|vivo IQOO 5 5G|PD2024F|Good|
|vivo IQOO 5 5G|PD2024|Good|
|vivo IQOO 5 pro|PD2025F|Good|
|vivo IQOO 5 pro|PD2025|Good|
|vivo IQOO 8 Pro|PD2141|Good|
|vivo IQOO 8|PD2136|Good|
|vivo IQOO 9|PD2171|Good|
|vivo IQOO 9 Pro|PD2172|Good|
|vivo IQOO 9 SE|2019|Good|
|vivo IQOO 9T|I2201|Good|
|vivo IQOO 10|PD2217|Good|
|vivo IQOO 10 Pro|PD2218|Good|
|vivo IQOO 12 Pro||Good|
|vivo IQOO 12||Good|
|vivo IQOO 13||Good|
|vivo IQOO 7||Good|
|vivo IQOO 11|PD2243|Good|
|vivo IQOO 11 Pro|PD2254|Good|
|vivo IQOO 11S|PD2304|Good|
|vivo IQOO neo5||Good|
|vivo IQOO neo5 Lite|PD2118|Good|
|vivo IQOO neo5 SE|PD2157|Good|
|vivo s10E|PD2130|Good|
|vivo s10|PD2121|Good|
|vivo s12|PD2162|Good|
|vivo s12|PD2163|Good|
|vivo S10||Good|
|vivo S10 Pro||Good|
|vivo S15||Good|
|vivo S15 Pro||Good|
|vivo s15|PD2203|Good|
|vivo s15|PD2207|Good|
|vivo s15|PD2190|Good|
|vivo s16|PD2244|Good|
|vivo s16|PD2245|Good|
|vivo s16|PD2239|Good|
|vivo s16 pro||Good|
|vivo S17|PD2283|Good|
|vivo S17T|PD2282|Good|
|vivo S17 Pro|PD2284|Good|
|vivo S17E|PD2285|Good|
|vivo S18||Good|
|vivo S18 Pro||Good|
|vivo S18E||Good|
|vivo S19||Good|
|vivo S19 Pro||Good|
|vivo S20||Good|
|vivo S20 Pro||Good|
|vivo S30||Good|
|vivo S30 Pro Mini||Good|
|vivo S12||Good|
|vivo S12 Pro||Good|
|vivo IQOO neo5s|PD2154|Limited|
|vivo IQOO neo6|PD2196|Good|
|vivo IQOO neo6 SE Neo 6 SE|PD2199|Good|
|vivo IQOO neo7|PD2231|Good|
|vivo IQOO neo7|PD2232|Good|
|vivo IQOO neo7|PD2238|Good|
|vivo IQOO neo8|PD2301|Good|
|vivo IQOO neo8|PD2302|Good|
|vivo IQOO neo9||Good|
|vivo IQOO neo9S||Good|
|vivo IQOO neo9 Pro||Good|
|vivo IQOO neo9S Pro Plus||Good|
|vivo IQOO neo10 pro||Good|
|vivo IQOO neo10||Good|
|vivo IQOO neo10 pro plus||Good|
|vivo T1 Pro|PD2123|Good|
|vivo T1|PD2115|Good|
|vivo T2||Good|
|vivo X70|PD2133|Good|
|vivo X70|PD2132|Good|
|vivo X70 Pro|PD2134|Good|
|vivo X70 Pro+|PD2145|Good|
|vivo X70 Pro+|PD2114|Good|
|vivo X fold 5||Good|
|vivo X fold|PD2178|Good|
|vivo X note|PD2170|Good|
|vivo X80||Good|
|vivo X80 Pro+||Good|
|vivo X80 Pro|PD2186|Good|
|vivo iqoo z6|PD2220|Good|
|vivo iqoo z6|PD2164U|Good|
|vivo X90|PD2241|Good|
|vivo X90|PD2242|Good|
|vivo X90|PD2227|Good|
|vivo X90S|PD2241|Good|
|vivo X100|PD2309|Limited|
|vivo X100 Pro||Good|
|vivo X100S||Good|
|vivo X100S Pro||Good|
|vivo X100 Ultra||Good|
|vivo X200||Good|
|vivo X200S||Good|
|vivo X200 Pro||Good|
|vivo X200 Pro Mini||Good|
|vivo X Fold 3||Good|
|vivo X Fold 3 Pro||Good|
|vivo S6 5G|PD1962|Good|
|vivo S6 5G|PD1962B|Good|
|vivo S7|PD2020|Good|
|vivo S7|PD2080|Good|
|vivo S7e|PD2031|Good|
|vivo S7e|PD2031EA|Good|
|vivo Z6|PD1963|Good|
|vivo Z6 5G|V1963A|Good|
|vivo Z6 5G|3PD1963|Good|
|vivo V20 2021|2040|Good|
|vivo V21e 5G|2055|Good|
|vivo V23e||Good|
|vivo V20|2025|Good|
|vivo S10e||Good|
|vivo V15 pro|1818|Good|
|vivo V15 pro|1818N|Good|
|vivo V15|1819N|Good|
|vivo V15|1819|Good|
|vivo V21 5G|2050|Good|
|vivo Y95|1807|Good|
|vivo Y95|1807N|Good|
|vivo V9 pro|1851|Good|
|vivo V9 6GB|1723CF|Good|
|vivo V9|1727ID|Good|
|vivo Y71|PD1731D|Good|
|vivo Y71|1801|Good|
|vivo V9 Youth / Y85|1727|Good|
|vivo V9 Youth / Y85|1726|Good|
|vivo Y7s|PD1913|Good|
|vivo Y20 2021||Good|
|vivo IQOO Z3||Good|
|vivo IQOO Y31s 5G||Good|
|vivo IQOO z5x||Good|
|vivo IQOO U3|PD2061|Good|
|vivo IQOO U5E||Good|
|vivo IQOO U5|PD2197|Bad|
|vivo Y70s|PD2002|Good|
|vivo Y70t||Good|
|vivo Y71t||Good|
|vivo Y72 5G||Good|
|vivo Y76s|PD2156|Good|
|vivo Y74s||Good|
|vivo Y50t/ IQOO U1|PD2023|Bad|
|vivo iqoo u1x|PD2065|Bad|
|vivo Y76|PD2156|Good|
|vivo Y76|PD2156U|Good|
|vivo Y77|PD2219|Good|
|vivo Y77|PD2224|Good|
|vivo Y77|PD2278|Good|
|vivo Y78|PD2271|Good|
|vivo Y78|PD2279|Good|
|vivo Y78T||Good|
|vivo Y81|PD1732|Good|
|vivo Y89|PD1730E|Good|
|vivo Y91|PD1818C|Good|
|vivo Y93|PD1818|Bad|
|vivo Y93 Standard|PD1818B|Bad|
|vivo Y93S|PD1818C|Bad|
|vivo Y97|PD1813|Bad|
|vivo Z3|PD1813B|Limited|
|vivo Y50|PD1965|Good|
|vivo Y50 5G|PD2443|Good|
|vivo Y51|Y51|Good|
|vivo Y55 5G|PD2164|Good|
|vivo Y55 5G|PD2279|Good|
|vivo Y53s||Good|
|vivo Y52 5G||Good|
|vivo Y52|PD2057|Good|
|vivo Y52|PD2106|Good|
|vivo T1x|PD2123|Good|
|vivo Y3|PD1901|Bad|
|vivo Y3|PD1930|Bad|
|vivo Y5 S|PD1934A|Good|
|vivo Y7S|PD1913|Bad|
|vivo Y73|PD1731C|Good|
|vivo Y73|PD2031|Good|
|vivo Y73|PD2164UC|Good|
|vivo Y100||Good|
|vivo Y100i||Good|
|vivo Y100T||Good|
|vivo Y100 GT||Good|
|vivo Y200i||Good|
|vivo Y200||Good|
|vivo Y200 GT||Good|
|vivo Y200T||Good|
|vivo Y300||Good|
|vivo Y300 pro||Good|
|vivo Y300T||Good|
|vivo Y12||Good|
|vivo Y85A|PD1730|Limited|
|vivo Y31S|PD2054|Bad|
|vivo Y31S|PD2068|Bad|
|vivo Y31S|PD2092|Bad|
|vivo Y30|PD2036|Bad|
|vivo Y32|PD2158|Bad|
|vivo Y32|PD2168|Bad|
|vivo Y32|PD2180|Bad|
|vivo Y32t||Good|
|vivo Y33|PD2166|Limited|
|vivo Y33|PD2317|Limited|
|vivo Y31||Good|
|vivo Y35|PD2205|Limited|
|vivo Y37||Good|
|vivo Y37 Pro||Good|
|vivo Y37T|PD2443|Limited|
|vivo Y37C||Good|
|vivo Y36|PD2318|Limited|
|vivo Y36t|PD2327|Limited|
|vivo IQOO Z5 Pro / Z5||Good|
|vivo IQOO Z6 Pro|I2126|Limited|
|vivo IQOO Z6|I2203|Limited|
|vivo IQOO Z6|I2208|Limited|
|vivo IQOO Z6|I2206|Limited|
|vivo IQOO Z6|I2127|Limited|
|vivo IQOO Z6|I2126|Limited|
|vivo IQOO Z6x||Good|
|vivo IQOO Z7||Good|
|vivo IQOO Z7X||Good|
|vivo IQOO Z7i||Good|
|vivo IQOO Z8X||Good|
|vivo IQOO Z8||Good|
|vivo IQOO Z9||Good|
|vivo IQOO Z9 Turbo||Good|
|vivo IQOO Z9X||Good|
|vivo IQOO Z10||Good|
|vivo IQOO Z10 Turbo+||Good|
|vivo IQOO Z10X||Good|
|vivo Z5i|PD1941|Good|
|vivo Z5|PD1921|Good|
|vivo Z5x|PD1911|Good|
|vivo Z5x|PD1919|Good|
|vivo Z5x|PD1990|Good|
|vivo Z5x 2020|PD2020|Good|
|vivo Z1 pro|1951|Good|
|vivo Y9s|PD1945|Bad|
|vivo S1|PD1831|Good|
|vivo S1 Pro|PD1832|Good|
|vivo X27|PD1829|Good|
|vivo X27|PD1838|Good|
|vivo X27 pro|PD1836|Good|
|vivo X30 /X30 pro|PD1938|Good|
|vivo X50|PD2001|Good|
|vivo X50|2004|Good|
|vivo X50 pro+|PD2011|Good|
|vivo X50 pro|PD2005|Good|
|vivo X60t||Good|
|vivo X60 5G||Good|
|vivo X60|PD2046|Good|
|vivo X60|PD2059|Good|
|vivo X60|PD2085|Good|
|vivo X60|PD2047|Good|
|vivo X60|PD2120|Good|
|vivo X60t Pro+||Good|
|vivo X51||Good|
|vivo X60 Pro 5G||Good|
|vivo X60 Pro+ 5G|PD2056|Good|
|vivo S9|PD2072|Good|
|vivo S9e|PD2048|Good|
|vivo S5|PD1932|Good|
|vivo S1 Prime|1920|Good|
|vivo S1 Prime|1937|Good|
|vivo V20 SE|2023|Good|
|vivo V23 5G|2130|Good|
|vivo V23 Pro 5G|2132|Good|
|vivo NEX S|PD1805|Good|
|vivo NEX 2|PD1821|Good|
|vivo X50 lite|1937|Good|
|vivo X50 lite|1920|Good|
|vivo G1|PD1962|Good|
|vivo G1|PD1962B|Good|
|vivo G2|PD2318|Good|
|vivo G3|PD2443|Good|
|vivo NEX 3|PD1923|Good|
|vivo NEX 3 5G|PD1924|Good|
|vivo NEX 3 5G|1913|Good|
|vivo NEX 5||Good|
|vivo NEX 3S|PD1950|Good|
|vivo Y10|PD2140|Bad|
|vivo Y10|PD2168|Bad|
|vivo Y10|PD2180|Bad|
|vivo X20A/X20|PD1709|Limited|
|vivo X20Plus|PD1710|Limited|
|vivo X20Plus UD|PD1721|Limited|
|vivo X23|PD1809|Good|
|vivo X23|PD1816|Good|
|vivo X21 /X21A|1725|Limited|
|vivo X21 /X21A|PD1728|Limited|
|vivo X21UD|PD1728UD|Limited|
|vivo X21i|PD1801|Limited|
|vivo X21s|PD1814|Limited|
|vivo X21s|1804|Limited|
|vivo X21s|1806|Limited|
|vivo X21s|1814|Limited|
|vivo X9|PD1616|Bad|
|vivo X9i|PD1624|Bad|
|vivo X9s plus|PD1635|Bad|
|vivo X9Plus|PD1619|Bad|
|vivo X9s|PD1616B|Bad|
|vivo V3Max|V3Max|Bad|
|vivo V3Max A|PD1523|Bad|
|vivo V3Max +A|PD1523B|Bad|
|vivo NEX A|PD1806B|Good|
|vivo NEX Dual Display Edition|PD1806|Good|
|vivo pad||Good|
|Mi Note 10 / MI CC9 Pro/ Note 10 Pro|tucana|Good|
|Mi Note 10 / MI CC9 Pro/ Note 10 Pro|sweet|Good|
|MI note 10 lite|toco|Good|
|MI 10|umi|Good|
|MI 10 lite 5|monet|Good|
|Mi lite 5G|monet|Good|
|Mi 10T lite|gauguin|Good|
|MI 10T / Mi 10T Pro|apollo|Good|
|Mi 10i 5G|gauguininpro|Good|
|Mi Mix Fold|cetus|Good|
|Mi Mix Fold 3||Good|
|Mi Mix Fold 4||Good|
|Mi Mix Flip|ruyi|Good|
|MI 10 Pro|cmi|Good|
|MI 10 lite zoom / F Mi 10 Lite 5G|vangogh|Good|
|Mi 10 Ultra|cas|Good|
|Mi 10s|thyme|Good|
|Mi civi|mona|Good|
|Mi civi 1s|zijin|Good|
|Mi civi 2|ziyi|Good|
|Mi civi 3|yuechu|Good|
|Mi civi 4 pro|chenfeng|Good|
|Mi civi 5 pro||Good|
|Mi 11|venus|Good|
|Mi 11T|amber|Good|
|Mi 11T Pro|vili|Good|
|Mi 11 Lite 5G NE|lisa|Good|
|Mi 11 Lite 5G|renoir|Good|
|Mi 11 Lite|courbet|Good|
|Mi 11 Pro|mars|Good|
|Mi 11 Ultra|star|Good|
|Mi 12|cupid|Good|
|Mi 12X|psyche|Good|
|Mi 12 Pro|zeus|Good|
|Mi 12 Pro|daumier|Good|
|Mi 12 Lite|taoyao|Good|
|Mi 11i HyperCharge|pissarroinpro|Good|
|Mi Mix Fold 2|zizhan|Good|
|Mi 12s|mayfly|Good|
|Mi 12S Ultra|thor|Good|
|Mi 12S Pro|unicorn|Good|
|Mi 13|fuxi|Good|
|Mi 13R||Good|
|Mi 13 5G|breeze|Bad|
|Mi 13C|gale|Bad|
|Mi 13|ishtar|Bad|
|Mi 13T||Good|
|Mi 13T Pro||Good|
|Mi 13 Pro|nuwa|Bad|
|Mi 13 lite|ziyi|Bad|
|Mi 14|houji|Bad|
|Mi 14T|degas|Bad|
|Mi 14T pro|rothko|Bad|
|Mi 14 Pro|shennong|Good|
|Mi 14 Ultra|aurora|Good|
|Mi 15 Ultra|xuanyuan|Good|
|Mi 15||Good|
|Mi 15 Pro||Good|
|Mi 15S Pro|dijun|Good|
|Mi 17||Good|
|Mi 17 Pro||Good|
|Mi 17 Pro Max||Good|
|Mi 17 Ultra||Good|
|Mi Pad 6||Good|
|Mi Pad 6S Pro|sheng|Good|
|Mi Pad 7|uke|Good|
|Mi pad 7||Good|
|Mi Pad 7 Pro|muyu|Good|
|Mi pad 7 Pro||Good|
|MI CC 9 Meitu Edition|vela|Good|
|MI CC 9e|laurus|Good|
|xiaomi MI 9 pro 5G|crux|Good|
|xiaomi MI 9|cepheus|Good|
|xiaomi MI 9 se|grus|Good|
|xiaomi REDMI k20 /Mi 9T|davinci|Good|
|xiaomi REDMI k20 /Mi 9T|davincin|Good|
|xiaomi REDMI k20 /Mi 9T|davinciin|Good|
|Mi 9T pro|raphaelin|Good|
|xiaomi REDMI k20 pro|raphael|Good|
|xiaomi REDMI k20 pro|raphaelin|Good|
|xiaomi REDMI k20 pro|raphaels|Good|
|Xiaomi Redmi 10X Pro 5G|bomb|Good|
|Xiaomi Redmi 10X Pro 5G|banana|Good|
|Xiaomi Redmi 10X 5G|atom|Good|
|Xiaomi Redmi 10X 5G|apricot|Good|
|Xiaomi Redmi 9T|lime|Good|
|Xiaomi Redmi 9|galahad|Good|
|Xiaomi Redmi 9A|dandelion|Good|
|Xiaomi Redmi 10X 4G|merlin|Bad|
|xiaomi REDMI k40 Gaming|ares|Good|
|xiaomi REDMI k40s|munch|Good|
|xiaomi REDMI k40 Pro||Good|
|xiaomi REDMI k40 Pro Plus||Good|
|Redmi A3|blue|Good|
|Redmi A3 Pro||Good|
|Redmi A5|serenity|Good|
|Redmi 12C|earth|Good|
|Redmi 12C|aether|Good|
|Redmi 13C|gale|Good|
|Redmi 13C|gust|Good|
|Redmi 14C|pond|Good|
|Redmi 14C|2409BRN2CC|Good|
|Redmi 14R 5G||Good|
|Redmi 15|spring|Good|
|Redmi 15 5G||Good|
|Redmi 15T|goya|Good|
|Redmi 15T Pro||Good|
|xiaomi POCO F3 GT|aresin|Good|
|xiaomi POCO F4 GT|ingres|Good|
|xiaomi POCO F4|munch|Good|
|xiaomi POCO F4 Pro|matisse|Good|
|xiaomi POCO F7|onyx|Good|
|xiaomi POCO F7 Pro|zorn|Good|
|xiaomi POCO F7 Ultra|miro|Good|
|xiaomi REDMI k50 Gaming|ingres|Good|
|xiaomi REDMI k50|rubens|Good|
|xiaomi REDMI k50i|xagain|Good|
|xiaomi REDMI k50 pro|matisse|Good|
|xiaomi REDMI k50 ultra|diting|Good|
|xiaomi REDMI k40 pro / REDMI k40 pro+ / Mi 11i|haydn|Good|
|xiaomi REDMI k40 / POCO F3|alioth|Good|
|Xiaomi Redmi K60|mondrian|Good|
|Xiaomi Redmi K60 Pro|socrates|Good|
|xiaomi Redmi K60 Ultra|corot|Good|
|Xiaomi Redmi K60E|rembrandt|Good|
|xiaomi Redmi K70|corot|Good|
|xiaomi Redmi K70 Pro||Good|
|xiaomi Redmi K70 Ultra||Good|
|xiaomi Redmi K70E||Good|
|xiaomi Redmi K80 Pro|miro|Good|
|xiaomi Redmi K80||Good|
|xiaomi REDMI k30|phoenix|Good|
|xiaomi REDMI k30 Ultra|cezanne|Good|
|xiaomi REDMI k30 5G /K30i|picasso|Good|
|xiaomi REDMI k30S Ultra|apollo|Good|
|xiaomi REDMI k30 pro / Poco F2 Pro|lmi|Good|
|xiaomi REDMI k30 pro / Poco F2 Pro|lmiin|Good|
|xiaomi REDMI k30 pro zoom Edition|lmipro|Good|
|xiaomi REDMI k30 pro zoom Edition|lmiinpro|Good|
|Xiaomi Pad 5|nabu|Good|
|Xiaomi Pad 5 Pro|elish|Good|
|Xiaomi Pad 5 Pro 5G|enuma|Good|
|xiaomi 11X|aliothin|Good|
|xiaomi 11X pro|haydnin|Good|
|xiaomi 11i||Good|
|xiaomi Mix 4|odin|Good|
|xiaomi Mix4||Good|
|Xiaomi Redmi Note 10 Pro/ max|sweet|Good|
|Xiaomi Redmi Note 10 Pro/ max|sweetin|Good|
|Xiaomi Redmi Note 10 Pro/ max|chopin|Good|
|Xiaomi Redmi Note 10|sunny|Good|
|Xiaomi Redmi Note 10s|maltose|Good|
|Xiaomi Redmi Note 10s|rosemary|Good|
|Xiaomi Redmi Note 10s|secret|Good|
|Xiaomi Redmi Note 10 5G|camellia|Good|
|Xiaomi Redmi Note 10 5G|camellian|Good|
|Xiaomi Redmi Note 10T 5G|camellia|Good|
|Xiaomi Redmi Note 11 / 11T|evergo|Good|
|Xiaomi Redmi Note 11s|fleur|Good|
|Xiaomi Redmi Note 11s|miel|Good|
|Xiaomi Redmi Note 11s|opal|Good|
|Xiaomi Redmi Note 11E|light|Good|
|Xiaomi Redmi Note 11E Pro|veux|Good|
|Xiaomi Redmi Note 11T Pro|xaga|Good|
|Xiaomi Redmi Note 11T Pro+|xagapro|Good|
|Xiaomi Redmi Note 11 Pro|pissarro|Good|
|Xiaomi Redmi Note 11 Pro|viva|Good|
|Xiaomi Redmi Note 11 Pro|vida|Good|
|Xiaomi Redmi Note 11 Pro+|pissarropro|Good|
|Xiaomi Redmi Note 11 Pro+|peux|Good|
|Xiaomi Redmi Note 12 5G|sunstone|Limited|
|Xiaomi Redmi Note 12 Tansuozhe|rubyplus|Limited|
|Xiaomi Redmi Note 12 Pro jisuban|redwood|Limited|
|Xiaomi Redmi Note 12 5G Pro|ruby|Good|
|Xiaomi Redmi Note 12 +|rubypro|Good|
|Xiaomi Redmi Note 12 Pro jisuban|marble|Good|
|Xiaomi Redmi Note 12T Pro||Good|
|Xiaomi Redmi Note 13||Good|
|Xiaomi Redmi Note 13 Pro||Good|
|Xiaomi Redmi Note 13 Pro Plus||Good|
|Xiaomi Redmi Note 13R||Good|
|Xiaomi Redmi Note 13R Pro|peridot|Good|
|Xiaomi Redmi Note 14 5G||Good|
|Xiaomi Redmi Note 14||Good|
|Xiaomi Redmi Note 14 Pro||Good|
|Xiaomi Redmi Note 14 Pro+||Good|
|Xiaomi Redmi Note 14S||Good|
|Xiaomi Redmi Note 15||Good|
|Xiaomi Redmi Note 15 Pro||Good|
|Xiaomi Redmi Note 15 Pro Plus||Good|
|Xiaomi Redmi Turbo 3||Good|
|Xiaomi Redmi Pad Pro||Good|
|Xiaomi Redmi Turbo 4||Good|
|Xiaomi Redmi Turbo 4 Pro||Good|
|xiaomi REDMI Note 7 Pro|violet|Good|
|xiaomi REDMI Note 7|lavender|Good|
|xiaomi REDMI Note 8|ginkgo|Good|
|xiaomi REDMI Note 8 pro|begonia|Good|
|xiaomi REDMI Note 8 pro|begoniain|Good|
|Redmi Note 8T|willow|Good|
|Redmi Note 8 2021|biloba|Good|
|Poco C3|angelicain|Good|
|Poco X2|phoenixin|Good|
|Poco X3|karna|Good|
|Poco X3 NFC|surya|Good|
|Poco X3 Pro|bhima|Good|
|Poco X3 Pro|vayu|Good|
|Poco X3 GT|chopin|Good|
|Poco X4 Pro|peux|Good|
|Poco X4 Pro|veux|Good|
|Xiaomi Poco M2 Pro|gram|Good|
|Xiaomi Poco M3 Pro / Redmi Note 10T 5G|camelliain|Good|
|Xiaomi Poco M3||Good|
|Xiaomi Poco M3 Pro 5G|camellian|Good|
|Xiaomi Poco M3 Pro 5G|camellia|Good|
|Xiaomi Poco M4 Pro 5G|miel|Good|
|Xiaomi Poco M4 Pro 5G|fleur|Good|
|Xiaomi Poco M4 Pro 5G|evergreen|Good|
|Xiaomi Poco M4 Pro 5G|evergo|Good|
|Redmi Note 9 / Redmi 10X 4G|merlin|Good|
|Redmi Note 9 / Redmi 10X 4G|merlinin|Good|
|Redmi Note 9 5G|cannon|Good|
|Redmi Note 9 Pro|joyeuse|Good|
|Redmi Note 9 Pro|lime|Good|
|Redmi Note 9 Pro / Redmi Note 9s / redmi Note 10 lite|curtana|Good|
|Redmi Note 9 Pro 5G|gauguinpro|Good|
|Redmi Note 9 Pro Max|excalibur|Good|
|Redmi Note 9T 5G|cannong|Good|
|Redmi Note 11/ Pro|selenes|Good|
|Redmi Note 11/ Pro|spes|Good|
|Redmi Note 11/ Pro|spesn|Good|
|Redmi Note 11/ Pro|evergo|Good|
|Redmi Note 11/ Pro|light|Good|
|Redmi Note 11/ Pro|miel|Good|
|Redmi Note 11/ Pro|fleur|Good|
|Redmi Note 11/ Pro|secret|Good|
|Redmi Note 11/ Pro|opal|Good|
|Redmi Note 11/ Pro|pissarro|Good|
|Redmi Note 11/ Pro|viva|Good|
|Redmi Note 11/ Pro|vida|Good|
|Redmi Note 11/ Pro|peux|Good|
|Redmi Note 11/ Pro|pissarropro|Good|
|Redmi Note 11/ Pro|xaga|Good|
|Redmi Note 11/ Pro|xagapro|Good|
|Redmi Note 12/ Pro|tapas|Good|
|Redmi Note 12/ Pro|topaz|Good|
|Redmi Note 12/ Pro|sunstone|Good|
|Redmi Note 12/ Pro|sky|Good|
|Redmi Note 12/ Pro|ocean|Good|
|Redmi Note 12/ Pro|sea|Good|
|Redmi Note 12/ Pro|sweet|Good|
|Redmi Note 12/ Pro|ruby|Good|
|Redmi Note 12/ Pro|rubypro|Good|
|Redmi Note 12/ Pro|rubyplus|Good|
|Redmi Note 12/ Pro|redwood|Good|
|Redmi Note 12/ Pro|pearl|Good|
|Redmi Note 12R|sky|Good|
|Redmi Note 12R|river|Good|
|Redmi Note 12C|earth|Good|
|Redmi Note 11/ Pro|veux|Good|
|Black Shark 3 / 3s|klein|Good|
|Black Shark 3 Pro|mobius|Good|
|Xiaomi Black Shark 5 Pro / 5Rs|katyusha|Good|
|Xiaomi Black Shark 5 Pro / 5Rs|kaiser|Good|
|Xiaomi Black Shark 5|patriot|Good|
|Xiaomi Black Shark 2 Pro|darklighter|Good|
|Xiaomi Black Shark 2|skywalker|Good|
|Xiaomi Black Shark Helo / Shark 1s|bullhead|Good|
|Xiaomi Black Shark|shark|Good|
|Xiaomi Black Shark 4 Pro / 4s Pro|penrose|Good|
|Xiaomi Black Shark 4 / 4|kaiser|Good|
|xiaomi MI 6|sagit|Bad|
|xiaomi note2|scorpio|Bad|
|xiaomi Max2|oxygen|Bad|
|xiaomi mix|lithium|Bad|
|xiaomi note3|jason|Limited|
|xiaomi MIX 2|chiron|Bad|
|xiaomi MIX FLIP||Good|
|Mi 5C|meri|Limited|
|Mi 5X /Xiaomi Mi A1|tiffany|Limited|
|xiaomi Max|helium|Bad|
|xiaomi redmi Note 5 /Note 5 pro|whyred|Bad|
|xiaomi Redmi Y1 / Note 5A|ugg|Bad|
|xiaomi redmi 5Plus|vince|Bad|
|xiaomi redmi 5|rosy|Bad|
|REDMI 6 PRO|sakura\_india|Limited|
|REDMI 6 PRO|sakura|Limited|
|Mi A3|laurel\_sprout|Limited|
|Mi 6X|wayne|Limited|
|Mi A2|jasmine\_sprout|Limited|
|Mi A2 lite|daisy\_sprout|Limited|
|Mi Pad 4 /4 plus|clover|Limited|
|Mi Max 3|nitrogen|Bad|
|xiaomi redmi note 4|mido|Bad|
|xiaomi redmi note 4|nikel|Bad|
|Xiaomi Redmi 4X|santoni|Bad|
|Xiaomi Redmi 4|prada|Bad|
|Xiaomi Redmi 4 Pro|markw|Bad|
|Mi 5s|capricorn|Bad|
|Mi 5s plus|natrium|Bad|
|xiaomi POCO F1|beryllium|Good|
|xiaomi MI 8|dipper|Good|
|xiaomi MIX 3 5G|andromeda|Good|
|xiaomi MIX 3|perseus|Good|
|xiaomi MIX 2S|polaris|Good|
|xiaomi MI 8 SE|sirius|Good|
|xiaomi MI 8 lite|platina|Good|
|xiaomi MI 8 Explorer Edition|ursa|Good|
|xiaomi MI 8 Pro / MI 8 UD|equuleus|Good|
|oneplus 7pro|OnePlus7Pro|Good|
|oneplus 7pro|OP7ProNRSpr|Good|
|oneplus 7pro|OnePlus7ProTMO|Good|
|oneplus 7pro 5G|OnePlus7ProNR|Good|
|oneplus 7|OnePlus7|Good|
|OnePlus Z|OnePlusZ|Good|
|OnePlus Z|OnePlusNord|Good|
|oneplus 7T|OnePlus7T|Good|
|oneplus 7T|OnePlus7TTMO|Good|
|oneplus 7T Pro|OnePlus7TPro|Good|
|oneplus 7T Pro 5G|OnePlus7TProNR|Good|
|oneplus 8|OnePlus8|Good|
|oneplus 8T 5G|OnePlus8TMO|Good|
|oneplus 8T 5G|OnePlus8VZW|Good|
|OnePlus 8 Pro|OnePlus8Pro|Good|
|OnePlus 8 Pro|OnePlus8ProNR|Good|
|OnePlus Nord|Nord|Good|
|OnePlus Nord CE|OnePlusNordCE|Good|
|OnePlus Nord CE 2|OnePlusNordCE2|Good|
|OnePlus Nord CE 3||Good|
|OnePlus Nord CE 3 Lite||Good|
|OnePlus Nord CE 4||Good|
|OnePlus Nord CE 4 Lite||Good|
|OnePlus Nord CE 5||Good|
|OnePlus Nord 5||Good|
|OnePlus Nord N200|OnePlusN200|Good|
|OnePlus Nord N200|OnePlusN200TMO|Good|
|OnePlus Nord 2T|OP557AL1|Good|
|OnePlus Nord 2|OP515BL1|Good|
|OnePlus Nord N10 5G|OnePlusN10|Good|
|OnePlus Nord N10 5G|OnePlusN10METRO|Good|
|OnePlus Nord N10 5G|OnePlusN10TMO|Good|
|OnePlus Nord N100|OnePlusN100|Good|
|OnePlus Nord N100|OnePlusN100METRO|Good|
|OnePlus Nord N100|OnePlusN100TMO|Good|
|OnePlus 8T|OnePlus8T|Good|
|OnePlus 8T+ 5G|OnePlus8TTMO|Good|
|OnePlus 9 Pro|OnePlus9Pro|Good|
|OnePlus 9 Pro|OnePlus9ProTMO|Good|
|OnePlus 9|OnePlus9|Good|
|OnePlus 9|OnePlus9TMO|Good|
|OnePlus 9R|OnePlus9R|Good|
|OnePlus 9RT|OnePlus9RT|Good|
|OnePlus 9RT|OP5154L1|Good|
|OnePlus 9RT|OP5155L1|Good|
|OnePlus 10 Pro|OP516FL1|Good|
|OnePlus 10 Pro|OP516EL1|Good|
|OnePlus 10R / Ace|OP5566L1|Good|
|OnePlus 10R / Ace|OP5565|Good|
|OnePlus 11|OP591BL1|Good|
|OnePlus 11|CPH2447|Good|
|OnePlus 11|CPH2449|Good|
|OnePlus 11|CPH2451|Good|
|OnePlus 12|PJD110|Good|
|OnePlus 12|CPH2573|Good|
|OnePlus 12|CPH2581|Good|
|OnePlus 12|CPH2583|Good|
|OnePlus 13|CPH2649|Limited|
|OnePlus 13|CPH2653|Limited|
|OnePlus 13|CPH2655|Limited|
|OnePlus 13R|CPH2645|Limited|
|OnePlus 13R|CPH2647|Limited|
|OnePlus 13R|CPH2691|Limited|
|OnePlus 13T|CPH2723|Limited|
|OnePlus Open|CPH2551|Limited|
|OnePlus Ace 3|PJE110|Good|
|OnePlus Ace 3|CPH2585|Good|
|OnePlus Ace 3|CPH2609|Good|
|OnePlus Ace 3|CPH2611|Good|
|OnePlus Ace 3|OP5CF9L1|Good|
|OnePlus Ace 5|PKG110|Good|
|OnePlus Ace 5|PLC110|Good|
|OnePlus Ace 5 Pro|PKR110|Good|
|OnePlus Ace 3V|PJF110|Good|
|OnePlus Ace 3 Pro|PJX110|Good|
|OnePlus Ace 2, 11R|PHK110|Good|
|OnePlus Ace 2, 11R|CPH2487|Good|
|OnePlus Ace 2, 11R|PHP110|Good|
|OnePlus Ace 2, 11R|OP5927|Good|
|OnePlus Ace 2 Pro|PJA110|Good|
|OnePlus Ace Racing|OP5911|Good|
|OnePlus Ace Pro|OP5551L1|Good|
|OnePlus Ace Pro|PGP110|Good|
|OnePlus|OnePlus3T|Good|
|OnePlus|OnePlus5T|Good|
|OnePlus|OnePlus5|Good|
|OnePlus|OnePlus6TSingle|Good|
|OnePlus|OnePlus6T|Good|
|OnePlus|OnePlus6|Good|
|sony Xperia XZ1|701SO|Good|
|sony Xperia XZ1|G8341|Good|
|sony Xperia XZ1|G8342|Good|
|sony Xperia XZ1|G8343|Good|
|sony Xperia XZ1|SO-01K|Good|
|sony Xperia XZ1|SOV36|Good|
|sony Xperia XZ1C|G8441|Good|
|sony Xperia 1|802SO|Good|
|sony Xperia 1|J8110|Good|
|sony Xperia 1|J8170|Good|
|sony Xperia 1|J9110|Good|
|sony Xperia 1|J9180|Good|
|sony Xperia 1|SO-03L|Good|
|sony Xperia 1|SOV40|Good|
|sony Xperia 1 II|SO-51A|Good|
|sony Xperia 1 II|SOG01|Good|
|sony Xperia 1 II|XQ-AT51|Good|
|sony Xperia 1 II|XQ-AT52|Good|
|sony Xperia 1 II|XQ-AT72|Good|
|sony Xperia 1 III||Good|
|sony Xperia 1 IV|A201SO|Good|
|sony Xperia 1 IV|SO-51C|Good|
|sony Xperia 1 IV|SOG06|Good|
|sony Xperia 1 IV|XQ-CT54|Good|
|sony Xperia 1 IV|XQ-CT72|Good|
|sony Xperia 1 V|XQ-DQ72|Good|
|sony Xperia 1 VI|XQ-EC72|Good|
|sony Xperia XZ Premium|G8141|Good|
|sony Xperia XZ Premium|G8142|Good|
|sony Xperia XZ Premium|G8188|Good|
|sony Xperia XZ Premium|SO-04J|Good|
|sony Xperia XZ1 Compact|G8441|Good|
|sony Xperia XZ1 Compact|SO-02K|Good|
|sony Xperia 5|901SO|Good|
|sony Xperia 5|J8210|Good|
|sony Xperia 5|J8270|Good|
|sony Xperia 5|J9210|Good|
|sony Xperia 5|SO-01M|Good|
|sony Xperia 5|SOV41|Good|
|sony Xperia 5 V|XQ-DE72|Good|
|sony Xperia 5 II|A002SO|Good|
|sony Xperia 5 II|SOG02|Good|
|sony Xperia 5 II|XQ-AS52|Good|
|sony Xperia 5 II|XQ-AS72|Good|
|sony Xperia 5 III||Good|
|sony Xperia 10 plus|I3213|Good|
|sony Xperia 10 plus|I3223|Good|
|sony Xperia 10 plus|I4213|Good|
|sony Xperia 10 plus|I4293|Good|
|sony Xperia 10|I3113|Good|
|sony Xperia 10|I3123|Good|
|sony Xperia 10|I4113|Good|
|sony Xperia 10|I4193|Good|
|sony Xperia 10 II|A001SO|Good|
|sony Xperia 10 II|SO-41A|Good|
|sony Xperia 10 II|SOV43|Good|
|sony Xperia 10 II|XQ-AU42|Good|
|sony Xperia 10 II|XQ-AU51|Good|
|sony Xperia 10 II|XQ-AU52|Good|
|sony Xperia 10 III|SO-52B|Good|
|sony Xperia 10 III|SOG04|Good|
|sony Xperia 10 IV|SO-52B|Good|
|sony Xperia 10 IV|SOG04|Good|
|sony Xperia 10 V|XQ-DC72|Good|
|sony Xperia 10 VI|XQ-ES72|Good|
|sony Xperia Pro|XQ-AQ52|Good|
|sony Xperia Pro|XQ-AQ62|Good|
|sony Xperia Pro|MK16a|Good|
|sony Xperia Pro-I|XQ-BE42|Good|
|sony Xperia Pro-I|XQ-BE52|Good|
|sony Xperia Pro-I|XQ-BE62|Good|
|sony Xperia Pro-I|XQ-BE72|Good|
|Xperia XZ3|801SO|Good|
|Xperia XZ3|H8416|Good|
|Xperia XZ3|H9493|Good|
|Xperia XZ3|SO-01L|Good|
|Xperia XZ3|SOV39|Good|
|Xperia XZ3|akatsuki|Good|
|Xperia XZ2|702SO|Good|
|Xperia XZ2|H8216|Good|
|Xperia XZ2|H8266|Good|
|Xperia XZ2|H8276|Good|
|Xperia XZ2|H8296|Good|
|Xperia XZ2|SOV37|Good|
|Xperia XZ2|SO-03K|Good|
|Xperia XZ2 Premium|H8116|Good|
|Xperia XZ2 Premium|H8166|Good|
|Xperia XZ2 Premium|SO-04K|Good|
|Xperia XZ2 Premium|SOV38|Good|
|Xperia XZ2 Compact|H8314|Good|
|Xperia XZ2 Compact|H8324|Good|
|Xperia XZ2 Compact|SO-05K|Good|
|Asus ROG Phone ll|ASUS\_I001\_1|Good|
|Asus ROG Phone 3|ASUS\_I003\_1|Good|
|Asus ROG Phone 3|ASUS\_I003|Good|
|Asus ROG Phone|ASUS\_Z01QD\_1|Good|
|Asus ROG Phone 5 / 5 Pro|ASUS\_I005\_1|Good|
|Asus ROG Phone 5s / 5s Pro|ASUS\_I005\_1|Good|
|Asus ZenFone 6|ASUS\_T00G|Good|
|Asus ZenFone 6|ASUS\_Z002|Good|
|Asus ZenFone 6|ASUS\_I01WD|Good|
|Asus ZenFone 7 / 7 Pro|ASUS\_I002D|Good|
|Asus ZenFone 8 Flip|ASUS\_I004D|Good|
|Asus ZenFone 8/ ASUS 8Z|ASUS\_I006D|Good|
|Asus ZenFone 5z|ASUS\_Z01R\_1|Good|
|Asus ZenFone 5 Lite|ASUS\_X017D\_1|Good|
|Asus ZenFone 5 Lite|ASUS\_X017D\_2|Good|
|Asus ZenFone 5|ASUS\_X00QD|Good|
|Asus ZenFone 5|ASUS\_T00K|Good|
|Asus ZenFone 5|ASUS\_T00J1|Good|
|Asus ZenFone 5|ASUS\_T00F1|Good|
|Asus ZenFone 5|ASUS\_T00F|Good|
|Asus Zenfone 3s Max ZC521TL|ASUS\_X00G\_1|Good|
|Asus ZenFone 4|ASUS\_T00I|Good|
|Asus ZenFone 4|ASUS\_Z01KDA|Good|
|Asus ZenFone 4|ASUS\_T00Q|Good|
|Asus ZenFone 4|ASUS\_Z01KD\_1|Good|
|Asus ZenFone 4|ASUS\_Z01KD\_2|Good|
|Asus ZenFone 4|ASUS\_Z01KD\_3|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_1|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_2|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_4|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_5|Good|
|Asus ZenFone 4 Max|ASUS\_X00ID|Good|
|Asus ZenFone 4 Max|ASUS\_X00IDB|Good|
|Asus ZenFone 4 Max|ASUS\_X00IDC|Good|
|Asus Zenfone 4 Pro|ASUS\_Z01GD\_1|Good|
|Asus Zenfone 4 Pro|ASUS\_Z01GD\_1|Good|
|Asus Zenfone 4 Selfie|ASUS\_X00LD\_1|Good|
|Asus Zenfone 4 Selfie Lite|ASUS\_X00HD\_3|Good|
|Asus Zenfone 4 Selfie Pro|ASUS\_Z01M\_1|Good|
|Asus ZenFone Max M2|ASUS\_X01A\_1|Good|
|Asus ZenFone Max Pro M2|ASUS\_X01BD\_2|Good|
|Asus ZenFone Max Pro M2|ASUS\_X01BD\_1|Good|
|Asus ZenFone Max Plus M2 /Zenfone Max Shot|ASUS\_A001D\_1|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_1|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_2|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_3|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_5|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_6|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_7|Good|
|Asus ZenFone AR|ASUS\_A002\_1|Good|
|Asus ZenFone AR|ASUS\_A002|Good|
|Asus ZenFone Ares|ASUS\_A002\_2|Good|
|Asus ROG Phone|ASUS\_Z01QD\_1|Good|
|Lenovo Z6 Pro 5G|cream|Good|
|Lenovo Z6 Pro / Z6|zippo|Good|
|Lenovo Y90||Good|
|Lenovo Legion 2 Pro / Legion Duel 2||Good|
|Lenovo Legion Pro /Lenovo Legion Phone Duel|moba|Good|
|Lenovo Tab P11|J606F|Good|
|Lenovo Tab P11|J606L|Good|
|Lenovo Tab P11 Plus|TB-J616F|Good|
|Lenovo Tab P11 Plus|TB-J616X|Good|
|Lenovo Tab P11 Pro|J706F|Good|
|Lenovo Tab P11 Pro|J706L|Good|
|Lenovo Tab P11 5G|J607Z|Good|
|Lenovo Tab P12 Pro|Q706F|Good|
|Lenovo Tab P12 Pro|Q706Z|Good|
|Lenovo Tab 11|YT-J706X|Good|
|Lenovo Yoga Tab 13|K606F|Good|
|Lenovo Yoga Tab 11|YT-J706F|Good|
|Lenovo Yoga Tab 11|YT-J706X|Good|
|Lenovo Pad Pro||Good|
|Lenovo Pad Plus||Good|
|Lenovo Pad||Good|
|Lenovo Legion Y700|TB-9707F|Good|
|Lenovo K10|X6C6F|Good|
|Lenovo K10|X6C6L|Good|
|Lenovo K10|X6C6X|Good|
|Lenovo K10|X6C6NBF|Good|
|Lenovo K10|X6C6NBL|Good|
|Lenovo K10|X6C6NBX|Good|
|Lenovo K13 Note|capri|Good|
|Lenovo K13 Pro|caprip|Good|
|Lenovo Y70|halo|Good|
|Lenovo Tab M10 FHD Plus|X606F|Bad|
|Lenovo Tab M10 FHD Plus|X606M|Bad|
|Lenovo Tab M10 FHD Plus|X606X|Bad|
|Lenovo Tab M10 FHD Plus|X616F|Bad|
|Lenovo Tab M10 FHD Plus|X616M|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306FC\_PRC|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306NC\_PRC|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306V|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306X|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306XA|Bad|
|Lenovo Tab M10 Plus 3rd Gen|TB125FU|Bad|
|Lenovo Tab M10 Plus 3rd Gen|X606X|Bad|
|Lenovo Tab M10 Plus 3rd Gen|X616F|Bad|
|Lenovo Tab M10 Plus 3rd Gen|X616M|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306F|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306FA|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306V|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306X|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306XA|Bad|
|Lenovo Tab M10 5G|TB-X607Z|Bad|
|Lenovo Tab M10 Plus|X606V|Bad|
|Lenovo Z5s|jd2019|Good|
|Lenovo Z5 Pro|zap|Good|
|Lenovo Z5 Pro|heart|Good|
|Lenovo A6 Note|Lenovo\_A6\_Note|Good|
|Lenovo S5 Pro|sprout|Good|
|Nokia 8 Sirocco|A1N|Good|
|Nokia 8 Sirocco|A1N\_sprout|Good|
|Nokia 8.3 5G||Good|
|Nokia 8 V 5G UW|RAV\_VZW|Good|
|Nokia 3.4||Good|
|Nokia X20||Good|
|Nokia X10||Good|
|Nokia G20||Good|
|Nokia XR20|TTG|Good|
|Nokia XR20|TTG\_sprout|Good|
|Nokia G50|PHR|Good|
|Nokia G50|PHR\_sprout|Good|
|Nokia X100|TTG|Good|
|Nokia 9|AOP\_sprout|Good|
|Nokia 9|AOP|Good|
|Nokia 7.1|CTL\_sprout|Good|
|Nokia 7.2|DDVA\_sprout|Good|
|Nokia 7.2|DDV\_sprout|Good|
|Nokia 3.1C /Nokia 3.1A|EAG|Good|
|Nokia 7 plus|B2N|Good|
|Nokia 7 plus|B2N\_sprout|Good|
|Nokia 5.1 plus / Nokia X5|PDA|Good|
|Nokia 5.4||Good|
|Nokia 6.1 plus / Nokia X6|DRG|Good|
|Nokia 6.1 plus / Nokia X6|DRG\_sprout|Good|
|Nokia 6.1|PL2|Good|
|Nokia 6.1|PL2\_sprout|Good|
|Nokia 6.2|SLDA\_sprout|Good|
|Nokia 6.2|SLD\_sprout|Good|
|Nokia X71|TAS|Good|
|Nokia 8|NB1|Good|
|Nokia 8.1 / Nokia X7|PNX\_sprout|Good|
|Nokia 8.1 / Nokia X7|PNXN|Good|
|Nokia 8.1 / Nokia X7|PNX|Good|
|Moto g(6)|ali|Good|
|Moto g(6)|ali\_n|Good|
|moto g7|river|Good|
|moto g7|river\_n|Good|
|moto g7 optimo maxx|ocean|Good|
|moto g(7) play|channel|Good|
|moto g(7) plus|lake|Good|
|moto g(7) plus|lake\_n|Good|
|moto g(7) power|ocean\_n|Good|
|moto g(8) play|lima|Good|
|moto g(8) plus|doha|Good|
|moto g(8) plus|doha\_n|Good|
|moto g(8) power|sofiar|Good|
|moto g(8) power lite|blackjack|Good|
|moto g Stylus|sofiap|Good|
|moto g power|sofia|Good|
|Moto One Hyper|def|Good|
|Moto One Macro|lima|Good|
|Moto One Zoom|parker|Good|
|Moto One Action|troika|Good|
|Moto One Action|troika\_sprout|Good|
|Moto One Vision / P50|kane\_sprout|Good|
|Moto One / P30 Play|deen\_sprout|Good|
|Moto One Power/ P30 Note|chef\_sprout|Good|
|Moto z3 play|beckham|Good|
|Moto z4|foles|Good|
|Moto P50|kane|Good|
|Moto Edge|racer|Good|
|Moto G60s|lisbon|Good|
|Moto G82|rhodep|Good|
|Moto Edge 20|berlin|Good|
|Moto Edge 20 lite|kyoto|Good|
|Moto Edge 20 Pro|pstar|Good|
|Moto Edge 30|dubai|Good|
|Moto Edge 30 Pro|hiphi|Good|
|Moto Edge plus|burton|Good|
|Moto G pro|sofiap\_sprout|Good|
|Moto G fast|rav|Good|
|Moto One Vision plus|doha\_n|Good|
|Moto One fusion+|liber|Good|
|Moto One fusion|astro|Good|
|moto g 5G plus /motorola one 5G /motorola one 5G UW|nairo|Good|
|moto g 5G|kiev|Good|
|moto g9 / moto g(9) play|guamp|Good|
|moto g9 plus|odessa|Good|
|moto razr|olson|Good|
|moto razr 5G/moto razr 2020|smith|Good|
|Moto one|deen\_sprout|Good|
|Moto one|deen\_sprout\_n|Good|
|Moto one 5G Ace|kiev|Good|
|Moto one 5G / 5G UW|nairo|Good|
|Moto one 5G UW Ace|kievv|Good|
|Moto Defy 2021|umts\_jordan|Good|
|Moto Defy 2021|bathena|Good|
|Moto Defy Pro|XT560|Good|
|moto G Stylus (2021)|minsk|Good|
|moto G Stylus (2022)|tonga|Good|
|moto G Stylus 5G|denver|Good|
|moto G power (2021)|borneo|Good|
|moto Edge X30|hiphic|Good|
|moto Edge S /G100|nio|Good|
|moto Edge(2021)|berlna|Good|
|moto G200 5G / edge S30|xpeng|Good|
|moto G100|nio|Good|
|moto G71|corfur|Good|
|moto G50 5G|saipan|Good|
|moto G51 /G51 5G|cypfq|Good|
|moto G50|ibiza|Good|
|moto G60|hanoip|Good|
|moto G40 Fusion|hanoip|Good|
|moto G41|corfu|Good|
|moto G31|coful|Good|
|moto G30|caprip|Good|
|moto G20|java|Good|
|moto G22|hawaiip|Good|
|moto G10 / G10 power|capri|Good|
|moto E7 Power|malta|Good|
|moto Tab G70|mototabg70|Good|
|moto Tab G70|mototabg70LTE|Good|
|Moto g(6) plus|evert|Good|
|Moto g(6) plus|evert\_n|Good|
|Moto g(6) plus|evert\_nt|Good|
|Moto Z(3)|messi|Good|
|Moto Z2 Force|nash|Good|
|Moto X4|payton|Good|
|Moto X4|payton\_sprout|Good|
|Moto G5S Plus|sanders|Good|
|Moto G5S Plus|sanders\_n|Good|
|Moto G5S Plus|sanders\_nt|Good|
|LG V50S ThinQ / G8X ThinQ|mh2lm|Good|
|LG W30 Pro|Neo4LM|Good|
|LG W30|LM-X440ZMW|Good|
|LG W30|LM-X440ZM|Good|
|LG W30|LM-X440IM|Good|
|LG W10|LMX130IM|Good|
|LG W10 Alpha|Neo2ALP|Good|
|LG V50 ThinQ|flashlm|Good|
|LG V50 ThinQ|flashlmdd|Good|
|LG VELVET|caymanslm|Good|
|LG VELVET|mcaymanlm|Good|
|LG Q61|mdh40lm|Good|
|LG Q92|acelm|Good|
|LG WING|winglm|Good|
|LG VELVET / LG Velvet 5G UW|caymanlm|Good|
|LG V60S ThinQ 5G / V60S ThinQ 5G UW|timelm|Good|
|LG G8S ThinQ / G8S|betalm|Good|
|LG G8X ThinQ|mh2lm|Good|
|LG G8 ThinQ / G8|alphaamz|Good|
|LG G8 ThinQ / G8|alphalm|Good|
|LG G8 ThinQ / G8|alphaplus|Good|
|LG Q9 /G7 Fit|falcon|Good|
|LG K61|mdh40lm|Good|
|LG V40 ThinQ|judypn|Good|
|LG G7 one|phoenix\_sprout|Good|
|LG Q8 (2018)|anna|Good|
|LG Q8 (2018)|cv7an|Good|
|Meizu 15|M15|Bad|
|Meizu 15|MX15|Bad|
|Meizu 15|15|Bad|
|Meizu 15 Plus|15PLus|Bad|
|Meizu 15 Lite|15Lite|Bad|
|Meizu 16 PLus|16PLus|Bad|
|Meizu 16 PLus|16|Bad|
|Meizu 16X|16X|Bad|
|Meizu 18|m2181|Good|
|Meizu note 8|meizunote8|Good|
|Meizu note 8|M1822|Good|
|Meizu M8|MeizuM8|Good|
|Meizu M8lite|M8lite|Good|
|Meizu 20|m2381|Good|
|Meizu 20|M381Q|Good|
|Meizu 20|meizu20|Good|
|Meizu 20 Pro|m2391|Good|
|Meizu 20 Pro|M391Q|Good|
|Meizu 20 Pro|meizu20Pro|Good|
|Meizu 21 Pro|m2481|Good|
|Meizu pro6s / pro6|PRO6|Bad|
|Meizu M6|meizu\_M6|Bad|
|Meizu M6 Note|M6Note|Bad|
|Meizu M6T|MeizuM6T|Bad|
|Meizu M6s|MeizuM6s|Bad|
|Meizu M6s|MeizumbluS6|Bad|
|Meizu Pro 6 plus|PRO6Plus|Bad|
|Meizu U20|U20|Bad|
|Meizu U20|MeizuU20|Bad|
|Meizu S6|MeizuS6|Bad|
|Meizu Pro 7|PRO7S|Bad|
|Meizu Pro 7|PRO7H|Bad|
|Meizu Pro 7 plus|PRO7Plus|Bad|
|Meizu Pro 7 plus|PRO7S|Bad|
|Meizu MX16|MX16|Good|
|Meizu 16T|meizu16T|Good|
|Meizu 16s pro|meizu16sPro|Good|
|Meizu 16s pro|16s|Good|
|Meizu 16Xs|16Xs|Good|
|Meizu 16Xs|meizu16Xs|Good|
|Meizu 17|meizu17|Good|
|Meizu 17 Pro|meizu17Pro|Good|
|Meizu 18|meizu18|Good|
|Meizu 18 Pro|meizu18Pro|Good|
|Meizu 18x|meizu18X|Good|
|Meizu 18s|meizu18s|Good|
|Meizu 18s Pro|meizu18sPro|Good|
|Meizu note9|meizunote9|Good|
|Meizu note9|Note9|Good|
|Meizu note9|meizuZero|Good|
|Meizu 16th|16th|Limited|
|Meizu 16th Plus|16thPlus|Limited|
|Meitu M8s|MayaS|Good|
|Meitu T9|Melody|Good|
|Meitu T9|Tiffany|Good|
|Meitu V6|Vivian|Good|
|Meitu T8s|VictoriaS|Good|
|Meitu T8|Victoria|Bad|
|Meitu M8|Maya|Bad|
|Smartisan N3|oscar|Bad|
|Smartisan R1|trident|Bad|
|Smartisan Pro 2S|ocean|Bad|
|Smartisan nut pro|odin|Bad|
|Smartisan pro 2|oxford|Bad|
|Smartisan pro 2|osborn|Bad|
|Smartisan Pro 3|delta|Good|
|Smartisan M1|surabaya|Bad|
|Smartisan M1L|colombo|Bad|
|le 2 X528|le\_s2\_cm|Bad|
|le S3|le\_s2\_na|Bad|
|le Pro3|le\_zl1|Bad|
|MAGNEO|MAGNEO|Bad|
|LGE G6|lucye|Good|
|LGE Q6|mh|Limited|
|LGE Q6|mhn|Limited|
|LGE Q6|flame|Good|
|Google Pixel 4 XL|coral|Good|
|Google Pixel 4a|sunfish|Good|
|Google Pixel 4a(5G)|bramble|Good|
|Google Pixel 5|redfin|Good|
|Google Pixel 5a 5G|barbet|Good|
|Google Pixel 6|oriole|Good|
|Google Pixel 6 Pro|raven|Good|
|Google Pixel 6a|bluejay|Good|
|Google Pixel 9|tokay|Good|
|Google Pixel 9 Pro|caiman|Good|
|Google Pixel 9 Pro Large|komodo|Good|
|Google Pixel 9 fold|comet|Good|
|Google Pixel 9a|tegu|Good|
|Pixel Fold|passport|Good|
|Wiko View 3 Pro|W-P611|Good|
|Wiko View 3|W-P311|Good|
|Wiko Y80|W-V720|Good|
|Stylo 5|cv7as|Good|
|Google Pixel|sailfish|Good|
|Google Pixel XL|marlin|Good|
|Infinix note 6|Infinix-X610|Good|
|Infinix note 7|Infinix-X690|Good|
|Infinix note 7|Infinix-X690B|Good|
|Infinix note 7|Infinix-X690C|Good|
|Infinix SMART 5|Infinix-X657|Good|
|Infinix SMART 5|Infinix-X657B|Good|
|Infinix SMART 5|Infinix-X657C|Good|
|Infinix SMART 5|Infinix-X688C|Good|
|Infinix note 10 pro|Infinix-X695|Good|
|Infinix note 10 pro|Infinix-X695D|Good|
|Infinix note 10 pro NFC|Infinix-X695C|Good|
|Infinix note 11s|Infinix-X698|Good|
|Infinix note 11 Pro|Infinix-X697|Good|
|Infinix note 11|Infinix-X663B|Good|
|Infinix note 11i|Infinix-X693|Good|
|Infinix note 12|Infinix-X670|Good|
|Infinix note 12|Infinix-X672|Good|
|Infinix note 12|Infinix-X663C|Good|
|Infinix note 12|Infinix-X663D|Good|
|Infinix note 12i|Infinix-X6819|Good|
|Infinix note 8|Infinix-X692|Good|
|Infinix Hot 10|Infinix-X682B|Good|
|Infinix Hot 10|Infinix-X682C|Good|
|Infinix zero 8|Infinix-X687|Good|
|Infinix zero 8i|Infinix-X687B|Good|
|Infinix S5|Infinix-X652|Good|
|Infinix S5|Infinix-X652A|Good|
|Infinix S5 pro|Infinix-X660|Good|
|Infinix HOT 9 Pro|Infinix-X655F|Good|
|Infinix S4|Infinix-X626|Good|
|Infinix S4|Infinix-X626B|Good|
|Infinix S4|Infinix-X626B-LTE|Good|
|Infinix zero 5G|Infinix-X6815|Good|
|Kyocera TORQUE G04|KYV46|Good|
|Kyocera GRATINA|KYV48|Good|
|Fujitsu F-51A / ARROWS 5G|F51A|Good|
|Fujitsu F-52A|F52A|Good|
|LitByLeia Lume Pad|LPD10-11|Good|
|LitByLeia Lume Pad|LPD10-10W|Good|
|LitByLeia Lume Pad|LPD10-11W|Good|
|Zebra ET51S|ET51S|Good|
|Zebra ET56S|ET56S|Good|
|Zebra TC52|TC52|Good|
|Zebra TC52X|TC52X|Good|
|Zebra TC57|TC57|Good|
|Zebra TC57X|TC57X|Good|
|Zebra TC72|TC72|Good|
|Zebra TC77|TC77|Good|
|Zebra TC26|TC26|Good|
|Zebra TC21|TC21|Good|
|Zebra EC50|EC50|Good|
|Zebra EC55|EC55|Good|
|Zebra TC8000|TC8000|Good|
|Sharp Aquos R3|SG808SH|Good|
|Sharp Aquos R3|SH-04L|Good|
|Sharp Aquos R3|SH-R10|Good|
|Sharp Aquos R3|NAX|Good|
|Sharp AQUOS R5G|SH-51A|Good|
|Sharp AQUOS R5G|SG908SH|Good|
|Sharp AQUOS R5G|Banagher|Good|
|Sharp sense3|PCZ-u|Good|
|Sharp sense3|SH-M12|Good|
|Sharp sense3|SH-02M|Good|
|Sharp sense3|PCZ|Good|
|Sharp sense3 basic|SG907SH|Good|
|Sharp sense3 basic|VIF|Good|
|Sharp sense3 plus|OBY|Good|
|Sharp sense3 plus|SH-RM11|Good|
|Sharp sense3 plus|SH-M11|Good|
|Sharp sense3 plus|SG901SH|Good|
|Sharp Aquos V|VGO|Good|
|Sharp AquosR2 compact|SH-M09|Good|
|Sharp AquosR2 compact|SG803SH|Good|
|Sharp Aquos S7|vespa\_sprout|Good|
|Sharp Aquos V|VGO|Good|
|Sharp Aquos zero5G basic / Aquos zero5G basic DX|SGA002SH|Good|
|Sharp Aquos zero5G basic / Aquos zero5G basic DX|OJ6|Good|
|Sharp Aquos zero2|SG906SH|Good|
|Sharp Aquos zero2|SH-01M|Good|
|Sharp Aquos zero2|SH-M13|Good|
|Sharp Aquos zero2|SH-Z20|Good|
|Sharp Aquos zero2|QDA|Good|
|Sharp Aquos zero|SG801SH|Good|
|Sharp Aquos zero|SH-Z10|Good|
|Sharp Aquos zero|SH-Z10A|Good|
|Sharp Aquos zero|SH-M10|Good|
|Tecno Camon 18i|TECNO-CG6|Good|
|Tecno Camon 18 Premier|TECNO-CH9|Good|
|Tecno Camon 18 Premier|TECNO-CH9n|Good|
|TECNO CAMON 18 P|TECNO-CH7|Good|
|TECNO CAMON 18 P|TECNO-CH7n|Good|
|TECNO CAMON 17 Pro|TECNO-CG8|Good|
|TECNO CAMON 17 Pro|TECNO-CG8h|Good|
|TECNO CAMON 16 Pro|TECNO-CE8|Good|
|TECNO CAMON 16 Premier|TECNO-CE8|Good|
|TECNO Camon 12 Pro|TECNO-CC9|Good|
|TECNO Phantom 9|TECNO-AB7|Good|
|TECNO Phantom X|TECNO-AC8|Good|
|TECNO POVA 2 not stable|TECNO-LE7|Good|
|TECNO POVA 2 not stable|TECNO-LE7n|Good|
|TECNO POVA 5G not stable|TECNO-LE8|Good|
|Umx(Ultimate Mobile Experience)|U3AR|Good|
|General Mobile GM 9 Plus|GM9PLUS\_s|Good|
|HTC Desire 21 Pro 5G|htc\_thudugl|Good|
|HTC Desire 20+|htc\_srcdugl|Good|
|HTC U20 5G|htc\_flhdugl|Good|
|HTC Desire 20 Pro|htc\_bymdugl|Good|
|TCL 10 5G UW|Seattle\_VZW|Good|
|TCL 10 5G|Seattle|Good|
|TCL 10 Plus|Boston|Good|
|TCL 10 Pro|T1\_PRO|Good|
|TCL 10 SE|Oakland|Good|
|TCL 10L|T1\_LITE|Good|
|TCL 10L|T1\_LITE|Good|
|TCL 20 5G|Irvine|Good|
|TCL 20 pro 5G|Ottawa|Good|
|TCL 20L|Richland|Good|
|TCL 20L+|Richland\_Pro|Good|
|TCL FFALCON FF1||Good|
|Vsmart live 4|cassia|Good|
|Vsmart Aris Pro|jacarandapro|Good|
|RED HydrogenONE|HydrogenONE|Good|
|Nexus 6P|angler|Good|
|Google Pixel 3|blueline|Good|
|Google Pixel 3a XL|bonito|Good|
|Google Pixel 3 XL|crosshatch|Good|
|Borqs Falcon|falcon|Good|
|Google Pixel 3a|sargo|Good|
|Google Pixel 2 XL|taimen|Good|
|Google Pixel 2|walleye|Good|
|BQ Aquaris X2|zangya\_sprout|Good|
|BQ Aquaris X2 Pro|zangyapro\_sprout|Good|
|glass kuak|bengal|Good|
|glass kuak|bengal\_global|Good|
|glass kuak|pluto|Good|
|glass kuak|pluto\_global|Good|

---

## 运动跟踪支持的设备
- 章节路径: `motion-tracking/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices.html

# 运动跟踪支持的设备
如果一个设备（手机、眼镜或头显）通过硬件或软件方案具有真实尺度的六自由度运动跟踪能力，我们称其为运动跟踪设备。这些设备包括但不限于可以运行 EasyAR 运动跟踪、 ARCore/ ARKit、华为 AR Engine 的设备，或具有六自由度跟踪能力的眼镜。
EasyAR 运动融合可以让图像和物体跟踪摆脱抖动困扰，跟踪稳定，并且可以在离开相机视野之后继续跟踪。
## 不同平台的运动跟踪方案的选择
部分操作系统或厂商通过系统原生的 AR SDK 提供类似的运动跟踪功能，如苹果 ARKit,谷歌 ARCore 和华为 AR Engine 等。
为保证最佳效果，在部分平台，EasyAR 自动选择当前可用的平台原生的运动跟踪方案而不需要额外配置。例如在 iOS 平台上，EasyAR 会优先调用 ARKit 的运动跟踪功能。需要进一步了解，请参阅[EasyAR运动跟踪与平台原生运动方案的关系](comparison.html)。
EasyAR 的运动跟踪解决方案，目前支持的设备包括主流的智能手机和平板电脑。EasyAR 的运动跟踪功能目前暂不支持 AR/MR 眼镜等可穿戴设备。如果这些设备本身支持六自由度的运动跟踪功能，开发者可以通过自定义相机接入 EasyAR 并与的其他功能联合使用。
对于微信小程序开发者，由于平台限制无法直接使用上述任何的运动跟踪方案，可以参阅微信小程序提供的类似[运动跟踪](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)功能。
## 延伸阅读
了解运动跟踪支持的具体机型
* [EasyAR 运动跟踪支持的设备](devices-easyar.html)
* [ARCore 运动跟踪支持的设备](devices-arcore.html)
* [AR Engine 运动跟踪支持的设备](devices-arengine.html)
* [微信小程序支持的设备](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)

---

## 什么是运动跟踪功能？
- 章节路径: `motion-tracking/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/intro.html

# 什么是运动跟踪功能？
## 运动跟踪功能介绍
AR 的运动跟踪功能泛指通过计算机视觉和传感器融合算法，实时跟踪设备（手机、平板、智能眼镜）相对于环境的六自由度位置和朝向的功能。部分厂商或操作系统原生的混合现实 SDK 提供类似的运动跟踪功能，如苹果 [ARKit](https://developer.apple.com/augmented-reality/arkit/),谷歌的 [ARCore](https://developers.google.com/ar),华为的 [AR Engine](https://developer.huawei.com/consumer/en/hms/huawei-arengine/) 等。在部分智能眼镜上，厂商提供类似的运动跟踪功能。在微信小程序平台上，微信开放了功能与运动跟踪相似的[6DoF AR 能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)。
通过厂商或操作系统支持的设备占比相对较低，为了使得更多机型支持运动跟踪功能， EasyAR 的运动跟踪（Motion Tracker）利用计算机视觉、惯性同步定位和建图（VI-SLAM）技术，在更多的机型上实现六自由度的实时跟踪。
![Motion Tracking](https://doc-asset.easyar.com/develop/motion-tracking/media/motion-tracking.png)
## 后续步骤
* 了解 [EasyAR 运动跟踪支持的设备](devices.html)
* 了解 [EasyAR 运动跟踪与 EasyAR 其他模块的关系](motion-tracking-and-easyar.html)
* 了解 [EasyAR 运动跟踪与ARKit/ARCore/华为AR Engine的关系](comparison.html)

---

## 为其他功能提供数据的运动跟踪
- 章节路径: `motion-tracking/motion-tracking-and-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/motion-tracking-and-easyar.html

# 为其他功能提供数据的运动跟踪
运动跟踪是增强现实与环境交互的基础功能之一。运动跟踪组件在提供这项功能的同时可以为其他功能提供输入帧数据，同时具有运动跟踪和摄像头控制的功能。
运动跟踪与 EasyAR 其他功能的关系主要有以下几种情况：
* 部分 EasyAR 的功能必须依赖运动跟踪功能。
* 功能不完全依赖运动跟踪，但是在支持运动跟踪的机型上效果更好。
* 部分功能独立于运动跟踪即可工作。
|EasyAR 功能|是否依赖运动跟踪功能|
|平面检测|是|
|稀疏空间地图|是|
|稠密空间地图|是|
|图片跟踪|否|
|3D 物体识别|否|
|表面跟踪|否|
|EasyAR Mega|否|
> **注意**
EasyAR Mega 功能并不依赖运动跟踪功能，但是在支持运动跟踪功能的设备上可以体验最优的 Mega 效果。
> **注意**
图片跟踪可以不依赖运动跟踪独立运行，也可以联合运动跟踪实现融合跟踪的效果。详情参见 [运动融合|扩展跟踪](../image-tracking/motion-fusion.html)
> **注意**
物体跟踪可以不依赖运动跟踪独立运行，也可以联合运动跟踪实现融合跟踪的效果。详情参见 [运动融合|扩展跟踪](../object-tracking/motion-fusion.html)
## 相关主题
* [运动跟踪](intro.html)
* [摄像头和输入扩展](../cameras/cameras.html)
