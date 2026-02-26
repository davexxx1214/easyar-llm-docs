---
source: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-windows.html
---

运行 EasyAR Windows 样例 | EasyAR 文档
**
##### Table of Contents
**
# 运行 EasyAR Windows 样例
本文介绍如何运行 EasyAR 提供的原生 Windows 样例。这里以 HelloARQt 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下内容
* Visual Studio 2022 或更高版本 (有 `.vcxproj` 工程的样例)
* CMake 3.8 或更高版本 (有 `CMakeLists.txt` 的样例)
* Qt 5.4 或更高版本 (Qt 样例)
* (USB) 摄像头，插入状态并可以正常工作。
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key
##### 注意
请确保 Visual Studio 的 C++ 支持库已经安装，这些在 Visual Studio 的默认安装情况下不会自动安装。
## 编译运行 EasyAR 的 Windows 的样例
以下以 HelloARQt 为例介绍如何编译运行 EasyAR 官方 Windows 的样例。
1. 打开 CMake，指定 `where is the source code` 目录为下载解压的样例目录，设置 binary 文件的路径。
2. 点击 `Configure`, 在弹出的窗口中，选择系统的 Visual Studio 版本。如果某些路径（如 Qt）没有自动设置报错，需要手动修改，重新 `Configure`，直至没有错误。
![sample1](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample1.png)
3. 点击 `Generate`，生成工程文件。
![sample2](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample2.png)
4. 点击 `Open Project`，在 Visual Studio 中打开工程。
![sample3](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample3.png)
5. 在 Visual Studio 点击运行，在运行窗口的输入框里填写官网获取的 License Key，点击 `Start` 运行样例。
![sample4](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample4.png)
## 常见问题
1. 如果运行时提示找不到 Qt，解决方案是添加 Qt 路径到 PATH 环境变量，注销并重新登录计算机。
2. 上面介绍的 HelloARQt 是**运行时**输入 License Key ，但是也有样例需要在**运行前**填写许可证，通常在 `initialize` 代码处，如 HelloAR 样例的 License 在 `main.cc` 中填写。
![sample5](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample5.png)
## 相关阅读
* [运行 EasyAR 安卓样例](quickstart-android.html)
* [运行 EasyAR iOS 样例](quickstart-ios.html)