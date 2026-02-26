---
source: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-android.html
---

运行 EasyAR Android 样例 | EasyAR 文档
**
##### Table of Contents
**
# 运行 EasyAR Android 样例
本文介绍如何运行 EasyAR 提供的原生 Android 样例。这里以 HelloAR 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下环境：
* Android Studio 2025.1.2 或更高版本
* JDK 17
* Android NDK r28
* Android 手机
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key，注意包名与样例一致，如 HelloAR 应为 `cn.easyar.samples.helloar`
## 导入并编译样例
1. 在 Android Studio 菜单依次选择 `File -&gt; New -&gt; Import Project...`，选择样例所在目录导入，等待 Android Studio 完成下载和配置。
![importhelloar](https://doc-asset.easyar.com/develop/native/getting-started/media/android-studio-import-hello-ar.png)
2. 设置许可证（License Key）
根据路径找到 ARActivity.java，按照代码提示填入开发中心获取的 License Key。
![fillkey](https://doc-asset.easyar.com/develop/native/getting-started/media/android_hello_ar_fill_in_key.png)
1. 编译并运行
连接手机到电脑上，点击运行按钮，按提示在手机上运行。
![buildandrun](https://doc-asset.easyar.com/develop/native/getting-started/media/android-build-run.png)
HelloAR 实现了对平面图像的识别跟踪并叠加虚拟物体的功能。样例中识别图像在 `assets/sightplus` 路径下找到。
HelloAR 样例的运行效果如下。
![rungif](https://doc-asset.easyar.com/develop/native/getting-started/media/android-helloar.gif)
## 相关阅读
* [运行 EasyAR iOS 样例](quickstart-ios.html)
* [运行 EasyAR Windows 样例](quickstart-windows.html)