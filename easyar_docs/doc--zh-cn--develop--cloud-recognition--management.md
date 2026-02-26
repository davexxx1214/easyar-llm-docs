---
source: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management.html
---

目标图像管理 | EasyAR 文档
**
##### Table of Contents
**
# 目标图像管理
目标图像（Targets）可以通过以下两种方式进行管理：
* **可视化管理**：登录 EasyAR 开发中心进行手动维护。
* **API 自动化管理**：通过调用 **Web Service REST API** 集成到自有业务系统或管理后台中。
##### 重要事项
云识别服务中，目标图管理和图像识别是两个不同需求，API 对应两个不同的 Cloud URL 入口。
### 数据中心区域选择
图库运行示例所在的数据中心支持以下区域选择：
* **中国-上海**
* **美国-硅谷**
## 方法1：在 EasyAR 开发中心管理目标图
适用于小规模测试或手动快速上传。操作步骤如下：
1. 登录 EasyAR 开发中心，进入 **云识别管理**。
2. 选择目标区域。若尚未创建图库，请先新建并开通云识别图库。
3. 在图库列表中点击 **管理**，即可进入目标图维护界面进行上传、修改或删除。
## ![create-web](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-crs-manage.png)
## 方法2：使用 REST API 进行自动化管理
对于需要处理大量目标图的应用，推荐使用 Web Service REST API，以便在您的应用程序或管理后台中实现自动化流程。
### 准备清单
以下是待准备清单。在您开始管理目标图像之前，您需要准备一个新的云识别数据库实例（Cloud Database）
* CRS AppId
* [API Key](../apikey.html) / API Secret 或者 Token
* Cloud URL
* Server-end URL：目标图像管理 URL 地址，https 使用 443 端口
* Client-end URL：图像识别服务 URL 地址，https 使用 8443 端口
##### 重要事项
**端口区分说明**：目标管理 API 入口（443）与移动端/Unity 调用的云识别 API 入口（8443）是两个不同的通道，配置时请务必区分。
### 清单各项如何获取
* CRS AppId 查看方式：
开发中心 -&gt; 云识别管理 -&gt; 选择图库 -&gt; 管理 -&gt; 密钥
![m1-appid](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-crs-appid.png)
* API Key / API Secret 查看方式：
开发中心 -&gt; 云服务 APIKey -&gt; 复制
![m1-apikey](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-apikey.png)
如您还没有 API Key，创建 APIKey，必须选中云识别（CRS） 权限。进一步了解 API Key 以及权限控制，参考主题[API Key 简介](../apikey.html)
![m1-apikey-cr](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-apikey-create.png)
* Token 查看方式：
开发中心 -&gt; 云服务 APIKey -&gt; 管理 -&gt; 选择有效期 -&gt; 生成 Token -&gt; 复制
![m1-token](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-token.png)
若您需要自定义 Token 的有效期，可以参考 [UAC API —— 创建 Token](../apikey-auth.html) 方式，使用原始 APIKey 和 APISecret 来创建 Token
* Cloud URL 查看方式：
图库中目标图管理使用的是 Server-end URL 443 端口，Server-end URL
开发中心 -&gt; 云识别管理 -&gt; 选择图库 -&gt; 管理 -&gt; 密钥 -&gt; 图库管理
![m1-server-url](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-server-url.png)
### 多端集成指引
在实际工作流中，目标图管理通常集成在开发者的业务服务器里，或者移动端或者 Unity 里：
* 业务服务平台：提供有常用服务器开发语言（Curl/Java/NodeJS/PHP）调用 API 示例代码，帮助开发者实现目标图的自动上传与元数据（Meta）更新。
* 移动端（Unity/Mobile）：提供基于 Unity 的目标图管理示例代码，开发者自己实现拍照上传目标图的方式。
运行示例代码
下图是一个 Java 示例代码使用，在示例代码中填写您自己的准备清单的各项，然后运行 Main
![m1-java](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-java.png)
### 相关主题：
* [云识别 APIs 简介](../../api/cloud/cloud-recognition/apis.html)
* [API Key 介绍](../apikey.html)
**下一主题：**
* [图像识别难度评估](management-grading.html)
* [创建目标图像](management-adding.html)
##### 注意
实际工作流中，创建目标图像建议遵循最佳实现，建议认真阅读。