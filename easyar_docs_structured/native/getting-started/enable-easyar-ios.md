---
source: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/enable-easyar-ios.html
original_file: doc--zh-cn--develop--native--getting-started--enable-easyar-ios.md
normalized_at: 2026-02-27
---
# 在 iOS 应用中启用 EasyAR 功能
本章介绍如何在 Xcode 中配置 EasyAR 的 iOS 工程 ， 而不需使用 Unity 等 3D 引擎。
## 准备工作
开始之前，您需要准备：
* Xcode 16 或更新版本
* 获取 EasyAR 授权许可证
* 选择 EasyAR Sense [发布版本并下载](variants.html)
## 使用 Objective-C 启用 EasyAR
1. 添加 Frameworks
在 `Frameworks, Libraries, and Embedded Content` 中添加 `easyar.xcframework`。
![addxframework1](https://doc-asset.easyar.com/develop/native/getting-started/media/xfframework.png)
2. 禁用 Bitcode
EasyAR 不使用 bitcode 也不提供 bitcode 兼容性, 需要在配置中禁用 bitcode。
![disablebitcode2](https://doc-asset.easyar.com/develop/native/getting-started/media/disablebitcode.png)
3. 初始化 EasyAR
使用 `easyar\_Engine` 的 `initialize:` 方法来初始化 EasyAR 。您可以添加初始化代码如下
```
[easyar\_Engine initialize:key];
```
4. 隐私配置
由于 AR 要使用摄像头，隐私配置需要添加 `Privacy - Camera Usage Description`，
![campermission](https://doc-asset.easyar.com/develop/native/getting-started/media/camerapermission.png)
如果要使用录屏功能，隐私配置需要添加 `Privacy - Microphone Usage Description`，
![microphonepermission](https://doc-asset.easyar.com/develop/native/getting-started/media/mcpermission.png)
## 通过 Swift API 启用 EasyAR
EasyAR Sense Swift API 是以源代码形式提供的，这样可以提供最好的兼容性（苹果从 Swift 5 开始提供 ABI 兼容）。
使用 EasyAR Sense Swift API 需要首先创建一个 framework 工程，然后将 framework target 嵌入到你的工程中。
### 创建 EasyARSwift framework 工程
1. 创建一个 Cocoa Touch Framework 类型的新工程并命名为 `EasyARSwift`
你可以选择将 EasyARSwift 工程嵌入到你的 app 工程里面或创建独立的工程。
![embedprj](https://doc-asset.easyar.com/develop/native/getting-started/media/embedproject.png)
2. 导入EasyAR Swift 代码到 EasyARSwift 工程
![embedswiftcode2](https://doc-asset.easyar.com/develop/native/getting-started/media/embedproject.png)
XCode 自动生成的 EasyARSwift.h 文件并没有被使用，可以安全删除。
3. 在 build settings 中配置 `Objective-C Bridging Header`
![bridgeheader](https://doc-asset.easyar.com/develop/native/getting-started/media/bridgingheader.png)
> **注意**
这个选项在导入 swift 文件之前不会显示在 XCode 选项中，所以请一定先导入 Swift 代码再进行配置更改。
4. 导入 `easyar.xcframework` 到 EasyARSwift 工程中
![addxframework3](https://doc-asset.easyar.com/develop/native/getting-started/media/xfframework.png)
5. 关闭 Bitcode
EasyAR 不使用 bitcode 也不提供 bitcode 兼容性, 需要保证在配置中禁用 bitcode。
![disablebitcode](https://doc-asset.easyar.com/develop/native/getting-started/media/disablebitcode.png)
6. Deployment Target
根据您的 app 工程修改 `deployment target`，保证 EasyARSwift 工程的 `deployment target`比 app 工程的小或相等。
![setdeploytarget](https://doc-asset.easyar.com/develop/native/getting-started/media/setdeploytarget.png)
### 嵌入和使用 EasyARSwift framework
1. 在工程中嵌入 EasyARSwift framework
![embedswiftfw](https://doc-asset.easyar.com/develop/native/getting-started/media/embedsffw.png)
![embedswiftfw2](https://doc-asset.easyar.com/develop/native/getting-started/media/embedsffw2.png)
2. 在 Swift 源代码中 `import EasyARSwift`
![importeasyswift](https://doc-asset.easyar.com/develop/native/getting-started/media/importeasyswift.png)
代码书写方式可以参考 `HelloARSwift` 样例中的代码或 API Reference 。
