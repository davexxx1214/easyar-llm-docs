---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_3.html
original_file: doc--zh-cn--develop--native--release-notes--release-notes-1_3.md
normalized_at: 2026-02-27
---
# EasyAR Sense 1.3 发行说明
## 1.3.1
2016-07-29
EasyAR 1.3.1 主要修复了某些 Android 设备的兼容性问题，并增加了中文路径（json 文件和图像路径）支持。
自 EasyAR 1.3.0 版本开始的详细更新内容如下。
>
> + 添加中文路径支持
>
> + 添加 json 文件中对"meta"数据的支持
>
> * 修正 UTF-8-BOM 编码的 json 文件解析
>
> * 修正在某些 Android 设备（Nexus 5s/6）上的 camera 显示问题
>
## 1.3.0
2016-05-28
EasyAR 1.3.0 增加了一些新特性并有很多改进，主要集中在这几方面：
1. 支持多目标。
EasyAR 现在可以支持同时跟踪多个目标。可以使用一个 tracker 进行多目标同时跟踪，也可以在不同 tracker 中加载不同的 target 来同时跟踪。EasyAR 支持运行时动态修改最大跟踪目标个数。更多使用细节请参考 [EasyAR Multi-Target](../../image-tracking/intro.html) 。
2. 接口修改，使用更加灵活。
这个版本和之前版本相比，一部分接口有所调整，但整体框架没有太大的变动。你现在可以像搭积木一样使用 EasyAR 的 Unity 基础 prefab，这个版本中也添加了很多预先搭好的模块以供参考。
3. 优化检测和跟踪，减少抖动。
4. 性能优化和降低功耗。
详细更新内容如下：
>
> + 添加多目标支持
>
> + 添加多目标的典型样例
>
> + 添加同时跟踪目标和识别二维码的样例
>
> + 提升检测和跟踪效果，减少抖动
>
> + 优化算法降低功耗
>
> + 添加直接画到 texture 的接口
>
> + 添加显式水平翻转相机输入的接口
>
> + 添加禁止 Android 自动旋转检测的接口
>
> + 添加设置外部旋转的接口
>
> + Unity: 优化渲染效率
>
> + Unity: 添加多个组合了基础 prefab 的常用 prefab
>
> + Unity: 添加 EasyARBehaviour，用以输入 key 并进行初始化，并显式处理 pause/resume/quit 事件
>
> + Unity: 添加显示/隐藏 RealityPlane 的选项
>
> + Unity: 添加使用索引打开 camera 的接口
>
> + Unity: 添加对自定义硬件设置旋转偏移的接口
>
> + Unity: 修改 AugmentedTarget 接口，支持在 FrameUpdate 事件中进行自定义的姿态滤波
>
> + Unity: 修改 Target 事件处理接口
>
> * 调整部分接口
>
> * 修正切换场景时的内存泄漏
>
> * 修正在暂停并恢复之后找到虚假的目标
>
> * 修正使用透明 PNG 图像的 target 检测
>
> * 修正因 key 中的空格导致的初始化失败
>
> * 修正 iOS 和 mac 某些分辨率下 camera 显示错误
>
> * 修正 native iOS 样例在切换到后台时崩溃
>
> * Unity: 修正在图像高比宽大的时候 ImageTarget mesh 显示错误
>
> * Unity: 修正在 OnFound 事件中重置 target
>
> * Unity: 修正 camera 打开之后有可能出现的白色帧
>
> * Unity: 修正 Augmenter 中心模式下的 TargetOnTheFly 和 Coloring3D 样例
>
> * Unity: 修正 TargetOnTheFly 样例在某些情况下崩溃的问题
>
