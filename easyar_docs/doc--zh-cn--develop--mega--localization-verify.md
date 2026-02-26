---
source: https://www.easyar.cn/doc/zh-cn/develop/mega/localization-verify.html
original_file: doc--zh-cn--develop--mega--localization-verify.md
normalized_at: 2026-02-27
---
# 我的定位库可以使用了吗？
恭喜您！现在您已经对 Mega 的工作原理、适用场景、设备支持等方面有了一个了解，并已学会获取和使用 APIKey，那么您的应用已经具备了实现高精度空间定位的基础。
## 开始之前
在您开始正式编写应用逻辑之前，请确保：
1. **定位库已添加正确地图**
检查您的定位库，确保其中已经正确添加了您的应用需要使用区域的地图。
2. **SDK 配置正确**
确认您的代码中已经正确初始化了 EasyAR SDK，配置了有效的 SDK License，并且传入了有效的 Mega 服务的 API Key。
3. **地图被正确引用**
在您的场景或代码中，确保 Mega 定位模块（如 `MegaTracker` 组件）已经正确指向了您添加的地图资源。
如果以上步骤都已完成，那么您的定位库理论上已经可以正常工作了。
## 遇到问题
如果您在检查以上步骤时遇到问题，参考阅读以下文章进行解决：
* **您还没有地图**
您需要先为目标物理空间创建一张 Mega 地图。这通常包含两个步骤：数据采集和建图。参考阅读：
* [数据采集](../../mega/acquisition/intro.html)
* [建图](../../mega/mapping/intro.html)
* **您已有地图但不确定质量**
地图的精度和覆盖范围直接影响定位效果。可查看建图结果来辅助您判断。参考阅读：
* [回看采集路线](../../mega/mapping/routes.html)
* [查看建图报告](../../mega/mapping/report.html)
* [预览 3D 实景网格](../../mega/mapping/textured-mesh.html)
* **关于地图的加载与管理**
关于如何在定位库中加载以及管理建图结果，参考阅读：
* [管理定位库](../../mega/localization/database-management.html)
* [确认定位库可用](../../mega/localization/verification.html)
* **SDK License 及 APIKey**
如果遇到 License 或 APIKey 相关问题，参考阅读：
* [EasyAR Sense 许可证](../license-sense.html)
* [获取和使用APIKey](../apikey-auth.html)
当您的项目中包含了**有效且高质量**的 Mega 地图后，您的定位库就真正准备就绪了。请根据您的具体情况，参考上述文档完成地图的准备和配置工作，然后就可以开始编写激动人心的 AR 应用了！
