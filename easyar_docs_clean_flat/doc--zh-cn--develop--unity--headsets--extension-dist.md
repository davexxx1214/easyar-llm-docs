---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-dist.html
original_file: doc--zh-cn--develop--unity--headsets--extension-dist.md
normalized_at: 2026-02-27
---
# 发布扩展包
本文介绍完成开发和运行验证后，如何将为特定头显开发的 EasyAR Sense Unity Plugin 扩展打包发布，以便用户可以方便地使用该扩展。
## 开始之前
* 完成 [让头显支持 EasyAR](extension-imp.html) 开发。
* 完成 [运行验证（bring-up）](extension-bring-up.html)，确保设备上运行效果正常。
## 完成包定义
包本身的定义在 `package.json` 中，可以根据 [Unity 创建自定义 package 的指南](https://docs.unity3d.com/Manual/CustomPackages.html) 来修改这个文件或创建一个新的包。注意确保修改 package 的 `name` 和 `displayName`，注意不要与 EasyAR 提供的模板本身或其它供应商的扩展发生冲突。
## 重新生成 meta 文件
删除并重新生成 package 中所有文件的 .meta 文件。否则它们会与模板本身或其它供应商的扩展发生冲突。
> **注意**
Unity 可能会缓存 .meta 文件，建议在 Unity 关闭状态下，删除包内所有 .meta 文件，并整个删除 `Library` 目录，然后重新打开 Unity 工程以重新生成 .meta 文件。
注意场景和资源文件中的引用都会变化，有可能需要重新创建或修改场景中的部分物体。文本替换 .unity 以及其它资源文件中的 GUID 是一种可行的方法。
## 检查版本兼容性
检查扩展与设备 SDK 以及 EasyAR Sense Unity Plugin 的版本兼容性。
> **注意**
从版本 4000 开始，EasyAR Sense Unity Plugin 遵循 Unity 所要求的 semantic versioning。在这之前每个小版本都可能会包含不兼容的更改。
## 打包发布
您可能还希望修改 package 中的其它一些文件，确保在发布前仔细审查整个 package。
建议使用 Unity package 来打包文件。如果设备 SDK 并没有准备好以 Unity package 形式发布，也可以选择通过 asset package 来发布。
需要提醒用户，EasyAR license key 的所有限制（尤其是针对自定义相机的限制）都适用于您的扩展包。
