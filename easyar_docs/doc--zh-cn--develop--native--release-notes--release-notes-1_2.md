---
source: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_2.html
---

EasyAR Sense 1.2 发行说明 | EasyAR 文档
**
##### Table of Contents
**
# EasyAR Sense 1.2 发行说明
## 1.2.1
2016-02-19
EasyAR 1.2.1 主要修复了 1.2.0 的一个使用问题，同时对跟踪算法做了一部分优化。这个问题只有在不正确的设置了 target 的 size 的时候才会出现，这个版本将可以容许这样的输入。
自 EasyAR 1.2.0 版本开始的详细更新内容如下。
>
> * 修正当输入 size 比例不正确的时候的闪烁和难以识别问题
>
> * 优化跟踪算法
>
## 1.2.0
2016-02-05
EasyAR 1.2.0 有两个使用体验上的显著改进。
1. 跟踪稳定性大幅提升，跟踪过程更加准确和鲁棒。
2. Unity3D 用户将不再需要在 Windows 系统中安装 Visual C++ 2015 RedistributablePackage。很多 Windows8.1 的用户将从中受益。
自 EasyAR 1.1.0 版本开始的详细更新内容如下。
>
> + 大幅提升跟踪稳定性和准确性
>
> + Unity: 移除 Visual C++运行时库依赖
>
> + Unity: 添加对 Unity 5.3+ OpenGLCore 的支持
>
> + Unity: 添加更多针对首次使用的引导
>
> + Unity: 添加关闭显示视频不支持信息的选项
>
> * 修正某些情况下 iOS 视频播放黑屏
>
> * 修正某些 Android 设备视频播放不正常
>
> * Unity: 微调整某些接口
>
> * Unity: 修正 invalid aabb
>
> * Unity: 修正 Unity 5 使用 prefab 创建场景灰屏
>
> * Unity: 修正 postbuild 脚本对 Unity 4.7 的兼容性
>
> * 其它修正和完善
>
> * 在发布包中添加一个 Unity 样例
>