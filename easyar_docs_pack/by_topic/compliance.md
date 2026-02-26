# EasyAR 专题包：compliance

适用于上下文长度有限时的分卷输入。

## 目录
- `compliance/data-access.md`
- `compliance/guide.md`
- `compliance/intro.md`

---

## EasyAR Sense 数据访问
- 章节路径: `compliance/data-access.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/compliance/data-access.html

# EasyAR Sense 数据访问
介绍 EasyAR Sense 中可能的数据访问。
## 数据访问情况列表

> **注意** 自动修复提示：该表格在抓取阶段已损坏，以下保留原始表格流供人工核对。

```text
|
功能
|
数据
|
使用类型
|
使用目的
|
传输加密
|
短暂使用
|
备注
|
|
基本
|
iOS: identifierForVendor
“设备-开发商”标识
|
访问/传输
|
统计分析
|
使用 TLS
|
否
||
|
设备型号、制造商、品牌、操作系统版本
|
访问/传输
|
统计分析
|
使用 TLS
|
否
||
|
设备型号、制造商、品牌、操作系统版本
|
访问
|
软件功能
|
不适用
|
不适用
|
用于选择软件实现，如在 CameraDeviceSelector、ARCoreCameraDevice、MotionTrackerCameraDevice 中
|
|
SDK 功能调用记录
|
访问/传输
|
统计分析
|
使用 TLS
|
否
||
|
平面图像跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
视频播放
|
开发者指定视频文件
|
访问
|
软件功能
|
不适用
|
不适用
||
|
云识别
|
相机图像
|
访问/传输
|
软件功能
|
根据调用方式可能不加密，也可能使用 TLS
|
是
||
|
3D 物体跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
录屏
|
屏幕图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
表面跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
运动传感器读数
|
访问
|
软件功能
|
不适用
|
不适用
||
|
稀疏空间地图
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
稀疏空间地图数据
|
访问/传输/分享
|
软件功能
|
使用 TLS
|
否
|
不包含图像，但包含从图像计算得到的衍生数据
可以通过管理页面或 WebAPI 删除
根据调用方式可以分享给其他最终用户
|
|
预览图像(可选)
|
访问/传输
|
软件功能
|
使用 TLS
|
否
|
可以通过管理页面或 WebAPI 删除
|
|
稠密空间地图
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
运动跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
运动传感器读数
|
访问
|
软件功能
|
不适用
|
不适用
||
|
Mega/云定位
|
相机图像
|
访问/传输
|
软件功能
|
根据调用方式可能不加密，也可能使用 TLS
|
是
||
|
位置信息(可选，根据调用情况决定为大致位置还是确切位置)
|
访问/传输
|
软件功能
|
根据调用方式可能不加密，也可能使用 TLS
|
是
||
```

注：
“访问”指在客户端获得数据。“传输”指将数据从客户端发送到 EasyAR 的服务器。“分享”指将数据从客户端发送到第三方设备。
“短暂使用”是指服务器处理请求之后不会保存此项数据。

---

## EasyAR Sense 合规指南
- 章节路径: `compliance/guide.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/compliance/guide.html

# EasyAR Sense 合规指南
欢迎您使用 EasyAR 平台（以下简称“本平台”或者“我们”），为完善您在本平台上的使用体验，并协助您在合法合规的前提下推进您的项目建设，我们根据中华人民共和国的法律、法规之规定制定本《合规指南》（以下简称“本指南”），以便您明确您在向最终用户提供产品或服务时可能涉及的义务与责任，最大程度避免违法违规。
请您注意，由于应用服务器所在区域、应用发布服务器所在的区域、用户所在的区域可能并不位于中华人民共和国境内或者位于不同的地区或国家，您提供产品或服务将适用并满足对应地区或国家的法律、法规、规则，承担适用法律项下应用开发者、数据处理者的责任。
请您合理参考本指南的内容，作为您合规向最终用户提供产品或服务的指引。
## 隐私政策
在您向最终用户提供产品或服务的过程中，如果您将自行或委托第三人收集、存储、处理最终用户的个人信息的，请您依照适用的法律、法规之规定制定《隐私政策》、《数据处理协议》或者相关书面协议以保护用户的个人信息安全以及您的权利。请您务必在初始化 EasyAR Sense 之前，向最终用户书面提示并充分告知收集其个人信息的范围、方式与目的。您可以参考以下的条文：
>
> 我们的产品集成 EasyAR Sense，可能会收集您的
> identifierForVendor(iOS)、设备型号、制造商、品牌、操作系统版本、SDK 功能调用记录
> 以进行统计分析、改进产品和服务，可能会获取您的
> 相机图像、运动传感器读数
> 以实现软件功能。
>
请您务必阅读并确认 [数据访问](data-access.html) ，并根据您提供产品或服务中对相关数据的实际使用情况，调整上述条文的内容。
为落实信息处理主体的法律责任要求，根据您实际提供产品或服务的情况，还请您进一步明确产品或服务功能所需使用的具体数据或信息，且仅在正当、合理、透明、必要原则的指引下收集相关个人信息。您知悉，如果由于您违反法律法规之规定，或者未告知或未完整告知最终用户关于您收集个人信息的使用规则、范围、方式与目的而导致相关权利主体、权力机关对我们的投诉、诉讼、处罚以及相关责任与后果，均由您承担。
## 数据安全表格
应用发布平台可能会要求填写数据安全表格披露数据访问、收集情况，如果适用，请务必阅读 [数据访问](data-access.html) ，根据应用的使用情况，填写应用发布平台的表格。
* Android
在应用发布到 Play Store 时会需要填写 Google 的数据安全表格，参考 [这里](https://support.google.com/googleplay/android-developer/answer/10787469) 。
* iOS
在应用发布到 Apple App Store 时会需要填写 Apple 的应用隐私表格，参考 [这里](https://developer.apple.com/app-store/app-privacy-details/) 。
## 与儿童相关的要求
法律、法规、规则或应用发布平台可能会对面向儿童的应用有特殊要求。如果适用，请务必满足这些特殊要求，包括但不限于展示年龄验证弹窗。
* Android
在应用发布到 Play Store 时的要求，参考 [这里](https://support.google.com/googleplay/android-developer/answer/9893335) 。
* iOS
在应用发布到 Apple App Store 时的要求，参考 [这里](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions/) 。
## 其他可能的问题
如果应用使用到其他工具或 SDK，请访问对应的官方网站查看其合规指南。
例如，Unity SDK 的指南可参考如下文档 [中国大陆](https://unity.cn/legal/privacy-policy) [其他国家和地区](https://unity.com/legal/privacy-policy) 。

---

## 合规
- 章节路径: `compliance/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/compliance/intro.html

# 合规
本章主要介绍使用 EasyAR Sense 的合规指南，并提供可能访问的数据列表。为了避免因权限过度申请或隐私声明缺失导致的合规风险（如应用下架等），在使用 EasyAR Sense 和 EasyAR Sense Unity Plugin 开发应用，并提交到应用商店上架之前，请务必确认 [EasyAR Sense 合规指南](guide.html) 和 [EasyAR Sense 数据访问](data-access.html)。
