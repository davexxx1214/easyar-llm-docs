---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/setup-easyar.html
---

EasyAR 配置 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR 配置
EasyAR 配置页面可以从 Unity 菜单 `EasyAR &gt; Sense &gt; Configuration` 或 `Edit &gt; Project Settings &gt; EasyAR` 进入。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
这里包含所有对 EasyAR Sense Unity Plugin 的全局配置
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/settings-easyar.png)
## Initialize On Startup
在启动时初始化 EasyAR。通常建议保持这个选项打开。
如果关闭该选项，需要手动初始化 EasyAR Sense，具体方法可以参考 [初始化 EasyAR Sense](initialization.html) 。
## EasyAR Sense License
EasyAR Sense License 相关配置。
### LicenseKey
EasyAR Sense License Key。使用 EasyAR 功能必须填写可用的 license。
仅当使用接口手动初始化 EasyAR Sense 时可留空。
##### 注意
在头显设备（Vision Pro、XREAL、Pico、Rokid 等）设备上使用时，需要使用 EasyAR XR License。
##### 注意
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
### Verify When Build
在构建 Unity 工程时验证 license Key。
当这个选项打开时，Unity 项目构建过程会验证 license Key，如果 license 在构建平台上无效或不包含 Unity Player Settings 中设置的包名，构建过程将会失败。如果需要使用其它地方配置的 license key 或者需要在 Unity 构建过程之后修改包名，可以关闭这个选项。
## Lib Variants
EasyAR Sense 库变种配置。
## EasyAR Sense License
EasyAR Sense License 相关配置。
### LicenseKey
EasyAR Sense License Key。使用 EasyAR 功能必须填写可用的 license。
仅当使用接口手动初始化 EasyAR Sense 时可留空。
##### 注意
在头显设备（Vision Pro、XREAL、Pico、Rokid 等）设备上使用时，需要使用 EasyAR XR License。
##### 注意
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
### Verify When Build
在构建 Unity 工程时验证 license Key。
当这个选项打开时，Unity 项目构建过程会验证 license Key，如果 license 在构建平台上无效或不包含 Unity Player Settings 中设置的包名，构建过程将会失败。如果需要使用其它地方配置的 license key 或者需要在 Unity 构建过程之后修改包名，可以关闭这个选项。
## Permissions
应用权限配置。通常建议保持默认。
除相机权限外，其它权限配置不可更改，由其它功能配置所决定。
|权限|是否可改|启用条件|权限说明|
|`Camera`|是||相机权限，使用相机设备需要的权限|
|`AndroidMicrophone`|否|Variant 为 VideoRecording|麦克风权限，使用录屏功能需要的权限|
|`Location`|否|导入 Mega 支持包|（fine）定位权限，使用 EasyAR Mega 需要的权限|
## Unity XR
Unity XR 框架（AR Foundation 等）相关配置。
### AR Foundation Support
AR Foundation 支持开关，建议保持打开。
在极个别情况下，比如需要使用 AR Foundation 4 或 AR Foundation 更新导致编译出错，可以关闭这个选项，但插件内所有与 AR Foundation 相关的功能将同时禁用。
##### 注意
修改此选项之后脚本会自动重新编译。
### Unity XR Auto Switch
自动切换 Unity XR（比如 AR Foundation）物体的功能配置。
* `Editor` ：编辑模式选项
* `Disable AR Session` ：存在 [ARSession](../../../api/unity/easyar.ARSession.html) 时，编辑时禁用 AR Foundation 的 ARSession。
* `Player` ：运行模式选项
* `Enable` ：启用运行时控制。注意：关闭该选项，编辑模式被禁用的组件在运行时不会被恢复。
* `Enable If Desktop` ：在 Windows/Mac 上启用。
* `Enable If Mobile AR On Startup` ：切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。通常这个选项需要 XR Plug-in Management 中的 `Initialize XR on Startup` 是选中的。
* `Disable If Non Mobile AR Post Startup` ：切换器启动时，如果存在移动 AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。通常这个选项会在 XR Plug-in Management 中的 `Initialize XR on Startup` 未选中时被使用。
* `Restore AR Session When Disabled` ：功能禁用时，恢复（启用）所有被禁用的 AR Foundation 的 ARSession（无论它是否由 EasyAR 所禁用）。这个选项通常用于恢复编辑时被禁用的组件。
详细功能说明可参考 [Unity XR 自动切换](unity-xr-switch.html) 。
## Mega
EasyAR Mega 功能配置。
### InertialCameraDevice Support
只读选项，显示当前配置下惯导功能是否可用以及 ONNX 运行时信息。
如果显示信息不符合需求，需要视情况修改 `Lib Variants` 以及 `ONNX Runtime (Bundled)` 选项。
### Mega Block &gt; Localization Service Access [Global]
全局 Mega Block 定位服务器配置。
### Mega Landmark &gt; Localization Service Access [Global]
全局 Mega Landmark 定位服务器配置。
## Spatial Map
EasyAR 空间地图功能配置。
### Service Access [Global]
全局稀疏地图服务器配置。
## Image Tracking
EasyAR 图像跟踪功能配置。
### Target Gizmo
编辑器下 ImageTarget 的 Gizmos 配置。
打开这些选项将会在 Unity Editor 中显示对应 gizmo，如果场景中该类 target 过多，可能会影响编辑器中的启动性能。在设备上运行时的性能不会受到影响。
* `Enable Image File` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.ImageFileSourceData](../../../api/unity/easyar.ImageTargetController.ImageFileSourceData.html) 的 target 的 Gizmos。
* `Enable Target Data File` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.TargetDataFileSourceData](../../../api/unity/easyar.ImageTargetController.TargetDataFileSourceData.html) 的 target 的 Gizmos。
* `Enable Target` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.TargetSourceData](../../../api/unity/easyar.ImageTargetController.TargetSourceData.html) 的 target 的 Gizmos。
* `Enable Texture 2D` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.Texture2DSourceData](../../../api/unity/easyar.ImageTargetController.Texture2DSourceData.html) 的 target 的 Gizmos。
### Cloud Recognition (CRS) &gt; Service Access [Global]
全局云识别服务器配置。
## Object Tracking
EasyAR 物体跟踪功能配置。
### Target Gizmo
编辑器下 ObjectTarget 的 Gizmos 配置。
* `Enable`：开启 Gizmos。
## Third-Party Libraries
第三方库配置。
### ARCore SDK
ARCore SDK 配置。
ARCore 提供了在部分 Android 设备上的运动跟踪能力，可以阅读 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 来了解 EasyAR 功能与运动跟踪的关系，以及是否需要和什么时候需要使用 ARCore。
* `AR Foundation Or Optional`: 随 EasyAR 或 `AR Foundation` 一起分发的 ARCore SDK 将会被包含在应用中，根据 ARCore XR Plugin 的设置决定。一般情况下推荐使用这个选项，它会自动处理 `AR Foundation` 的情况。
* `Optional`: ARCore 功能在支持 ARCore 并安装了 Google Play Services for AR 的设备上可以使用。
* `Required`: 应用将只能在支持 ARCore 并安装了 Google Play Services for AR 的设备上运行。
* `External`: 如果在使用 `AR Foundation` 或其它 ARCore SDK 分发，可以使用这个选项。这样随 EasyAR 一起分发的 ARCore SDK 将不会使用。也可以使用这个选项来完全排除 ARCore SDK 在应用中的使用。
##### 小心
如果把 `ARCore SDK` 设置为 `Required`，或是在 AR Foundation 的 ARCore 配置中将 `Requirement` 设置为 `Required`，并在不支持 ARCore 的设备上安装了打包后的应用，设备会错误地报告 ARCore 是可用的并以 ARCore 运行。这会造成一个假象，似乎这些设备正在运行 ARCore 并且运行不正常（黑屏或其它异常情况），但这是错误的。
出现这个现象的原因是由于 Google Play 商店阻止在不受支持的设备上安装标记 ARCore 为必需的应用，所以这些应用总是假设它们正在受支持的设备上运行。
正常配置下，这些设备会在 session 组装时判断 ARCore 不受支持并使用 EasyAR 的功能。
关于 `Optional` 和 `Required` 的详细说明及上线 Google Play Store 应用需要做的其它配置可以参考 Google 的说明（[中国大陆](https://developers.google.cn/ar/develop/java/enable-arcore)，[国际](https://developers.google.com/ar/develop/java/enable-arcore)）。
##### 注意
在 EasyAR Sense Unity Plugin 中，ARCore 的支持所需的库文件和配置已经在插件包中，但要在手机上运行，仍需在手机上安装 [Google Play Services for AR](https://play.google.com/store/apps/details?id=com.google.ar.core) 。
有三种不同来源的 ARCore SDK 可以使用：
* 使用随插件分发的 ARCore SDK
插件内集成了一个 ARCore SDK 版本，详细信息可以参考 [ARCore、AR Engine 版本兼容性](../motion-tracking/3rdparty-compatibility.html)。在使用 EasyAR 的 ARCore 封装时，可以不另外导入 AR Foundation。
* 使用 AR Foundation 的 ARCore SDK
如果需要使用 AR Foundation 的 ARCore SDK，可以参考 Google 的说明（[中国大陆](https://developers.google.cn/ar/develop/java/enable-arcore)，[国际](https://developers.google.com/ar/develop/java/enable-arcore)）进行配置，这时 `ARCore SDK` 选项需要选择 `AR Foundation Or Optional` 或 `External` 。
* 使用其它 ARCore SDK
如果有其它第三方插件或项目内有 ARCore SDK 的分发，也可以使用这些 ARCore SDK。这时 `ARCore SDK` 选项需要选择 `External` ，并根据具体插件或项目的要求进行配置。
**Warn 32-bit-only ARCore-enabled build**
根据 Google 的说明，在 arm64 的设备上运行仅有 armv7 库文件的程序，ARCore 不会正常工作。在打包时如果未选择 ARM64 会弹出警告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/settings-arcore-warn.png)
这时需要修改项目配置，使用 IL2CPP 编译并选择 ARM64 支持。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/adnroid-64bit.png)
##### 小心
如确有需要，可以选择 `Continue and don't warn me again`，或者关闭该选项，这将关闭打包时的检查。关闭检查只是在打包时不弹出提示，但运行时在一些设备上将有可能出现异常，包括但不限于崩溃或黑屏等。
### AR Engine SDK
AR Engine SDK 配置。
AR Engine 提供了在部分 Android 设备上的运动跟踪能力，可以阅读 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 来了解 EasyAR 功能与运动跟踪的关系，以及是否需要和什么时候需要使用 AR Engine。
* `AREngineInterop` ：AREngineInterop 可用。随 EasyAR 一起分发的 AR Engine SDK 将会被包含在应用中。
* `External` ：AREngineInterop 可用。随 EasyAR 一起分发的 AR Engine SDK 将不会使用。
* `Disabled` ：AREngineInterop 不可用。随 EasyAR 一起分发的 AR Engine SDK 将不会使用。所有与 AR Engine 有关的功能将被禁用。
### ONNX Runtime (Bundled)
是否使用捆绑的 ONNX 运行时。仅在 `Lib Variant` 为 `Full` 时有效。
如需使用不同版本的 ONNX，可用从 ONNX 官方获取更新版本并关闭该选项。使用自己编译的二进制不兼容的 ONNX 将导致未知错误。
## Workaround For Unity
针对 Unity bug 或不合理行为的应对方案。
### GenerateXMLDoc
在脚本重新加载时生成 XML 文档，以使 API 文档的 intelliSense 可以工作。
### URP17RG\_DX11\_RuinedScene
Workaround URP 17 Render Graph DX11 场景渲染被毁损。Unity 6.2 及更新版本中该选项已关闭。
### URP17RG\_IOS\_Glitches\_Partial
部分规避 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture)。
问题简述：当从 EasyAR 获取相机纹理（类似 ImageTracking\_Coloring3D示例 及 [ARSession 工作流（CameraDevice）](../cameras/sample-camera-device.html) 示例中的使用），在 iOS/Mac 设备上可以观察到视觉故障和伪影。我们已经在纯 Unity 包中复现该问题并报告给了 Unity： [Glitches on iOS with AR Camera Image Rendering (URP 17 render graph)](https://discussions.unity.com/t/glitches-on-ios-with-ar-camera-image-rendering-urp-17-render-graph/1548048) 。问题进展可以关注 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 更新以及 Unity 未来版本的发布日志。