---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-ctrl.html
---

session 的流程控制 | EasyAR 文档
**
##### Table of Contents
**
# session 的流程控制
在 session 的运行过程中，有时需要对 session 组件进行修改，这时就需要停止再重新启动 session。有时还可能需要停止 session 的某些输出。本文介绍了如何控制 session 的运行流程。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 了解如何 [创建 session](session-creation.html)
## session 的组装
通常在启动 session 时会自动触发组装过程。
下面这段代码会隐式执行组装过程。
```
`Session.StartSession();
`
```
有些时候，比如需要提前 [判断可用性和设备支持](session-assemble.html)，也可以使用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 手动触发 session 组装过程：
```
`StartCoroutine(Session.Assemble());
`
```
##### 注意
[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 返回一个协程，需要通过 [StartCoroutine(IEnumerator)](https://docs.unity3d.com/ScriptReference/MonoBehaviour.StartCoroutine.html) 启动。
## 启动 session
[AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 控制 session 是否自动启动。如果 [AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 为 `true`（默认值），则在 [MonoBehaviour.Start()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) 时 session 会自动启动。
session 也可以手动启动，这需要提前修改 [AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 为 `false`。然后可以使用 [StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 来启动 session。
```
`Session.StartSession();
`
```
## 停止 session
可以使用 [StopSession(bool)](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StopSession_System_Boolean_) 来停止 session。
```
`Session.StopSession(keepLastFrame);
`
```
可以通过参数 `keepLastFrame` 来控制 session 停止后是否保留最后一帧的物理相机图像。这在需要切换不同 session 时比较有用，可以避免画面闪烁。
##### 注意
`keepLastFrame` 只能控制那些由 EasyAR 进行画面绘制的 session。一般来说，使用 AR Foundation 或头显时该参数无效。
## 停止 session 输出
session 运行时，可以通过 [enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 来控制 session 的输出。
下面这段代码可以停止 session 的所有输出，这时 session 仍然处于运行状态，但不会更新任何内容（包括由 EasyAR 绘制的物理相机画面和所有 EasyAR 控制的节点的 transform 等）。
```
`Session.enabled = false;
`
```
## 停止 session 绘制物理相机图像
可以使用 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 来控制物理相机图像的绘制。
下面这段代码可以停止物理相机图像的绘制：
```
`if (Session.Assembly != null &amp;&amp; Session.Assembly.CameraImageRenderer.OnSome)
{
Session.Assembly.CameraImageRenderer.Value.enabled = false;
}
`
```
需要注意的是，这里需要先判断 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 是否存在。
##### 注意
[ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 只在由 EasyAR 进行画面绘制的 session 中有效。一般来说，使用 AR Foundation 或头显时是无效的，这时物理相机画面的绘制由 AR Foundation 或头显 SDK 完成。
## 后续步骤
* 尝试 [访问 AR 功能组件](session-components.html)，了解更多 AR 功能的控制方法
* 了解如何 [获取 session 的运行结果](session-output.html)
* 了解如何 [判断可用性和设备支持](session-assemble.html)