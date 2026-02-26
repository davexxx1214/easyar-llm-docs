---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/transparent-video.html
---

在 xr-frame 微信小程序上播放透明视频 | EasyAR 文档
**
##### Table of Contents
**
# 在 xr-frame 微信小程序上播放透明视频
## 开始之前
* 准备需要播放的透明视频：将透明视频上传至文件服务器并获取用于在 xr-frame 中加载的 URL。
* 由于透明视频的播放依赖于替换场景中的贴图，需要事先标注播放透明视频的位置。
需要能够[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
## 什么是透明视频
**透明视频** 是一种为了在不原生支持透明通道的视频编码格式（如 H.264/AVC， H.265/HEVC） 中实现透明背景效果的技术方案。
该方案通过将视频画面的**颜色信息 （RGB）** 和**透明度信息 （Alpha）** 拆分，并按照特定的空间布局拼接到同一帧图像中，从而生成一个带有黑白遮罩的普通视频文件。在播放端，通过图形渲染管线实时采样并将两部分合成，还原出具有透明背景的动态画面。
根据颜色区域与 Alpha 区域的拼接方式，主要分为两种格式：
1. Side-by-Side （SBS）
Side-by-Side 是一种将 RGB 颜色帧与 Alpha 遮罩帧在**水平方向**上并排拼接的格式。通常约定左侧为颜色区域，右侧为对应的灰度 Alpha 区域。
2. Top-by-Bottom （TBB）
Top-by-Bottom 是一种将 RGB 颜色帧与 Alpha 遮罩帧在**垂直方向**上堆叠拼接的格式。通常约定上半部分为颜色区域，下半部分为对应的灰度 Alpha 区域。
## 在 xr-frame 小程序上标注位置播放透明视频
首先加载类型为 `video-texture` 的视频资源。
```
`async loadAsset() {
const videoTexture = {
assetId: "fireball",
type: "video-texture",
// 视频资源 URL
src: "url/video-resource.mp4",
options: {
autoPlay: true,
loop: true,
}
};
try {
// 加载 video-texture 类型资源
await scene.assets.loadAsset(videoTexture);
} catch (err) {
console.error(`Failed to load video texture: ${err.message}`);
}
}
`
```
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRMesh,{})` 创建简单的几何体赋予 `easyar-video-tsbs` 材质， 并修改 `uniform` 为 `u\_baseColorMap:video-{$assetId}`。
##### 注意
`easyar-video-tsbs` 和 `easyar-video-ttbb` 材质的加载，注册，反注册，卸载由 AR Session 控制。
```
`handleEmaResult(ema: easyar.ema.v0\_5.Ema) {
const blockHolder: easyar.BlockHolder = session.blockHolder;
ema.blocks.forEach(emaBlock =&gt; {
const blockInfo: easyar.BlockInfo = {
id: emaBlock.id
};
// 若 Block 节点不存在，创建 Block 节点
blockHolder.holdBlock(blockInfo, easyarPlugin.toXRFrame(emaBlock.transform));
});
ema.annotations.forEach(annotation =&gt; {
if (annotation.type !== mega.EmaV05AnnotationType.Node) {
return;
}
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
const assetInfo = AnnotationMetaData[nodeAnnotation.id as keyof typeof AnnotationMetaData];
let model: xrfs.Element;
if (assetInfo) {
// GLTF 部分
} else {
// 利用内置 Mesh 创建用于渲染的几何体
model = scene.createElement(xrFrameSystem.XRMesh, {
geometry: "cube",
material: "easyar-video-tsbs",
uniforms: "u\_baseColorMap:video-fireball",
});
xrNode.addChild(model);
}
});
}
`
```
##### 注意
在使用 `video-texture` 时，若控制台出现 `wx.createVideoDecoder with type: 'wemedia' is deprecated` 警告，请忽略。
经与微信官方团队确认，该警告不影响使用。
## 后续步骤
* [完整运行示例工程](fullstart.html)
* [示例工程说明](sample.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)