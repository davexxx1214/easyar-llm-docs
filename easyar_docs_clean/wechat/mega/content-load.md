---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-load.html
original_file: doc--zh-cn--develop--wechat--mega--content-load.md
normalized_at: 2026-02-27
---
# 如何在 xr-frame 运行时加载 AR 场景下的 3D 内容
本文详细阐述了 xr-frame 资源加载与节点挂载的分离机制，通过脚本动态实现 3D 内容在 Block 节点下的灵活挂载，实现 AR。
## 官方资料
* [xr-frame 开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)：微信官方 XR 引擎文档。
* [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)：包含各类基础与进阶用法示例。
官方资料中已经有充分的内容说明如何在运行时加载 3D 内容，本文中仅简要说明一些 AR 场景下常用的内容和加载方式。
## 资源加载 vs 节点挂载
在 xr-frame 中，显示一个 3D 模型分为两个阶段：
1. 资源加载：指将模型文件（如 `.glb` ）从网络或本地下载并解析到内存中。此时模型已就绪，但在场景中不可见。
2. 节点挂载：指在场景树中创建一个节点，并将已加载的资源关联到该节点上。此时模型才会正式出现在渲染画布中。
## 如何使用代码动态加载 3D 内容
1. 资源加载
通过 xr-frame 场景的资源管理系统调用 [loadAsset](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetsSystem.html#loadAsset)手动加载资源。
参数中的 `type` 指资源类型，`assetId` 指加载后的资源 id，`src` 指资源的 url，一般是资源托管服务器的地址。
需要记录 `assetId` 用于后续的挂载和释放资源。
```
try {
await scene.assets.loadAsset({type: 'gltf', assetId: 'panda', src: 'url/EasyARPanda.glb'});
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
```
2. 节点挂载
使用 `element.addChild()` 将加载好的模型放在 ShadowRoot 下。
```
const root = scene.getElementById("shadow-root");
let panda = scene.createElement(xrFrameSystem.XRGLTF,
{
"model": "panda",
"anim-autoplay": ""
}
);
root.addChild(panda);
```
ShadowRoot 元素是 xr-frame 专门用来防止动态创建和移除节点的根节点，详见 [Shadow节点](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/shadow.html)。
使用插件对象提供的 [createXRNodeFromNodeAnnotation](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_createXRNodeFromNodeAnnotation_member) 方法能够根据 EMA 数据创建 Block 的子节点，确保 3D 内容显示在正确的空间位置。
```
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
let panda = scene.createElement(xrFrameSystem.XRGLTF,
{
"model": "panda",
"anim-autoplay": ""
}
);
xrNode.addChild(panda);
```
## 如何在 Block 下不使用标注直接挂载内容
> **警告**
使用此方法的前提是，您已验证该 LocalTransform 的数值在 xr-frame 坐标系下能够实现预期的渲染效果。
除此以外的情况请[使用 Unity 编辑器的标注功能](content-annotation-creation.html)实现。
通过 [getBlockById(id)](../../../api/wechat/easyar.BlockHolder.html#w_easyar_BlockHolder_getBlockById_member_1_) 获取场景树上的 block 节点对象，如果不存在相应的 block 节点说明对这个 Block 的定位还未成功过（在第一次定位到该 Block 时节点会被自动创建）。可以用 [holdBlock(blockInfo, blockTransformInput)](../../../api/wechat/easyar.BlockHolder.html#w_easyar_BlockHolder_holdBlock_member_1_) 创建一个该 Block 的节点，也可以在定位回调中判断对该 Block 的定位成功再挂载内容。
> **提示**
在 Unity 编辑器的场景树中选择 **Block 节点** 记录它 **Inspector** 面板上显示的 **ID**
![Unity编辑器中的BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/content-load01.png)
也可以在云定位库页面中查到 **Block ID**
![定位库中的BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/content-load02.png)
```
const blockID = "aaaa1234-bbbb-cccc-dddd-eeeeee123456"
if (!blockHolder.getBlockById(blockParent.id)) {
// 没有存在的 Block 节点，创建一个
blockHolder.holdBlock({
id: blockID
})
}
let blockElement = blockHolder.getBlockById(blockParent.id).el;
```
将模型节点以挂载到指定的 Block 下，分别用 `position.setArray()`，`quaternion.set()` 和 `scale.setArray()` 把修改模型节点的 **LocalTransform** 。
```
export interface LocalTransform {
/\*\* @description 位置 \*/
position: xrfs.Vector3;
/\*\* @description 旋转 \*/
rotation: xrfs.Quaternion;
/\*\* @description Scale \*/
scale: xrfs.Vector3;
}
// 假设有一个已知的在 Block 下的 LocalTransform
const targetTransform: LocalTransform;
blockElement.addChild(modelNode);
let modelTransform = modelNode.getComponent(xrFrameSystem.Transform);
modelTransform.position.setArray([
targetTransform.position.x,
targetTransform.position.y,
targetTransform.position.z
]);
let annoRotation = new xrFrameSystem.Quaternion().setValue(
targetTransform.rotation.x,
targetTransform.rotation.y,
targetTransform.rotation.z,
targetTransform.rotation.w
);
modelTransform.quaternion.set(annoRotation);
modelTransform.scale.setArray([
targetTransform.scale.x,
targetTransform.scale.y,
targetTransform.scale.z
]);
```
## xr-frame 支持的资源类型
* Texture 纹理和图像
* CubeTexture 立方体纹理
* VideoTexture 视频纹理
* EnvData 环境
* GLTF 模型
* Keyframe 帧动画
* Atlas 图集
每种资源的加载方法详细见[微信官方文档](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render)及 [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)
> **注意**
支持的 GLTF 格式及拓展参考 [xr-frame 官方 GLTF 使用说明](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)
