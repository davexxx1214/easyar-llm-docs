---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/quickstart.html
original_file: doc--zh-cn--develop--wechat--mega--quickstart.md
normalized_at: 2026-02-27
---
# 快速运行微信小程序 Mega 插件示例工程
这篇文章将介绍如何快速运行微信小程序 Mega 插件的示例工程。您将学习如何：
* 搭建与配置示例工程的开发环境。
* 运行示例的部分功能：使用 Mega 云定位。
## 开始之前
* 参考文档 [我的定位库可以使用了吗？](../../mega/localization-verify.html) 确认定位库已正确创建并添加 Mega Block。
## 确认小程序主体为企业主体
> **重要事项**
Mega 小程序插件**仅支持企业主体**的微信小程序。
个人主体类型的小程序**无法**使用 Mega 小程序插件。
需要确认在 [小程序后台](https://mp.weixin.qq.com) 中 **设置** > **基本信息** > **主体信息** 显示为 **企业法人或个体工商户**。
由于 Mega 功能以小程序插件形式提供，您必须拥有一个**企业主体**的微信小程序作为宿主环境。
即使仅为了运行我们提供的示例工程，您也需要配置**自己的微信小程序 AppID** 才能在开发者工具中进行调试和预览。
## 下载示例工程
1. 前往 [开发工具下载页面](https://www.easyar.cn/view/download.html)。
2. 确认 *EasyAR 隐私政策* 后点击下载。
![下载Sample](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart02.png)
3. 下载完成后，在本地解压缩 `.zip` 包。
## 配置示例工程
1. 登录微信小程序开发者工具。
2. 使用微信小程序开发者工具导入示例项目。
* 打开开发者工具后，点击导入按钮， 选择本地解压好的目录。
![导入开发者工具](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart03.png)
![选择本地目录](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart04.png)
* 确保 AppID 与 **申请 Mega 许可证时填写的 AppID** 一致，开发模式为**小程序**，点击创建。
> **注意**
AppID 不一致会导致许可证校验不通过
![导入开发者工具选项](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart05.png)
* 配置 Mega 许可证及云服务
打开文件 `miniprogram/components/sample-data/easyar-settings.ts`，根据准备工作中的许可证和服务信息填入该文件中的相应字段：
* **Mega 许可证**
```
/\*\* 您的小程序 Mega 许可证 \*/
export const EasyARLicenseKey: string = "";
```
**如何获取 Mega 微信小程序许可证**
>
> 在
> EasyAR 开发中心
> 中选择
> Mega 微信小程序
> 。
>
![许可证列表](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites04.png)
>
> 列表中应存在要使用的
> Mega 微信小程序许可证
> 。（若不存在可用许可证，请检查您的账号和用于创建 Mega 定位库的账号是否是同一个）
>
> 点击
> 小程序名称
> 可以获取该小程序的 Mega 许可证（点击右侧复制，然后粘贴至
`> easyar-settings.ts
`> 文件中作为
`> EasyARLicenseKey
`> 的值），并确认其关联的 AppID 与您的微信小程序 AppID 完全一致。
>
![许可证详细信息](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart13.png)
>
* **云服务 API Key 及 Seceret**
```
/\*\* 您的云服务 API Key 及 Seceret \*/
export const EasyARAPIKey: string = "";
export const EasyARAPISecret: string = "";
```
**如何获取云服务 API Key 及 Seceret**
>
> 在
> EasyAR 开发中心
> 选择
> 云服务 API KEY
> 。
>
> 若先前已经创建过云服务 API Key 及 Seceret，此处可以依次点击右侧复制，粘贴至
`> easyar-settings.ts
`> 文件中作为
`> EasyARAPIKey
`> 和
`> EasyARAPISecret
`> 的值。
>
![云服务 API KEY](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites08.png)
>
> 若之前没有创建过云服务 API Key 及 Seceret，可以通过以下方式创建：
>
> 在
> Easy> AR 开发中心
> 选择
> 云服务 API KEY
> >
> 创建 API KEY
> 。
>
![创建 API KEY](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites06.png)
>
![创建 API KEY 详细](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites07.png)
>
> 输入应用名称，选中需要使用的云服务：
> Mega Block
> 和/或
> Mega Landmark
> ，点击确定。
>
* **云服务 ServerAddress 及 AppID**：
```
/\*\* 您的 Mega 云定位库的 ServerAddress 及 AppID \*/
export const MegaTrackerServerAddress: string = "";
export const MegaTrackerAppID: string = "";
```
**如何获取 Mega 云定位库的 ServerAddress 及 AppID**
>
> 在
> EasyAR 开发中心
> 选择
> Block 云定位
> ，之后选择您的
> Mega 云定位服务组
> 。
>
![选择云定位服务组](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites09.png)
>
> 选择您的 Mega 云定位库：
>
![选择云定位库](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites10.png)
>
![获取云定位信息](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites11.png)
>
> 点击
> 密钥
> ，在下方依次获取云定位库的 AppID 和 Server Address （点击右侧复制，然后粘贴至
`> easyar-settings.ts
`> 文件中作为
`> MegaTrackerAppID
`> 和
`> MegaTrackerServerAddress
`> 的值）。
>
## 实机运行示例
1. 点击小程序开发工具上方栏的实机预览按钮，通过扫描二维码加载到开发用的手机。
> **小心**
不能在开发工具上直接模拟运行带有 AR 功能的 xr-frame 组件。
![模拟运行](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart07.png)
![二维码加载](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart06.png)
> **注意**
当您在微信开发者工具中首次运行示例项目时，如果尚未获得插件权限，工具通常会弹窗提示插件未授权。可以通过微信开发者工具自动授权，或参考 [插件接入流程](https://developers.weixin.qq.com/miniprogram/introduction/plugin.html#插件开发接入流程)
2. 点击 **EasyAR Mega Samples** 进入示例项目的 AR 场景。
![Sample入口](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart08.png)
> **注意**
若无法进入示例项目的 AR 场景，可能是由于当前设备不支持微信的视觉算法组件 VisionKit，具体请参考[机型限制](known-issues.html#wechat-mega-known-issues-devices)。
3. 屏幕中提示 `EasyAR Session is initializing` 表示微信平面检测正在初始化。
> **提示**
确保在光线充足的环境下测试，避开大面积纯色墙面或纯色地板。
对着地面或其他平面匀速左右摆动以加快这个过程。
![初始化](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart09.png)
4. 初始化完成后，将手机竖直使相机拍到正常的现实画面，当定位成功，Debug 信息中出现 `Found` 字样，并且右下方的状态指示物由白色变为绿色。
![定位](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart10.png)
## 后续步骤
* [在 Unity 里使用 Mega Studio](content-unity-setup.html)
* [使用 Unity 编辑器 摆放 3D 内容](content-simple.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
* [Mega 简介](../../mega/intro.html)
* [获取和使用 APIKey](../../apikey-auth.html)
