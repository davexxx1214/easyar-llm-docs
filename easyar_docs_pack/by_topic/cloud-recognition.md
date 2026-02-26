# EasyAR 专题包：cloud-recognition

适用于上下文长度有限时的分卷输入。

## 目录
- `cloud-recognition/image-recognition-with-tracking.md`
- `cloud-recognition/intro.md`
- `cloud-recognition/management-adding.md`
- `cloud-recognition/management-deletion.md`
- `cloud-recognition/management-gallery.md`
- `cloud-recognition/management-grading.md`
- `cloud-recognition/management.md`

---

## 与平面图像跟踪的混合使用
- 章节路径: `cloud-recognition/image-recognition-with-tracking.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/image-recognition-with-tracking.html

# 与平面图像跟踪的混合使用
图像云识别还可与平面图像跟踪结合使用，实现“识别+持续跟踪”的混合模式。本篇将介绍如何使用，并分析其优势与适用场景。
## 工作流程
混合模式的核心是**云端识别**与**本地跟踪**的无缝衔接，流程如下：
### 云端识别阶段
1. **发送请求**：设备摄像头捕获当前画面，并将图像上传至 CRS 服务器。
2. **云端匹配**：CRS 在目标库中检索，返回匹配目标的 ID 以及图像数据（Base64 编码）。
3. **结果接收**：客户端收到识别结果，触发后续处理逻辑。
### 本地跟踪阶段
1. **图像解码**：客户端将 Base64 数据解码为图像，并据此在本地生成一个 `ImageTarget` 实例。
2. **初始化跟踪**：初始化 `ImageTracker` 并调用 `loadTarget` 方法，启动平面图像跟踪。
3. **持续跟踪**：设备本地计算 6DoF 位姿，虚拟内容实时跟随图像移动。
## 混合使用的优势
相比单独使用云识别，混合使用的模式在以下方面表现更优：
* **减少误识别概率**
单独使用云识别时，若目标库中有相似图像，可能返回错误目标。借助本地图像跟踪后，本地跟踪会持续验证图像特征。若图像实际内容与识别结果不匹配，跟踪会快速丢失，触发重新识别。 因此混合使用可极大地降低云识别的误识别率。
* **支持持续跟踪与交互**
单独使用云识别只能返回目标的 ID，无法支持旋转、缩放等持续交互。在混合模式下，识别后立即切换至本地跟踪，支持 6DoF 实时位姿更新。用户可移动设备或图像，虚拟内容始终跟随，适合 AR 游戏、产品展示等场景。
* **降低云端负载**
频繁调用云识别（如每秒1次）会增加服务器压力和延迟。在混合模式下，识别成功后，后续跟踪由设备本地完成，无需持续上传图像。仅在跟踪丢失时重新触发云识别，可以大幅度减少云端请求量，降低客户端的网络流量消耗。
* **弱网环境适应性**
单独使用云识别在网络不稳定时容易超时或失败。在混合模式下，一旦识别成功后，即使网络断开，本地跟踪仍可继续工作。可结合本地目标库，为应用在网络恢复前提供降级体验。
## 最佳实践
选择是否使用云识别、平面图像跟踪或混合模式时，可根据以下维度评估：
### 如何选择功能
|应用特点|推荐方案|理由|
|**目标数量 < 100个**|平面图像跟踪|本地内存充足，无需网络依赖|
|**无网络或网络不稳定**|平面图像跟踪|避免识别失败，确保离线可用|
|**目标需实时更新**|云识别|上传后立即生效，适合动态内容|
|**设备性能有限**|云识别|嵌入式设备或有极端功耗要求|
|**无持续跟踪需求**|云识别|如一次性扫描识别，无需跟踪|
### 何时选择混合模式
* **目标数量大（>100个）**：云端存储无限，本地仅加载当前目标，节省内存。
* **需要持续交互**：如 AR 教育（识别教材后旋转 3D 模型）、AR 营销（识别产品后查看 3D 演示）。
* **误识别敏感**：如医疗、工业场景，需确保识别准确性。
* **弱网环境需降级**：识别成功后，网络断开仍可继续跟踪。
## 总结与扩展
云识别与平面图像跟踪的混合模式结合了云端的大容量和本地的持续跟踪能力，特别适合需要高准确性和交互性的复杂场景。开发者应根据目标数量、更新频率、网络环境和交互需求，灵活选择单独功能或混合模式。

---

## 图像云识别简介
- 章节路径: `cloud-recognition/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/intro.html

# 图像云识别简介
本篇介绍 EasyAR CRS（Cloud Recognition Service）云识别功能的核心原理、预期效果及与平面图像跟踪的区别，帮助开发者理解云端识别的适用场景与限制。
## 基本原理
**云识别（Cloud Recognition）** 是一种将识别过程迁移到云端的方案，适用于目标库庞大或需要动态更新的场景。其核心流程如下：
### 图库管理
1. **创建图库**：在 CRS 控制台上传您的目标图像。系统会自动计算目标图像的视觉特征并作为一个 Target 添加到后台数据库中。
2. **增删改查**：在 CRS 控制台可以对您的目标库进行增、删、改、查等操作。操作完毕后，客户端无需更新应用即可使用。
> **重要事项**
用于云识别的目标图像对图像质量的要求与平面图像跟踪中的要求是完全一致的。详情参考：[目标图像最佳实践](../image-tracking/intro.html#bestpratice)。
### 识别流程
1. **图像上传**：客户端通过摄像头捕获当前画面，将图像数据发送至 EasyAR CRS 服务。
2. **云端匹配**：服务器在云端目标库中进行快速检索，匹配预存的 Target 数据（即开发者上传的目标图像）。
3. **结果返回**：匹配成功后，云端将识别结果（目标ID、目标图像等）返回至客户端，客户端据此显示虚拟内容或利用图像继续进行后续的跟踪。
### 与平面图像跟踪的区别
|特性|平面图像跟踪（本地）|云识别（云端）|
|**识别计算**|设备本地完成|云端服务器完成|
|**目标库大小**|受内存限制和加载时间的权衡，通常不建议超过100张|单库最大10万张目标图像，可扩充至亿级|
|**目标更新**|需重新打包分发应用|实时上传，立即生效|
|**网络依赖**|无需网络（离线可用）|必须联网（识别请求需网络）|
|**功能侧重**|识别并持续跟踪（输出 6DoF 位姿）|一次性识别（目标匹配）|
**关键说明**：
* **识别（Recognition）**：仅完成“这是什么目标”的匹配，不提供持续跟踪。若需跟踪，需结合本地平面图像跟踪功能。
* **适用场景**：目标数量多（如商品库、儿童绘本）、需频繁更新（如活动海报）或功能需求单一（如只需要识别不需要跟踪）。
## 服务使用与管理
EasyAR CRS 提供灵活、安全的云端目标管理方案，支持从个人开发到企业级应用的多样化需求。
### 图库隔离与安全
* **多图库支持**：您可以创建多个独立的 CRS 图库，每个图库之间完全隔离，目标不会冲突。例如：
* 图库 A：用于营销活动，存放产品海报。
* 图库 B：用于教育培训，存放教材插图。
* **安全机制**：每个图库通过唯一的 API Key 和 Secret 访问，确保数据安全。
### 并发量模式选择
根据应用规模和扫描量需求，CRS 提供两种并发模式：
|模式|适用场景|特点|开通方式|
|**基本并发量**|AR 应用 QPS < 50，一般扫描量|自助开通，稳定可靠|在 CRS 控制台在线申请|
|**高并发量**|AR 应用 QPS ≥ 50，大流量扫描|专享资源保障，低延迟|联系 [EasyAR 技术支持](mailto://support@easyar.com)，评估后开通|
> **提示**
初创项目或测试阶段可选择基本模式，应用上线后根据实际流量（如监控 QPS 识别请求量）决定是否升级。
### 图库管理与 API
* **图库管理**：日常操作（如创建、删除、上传目标）请参考 [图库管理](management.html) 章节，内含详细步骤和截图。
* **CRS API**：提供丰富的 REST API，支持以下场景：
* **健康检查**：通过 API 查询服务状态。
* **自动化**：批量上传、删除、修改、查询目标。
* **实用工具**：目标识别度打分，相似性冲突检查。
> **注意**
CRS 支持通过 SDK、微信小程序、Web 等方式集成使用。通过 SDK 集成仅支持 *EasyAR Sense v2.0.0* 及以上版本。
## 效果与预期结果
了解云识别的实际表现有助于开发者合理设定项目目标。以下是典型场景下的效果描述：
### 理想效果
* **识别速度快**：从拍摄到返回结果延迟 < 1秒（网络良好时）。
* **识别准确率高**：在目标图像清晰、网络稳定的情况下，准确率 > 98%。
* **支持大规模目标库**：单库可管理多达10万个目标识别图。
* **实时更新**：上传新目标后，客户端无需更新即可识别（仅需联网）。
### 不理想情况与应对
|现象|原因|用户感知|解决方案|
|**识别延迟高**|网络差、图像上传慢|需等待数秒才出现结果|应用上做适当提示|
|**识别失败**|图像模糊、目标未上传至云端|虚拟内容不出现|检查 CRS 目标库状态，引导用户稳定设备|
|**目标冲突**|目标库中相似图像过多|识别到错误目标|优化目标图像，增加区分度。或将相似图像分库管理|
### 预期结果验证方法
* **开发阶段**：在 EasyAR CRS 控制台上传测试目标，先通过 HelloARCRS 样例验证识别流程并熟悉应用逻辑，然后在自己的应用内进行集成。
* **测试阶段**：使用自己的应用在各种条件下测试识别成功率，如弱网环境、动态更新目标图像、增加云端图库大小等。
## 最佳实践
云识别通过云端计算扩展了目标库容量和动态更新能力，但牺牲了离线能力和实时跟踪。开发者需根据项目需求（目标数量、更新频率、网络环境等）选择方案：小规模静态场景用本地跟踪，大规模动态场景用云识别。
在使用 CRS 时，建议按照如下模式进行开发：
* **测试阶段**：使用基本并发模式，上传少量目标验证流程。
* **上线前**：评估预期并发量，提前联系技术支持升级高并发模式（需1\~2个工作日）。
* **运维阶段**：定期使用 API 监控图库健康状态，确保服务稳定。
> **重要事项**
**季节性流量高峰预警**：若您的应用在节假日、大型活动或营销推广期间可能面临临时并发量激增，请务必提前至少3个工作日联系 EasyAR 技术支持申请服务升级，以避免识别服务使用受限。
另外，如果您的应用需要大规模的图库，同时又需要有目标图像跟踪的需求，可以将云识别与平面图像跟踪功能结合起来使用。具体介绍和说明可以参阅 [与平面图像跟踪结合](image-recognition-with-tracking.html) 章节。
## 平台专用指南
* [快速入门](../wechat/cloud-recognition/quickstart.html)
* [开发者指南](../wechat/cloud-recognition/guide.html)
* [示例说明](../wechat/cloud-recognition/sample.html)
* [快速入门](../web/cloud-recognition/quickstart.html)
* [开发者指南](../web/cloud-recognition/guide.html)
* [示例说明](../web/cloud-recognition/sample.html)

---

## 创建目标图像 (Target)
- 章节路径: `cloud-recognition/management-adding.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-adding.html

# 创建目标图像 (Target)
为了确保 AR 识别的稳定性和准确性，建议您上传纹理丰富、特征点明显且无模糊区域的图像。
在开始集成前，请注意以下核心原则：
* **质量优先**：避免上传低对比度或纹理稀疏的图片。
* **避免冲突**：请勿上传内容高度相似的多张图像。虽然 EasyAR CRS 会返回最匹配的结果，但相似图会导致识别结果的置信度下降或出现意外跳转。
开始验证阶段可以通过[EasyAR Web 直接添加](management-adding.html#create-web)方法创建目标图。
创建目标图片对应 API 接口是：[API —— 新建目标图像](../../api/cloud/cloud-recognition/target-create.html)。
不推荐生产上直接通过[EasyAR Web 上传](management-adding.html#create-web) 或者直接调用[API —— 新建目标图像](../../api/cloud/cloud-recognition/target-create.html)上传目标图像。
推荐参考[创建目标图最佳实践](management-adding.html#create-best-practice)方法创建目标图。
## 创建目标图最佳实践
在生产环境下，我们强烈建议开发者遵循以下三步法通过 API 自动化管理目标图，而不是直接强制上传。
### 第一步：检查相似/冲突目标图
在正式添加之前，先检查当前图库中是否已存在相同或极度相似的目标。
* **工具**：使用 [相似性检查 API (similar)](../../api/cloud/cloud-recognition/target-similar.html)。
* **处理逻辑**：如果 API 返回了已存在的 `targetId`，建议您评估是否需要覆盖、删除旧图或停用冲突项，以确保识别逻辑的唯一性。
### 第二步：识别难度评级预检
利用算法预判图像是否适合作为识别目标图。
* **工具**：使用 [识别难度评分 API (grade)](../../api/cloud/cloud-recognition/target-grade.html)。
* **判定标准**：若测试发现目标图极难识别，建议更换素材。
* **参考指南**：详细评分标准请参阅 [识别难度评级说明](management-grading.html)。
### 第三步：正式上传目标图
在通过上述两项检查后，即可安全地执行上传操作。
* **工具**：调用 [新建目标图像 API](../../api/cloud/cloud-recognition/target-create.html)。
## 通过 EasyAR Web 手动管理
适用于验证阶段或维护少量目标图。Web 管理端采取“强制创建”模式，不会自动进行相似性校验，也不校验图片的可识别性。
**操作步骤**：
1. 登录 [EasyAR 开发中心](https://www.easyar.cn/view/login.html) -> **云识别管理** -> 选择图库 -> 点击 **管理**。
2. 在界面中点击 **上传目标图**。
![Web 创建引导](https://doc-asset.easyar.com/develop/cloud-recognition/media/m2-web-create-target.png)
1. **关键参数配置**：
* **名称 (Name)**：识别图的标识符。
* **宽度 (Width)**：填入图像在物理世界中的实际尺寸。这决定了 Unity 等客户端在识别后渲染 AR 内容的初始比例。
* **元数据 (Meta)**：存放与该图关联的 URL、模型路径或 JSON 配置。数据需先进行 **Base64 编码** 后上传。
![参数填写示例](https://doc-asset.easyar.com/develop/cloud-recognition/media/m2-target-name.png)
## 使用 API 自动化创建
如需大规模管理或集成到自有后台，请使用 Web Service REST API 自动化创建。
API 接口参考 [创建目标图像 API](../../api/cloud/cloud-recognition/target-create.html)
### 准备清单
在发起请求前，请确保获取以下资源（详见 [API 调用准备清单](management.html#prepare)）：
* **CRS AppId**
* **API Key / Secret** 或 **Token**
* **Server-end URL**（目标管理入口，https 的端口 443）
* **测试图片**（支持 JPEG/PNG 格式，需转为 Base64 字符串）
* 先将本地目标图片转为 Base64（macOS / Linux），结果存入 image\_base64.txt
```
base64 -i ./target.jpg | tr -d '\\n' > image\_base64.txt
```
* 请替换占位符为实际参数，并运行 curl 脚本
* Your-Server-side-URL → 实际 API Host
* Your-Token → 实际的 API Key Authorization Token
* Your-CRS-AppId → 您的 appId
* demo\_target → 目标名称
* size → 目标图片宽度(cm)
```
curl -X POST "https://<Your-Server-side-URL>/targets" \\
-H "Content-Type: application/json" \\
-H "Authorization: <YOUR-TOKEN>" \\
-d '{
"appId": "<Your-CRS-AppId>",
"image": "'"$(cat image\_base64.txt)"'",
"active": "1",
"name": "demo\_target",
"size": "20",
"type": "ImageTarget",
"allowSimilar": "1"
}'
```
下载 Java 示例代码
* [Java Samples Download](https://github.com/EasyAR-CRS/java-sdk)
通过 Maven 方式导入项目
Step 1. 打开相关代码文件 CreateTarget.java
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* Server-end URL
* IMAGE\_PATH : 待上传目标图文件
```
public class CreateTarget {
private static final String TARGET\_MGMT\_URL = "http://cn1.crs.easyar.com:8888";
private static final String CRS\_APPID = "--here is your CRS AppId--";
private static final String API\_KEY = "--here is your API Key--";
private static final String API\_SECRET = "--here is your API Secret--";
private static final String IMAGE\_PATH = "test\_target\_image.jpg";
public String create(Auth auth, String imgPath) throws IOException{
byte[] image = Files.readAllBytes(Paths.get(imgPath));
if(image.length > Common.MAXIMUM\_SIZE) {
System.err.println("maximum image size is 2MB");
System.exit(-1);
}
JSONObject params = new JSONObject()
.put("name", "java-sdk-test")
.put("image", Base64.getEncoder().encodeToString(image))
.put("type","ImageTarget")
.put("size", "20")
.put("meta", "Your customized meta info");
RequestBody requestBody = FormBody.create(MediaType.parse("application/json; charset=utf-8"),
Auth.signParam(params, auth.getAppId(), auth.getApiKey(), auth.getApiSecret()).toString());
Request request = new Request.Builder()
.url(auth.getCloudURL() + "/targets")
.post(requestBody)
.build();
return new OkHttpClient.Builder().readTimeout(120,TimeUnit.SECONDS).build().newCall(request).execute().body().string();
}
public static void main(String[] args) throws IOException {
Auth accessInfo = new Auth(CRS\_APPID, API\_KEY, API\_SECRET, TARGET\_MGMT\_URL);
JSONObject createResponse = new JSONObject(new CreateTarget().create(accessInfo, IMAGE\_PATH)).getJSONObject(Common.KEY\_RESULT);
System.out.println("created target: "+ createResponse.getString(Common.KEY\_TARGETID));
}
}
```
Step 3. 运行 Main
下载 NodeJS 示例代码
* [NodeJS Samples Download](https://github.com/EasyAR-CRS/nodejs-sdk)
Step 1. 配置密钥文件 keys.json
* CRS AppId
* API Key / API Secret
```
{
"appId": "--here is your appId for CRS App Instance for SDK 4--",
"apiKey": "--here is your api key which is create from website and which has crs permission--",
"apiSecret": "--here is your api secret which is create from website--"
}
```
Step 2. 运行，指定测试图片、密钥文件以及 Server-end URL
```
node bin/addTarget test.jpeg -t <Server-end-URL> -c keys.json
```
[可选] 目标图参数代码
添加目标图的逻辑，修改代码文件 addTarget.js
编辑目标图的参数，例如 meta，目标图名称等，对应 createTarget 方法里传入匿名 target 结构
```
var argv = require('yargs')
.usage('Usage: $0 [image] -t [host] -c [keys]')
.demand(1)
.default('t', 'http://localhost:8888').alias('t', 'host')
.default('c', 'keys.json').alias('c', 'keys')
.help('h').alias('h', 'help')
.epilog('copyright 2015, sightp.com')
.argv;
var fs = require('fs');
var imageFn = argv.\_[0];
var host = argv.host;
var keys = JSON.parse(fs.readFileSync(argv.keys));
var farmer = require('../farmer')(host, keys.appKey, keys.appSecret);
farmer.createTarget({
'image': fs.readFileSync(imageFn).toString('base64'),
'name':'test2',
'allowSimilar': '1',
'active':'1',
'size':'20',
'type':'imageTarget'
})
.then(function(resp) {
console.log(resp.result.targetId);
})
.fail(function(err) {
console.log(err);
});
```
createTarget 调用云服务接口，示例代码在 farmer.js
```
function createTarget(target) {
return Q.promise(function(resolve, reject) {
request.post(host + '/targets')
.send(signParams(target))
.end(done(resolve, reject));
});
}
```
新建相关代码文件 create\_target.py，修改全局变量，然后运行
```
pip install requests
python create\_target.py
```
```
import base64, hashlib, json, time, requests
APP\_ID = "your\_app\_id"
API\_KEY = "your\_api\_key"
API\_SECRET = "your\_api\_secret"
IMAGE\_PATH = "test.jpg"
API\_HOST = "https://cn1-crs.easyar.com"
def sha256\_hex(s: str) -> str:
return hashlib.sha256(s.encode()).hexdigest()
image\_b64 = base64.b64encode(open(IMAGE\_PATH, "rb").read()).decode()
timestamp = int(time.time() \* 1000)
sign\_params = {
"image": image\_b64,
"name": "demo\_target",
"size": "20",
"meta": "",
"type": "ImageTarget",
"timestamp": timestamp,
"appId": APP\_ID,
"apiKey": API\_KEY
}
sign\_str = "".join(f"{k}{sign\_params[k]}" for k in sorted(sign\_params)) + API\_SECRET
print(sign\_str)
signature = sha256\_hex(sign\_str)
body = dict(sign\_params)
body["signature"] = signature
headers = {
"Content-Type": "application/json",
"appId": APP\_ID
}
resp = requests.post(f"{API\_HOST}/targets", headers=headers, json=body)
print(resp.text)
```
下载 Php 示例代码
* [PHP Samples Download](https://github.com/EasyAR-CRS/php-sdk)
Step 1. 打开入口代码 demo.php
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* Server-end URL
* imageFilePath : 待上传目标图文件路径
```
<?php
include 'EasyARClientSdkCRS.php';
$apiKey = 'API Key';
$apiSecret = 'API Secret';
$crsAppId = 'CRS AppId'
$crsCloudUrl = 'https://cn1-crs.easyar.com';
$imageFilePath = '1.jpg'
$sdk = new EasyARClientSdkCRS($apiKey, $apiSecret, $crsAppId, $crsCloudUrl);
$params = [
'name' => 'image 1',
'active' => '1',
'size' => '1',
'meta' => base64\_encode('hello world'),
'image' => base64\_encode(file\_get\_contents($imageFilePath)),
];
$rs = $sdk->targetAdd($params);
if ($rs->statusCode == 0) {
print\_r($rs->result);
} else {
print\_r($rs);
}
```
Step 3. 运行 php demo.php
`Cargo.toml:`
```
[dependencies]
reqwest = { version = "0.11", features = ["json"] }
serde\_json = "1"
sha2 = "0.10"
base64 = "0.21"
tokio = { version = "1", features = ["full"] }
```
`main.rs:`
```
use std::{fs, collections::BTreeMap};
use sha2::{Sha256, Digest};
use base64::Engine;
use reqwest::Client;
use std::time::{SystemTime, UNIX\_EPOCH};
const APP\_ID: &str = "your\_app\_id";
const API\_KEY: &str = "your\_api\_key";
const API\_SECRET: &str = "your\_api\_secret";
const IMAGE\_PATH: &str = "test.jpg";
const API\_HOST: &str = "https://cn1-crs.easyar.com";
fn sha256\_hex(s: &str) -> String {
let mut h = Sha256::new();
h.update(s.as\_bytes());
format!("{:x}", h.finalize())
}
#[tokio::main]
async fn main() {
let img = fs::read(IMAGE\_PATH).unwrap();
let image\_b64 = base64::engine::general\_purpose::STANDARD.encode(img);
let timestamp = SystemTime::now()
.duration\_since(UNIX\_EPOCH).unwrap()
.as\_millis();
let mut sign = BTreeMap::new();
sign.insert("image", image\_b64);
sign.insert("name", "demo\_target".into());
sign.insert("size", "20".into());
sign.insert("meta", "".into());
sign.insert("type", "ImageTarget".into());
sign.insert("timestamp", timestamp.to\_string());
sign.insert("appId", APP\_ID.into());
sign.insert("apiKey", API\_KEY.into());
let mut raw = String::new();
for (k, v) in &sign {
raw.push\_str(&format!("{}{}", k, v));
}
raw.push\_str(API\_SECRET);
sign.insert("active", "1".into());
sign.insert("signature", sha256\_hex(&raw));
let client = Client::new();
let resp = client.post(format!("{}/targets", API\_HOST))
.header("Content-Type", "application/json")
.header("appId", APP\_ID)
.json(&sign)
.send().await.unwrap()
.text().await.unwrap();
println!("{}", resp);
}
```
```
cargo run
```
新建相关代码文件 main.go，修改全局变量，然后运行
```
go run main.go
```
`main.go:`
```
package main
import (
"bytes"
"crypto/sha256"
"encoding/base64"
"encoding/json"
"fmt"
"os"
"sort"
"net/http"
"time"
)
const (
AppID = "your\_app\_id"
ApiKey = "your\_api\_key"
ApiSecret = "your\_api\_secret"
ImagePath = "test.jpg"
ApiHost = "https://cn1-crs.easyar.com"
)
func sha256Hex(s string) string {
sum := sha256.Sum256([]byte(s))
return fmt.Sprintf("%x", sum)
}
func main() {
img, \_ := os.ReadFile(ImagePath)
imageB64 := base64.StdEncoding.EncodeToString(img)
timestamp := time.Now().UnixMilli()
sign := map[string]string{
"image": imageB64,
"name": "demo\_target",
"size": "20",
"meta": "",
"type": "ImageTarget",
"timestamp": fmt.Sprint(timestamp),
"appId": AppID,
"apiKey": ApiKey,
}
keys := make([]string, 0, len(sign))
for k := range sign { keys = append(keys, k) }
sort.Strings(keys)
builder := ""
for \_, k := range keys {
builder += k + sign[k]
}
builder += ApiSecret
signature := sha256Hex(builder)
sign["signature"] = signature
body, \_ := json.Marshal(sign)
req, \_ := http.NewRequest("POST", ApiHost+"/targets", bytes.NewReader(body))
req.Header.Set("Content-Type", "application/json")
resp, \_ := http.DefaultClient.Do(req)
defer resp.Body.Close()
buf := new(bytes.Buffer)
buf.ReadFrom(resp.Body)
fmt.Println(buf.String())
}
```
创建 .NET 控制台项目。
```
dotnet new console
dotnet run
```
```
using System;
using System.IO;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Collections.Generic;
using System.Linq;
class Program
{
const string APP\_ID = "your\_app\_id";
const string API\_KEY = "your\_api\_key";
const string API\_SECRET = "your\_api\_secret";
const string IMAGE\_PATH = "test.jpg";
const string API\_HOST = "https://cn1-crs.easyar.com";
static string Sha256(string s)
{
return Convert.ToHexString(
SHA256.HashData(Encoding.UTF8.GetBytes(s))
).ToLower();
}
static void Main()
{
var imageB64 = Convert.ToBase64String(File.ReadAllBytes(IMAGE\_PATH));
var timestamp = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds();
var sign = new SortedDictionary<string, string> {
["image"] = imageB64,
["name"] = "demo\_target",
["size"] = "20",
["type"] = "ImageTarget",
["timestamp"] = timestamp.ToString(),
["appId"] = APP\_ID,
["apiKey"] = API\_KEY
};
var builder = string.Concat(sign.Select(p => p.Key + p.Value)) + API\_SECRET;
sign["signature"] = Sha256(builder);
var json = JsonSerializer.Serialize(sign);
var client = new HttpClient();
var resp = client.PostAsync(
API\_HOST + "/targets",
new StringContent(json, Encoding.UTF8, "application/json")
).Result;
Console.WriteLine(resp.Content.ReadAsStringAsync().Result);
}
}
```
* 运行环境
* Unity 2020 LTS 以上版本
* Scripting Backend：Mono 或 IL2CPP 均可
* API Compatibility Level：.NET Standard 2.1（推荐）
Step 1：准备图片文件
* 在 Unity 项目中创建目录：
```
Assets/
└── StreamingAssets/
| └── target.jpg
└── Scripts/
└── CreateImageTarget.cs
```
* 按照 Assets 目录名
* 创建脚本 CreateImageTarget.cs，复制下面示例代码
* 准备一张图片目标测试图
```
using System;
using System.IO;
using System.Text;
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
public class CreateImageTarget : MonoBehaviour
{
[Header("Config")]
public string apiUrl = "https://Your-Server-end-URL" + "/targets";
public string authorizationToken = "YOUR API KEY AUTH TOKEN";
public string imageFilePath = "target.jpg"; // StreamingAssets
public string crsAppId = "<Your-CRS-AppId>";
private void Start()
{
StartCoroutine(CreateTarget());
}
private IEnumerator CreateTarget()
{
// Read image file（Unity StreamingAssets）
string fullPath = Path.Combine(Application.streamingAssetsPath, imageFilePath);
if (!File.Exists(fullPath))
{
Debug.LogError($"Image file not found: {fullPath}");
yield break;
}
byte[] imageBytes = File.ReadAllBytes(fullPath);
string imageBase64 = Convert.ToBase64String(imageBytes);
TargetRequestBody body = new TargetRequestBody
{
appId = crsAppId,
image = imageBase64,
active = "1",
name = "unity\_target",
size = "20",
meta = "created from unity",
type = "ImageTarget",
allowSimilar = "1"
};
string json = JsonUtility.ToJson(body);
// UnityWebRequest
UnityWebRequest request = new UnityWebRequest(apiUrl, "POST");
byte[] jsonBytes = Encoding.UTF8.GetBytes(json);
request.uploadHandler = new UploadHandlerRaw(jsonBytes);
request.downloadHandler = new DownloadHandlerBuffer();
request.SetRequestHeader("Content-Type", "application/json");
request.SetRequestHeader("Authorization", authorizationToken);
yield return request.SendWebRequest();
if (request.result == UnityWebRequest.Result.Success)
{
Debug.Log("Create target success:");
Debug.Log(request.downloadHandler.text);
}
else
{
Debug.LogError("Create target failed:");
Debug.LogError(request.error);
Debug.LogError(request.downloadHandler.text);
}
}
[Serializable]
private class TargetRequestBody
{
public string appId;
public string image;
public string active;
public string name;
public string size;
public string meta;
public string type;
public string allowSimilar;
}
}
```
* 在 Unity Editor 中：
* 创建一个空 GameObject
* 命名为 TargetUploader
* 将 CreateImageTarget 脚本拖到该对象上
Step 3：配置参数（Inspector）
* 在 Inspector 面板中修改。按照前面准备清单的数据修改。
* Api Url
* Authorization Token
* Image File Path : 默认 target.jpg
* CRS AppId
* 只需修改这四项即可运行，填入准备清单准备好的参数
Step 4：运行
* 点击 Play
* 在 Console 中查看结果：
* 成功：返回 JSON（含 targetId）
* 失败：HTTP / 错误信息
**相关主题：**
* [API Key 介绍](../apikey.html)
* [API Key 和 Token 使用指南](../apikey-auth.html)
* [如何使用 API Key / API Secret 签名](../apikey-auth.html#signature)
**下一主题：**
* [目标图列表查询](management-gallery.html)

---

## 删除目标图
- 章节路径: `cloud-recognition/management-deletion.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-deletion.html

# 删除目标图
EasyAR 提供了两种方式处理不再需要的识别图：**永久删除**和**临时停用**。为了保证生产环境的稳定性，建议您仔细阅读以下操作说明。
## 通过 EasyAR Web 管理中心操作
* **操作步骤**：登录 EasyAR 开发中心 -> 云识别管理 -> 选择对应图库 -> 点击 **管理** 进入图库管理界面。
* **删除方式**：
* **批量删除**：在列表中勾选目标图，点击 **删除** 并确认即可。
* **单个删除**：点击进入目标图详情页，点击页面内的 **删除** 按钮。
![删除操作引导](https://doc-asset.easyar.com/develop/cloud-recognition/media/m5-delete.png)
> **警告**
**删除操作不可逆**。一旦确认删除，该图像的所有特征数据及关联信息将永久丢失。建议先在测试图库中验证流程，严禁直接在生产环境进行破坏性测试。
## 最佳实践：目标图停用
在大多数业务场景下，如果您不确定是否未来还会用到某张图，推荐使用 **停用** 代替 **删除**。
* **功能特点**：停用后的目标图保留在数据库列表中，但**不会**参与云识别搜索过程。但会占用识别配额。
* **停用方法**：在管理界面勾选识别图，点击 **停用** 即可。
![停用操作引导](https://doc-asset.easyar.com/develop/cloud-recognition/media/m5-inactive.png)
* **API 停用**：通过调用 [更新目标图 API](../../api/cloud/cloud-recognition/target-update.html)，将 `active` 属性设置为 `0`。
## 使用 API 删除目标图
通过 REST API 可以实现识别图的自动化清理。
### 准备工作
开始前请阅读 [删除目标图 API 文档](../../api/cloud/cloud-recognition/target-delete.html)，并准备好以下资源：
* **CRS AppId**
* **API Key / Secret** 或 **Token**
* **Server-end URL** (443 端口)
* **TargetId**：待删除目标图的唯一 ID。若 TargetId 不存在，API 将返回 `statusCode: 404` (Target not found)。
请替换占位符为实际参数，并运行 curl 脚本
* Your-Server-side-URL → 实际 API Host
* Your-Token → 实际的 API Key Authorization Token
* Your-CRS-AppId → 您的 appId
* Your-todo-TargetId → 待删除目标 targetId
```
curl -X DELETE "https://<Your Server-side-URL>/target/<Your-todo-TargetId>?appId=<Your-CRS-AppId>" \\
-H "Content-Type: application/json" \\
-H "Authorization: <Your-Token>"
```
下载 Java 示例代码
* [Java Samples Download](https://github.com/EasyAR-CRS/java-sdk)
通过 Maven 方式导入项目
Step 1. 打开相关代码文件 RemoveTarget.java
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* TARGET\_MGMT\_URL → Server-end URL
* TARGET\_ID → 待删除目标 targetId
```
public class RemoveTarget {
private static final String TARGET\_MGMT\_URL = "https://cn1.crs.easyar.com";
private static final String CRS\_APPID = "--here is your CRS AppId--";
private static final String API\_KEY = "--here is your API Key--";
private static final String API\_SECRET = "--here is your API Secret--";
private static final String TARGET\_ID = "my\_targetid";
/\* TO\_DEL\_IDs lists all the targetIds to be removed
\* must be separated by ","
\*/
private static final String TO\_DEL\_IDs = "targetId1,targetId2,targetId3";
public String remove(Auth auth, String targetId) throws IOException {
okhttp3.Request request = new okhttp3.Request.Builder()
.url(auth.getCloudURL()+"/target/"+targetId+"?"+ Common.toParam(
Auth.signParam(new JSONObject(), auth.getAppId(), auth.getApiKey(), auth.getApiSecret())
))
.delete()
.build();
return new OkHttpClient.Builder().build().newCall(request).execute().body().string();
}
public String removeMultiTargets(Auth auth, String targetIds) throws IOException {
JSONObject params = new JSONObject().put("targetId", targetIds);
Auth.signParam(params, auth.getAppId(), auth.getApiKey(), auth.getApiSecret());
RequestBody requestBody = FormBody.create(MediaType.parse("application/json; charset=utf-8")
, params.toString());
okhttp3.Request request = new okhttp3.Request.Builder()
.url(auth.getCloudURL() + "/targets")
.delete(requestBody)
.build();
return new OkHttpClient.Builder().build().newCall(request).execute().body().string();
}
public static void main(String[] args) throws IOException{
Auth accessInfo = new Auth(CRS\_APPID, API\_KEY, API\_SECRET, TARGET\_MGMT\_URL);
System.out.println(new RemoveTarget().remove(accessInfo, TARGET\_ID));
System.out.println(new RemoveTarget().removeMultiTargets(accessInfo, TO\_DEL\_IDs));
}
}
```
Step 3. 运行 Main
下载 NodeJS 示例代码
* [NodeJS Samples Download](https://github.com/EasyAR-CRS/nodejs-sdk)
Step 1. 配置密钥文件 keys.json
* CRS AppId
* API Key / API Secret
* to-delete-targetId
```
{
"appId": "--here is your appId for CRS App Instance for SDK 4--",
"apiKey": "--here is your api key which is create from website and which has crs permission--",
"apiSecret": "--here is your api secret which is create from website--"
}
```
Step 2. 运行，指定密钥文件以及 Server-end URL
```
node bin/deleteTarget <to-delete-targetId> -t <Server-end-URL> -c keys.json
```
```
var argv = require('yargs')
.usage('Usage: $0 [targetId] -t [host] -c [keys]')
.demand(1)
.default('t', 'http://localhost:8888').alias('t', 'host')
.default('c', 'keys.json').alias('c', 'keys')
.help('h').alias('h', 'help')
.epilog('copyright 2015, sightp.com')
.argv;
var fs = require('fs');
var targetId = argv.\_[0];
var host = argv.host;
var keys = JSON.parse(fs.readFileSync(argv.keys));
var farmer = require('../farmer')(host, keys.appKey, keys.appSecret);
farmer.deleteTarget(targetId)
.then(function(resp) {
console.log(resp.result.targetId);
})
.fail(function(err) {
console.log(err);
});
```
deleteTarget 调用云服务接口，示例代码在 farmer.js
```
function deleteTarget(targetId) {
return Q.promise(function(resolve, reject) {
request.del(host + '/target/' + targetId)
.query(signParams())
.end(done(resolve, reject));
});
}
```
下载 Php 示例代码
* [PHP Samples Download](https://github.com/EasyAR-CRS/php-sdk)
Step 1. 打开入口代码 demo.php
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* Server-end URL
* toDeleteTargetId
```
<?php
include 'EasyARClientSdkCRS.php';
$apiKey = 'API Key';
$apiSecret = 'API Secret';
$crsAppId = 'CRS AppId'
$crsCloudUrl = 'https://cn1-crs.easyar.com';
$toDeleteTargetId = 'to-delete-targetId';
$sdk = new EasyARClientSdkCRS($apiKey, $apiSecret, $crsAppId, $crsCloudUrl);
$rs = $sdk->delete($toDeleteTargetId);
if ($rs->statusCode == 0) {
print\_r($rs->result);
} else {
print\_r($rs);
}
```
Step 3. 运行 php demo.php
新建相关代码文件 delete\_target.py，修改全局变量，然后运行
```
pip install requests
python delete\_target.py
```
```
import time
import hashlib
import requests
# --- 全局变量配置 ---
API\_KEY = "YOUR\_API\_KEY"
API\_SECRET = "YOUR\_API\_SECRET"
APP\_ID = "YOUR\_APP\_ID"
HOST = "https://crs-cn1.easyar.com"
TARGET\_ID = "TARGET\_ID"
def main():
timestamp = str(int(time.time() \* 1000))
params = {
'apiKey': API\_KEY,
'appId': APP\_ID,
'timestamp': timestamp
}
sorted\_keys = sorted(params.keys())
sign\_str = "".join([f"{k}{params[k]}" for k in sorted\_keys]) + API\_SECRET
signature = hashlib.sha256(sign\_str.encode('utf-8')).hexdigest()
url = f"{HOST}/target/{TARGET\_ID}"
final\_params = {\*\*params, 'signature': signature}
print(f"Requesting DELETE {url}...")
response = requests.delete(url, params=final\_params)
print(f"Response: {response.text}")
if \_\_name\_\_ == "\_\_main\_\_":
main()
```
新建相关代码文件 main.go，修改全局变量，然后运行
```
go run main.go
```
`main.go:`
```
package main
import (
"crypto/sha256"
"fmt"
"io"
"net/http"
"sort"
"strconv"
"time"
)
var (
ApiKey = "YOUR\_API\_KEY"
ApiSecret = "YOUR\_API\_SECRET"
AppId = "YOUR\_APP\_ID"
Host = "https://crs-cn1.easyar.com"
TargetId = "TARGET\_ID"
)
func main() {
ts := strconv.FormatInt(time.Now().UnixNano()/1e6, 10)
params := map[string]string{
"apiKey": ApiKey,
"appId": AppId,
"timestamp": ts,
}
keys := make([]string, 0, len(params))
for k := range params { keys = append(keys, k) }
sort.Strings(keys)
builder := ""
for \_, k := range keys { builder += k + params[k] }
builder += ApiSecret
signature := fmt.Sprintf("%x", sha256.Sum256([]byte(builder)))
url := fmt.Sprintf("%s/target/%s?apiKey=%s&appId=%s&timestamp=%s&signature=%s",
Host, TargetId, ApiKey, AppId, ts, signature)
req, \_ := http.NewRequest("DELETE", url, nil)
resp, \_ := http.DefaultClient.Do(req)
defer resp.Body.Close()
body, \_ := io.ReadAll(resp.Body)
fmt.Printf("Response: %s\\n", string(body))
}
```
在 Cargo.toml 中添加 reqwest, tokio, sha2, hex 依赖。
执行 cargo run。
```
use sha2::{Sha256, Digest};
use std::collections::BTreeMap;
use std::time::{SystemTime, UNIX\_EPOCH};
const API\_KEY: &str = "YOUR\_API\_KEY";
const API\_SECRET: &str = "YOUR\_API\_SECRET";
const APP\_ID: &str = "YOUR\_APP\_ID";
const HOST: &str = "https://crs-cn1.easyar.com";
const TARGET\_ID: &str = "YOUR\_TARGET\_ID";
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
let ts = SystemTime::now().duration\_since(UNIX\_EPOCH)?.as\_millis().to\_string();
let mut params = BTreeMap::new();
params.insert("apiKey", API\_KEY);
params.insert("appId", APP\_ID);
params.insert("timestamp", &ts);
let mut sign\_str = String::new();
for (k, v) in &params {
sign\_str.push\_str(k);
sign\_str.push\_str(v);
}
sign\_str.push\_str(API\_SECRET);
let mut hasher = Sha256::new();
hasher.update(sign\_str.as\_bytes());
let signature = hex::encode(hasher.finalize());
let url = format!("{}/target/{}?apiKey={}&appId={}&timestamp={}&signature={}",
HOST, TARGET\_ID, API\_KEY, APP\_ID, ts, signature);
let res = reqwest::Client::new().delete(url).send().await?;
println!("Response: {}", res.text().await?);
Ok(())
}
```
创建 .NET 控制台项目。
```
dotnet new console
dotnet run
```
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Net.Http;
class Program {
static string API\_KEY = "API\_KEY";
static string API\_SECRET = "API\_SECRET";
static string APP\_ID = "APP\_ID";
static string HOST = "https://crs-cn1.easyar.com";
static string TARGET\_ID = "TARGET\_ID";
static async System.Threading.Tasks.Task Main() {
string timestamp = DateTimeOffset.Now.ToUnixTimeMilliseconds().ToString();
var dict = new SortedDictionary<string, string> {
{ "apiKey", API\_KEY },
{ "appId", APP\_ID },
{ "timestamp", timestamp }
};
StringBuilder sb = new StringBuilder();
foreach (var kv in dict) sb.Append(kv.Key).Append(kv.Value);
sb.Append(API\_SECRET);
string signature = Sha256(sb.ToString());
using var client = new HttpClient();
string query = string.Join("&", dict.Select(x => $"{x.Key}={x.Value}")) + $"&signature={signature}";
string url = $"{HOST}/target/{TARGET\_ID}?{query}";
var response = await client.DeleteAsync(url);
Console.WriteLine($"Result: {await response.Content.ReadAsStringAsync()}");
}
static string Sha256(string str) {
byte[] bytes = SHA256.HashData(Encoding.UTF8.GetBytes(str));
return BitConverter.ToString(bytes).Replace("-", "").ToLower();
}
}
```
* 运行环境
* Unity 2020 LTS 以上版本
* Scripting Backend：Mono 或 IL2CPP 均可
* API Compatibility Level：.NET Standard 2.1（推荐）
Step 1：准备图片文件
* 在 Unity 项目中创建目录：
```
Assets/
└── Scripts/
└── DeleteImageTarget.cs
```
* 按照 Assets 目录名
* 复制下面示例代码 DeleteImageTarget.cs
```
using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
public class DeleteImageTarget : MonoBehaviour
{
[Header("Config")]
public string targetId = "Your targetId";
public string apiBaseUrl = "https://Your-Server-end-URL";
public string authorizationToken = "YOUR API KEY AUTH TOKEN";
public string crsAppId = "CRS-AppId";
private void Start()
{
StartCoroutine(DeleteTarget());
}
private IEnumerator DeleteTarget()
{
string url =
$"{apiBaseUrl}/target/{targetId}?appId={crsAppId}";
UnityWebRequest request = UnityWebRequest.Delete(url);
request.downloadHandler = new DownloadHandlerBuffer();
request.SetRequestHeader("Content-Type", "application/json");
request.SetRequestHeader("Authorization", authorizationToken);
yield return request.SendWebRequest();
if (request.result == UnityWebRequest.Result.Success)
{
Debug.Log("Delete target success:");
Debug.Log(request.downloadHandler.text);
}
else
{
Debug.LogError("Delete target failed:");
Debug.LogError(request.error);
Debug.LogError(request.downloadHandler.text);
}
}
}
```
* 在 Unity Editor 中：
* 创建一个空 GameObject
* 命名为 DeleteTarget
* 将 DeleteImageTarget 脚本拖到该对象上
Step 3：配置参数（Inspector）
* 在 Inspector 面板中修改：
* Api Url
* Authorization Token
* Crs App Id
* Target Id : 待删除目标图的 targetId
* 只需修改这几项即可运行，填入准备清单准备好的参数
Step 4：运行
* 点击 Play
* 在 Console 中查看结果：
* 成功：返回 JSON（含 targetId）
* 失败：HTTP / 错误信息
**相关主题：**
* [API Key 介绍](../apikey.html)
* [API Key 和 Token 使用指南](../apikey-auth.html)
* [如何使用 API Key / API Secret 签名](../apikey-auth.html#signature)

---

## 目标图列表查询
- 章节路径: `cloud-recognition/management-gallery.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-gallery.html

# 目标图列表查询
云识别（CRS）数据库中通常存储着海量的目标图。为了方便开发者快速定位和管理这些数据，本章将详细介绍目标图的查看、分页查询及详情说明。
## 通过 EasyAR Web 管理目标图集合
在可视化界面中，系统默认采用**分页列表**形式展示目标图，并按照**最后修改时间进行逆序排列**（最新改动的排在最前）。
### 目标图集合
**操作路径**：登录 EasyAR Web [开发中心] -> [云识别管理] -> 选择图库 -> 点击 [管理]。
在此界面中，您可以进行以下操作：
* **列表浏览**：查看分页展示的目标图集合。
* **详情入口**：点击图中 按钮1 的 **[管理]** 可进入该目标图的详情页。
* **精准检索**：在输入框2 中，支持以下两种检索方式：
* **按名称检索**：若您的系统按规则（如应用内 ID）命名图片，可通过名称快速定位。
* **按 TargetId 检索**：例如当您通过相似图查询接口获得具体 `targetId` 后，可在此查询其详细配置。
![filter](https://doc-asset.easyar.com/develop/cloud-recognition/media/m4-filter.png)
### 目标图详情说明
点击进入详情页后，您可以查看到目标图的完整属性，包括：
* **灰度图**
* **图片名称**：自定义的目标图标识。
* **TargetId**：系统生成的唯一 ID。
* **状态**：显示当前目标图是否处于激活或禁用状态。
* **质量评分**：关于识别与跟踪性能的量化评分，详情参考 [目标图识别难度评级](management-grading.html)。
* **自定义 Meta**：该目标图关联的元数据（如模型 URL 等）
![detail](https://doc-asset.easyar.com/develop/cloud-recognition/media/m4-detail.png)
## 使用 API 查询目标图集合
对于需要集成到自有后台的开发者，建议使用 REST API 进行管理。
**参考文档**：[目标图集合列表 API 接口](../../api/cloud/cloud-recognition/target-list.html)
### 准备清单
在发起请求前，请确保已准备好以下信息（详情请参考 [API 调用准备清单](management.html#prepare)）:
* CRS AppId
* API Key / API Secret 或者 Token
* Server-end URL: 目标图像管理 URL 地址，https 使用 443 端口
请替换占位符为实际参数，并运行 curl 脚本
* Your-Server-side-URL → 实际 API Host
* Your-Token → 实际的 API Key Authorization Token
* Your-CRS-AppId → 您的 appId
```
curl -X GET "https://<Your Server-side-URL>/targets/infos?appId=<Your-CRS-AppId>" \\
-H "Content-Type: application/json" \\
-H "Authorization: <Your-Token>"
```
下载 Java 示例代码
* [Java Samples Download](https://github.com/EasyAR-CRS/java-sdk)
通过 Maven 方式导入项目
Step 1. 打开相关代码文件 ListTargets.java
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* TARGET\_MGMT\_URL → Server-end URL
```
public class ListTargets {
private static final String TARGET\_MGMT\_URL = "http://cn1.crs.easyar.com:8888";
private static final String CRS\_APPID = "--here is your CRS AppId--";
private static final String API\_KEY = "--here is your API Key--";
private static final String API\_SECRET = "--here is your API Secret--";
public String list(Auth auth) throws IOException {
OkHttpClient client = new OkHttpClient.Builder().build();
JSONObject params = new JSONObject();
Auth.signParam(params, auth.getAppId(), auth.getApiKey(), auth.getApiSecret());
okhttp3.Request request = new okhttp3.Request.Builder()
.url(auth.getCloudURL() + "/targets/infos?"+ Common.toParam(params))
.get()
.build();
Response response = client.newCall(request).execute();
return response.body().string();
}
public static void main(String[] args) throws IOException{
Auth accessInfo = new Auth(CRS\_APPID, API\_KEY, API\_SECRET, TARGET\_MGMT\_URL);
System.out.println(new ListTargets().list(accessInfo));
}
}
```
Step 3. 运行 Main
下载 NodeJS 示例代码
* [NodeJS Samples Download](https://github.com/EasyAR-CRS/nodejs-sdk)
Step 1. 配置密钥文件 keys.json
* CRS AppId
* API Key / API Secret
```
{
"appId": "--here is your appId for CRS App Instance for SDK 4--",
"apiKey": "--here is your api key which is create from website and which has crs permission--",
"apiSecret": "--here is your api secret which is create from website--"
}
```
Step 2. 运行，指定密钥文件以及 Server-end URL
```
node bin/getTargets -t <Server-end-URL> -c keys.json
```
若需更改分页策略，传入 getTargets 分页参数
* 'pageSize': 分页大小
* 'pageNum': 第几页
```
var argv = require('yargs')
.usage('Usage: $0 [targetId] -t [host] -c [keys]')
.demand(0)
.default('t', 'http://localhost:8888').alias('t', 'host')
.default('c', 'keys.json').alias('c', 'keys')
.help('h').alias('h', 'help')
.epilog('copyright 2015, sightp.com')
.argv;
var fs = require('fs');
var host = argv.host;
var keys = JSON.parse(fs.readFileSync(argv.keys));
var farmer = require('../farmer')(host, keys.appKey, keys.appSecret);
farmer.getTargets({
'pageSize': 5,
'pageNum': 1,
})
.then(function(resp) {
console.log(resp.result.targets);
})
.fail(function(err) {
console.log(err);
});
```
getTargets 调用云服务接口，示例代码在 farmer.js
```
function getTargetsByPage(pageNum,pageSize) {
return Q.promise(function(resolve, reject) {
request.get(host + '/targets/infos?pageNum=' + pageNum + '&pageSize=' + pageSize)
.query(auth.signParams(keypair, {
"pageNum":pageNum,
"pageSize":pageSize
}))
.end(done(resolve, reject));
});
}
```
下载 Php 示例代码
* [PHP Samples Download](https://github.com/EasyAR-CRS/php-sdk)
Step 1. 打开入口代码 demo.php
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* Server-end URL
```
<?php
include 'EasyARClientSdkCRS.php';
$apiKey = 'API Key';
$apiSecret = 'API Secret';
$crsAppId = 'CRS AppId'
$crsCloudUrl = 'https://cn1-crs.easyar.com';
$pageNum = 1;
$pageSize = 5;
$sdk = new EasyARClientSdkCRS($apiKey, $apiSecret, $crsAppId, $crsCloudUrl);
$rs = $sdk->targetsV3($pageNum, $pageSize);
if ($rs->statusCode == 0) {
print\_r($rs->result);
} else {
print\_r($rs);
}
```
Step 3. 运行 php demo.php
新建相关代码文件 list\_targets.py，修改全局变量，然后运行
```
pip install requests
python list\_targets.py
```
```
import time
import hashlib
import requests
# --- Global Configuration ---
API\_KEY = "YOUR\_API\_KEY"
API\_SECRET = "YOUR\_API\_SECRET"
APP\_ID = "YOUR\_APP\_ID"
HOST = "https://crs-cn1.easyar.com"
def main():
timestamp = str(int(time.time() \* 1000))
params = {
'apiKey': API\_KEY,
'appId': APP\_ID,
'timestamp': timestamp
}
# Signature: Sort keys -> Concat -> Append Secret -> SHA256
sorted\_keys = sorted(params.keys())
sign\_str = "".join([f"{k}{params[k]}" for k in sorted\_keys]) + API\_SECRET
signature = hashlib.sha256(sign\_str.encode('utf-8')).hexdigest()
url = f"{HOST}/targets/infos"
params['signature'] = signature
print(f"Requesting GET {url}...")
response = requests.get(url, params=params)
print(f"Response: {response.text}")
if \_\_name\_\_ == "\_\_main\_\_":
main()
```
新建相关代码文件 main.go，修改全局变量，然后运行
```
go run main.go
```
`main.go:`
```
package main
import (
"crypto/sha256"
"fmt"
"io"
"net/http"
"sort"
"strconv"
"time"
)
// --- Global Configuration ---
var (
ApiKey = "YOUR\_API\_KEY"
ApiSecret = "YOUR\_API\_SECRET"
AppId = "YOUR\_APP\_ID"
Host = "https://crs-cn1.easyar.com"
)
func main() {
ts := strconv.FormatInt(time.Now().UnixNano()/1e6, 10)
params := map[string]string{
"apiKey": ApiKey,
"appId": AppId,
"timestamp": ts,
}
keys := make([]string, 0, len(params))
for k := range params { keys = append(keys, k) }
sort.Strings(keys)
builder := ""
for \_, k := range keys { builder += k + params[k] }
builder += ApiSecret
signature := fmt.Sprintf("%x", sha256.Sum256([]byte(builder)))
url := fmt.Sprintf("%s/targets/infos?apiKey=%s&appId=%s&timestamp=%s&signature=%s",
Host, ApiKey, AppId, ts, signature)
resp, \_ := http.Get(url)
defer resp.Body.Close()
body, \_ := io.ReadAll(resp.Body)
fmt.Printf("Response: %s\\n", string(body))
}
```
在 Cargo.toml 中添加 reqwest, tokio, sha2, hex 依赖。
执行 cargo run。
```
use sha2::{Sha256, Digest};
use std::collections::BTreeMap;
use std::time::{SystemTime, UNIX\_EPOCH};
// --- Global Configuration ---
const API\_KEY: &str = "YOUR\_API\_KEY";
const API\_SECRET: &str = "YOUR\_API\_SECRET";
const APP\_ID: &str = "YOUR\_APP\_ID";
const HOST: &str = "https://crs-cn1.easyar.com";
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
let ts = SystemTime::now().duration\_since(UNIX\_EPOCH)?.as\_millis().to\_string();
let mut params = BTreeMap::new();
params.insert("apiKey", API\_KEY);
params.insert("appId", APP\_ID);
params.insert("timestamp", &ts);
let mut sign\_str = String::new();
for (k, v) in &params {
sign\_str.push\_str(k);
sign\_str.push\_str(v);
}
sign\_str.push\_str(API\_SECRET);
let mut hasher = Sha256::new();
hasher.update(sign\_str.as\_bytes());
let signature = hex::encode(hasher.finalize());
let url = format!("{}/targets/infos?apiKey={}&appId={}&timestamp={}&signature={}",
HOST, API\_KEY, APP\_ID, ts, signature);
let res = reqwest::get(url).await?;
println!("Response: {}", res.text().await?);
Ok(())
}
```
创建 .NET 控制台项目。
```
dotnet new console
dotnet run
```
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Net.Http;
class Program {
// --- Global Configuration ---
static string API\_KEY = "YOUR\_API\_KEY";
static string API\_SECRET = "YOUR\_API\_SECRET";
static string APP\_ID = "YOUR\_APP\_ID";
static string HOST = "https://crs-cn1.easyar.com";
static async System.Threading.Tasks.Task Main() {
string timestamp = DateTimeOffset.Now.ToUnixTimeMilliseconds().ToString();
var dict = new SortedDictionary<string, string> {
{ "apiKey", API\_KEY },
{ "appId", APP\_ID },
{ "timestamp", timestamp }
};
StringBuilder sb = new StringBuilder();
foreach (var kv in dict) sb.Append(kv.Key).Append(kv.Value);
sb.Append(API\_SECRET);
string signature = Sha256(sb.ToString());
using var client = new HttpClient();
string query = string.Join("&", dict.Select(x => $"{x.Key}={x.Value}")) + $"&signature={signature}";
string url = $"{HOST}/targets/infos?{query}";
var response = await client.GetAsync(url);
Console.WriteLine($"Result: {await response.Content.ReadAsStringAsync()}");
}
static string Sha256(string str) {
byte[] bytes = SHA256.HashData(Encoding.UTF8.GetBytes(str));
return BitConverter.ToString(bytes).Replace("-", "").ToLower();
}
}
```
* 运行环境
* Unity 2020 LTS 以上版本
* Scripting Backend：Mono 或 IL2CPP 均可
* API Compatibility Level：.NET Standard 2.1（推荐）
Step 1：准备图片文件
* 在 Unity 项目中创建目录：
```
Assets/
└── Scripts/
└── ListImageTarget.cs
```
* 按照 Assets 目录名
* 复制下面示例代码 ListImageTarget.cs
```
using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
public class ListImageTarget : MonoBehaviour
{
[Header("Config")]
public string apiBaseUrl = "https://Your-Server-end-URL";
public string authorizationToken = "YOUR API KEY AUTH TOKEN";
public string crsAppId = "CRS-AppId";
public int pageSize = 5;
public int pageNum = 1;
private void Start()
{
StartCoroutine(ListTarget());
}
private IEnumerator ListTarget()
{
string url =
$"{apiBaseUrl}/targets/infos?appId={crsAppId}&pageSize={pageSize}&pageNum={pageNum}";
UnityWebRequest request = UnityWebRequest.Get(url);
request.downloadHandler = new DownloadHandlerBuffer();
request.SetRequestHeader("Content-Type", "application/json");
request.SetRequestHeader("Authorization", authorizationToken);
yield return request.SendWebRequest();
if (request.result == UnityWebRequest.Result.Success)
{
Debug.Log("List target success:");
Debug.Log(request.downloadHandler.text);
}
else
{
Debug.LogError("List target failed:");
Debug.LogError(request.error);
Debug.LogError(request.downloadHandler.text);
}
}
}
```
* 在 Unity Editor 中：
* 创建一个空 GameObject
* 命名为 ListTarget
* 将 ListImageTarget 脚本拖到该对象上
Step 3：配置参数（Inspector）
* 在 Inspector 面板中修改：
* Api Url
* Authorization Token
* Crs App Id
* page size
* page num
* 只需修改这几项即可运行，填入准备清单准备好的参数
Step 4：运行
* 点击 Play
* 在 Console 中查看结果：
* 成功：返回 JSON（含 targetId）
* 失败：HTTP / 错误信息
**相关主题：**
* [API Key 介绍](../apikey.html)
* [API Key 和 Token 使用指南](../apikey-auth.html)
* [如何使用 API Key / API Secret 签名](../apikey-auth.html#signature)
**下一主题：**
* [删除目标图像](management-deletion.html)

---

## 图像识别难度评级
- 章节路径: `cloud-recognition/management-grading.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-grading.html

# 图像识别难度评级
在将图像正式添加到云识别（CRS）图库之前，**最佳实践**是预先对其进行质量评估。
如果目标图的可识别区域过少（如白墙、纯色色块）或纹理过于简单，其识别成功率将大幅降低。本章将详细介绍 CRS 的评级机制，帮助您筛选高质量的 AR 识别素材。
## 评级机制与分数含义
|分值|评价|建议|
|**0 - 1**|优秀|纹理极其丰富，识别速度快，跟踪非常稳定。|
|**2**|良好|具备足够的特征点，能够正常进行 AR 业务。|
|**3**|一般|识别率可能受光照或角度影响，建议优化纹理。|
|**4**|较差|极难识别，不建议作为生产环境的识别图。|
|**-1**|错误|图片格式不支持或文件损坏。|
> **重要事项**
**实际测试原则**：如果图库内目标总数较少，即使评级分稍高，在特定环境下可能依然可用。建议以实际真机测试效果为准。
### 核心综合指标
我们主要关注以下两个综合指标，这两个指标有单独的 API 接口，给出综合评级：
* **识别难度综合级别 (detectableRate)**：
* **最核心指标**。决定了云端“以图搜图”的成功率。
* [`/grade/detection` API 接口](../../api/cloud/cloud-recognition/target-grade.html)给出的综合评级
* **跟踪难度综合级别 (trackableRate)**：
* 如果您在 Unity/App 端使用 **EasyAR Sense SDK** 进行本地跟踪，该指标决定了 AR 内容叠加的稳定性。
* [`/grade/tracking` API 接口](../../api/cloud/cloud-recognition/target-grade.html)给出的综合评级
### 其它细节指标
* detectableDistinctiveness
* detectableFeatureCount
* trackableDistinctiveness
* trackableFeatureCount
* trackableFeatureDistribution
* trackablePatchContrast
* trackablePatchAmbiguity
这些指标从图像算法维度来评级，每个指标依然是依据难度从 0 到 4 给出。
## 如何浏览评级结果
数据库的每张目标图的详情里都有目标图的详细评级。可通过 API 获取目标图属性查看。也可以通过 EasyAR 云识别管理查看。
### 通过 EasyAR Web 查看
* 登录 EasyAR Web 进入开发中心
* 云识别管理
* 选择开通的图库
* 点击`管理`进入图库管理
* 选中目标图
* 点`管理`查看目标是图的详情。
如图所示，详情页中有两项核心综合指标，以及五边形展示了五个细节指标。
* 可识别度：依据原识别难度综合分数 (detectableRate) 对应成可识别度五星级别。原难度分越小，星星越多，越容易识别
* 可跟踪度：依据原跟踪难度综合分数 (trackableRate) 对应成可跟踪度五星级别。原难度分越小，星星越多，越容易识别
![detail](https://doc-asset.easyar.com/develop/cloud-recognition/media/m4-detail-rate.png)
### API 获取评级结果 —— 目标图列表接口
通过 [目标图列表接口](../../api/cloud/cloud-recognition/target-list.html) 或获取详情，可以得到每个目标图包含 `detectableRate` 在内的所有详细算法指标（如纹理分布、特征点数量等）。
## 最佳实践：API 预先评级
在构建自动化上传后台时，建议在正式上传前调用评级接口。
**参考文档**：[图片识别难度评级 API 接口](../../api/cloud/cloud-recognition/target-grade.html)
### 评级接口分类
1. **识别评级 (`/grade/detection`)**：仅返回识别难度。**（最常用）**
2. **跟踪评级 (`/grade/tracking`)**：仅返回跟踪难度。
3. **详细评级 (`/grade/detail`)**：返回多维度指标，供专业算法人员参考。
### 调用准备
* 准备清单如下，如何准备请参考[调用准备清单](management.html#prepare)
* **CRS AppId**
* **鉴权凭证**: API Key / API Secret 或者 Token
* **Server-end URL**: 目标图像管理 URL 地址，https 使用 443 端口
* **测试图片**: JPEG/PNG 格式，大小不得超过 **2 MB**
* 先将本地目标图片转为 Base64（macOS / Linux），结果存入 image\_base64.txt
```
base64 -i ./target.jpg | tr -d '\\n' > image\_base64.txt
```
* 请替换占位符为实际参数，并运行 curl 脚本
* Your-Server-side-URL → 实际 API Host
* Your-Token → 实际的 API Key Authorization Token
* Your-CRS-AppId → 您的 appId
```
curl -X POST "https://<Your-Server-side-URL>/grade/detail" \\
-H "Content-Type: application/json" \\
-H "Authorization: <YOUR-TOKEN>" \\
-d '{
"appId": "<Your-CRS-AppId>",
"image": "'"$(cat image\_base64.txt)"'"
}'
```
下载 Java 示例代码
* [Java Samples Download](https://github.com/EasyAR-CRS/java-sdk)
通过 Maven 方式导入项目
Step 1. 打开相关代码文件 Grade.java
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* Server-end URL
* IMAGE\_PATH : 待上传目标图文件
```
import okhttp3.\*;
import org.json.JSONObject;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
public class Grade {
private static final String TARGET\_MGMT\_URL = "http://cn1.crs.easyar.com:8888";
private static final String CRS\_APPID = "--here is your CRS AppId--";
private static final String API\_KEY = "--here is your API Key--";
private static final String API\_SECRET = "--here is your API Secret--";
private static final String IMAGE\_PATH = "test\_target\_image.jpg";
enum GradeType {
DETAIL,
DETECTION,
TRACKING
}
private static final Map<GradeType, String> GRADE\_URL = new HashMap<GradeType, String>(){
{
put(GradeType.DETAIL, "/grade/detail") ;
put(GradeType.DETECTION, "/grade/detection") ;
put(GradeType.TRACKING, "/grade/tracking") ;
}
};
public String grade(Auth auth, String imgPath, GradeType gradeType) throws IOException {
final Path mImagePath = Paths.get(imgPath);
JSONObject params = new JSONObject().put("image", Base64.getEncoder().encodeToString(
Files.readAllBytes(mImagePath)
));
Auth.signParam(params, auth.getAppId(), auth.getApiKey(), auth.getApiSecret());
RequestBody requestBody = FormBody.create(MediaType.parse("application/json; charset=utf-8")
, params.toString());
Request request = new Request.Builder()
.url(auth.getCloudURL() + GRADE\_URL.get(gradeType))
.post(requestBody)
.build();
return new OkHttpClient.Builder().build().newCall(request).execute().body().string();
}
public static void main(String[] args) throws IOException {
Auth accessInfo = new Auth(CRS\_APPID, API\_KEY, API\_SECRET, TARGET\_MGMT\_URL);
System.out.println("================== grade details ==================");
System.out.println(new Grade().grade(accessInfo, IMAGE\_PATH, GradeType.DETAIL));
System.out.println("================== grade for detection ==================");
JSONObject gradeResp = new JSONObject(new Grade().grade(accessInfo, IMAGE\_PATH, GradeType.DETECTION));
System.out.println("Detection grade: " + gradeResp.getJSONObject(Common.KEY\_RESULT).get(Common.KEY\_GRADE));
System.out.println("================== grade for tracking =================== ");
gradeResp = new JSONObject(new Grade().grade(accessInfo, IMAGE\_PATH, GradeType.TRACKING));
System.out.println("Tracking grade: " + gradeResp.getJSONObject(Common.KEY\_RESULT).get(Common.KEY\_GRADE));
}
}
```
Step 3. 运行 Main
下载 NodeJS 示例代码
* [NodeJS Samples Download](https://github.com/EasyAR-CRS/nodejs-sdk)
Step 1. 配置密钥文件 keys.json
* CRS AppId
* API Key / API Secret
```
{
"appId": "--here is your appId for CRS App Instance for SDK 4--",
"apiKey": "--here is your api key which is create from website and which has crs permission--",
"apiSecret": "--here is your api secret which is create from website--"
}
```
Step 2. 运行，指定测试图片、密钥文件以及 Server-end URL
```
node bin/grade test.jpeg -t <Server-end-URL> -c keys.json
```
```
var argv = require('yargs')
.usage('Usage: $0 [image] -t [host] -c [keys]')
.demand(1)
.default('t', 'http://localhost:8888').alias('t', 'host')
.default('c', 'keys.json').alias('c', 'keys')
.help('h').alias('h', 'help')
.epilog('copyright 2015, sightp.com')
.argv;
var fs = require('fs');
var imageFn = argv.\_[0];
var host = argv.host;
var keys = JSON.parse(fs.readFileSync(argv.keys));
var farmer = require('../farmer')(host, keys);
farmer.getTrackingGrade({
'image': fs.readFileSync(imageFn).toString('base64')
})
.then(function(resp) {
console.log(resp);
})
.fail(function(err) {
console.log(err);
});
```
下载 Php 示例代码
* [PHP Samples Download](https://github.com/EasyAR-CRS/php-sdk)
Step 1. 打开入口代码 demo.php
Step 2. 修改全局变量，替换你准备清单里的认证参数
* CRS AppId
* API Key / API Secret
* Server-end URL
* imageFilePath : 待上传目标图文件路径
```
<?php
include 'EasyARClientSdkCRS.php';
$apiKey = 'API Key';
$apiSecret = 'API Secret';
$crsAppId = 'CRS AppId'
$crsCloudUrl = 'https://cn1-crs.easyar.com';
$imageFilePath = '1.jpg'
$sdk = new EasyARClientSdkCRS($apiKey, $apiSecret, $crsAppId, $crsCloudUrl);
$image = base64\_encode(file\_get\_contents($imageFilePath));
$rs = $sdk->detection($image);
if ($rs->statusCode == 0) {
print\_r($rs->result->grade);
} else {
print\_r($rs);
}
```
Step 3. 运行 php demo.php
新建相关代码文件 grade.py，修改全局变量，然后运行
```
pip install requests
python grade.py
```
```
import time
import hashlib
import requests
import base64
# --- Global Configuration ---
API\_KEY = "YOUR\_API\_KEY"
API\_SECRET = "YOUR\_API\_SECRET"
APP\_ID = "YOUR\_APP\_ID"
HOST = "https://crs-cn1.easyar.com"
IMAGE\_PATH = "test.jpg"
def main():
# 1. Read and encode image
with open(IMAGE\_PATH, "rb") as f:
image\_base64 = base64.b64encode(f.read()).decode('utf-8')
timestamp = str(int(time.time() \* 1000))
# 2. Build parameter dictionary (including image)
params = {
'apiKey': API\_KEY,
'appId': APP\_ID,
'timestamp': timestamp,
'image': image\_base64
}
# 3. Sort by key and concatenate
sorted\_keys = sorted(params.keys())
builder = "".join([f"{k}{params[k]}" for k in sorted\_keys])
builder += API\_SECRET
# 4. Generate SHA256 Signature
signature = hashlib.sha256(builder.encode('utf-8')).hexdigest()
# 5. Send POST request
payload = {\*\*params, "signature": signature, "timestamp": int(timestamp)}
response = requests.post(f"{HOST}/grade/detection", json=payload)
print(f"Status: {response.status\_code}")
print(f"Response: {response.text}")
if \_\_name\_\_ == "\_\_main\_\_":
main()
```
新建相关代码文件 main.go，修改全局变量，然后运行
```
go run main.go
```
`main.go:`
```
package main
import (
"bytes"
"crypto/sha256"
"encoding/base64"
"encoding/json"
"fmt"
"io"
"net/http"
"os"
"sort"
"strconv"
"time"
)
var (
ApiKey = "YOUR\_API\_KEY"
ApiSecret = "YOUR\_API\_SECRET"
AppId = "YOUR\_APP\_ID"
Host = "https://crs-cn1.easyar.com"
ImagePath = "test.jpg"
)
func main() {
fileData, \_ := os.ReadFile(ImagePath)
imgBase64 := base64.StdEncoding.EncodeToString(fileData)
tsInt := time.Now().UnixNano() / 1e6
tsStr := strconv.FormatInt(tsInt, 10)
params := map[string]string{
"apiKey": ApiKey,
"appId": AppId,
"timestamp": tsStr,
"image": imgBase64,
}
keys := make([]string, 0, len(params))
for k := range params { keys = append(keys, k) }
sort.Strings(keys)
var builder bytes.Buffer
for \_, k := range keys {
builder.WriteString(k)
builder.WriteString(params[k])
}
builder.WriteString(ApiSecret)
signature := fmt.Sprintf("%x", sha256.Sum256(builder.Bytes()))
payload := map[string]interface{}{
"image": imgBase64,
"apiKey": ApiKey,
"appId": AppId,
"timestamp": tsInt,
"signature": signature,
}
jsonBytes, \_ := json.Marshal(payload)
resp, \_ := http.Post(Host+"/grade/detection", "application/json", bytes.NewBuffer(jsonBytes))
defer resp.Body.Close()
body, \_ := io.ReadAll(resp.Body)
fmt.Printf("Response: %s\\n", string(body))
}
```
在 Cargo.toml 中添加 reqwest, tokio, sha2, hex 依赖。
执行 cargo run。
```
use sha2::{Sha256, Digest};
use std::collections::BTreeMap;
use std::time::{SystemTime, UNIX\_EPOCH};
use base64::{Engine as \_, engine::general\_purpose};
const API\_KEY: &str = "YOUR\_API\_KEY";
const API\_SECRET: &str = "YOUR\_API\_SECRET";
const APP\_ID: &str = "YOUR\_APP\_ID";
const HOST: &str = "https://crs-cn1.easyar.com";
const IMAGE\_PATH: &str = "test.jpg";
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
let img\_bytes = std::fs::read(IMAGE\_PATH)?;
let img\_b64 = general\_purpose::STANDARD.encode(img\_bytes);
let ts\_raw = SystemTime::now().duration\_since(UNIX\_EPOCH)?.as\_millis();
let ts\_str = ts\_raw.to\_string();
// 1. Collect params in BTreeMap for automatic sorting
let mut params = BTreeMap::new();
params.insert("apiKey", API\_KEY);
params.insert("appId", APP\_ID);
params.insert("timestamp", &ts\_str);
params.insert("image", &img\_b64);
// 2. Build sign string
let mut builder = String::new();
for (k, v) in &params {
builder.push\_str(k);
builder.push\_str(v);
}
builder.push\_str(API\_SECRET);
// 3. Hash
let mut hasher = Sha256::new();
hasher.update(builder.as\_bytes());
let signature = hex::encode(hasher.finalize());
let mut body = serde\_json::Map::new();
body.insert("image".into(), img\_b64.into());
body.insert("apiKey".into(), API\_KEY.into());
body.insert("appId".into(), APP\_ID.into());
body.insert("timestamp".into(), ts\_raw.into());
body.insert("signature".into(), signature.into());
let client = reqwest::Client::new();
let res = client.post(format!("{}/grade/detection", HOST))
.json(&body)
.send()
.await?;
println!("Response: {}", res.text().await?);
Ok(())
}
```
创建 .NET 控制台项目。
```
dotnet new console
dotnet run
```
```
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Net.Http;
using System.Text.Json;
class Program {
static string API\_KEY = "YOUR\_API\_KEY";
static string API\_SECRET = "YOUR\_API\_SECRET";
static string APP\_ID = "YOUR\_APP\_ID";
static string HOST = "https://crs-cn1.easyar.com";
static string IMAGE\_PATH = "test.jpg";
static async System.Threading.Tasks.Task Main() {
string timestamp = DateTimeOffset.Now.ToUnixTimeMilliseconds().ToString();
string imageBase64 = Convert.ToBase64String(File.ReadAllBytes(IMAGE\_PATH));
// 1. Prepare data for signing
var data = new SortedDictionary<string, string> {
{ "apiKey", API\_KEY },
{ "appId", APP\_ID },
{ "timestamp", timestamp },
{ "image", imageBase64 }
};
// 2. Concatenate keys and values
StringBuilder sb = new StringBuilder();
foreach (var pair in data) sb.Append(pair.Key).Append(pair.Value);
sb.Append(API\_SECRET);
string signature = Sha256(sb.ToString());
// 3. Construct JSON body
var body = new {
image = imageBase64,
apiKey = API\_KEY,
appId = APP\_ID,
timestamp = long.Parse(timestamp),
signature = signature
};
using var client = new HttpClient();
var content = new StringContent(JsonSerializer.Serialize(body), Encoding.UTF8, "application/json");
var response = await client.PostAsync($"{HOST}/grade/detection", content);
Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
}
static string Sha256(string str) {
byte[] bytes = SHA256.HashData(Encoding.UTF8.GetBytes(str));
return BitConverter.ToString(bytes).Replace("-", "").ToLower();
}
}
```
* 运行环境
* Unity 2020 LTS 以上版本
* Scripting Backend：Mono 或 IL2CPP 均可
* API Compatibility Level：.NET Standard 2.1（推荐）
Step 1：准备图片文件
* 在 Unity 项目中创建目录：
```
Assets/
└── StreamingAssets/
| └── target.jpg
└── Scripts/
└── GrageImage.cs
```
* 按照 Assets 目录名
* 创建脚本 GrageImage.cs，复制下面示例代码
* 准备一张图片目标测试图
```
using System;
using System.IO;
using System.Text;
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
public class GrageImage : MonoBehaviour
{
[Header("Config")]
public string apiUrl = "https://Your-Server-end-URL" + "/grade/detection";
public string authorizationToken = "YOUR API KEY AUTH TOKEN";
public string imageFilePath = "target.jpg"; // StreamingAssets
public string crsAppId = "<Your-CRS-AppId>";
private void Start()
{
StartCoroutine(Grade());
}
private IEnumerator Grade()
{
// Read image file（Unity StreamingAssets）
string fullPath = Path.Combine(Application.streamingAssetsPath, imageFilePath);
if (!File.Exists(fullPath))
{
Debug.LogError($"Image file not found: {fullPath}");
yield break;
}
byte[] imageBytes = File.ReadAllBytes(fullPath);
string imageBase64 = Convert.ToBase64String(imageBytes);
TargetRequestBody body = new TargetRequestBody
{
appId = crsAppId,
image = imageBase64,
};
string json = JsonUtility.ToJson(body);
// UnityWebRequest
UnityWebRequest request = new UnityWebRequest(apiUrl, "POST");
byte[] jsonBytes = Encoding.UTF8.GetBytes(json);
request.uploadHandler = new UploadHandlerRaw(jsonBytes);
request.downloadHandler = new DownloadHandlerBuffer();
request.SetRequestHeader("Content-Type", "application/json");
request.SetRequestHeader("Authorization", authorizationToken);
yield return request.SendWebRequest();
if (request.result == UnityWebRequest.Result.Success)
{
Debug.Log("Grade detail success:");
Debug.Log(request.downloadHandler.text);
}
else
{
Debug.LogError("Grade detail failed:");
Debug.LogError(request.error);
Debug.LogError(request.downloadHandler.text);
}
}
[Serializable]
private class TargetRequestBody
{
public string appId;
public string image;
}
}
```
* 在 Unity Editor 中：
* 创建一个空 GameObject
* 命名为 GradeImage
* 将 GrageImage 脚本拖到该对象上
Step 3：配置参数（Inspector）
* 在 Inspector 面板中修改。按照前面准备清单的数据修改。
* Api Url
* Authorization Token
* Image File Path : 默认 target.jpg
* CRS AppId
* 只需修改这四项即可运行，填入准备清单准备好的参数
Step 4：运行
* 点击 Play
* 在 Console 中查看结果：
* 成功：返回 JSON（result 含有对象）
* 失败：HTTP / 错误信息
**相关主题：**
* [API Key 介绍](../apikey.html)
* [API Key 和 Token 使用指南](../apikey-auth.html)
* [如何使用 API Key / API Secret 签名](../apikey-auth.html#signature)
**下一主题：**
* [创建目标图像](management-adding.html)

---

## 目标图像管理
- 章节路径: `cloud-recognition/management.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management.html

# 目标图像管理
目标图像（Targets）可以通过以下两种方式进行管理：
* **可视化管理**：登录 EasyAR 开发中心进行手动维护。
* **API 自动化管理**：通过调用 **Web Service REST API** 集成到自有业务系统或管理后台中。
> **重要事项**
云识别服务中，目标图管理和图像识别是两个不同需求，API 对应两个不同的 Cloud URL 入口。
### 数据中心区域选择
图库运行示例所在的数据中心支持以下区域选择：
* **中国-上海**
* **美国-硅谷**
## 方法1：在 EasyAR 开发中心管理目标图
适用于小规模测试或手动快速上传。操作步骤如下：
1. 登录 EasyAR 开发中心，进入 **云识别管理**。
2. 选择目标区域。若尚未创建图库，请先新建并开通云识别图库。
3. 在图库列表中点击 **管理**，即可进入目标图维护界面进行上传、修改或删除。
## ![create-web](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-crs-manage.png)
## 方法2：使用 REST API 进行自动化管理
对于需要处理大量目标图的应用，推荐使用 Web Service REST API，以便在您的应用程序或管理后台中实现自动化流程。
### 准备清单
以下是待准备清单。在您开始管理目标图像之前，您需要准备一个新的云识别数据库实例（Cloud Database）
* CRS AppId
* [API Key](../apikey.html) / API Secret 或者 Token
* Cloud URL
* Server-end URL：目标图像管理 URL 地址，https 使用 443 端口
* Client-end URL：图像识别服务 URL 地址，https 使用 8443 端口
> **重要事项**
**端口区分说明**：目标管理 API 入口（443）与移动端/Unity 调用的云识别 API 入口（8443）是两个不同的通道，配置时请务必区分。
### 清单各项如何获取
* CRS AppId 查看方式：
开发中心 -> 云识别管理 -> 选择图库 -> 管理 -> 密钥
![m1-appid](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-crs-appid.png)
* API Key / API Secret 查看方式：
开发中心 -> 云服务 APIKey -> 复制
![m1-apikey](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-apikey.png)
如您还没有 API Key，创建 APIKey，必须选中云识别（CRS） 权限。进一步了解 API Key 以及权限控制，参考主题[API Key 简介](../apikey.html)
![m1-apikey-cr](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-apikey-create.png)
* Token 查看方式：
开发中心 -> 云服务 APIKey -> 管理 -> 选择有效期 -> 生成 Token -> 复制
![m1-token](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-token.png)
若您需要自定义 Token 的有效期，可以参考 [UAC API —— 创建 Token](../apikey-auth.html) 方式，使用原始 APIKey 和 APISecret 来创建 Token
* Cloud URL 查看方式：
图库中目标图管理使用的是 Server-end URL 443 端口，Server-end URL
开发中心 -> 云识别管理 -> 选择图库 -> 管理 -> 密钥 -> 图库管理
![m1-server-url](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-server-url.png)
### 多端集成指引
在实际工作流中，目标图管理通常集成在开发者的业务服务器里，或者移动端或者 Unity 里：
* 业务服务平台：提供有常用服务器开发语言（Curl/Java/NodeJS/PHP）调用 API 示例代码，帮助开发者实现目标图的自动上传与元数据（Meta）更新。
* 移动端（Unity/Mobile）：提供基于 Unity 的目标图管理示例代码，开发者自己实现拍照上传目标图的方式。
运行示例代码
下图是一个 Java 示例代码使用，在示例代码中填写您自己的准备清单的各项，然后运行 Main
![m1-java](https://doc-asset.easyar.com/develop/cloud-recognition/media/m1-java.png)
### 相关主题：
* [云识别 APIs 简介](../../api/cloud/cloud-recognition/apis.html)
* [API Key 介绍](../apikey.html)
**下一主题：**
* [图像识别难度评估](management-grading.html)
* [创建目标图像](management-adding.html)
> **注意**
实际工作流中，创建目标图像建议遵循最佳实现，建议认真阅读。
