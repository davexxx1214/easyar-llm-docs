---
source: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/enable-easyar-android.html
---

在 Android 应用中启用 EasyAR 功能 | EasyAR 文档
**
##### Table of Contents
**
# 在 Android 应用中启用 EasyAR 功能
本章介绍如何在 Android Studio 中配置 EasyAR 的 Android 工程，无需使用 Unity 等 3D 引擎。
## 准备工作
开始之前，您需要准备：
* 最新版本的 Android Studio
* JDK 8/11/17
* Android Gradle Plugin 4.0 或以上
* Android NDK r28 或以上
* 获取 EasyAR 授权许可证
* 选择 EasyAR Sense [发布版本并下载](variants.html)
##### 注意
并非所有安卓设备均支持 EasyAR Sense 的所有功能，部分功能依赖额外硬件或配置，具体可查阅对应功能支持的设备列表。
## 导入 EasyAR Sense for Android
本节介绍如何在**非 Unity 的 Android 工程**中导入 EasyAR Sense SDK。 EasyAR Sense 提供 Java 和 C++ API，并支持 Kotlin，您可以使用最习惯的语言进行开发。
由于不同 IDE 的配置方式可能存在差异，这里仅说明**基于 Android Studio + Gradle 的典型配置方式**。
### 选择 API 使用方式
EasyAR Sense for Android 提供两种 API 使用方式：
* 仅使用 Java API
* 使用 Java 和 C++ API
请根据项目需求选择其中一种进行配置。
#### 仅使用 Java API
当仅使用 EasyAR 的 Java API 时，**无需配置 NDK**。
将 `EasyAR.aar` 放入`app/libs/` 或 Gradle 指定目录。
#### 使用 Java 和 C++ API
当需要同时使用 EasyAR 的 C++ API 时，需要同时配置 Java 依赖与原生库。
* Java 层文件
将 `EasyAR.jar` 放入 `app/libs/` 或 Gradle 指定路径。
* 原生库（`.so`）
将 EasyAR 提供的原生库按 ABI 放入以下路径或 Gradle 指定路径。
```
`app/src/main/jniLibs/
├── armeabi-v7a/
│ └── libEasyAR.so
└── arm64-v8a/
└── libEasyAR.so
`
```
* C++ 头文件
将 EasyAR SDK 中 `include` 目录下的 `easyar` 文件夹拷贝到以下路径或 `Android.mk`/`CMakeLists.txt` 指定路径。
```
`app/src/main/jni/easyar/
`
```
头文件路径需在 `Android.mk` 或 `CMakeLists.txt` 中显式指定。
### Gradle 配置说明
当您使用 C++ API 时，需要在 Gradle 中启用 Native Build, **仅适用 Java API 无需配置**。 您可以使用 ndk-build（Android.mk）进行配置。
在 `app/build.gradle` 中添加：
```
`android {
externalNativeBuild {
ndkBuild {
path "src/main/jni/Android.mk"
}
}
}
`
```
>
> 如果使用 CMake，请参考
[> Google 官方文档
](https://developer.android.google.cn/studio/projects/add-native-code.html)> 进行配置。
>
### NDK 配置
#### 声明 EasyAR 为预编译库
```
`include $(CLEAR\_VARS)
# 确保该路径指向 jniLibs 中当前 ABI 目录
LOCAL\_PATH := $(LOCAL\_PATH\_TOP)/../jniLibs/$(TARGET\_ARCH\_ABI)
LOCAL\_MODULE := EasyAR
LOCAL\_SRC\_FILES := libEasyAR.so
include $(PREBUILT\_SHARED\_LIBRARY)
`
```
#### 链接 EasyAR 与系统库
```
`LOCAL\_SHARED\_LIBRARIES += EasyAR
# OpenGL ES（必需）
LOCAL\_LDLIBS += -lGLESv3
`
```
>
> EasyAR 运行至少需要 OpenGL ES 2.0，推荐使用 OpenGL ES 3.0（GLESv3）。
>
### 指定 ABI 架构
在 `app/build.gradle` 中显式指定 ABI，避免无效架构被打包：
```
`android {
defaultConfig {
ndk {
abiFilters "armeabi-v7a", "arm64-v8a"
}
}
}
`
```
如果只需要其中一种架构，可只保留对应项。
### AndroidManifest 权限配置
EasyAR Sense 需要以下权限，缺失将导致初始化失败或黑屏：
```
`&lt;uses-permission android:name="android.permission.CAMERA" /&gt;
&lt;uses-permission android:name="android.permission.INTERNET" /&gt;
`
```
完整示例：
```
`&lt;manifest xmlns:android="http://schemas.android.com/apk/res/android"
package="cn.easyar.samples.helloar"&gt;
&lt;uses-permission android:name="android.permission.CAMERA" /&gt;
&lt;uses-permission android:name="android.permission.INTERNET" /&gt;
&lt;/manifest&gt;
`
```
### 初始化 EasyAR
在应用启动时调用 `Engine.initialize` 进行初始化。
示例（Java）：
```
`@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
Engine.initialize(this, key);
}
`
```
##### 注意
初始化必须在使用 EasyAR 相关功能之前完成。
## 额外配置
在 Android 平台上，根据系统版本及所使用的功能不同，可能还需要注意以下配置和限制。
### 配置使用 ARCore
如果项目中使用 **ARCore**，请参考其官方文档完成 `AndroidManifest.xml` 和 `build.gradle` 的相关配置。
此外，在初始化 EasyAR 之前，必须显式加载 ARCore 的原生库：
```
`System.loadLibrary("arcore\_sdk\_c");
`
```
##### 注意
使用 **ARCore v1.19.0 之前的版本**时，在 **Android 11** 上将无法被检测到。
这是由于 Android 11 开始引入了应用可见性限制，需要在 `AndroidManifest.xml` 中声明 ARCore 包名。
```
`&lt;queries&gt;
&lt;package android:name="com.google.ar.core" /&gt;
&lt;/queries&gt;
`
```
### 配置混淆（ProGuard）
如果对 Java 代码启用混淆，需要 **排除 `cn.easyar` 命名空间**。
EasyAR Sense 在运行时会通过 JNI 使用 **类名反射获取 Java 类型**。
如果 `cn.easyar` 下的类被混淆或重命名，可能导致未定义行为。
#### 基本规则
```
`-keep class cn.easyar.\*\* { \*; }
`
```
#### 推荐的精确规则
```
`-dontwarn javax.annotation.Nonnull
-dontwarn javax.annotation.Nullable
-keepattributes \*Annotation\*
-keep class cn.easyar.RefBase { native &lt;methods&gt;; }
-keepclassmembers class cn.easyar.\* {
&lt;fields&gt;;
protected &lt;init&gt;(long, cn.easyar.RefBase);
}
-keep,allowobfuscation interface cn.easyar.FunctorOf\* { \*; }
-keep class cn.easyar.Buffer { native &lt;methods&gt;; }
-keep class cn.easyar.Engine { native &lt;methods&gt;; }
-keep class cn.easyar.JniUtility { native &lt;methods&gt;; }
-keep class cn.easyar.engine.\*\* { \*; }
-keep class cn.easyar.CameraParameters
-keep interface cn.easyar.FunctorOfVoidFromInputFrame
`
```
上述 ProGuard 规则 **已包含在 EasyAR 的 aar 库中**，通常无需重复配置。
### Scoped Storage
Android 10 开始引入的 **Scoped Storage（分区存储）** 机制，会对部分依赖文件路径的 API 造成影响。这是由于 /sdcard 下的非媒体路径（如自定义目录）在 Android 10 上无法直接访问所致。对 EasyAR 的影响体现在部分需要传入文件路径的 API（如录屏）在 Android 10 上，不支持直接读写媒体路径，但是在 Android 11 上可以正常工作。
**解决方式**：
* 简便方案（Android 10）
在 `AndroidManifest.xml` 中禁用 Scoped Storage：
```
`&lt;application
android:requestLegacyExternalStorage="true"
... &gt;
&lt;/application&gt;
`
```
* 推荐方案
* 仅使用应用内部存储
* 或通过 MediaStore 与媒体路径进行数据交换
### Android Gradle Plugin 与 NDK
自 NDK r22 起，默认使用 LLD 链接器，并需要配合 `llvm-strip` 使用；这与 Android Gradle Plugin 4.0 以下版本内置的 `strip` 工具不兼容。
**解决方式**:
* 升级至 **Android Gradle Plugin 4.0 或以上**
* 或在 `packagingOptions` 中使用 `doNotStrip` 禁用 stripping（不推荐）
### Windows 路径长度限制
在 Windows 系统上，如果工程中任意文件（包括构建过程中生成的临时文件）的**绝对路径长度超过 260 个字符**，
可能会导致 Android Studio 构建失败。
**解决方式**：
* 将工程放置在更短路径下（例如 `C:\\user\\project`）
* 避免过深的目录层级
## 延伸阅读
* [EasyAR Mega 支持的设备](../../mega/devices.html)
* [图像跟踪支持的设备](../../image-tracking/devices.html)
* [运动跟踪支持的设备](../../motion-tracking/devices.html)
* [稀疏空间地图支持的设备](../../sparse-spatial-mapping/devices.html)
* [稠密空间地图支持的设备](../../dense-spatial-mapping/devices.html)
* [运动跟踪与 EasyAR 其他模块的关系](../../motion-tracking/motion-tracking-and-easyar.html)