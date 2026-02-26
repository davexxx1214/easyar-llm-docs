---
source: https://www.easyar.cn/doc/zh-cn/develop/apikey-auth.html
---

获取和使用 API Key | EasyAR 文档
**
##### Table of Contents
**
# 获取和使用 API Key
在 EasyAR 开发中心创建 API Key 无数量限制，建议为不同应用分配独立的 API Key，以便更精细地管控权限。
## 创建 API Key
登录到 EasyAR [开发中心](https://www.easyar.cn/view/login.html)，如果您是首次使用 API Key，请先创建一个 API Key，步骤如下：
* 在“授权”下，点击“云服务 API KEY”
* 在“API KEY”页面点击“创建 API KEY”按钮
![APIKey](https://doc-asset.easyar.com/develop/media/api-key-1.jpg)
* 填写“应用名称”
* 根据您的应用需求进行勾选所需云服务，不建议全部授权。
* 点击“确定”
##### 提示
使用 [SpatialMap](sparse-spatial-mapping/intro.html)，勾选 SpatialMap。
使用[云识别](cloud-recognition/intro.html)，勾选云识别。
使用 Mega Landmark，勾选 Mega Landmark，使用此功能前需要向商务申请。
使用 AR 运营中心，勾选 AR 运营中心，使用此功能前需要向商务申请。
使用 [Mega Block 云定位](mega/intro.html)，勾选 Mega Block。
![APIKey](https://doc-asset.easyar.com/develop/media/api-key-2.jpg)
* 此时会在页面生成 API Key 与 API Secret，如下图所示，注意不要泄露。
![APIKey](https://doc-asset.easyar.com/develop/media/api-key-3.jpg)
##### 警告
不要在客户端（如 Web，微信小程序等）应用上直接使用 API Key 与 API Secret。
## 获取 Token
有两种方式可以获取到 Token：1. 从开发中心直接获取；2. 编写代码获取。如果你对资源的访问权限有控制需求，建议使用第2种方式。下面将分别介绍这两种获取方式，可根据您的需求自行选择。
### 从开发中心获取 Token
* 选择一个您要使用的 API Key，点击右侧的“管理”
![APIKeyToken](https://doc-asset.easyar.com/develop/media/api-token-1.jpg)
* 选择一个 Token 的有效期
* 点击“生成 Token”
* 点击“复制”即可
![APIKeyToken](https://doc-asset.easyar.com/develop/media/api-token-2.jpg)
##### 注意
‌安全性是 Token 有效期设置的首要原因。‌ 如果 Token 有效期过长，一旦被泄露或窃取，攻击者可长期使用，导致数据泄露或未授权操作；有效期限制了 Token 的有效窗口，即使泄露，危害也仅限于短时间。
### 使用 API Key 与 API Secret 生成 Token
Token 的生成过程要求核心参数进行签名操作，确保传输安全性。随后，这些签名后的数据被发送到 STS（Security Token Service）服务进行身份验证。STS 服务验证通过后，会颁发一个临时访问 Token，该 Token 仅在指定时间窗口内有效，超时后需重新发起认证流程。
##### 警告
不要在客户端代码中生成 Token，而是在服务器端生成 Token 后传给客户端使用。
#### 请求参数
|字段名|类型|是否必填|描述|
|apiKey|string|是|API Key|
|expires|int|是|生成的 Token 有效时间, 单位为秒|
|acl|string|是|访问控制列表 (Access Control List)，控制 token 可访问资源权限|
|timestamp|long|是|时间戳，单位为毫秒|
|signature|string|是|签名|
acl： 由一个或多个 AC（访问控制）组成，每个 AC 包含 service，effect，resource，permission 四个部分。
1. service：服务类型，当前支持 ecs:crs（云识别），ecs:spatialmap（稀疏空间地图），ecs:cls（Mega Block 云定位），ecs:vps1（landmark）
2. resource： 具体服务的 app id，例如云识别库的 CRS AppId
3. effect： 指定与该条 resource 配置项匹配的访问能否执行, 取值 Allow，Deny
4. permission： 权限取值 READ，WRITE
结构举例如下：
```
`[
{
"service": "ecs:crs",
"resource": ["f7ff497727ab2d55ea01d9984ef8068c"],
"effect": "Allow",
"permission": ["READ"]
}
]
`
```
#### 签名方法
1. 将请求的所有参数按键名排序
2. 对于每个参数，将其键名与值拼接成字符串
3. 将这样得到的所有字符串拼接，在最后拼上 API Secret
4. 计算字符串 sha256 哈希的十六进制即为签名
##### 签名样例
```
`&lt;?php
// 您的 API Key 与 API Secret
$apiKey = '6a47f7f8ff6......68744b4bcf';
$apiSecret = '87745d866345256b......fbae27c502a';
// 您的服务 App ID
$appId = 'f7ff497727ab2d55ea01d9984ef8068c';
// 有效时间, 单位为秒
$expires = 3600;
// 构建待签名参数
$data = [
'apiKey' =&gt; $apiKey,
'expires' =&gt; $expires,
'acl' =&gt; '[{"service":"ecs:crs","resource":["'. $appId .'"],"effect":"Allow","permission":["READ"]}]',
'timestamp' =&gt; time() \* 1000,
];
// 排序
ksort($data);
// 拼接字符串
$builder = [];
foreach ($data as $key =&gt; $value) {
array\_push($builder, $key . $value);
}
// 拼接 API Secret
array\_push($builder, $apiSecret);
// 生成签名
$signature = hash('sha256', implode('', $builder));
echo $signature;
`
```
```
`const crypto = require('crypto');
// 您的 API Key 与 API Secret
const apiKey = '6a47f7f8ff6......68744b4bcf'
const apiSecret = '87745d866345256b......fbae27c502a'
// 您的服务 App ID
const appId = 'f7ff497727ab2d55ea01d9984ef8068c';
// 有效时间, 单位为秒
const expires = 3600
// 构建待签名参数
const data = {
apiKey: apiKey,
expires: expires,
acl: `[{"service":"ecs:crs","resource":["${appId}"],"effect":"Allow","permission":["READ"]}]`,
timestamp: Date.now(),
}
// 排序与拼接字符串
let builder = [];
Object.keys(data).sort().forEach(key =&gt; builder.push(`${key}${data[key]}`));
// 拼接 API Secret
builder.push(apiSecret);
// 生成签名
const signature = crypto.createHash('sha256').update(builder.join('')).digest('hex');
console.info(signature);
`
```
```
`import time
import hashlib
# 您的 API Key 与 API Secret
apiKey = '6a47f7f8ff6......68744b4bcf'
apiSecret = '87745d866345256b......fbae27c502a'
# 您的服务 App ID
appId = 'f7ff497727ab2d55ea01d9984ef8068c'
# 有效时间, 单位为秒
expires = 3600
# 构建待签名参数
data = dict(sorted({
'apiKey': apiKey,
'expires': expires,
'acl': '[{"service":"ecs:crs","resource":["'+ appId +'"],"effect":"Allow","permission":["READ"]}]',
'timestamp': int(time.time() \* 1000),
}.items()))
# 拼接字符串
builder = [f'{key}{value}' for key, value in data.items()]
# 拼接 API Secret
builder.append(apiSecret)
# 生成签名
signature = hashlib.sha256(''.join(builder).encode('utf8')).hexdigest()
print(signature)
`
```
```
`package com.easyar;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.SortedMap;
import java.util.TreeMap;
public class App {
public static void main(String[] args) throws NoSuchAlgorithmException {
// 您的 API Key 与 API Secret
String apiKey = "6a47f7f8ff6......68744b4bcf";
String apiSecret = "87745d866345256b......fbae27c502a";
// 服务的 App ID
String appId = "f7ff497727ab2d55ea01d9984ef8068c";
// 有效时间, 单位为秒
int expires = 3600;
// 构建待签名参数
SortedMap&lt;String, Object&gt; data = new TreeMap&lt;&gt;();
data.put("apiKey", apiKey);
data.put("expires", expires);
data.put("timestamp", System.currentTimeMillis());
data.put("acl", "[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"" + appId + "\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]");
// 拼接字符串
StringBuilder builder = new StringBuilder();
data.forEach((key, value) -&gt; builder.append(String.format("%s%s", key, value)));
// 拼接 API Secret
builder.append(apiSecret);
// 生成签名
String signature = sha256(builder.toString());
System.out.println(signature);
}
private static String sha256(String str) throws NoSuchAlgorithmException {
StringBuilder builder = new StringBuilder();
MessageDigest digest = MessageDigest.getInstance("sha-256");
digest.update(str.getBytes(StandardCharsets.UTF\_8));
byte[] bytes = digest.digest();
for (byte b : bytes) {
String hex = Integer.toHexString(b &amp; 0XFF);
if (hex.length() == 1) {
builder.append("0");
}
builder.append(hex);
}
return builder.toString();
}
}
`
```
```
`using System.Text;
using System.Security.Cryptography;
namespace EasyAR {
static class Program {
static void Main(string[] args) {
// 您的 API Key 与 API Secret
string apiKey = "6a47f7f8ff6......68744b4bcf";
string apiSecret = "87745d866345256b......fbae27c502a";
// 服务的 App ID
string appId = "f7ff497727ab2d55ea01d9984ef8068c";
// 有效时间, 单位为秒
int expires = 3600;
// 构建待签名参数
SortedDictionary&lt;string, object&gt; data = new() {
{ "apiKey", apiKey },
{ "expires", expires },
{ "timestamp", DateTimeOffset.Now.ToUnixTimeMilliseconds() },
{ "acl", "[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"" + appId + "\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]" }
};
// 拼接字符串
StringBuilder builder = new StringBuilder();
data.ToList().ForEach(pair =&gt; builder.Append($"{pair.Key}{pair.Value}"));
// 拼接 API Secret
builder.Append(apiSecret);
// 生成签名
string signature = Sha256(builder.ToString());
Console.WriteLine(signature);
}
static string Sha256(string str) {
byte[] data = SHA256.HashData(Encoding.UTF8.GetBytes(str));
StringBuilder builder = new StringBuilder();
for (int i = 0; i &lt; data.Length; i++) {
builder.Append(data[i].ToString("x2"));
}
return builder.ToString();
}
}
}
`
```
```
`package main
import (
"crypto/sha256"
"fmt"
"sort"
"strings"
"time"
)
func main() {
// 您的 API Key 与 API Secret
apiKey := "6a47f7f8ff6......68744b4bcf"
apiSecret := "87745d866345256b......fbae27c502a"
// 您的服务 App ID
appId := "f7ff497727ab2d55ea01d9984ef8068c"
// 有效时间, 单位为秒
expires := 3600
// 构建待签名参数
data := map[string]any{
"apiKey": apiKey,
"expires": expires,
"acl": `[{"service":"ecs:crs","resource":["` + appId + `"],"effect":"Allow","permission":["READ"]}]`,
"timestamp": time.Now().Unix() \* 1000,
}
// 排序
keys := []string{}
for key := range data {
keys = append(keys, key)
}
sort.Strings(keys)
// 拼接字符串
builder := strings.Builder{}
for \_, key := range keys {
builder.WriteString(fmt.Sprintf("%s%v", key, data[key]))
}
// 拼接 API Secret
builder.WriteString(apiSecret)
// 生成签名
signature := fmt.Sprintf("%x", sha256.Sum256([]byte(builder.String())))
fmt.Println(signature)
}
`
```
##### 提示
加入签名时需要 ACL 转换为 JSON 字符串。
#### 获取 Token
将上述生成好的签名加入到参数列表中，发送请求到 `/token/v2` 接口，获取 Token。
* 请求地址：`https://uac.easyar.com/token/v2` 或 `https://uac-na1.easyar.com/token/v2` （北美1区）
* 请求方式：POST
* 请求头：Content-Type: application/json
* 请求参数：`{"apiKey":"6a47f7f8ff6......68744b4bcf","expires":3600,"acl":"[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"f7ff497727ab2d55ea01d9984ef8068c\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]","timestamp":1765954279002,"signature":"32f18a37fc3c18......55c4943af9"}`
示例如下：
```
`curl -X POST https://uac.easyar.com/token/v2 \\
-H 'Content-Type: application/json' \\
-d '{"apiKey":"6a47f7f8ff6......68744b4bcf","expires":3600,"acl":"[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"f7ff497727ab2d55ea01d9984ef8068c\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]","timestamp":1765954279002,"signature":"32f18a37fc3c18......55c4943af9"}'
`
```
**返回结果中如果 `statusCode` 为 0，则表示成功。**
正常返回格式：
```
`{
"statusCode": 0,
"timestamp": 1765954874399,
"msg": "Success",
"result": {
"apiKey": "6a47f7f8ff6......68744b4bcf",
"expires": 3600,
"token": "nuPDCj......xstQX",
"expiration": "2025-12-17T08:01:14.399+0000"
}
}
`
```
* token： 业务请求认证的 Token。
* expiration： token 的到期时间，过期过后需要重新申请 token。
错误返回格式：
```
`{
"statusCode": 4001017,
"timestamp": 1765954666624,
"msg": "AppId is not authorized by this API Key",
"result": null
}
`
```
## 使用 Token
在业务 https 请求中，将 Token 加入请求头，格式：`{"Authorization": "nuPDCj......xstQX"}`。
发送业务 API 请求时，需要添加参数 appId（获取出处请在开发中心查看相关服务）。
## 错误码说明
在 Token 生成与 Token 使用过程中，可能会引发各类错误或异常情况。
为帮助开发者快速定位问题并采取有效解决措施，以下详细说明常见错误码及其含义：
|错误码|错误信息|错误说明|解决方案|
|4001011|API Key invalid|API Key 无效|查看“云服务 API KEY”下是否有此 API Key|
|4001012|Timestamp invalid|时间戳无效|时间戳单位为毫秒，且与标准时间误差不要超过 5 分钟|
|4001015|Signature invalid|签名无效|检查签名算法是否正确，以及查看 API Secret 与 API KEY 是否匹配|
|4001017|AppId is not authorized by this API Key|API Key 未获此 AppId 授权|检查 AppId 所在的服务是否关联到此 API Key|
|4001018|Base64 decode error|请求头中设置的 Authorization 不是有效 base64 格式|获取到的 Token，不要作任何处理，直接使用|
|4001019|Decryption error|请求头中设置的 Authorization 不是 EasyAR 生成的|获取到的 Token，不要作任何处理，直接使用|
|4001022|API Key's resource is empty|API Key 没有关联的云服务|检查 API Key 是否关联了云服务及关联的云服务是否已经过期|
|4001024|Token is expired|Token 已过期|重新生成|
|4001025|Token generate fail|Token 生成失败|与技术支持联系：support@easyar.com|