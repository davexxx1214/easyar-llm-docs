---
source: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-adding.html
original_file: doc--zh-cn--develop--cloud-recognition--management-adding.md
normalized_at: 2026-02-27
---
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
