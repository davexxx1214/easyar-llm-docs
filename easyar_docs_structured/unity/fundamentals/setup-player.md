---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/setup-player.html
original_file: doc--zh-cn--develop--unity--fundamentals--setup-player.md
normalized_at: 2026-02-27
---
# Player 配置
本文介绍在 Unity 中使用 EasyAR Sense Unity Plugin 打包应用时需要注意的 Player 配置选项。
## 不同平台配置说明
在 Unity 打包时，需要检查并确认下列配置。
依次在 Unity 菜单 `File -> Build Settings-> Player Settings`，点击安卓图标，调出 Android平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
通常情况下需要设置以下选项。
* Package Name
设置 Android 应用的 `Package Name`, **注意 `Package Name` 要与创建 License Key 时填写的必须一致**。
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
* API Level
EasyAR 支持的 `API level` 与使用的版本有关， 使用 `Full` 变种时，需要 `Android API Level 24` 或以上; 使用其他变种时，EasyAR Sense 需要 `Android API Level 21` 或以上。
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* Target Architecture
如果需要使用 Google ARCore ，或其它情况需要编译支持 ARM64 ，需要使用 `IL2CPP` 编译并选择 `ARM64 支持`。在不需要支持 ARM64 架构的情况下无需配置。
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/adnroid-64bit.png)
* 视频录制功能的特殊配置
如果要使用视频录制功能，需设置 `Graphics API` 为 `OpenGLES3` 或 `OpenGLES2`，并去掉 `Multithreaded Rendering` 的勾选。另外还需要在 EasyAR 配置 中将 `Lib Variants > Android` 设为 `VideoRecording` 。
![androidvideorecord](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-video-recording.png)
依次在 Unity 菜单 `File -> Build Settings-> Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
通常情况下需要设置以下选项。
* Bundle ID
设置 iOS 应用的 `Bundle ID`, 注意 `Bundle ID` 与创建 License Key 时填写的**必须一致**。
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
* Target Architecture
在 `Player Settings` 中修改 `architecture` 为 `ARM64`, 不可使用 `Universal`。
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* Usage Description配置
根据 EasyAR 配置 中 Permissions 中的启用情况，需要配置不同的 Usage Description。
* 如果 `Camera` 权限开启，需要添加 `Camera Usage Description`，否则构建将失败。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-camera-permission.png)
* 如果 `Location` 权限开启，需要添加 `Location Usage Description`，否则构建将失败。
![ioslocationpermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-location-permission.png)
* 需要 EIF 录制的额外配置（XCode 工程，需要时）
若需要录制 EIF 到默认目录并通过 iOS 的文件应用投送到电脑或其他设备，需要在 `Info.plist` 中增加 `UIFileSharingEnabled` 并将值设置为 `true`。
![iosstore](https://doc-asset.easyar.com/develop/unity/fundamentals/media/ios-plist-uifilesharingenabled.png)
## 常见问题
下面是与Player 配置相关的一些常见错误和解决方案。
* License Key 异常的报错
如果 License Key 异常（比如 `Package Name` 不匹配），在打包应用时将会类似 `is not a valid EasyAR Sense license key or it does not match package name `。这时如果选择继续打包，打包出的应用将无法正常使用，请根据窗口提示仔细检查并修复问题后再继续打包。
* 关闭打包时的许可证检查
在一些特殊情况，如果你使用 EasyAR 的接口手动初始化，不使用 `Setttings` 文件中的 `License Key`，你可以选择 `Continue and don't warn me again` ，或者关闭 EasyAR 配置 中的 `EasyAR Sense License > Verify When Build` 选项，这将关闭打包时的检查。
* 非 ARM 架构的 Android 设备支持
EasyAR Sense 不直接支持 x86 及 x86-64 架构的 Android 系统，但是一般x86架构的设备芯片可以兼容 ARM 程序，因此需要配置取消选择 x86 架构，这样在一些 x86 设备上可以正常使用。
