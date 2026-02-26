---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/fullstart.html
---

完整运行微信小程序 Mega 插件示例工程 | EasyAR 文档
**
##### Table of Contents
**
# 完整运行微信小程序 Mega 插件示例工程
这篇文章将介绍如何完整运行微信小程序 Mega 插件的示例项目（包含标注的使用）。
## 开始之前
* 完成[快速运行示例工程](quickstart.html)。
* 完成[使用 Unity 上的 Mega Studio 摆放 3D 内容](content-simple.html)，获取**标注数据包 ID 和标注点 ID**。
**[Block 云定位]** &gt; **[标注数据]** 在云定位库列表里的 ID 是 **标注数据包 ID**。
![云定位库中的标注信息](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple16.png)
点击右侧 **[查看]** 可以查看上传的标注数据名称和 ID，这个页面中列表里的 ID 是 **标注点 ID**。
![云定位库中的标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 配置 Mega 标注数据包 ID
在 `miniprogram/components/sample-data/easyar-settings.ts` 中填入标注数据包 ID：
```
`/\*\* 填 Mega 标注数据包 ID \*/
export const MegaAnnotationId: string = "";
`
```
## 配置标注点要展示的模型
在 `miniprogram/components/sample-data/annotation-metadata.ts` 中通过将 `key` 改成标注点 id 配置要替换的标注，如果要替换多个则用逗号隔开。
```
`export const AnnotationMetaData: Record&lt;string, any&gt; = {
/\*\* 填标注点 ID \*/
"aaaaaaaa-bbbb-cccc-dddd-123456789012": {
assetId: "panda",
scale: "1 1 1"
},
"aaaaaaaa-bbbb-cccc-dddd-123456789013": {
assetId: "panda",
scale: "1 1 1"
}
};
`
```
>
> 关于如何记录和对应标注点 ID 可以参考
[> 确认标注数据
](content-simple.html#wechat-mega-content-simple-save-annotation-id)> 。
>
## 实机运行
1. 点击小程序开发工具上方栏的实机预览按钮，通过扫描二维码加载。
##### 注意
不能在开发工具上直接模拟运行带有 AR 功能的 xr-frame 组件。
![二维码加载](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart06.png)
2. 点击 **EasyAR Mega Samples** 进入示例项目的 AR 场景。
![Sample入口](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart08.png)
3. 屏幕中提示 `EasyAR Session is initializing` 表示微信平面检测正在初始化。
##### 提示
确保在光线充足的环境下测试，避开大面积纯色墙面或纯色地板。
对着地面或其他平面匀速左右摆动以加快这个过程。
![初始化](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart09.png)
4. 初始化完成后，将手机竖直使相机拍到正常的现实画面，当定位成功， debug 信息中出现 `Found` 字样，并且右下方的状态指示物变为绿色。
![定位](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart10.png)
5. 将在标注的位置加载并渲染 GLTF 模型或方块（取决于是否配置了 `assetId`）。
运行效果：
## 相关主题
* [Mega 简介](../../mega/intro.html)
* [获取和使用 APIKey](../../apikey-auth.html)
* [开始开发之前](../../mega/localization-verify.html)
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [示例说明](sample.html)