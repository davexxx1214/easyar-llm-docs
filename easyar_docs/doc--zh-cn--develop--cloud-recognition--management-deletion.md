---
source: https://www.easyar.cn/doc/zh-cn/develop/cloud-recognition/management-deletion.html
---

删除目标图 | EasyAR 文档
**
##### Table of Contents
**
# 删除目标图
EasyAR 提供了两种方式处理不再需要的识别图：**永久删除**和**临时停用**。为了保证生产环境的稳定性，建议您仔细阅读以下操作说明。
## 通过 EasyAR Web 管理中心操作
* **操作步骤**：登录 EasyAR 开发中心 -&gt; 云识别管理 -&gt; 选择对应图库 -&gt; 点击 **管理** 进入图库管理界面。
* **删除方式**：
* **批量删除**：在列表中勾选目标图，点击 **删除** 并确认即可。
* **单个删除**：点击进入目标图详情页，点击页面内的 **删除** 按钮。
![删除操作引导](https://doc-asset.easyar.com/develop/cloud-recognition/media/m5-delete.png)
##### 警告
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
`curl -X DELETE "https://&lt;Your Server-side-URL&gt;/target/&lt;Your-todo-TargetId&gt;?appId=&lt;Your-CRS-AppId&gt;" \\
-H "Content-Type: application/json" \\
-H "Authorization: &lt;Your-Token&gt;"
`
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
`public class RemoveTarget {
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
`
```
Step 3. 运行 Main
下载 NodeJS 示例代码
* [NodeJS Samples Download](https://github.com/EasyAR-CRS/nodejs-sdk)
Step 1. 配置密钥文件 keys.json
* CRS AppId
* API Key / API Secret
* to-delete-targetId
```
`{
"appId": "--here is your appId for CRS App Instance for SDK 4--",
"apiKey": "--here is your api key which is create from website and which has crs permission--",
"apiSecret": "--here is your api secret which is create from website--"
}
`
```
Step 2. 运行，指定密钥文件以及 Server-end URL
```
`node bin/deleteTarget &lt;to-delete-targetId&gt; -t &lt;Server-end-URL&gt; -c keys.json
`
```
```
`var argv = require('yargs')
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
`
```
deleteTarget 调用云服务接口，示例代码在 farmer.js
```
`function deleteTarget(targetId) {
return Q.promise(function(resolve, reject) {
request.del(host + '/target/' + targetId)
.query(signParams())
.end(done(resolve, reject));
});
}
`
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
`&lt;?php
include 'EasyARClientSdkCRS.php';
$apiKey = 'API Key';
$apiSecret = 'API Secret';
$crsAppId = 'CRS AppId'
$crsCloudUrl = 'https://cn1-crs.easyar.com';
$toDeleteTargetId = 'to-delete-targetId';
$sdk = new EasyARClientSdkCRS($apiKey, $apiSecret, $crsAppId, $crsCloudUrl);
$rs = $sdk-&gt;delete($toDeleteTargetId);
if ($rs-&gt;statusCode == 0) {
print\_r($rs-&gt;result);
} else {
print\_r($rs);
}
`
```
Step 3. 运行 php demo.php
新建相关代码文件 delete\_target.py，修改全局变量，然后运行
```
`pip install requests
python delete\_target.py
`
```
```
`import time
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
`
```
新建相关代码文件 main.go，修改全局变量，然后运行
```
`go run main.go
`
```
`main.go:`
```
`package main
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
url := fmt.Sprintf("%s/target/%s?apiKey=%s&amp;appId=%s&amp;timestamp=%s&amp;signature=%s",
Host, TargetId, ApiKey, AppId, ts, signature)
req, \_ := http.NewRequest("DELETE", url, nil)
resp, \_ := http.DefaultClient.Do(req)
defer resp.Body.Close()
body, \_ := io.ReadAll(resp.Body)
fmt.Printf("Response: %s\\n", string(body))
}
`
```
在 Cargo.toml 中添加 reqwest, tokio, sha2, hex 依赖。
执行 cargo run。
```
`use sha2::{Sha256, Digest};
use std::collections::BTreeMap;
use std::time::{SystemTime, UNIX\_EPOCH};
const API\_KEY: &amp;str = "YOUR\_API\_KEY";
const API\_SECRET: &amp;str = "YOUR\_API\_SECRET";
const APP\_ID: &amp;str = "YOUR\_APP\_ID";
const HOST: &amp;str = "https://crs-cn1.easyar.com";
const TARGET\_ID: &amp;str = "YOUR\_TARGET\_ID";
#[tokio::main]
async fn main() -&gt; Result&lt;(), Box&lt;dyn std::error::Error&gt;&gt; {
let ts = SystemTime::now().duration\_since(UNIX\_EPOCH)?.as\_millis().to\_string();
let mut params = BTreeMap::new();
params.insert("apiKey", API\_KEY);
params.insert("appId", APP\_ID);
params.insert("timestamp", &amp;ts);
let mut sign\_str = String::new();
for (k, v) in &amp;params {
sign\_str.push\_str(k);
sign\_str.push\_str(v);
}
sign\_str.push\_str(API\_SECRET);
let mut hasher = Sha256::new();
hasher.update(sign\_str.as\_bytes());
let signature = hex::encode(hasher.finalize());
let url = format!("{}/target/{}?apiKey={}&amp;appId={}&amp;timestamp={}&amp;signature={}",
HOST, TARGET\_ID, API\_KEY, APP\_ID, ts, signature);
let res = reqwest::Client::new().delete(url).send().await?;
println!("Response: {}", res.text().await?);
Ok(())
}
`
```
创建 .NET 控制台项目。
```
`dotnet new console
dotnet run
`
```
```
`using System;
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
var dict = new SortedDictionary&lt;string, string&gt; {
{ "apiKey", API\_KEY },
{ "appId", APP\_ID },
{ "timestamp", timestamp }
};
StringBuilder sb = new StringBuilder();
foreach (var kv in dict) sb.Append(kv.Key).Append(kv.Value);
sb.Append(API\_SECRET);
string signature = Sha256(sb.ToString());
using var client = new HttpClient();
string query = string.Join("&amp;", dict.Select(x =&gt; $"{x.Key}={x.Value}")) + $"&amp;signature={signature}";
string url = $"{HOST}/target/{TARGET\_ID}?{query}";
var response = await client.DeleteAsync(url);
Console.WriteLine($"Result: {await response.Content.ReadAsStringAsync()}");
}
static string Sha256(string str) {
byte[] bytes = SHA256.HashData(Encoding.UTF8.GetBytes(str));
return BitConverter.ToString(bytes).Replace("-", "").ToLower();
}
}
`
```
* 运行环境
* Unity 2020 LTS 以上版本
* Scripting Backend：Mono 或 IL2CPP 均可
* API Compatibility Level：.NET Standard 2.1（推荐）
Step 1：准备图片文件
* 在 Unity 项目中创建目录：
```
`Assets/
└── Scripts/
└── DeleteImageTarget.cs
`
```
* 按照 Assets 目录名
* 复制下面示例代码 DeleteImageTarget.cs
```
`using System.Collections;
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
`
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