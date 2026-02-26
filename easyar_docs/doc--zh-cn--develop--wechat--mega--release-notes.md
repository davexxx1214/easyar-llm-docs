---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/release-notes.html
original_file: doc--zh-cn--develop--wechat--mega--release-notes.md
normalized_at: 2026-02-27
---
# EasyAR Mega 微信小程序插件发布日志
本页面记录了 EasyAR Mega 微信小程序插件各个版本的发布日志。
> **重要事项**
**版本维护及升级建议**
* **2.0.0 及以上版本**：建议所有用户升级至 [最新版本 (2.0.2)](#mega-wechat-miniprogram-plugin-v202) 以获得最佳稳定性。
* **2.0.0 以下版本**：已完全重构并不再维护，请迁移至新版本。
## 快速导航
* [🚀 最新版本 (2.0.2)](#mega-wechat-miniprogram-plugin-v202)
* [📦 2.x 版本历史记录](#mega-wechat-miniprogram-plugin-v2-series)
* [📜 1.x 历史版本 (已不再维护)](#mega-wechat-miniprogram-plugin-v1-series)
## 2.0.2
>
> 发布日期：2025-11-19
>
* 修复了高网络延迟环境下，初始的定位跟踪效果不如预期的问题。
## 2.x 版本历史记录
2.x 是重构后稳定版本，提供了更加鲁棒的 AR 体验和更清晰的 API 调用方式。
### 2.0.1
* 优化了跟踪效果。
### 2.0.0
* **新增**：Sample, Toolbox 及 API 文档全面更新。
* **新增**：支持 APIToken。
* **新增**：全方位支持 TypeScript 类型推断。
* **新增**：支持使用旋转后的屏幕。
* **优化**：提供了更流畅的 AR 体验，不再会因获取图片卡顿。
* **优化**：使用微信原生提供的图片接口，更鲁棒。
* **优化**：AR 内容的跟踪更平滑，更稳定。
* **重构**：重写了 MegaSession 的工作流，大幅简化流程，支持纯代码创建。
* **重构**：解耦 Ema 标注数据的获取和场景中加载过程。
## 1.x 历史版本记录
1.x 是历史版本，已停止维护，以下内容仅供参考。
### 1.1.12
* 支持 v4DH CLS 库。
### 1.1.10
* 修复了上个版本中 `viewLocalizationInfo` 的版本兼容性问题。
### 1.1.9
* 增加了定位成功时的上报信息。
### 1.1.2 - 1.1.8
* 优化跟踪效果。
* 修复 Android 8.0.37 获取图像为纯黑问题。
* 修复无 Ema 时 Block 默认位置到世界原点。
### 1.1.1
* 修复不设置配置信息时运行错误。
### 1.1.0
* **新增**：导出数学方法。
* **新增**：调整为组件，使用 XML 标签方式引入插件。
* **修复**：修复重新设置 Mega 参数时的异常。
* **优化**：插件退出时增加资源释放，优化内部实现。
### 1.0.5
* 首次上线。
