---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/samples.html
original_file: doc--zh-cn--develop--unity--headsets--samples.md
normalized_at: 2026-02-27
---
# 在 XR 头显或眼镜上使用 EasyAR 样例
EasyAR 对所有头显提供统一的样例，样例中没有任何代码，全部由场景中配置实现。功能本身的使用可以参考相关功能在 Android/iOS 手机上样例实现。
头显样例名称为 `Combination\_BasedOn\_\*` , 比如 Pico 的样例为 `Combination\_BasedOn\_Pico`。 该样例在一个场景中演示了大部分 EasyAR 功能，它们可以动态开关，可以单独使用，也可以同时打开。
## 准备工作
* 确定您的头显或眼镜当前在 EasyAR [支持列表](../../headsets/headsets.html)
* 下载并导入 [EasyAR Unity 插件包](https://www.easyar.cn/view/download.html)
* 下载并导入 [EasyAR Unity XR设备扩展包](https://www.easyar.cn/view/download.html)
* 获取适合 XR 头显或者眼镜的 EasyAR 许可证，头显或眼镜可用 License 类型包括
* EasyAR Sense 4.x **XR License** 试用版（试用，在 EasyAR 网站自主开通）
* EasyAR Sense 4.x **XR License** 正式版（付费后使用，请联系商务购买开通）
* EasyAR Sense 4.x **XR License** 企业版（企业版 SDK 使用）
> **小心**
头显和眼镜上**仅允许使用 XR License**，普通 License 无法使用 EasyAR 功能。
## 导入官方样例
1. 内建支持的设备的样例位于 EasyAR Unity 插件包中，根据设备单独导入需要的样例。
![xr-samples-location](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-samples-location.png)
2. 通过扩展支持的设备样例随对应的头显扩展一起分发。可以使用 Unity 将样例导入工程中。以Pico为例。
![xr-pico-extension](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-pico-extension.png)
## 样例打包并运行
分别完成头显工程配置和样例使用说明。
* 严格参照对应头显官方的文档和说明做好对应的配置，EasyAR 文档中不会覆盖相关内容。
* 按照 EasyAR 文档中各平台说明进行配置。
Android: 请参考 [Android 工程配置](../fundamentals/setup-player.html)
visionOS: 请参考 [visionOS 工程配置](setup-visionpro.html)
XREAL 除了按照 Android 平台设置外，额外需要 [XREAL 工程配置](setup-xreal.html)
* 样例打包
在 Unity 里打包样例使用，并部署到设备上运行。具体方法参见 [Unity上运行样例](../getting-started/quickstart.html)。
## 用法说明
样例内置多个按钮，其具体功能如下。
![xr-sample-usage-7](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-sample-usage-7.png)
* 按钮1 `HUD`：切换UI显示模式，初始状态UI会固定在现实世界中，打开HUD之后UI会始终显示在眼前。
* 按钮2 `Record`：开关EIF录制。打开之后必须关闭才能录制正常的EIF文件，否则录出来的文件将无法使用。
* 按钮3 `Image`：开关图像跟踪。
* 按钮4 `Image Fusion`：开关图像跟踪+运动融合模式。
* 按钮5 `Dense`：开关稠密空间建图。
* 按钮6 `Sparse`：开关稀疏空间建图。
* 按钮7 `Mega`：开关 Mega。
## 功能详解
* 默认功能开关
所有功能启动时默认都是**关闭**的，这是通过在编辑器上将对应脚本停用实现的，按钮操作操作的是对应脚本的启用/停用，可以根据实际要运行的样例设置默认启用的功能。
![hmd-default-disable](https://doc-asset.easyar.com/develop/unity/headsets/media/hmddefault-all.png)
* 坐标系原点参照
样例中在[运动跟踪](../../motion-tracking/intro.html)的坐标系原点都放置了一个静止的熊猫模型，用于检查运动跟踪状态。这个模型对于解耦问题是有帮助的，比如在运行 Mega 的时候，有些快速漂移就是设备运动跟踪（即设备自身缺陷）导致的，这时候这个模型也会跟着一起漂移/可以根据需要，调整或删除这个熊猫模型。
* 使用内嵌图像跟踪的识别图
* 样例中预设了平面图像跟踪使用的图像的大小，您需要使用 A4 纸打印 namecard.jpg，必须保持图像的比例不拉伸，不裁剪，尽量充满纸张（下图）。
![namecard](https://doc-asset.easyar.com/develop/unity/headsets/media/namecard.jpg)
* 测量打印完成纸张上名片图案的长度，根据测量的结果，需将 Unity 场景中 `Image Target` 的 `Scale` 设为**与真实物理大小一致**（单位是米）。
![set-the-actual-size](https://doc-asset.easyar.com/develop/unity/headsets/media/set-the-actual-size.png)
* 在 `EasyAR 运动融合` 打开时，只能跟踪固定位置（不能移动）的图像。如果运动融合关闭，图像超出视野的时候就无法跟踪。
* 有时候眼镜视角不能很好的反应相机图像大小，如果识别不到可以尝试让眼镜相机靠近图像。实际使用时建议跟踪更大的图像，比如 5米\*5米 大小。
> **注意**
在头显上无论 EasyAR 运动融合功能是开是关，`image target` 的 `Scale` 参数都必须设置为真实的物理大小，否则显示位置会是错误的。
* Mega 配置
如果你在使用 EasyAR Mega，你需要参考 [Mega Unity 快速入门](../mega/quickstart.html)。
