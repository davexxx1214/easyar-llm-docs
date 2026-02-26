---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/onsite-and-simulation.html
original_file: doc--zh-cn--develop--unity--mega--onsite-and-simulation.md
normalized_at: 2026-02-27
---
# 现场使用和模拟运行
本文介绍了 Mega 在现场使用和非现场模拟运行时的配置差异，以及如何根据需求进行配置。
## 现场使用和模拟运行的差异
Mega 会使用 GNSS（GPS、北斗等）信息对定位过程进行辅助，以提升定位的精度和稳定性。在现场使用时，设备的 GNSS 信息是准确的可以用来辅助定位。而在非现场模拟运行时，设备的 GNSS 信息与环境是不匹配的，这个数据不能用来辅助定位，反而会影响定位效果。因此，Mega 提供了两种不同的配置以适应现场使用和非现场模拟运行的需求。
默认配置为模拟运行配置，以避免初次使用时因错误配置导致的定位失败的问题。
在模拟运行的配置下，屏幕上会始终显示警告信息，这段信息无法关闭，以确保应用不会以错误的配置发布到最终用户手中。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/warn-simulation.png)
> **提示**
如果要关闭警告信息，需要确保应用只会在现场使用，并使用现场配置。
## 配置以用于非现场模拟运行
选中 session 下的 `Mega Tracker` 物体，找到 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件，选择 `Location Input Mode` 为 `Simulator` 选项即可启用模拟运行配置。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-simulator.png)
在脚本中，可以设置 [MegaTrackerFrameFilter.LocationInputMode](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocationInputMode) 为 [Simulator](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_Simulator) 来达到同样的效果。
> **注意**
[使用 EIF 文件模拟运行](../simulation/playback.html) 时，该选项会被自动设置为 [FramePlayer](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_FramePlayer) 且不可更改，以确保 EIF 文件内记录的 GNSS 数据被正确使用。
## 配置以用于现场使用
选中 session 下的 `Mega Tracker` 物体，找到 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件，选择 `Location Input Mode` 为 `Onsite` 选项即可启用现场使用配置。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-onsite.png)
在脚本中，可以设置 [MegaTrackerFrameFilter.LocationInputMode](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocationInputMode) 为 [Onsite](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_Onsite) 来达到同样的效果。
> **小心**
如果在非现场模拟运行时错误地使用了现场配置，可能会导致定位失败进而影响内容的显示。
