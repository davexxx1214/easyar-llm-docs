---
source: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-grading.html
original_file: doc--zh-cn--develop--cloud-recognition--management-grading.md
normalized_at: 2026-02-27
---
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
