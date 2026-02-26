---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/initialization.html
original_file: doc--zh-cn--develop--unity--fundamentals--initialization.md
normalized_at: 2026-02-27
---
# 使用 License Key 初始化 EasyAR Sense
在 Unity 中使用 EasyAR，需要使用 license key 初始化 EasyAR Sense，以确保功能被激活。有两种初始化方式：自动初始化和手动初始化。
初始化成功后，可以通过 Unity 控制台或操作系统日志看到 EasyAR Sense 的版本号和运行平台信息，例如：
>
> EasyAR Sense (Android-arm64) Version 4.7.0.11800-cf8e24e30
>
## 开始之前
* [EasyAR Sense 许可证](../../license-sense.html) 描述了如何获取 EasyAR Sense 许可证（license key）。在初始化 EasyAR Sense 之前，需要根据实际使用的设备和开发阶段准备好合适的许可证。
## 自动初始化
自动初始化适用于大部分使用场景。
打开 `EasyAR 全局配置`，勾选 `Initialize On Startup` 选项，并填写 `EasyAR Sense License` > `LicenseKey`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-license-settings.png)
自动初始化会在 Unity 的 [BeforeSceneLoad](https://docs.unity3d.com/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) 时间点自动调用。
> **注意**
在编辑器下使用的 license 不会校验应用包名，所以编辑器中可以正常使用的 license，在打包到平台应用或 app 运行时仍有可能失败，这时候需要注意两种情况：
1. 填写的 license 的包名与 Unity Player Settings 中填写的 bundle id/package name 应该一致。
2. 如果 Unity 打包后，在 gradle 或 XCode 工程中修改了包名。这时需要在 Unity 中使用 gradle 或 XCode 里面的包名。
## [可选] 手动初始化
手动初始化主要用于自定义的初始化流程，比如在调用 EasyAR 接口之前弹出用户隐私说明（请参阅 [合规指南](../../compliance/guide.html) ）等。
打开 `EasyAR 全局配置` ，取消勾选 `Initialize On Startup` 选项。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-license-settings-manual.png)
然后使用 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 接口手动调用初始化。
可以通过参数传入 license，
```
EasyARController.Initialize("my-license");
```
也可以使用 `EasyAR 全局配置` 中填写的 license,
```
EasyARController.Initialize();
```
> **重要事项**
[EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 必须在 [ARSession](../../../api/unity/easyar.ARSession.html) 启动之前调用。
在一些特殊情况下，如果要多次调用 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize)，需要确保每次 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 执行后通过 [EasyARController.Deinitialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Deinitialize) 进行反初始化。
## 初始化失败的解决方法
在包含了 [ARSession](../../../api/unity/easyar.ARSession.html) 的场景运行后，如果日志中没有包含类似的信息，则说明初始化失败。
>
> EasyAR Sense (Android-arm64) Version 4.7.0.11800-cf8e24e30
>
在 Unity 编辑器中，可能还会看到类似这样的弹窗
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-fail.png)
> **注意**
需要注意阅读弹窗中显示的文字信息，并不是所有弹窗都是初始化失败。
常见的出错信息和原因如下：
* EasyARSettings is not found
* `EasyAR 全局配置` 资源文件未创建（常见于没有填写 license）
* License Key is empty
* `EasyAR 全局配置` 中未填写 license，或工程中存在多个 `EasyAR 全局配置` 资源文件
* EasyARController.Initialize is not called (InitializeOnStartup = false)
* 手动初始化未在正确的时机调用
* EasyAR stops after script change in play mode
* 编辑器中运行时，脚本发生了改动。这时需要重新运行即可
## 相关主题
* [ARSession](session.html)
* [EasyAR 全局配置](setup-easyar.html)
* [合规指南](../../compliance/guide.html)
* 日志查看方法： [Android](../../diagnostics/log-android.html)、[iOS](../../diagnostics/log-ios.html)、[Unity 编辑器](../../diagnostics/log-windows.html)
