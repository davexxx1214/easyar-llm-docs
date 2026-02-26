---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/sample-arsession.html
---

Workflow\_ARSession 示例详解 | EasyAR 文档
**
##### Table of Contents
**
# Workflow\_ARSession 示例详解
`Workflow\_ARSession` 是一个**轻量级**的 AR 会话管理示例，旨在展示如何以最小依赖构建一个完整的 AR 应用流程。该示例同时支持 **AR Foundation 兼容模式** 和 **简易模式** ，您可以根据项目需求灵活选择。
## 使用方法
### 场景选择（二选一）
在 Unity 编辑器中，`Workflow\_ARSession` 场景包含两组互斥的配置根对象，请**仅启用其中一组**（确保另一组处于非激活状态）：
|配置名称|适用场景|依赖|
|`ARFoundationCompatibleSceneSetup`|已使用或计划集成 **AR Foundation** 的项目|需完成 [AR Foundation 配置](arfoundation.html)|
|`SimpleSceneSetup`|**不依赖 AR Foundation**，直接使用 EasyAR 原生能力|无额外依赖，适合轻量级 AR 应用|
### 构建与运行
1. 将 `Workflow\_ARSession` 添加至菜单栏 `File` &gt; `Build Settings` 或 `Build Profiles` &gt; `Scene List` 中。
2. 根据所选目标平台（如 Android 或 iOS），在 `Project Settings` &gt; `Player` 中确认构建选项。
3. 构建到真机并运行。
应用启动后，将自动初始化摄像头并等待识别目标。
## 识别目标与获取方法
本示例默认演示 **图像识别（Image Tracking）** 功能，但其架构可轻松扩展至物体跟踪、云识别等其他模式。
### 默认目标：`namecard.jpg`
* **目标类型**：2D 图像（建议打印尺寸 ≥ 90mm × 54mm）
* **下载地址**：🔗 [namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
### 如何替换目标？
1. 将您的图像（JPG/PNG）放入 `Assets/Samples/EasyAR Sense Unity Plugin/[版本号]/\_\_All Samples\_\_/Workflow/Workflow\_ARSession/Targets`。
2. 选择场景中的 `ImageTarget-namecard` 组件，在 **Inspector** 的 `Image Target Controller (Script)` 中更改 `Texture` 为您的图像。
3. 修改 `Name` 和 `Scale`。 `Scale` 是您的目标的物理尺寸（单位：米），以图像的长边为准。
![Replace Image Target](https://doc-asset.easyar.com/develop/unity/fundamentals/media/image-target-config.png)
4. 保存并重新构建。
## 预期效果
当摄像头对准目标图像时，系统将：
1. 实时检测并跟踪图像；
2. 在图像平面上叠加一个 3D 熊猫；
熊猫的位置、朝向与缩放严格绑定于图像目标的位姿，即使图像运动、部分遮挡或光照变化，仍能稳定跟踪。
## 扩展建议
* **添加物体跟踪**：替换 `ImageTracker` 为 `ObjectTracker`，加载 `.obj` 模型文件；
* **接入云识别**：使用 `CloudRecognizer` 替代本地目标列表；
* **多目标支持**：从单个图像目标扩展为多个图像，系统将自动处理并发跟踪。
##### 提示
更多功能组件请 [访问AR功能组件](session-components.html)。
通过 `Workflow\_ARSession`，您可快速掌握 EasyAR 的核心工作流，并以此为基础构建生产级 AR 应用。