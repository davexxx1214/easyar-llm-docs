---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session.html
---

Mega 微信小程序插件上的 AR Session 概念与流程 | EasyAR 文档
**
##### Table of Contents
**
# Mega 微信小程序插件上的 AR Session 概念与流程
这篇文档将介绍 Mega 微信小程序插件上的 AR Session 的概念与流程。
## AR Session 是什么
Mega 微信小程序插件提供的 AR Session 是所有 AR 功能的入口。它管理运行过程和状态：包括从 VisionKit 和微信提供的传感器 API 获取数据、融合云定位与本地 AR 跟踪器结果、驱动场景中相机等其它部分物体的移动和渲染等。
```
`flowchart LR
Pose(VisionKit 相机位姿) -- 每帧同步 --&gt; Session[Session]
Image(计算该帧相机位姿所使用的相机图片) -. 仅 Mega 定位时发送 .-&gt; Session
Sensor(微信传感器数据) -. 异步 .-&gt; Session
Session -- Transform --&gt; Camera(xr-frame 摄像机)
`
```
## AR Session 的流程
```
`flowchart LR
Start((" "))
End((" "))
Init[Initializing]
Run[Running]
Check{Success?}
Start --&gt;|调用 start| Init
Init --&gt; Check
Check --&gt;|是| Run
Check --&gt;|否 / 重试次数超过上限| End
Run --&gt;|调用 stop| End
`
```
启动： session 状态转为 Initializing 。包含环境检查、资源加载以及等待微信 xr-frame 的 AR 系统就绪。
运行： session 状态转为 Running 。在此阶段，session 每帧输出跟踪结果并更新 xr-frame 相机的 Transform。
停止： session 状态转为 None 。包含释放资源、重置状态、销毁 MegaTracker。
##### 警告
AR 功能必须在 session 启动成功后才能使用。
AR Session 状态：
|状态|描述|
|None|初始状态，session 未启动或初始化失败|
|Initializing|初始化过程中|
|Running|运行状态，session已启动且初始化完成|
## [可选] 微信小程序插件上的 AR Session 与 Unity 上的 AR Session
##### 注意
仅针对 Unity 项目迁移的开发者。
Mega 微信小程序插件上的 AR Session 是 Unity 上 AR Session 的简化版本。由于不支持其他算法组件同时使用，微信小程序上的 AR Session 使用预集成的数据源组件和算法组件，用户不能选择数据源和/或组装算法组件。
此外，可以认为 Mega 微信小程序插件仅支持以 Block 为 target 且使用以 target 为中心的中心模式。
## 后续步骤
* [AR Session 流程控制](session-state.html)
## 相关主题
* [MegaTracker 的概念与工作流](tracker.html)