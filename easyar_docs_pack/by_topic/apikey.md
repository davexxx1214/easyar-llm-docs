# EasyAR 专题包：apikey

适用于上下文长度有限时的分卷输入。

## 目录
- `apikey.md`

---

## EasyAR 云服务 API Key 统一认证
- 章节路径: `apikey.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/apikey.html

# EasyAR 云服务 API Key 统一认证
API Key 通过统一的身份认证机制，实现对所有 EasyAR 云服务 API 的集中访问管理，简化开发流程，提升安全性和易用性，从而显著降低开发者在服务接入、权限控制和维护管理等方面的成本与复杂度。
## 什么是 API Key
API Key（Application Programming Interface Key）即应用程序编程接口密钥，是一串由数字、字母或特殊字符组成的唯一识别码。主要作用是让您的应用或服务在调用 EasyAR API 时，证明自己的合法身份，由 EasyAR 平台生成并分配给您使用。
## 什么是 Token
在 API 访问认证中，Token 是一种临时的、加密的身份凭证，由服务端在用户或应用完成身份验证后生成，它相当于 API 调用的 “身份凭证”，用于您的应用或服务与 EasyAR API 服务之间建立通信时，验证是否有合法身份，同时根据 Token 绑定的权限，判断其是否能访问目标接口或数据。
## 使用 API Key / Token 的云服务
在 EasyAR 云服务中，API Key / Token 可用于访问以下服务：
* [云识别](cloud-recognition/intro.html)
* [稀疏空间地图](sparse-spatial-mapping/intro.html)
* [Mega Block 云定位](mega/intro.html)
## 相关主题
* [获取 API Key](apikey-auth.html#api-key)
* [获取 Token](apikey-auth.html#api-token)
