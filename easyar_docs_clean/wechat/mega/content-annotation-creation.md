---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-annotation-creation.html
original_file: doc--zh-cn--develop--wechat--mega--content-annotation-creation.md
normalized_at: 2026-02-27
---
# 使用 Unity 编辑器创建并上传标注
这篇文章介绍了如何使用 Unity 编辑器上的 Mega Studio 创建并上传标注。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)
* 准备模型： 使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[XRFame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)，准备符合 xr-frame 要求的模型文件。
* 将模型的文件导入 Unity 。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
## 为什么需要标注
EasyAR Mega Annotation（EMA） 可用于同步跨平台的（坐标系定义不同）空间位置。
![Unity](https://doc-asset.easyar.com/develop/wechat/mega/media/content-transform-sync01.png)
Unity 环境下标注的本地坐标系： X 正方向朝后，Y 正方向朝上，Z 正方向朝右。
![xr-frame](https://doc-asset.easyar.com/develop/wechat/mega/media/content-transform-sync02.png)
xr-frame 环境下标注的本地坐标系： X 正方向朝后，Y 正方向朝上，Z 正方向朝左。
上述方向差异源于 Unity 与 xr-frame 采用的坐标系定义（左手/右手系）不同。
使用 EMA 同步空间位置有以下显著优势：
1. 简化开发流程： 自动处理跨平台坐标转换，规避了手动计算导致的繁琐逻辑及易错性。
2. 提升调试效率： 能够直接在 [MegaToolbox](../../../mega/reference/toolbox-wechat/intro.html) 上加载，便于快速进行真机测试与数据验证。
## 操作步骤
1. **创建标注工具**
在 Unity 的 **Hierarchy** 面板中点击右键，依次选择： **EasyAR Mega** > **Tool** > **Annotation Tool（Edit Mode）**。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation01.png)
创建完成后，场景中生成 EasyAR.Mega.Annotation 和 MegaBlocks 两个节点。
选中 EasyAR.Mega.Annotation 节点，在其 **Inspector** 面板中会出现用户名/邮箱及密码输入框。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation02.png)
2. **登录账号**
输入 EasyAR 账号，密码后点击登录，若成功 **Inspector** 面板中会出现 Studio 工具。
3. **选择 Mega 云定位库**
点击 Mega Cloud Service 右侧的图标。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation04.png)
选择要使用的库。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation05.png)
加载定位库及 Mega Blocks 信息成功后， Studio 工具面板如图所示。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation06.png)
4. **加载Block稠密模型**
点击 Block 名称右侧的 加载 即可动态加载该 Block 的稠密模型。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation07.png)
模型加载完成后出现在 Scene 标签页面中，注意当左下角出现图中标识时当前视野内的模型尚未加载完成，稍等一会儿待该标识消失表示加载已经完成。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation08.png)
5. **创建标注**
在场景中按住 Ctrl （Windows） / Command （Mac） 键，然后在需要标注的地方点击鼠标左键即可。
6. **使用模型**
将导入的模型拖到场景节点，作为标注的子节点。
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0** ， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
7. **[可选] 精确调整模型位置**
如果需要精确调整模型位置和朝向，可以参考[如何使用 Unity 编辑器使 3D 内容与实景精确对齐](content-realworld-alignment.html#wechat-mega-content-realworld-alignment-precise-adjustment)。
8. **新建标注数据包**
点击 **Inspector** 面板中的标注数据包右侧的图标。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation16.png)
在框中填入标注数据的名称，并点击右侧的勾。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation17.png)
创建成功后应如图所示，之后点击下方的确定。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation18.png)
点击上传图标进行上传。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation19.png)
上传成功后弹出提示。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation20.png)
9. **记录标注 ID**
您需要记录标注数据的名称或 ID 以在 xr-frame 上加载对应的标注数据。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation21.png)
在上传成功后，您在云定位库中也可以看到相应的信息。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation22.png)
此处也可以查看上传的标注数据名称和 ID。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 后续步骤
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* 尝试[在 Unity 编辑器上模拟运行](content-simulation.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)
