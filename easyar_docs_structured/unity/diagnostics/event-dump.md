---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/event-dump.html
original_file: doc--zh-cn--develop--unity--diagnostics--event-dump.md
normalized_at: 2026-02-27
---
# 录制 EED dump 文件
EED（EasyAR Event Dump）文件可用于抓取一些运行时的关键数据提供给 EasyAR 技术支持进行问题分析，例如一些跟踪器的跟踪结果、程序与 Mega 服务之间的网络请求等。通常在使用 [EIF 文件](../../simulation/simulation.html) 无法重现问题的时候使用。
## 使用开发者模式面板录制
运行程序，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。
![diagnostics eed windows](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-windows.png)
录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed windows 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-windows-2.png)
打开应用，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed android](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-android.png)
默认的 EED 文件路径位于 `/sdcard/Android/data` 中，在 Android 11 或更高版本的设备上，将无法通过文件管理器或 `adb pull` 来获得。建议使用 [Shizuku](https://shizuku.rikka.app/) 和 [MiXplorer](https://mixplorer.com/) 来获取文件。需要先在 WLAN 环境使用 Shizuku 与手机的无线调试配对并启动，然后在 Shizuku 中对 MiXplorer 授权，即可使用 MiXplorer 管理 `/sdcard/Android/data` 文件夹。
![diagnostics eed android 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-android-2.png)
打开应用，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed ios](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios.png)
使用示例时，可以将 iOS 设备连接到 Mac 设备，然后从 Mac 设备的 Finder 中找到 iOS 设备示例应用中录制完成的 EED 文件。
![diagnostics eed ios 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios-2.png)
如果无法在 Finder 中找到文件，可以在 Xcode 主菜单的 `Window -> Devices and Simulators` 中，选中应用，点击 `…`，选择 `Download Container…`，也可以获得 EED 文件。
![diagnostics eed ios 3](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios-3.png)
## 使用脚本录制
可以使用 [EventDumpRecorder.start(string, int)](../../../api/unity/easyar.EventDumpRecorder.html#u_easyar_EventDumpRecorder_start_System_String_System_Int32_) 开始录制 EED 文件，使用 [EventDumpRecorder.stop()](../../../api/unity/easyar.EventDumpRecorder.html#u_easyar_EventDumpRecorder_stop) 停止录制。
比如，下面的代码展示了如何在脚本中录制 EED 文件：
```
EventDumpRecorder eedRecorder;
bool RecordEED(bool on)
{
if (on)
{
if (session.Assembly == null || session.Assembly.Display == null) { return false; }
var path = Path.Combine(Application.persistentDataPath, DateTime.Now.ToString("yyyy-MM-dd\_HH-mm-ss.fff") + ".eed");
eedRecorder = EventDumpRecorder.create();
eedRecorder?.start(path, session.Assembly.Display.Rotation);
}
else
{
eedRecorder?.stop();
eedRecorder?.Dispose();
eedRecorder = null;
}
return true;
}
```
## 相关主题
* [开发者模式](developer-mode.html)
