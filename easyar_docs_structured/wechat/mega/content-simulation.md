---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-simulation.html
original_file: doc--zh-cn--develop--wechat--mega--content-simulation.md
normalized_at: 2026-02-27
---
# 在 Unity 编辑器中模拟运行
这篇文档将指引您通过 Unity 编辑器模拟真实场景定位，帮助您在小程序上线前完成虚拟内容的静态对齐检查。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* [确认定位库已经可以使用](../../mega/localization-verify.html)。
* 使用 Mega Toolbox 工具[采集模拟运行数据](../../mega/input-recording.html)。
* [使用标注工具创建标注](content-annotation-creation.html)。
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)，比如：
![摆放完成的场景](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation08.png)
> **重要事项**
使用现场录制的 EIF 数据可以直观地验证虚拟内容的位置摆放是否准确。
但由于 xr-frame 和 Unity 平台环境不同，代码脚本逻辑和渲染结果无法在模拟运行中得到验证。
## 模拟运行
1. 创建一个 **Sense 许可证**
由于在 Unity 上模拟运行需要用到 EasyAR Sense ，需要准备一个 Sense 的许可证（它可以是试用的）。
在 EasyAR 开发中心中选择 [**Sense 授权管理**] > [**创建一个新的 Sense 许可证密钥**]：
![Sense许可证](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation01.png)
* 选择 EasyAR Sense 个人版。
* 在‘是否使用稀疏空间’选项中选择‘否’。
* 填写任意的应用名称，iOS Bundle ID 及 Android Package Name。
* 点击确定，此后在开发中心的 Sense 授权管理中会出现申请的许可证。
![Sense许可证信息](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation02.png)
* 在 EasyAR 开发中心中选择准备工作中申请的 Sense 许可证。
![Sense许可证列表](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation03.png)
点击复制：
![Sense许可证复制](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation04.png)
* 点击 Unity 编辑器上方菜单栏中的 **[EasyAR]** > **[Mega]** > **[Configuration]** 进入配置页面：
![Configuration](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation05.png)
* 点击左侧 **Sense** 进行配置，填入 **Sense 许可证**。
![Sense许可证填入](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation06.png)
* 启用验证工具，点击**运行**。
![摆放完成的场景](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation09.png)
在弹出窗口中点击 **OK**。
![弹出窗口](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation10.png)
* 点击**加载按钮**，加载 EIF 文件。
![加载按钮](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation11.png)
选择准备工作中保存的 EIF 文件（后缀名为 `.eif` 或 `.mkveif`）。
![选择EIF](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation12.png)
* **隐藏 Block Mesh**。
* 可以将 Block Mesh 全部设置为**隐藏**。
![隐藏Block Mesh](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation13.png)
* 可以在验证工具中将 **Block Mesh Alpha** 设置为 0，即透明。
![更改Alpha](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation14.png)
将控制条拖至最左侧。
* **播放 EIF**
> **重要事项**
在 Unity 编辑器上播放 EIF 时使用的 SDK 以及输入帧数据与 xr-frame 小程序使用的均不同，因此这种方式：
✅ 可以用于直观地验证虚拟内容的位置摆放是否准确，验证云定位服务在该位置的定位准确度。
❌ 不能用于验证 xr-frame 小程序实机运行的最终效果。
工作原理与预期： 在 Unity 播放 EIF 数据时，EasyAR SDK 会调用录制的输入帧数据，向配置的定位服务发起**真实**的云端请求。
* **若定位成功且表现稳定**： 模型位置准确且无漂移，则可预期该场景在 xr-frame 小程序上也能达到较理想的效果。
* **若定位失败或表现异常**： 模型出现频繁跳动、偏移或无法定位，通常意味着 xr-frame 小程序实机运行时也会面临相似的问题。
## 相关主题
* [使用Session验证工具播放EIF文件](../../unity/simulation/tool.html)
