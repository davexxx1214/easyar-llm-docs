---
source: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-unity-setup.html
---

如何安装 Unity 并使用 Mega Studio | EasyAR 文档
**
##### Table of Contents
**
# 如何安装 Unity 并使用 Mega Studio
这篇文章将介绍如何安装 Unity 以及如何下载并加载 Mega Unity 插件以在 Unity 编辑器上使用 Mega Studio。
## 安装 2021.3 或更高版本的 Unity 长期支持版本（LTS）
从 [Unity 官方网站](https://unity.com/download)，在中国大陆可以从[Unity 中文页面](https://unity.cn/releases)获取安装包，遵循官方指引进行安装。
您可以先下载 Unity Hub，之后在网页上选择 Unity 版本并从 Hub 下载或在 Unity Hub 中选择并安装。
![网页上安装Unity](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup01.png)
## 新建 Unity 项目
使用 **Built-in Render Pipeline**
![创建项目](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup05.png)
![下载模板](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup06.png)
在一些版本上，比如 Unity 6 ，您需要先下载对应的模板再创建项目
## 下载 Mega Unity 插件
![下载页面导航](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup07.png)
登录 EasyAR 账号，进入下载页面。
![下载Mega插件](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup08.png)
下载 **EasyAR Sense Unity Plugin(for Mega)**。
![解压文件](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup09.png)
解压下载的 `.zip` 压缩包后，您将获得以下目录结构：
##### 重要事项
注意：请勿解压 `.tgz` 文件。 这些是 Unity 软件包，需通过 Unity Package Manager 直接导入。
```
`.
└── EasyARSenseUnityPluginForMega\_\*\*.zip # 完整安装包
├── com.easyar.mega-\*\*.tgz # 包含标注工具及 Block 浏览工具
├── com.easyar.sense-\*\*.tgz # 包含 EasyAR Sense 核心库及 Unity 插件
├── readme.cn.txt # 中文自述文件
└── readme.en.txt # 英文自述文件
`
```
版本号说明： 文件名中的 \*\* 代表版本号，格式为：**Major.Minor.Patch + BuildNum.BuildHash** 。请以官方发布的最新版本为准。
## 在项目中导入 package （UPM 包）
请依次导入：
```
`com.easyar.sense-\*\*.tgz
com.easyar.mega-\*\*.tgz
`
```
##### 注意
在导入之前，建议将 `.tgz` 文件先拷贝到您的 Unity 项目文件夹内（例如存放在 Packages 目录下）。
导入后请勿移动或删除这些 `.tgz` 源文件，否则 Unity 将无法加载对应的包。
点击 **Window** &gt; **Package Management** &gt; **Package Manager** ，在弹出的窗口左上角点击 **+** 号，选择 **Install package from tarball...**
![Install package](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup10.png)
## 创建标注工具
在 **Hierarchy** 面板中空白处右键 **EasyAR Mega** &gt; **Tool** &gt; **Annotation Tool（Edit Mode）** 创建标注工具
![创建标注工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup11.png)
## 登录后使用 Mega Studio
在 **Hierarchy** 面板中点击 `EasyAR.Mega.Annotation`，在 **Inspector** 面板中输入 EasyAR 账号，密码后点击登录。
![登录 Mega Studio](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup12.png)
登陆成功后即可使用 Mega Studio 的编辑器功能。
![登录 Mega Studio 成功](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup13.png)
## 后续步骤
* [使用 Unity 编辑器摆放 3D 内容](content-simple.html)
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [在Unity 编辑器中模拟运行](content-simulation.html)