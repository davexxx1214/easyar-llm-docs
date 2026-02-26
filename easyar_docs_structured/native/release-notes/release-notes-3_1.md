---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-3_1.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-3_1.md
normalized_at: 2026-02-27
---
# EasyAR Sense 3.1 发行说明
## 3.1.0
2020-01-14
EasyAR Sense 3.1.0 从 4.0.0 中反向移植了许多设计优化和问题修复。
EasyAR Sense Unity 插件也更新到新版本，有了巨大提升。
详细更新内容如下：
EasyAR Sense
>
> + CameraDevice 增加了获得 camera 数量、索引，获得 camera 前后位置的功能（Mac 不支持）和以指定前后位置打开 camera 的功能
>
> + 增加了各组件汇报占用的 camera buffer 需求的功能，用于 CameraDevice.setBufferCapacity
>
> * 编程语言支持：Swift 升级到 Swift 5
>
> * 不再区分 Basic 和 Pro 二进制包
>
> * CloundRecognitionService 从使用 AppKey 改为使用 ApiKey
>
> * 修正 iOS 上只能使用有限种类分辨率的问题，使得 iPad 上能够使用最大视野
>
> * 修正部分 iPad 设备上 camera 分辨率较高时会崩溃的问题
>
> * 修正 Google Play Store Android App Bundle 支持
>
> * 修正 ImageTracker.unloadTarget 和 ObjectTracker.unloadTarget 无法卸载 target 的问题
>
> * 修复了一些稳定性问题
>
Unity Plugin for EasyAR Sense 3.1.0
>
> ++ 恢复类似 Sense 2.3 的接口设计和行为，并有非常多改进
>
> + 添加严重出错情况的弹出消息（可在 EasyARController 上关闭）
>
> + Components: 大多数组件可以使用 Unity 组件的 enabled 来控制 start/stop
>
> + Component ARSenssion: AR 入口，控制 center mode，具备支持外部设备的能力，比如自定义相机及 AR 眼镜
>
> + Component ARAssembly: 展示 EasyAR Sense 组件化 API 的组装过程，支持所有 EasyAR Sense 的组件
>
> + Component ImageTargetController: 改善对不同类型输入的支持，可以从本地文件系统或 web URL 加载图像和.etd 文件
>
> + Component CameraImageRenderer: camera 图像渲染可由 disable 该组件来关闭
>
> + Scene: 添加 target gizmo，可在 Unity 编辑器中显示 target 细节
>
> + Asset: 添加全局服务配置及 gizmo 控制选项
>
> + Window: 添加生成 image target data（.etd 文件）的窗口
>
> + Window: 添加菜单跳转到 license key 设置界面和其他全局配置
>
> * 修复目标跟踪存在一帧延迟的问题
>
> * 修复阻塞式 target 加载，减少 target 加载时间
>
> * 修复 target size 获取
>
> * 许多其他改进及 bug 修复
>
Samples of Unity Plugin for EasyAR Sense 3.1.0
>
> ++ 添加回所有 Sense 2.3 的 sample
>
> + 添加 sample 启动器，可以通过启动器加载所有 samples
>
> + 添加屏幕上显示的组件状态信息，覆盖所有 sample
>
> + 添加展示 AR 眼镜支持的 sample
>
> + 添加表面跟踪与图像跟踪同时使用的 sample
>
> + 添加获取 camera 图像贴图和控制 camera 显示的 sample
>
> + 添加修改视频 aspect ratio （Unity VideoPlayer 功能） 适配 image target 的 sample
>
> + 添加展示从图像扩展跟踪的 sample
>
> + 云识别 sample 现在使用本地缓存，并在跟踪状态下停止云端识别，以覆盖常见的使用场景
>
> + 优化 coloring3D sample，修复 bug
>
