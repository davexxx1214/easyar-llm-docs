---
source: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/initialization.html
---

库加载和初始化 | EasyAR 文档
**
##### Table of Contents
**
# 库加载和初始化
在使用 EasyAR Sense 的功能之前，需要进行初始化。初始化时，EasyAR Sense 会建立一些必要的环境，并验证 License Key。
## 非 Android 平台
对于 iOS/macOS/visionOS/Windows 平台，一般通过编译时动态链接来实现库的加载，参考示例添加对 EasyAR 库的引用，并在需要时添加 EasyAR 库的头文件即可。
初始化只需要调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_System_String_) 并传入 license key 即可。
## Android 平台
对于 Android 平台，一般是通过 java.lang.System.loadLibrary 来进行动态库的加载。
初始化只需要调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_android_app_Activity_System_String_) 并传入当前 Activity 和 License Key 即可，其中会自动调用 java.lang.System.loadLibrary。
如果您需要将 libEasyAR.so 放在非默认位置（例如需要在运行过程中动态下载），则您需要改为调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_android_app_Activity_System_String_System_String_) 并传入当前 Activity、License Key 和 libEasyAR.so 存放路径。
如果您有更复杂的需求，可以将加载 libEasyAR.so，设置 Activity 和验证 License Key 三个步骤分开进行。您可以先调用 [loadLibraries](../../../api/native/easyar.Engine.html#n_easyar_Engine_loadLibraries_System_String_)，再调用[setupActivity](../../../api/native/easyar.Engine.html#n_easyar_Engine_setupActivity)，再调用 [initializeKey](../../../api/native/easyar.Engine.html#n_easyar_Engine_initializeKey)。