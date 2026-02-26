---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/target-state.html
---

获取 target 的状态 | EasyAR 文档
**
##### Table of Contents
**
# 获取 target 的状态
session 运行过程中，target 会经历跟踪和丢失等状态变化。通过以下内容，您将了解如何获取和使用 target 的状态信息，以及如何使用 found 和 lost 事件来控制内容的显示。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [Target](target.html) 了解 target 的基本概念、状态和生命周期。
## 判断 target 是否被跟踪
可以使用 [TargetController.IsTracked](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_IsTracked) 属性判断 target 是否被跟踪。
## 使用 target 的 found 和 lost 事件
可以使用 [TargetController.TargetFound](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetFound) 和 [TargetController.TargetLost](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetLost) 事件来处理 target 被跟踪和丢失的情况。
比如，下面的代码展示了在 target 被跟踪时播放视频，并在 target 丢失时暂停视频播放的过程：
```
`target.TargetFound += () =&gt;
{
if (player &amp;&amp; player.gameObject.activeInHierarchy)
{
player.Play();
}
};
target.TargetLost += () =&gt;
{
if (player &amp;&amp; player.gameObject.activeInHierarchy)
{
player.Pause();
}
};
`
```
##### 小心
如果没有手动卸载 target，[TargetController.TargetLost](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetLost) 有可能在 session 停止时被调用。如果没有手动停止 session，则它可能在 session 的 OnDestroy 过程中被调用，由于 Unity 的 OnDestroy 执行顺序是不受保证的，所以在事件中使用的对象需要进行有效性检查以避免在 OnDestroy 过程中访问已经被销毁的对象。
## 后续步骤
* [active 控制策略](active-control.html) 介绍了 target 下物体的默认显示和隐藏策略，以及如何根据需要进行调整。