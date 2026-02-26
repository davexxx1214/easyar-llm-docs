---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/active-control.html
original_file: doc--zh-cn--develop--unity--fundamentals--active-control.md
normalized_at: 2026-02-27
---
# 适用于 target 和 origin 的 active 控制策略
通过以下内容，您将了解 target 和 origin 下物体的默认显示和隐藏策略，以及如何根据需要进行调整。
## 开始之前
* 阅读 [Target](target.html) 了解 target 的基本概念、状态和生命周期。
* 阅读 [XR Origin](origin.html) 了解 XR Origin 的基本概念、组成和生命周期。
## active 控制和控制策略类型
session 运行过程中，target 和 origin 会经历跟踪和丢失等状态变化。通过 active 控制策略，可以自动管理 target 和 origin 下物体的显示和隐藏行为。
在 Unity 中，[ActiveController](../../../api/unity/easyar.ActiveController.html) 组件负责自动管理 target 和 orign 物体的 [GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 状态，以便在 target 被跟踪或运动跟踪开始跟踪后显示内容，在 target 丢失或运动跟踪成功初始化之前隐藏内容。
[ActiveController](../../../api/unity/easyar.ActiveController.html) 提供了两种不同的 active 控制策略：
* [ActiveWhileTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveWhileTracked)：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `true`）；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `false`）。
* [ActiveAfterFirstTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveAfterFirstTracked)：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `false`）；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活（[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 设置为 `true`）。
默认情况下，[TargetController](../../../api/unity/easyar.TargetController.html) 使用 [ActiveWhileTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveWhileTracked) 策略，这意味着当 target 被跟踪时，target 以及其下的内容会被激活，而当跟踪丢失时，target 以及其内容会被停用。
默认情况下，[XROriginChildController](../../../api/unity/easyar.XROriginChildController.html) 使用 [ActiveAfterFirstTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveAfterFirstTracked) 策略，这意味着在运动跟踪成功初始化之前，origin 以及其下的内容会被停用，而一旦运动跟踪成功初始化，origin 以及其下的内容会被持续激活。
## 选择不同的 active 控制策略
打开 Inspector 面板，在 `Strategy` 下拉菜单中选择 `Input`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/active-select.png)
然后在右侧选择所需的 active 控制策略来覆盖默认策略。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/active-select2.png)
在脚本中，可以通过 [OverrideStrategy](../../../api/unity/easyar.ActiveController.html#u_easyar_ActiveController_OverrideStrategy) 属性来覆盖默认的 active 控制策略。
比如，下面的代码展示了如何将 target 的 active 控制策略设置为 [ActiveAfterFirstTracked](../../../api/unity/easyar.ActiveController.Strategy.html#u_easyar_ActiveController_Strategy_ActiveAfterFirstTracked)：
```
target.ActiveController.OverrideStrategy = ActiveController.Strategy.ActiveAfterFirstTracked;
```
对 active 策略的修改会即时生效，并根据当前的跟踪状态更新 [GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html)。
## 关闭 active 控制
如果需要完全禁用 active 控制，比如需要根据需要进行控制，可以通过禁用 [ActiveController](../../../api/unity/easyar.ActiveController.html) 组件来关闭 active 控制。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/active-disable.png)
在脚本中，可以通过设置 [ActiveController](../../../api/unity/easyar.ActiveController.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 属性来关闭 active 控制。
```
target.ActiveController.enabled = false;
```
[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 属性的修改会即时生效，并且不会再根据跟踪状态更新 [GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html)。如果再次启用 [ActiveController](../../../api/unity/easyar.ActiveController.html) 组件，[GameObject.activeSelf](https://docs.unity3d.com/ScriptReference/GameObject-activeSelf.html) 会根据当前的跟踪状态进行更新。
