---
source: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-ios.html
original_file: doc--zh-cn--develop--native--getting-started--quickstart-ios.md
normalized_at: 2026-02-27
---
# 运行 EasyAR 的 iOS 样例
本文介绍如何运行 EasyAR 提供的原生 iOS 样例。这里以 HelloAR 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下环境：
* Xcode 16 或更高版本
* ARM64 CPU 的 iPhone 或 iPad 真机
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key，注意包名与样例一致，如 HelloAR 为 `cn.easyar.samples.helloar`
## 导入并编译样例
1. 使用 Xcode 打开下载解压的样例，如 `helloar.xcodeproj`
![openiossample](https://doc-asset.easyar.com/develop/native/getting-started/media/openiossample.png)
2. 设置许可证（License Key）
根据路径找到 `ViewController.m`，按照代码提示填入开发中心获取的 License Key。
![xcodefillkey](https://doc-asset.easyar.com/develop/native/getting-started/media/ios-fill-key.png)
3. 编译并运行
连接手机到电脑上，点击运行按钮，按提示在 iPhone /iPad 上运行样例。
HelloAR 实现了对平面图像的识别跟踪并叠加虚拟物体的功能，摄像头对准识别图（在 `assets` 文件夹下也可以找到）即可体验效果。
![namecard](https://doc-asset.easyar.com/develop/unity/headsets/media/namecard.jpg)
## 相关阅读
* [运行 EasyAR 安卓样例](quickstart-android.html)
* [运行 EasyAR Windows 样例](quickstart-windows.html)
