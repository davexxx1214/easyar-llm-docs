---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-simple.html
original_file: doc--zh-cn--develop--wechat--mega--content-simple.md
normalized_at: 2026-02-27
---
# 如何使用 Unity 上的 Mega Studio 摆放 3D 内容
这篇文档将带您快速学习如何在 Unity 编辑器上使用标注工具进行模型摆放，为后续在 xr-frame 上的渲染做准备。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)
## 准备 GLTF 模型并拖入 Unity Assets
可以使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[xr-frame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)准备自己的模型并上传到资源托管服务器。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
![模型拖入 Unity Assets](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple01.png)
## 选择Mega云定位库
点击 **Mega Cloud Service** 右侧的图标。
![Studio工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation04.png)
选择要使用的库。
![选择库](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation05.png)
加载定位库及 Mega Blocks 信息成功后， Studio 工具面板如图所示。
![加载后的Studio工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation06.png)
## 加载Block稠密模型
点击 Block 名称右侧的 加载 即可动态加载该 Block 的稠密模型。
![点击Block加载](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation07.png)
## 创建标注
在场景中按住 Ctrl （Windows） / Command （Mac） 键，然后在需要标注的地面上点击鼠标左键即可。
![创建标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple06.png)
## 将 3D 内容作为标注的子节点
将导入的模型拖到场景节点，作为标注的子节点。
![拖入模型](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple07.png)
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0**， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![修改模型Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
## [可选]调整模型位置
选择 **标注节点** 在场景中对着稠密模型调整模型的位置和旋转。
> **注意**
模型相对于标注的 Position 和 Rotation 必须始终全部为 **0** ，否则您无法在 xr-frame 上得到正确的渲染结果。
![修改标注节点Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple09.png)
## 新建标注数据包
点击 **Inspector** 面板中的标注数据包右侧的图标。
![添加标注数据](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation16.png)
在框中填入标注数据的名称，并点击右侧的勾。
![填入标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation17.png)
创建成功后应如图所示，之后点击下方的确定。
![确定创建标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation18.png)
点击上传图标进行上传。
![上传标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple13.png)
上传成功后弹出提示。
![成功提示](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation20.png)
## 确认标注数据
您需要记录标注数据的 **ID** 以在 xr-frame 上加载对应的标注数据。
![标注数据面板](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation21.png)
在上传成功后，您在云定位库中也可以看到相应的信息，这个页面中列表里的 ID 是 **标注数据包 ID**。
![云定位库中的标注信息](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple16.png)
此处也可以查看上传的标注数据名称和 ID，这个页面中列表里的 ID 是 **标注点 ID**。
![云定位库中的标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 后续步骤
* 使用上传的标注[完整运行示例工程](fullstart.html)
* 尝试[使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
## 相关主题
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
