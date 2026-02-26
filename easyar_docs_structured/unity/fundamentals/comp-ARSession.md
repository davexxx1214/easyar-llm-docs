---
source: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/comp-ARSession.html
original_file: doc--zh-cn--develop--unity--fundamentals--comp-ARSession.md
normalized_at: 2026-02-27
---
# AR Session 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ARSession.html)
>
探索 AR Session 组件窗口中的各项属性以自定义 session 参数。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/comp-ARSession.png)
默认条件下组件截图。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/comp-ARSession-runtime.png)
运行时的组件截图。
|属性|描述|
|**Auto Start**|控制 session 是否自动启动。如果值为 `true`（默认值），则在 [MonoBehaviour.Start()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) 时 session 会自动启动。
参见：[session 的流程控制](session-ctrl.html)|
|**Assemble Options**|Session 的组装选项。|
|*Enable Custom Camera*|启用自定义相机（默认 `true`）。
自定义相机包括：AR Engine frame source、AR Foundation frame source、所有头显以及所有自定义的 frame source。
*在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。*|
|*Frame Source*|FrameSource 的选择策略：
* Auto（默认）：自动选择，选择第一个可用且 active 的子节点。
* Manual：手动指定。需要在展开的选项内选择 session 的一个 frame source。
* FramePlayer：选择 frame player。参见：[帧数据源](../cameras/frame-source.html)|
|*Frame Filter*|FrameFilter 的选择策略：
* Auto（默认）：自动选择。选择所有 active 的子节点。
* AutoAvailable：自动选择。选择所有 active 且可用的子节点。
* Manual：手动指定。需要在展开的选项内选择 session 的一组 frame filter。
* None：不选择。|
|*Device List Update Options*|设备列表更新选项。
参见：[判断可用性和设备支持](session-assemble.html)|
|*Timeout*|请求超时时间，单位：s。|
|*Wait Time*|等待时间，单位：s。
超过等待时间即使下载未完成也会继续，这时下载完成后会通过事件更新。|
|*Ignore Cache*|忽略缓存，无论当前进程近期是否下载过都强制下载。|
|**Center**|AR中心模式：
* FirstTarget（默认）：以第一个跟踪到的 target 为中心。
* Camera：以 [ARAssembly.Camera](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Camera) 为中心。
* SpecificTarget：以 手动指定的 *target* 为中心。
* SessionOrigin：以 [ARSession.Origin](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Origin) 为中心。在编辑器内运行时，随 session 状态随时更新且修改立即生效。
参见：[中心模式](center-mode.html)|
|*Target*|手动指定的中心物体。
在编辑器内运行时，随 session 状态随时更新且修改立即生效。|
|*Current*|运行时表示 session 当前正在使用的中心物体。|
|**Horizontal Flip**|水平镜像渲染模式。仅在使用图像或物体跟踪时可用。
在编辑器内运行时，随 session 状态随时更新且修改立即生效。|
|*Back Camera*|后置摄像头的水平镜像渲染模式：
* None（默认）：不翻转。
* World：水平镜像渲染，camera 图像会镜像显示，camera 投影矩阵会变化进行镜像渲染，target scale 不会改变。
* Target：水平镜像渲染，camera 图像会镜像显示，target scale 会改变进行镜像渲染，camera 投影矩阵不会改变。|
|*Front Camera*|前置摄像头的水平镜像渲染模式：
* None：不翻转。
* World（默认）：水平镜像渲染，camera 图像会镜像显示，camera 投影矩阵会变化进行镜像渲染，target scale 不会改变。
* Target：水平镜像渲染，camera 图像会镜像显示，target scale 会改变进行镜像渲染，camera 投影矩阵不会改变。|
