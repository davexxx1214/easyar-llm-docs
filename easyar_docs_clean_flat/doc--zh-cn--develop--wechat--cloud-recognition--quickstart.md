---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/quickstart.html
original_file: doc--zh-cn--develop--wechat--cloud-recognition--quickstart.md
normalized_at: 2026-02-27
---
# 图像云识别微信小程序开发快速入门
本篇将带大家快速开发微信小程序上基于 EasyAR 图像云识别的 AR 应用，通过本文介绍，开发者可以掌握如何在微信小程序环境中集成 EasyAR 的云识别能力，并利用 XR-FRAME 框架构建交互式 AR 体验。
## 开发准备
1. [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。
2. 获取 “AppID(小程序ID)”，如果没有，请注册[微信公众平台账号](https://mp.weixin.qq.com/)或[申请测试账号](https://developers.weixin.qq.com/miniprogram/dev/devtools/sandbox.html)。
3. 微信开发者工具[下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。
4. 支持云识别的 [API Key](../../apikey-auth.html)。
5. 运行中的[云识别库](../../cloud-recognition/management.html)。
## 上传云识别图片
准备一张识别图片，并上传到云识别库，上传方法参考 [图库管理](../../cloud-recognition/management-adding.html)。
## 下载 Sample
在 [EasyAR 下载页面](https://www.easyar.cn/view/download.html)下载 “EasyAR CRS 微信小程序Sample”。
![crs-wx](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-dl-1.jpg)
## 配置 sample
* 将下载的 “EasyAR-miniprogram-WebAR-Demo-tracking.zip”，解压到你的目录。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-21.png)
* 导入微信开发者工具。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-22.jpg)
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-23.jpg)
* 在“详情”下的“本地设置”中勾选“不检验合法域名、web-view（业务域名）、TLS版本以及HTTPS证书”。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-24.jpg)
* “微信开发者工具”中的预览效果。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-25.jpg)
* sample 代码中已预留配置项，请根据实际环境进行配置。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-26.jpg)
## 效果预览
* 在“微信开发者工具”上点击“预览”。
* 选择“启动手机端自动预览”。
* 点击“编译并预览”
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-27.jpg)
> **提示**
不要使用“真机调试”。
* 在手机上的运行效果。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-1.jpg)
* 如果你未将域名添加到合法请求列表中，请开启“开发调试”。打开方法如下：
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-2.jpg)
* 如果是首次运行，点击“允许”授权摄像头访问权限。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-3.jpg)
* 点击预览页面中的“云识别功能”。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-5.jpg)
* 将手机摄像头对准您上传的识别图片，点击“点击识别”，如果识别到目标，则会弹出识别目标的名称。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-4.jpg)
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)
