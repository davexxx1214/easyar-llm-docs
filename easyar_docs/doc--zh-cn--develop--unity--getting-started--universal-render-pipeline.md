---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/universal-render-pipeline.html
---

配置 Universal Render Pipeline（URP） | EasyAR 文档
**
##### Table of Contents
**
# 配置 Universal Render Pipeline（URP）
这篇文档介绍了 Universal Render Pipeline（URP） 工程接入 EasyAR 功能时如何配置。
## 开始之前
* 了解[在 Unity 中使用 URP 的方法](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest?subfolder=/manual/InstallingAndConfiguringURP.html)。
* 参考[在 Unity 中启用 EasyAR](enable-easyar.html) 导入 EasyAR Unity 插件。
## 创建 Universal Render Pipeline 资产
##### 注意
如果 Unity 项目使用 URP 项目模板创建，或项目中已经存在 UniversalRenderPipelineAsset 和 Universal Renderer，可以直接跳到[确认项目已切换至 URP 渲染管线](#unity-gettingstarted-universal-render-pipeline-switch)。
在 **Project** 窗口通过右键菜单 **Create** &gt; **Rendering** &gt; **URP Asset(with Universal Renderer)** 创建所需资产：
![Unity6.2_URP_Create_Asset](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline06.png)
## 找到目标平台所使用的 Universal Render Pipeline 资产
1. 点击菜单栏 **Edit** &gt; **Project Settings** &gt; **Graphics**。
顶部的 **Default Render Pipeline** 槽位应当已分配了一个 `Universal Render Pipeline Asset`。
![Unity6.2_URP_Graphics](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline01.png)
##### 提示
该选项在旧版 Unity 中的名称为 **Scriptable Render Pipeline Settings**。
2. 点击菜单栏 **Project Settings** &gt; **Quality**。
选择目标平台的质量级别，下方的 **Render Pipeline Asset** 即目标平台使用的 Universal Render Pipeline 资产。若为空，则目标平台使用的 Universal Render Pipeline 资产为 **Graphics** 窗口中配置的资产。
![Unity6.2_URP_Quality](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline02.png)
##### 提示
若 **Quality** 中的设置与 **Graphics** 不一致，系统将优先使用 **Quality** 中的 Asset。
## 配置 Universal Render Pipeline 资产
##### 重要事项
Unity 编辑器与 Android/iOS 等设备上使用的 Universal Render Pipeline 资产往往是不同的，在编辑器上使用和在设备上使用需要分别配置。
1. 选择目标平台使用的 `Universal Render Pipeline Asset`，然后选择它所使用的 `Universal Renderer Data`。
![Unity6.2_URP_Renderer](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline03.png)
##### 提示
如果项目中配置了多个 Renderer，确保选择的是 **AR 相机正在使用** 的那个渲染器。您可以在场景相机的 **Camera** 组件 &gt; **Rendering** &gt; **Renderer** 选项中确认当前的索引值。
2. 在 `Universal Renderer Data` 的 **Inspector** 面板下方点击 **Add Renderer Feature**，添加 [EasyARCameraImageRendererFeature](../../../api/unity/easyar.EasyARCameraImageRendererFeature.html)。
![Unity6.2_URP_Renderer_Add_Feature](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline04.png)
## 使用 EasyAR 示例的注意事项
EasyAR Unity 插件自带的示例场景默认使用 `Built-in` 渲染管线的材质和着色器。Unity 会自动将这些材质和着色器转换为 URP 兼容的版本，但有少部分资源可能会渲染异常，需要参考 [Convert assets using the Render Pipeline Converter](https://docs.unity3d.com/Documentation/Manual/urp/features/rp-converter.html) 手动转换。
![非 URP 渲染异常](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline08.png)
点击菜单 **Window** &gt; **Rendering** &gt; **Render Pipeline Converter**，选择 **Built-in to URP** 打开转换窗口。勾选 **Material Upgrade** 和 **Readonly Material Converter** &gt; 点击下方的 **Convert Assets**。
![Render Pipeline Converter](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline09.png)
转换完成后，示例材质显示将恢复正常。
## 常见问题
若配置不正确，运行时将没有相机画面，常常为显示为黑屏，但是在跟踪上目标时，添加在跟踪目标下的内容会正常显示。
在 4000 及以上版本中，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，这时画面或日志中会显示 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 为 `URP RenderPipeLineAsset not properly setup`：
![Session_Broken_Caused_By_URP](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline07.png)
解决该问题需按本文描述正确配置 `Universal Render Pipeline Asset`。
## 相关主题
* [Unity 兼容性](../fundamentals/unity-compatibility.html)