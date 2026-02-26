---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/arfoundation.html
---

在 EasyAR 项目中启用 AR Foundation | EasyAR 文档
**
##### Table of Contents
**
# 在 EasyAR 项目中启用 AR Foundation
如果需要启用 EasyAR 的 AR Foundation 支持，或使用 AR Foundation 的其它功能，需要正确安装配置 AR Foundation。以下内容介绍如何完成这些操作。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
## AR Foundation 版本兼容性
EasyAR 支持 AR Foundation 5 或更新版本。
##### 重要事项
AR Foundation 的支持是通过自定义相机实现的。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
## 安装 AR Foundation
建议参考 [AR Foundation 官方文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest) 来安装 AR Foundation。阅读前注意选择对应的文档版本。
### Unity 2022 及更新版本
如果工程中未安装过 XR 相关插件，需要在 `Project Settings` &gt; `XR Plug-in Management` 中，点击 `Install XR Plugin Management` 按钮来安装 XR Plug-in Management 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-managment.png)
如果需要在 Android 平台使用 AR Foundation，在 Android 标签下勾选 `Google ARCore` 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-arcore.png)
如果需要在 iOS 平台使用 AR Foundation，在 iOS 标签下勾选 `Apple ARKit` 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-arkit.png)
如果需要在 visionOS 平台使用 AR Foundation，需要阅读 [Vision Pro 工程配置](../headsets/setup-visionpro.html)。
##### 提示
建议保持 `Initialize XR On Startup` 处于勾选状态，以确保 AR Foundation 能够在默认时间点初始化。
安装完成后，打开 `Package Manager` 窗口，可以看到 `AR Foundation` 以及对应平台的插件会出现在已安装的包列表中。注意这些包的版本号应完全一致。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install.png)
##### 重要事项
在安装和更新 AR Foundation 时，需要确保 `Google ARCore XR Plugin` 和 `Apple ARKit XR Plugin` 版本与 `AR Foundation` 版本完全一致。版本不匹配可能会导致运行时错误或功能异常。
### Unity 2021
在 Unity 2021 版本中，需要手动编辑 `Packages/manifest.json` 文件来指定版本，参考 [官方文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.2/manual/project-setup/edit-your-project-manifest.html)。
比如，如果需要安装 AR Foundation 5.2.0 版本并在 Android 和 iOS 平台使用，要确保 `Packages/manifest.json` 文件中包含以下内容：
```
`{
"dependencies": {
...
"com.unity.xr.arcore": "5.2.0",
"com.unity.xr.arfoundation": "5.2.0",
"com.unity.xr.arkit": "5.2.0",
...
}
}
`
```
## 配置 XR Plug-in
在使用 EasyAR 时，通常 ARCore 的存在并不是必需的。因此应配置 ARCore 为可选，以避免在不支持 ARCore 的设备上应用无法正常运行。
在 `Project Settings` &gt; `XR Plug-in Management` &gt; `ARCore` 中，将 `Requirement` 和 `Depth` 都设置为 `Optional`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-config-arcore.png)
##### 小心
如果把 `Requirement` 设置为 `Required`，并在不支持 ARCore 的设备上安装了打包后的应用，设备会错误地报告 ARCore 是可用的并以 ARCore 运行。这会造成一个假象，似乎这些设备正在运行 ARCore 并且运行不正常（黑屏或其它异常情况），但这是错误的。
出现这个现象的原因是由于 Google Play 商店阻止在不受支持的设备上安装标记 ARCore 为必需的应用，所以这些应用总是假设它们正在受支持的设备上运行。
正常配置下，这些设备会在 session 组装时判断 ARCore 不受支持并使用 EasyAR 的功能。
如有需要，也可以参考以下官方文档来进一步配置 ARCore 和 ARKit。阅读前注意选择对应的文档版本。
* [ARCore 插件配置](https://docs.unity3d.com/Packages/com.unity.xr.arcore@6.4/manual/project-configuration-arcore.html)
* [ARKit 插件配置](https://docs.unity3d.com/Packages/com.unity.xr.arkit@6.4/manual/project-configuration-arkit.html)
## 配置 Universal Render Pipeline
如果当前工程在使用 URP，需要配置 URP 资产。如未正确配置，AR Foundation 的摄像机背景图可能无法正确渲染。
首先确保已经正确配置 EasyAR 的 URP Renderer Feature，参考 [EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html)。
然后在Renderer Features 列表中添加 [ARBackgroundRendererFeature](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARBackgroundRendererFeature.html)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-config-urp.png)
与 EasyAR 的 URP Renderer Feature 配置一样，需要关注 `Project Settings` &gt; `Quality` 中不同平台的配置，确保在所有需要使用 AR Foundation 的平台上都使用了正确配置了 [ARBackgroundRendererFeature](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARBackgroundRendererFeature.html) 的 URP 资产。
另外也可以参考 [AR Foundation 官方的 URP 配置文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/project-setup/universal-render-pipeline.html) 进行配置，阅读前注意选择对应的文档版本。
##### 注意
[EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html) 仍是需要的，这样才能确保在不支持 AR Foundation 的设备上使用 EasyAR 接口的相关功能渲染仍能正常。
## 启用 EasyAR AR Foundation 支持
在 `Project Settings` &gt; `EasyAR` &gt; `Sense` 中，确保 `Unity XR` &gt; `AR Foundation Support` 选项被启用。**该选项是默认开启的。**
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-enable.png)
修改该选项会触发脚本重新编译，需要等待脚本编译完成修改才会生效。如果 Unity 因为某种原因未正常触发编译，可以关闭 Unity，删除 `Library/ScriptAssemblies` 文件夹来强制 Unity 重新编译脚本。
##### 提示
如果 EasyAR 与工程中的 AR Foundation 不兼容，且没有同时使用 EasyAR 和 AR Foundation 的需求，可以关闭该选项。
## 后续步骤
* 了解 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html)
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* [EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html)