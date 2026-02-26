---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/setup-xreal.html
---

XREAL 工程配置方法 | EasyAR 文档
**
##### Table of Contents
**
# XREAL 工程配置方法
本章介绍如何配置 Unity 工程使其在 XREAL 头显上使用 EasyAR 的相关功能。
## 准备工作
* 获取适合 XR 头显或者眼镜的 EasyAR 许可证，头显或眼镜可用 License 类型包括
* EasyAR Sense 4.x **XR License 试用版**（试用，在 EasyAR 网站自主开通）
* EasyAR Sense 4.x **XR License 正式版**（付费后使用，请联系商务购买开通）
* EasyAR Sense 4.x **XR License 企业版**（企业版 SDK 使用）
其他许可证均不支持。
* 请通过商务获取 **XREAL** 的企业 License （注意，这个 License 是 XREAL 公司分发的文件，与 EasyAR 的 License 不同）。
* 下载并导入 [XREAL 的 SDK](https://developer.xreal.com/download)
* 下载并导入[EasyAR Unity 插件包](https://www.easyar.cn/view/download.html)
* 下载并导入 [EasyAR Unity XR设备扩展包](https://www.easyar.cn/view/download.html)
* 参考 [Android 工程配置](../fundamentals/setup-player.html)
##### 注意
当前仅支持 XREAL SDK &gt;= 3.1
## 启用 XREAL 插件
1. 在 `Project Settings &gt; XR Plug-in Management &gt; XREAL` 中勾选 `Enable Native Session Manager`
![enablenativesession](https://doc-asset.easyar.com/develop/unity/headsets/media/xreal-enable-sdk-manager.png)
2. 在 `Project Settings &gt; XR Plug-in Management &gt; XREAL` 中配置 `License Asset` 为 XREAL 的企业许可证
![addxreallicense](https://doc-asset.easyar.com/develop/unity/headsets/media/xreal-add-license.png)
##### 注意
在 XREAL 上， 如果 `Frame Recorder` 的 `Format` 为 `Auto` 或 `H264` ，录制的数据质量被有意降低，Mega 的成功率和准确度都有不同程度的降低，因此其在电脑上的运行效果仅作为参考。
##### 注意
如需向 EasyAR 反馈问题数据，请设置 ARSession 上的 `Frame Recorder` 的 `Format` 为 `Obsolete` 进行录制，注意录制完成必须调用停止（设置 `enabled` 为 `false`）否则无法使用。这样录制出来的数据在 Unity 中使用会显示数据加密无法播放，这是正常的。