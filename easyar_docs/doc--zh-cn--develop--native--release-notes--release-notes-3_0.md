---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-3_0.html
---

EasyAR Sense 3.0 发行说明 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR Sense 3.0 发行说明
## 3.0.1
2019-07-26
EasyAR SDK 3.0.1 修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> * 增加 Windows 上对摄像头的 YUY2 和 I420 像素格式的支持，减少出现黑屏的情况
>
> * 修正 Objective-C 示例中的 Renderer 的多个实例状态不独立，导致第二次进入时会在 glDrawArrays 处崩溃的问题
>
> * 增加对每通道 16 位的 png 图片的支持
>
> * 修正 Unity HelloAR_Coloring3D 示例在非 OpenGLES 和屏幕旋转等情况下贴图坐标出错的问题
>
> * 修正 Unity 示例默认不自动调焦的问题
>
> * 修正 Unity 示例中运行的一瞬间模型仍然显示，之后才消失的问题
>
> * 去除 Unity 示例初始化成功界面提示
>
> * 在 Unity 示例中增加对第二摄像头的支持(例如：在 Windows/Mac 上内置摄像头之外的 USB 摄像头)
>
> * 将 ExternalCamera 改名为 CustomCamera 以减少歧义
>
## 3.0.0
2019-07-07
EasyAR SDK 3.0 是 EasyAR SDK 2.x 的升级版。EasyAR SDK 3.0 有许多改进，主要集中在这几方面：
1. 更灵活的基于数据流的组件化 API
EasyAR 的 API 在 3.0 版本中，对原有 API 按照数据流进行了组件化的组织，使得 EasyAR 可以更容易与其他系统进行对接，以满足更为灵活的需求。
在此基础上，实现了外部摄像头接入和外部算法接入。
扩展 Camera 接口支持接收图片帧用于 AR 识别和跟踪。AR 展示将不依赖于手机自带摄像头，只要设备能够检测到外部摄像头并获取到视频流，就可以通过将视频流转成图片帧的方式传入 EasyAR SDK 用于 AR 应用，从而帮助 EasyAR 开发者为 AR/VR/MR 眼镜、无人机以及 USB 设备开发应用。
新的 API 支持开发者接入 EasyAR SDK 自有算法（ImageTracker 等）以外的其他算法，提供更灵活的能力扩展。
2. 编程语言和平台支持
增加了 C# for .Net/Mono 支持。
将 C++11 接口升级到 C++17，采用 std::optional 来明确参数和返回值的可空性。
将 Kotlin 和 Swift 接口升级到最新版本，并改善对 Optional 的支持。
增加了 Android ARM64 支持。
非 OpenGLES2 的渲染 API 支持(除 VideoPlayer 和 Recorder 以外实现渲染 API 中立)。
3. 表面跟踪
针对小型 AR 交互游戏、AR 短视频拍摄以及产品放置展示等应用场景，EasyAR SDK 3.0 增加 Surface Tracking 功能，使用检测任意表面特征点计算跟踪，不需要消耗时间寻找平面，实现更快速的表面贴合及姿态跟踪。
4. Image Target Data 生成
支持在原生及 Unity 应用中将待识别的图片提前生成一个数据包，用于识别跟踪，提高识别图加载速度。
5. 降低包体大小
通过架构的结构性改进和功能裁剪，减小了 SDK 的包体大小。
当前版本中去除了二维码扫描等冗余功能，以换取更小的包体。
6. 许多改进、bug 修复和兼容性提升
详细更新内容如下：
>
> ++ 更灵活的基于数据流的组件化 API
>
> ++ 表面跟踪
>
> + Image Target Data 生成
>
> + 编程语言支持：C# for .Net/Mono 支持
>
> + 编程语言支持：C++11 升级到 C++17
>
> + 编程语言支持：Kotlin/Swift 升级并支持 Optional
>
> + Unity 插件重写并开源，底层 API 与非 Unity 统一
>
> + Unity 插件涂涂乐示例新增截取静态图像绘制小熊的功能
>
> + Unity 插件新增 key 填错等 UI 提示
>
> + Android ARM64 支持
>
> + 非 OpenGLES2 的渲染 API 支持(除 VideoPlayer 和 Recorder 以外实现渲染 API 中立)
>
> + 外部摄像头接入
>
> + 外部算法接入
>
> + 降低包体大小
>
> - 二维码识别功能移除
>
> - 渲染器移除，改为提供各平台示例渲染代码
>
> * 支持从内存加载识别图
>
> * CloudRecognizer 支持 https(Android 和 iOS 上)
>
> * Android CameraDevice 增加对 Camera2 的支持
>
> * 修正 Android 9.0 上录屏崩溃的问题
>
> * 支持 Unity 5.6, 2017.4, 2018.4, 2019.1，去除对 5.6 以下版本的支持
>
> * 去除对 iOS 7 及以下版本的支持
>
> * Unity 插件使用 CommandBuffer 绘制相机背景
>
> * 修复了一些稳定性问题
>