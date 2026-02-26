---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/release-notes/release-notes.html
original_file: doc--zh-cn--develop--unity--release-notes--release-notes.md
normalized_at: 2026-02-27
---
# EasyAR Sense Unity Plugin 发行说明
我们很高兴地宣布 EasyAR Sense Unity Plugin 4000 发布。此版本标志着 EasyAR 具备了完善的 API 和与时俱进的设备支持，同时新版本发布也将比以往更加频繁。
下载 [EasyAR Sense Unity Plugin 4000](https://www.easyar.cn/view/download.html) 以享受这些新功能和改进。
## 历史版本
* [EasyAR Sense Unity Plugin 版本 4 发行说明](release-notes-v4.html)
## 版本 4000.0.1
>
> 发布日期：2025-11-14
>
* 🐛 修复：解决了在启用 minify 打包的 Android 构建中，因缺少静态方法（ `loadLibraries` 、 `setupActivity` ）而可能触发的运行时 `AndroidJavaException` 异常，该错误会导致 EasyAR 无法运行。
## 版本 4000.0.0
>
> 发布日期：2025-10-20
>
从这个版本开始，EasyAR Sense Unity Plugin 将遵循 Unity 所要求的 [包版本控制（使用 Semantic Versioning）](https://docs.unity3d.com/Manual/upm-semver.html) ，因此版本号将与 EasyAR Sense 相异，发布频率也可能不同。该版本插件内包含 EasyAR Sense 4.7.0 正式版。
EasyAR Sense Unity Plugin 4000.0.0 迎来了大幅改变，主要集中在这几方面：
1. Unity 及 AR Foundation 兼容性变化
从这个版本开始，EasyAR Sense Unity Plugin 将只支持 Unity 2021.3 及更新版本，Unity 6 支持也已经完善。同时，AR Foundation 支持已经合并到插件包内，这个版本将只支持 AR Foundation 5 及更新版本，其使用经过大量简化。如果场景中添加了 AR Foundation 的组件，无论运行之后 AR Foundation 是否最终使用，场景配置和脚本代码都可以不变。
2. 与时俱进的头显支持，新增支持多款 OST/VST 头显
经过与行业内多家企业多年的打磨，EasyAR 对头显的支持已经标准化。现在您可以通过 EasyAR Sense Unity Plugin 扩展实现第三方头显设备的支持（可能需要头显厂商提供部分数据接口）。这个版本内置了 Apple Vision Pro 以及 XREAL Air2 Ultra 的支持，同时通过 EasyAR Sense Unity Plugin 扩展包支持 Pico 4 Ultra Enterprise 及 Rokid AR Studio。
同时您也可以从 EasyAR 的一些合作伙伴那里获取其它设备的支持扩展包（比如 Xrany 元霓）。
3. 完善 Unity 组件接口，大幅优化 ARSession 工作流
这个版本是第一个通过 Unity 组件完整封装 EasyAR Sense 功能的版本。ARSession 经过了大量优化和重写，现在您可以轻松实现设备或功能的支持判断，根据具体情况启动或停止 ARSession 以实现运行时切换 ARSession 或不同 AR 功能。同时，您也可以使用 ARSessionFactory 在运行时创建 ARSession 及相关组件。这个版本还添加了惯性导航和 3DoF 相机功能，这些功能主要为 EasyAR Mega 所设计，但也可以单独使用。
4. 新增多个开发及诊断工具
这个版本增加了提供了全新的 EIF 录制和播放功能，虽然 EIF 录制和播放在过去的版本中也能使用，但使用 EIF 从未如此简单。您现在可以在 Unity 编辑器中使用时诊断工具 Session Validaion Tool 直接播放 eif 并驱动您的场景，无论是图像跟踪、空间地图还是 EasyAR Mega，都可以在电脑上还原设备上的运行效果。现在您可以使用运行时诊断面板 EasyAR Diagnostics Panel 在 app 中轻松开启 eif 录制功能，或是随时开关 ARSession 及其组件的关键状态信息显示。同时，这个版本的 sample 已经全部重写，运行 sample 就可以直接看到 ARSession 状态以及录制 eif 的按钮以方便使用。
5. EasyAR Mega 工具全面公开
这个版本集成发布了 Mega Studio 2.12。今后插件的更新将更加频繁，Unity 侧 Mega 工具将逐步合并进插件内部并与插件常规更新合并发布。除了过去预发布版本中的更新之外，这个版本会默认开启惯导支持，进一步大幅拓展 EasyAR Mega 的设备支持。这个版本还包含对最新版本 EasyAR Mega Landmark 服务的支持。使用 EasyAR Mega 可以通过 [EasyAR 网站页面](https://www.easyar.cn/view/apply.html) 进行申请。
详细更新内容如下：
**Unity 及 AR Foundation 兼容性变化：**
* 🔧 Unity：支持 Unity 2021.3 及更新版本（包括 Unity 2022.x/Unity 6.x）
* 🔥 移除对 Unity 2019/Unity 2020 的支持
* 🔥 移除用于 Unity 2019 的 gradle 版本检测
* 🔥 移除用于 Unity 2019 的选项 DisableARCoreAREngine
* ✨ Unity 6：全面支持 Unity 6
* ✨ 支持 URP 17+ 及 Render Graph
* 🐛 已修复：Unity 6 上 ClassLoader 行为变化导致 ARCore 失效
* 🐛 已修复：Render Scale 非 1 时相机渲染失效
* 🐛 Unity 6 自身 BUG：在 iOS/Mac 设备上可以观察到视觉故障和伪影。该问题仅发生在需要获取相机纹理的情况，我们添加了部分缓解措施但无法完全消除。已反馈至 Unity，见 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 。Unity 6.2 以上可以通过设置 Universal Render Pipeline Asset 中的 Render Scale 为 0.96-1.05 以外的数值来规避这个问题。
* 🐛 Unity 6 自身 BUG：Windows DX11 上的渲染效果不正常。我们在 Unity 6.0-6.1 中已添加缓解措施。实测 Unity 6.2 已修复该问题。
* ✨ AR Foundation：支持 AR Foundation 5 及更新版本，大幅简化使用
* ✨ AR Foundation 支持已经合并到插件包内，不再需要单独导入包（特殊需要可以通过配置选项关闭）
* ✨ 支持复用 `Unity.XR.CoreUtils.XROrigin` 作为 ARSession 的原点，支持复用 XROrigin 的 Camera
* ✨ 添加 `Unity XR Auto Switch` 配置选项，默认处理 Unity XR（包含 AR Foundation）物体的切换
* ✨ 通过 EasyAR 菜单创建的 ARSession 自动包含并默认开启 AR Foundation 支持
* ✨ 绝大部分 sample 都已添加 AR Foundation 支持（AR Foundation 本身需要手动导入并正确配置）
* 🔧 ARCore 及 ARKit 可单独控制，且可控制 EasyAR 内置的 ARCore/ARKit 与 AR Foundation 的 ARCore/ARKit 的优先顺序
* 🔥 移除对 AR Foundation 4 的支持
* 🔥 移除对 ARSessionOrigin 的支持，仅支持 XROrigin
* 🔥 移除代理执行 AR Foundation 的 ARCore 安装流程
* ✨ 全面兼容 Input System Package
**与时俱进的头显支持，新增支持多款 OST/VST 头显：**
* 🚀 头戴显示设备接口已稳定，支持第三方接入
* ✨ 支持第三方设备接入（需要头显厂商提供特定数据接口）
* ✨ 支持 XROrigin 及 XR Interaction Toolkit
* ✨ 简化并统一所有头显样例，零代码，并支持功能切换
* ✨ 支持鱼眼相机输入
* ✨ 支持自定义相机输入 3DOF 数据
* ✨ 添加菜单功能：Extensions，整合所有扩展菜单项
* 🐛 修复部分头显运行 DenseSpatialMap 时出现渲染异常
* 🔥 移除 ActionOne 和 BT350 等古早眼镜 sample
* ✨ 内建支持 Apple Vision Pro
* ✨ 支持 Metal、RealityKit 及 Hybrid 模式
* ✨ 支持 visionOS >= 2.0，支持 visionOS 26
* ✨ 内建支持 XREAL Air2 Ultra（需要 XREAL SDK >= 3.1）
* ✨ 不再需要导入单独的支持包
* ⚡ 优化 XREAL 上的运行效果
* 🔥 移除 XREAL Light 支持
* ✨ 通过 EasyAR Sense Unity Plugin 扩展分发 Pico 及 Rokid 等其它设备支持
* ✨ 提供第三方设备接入的参考模板 `com.easyar.sense.ext.hmdtemplate`
* ✨ 支持 Pico 4 Ultra Enterprise（需要 PICO Unity Integration SDK >= 3.1）
* ✨ 支持 Rokid AR Studio（需要 Rokid Unity OpenXR Plugin >= 3.0.3）
* ✨ 这些扩展将支持今后多个版本的 EasyAR Sense Unity Plugin
* ✨ 支持 EasyAR XR License
* 🔧 头显上使用 EasyAR 需要 EasyAR XR License 并保证首次联网（试用需每次联网）
**完善 Unity 组件接口，大幅优化 ARSession 工作流：**
* 🚀 完善 Unity 组件层封装
* ✨ 完善场景组件，提供所有 EasyAR Sense 功能
* 🔥 移除所有通过组件封装的 EasyAR Sense 层接口
* 🔥 移除所有内部接口
* ✨ ARSession：重写并大幅优化工作流
* ✨ 支持在任意时刻启动和停止 session
* ✨ 支持 session 自动启动控制
* ✨ 支持不黑屏切换 session 功能和输入源
* ✨ 简化设备支持判断，以一致接口提供
* ✨ 启动时更新 MotionTracker、ARCore、AR Engine 的设备支持列表
* ✨ 支持设备列表更新后 session 自动重启
* ✨ 支持获取详细 session 损坏信息
* ✨ 添加 session 内部状态自检
* 🔥 移除 ARComponentPicker，其功能由其余 session 流程替代
* 🔥 禁止多个 ARSession 同时运行
* ✨ ARSessionFactory：提供运行时创建 ARSession 及相关组件的功能
* ✨ 支持通过 ARSessionFactory 运行时创建与编辑器菜单相同的 session
* ✨ 添加 Frame Source 排序功能（含菜单项）
* ✨ FrameSource：添加惯导和 3DoF 支持
* ✨ 添加 InertialCameraDeviceFrameSource 用于支持惯性导航
* ✨ 添加 ThreeDofCameraDeviceFrameSource 用于支持 3DoF 的相机
* ✨ 添加菜单功能：Frame Source by Transform Type，提供所有内置 FrameSource 的列表
* ⚡ 优化 Inspector 选项
* ✨ 其它接口调整及功能更新
* ✨ 添加使用 Texture2D 创建 ImageTarget 的功能
* ✨ 添加 ImageMaterial 用于渲染 Image 类型的数据（相机图像或 Target 图像等）
* ✨ 添加 ActiveController 用于控制 GameObject 的 active，统一相关控制逻辑
* ✨ 添加在桌面上模拟屏幕旋转的功能
* ✨ 添加 XROriginChildController，控制 Session 原点下物体的行为
* 🔥 移除 WorldRootController
* 🔧 稀疏空间地图接口拆分成 Builder 和 Tracker 两个不同功能组件
* 🔧 调整 EasyARController，提供应用/系统级静态功能
* 🔧 统一 Target 组件接口
* 🔧 统一服务访问数据的接口
**新增多个开发及诊断工具：**
* 🚀 添加编辑时诊断工具：Session Validaion Tool
* ✨ 简化在任意场景中播放 eif
* ✨ 支持控制 eif 播放流程
* ✨ 支持控制 session 流程
* 🚀 添加运行时诊断面板：EasyAR Diagnostics Panel
* ✨ 添加 Developer Mode 开关，默认点击屏幕 8 次开启和关闭 Diagnostics Panel，简化线上 app 录制 eif 和问题反馈
* ✨ 支持自定义 Developer Mode 开关，使用自定义交互开关 Diagnostics Panel
* ✨ 支持控制 eif 录制
* ✨ 支持控制 session 信息显示
* ✨ 支持控制 eed 录制
* ✨ 添加全新的 EIF 录制和播放功能
* ✨ FrameRecorder 会自动组装进 ARSession，不再需要手动选择
* ✨ FrameRecorder 会默认自动生成文件名以支持无脚本使用
* ✨ FramePlayer 使用新格式录制的数据支持播放跳转及速度调节，文件体积降低
* 🔧 支持在电脑上使用 eif 驱动场景和 AR 功能（非新功能）
* ✨ 添加 DiagnosticsController，统一和优化诊断功能
* ✨ 添加信息分级显示及控制，默认所有错误及警告信息都会通过 UI 展示
* ✨ 添加显示 ARSession 及其组件的关键状态信息的功能，默认会通过 UI 展示并每帧更新
* 🔧 使用诊断功能简化问题反馈信息的获取
* 🔥 删除 GUIPopup
* 🔧 优化异常状态行为及错误信息展示
* 🔧 优化无可用 frame source 时的错误信息
* 🔧 URP 环境使用 EasyAR 而非 AR Foundation 或头显渲染相机图像时，未正确配置 RendererFeature 会报错并中断 ARSession 执行
* 🔧 修改 Origin 默认的 Active 控制策略，在跟踪丢失时内容贴屏而非消失
* 🔧 自定义相机或头显上使用试用产品时，到达限制时间将隐藏所有内容以避免效果误判
* 🔧 优化配置页面内容和选项
* ✨ 支持选择 EasyAR Sense 库的变种
* 🔒 应用权限部分除相机权限外，其余权限不再可改，由 EasyAR Sense 库变种及 Mega 是否启用而决定
* 🔧 功能及服务器配置按 EasyAR 功能分组
* 🔧 集中管理第三方 AR SDK 配置
* 🔧 集中管理针对 Unity 的 Workaround 配置
**EasyAR Mega 工具全面公开：**
* 🚀 全面公开，同步更新
* ✨ 集成发布 Mega Studio 2.12
* 🔧 Unity 侧 Mega 工具将逐步合并进插件内部，今后仍将只提供最新版本的整合包，但将与 EasyAR Sense Unity Plugin 常规更新合并发布
* 🔧 EasyAR Mega 仍需通过 [EasyAR 网站页面](https://www.easyar.cn/view/apply.html) 申请并通过后才能使用
* ✨ 新增支持 EasyAR Mega Landmark
* ✨ 新增支持 5DOF 惯导并默认开启，进一步大幅拓展 EasyAR Mega 的设备支持
* ✨ 新增支持使用 API Token 访问 Mega 服务
* 🔧 优化 Mega 效果及开发体验（包含在过去更新的 4.7.x 版本内）
* ✨ 支持 3DOF 纯旋转模式和 0DOF 模式（默认未启用）
* ✨ 添加 EditorCameraDeviceFrameSource 用于编辑器诊断，避免由于不完整的复制 sample 导致手机上错误运行
* ✨ 使用 Mega时录制老版本 eif 数据，FrameRecorder 将自动生成 .eif.json 文件
* 🔧 使用 LocationInputMode 替代远程调试的退化选项
* 🔧 拆分无跟踪模式为独立组件，通常不再需要使用和关注
* 🔧 添加 BlockRootSource 选项，默认配置下忘记设置 BlockRoot 将报错
* 🔧 调整定位到多 block 时的默认行为，确保多 block 不会被默认使用
* 🔧 调整部分接口命名
* 🔧 在 Session 包含 Mega 但无法使用时抛出更明确的异常
* 🔧 调整 Mega 支持的 MotionTracker 最低 QualityLevel 为 Limited
* 🐛 修复 CloudLocalizerStatus.WakingUp 状态未正确转义导致运行报错
* 🔧 部分优化及修改见 EasyAR Sense 的更新日志
**Sample 重写及优化：**
* ✨ 重写所有 sample
* ✨ 兼容不同 Input System 配置
* ✨ 兼容 URP17+
* ✨ 兼容使用 AR Foundation
* 🔧 兼容不使用 AR Foundation
* 🔧 保留少量不含 AR Foundation 支持的 sample
* ⚡ 优化脚本及接口调用
* 🚚 部分 sample 已重命名
* 🔧 替换 sample 内模型和视频等资源
* ⚡ 减少 streaming assets的使用，仅在展示特定功能的 sample 中使用并导入
* ✨ 使用 Texture2D 创建 ImageTarget
* ✨ 增加新功能和接口演示
* ✨ 添加 Workflow\_ARSession sample，用于学习 session 基础流程和设备支持等
* ✨ 添加 Workflow\_FrameSource\_ExternalImageStream sample，以视频作为自定义相机（不能用于头显）
* ✨ 添加 Combination\_BasedOn\_MotionTracking sample，用于学习运动跟踪可用时各种功能的使用、切换以及 AR Foundation 切换
* ✨ 添加 Combination\_BasedOn\_AppleVisionPro sample，用于展示 Apple Visio Pro 上各种功能的使用和切换
* ✨ 添加 Combination\_BasedOn\_Xreal sample，用于展示 XREAL 设备上各种功能的使用和切换
* ✨ 添加多个 Mega sample（包含在过去更新的 4.7.x 版本内）
* ✨ 添加 Workflow\_FrameSource\_CameraDevice 中切换相机尺寸和 torch 模式的功能
* 🔥 移除单独的 AR Foundation sample，其功能已经包含在其它 sample 中
* 🔥 移除 FrameRecording sample，其功能已经包含在其它 sample 中
* 🔥 移除 MotionTracking\_Fusion sample，其功能已经包含在 Combination\_BasedOn\_MotionTracking 中
* 🔥 移除 SurfaceTracking\_ImageTarget sample，功能组合仍可用轻松实现
* 🔥 移除 Camera\_CustomCamera sample，如有需要仍可自行实现
* 🔥 移除 ActionOne 和 BT350 等古早眼镜 sample
* ✨ 简化 eif 录制和播放使用
* ✨ 所有 sample 均添加 eif 录制按钮，录制的 eif 文件可在编辑器内使用
* ✨ 重写 launcher，加入 sample 说明
* 🐛 修复通过 launcher 加载 sample 场景偏暗的问题
**EasyAR 及第三方 AR 功能集成：**
* ⬆️ 更新 EasyAR Sense 到 4.7.0 正式版
* ⬆️ 更新 EasyAR AR Engine Interop
* ⬆️ 更新 ARCore SDK 到 1.46.0
* 🔧 在部分无法合理运行 AR Engine 的手机上禁用 AR Engine
* 🐛 修复 Unity 6 上 ClassLoader 行为变化导致 ARCore 失效
