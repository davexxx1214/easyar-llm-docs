---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_2.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-2_2.md
normalized_at: 2026-02-27
---
# EasyAR Sense 2.2 发行说明
## 2.2.1
2018-10-24
EasyAR SDK 2.2.1 修复了在 Android 8、iPhone XS/XS Max 以及 Unity 2018 上的一些兼容性问题。
详细更新内容如下：
>
> + 提升 EasyAR CRS 连接的安全性
>
> * 修复了在 Android 8 及新版本上 ARSceneTracker 停止时崩溃
>
> * 修复了在 Unity 2018 上使用 Android/iOS/Mac 发布黑屏
>
> * 修复了在 iPhone XS/XS Max 上的崩溃
>
## 2.2.0
2018-03-06
EasyAR SDK 2.2.0 对图像跟踪做了大幅改进。这个版本中 ImageTracker 变得更加稳定，跟踪不易丢失，同时姿态的抖动也有所减弱。算法默认将以最高质量模式运行，可以通过选择 ImageTracker 的不同模式来平衡跟踪运行效率和质量。
详细更新内容如下：
>
> + 优化图像跟踪算法
>
> + 添加 ImageTracker 模式选择的接口
>
> * 修复在 Java 接口中使用非 ASCII 字符造成的崩溃
>
> * 修复某些类型 PNG 图像在某些硬件下的加载和跟踪问题
>
> * 修复在使用多个 camera 实例的时候，某些情况下 camera 打开失败
>
> * 修复在经打开的 camera 在未关闭的情况下再次调用打开接口时崩溃
>
> * 修复录屏缩放模式无效
>
> * 修复在某些情况下录屏关闭时崩溃
>
