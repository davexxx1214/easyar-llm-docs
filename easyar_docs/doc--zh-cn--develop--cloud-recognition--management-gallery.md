---
source: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-gallery.html
original_file: doc--zh-cn--develop--cloud-recognition--management-gallery.md
normalized_at: 2026-02-27
---
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
