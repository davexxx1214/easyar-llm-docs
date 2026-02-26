# EasyAR 文档全集（LLM 输入包）

本文件由清洗后的文档自动拼接而成。
建议提示词：先根据目录定位章节，再结合章节原文给出答案，并标注“章节路径 + source URL”。

## 目录
- `apikey-auth.md`
- `apikey.md`
- `cameras/cameras.md`
- `cameras/custom-camera.md`
- `cloud-recognition/image-recognition-with-tracking.md`
- `cloud-recognition/intro.md`
- `cloud-recognition/management-adding.md`
- `cloud-recognition/management-deletion.md`
- `cloud-recognition/management-gallery.md`
- `cloud-recognition/management-grading.md`
- `cloud-recognition/management.md`
- `compliance/data-access.md`
- `compliance/guide.md`
- `compliance/intro.md`
- `dense-spatial-mapping/devices.md`
- `dense-spatial-mapping/intro.md`
- `devices-crs.md`
- `devices-sense.md`
- `diagnostics/crash-android.md`
- `diagnostics/crash-ios.md`
- `diagnostics/crash-windows.md`
- `diagnostics/diagnostics.md`
- `diagnostics/log-android.md`
- `diagnostics/log-ios.md`
- `diagnostics/log-wechat.md`
- `diagnostics/log-windows.md`
- `diagnostics/recordings-headsets.md`
- `diagnostics/recordings.md`
- `diagnostics/simulation.md`
- `fundamentals/fundamentals.md`
- `getting-started/ar.md`
- `headsets/headsets.md`
- `image-tracking/devices.md`
- `image-tracking/intro.md`
- `image-tracking/motion-fusion.md`
- `license-sense.md`
- `mega/content-drift.md`
- `mega/content-nodisplay.md`
- `mega/devices.md`
- `mega/faq.md`
- `mega/input-recording.md`
- `mega/intro.md`
- `mega/localization-verify.md`
- `mega/navigation.md`
- `mega/report.md`
- `motion-tracking/comparison.md`
- `motion-tracking/devices-arcore.md`
- `motion-tracking/devices-arengine.md`
- `motion-tracking/devices-easyar.md`
- `motion-tracking/devices.md`
- `motion-tracking/intro.md`
- `motion-tracking/motion-tracking-and-easyar.md`
- `native/fundamentals/3dengine.md`
- `native/fundamentals/contents.md`
- `native/fundamentals/coordinates.md`
- `native/fundamentals/dataflow.md`
- `native/fundamentals/initialization.md`
- `native/getting-started/choosing-an-engine.md`
- `native/getting-started/enable-easyar-android.md`
- `native/getting-started/enable-easyar-ios.md`
- `native/getting-started/quickstart-android.md`
- `native/getting-started/quickstart-ios.md`
- `native/getting-started/quickstart-windows.md`
- `native/getting-started/variants.md`
- `native/release-notes/release-notes-1_0.md`
- `native/release-notes/release-notes-1_1.md`
- `native/release-notes/release-notes-1_2.md`
- `native/release-notes/release-notes-1_3.md`
- `native/release-notes/release-notes-2_0.md`
- `native/release-notes/release-notes-2_1.md`
- `native/release-notes/release-notes-2_2.md`
- `native/release-notes/release-notes-2_3.md`
- `native/release-notes/release-notes-3_0.md`
- `native/release-notes/release-notes-3_1.md`
- `native/release-notes/release-notes-4_0.md`
- `native/release-notes/release-notes-4_1.md`
- `native/release-notes/release-notes-4_2.md`
- `native/release-notes/release-notes-4_3.md`
- `native/release-notes/release-notes-4_4.md`
- `native/release-notes/release-notes-4_5.md`
- `native/release-notes/release-notes-4_6.md`
- `native/release-notes/release-notes-4_7.md`
- `native/release-notes/release-notes.md`
- `object-tracking/intro.md`
- `object-tracking/model-requirements.md`
- `object-tracking/motion-fusion.md`
- `overview.md`
- `plane-detection/devices.md`
- `plane-detection/intro.md`
- `simulation/simulation.md`
- `sparse-spatial-mapping/comparison.md`
- `sparse-spatial-mapping/devices.md`
- `sparse-spatial-mapping/intro.md`
- `surface-tracking/devices.md`
- `surface-tracking/intro.md`
- `unity/cameras/comp-CameraDeviceFrameSource.md`
- `unity/cameras/comp-InertialCameraDeviceFrameSource.md`
- `unity/cameras/comp-ThreeDofCameraDeviceFrameSource.md`
- `unity/cameras/external-device-frame-source.md`
- `unity/cameras/external-frame-source.md`
- `unity/cameras/external-image-stream-frame-source.md`
- `unity/cameras/external-input-frame.md`
- `unity/cameras/frame-source-builtin.md`
- `unity/cameras/frame-source-group.md`
- `unity/cameras/frame-source.md`
- `unity/cameras/sample-camera-device.md`
- `unity/diagnostics/comp-DiagnosticsController.md`
- `unity/diagnostics/developer-mode.md`
- `unity/diagnostics/diagnostics.md`
- `unity/diagnostics/event-dump.md`
- `unity/diagnostics/report.md`
- `unity/diagnostics/ui-messages.md`
- `unity/fundamentals/active-control.md`
- `unity/fundamentals/arfoundation-scene-setup.md`
- `unity/fundamentals/arfoundation.md`
- `unity/fundamentals/camera-configs.md`
- `unity/fundamentals/camera.md`
- `unity/fundamentals/center-mode-choosing.md`
- `unity/fundamentals/center-mode.md`
- `unity/fundamentals/comp-ARSession.md`
- `unity/fundamentals/initialization.md`
- `unity/fundamentals/intro.md`
- `unity/fundamentals/origin-creation.md`
- `unity/fundamentals/origin.md`
- `unity/fundamentals/sample-arsession.md`
- `unity/fundamentals/session-assemble.md`
- `unity/fundamentals/session-components.md`
- `unity/fundamentals/session-creation.md`
- `unity/fundamentals/session-ctrl.md`
- `unity/fundamentals/session-output.md`
- `unity/fundamentals/session-report.md`
- `unity/fundamentals/session.md`
- `unity/fundamentals/setup-easyar.md`
- `unity/fundamentals/setup-player.md`
- `unity/fundamentals/target-state.md`
- `unity/fundamentals/target.md`
- `unity/fundamentals/unity-compatibility.md`
- `unity/fundamentals/unity-xr-switch.md`
- `unity/fundamentals/unity-xr.md`
- `unity/getting-started/diagnostics.md`
- `unity/getting-started/enable-easyar.md`
- `unity/getting-started/quickstart.md`
- `unity/getting-started/sample-launcher.md`
- `unity/getting-started/scene.md`
- `unity/getting-started/universal-render-pipeline.md`
- `unity/headsets/enable-headset.md`
- `unity/headsets/extension-bring-up.md`
- `unity/headsets/extension-dist.md`
- `unity/headsets/extension-imp.md`
- `unity/headsets/extension-template.md`
- `unity/headsets/extension.md`
- `unity/headsets/headsets.md`
- `unity/headsets/samples.md`
- `unity/headsets/setup-visionpro.md`
- `unity/headsets/setup-xreal.md`
- `unity/mega/comp-BlockController.md`
- `unity/mega/comp-BlockHolder.md`
- `unity/mega/comp-BlockRootController.md`
- `unity/mega/comp-MegaTrackerFrameFilter.md`
- `unity/mega/content-realworld-alignment.md`
- `unity/mega/enable-mega.md`
- `unity/mega/occlusion.md`
- `unity/mega/onsite-and-simulation.md`
- `unity/mega/quickstart.md`
- `unity/mega/session-best-practice.md`
- `unity/mega/target.md`
- `unity/mega/tracker.md`
- `unity/mega/verify-pc-camera.md`
- `unity/mega/verify-session-tool.md`
- `unity/motion-tracking/3rdparty-compatibility.md`
- `unity/motion-tracking/comp-ARCoreFrameSource.md`
- `unity/motion-tracking/comp-AREngineFrameSource.md`
- `unity/motion-tracking/comp-ARKitFrameSource.md`
- `unity/motion-tracking/comp-MotionTrackerFrameSource.md`
- `unity/release-notes/release-notes-v4.md`
- `unity/release-notes/release-notes.md`
- `unity/simulation/comp-FramePlayer.md`
- `unity/simulation/comp-FrameRecorder.md`
- `unity/simulation/playback.md`
- `unity/simulation/recording.md`
- `unity/simulation/simulation.md`
- `unity/simulation/tool.md`
- `web/cloud-recognition/guide.md`
- `web/cloud-recognition/quickstart.md`
- `web/cloud-recognition/sample.md`
- `web/getting-started/quickstart.md`
- `wechat/cloud-recognition/guide.md`
- `wechat/cloud-recognition/quickstart.md`
- `wechat/cloud-recognition/sample.md`
- `wechat/diagnostics/report.md`
- `wechat/getting-started/quickstart.md`
- `wechat/mega/content-annotation-creation.md`
- `wechat/mega/content-load.md`
- `wechat/mega/content-realworld-alignment.md`
- `wechat/mega/content-simple.md`
- `wechat/mega/content-simulation.md`
- `wechat/mega/content-unity-setup.md`
- `wechat/mega/fullstart.md`
- `wechat/mega/integration.md`
- `wechat/mega/known-issues.md`
- `wechat/mega/occlusion.md`
- `wechat/mega/quickstart.md`
- `wechat/mega/release-notes.md`
- `wechat/mega/sample.md`
- `wechat/mega/session-device-orientation.md`
- `wechat/mega/session-dump.md`
- `wechat/mega/session-gnss-simulation.md`
- `wechat/mega/session-plane-detection-error.md`
- `wechat/mega/session-state.md`
- `wechat/mega/session.md`
- `wechat/mega/tracker-access.md`
- `wechat/mega/tracker-external-sensor.md`
- `wechat/mega/tracker-landmark.md`
- `wechat/mega/tracker.md`
- `wechat/mega/transparent-video.md`

---

## 获取和使用 API Key
- 章节路径: `apikey-auth.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/apikey-auth.html

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
> **提示**
使用 [SpatialMap](sparse-spatial-mapping/intro.html)，勾选 SpatialMap。
使用[云识别](cloud-recognition/intro.html)，勾选云识别。
使用 Mega Landmark，勾选 Mega Landmark，使用此功能前需要向商务申请。
使用 AR 运营中心，勾选 AR 运营中心，使用此功能前需要向商务申请。
使用 [Mega Block 云定位](mega/intro.html)，勾选 Mega Block。
![APIKey](https://doc-asset.easyar.com/develop/media/api-key-2.jpg)
* 此时会在页面生成 API Key 与 API Secret，如下图所示，注意不要泄露。
![APIKey](https://doc-asset.easyar.com/develop/media/api-key-3.jpg)
> **警告**
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
> **注意**
‌安全性是 Token 有效期设置的首要原因。‌ 如果 Token 有效期过长，一旦被泄露或窃取，攻击者可长期使用，导致数据泄露或未授权操作；有效期限制了 Token 的有效窗口，即使泄露，危害也仅限于短时间。
### 使用 API Key 与 API Secret 生成 Token
Token 的生成过程要求核心参数进行签名操作，确保传输安全性。随后，这些签名后的数据被发送到 STS（Security Token Service）服务进行身份验证。STS 服务验证通过后，会颁发一个临时访问 Token，该 Token 仅在指定时间窗口内有效，超时后需重新发起认证流程。
> **警告**
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
[
{
"service": "ecs:crs",
"resource": ["f7ff497727ab2d55ea01d9984ef8068c"],
"effect": "Allow",
"permission": ["READ"]
}
]
```
#### 签名方法
1. 将请求的所有参数按键名排序
2. 对于每个参数，将其键名与值拼接成字符串
3. 将这样得到的所有字符串拼接，在最后拼上 API Secret
4. 计算字符串 sha256 哈希的十六进制即为签名
##### 签名样例
```
<?php
// 您的 API Key 与 API Secret
$apiKey = '6a47f7f8ff6......68744b4bcf';
$apiSecret = '87745d866345256b......fbae27c502a';
// 您的服务 App ID
$appId = 'f7ff497727ab2d55ea01d9984ef8068c';
// 有效时间, 单位为秒
$expires = 3600;
// 构建待签名参数
$data = [
'apiKey' => $apiKey,
'expires' => $expires,
'acl' => '[{"service":"ecs:crs","resource":["'. $appId .'"],"effect":"Allow","permission":["READ"]}]',
'timestamp' => time() \* 1000,
];
// 排序
ksort($data);
// 拼接字符串
$builder = [];
foreach ($data as $key => $value) {
array\_push($builder, $key . $value);
}
// 拼接 API Secret
array\_push($builder, $apiSecret);
// 生成签名
$signature = hash('sha256', implode('', $builder));
echo $signature;
```
```
const crypto = require('crypto');
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
Object.keys(data).sort().forEach(key => builder.push(`${key}${data[key]}`));
// 拼接 API Secret
builder.push(apiSecret);
// 生成签名
const signature = crypto.createHash('sha256').update(builder.join('')).digest('hex');
console.info(signature);
```
```
import time
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
```
```
package com.easyar;
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
SortedMap<String, Object> data = new TreeMap<>();
data.put("apiKey", apiKey);
data.put("expires", expires);
data.put("timestamp", System.currentTimeMillis());
data.put("acl", "[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"" + appId + "\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]");
// 拼接字符串
StringBuilder builder = new StringBuilder();
data.forEach((key, value) -> builder.append(String.format("%s%s", key, value)));
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
String hex = Integer.toHexString(b & 0XFF);
if (hex.length() == 1) {
builder.append("0");
}
builder.append(hex);
}
return builder.toString();
}
}
```
```
using System.Text;
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
SortedDictionary<string, object> data = new() {
{ "apiKey", apiKey },
{ "expires", expires },
{ "timestamp", DateTimeOffset.Now.ToUnixTimeMilliseconds() },
{ "acl", "[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"" + appId + "\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]" }
};
// 拼接字符串
StringBuilder builder = new StringBuilder();
data.ToList().ForEach(pair => builder.Append($"{pair.Key}{pair.Value}"));
// 拼接 API Secret
builder.Append(apiSecret);
// 生成签名
string signature = Sha256(builder.ToString());
Console.WriteLine(signature);
}
static string Sha256(string str) {
byte[] data = SHA256.HashData(Encoding.UTF8.GetBytes(str));
StringBuilder builder = new StringBuilder();
for (int i = 0; i < data.Length; i++) {
builder.Append(data[i].ToString("x2"));
}
return builder.ToString();
}
}
}
```
```
package main
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
```
> **提示**
加入签名时需要 ACL 转换为 JSON 字符串。
#### 获取 Token
将上述生成好的签名加入到参数列表中，发送请求到 `/token/v2` 接口，获取 Token。
* 请求地址：`https://uac.easyar.com/token/v2` 或 `https://uac-na1.easyar.com/token/v2` （北美1区）
* 请求方式：POST
* 请求头：Content-Type: application/json
* 请求参数：`{"apiKey":"6a47f7f8ff6......68744b4bcf","expires":3600,"acl":"[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"f7ff497727ab2d55ea01d9984ef8068c\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]","timestamp":1765954279002,"signature":"32f18a37fc3c18......55c4943af9"}`
示例如下：
```
curl -X POST https://uac.easyar.com/token/v2 \\
-H 'Content-Type: application/json' \\
-d '{"apiKey":"6a47f7f8ff6......68744b4bcf","expires":3600,"acl":"[{\\"service\\":\\"ecs:crs\\",\\"resource\\":[\\"f7ff497727ab2d55ea01d9984ef8068c\\"],\\"effect\\":\\"Allow\\",\\"permission\\":[\\"READ\\"]}]","timestamp":1765954279002,"signature":"32f18a37fc3c18......55c4943af9"}'
```
**返回结果中如果 `statusCode` 为 0，则表示成功。**
正常返回格式：
```
{
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
```
* token： 业务请求认证的 Token。
* expiration： token 的到期时间，过期过后需要重新申请 token。
错误返回格式：
```
{
"statusCode": 4001017,
"timestamp": 1765954666624,
"msg": "AppId is not authorized by this API Key",
"result": null
}
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

---

## EasyAR 云服务 API Key 统一认证
- 章节路径: `apikey.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/apikey.html

# EasyAR 云服务 API Key 统一认证
API Key 通过统一的身份认证机制，实现对所有 EasyAR 云服务 API 的集中访问管理，简化开发流程，提升安全性和易用性，从而显著降低开发者在服务接入、权限控制和维护管理等方面的成本与复杂度。
## 什么是 API Key
API Key（Application Programming Interface Key）即应用程序编程接口密钥，是一串由数字、字母或特殊字符组成的唯一识别码。主要作用是让您的应用或服务在调用 EasyAR API 时，证明自己的合法身份，由 EasyAR 平台生成并分配给您使用。
## 什么是 Token
在 API 访问认证中，Token 是一种临时的、加密的身份凭证，由服务端在用户或应用完成身份验证后生成，它相当于 API 调用的 “身份凭证”，用于您的应用或服务与 EasyAR API 服务之间建立通信时，验证是否有合法身份，同时根据 Token 绑定的权限，判断其是否能访问目标接口或数据。
## 使用 API Key / Token 的云服务
在 EasyAR 云服务中，API Key / Token 可用于访问以下服务：
* [云识别](cloud-recognition/intro.html)
* [稀疏空间地图](sparse-spatial-mapping/intro.html)
* [Mega Block 云定位](mega/intro.html)
## 相关主题
* [获取 API Key](apikey-auth.html#api-key)
* [获取 Token](apikey-auth.html#api-token)

---

## 摄像头和输入扩展
- 章节路径: `cameras/cameras.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cameras/cameras.html

# 摄像头和输入扩展
本文介绍物理相机的相机模型、参数和一些其他使用上的注意点，以及使用自定义相机的方式进行输入扩展。
![camera](https://doc-asset.easyar.com/develop/cameras/media/cameras-camera.jpg)
## 输入帧
输入帧（Input Frame）是 AR 中的基本数据单元，它表示一次从摄像头或其他数据源捕获的帧的所有相关信息。一个输入帧通常包含：
* 原始图像数据（camera image）
* 相机参数（如内参）
* 时间戳
* 相机在世界坐标中的变换矩阵
* 跟踪状态（tracking status）
这些信息为 AR 算法提供定位、跟踪、渲染等所需的时空上下文数据。
## 物理相机
目前电子设备上使用的摄像头，通常由多片透镜和反射镜组成。但一般不使用实际的光学结构来构建相机模型，而是使用一些简化的模型。
### 针孔相机模型
![pinhole camera](https://doc-asset.easyar.com/develop/cameras/media/cameras-pinhole.png)
这是通常使用的最简单的模型，光通过一个小孔成一个旋转 180 度的像。但相机输出的数据中会将像正过来。需要六个参数来描述这个模型，像素宽高 \\(w, h\\) ，像素焦距 \\(f\_x, f\_y\\) ，主点像素位置 \\(c\_x, c\_y\\) 。可以注意到如果像素宽高缩放时，像素焦距和主点像素位置也对应缩放，可以保持像的位置不变。
### OpenCV 相机模型
有些相机会存在显著的径向畸变和切向畸变，[OpenCV 相机模型](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)在针孔相机模型上的基础上增加了高次参数来描述径向畸变和切向畸变。径向畸变使用 \\(k\_1, k\_2, k\_3, \\cdots\\) 来描述。切向畸变使用 \\(p\_1, p\_2\\) 来描述。
> **注意**
有一些跟踪器不支持 OpenCV 相机模型。
### OpenCV 鱼眼相机模型
鱼眼相机通过透视投影以将大视角内容压缩到较小的成像面积内。[OpenCV 鱼眼相机模型](https://docs.opencv.org/4.x/db/d58/group__calib3d__fisheye.html)不带畸变矫正，在针孔相机模型 6 个参数的基础上，使用 \\(k\_1, k\_2, k\_3, k\_4, \\cdots\\) 来描述。
> **注意**
有一些跟踪器不支持 OpenCV 鱼眼相机模型。
![fisheye camera](https://doc-asset.easyar.com/develop/cameras/media/cameras-fisheye.jpg)
### 相机朝向与图像朝向
在手机上，通常横向拿（从正常竖向拿逆时针旋转 90 度）且屏幕显示方向也是横向的时候，后置摄像头输出的图像在屏幕上显示时的方向和真实场景一致。不改变屏幕物理方向只改变屏幕显示方向不会改变物理相机输出的图像方向。当正常竖向拿且屏幕显示方向也是正常竖向的时候，后置摄像头输出的图像需要顺时针旋转 90 度后显示到屏幕上，才和真实场景一致。当屏幕显示方向旋转时，渲染相机图像需要进行反向的旋转补偿，才能和真实场景一致。
相机朝向和图像朝向，通常都是相对于设备的自然方向来定义的：
* 手机
* Android
Android 定义了一个自然方向，是指正常竖向拿手机的方向，惯性传感器单元(IMU)也是以这个方向为基准。相机输出图像相对于这个方向的旋转角度，作为相机的参数，可以获得。
* iOS
iOS 上，虽然未明确定义自然方向，但惯性传感器单元也是使用的和 Android 一样的基准。
* 平板
平板的自然方向，有一些是横向拿的方向，有些和手机一样是正常竖向拿的方向。
* 眼镜
眼镜的自然方向，通常是横向拿的方向。
渲染相机图像时，会综合相机朝向和屏幕朝向进行渲染。
### 相机类型与相机翻转
手机上一般有后置摄像头和前置摄像头。前置摄像头输出的图像，需要进行左右翻转后再显示到屏幕上，模拟一面镜子。如果不进行左右翻转，看起来会很不习惯。
## 输入扩展
EasyAR 支持使用自定义相机的方式进行输入扩展。自定义相机可以支持从外部获得输入帧传输到 AR 系统中，供跟踪器使用。自定义相机可以由您自行实现图像数据获取。
## 平台专用指南
摄像头和输入扩展的使用与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [帧数据源](../unity/cameras/frame-source.html)
* [创建一组输入源](../unity/cameras/frame-source-group.html)
* [自定义相机和外部帧输入](../unity/cameras/external-frame-source.html)
* [内置Frame Source参考](../unity/cameras/frame-source-builtin.html)
* [示例说明](../unity/cameras/sample-camera-device.html)

---

## 自定义相机
- 章节路径: `cameras/custom-camera.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/cameras/custom-camera.html

# 自定义相机
在一些情况下，内置支持的摄像头不能满足需求，此时可能需要考虑使用自定义相机，自定义相机可以支持从外部获得图像数据输入到 AR 系统中，供跟踪器使用。自定义相机可以由您自行实现图像数据获取。
可用平台：Unity、原生
## 开始之前
* 通过 [摄像头和输入扩展](cameras.html) 了解物理相机的相机模型、参数和一些其他使用上的注意点。
## 自定义相机的使用场景
以下场景中可以使用自定义相机：
* 外置摄像头
例如在 Android 上，系统 API 不支持外置摄像头，只能通过 libuvc 来调用外置摄像头
* 远程摄像头串流
* 视频文件
* 头显
## AR 系统中使用的自定义相机
AR 系统中使用的自定义相机有：
* AREngineInterop
在鸿蒙 4.x 及以前版本上提供华为 AR Engine 支持，通过自定义相机使用手机提供的运动跟踪功能
* 头显
多种头显的图像输入是通过自定义相机来实现的
## 自定义相机使用限制
自定义相机使用限制有
* 在头显设备上
* EasyAR Sense XR License 试用版
每次运行可以使用 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度），在部分条件下运行时会显示水印，在某些设备上需要联网才能使用
* EasyAR Sense XR License 正式版
无限制
* 在其他设备上
* EasyAR Sense 个人版
每次运行可以使用 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度），在部分条件下运行时会显示水印
* EasyAR Sense 专业版/经典版/企业版
无限制

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

---

## EasyAR Sense 数据访问
- 章节路径: `compliance/data-access.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/compliance/data-access.html

# EasyAR Sense 数据访问
介绍 EasyAR Sense 中可能的数据访问。
## 数据访问情况列表

> **注意** 自动修复提示：该表格在抓取阶段已损坏，以下保留原始表格流供人工核对。

```text
|
功能
|
数据
|
使用类型
|
使用目的
|
传输加密
|
短暂使用
|
备注
|
|
基本
|
iOS: identifierForVendor
“设备-开发商”标识
|
访问/传输
|
统计分析
|
使用 TLS
|
否
||
|
设备型号、制造商、品牌、操作系统版本
|
访问/传输
|
统计分析
|
使用 TLS
|
否
||
|
设备型号、制造商、品牌、操作系统版本
|
访问
|
软件功能
|
不适用
|
不适用
|
用于选择软件实现，如在 CameraDeviceSelector、ARCoreCameraDevice、MotionTrackerCameraDevice 中
|
|
SDK 功能调用记录
|
访问/传输
|
统计分析
|
使用 TLS
|
否
||
|
平面图像跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
视频播放
|
开发者指定视频文件
|
访问
|
软件功能
|
不适用
|
不适用
||
|
云识别
|
相机图像
|
访问/传输
|
软件功能
|
根据调用方式可能不加密，也可能使用 TLS
|
是
||
|
3D 物体跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
录屏
|
屏幕图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
表面跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
运动传感器读数
|
访问
|
软件功能
|
不适用
|
不适用
||
|
稀疏空间地图
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
稀疏空间地图数据
|
访问/传输/分享
|
软件功能
|
使用 TLS
|
否
|
不包含图像，但包含从图像计算得到的衍生数据
可以通过管理页面或 WebAPI 删除
根据调用方式可以分享给其他最终用户
|
|
预览图像(可选)
|
访问/传输
|
软件功能
|
使用 TLS
|
否
|
可以通过管理页面或 WebAPI 删除
|
|
稠密空间地图
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
运动跟踪
|
相机图像
|
访问
|
软件功能
|
不适用
|
不适用
||
|
运动传感器读数
|
访问
|
软件功能
|
不适用
|
不适用
||
|
Mega/云定位
|
相机图像
|
访问/传输
|
软件功能
|
根据调用方式可能不加密，也可能使用 TLS
|
是
||
|
位置信息(可选，根据调用情况决定为大致位置还是确切位置)
|
访问/传输
|
软件功能
|
根据调用方式可能不加密，也可能使用 TLS
|
是
||
```

注：
“访问”指在客户端获得数据。“传输”指将数据从客户端发送到 EasyAR 的服务器。“分享”指将数据从客户端发送到第三方设备。
“短暂使用”是指服务器处理请求之后不会保存此项数据。

---

## EasyAR Sense 合规指南
- 章节路径: `compliance/guide.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/compliance/guide.html

# EasyAR Sense 合规指南
欢迎您使用 EasyAR 平台（以下简称“本平台”或者“我们”），为完善您在本平台上的使用体验，并协助您在合法合规的前提下推进您的项目建设，我们根据中华人民共和国的法律、法规之规定制定本《合规指南》（以下简称“本指南”），以便您明确您在向最终用户提供产品或服务时可能涉及的义务与责任，最大程度避免违法违规。
请您注意，由于应用服务器所在区域、应用发布服务器所在的区域、用户所在的区域可能并不位于中华人民共和国境内或者位于不同的地区或国家，您提供产品或服务将适用并满足对应地区或国家的法律、法规、规则，承担适用法律项下应用开发者、数据处理者的责任。
请您合理参考本指南的内容，作为您合规向最终用户提供产品或服务的指引。
## 隐私政策
在您向最终用户提供产品或服务的过程中，如果您将自行或委托第三人收集、存储、处理最终用户的个人信息的，请您依照适用的法律、法规之规定制定《隐私政策》、《数据处理协议》或者相关书面协议以保护用户的个人信息安全以及您的权利。请您务必在初始化 EasyAR Sense 之前，向最终用户书面提示并充分告知收集其个人信息的范围、方式与目的。您可以参考以下的条文：
>
> 我们的产品集成 EasyAR Sense，可能会收集您的
> identifierForVendor(iOS)、设备型号、制造商、品牌、操作系统版本、SDK 功能调用记录
> 以进行统计分析、改进产品和服务，可能会获取您的
> 相机图像、运动传感器读数
> 以实现软件功能。
>
请您务必阅读并确认 [数据访问](data-access.html) ，并根据您提供产品或服务中对相关数据的实际使用情况，调整上述条文的内容。
为落实信息处理主体的法律责任要求，根据您实际提供产品或服务的情况，还请您进一步明确产品或服务功能所需使用的具体数据或信息，且仅在正当、合理、透明、必要原则的指引下收集相关个人信息。您知悉，如果由于您违反法律法规之规定，或者未告知或未完整告知最终用户关于您收集个人信息的使用规则、范围、方式与目的而导致相关权利主体、权力机关对我们的投诉、诉讼、处罚以及相关责任与后果，均由您承担。
## 数据安全表格
应用发布平台可能会要求填写数据安全表格披露数据访问、收集情况，如果适用，请务必阅读 [数据访问](data-access.html) ，根据应用的使用情况，填写应用发布平台的表格。
* Android
在应用发布到 Play Store 时会需要填写 Google 的数据安全表格，参考 [这里](https://support.google.com/googleplay/android-developer/answer/10787469) 。
* iOS
在应用发布到 Apple App Store 时会需要填写 Apple 的应用隐私表格，参考 [这里](https://developer.apple.com/app-store/app-privacy-details/) 。
## 与儿童相关的要求
法律、法规、规则或应用发布平台可能会对面向儿童的应用有特殊要求。如果适用，请务必满足这些特殊要求，包括但不限于展示年龄验证弹窗。
* Android
在应用发布到 Play Store 时的要求，参考 [这里](https://support.google.com/googleplay/android-developer/answer/9893335) 。
* iOS
在应用发布到 Apple App Store 时的要求，参考 [这里](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions/) 。
## 其他可能的问题
如果应用使用到其他工具或 SDK，请访问对应的官方网站查看其合规指南。
例如，Unity SDK 的指南可参考如下文档 [中国大陆](https://unity.cn/legal/privacy-policy) [其他国家和地区](https://unity.com/legal/privacy-policy) 。

---

## 合规
- 章节路径: `compliance/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/compliance/intro.html

# 合规
本章主要介绍使用 EasyAR Sense 的合规指南，并提供可能访问的数据列表。为了避免因权限过度申请或隐私声明缺失导致的合规风险（如应用下架等），在使用 EasyAR Sense 和 EasyAR Sense Unity Plugin 开发应用，并提交到应用商店上架之前，请务必确认 [EasyAR Sense 合规指南](guide.html) 和 [EasyAR Sense 数据访问](data-access.html)。

---

## 稠密空间地图支持的设备和平台
- 章节路径: `dense-spatial-mapping/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/dense-spatial-mapping/devices.html

# 稠密空间地图支持的设备和平台
本章介绍稠密空间地图（Dense Spatial Map）功能支持的设备硬件要求和开发平台。
## 稠密空间地图支持的设备
稠密空间地图支持 iOS、Android、鸿蒙平台以及部分头显平台。硬件上，需要设备支持六自由度的[运动跟踪](../motion-tracking/intro.html)功能。
稠密空间地图可用的运动跟踪类型包括：
* EasyAR 运动跟踪（Motion Tracker）
* 谷歌 ARCore
* 苹果 ARKit
* 华为 AR Engine
* 六自由度跟踪能力的头显或眼镜
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上通过 Unity 或者原生使用稠密空间地图功能。需要注意录制 EIF 的设备必须支持运动跟踪功能。
如果您的设备支持运动跟踪功能，可以参照 [自定义相机](../cameras/custom-camera.html) 的方式接入 EasyAR 并使用稠密空间地图功能。
## 延伸阅读
* [运动跟踪与 EasyAR 其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker 支持的设备](../motion-tracking/devices-easyar.html)
* [华为 AR Engine 支持的设备](../motion-tracking/devices-arengine.html)

---

## EasyAR 稠密空间地图
- 章节路径: `dense-spatial-mapping/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/dense-spatial-mapping/intro.html

# EasyAR 稠密空间地图
EasyAR 稠密空间地图利用设备的摄像头数据对周围环境进行三维重建，得到稠密的点云地图和网格地图。利用稠密空间地图让虚拟物体更好地融入真实环境之中，以实现真实物体和虚拟物体正确遮挡、碰撞等 AR 应用。
## 稠密空间地图功能简介
EasyAR 稠密空间地图在运动跟踪的基础上，分析设备的摄像头数据，建立环境的稠密点云信息并逐渐融合、构建网格（Mesh），得到环境的几何表示，可以用来实现虚拟物体和真实环境的遮挡关系等效果，从而提高 AR 的真实体验感。
EasyAR 稠密空间地图需要基于稳定的 [运动跟踪系统](../motion-tracking/intro.html) 提供六自由度的相机位置和姿态，可以从 EasyAR 运动跟踪模块或者 ARKit/ARCore 等获取。
![densespatialmap](https://doc-asset.easyar.com/develop/dense-spatial-mapping/media/densespatialmap-intro.png)
## 最佳实践
要想得到比较好的重建结果，建议用户按照如下方式进行操作：
* 尽量横移手机，避免原地旋转手机。
* 覆盖尽可能多的扫描角度。
* 不要在大片的纯色区域或对带有反光的物体重建。
* 避免快速的移动或遮挡摄像头。
## 延伸阅读
* [稠密空间地图支持的设备](devices.html)
* [运动跟踪与 EasyAR 其他模块的关系](../motion-tracking/motion-tracking-and-easyar.html)

---

## EasyAR CRS 支持的设备和平台应用
- 章节路径: `devices-crs.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/devices-crs.html

# EasyAR CRS 支持的设备和平台应用
EasyAR 图像云识别 Cloud Recognition Service （CRS） 支持不同的硬件设备、操作系统和开发平台的支持。
|设备类型|操作系统|目标平台|
|智能手机/平板|• iOS
• iPadOS
• Android|• Native
• Unity
• 微信小程序
• Web|
|XR 头显/眼镜|• visionOS
• Android XR|• Unity|
|电脑(PC)|• Windows
• macOS|• Native
• Unity
• Web|
|自定义设备|• Android|• Native
• Unity|

---

## EasyAR Sense 支持的系统和设备
- 章节路径: `devices-sense.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/devices-sense.html

# EasyAR Sense 支持的系统和设备
EasyAR Sense支持不同的硬件设备、操作系统和开发平台的支持，不同的功能对于设备的硬件或者系统功能要求可能存在差异。
## EasyAR Sense支持的操作系统
EasyAR Sense 是一款跨平台的增强现实（AR）SDK，支持以下操作系统：
* **Windows**：7 及以上版本（7 / 8.1 / 10 / 11）
* **macOS**：10.15 及以上版本
* **Android**：5.0 及以上版本（兼容手机鸿蒙系统 1.x–4.x）
* **iOS**：12.0 及以上版本
* **visionOS**：2.0 及以上版本
* **Android XR**
## EasyAR 不同功能的硬件要求
不同的 EasyAR 功能对硬件的支持略有不同，除摄像头外，部分功能还有额外的硬件要求，具体要求见如下表。
|功能|额外要求|
|Mega / 云定位|参考 [Mega支持机型](mega/devices.html)|
|运动跟踪|参考 [运动跟踪支持机型](motion-tracking/devices.html)|
|稀疏空间地图|支持 ARKit,ARCore 或运动跟踪等|
|稠密空间地图|支持 ARKit,ARCore 或运动跟踪等|
|表面跟踪|加速度计 + 陀螺仪|

---

## Android 上的崩溃分析
- 章节路径: `diagnostics/crash-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-android.html

# Android 上的崩溃分析
关于 原生(Android) 和 Unity(Android)上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在 Android Studio 中调试 Android 的 Native 程序时，需要在 Configuration 设置中将 Debugger - Debug type 改为Dual (Java + Native)。
![crash Android configuratio](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-configuration.png)
在 Android Studio 中调试时需要的信息如下图。
![crash Android stack](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-stack.png)
在 lldb 中输入 `bt` ，可以获得崩溃原因和代码运行栈，如下
```
(lldb) bt
\* thread #16, name = 'samples.helloar', stop reason = signal SIGSEGV: invalid address (fault address: 0x9c40)
\* frame #0: 0x0000004922f3a1d8 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol3056$$libEasyAR.so + 6088
frame #1: 0x0000004922f38568 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol3054$$libEasyAR.so + 288
frame #2: 0x0000004922f347f8 libEasyAR.so`\_\_\_lldb\_unnamed\_symbol2876$$libEasyAR.so + 332
frame #3: 0x00000049be2390c8 libc.so`\_\_pthread\_start(void\*) + 40
frame #4: 0x00000049be1f04f8 libc.so`\_\_start\_thread + 72
```
当代码运行栈中存在 `libEasyAR.so` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
在 lldb 中输入 `image dump sections libEasyAR.so`，可以获得动态库 `.text` 节加载地址，如下
```
(lldb) image dump sections libEasyAR.so
...
SectID Type Load Address Perm File Off. File Size Flags Section Name
...
0x00000010 code [0x0000004922e30cfc-0x0000004923654558) r-x 0x00256cfc 0x0082385c 0x00000006 libEasyAR.so..text
...
```
## 发布后的崩溃位置获取
发布后，也有可能遇到崩溃的情况。
如果出现可以重现的崩溃，可以尝试使用 Android Studio 自带的 Profile/Debug 工具。然后按照开发中的做法即可获得崩溃位置。
![crash Android debug](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-android-debug.png)
如果出现难以重现的崩溃，可以使用一些 crash 报告库，拦截应用崩溃信息，并报告到服务器。但是需要注意，崩溃信息中一定要包含代码运行栈和模块加载地址两部分信息。由于 Android 从 4.0 开始引入 ASLR（地址空间布局随机化），动态库模块加载地址在每次运行时都可能不同，会导致代码地址也会动态变化，只有知道代码栈中的代码地址和动态库模块加载地址的相对值，才能知道程序在什么位置发生了崩溃。
当代码运行栈中存在 `libEasyAR.so` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
## 其他崩溃相关信息
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* CPU 架构
aarch64/armeabi-v7a

---

## iOS/macOS/visionOS 上的崩溃分析
- 章节路径: `diagnostics/crash-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-ios.html

# iOS/macOS/visionOS 上的崩溃分析
关于 原生(iOS/macOS) 、 Unity(iOS/macOS/visionOS) 和 Unity 编辑器(macOS) 上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在 XCode 中调试时需要的信息如下图。
![crash iOS](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-ios.png)
在 lldb 中输入bt，可以获得崩溃原因和代码运行栈，如下
```
(lldb) bt
\* thread #11, stop reason = EXC\_BAD\_ACCESS (code=1, address=0x9c40)
\* frame #0: 0x00000001057e7cb0 easyar`\_\_\_lldb\_unnamed\_symbol2693$$easyar + 6984
frame #1: 0x00000001057e5e14 easyar`\_\_\_lldb\_unnamed\_symbol2692$$easyar + 276
frame #2: 0x00000001057e2500 easyar`\_\_\_lldb\_unnamed\_symbol2532$$easyar + 360
frame #3: 0x00000001f3d60bfc libsystem\_pthread.dylib`\_pthread\_start + 320
```
当代码运行栈中存在 `easyar` 或 `libEasyAR.dylib` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
在 lldb 中输入 `image list easyar` 或者 `image list libEasyAR.dylib`，可以获得动态库加载地址，如下
```
(lldb) image list easyar
[ 0] DF06BDD8-A8AF-3982-897D-A906EE229A4F 0x0000000105730000 /Users/<user>/Library/Developer/Xcode/DerivedData/helloar-bpvpobshgxnnwwdiryfjufioysag/Build/Products/Debug-iphoneos/helloar.app/Frameworks/easyar.framework/easyar
```
## 开发中的崩溃位置获取（Unity）
在使用 Unity 开发应用时，还可以使用 Unity 的日志来分析崩溃。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|macOS|\~/Library/Logs/Unity/Editor.log|
|播放器|iOS|使用 XCode 的 lldb 控制台|
|播放器|macOS|\~/Library/Logs/Company Name/Product Name/Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
托管异常(C#)可以在 Unity 编辑器的 Console 窗口中查看（Unity 主菜单的 `Window -> General -> Console`）。
## 发布后的崩溃位置获取
发布后，也有可能遇到崩溃的情况。此时从设备的 Privacy - Analytics & Improvements - Analytic Data 查看或通过 TestFlight 和 App Store 来[收集崩溃日志](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs#Collect-crash-reports-from-TestFlight-and-the-App-Store)。
以下为一个崩溃的例子：
```
Incident Identifier: 5916E252-D8C2-43C3-B583-7E38399597C9
CrashReporter Key: 2075d595d8d96cf07913a12798d5e0aba79c5358
Hardware Model: iPhone9,2
Process: ARManualEditorDemo [2352]
Path: /private/var/containers/Bundle/Application/ED9F6959-612A-4595-A7B9-3F573B5097DD/ARManualEditorDemo.app/ARManualEditorDemo
Identifier: cn.easyar.demo.ARManualEditor
Version: 6 (2.0.1)
Code Type: ARM-64 (Native)
Role: Non UI
Parent Process: launchd [1]
Coalition: cn.easyar.demo.ARManualEditor [1831]
Date/Time: 2019-09-17 16:21:13.1246 +0800
Launch Time: 2019-09-17 16:08:08.3605 +0800
OS Version: iPhone OS 12.4 (16G77)
Baseband Version: 5.70.01
Report Version: 104
Exception Type: EXC\_BREAKPOINT (SIGTRAP)
Exception Codes: 0x0000000000000001, 0x000000019d7e86fc
Triggered by Thread: 0
Thread 0 name: Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0 JavaScriptCore 0x000000019d7e86fc WTFCrashWithInfo+ 2471676 (int, char const\*, char const\*, int) + 20
1 JavaScriptCore 0x000000019dd85da0 llint\_slow\_path\_get\_by\_val + 6032
2 JavaScriptCore 0x000000019d7a25cc llint\_entry + 34380
...
13 JavaScriptCore 0x000000019d799cec vmEntryToJavaScript + 268
14 JavaScriptCore 0x000000019dccb4d0 JSC::Interpreter::executeCall+ 7595216 (JSC::ExecState\*, JSC::JSObject\*, JSC::CallType, JSC::CallData const&, JSC::JSValue, JSC::ArgList const&) + 424
15 JavaScriptCore 0x000000019dead560 JSC::profiledCall+ 9569632 (JSC::ExecState\*, JSC::ProfilingReason, JSC::JSValue, JSC::CallType, JSC::CallData const&, JSC::JSValue, JSC::ArgList const&) + 188
16 JavaScriptCore 0x000000019d7df170 JSObjectCallAsFunction + 376
17 EasyARPlayer 0x000000010353d284 0x10326c000 + 2953860
18 EasyARPlayer 0x000000010363c880 0x10326c000 + 3999872
19 EasyARPlayer 0x000000010364ee1c 0x10326c000 + 4075036
20 EasyARPlayer 0x0000000103295388 0x10326c000 + 168840
21 GLKit 0x00000001a337b91c -[GLKView \_display:] + 256
...
33 libdyld.dylib 0x0000000195e468e0 start + 4
...
Thread 8:
0 libsystem\_kernel.dylib 0x0000000195f92ee4 \_\_psynch\_cvwait + 8
1 libsystem\_pthread.dylib 0x000000019600dcf8 \_pthread\_cond\_wait$VARIANT$mp + 636
2 easyar 0x0000000102fba7c0 0x1028b4000 + 7366592
3 easyar 0x0000000102e7627c 0x1028b4000 + 6038140
4 easyar 0x0000000102e452e8 0x1028b4000 + 5837544
5 libsystem\_pthread.dylib 0x00000001960152c0 \_pthread\_body + 128
6 libsystem\_pthread.dylib 0x0000000196015220 \_pthread\_start + 44
7 libsystem\_pthread.dylib 0x0000000196018cdc thread\_start + 4
...
Binary Images:
0x1023e4000 - 0x1024f3fff ARManualEditorDemo arm64 <0fb0d9b7d18c3e2ebf44e950a68af61f> /var/containers/Bundle/Application/ED9F6959-612A-4595-A7B9-3F573B5097DD/ARManualEditorDemo.app/ARManualEditorDemo
...
0x1028b4000 - 0x10310bfff easyar arm64 <cb52ccf821e33255a0c30ca2422d2862> /var/containers/Bundle/Application/ED9F6959-612A-4595-A7B9-3F573B5097DD/ARManualEditorDemo.app/Frameworks/easyar.framework/easyar
...
EOF
```
其中，包含 `easyar` 的代码栈有
```
2 easyar 0x0000000102fba7c0 0x1028b4000 + 7366592
3 easyar 0x0000000102e7627c 0x1028b4000 + 6038140
4 easyar 0x0000000102e452e8 0x1028b4000 + 5837544
```
这里的 0x0000000102fba7c0 为代码在内存中的虚拟地址，0x1028b4000 为 `easyar` 的模块加载地址，7366592 为偏移量。
从 `Binary Images` 的部分也能看出0x1028b4000 为 `easyar` 的模块加载地址。
需要注意，崩溃信息中一定要包含代码运行栈和模块加载地址两部分信息。由于 ASLR（地址空间布局随机化），动态库模块加载地址在每次运行时都可能不同，会导致代码地址也会动态变化，只有知道代码栈中的代码地址和动态库模块加载地址的相对值，才能知道程序在什么位置发生了崩溃。
当代码运行栈中存在 `easyar` 或 `libEasyAR.dylib` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
## 其他崩溃相关信息
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台和 CPU 架构
* iOS
arm64
* macOS
x86\_64/arm64
* visionOS
arm64

---

## Windows 上的崩溃分析
- 章节路径: `diagnostics/crash-windows.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/crash-windows.html

# Windows 上的崩溃分析
关于 原生(Windows) 和 Unity 编辑器(Windows)上的崩溃，可参考如下说明。
## 开发中的崩溃位置获取
在Visual Studio中调试时需要的信息如下图。
![crash Windows](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-crash-windows.png)
其中崩溃原因为
```
Exception thrown at 0x00007FFB7747317B (EasyAR.dll) in HelloAR.exe: 0xC0000005: Access violation writing location 0x0000000000009C40.
```
代码运行栈为
```
> EasyAR.dll!00007ffb7747317b() Unknown
EasyAR.dll!00007ffb774719cc() Unknown
EasyAR.dll!00007ffb77477db3() Unknown
EasyAR.dll!00007ffb77474eb3() Unknown
ucrtbase.dll!00007ffbfee910b2() Unknown
kernel32.dll!00007ffc009f7c24() Unknown
ntdll.dll!00007ffc0148d721() Unknown
```
动态库加载地址为
```
0x00007FFB75BC0000
```
当代码运行栈中存在 `EasyAR.dll` 相关的内容时，可能说明崩溃和 EasyAR 有关；如果不存在，则有较大概率崩溃和 EasyAR 无关。
## 开发中的崩溃位置获取（Unity）
在使用 Unity 开发应用时，还可以使用 Unity 的日志来分析崩溃。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|Windows|%LOCALAPPDATA%\\Unity\\Editor\\Editor.log|
|播放器|Windows|%USERPROFILE%\\AppData\\LocalLow\\CompanyName\\ProductName\\Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
托管异常(C#)可以在 Unity 编辑器的 Console 窗口中查看（Unity 主菜单的 `Window -> General -> Console`）。
## 其他崩溃相关信息
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台
Win32
* CPU 架构
x86\_64/x86

---

## 问题诊断和报告
- 章节路径: `diagnostics/diagnostics.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/diagnostics.html

# 问题诊断和报告
本章主要描述构建AR应用时可能遇到的问题、主要的分析方法，以及报告问题所需要收集的信息和联系途径。
## AR 场景中问题分析的挑战
在 AR 场景中的问题分析，存在一些独特的挑战。
### 输入的不确定性
在传统应用中，输入通常是确定的点击或键盘事件。而在 AR 中，输入源自变动的物理环境，这带来了极大的分析难度。AR 应用需要结合物理环境来使用，但开发和测试时，在物理环境中无法每次获得相同的输入，即使按照同一条路线行进，取得的相机图像、加速度计、陀螺仪等传感器的数据都可能产生一些变化，而这对跟踪结果的影响可能是巨大的。
EasyAR 中提供了 EIF 文件的录制和回放功能，可以在一定程度上缓解输入的不确定性，但由于算法的不确定性，最终的跟踪结果本质上还是不确定的。同时，EIF 录制数据覆盖不全、光照变化、行人或车辆造成的动态遮挡等，也会影响实际使用时的跟踪质量。
### 算法的不确定性
AR 的核心算法是一些视觉算法，例如 SLAM（即时定位与地图构建）。这些算法本质上是概率性的而非确定性的。
当输入的相机图像缺乏显著的特征时，算法可能使用历史位置姿态和加速度计、陀螺仪等传感器数据进行预测，预测的位置和姿态的结果会随着时间推移而累积，产生飘移。而每次的预测结果和数据的传入时机、设备的温度、CPU 的频率、网络传输速度等外界因素有关，存在动态变化，累积下来即使是同样的输入，多次运行的结果也可能偏差很大。
## 不同问题的分析方法
对于不同的问题，可能需要不同的分析方法。
### 日志
对于一些程序运行不正常的情况，例如黑屏、无法正常定位、无法正常跟踪的情况，最基本的方法是查看日志，检查其中是否有错误信息。EasyAR 中产生的日志，均会使用特定的标签，便于识别。
### 崩溃
有时候程序会发生崩溃，崩溃的位置可能在库的代码中，也可能在程序自己的代码中。崩溃发生的原因有可能是由于程序本身的问题，也可能是库中存在问题。
### 抖动、跳动等视觉异常
由于传感器数据精度或者算法适配原因，可能会发生定位抖动或跳动。此时应尝试使用不同设备重现此问题，并截图、录屏和录制 EIF 文件。
## 平台专用指南
问题诊断和报告与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [日志分析 Android](log-android.html)
* [日志分析 iOS/macOS/visionOS](log-ios.html)
* [日志分析 Windows](log-windows.html)
* [崩溃分析 Android](crash-android.html)
* [崩溃分析 iOS/macOS/visionOS](crash-ios.html)
* [崩溃分析 Windows](crash-windows.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)
* [Unity 简介](../unity/diagnostics/diagnostics.html)
* [Unity UI消息](../unity/diagnostics/ui-messages.html)
* [Unity 开发者模式](../unity/diagnostics/developer-mode.html)
* [Unity 录制EED dump文件](../unity/diagnostics/event-dump.html)
* [Unity 问题报告](../unity/diagnostics/report.html)
* [Unity Diagnostics Controller 组件参考](../unity/diagnostics/comp-DiagnosticsController.html)
* [日志分析](log-wechat.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)
* [问题报告](../wechat/diagnostics/report.html)
* [日志分析 Android](log-android.html)
* [日志分析 iOS/macOS/visionOS](log-ios.html)
* [日志分析 Windows](log-windows.html)
* [崩溃分析 Android](crash-android.html)
* [崩溃分析 iOS/macOS/visionOS](crash-ios.html)
* [崩溃分析 Windows](crash-windows.html)
* [抖动、跳动等视觉异常分析 截图和录屏](recordings.html)
* [抖动、跳动等视觉异常分析 XR头显的录屏](recordings-headsets.html)
* [抖动、跳动等视觉异常分析 使用EIF复现异常](simulation.html)

---

## Android 上的日志分析
- 章节路径: `diagnostics/log-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-android.html

# Android 上的日志分析
关于 原生(Android) 和 Unity(Android) 上的日志，可参考如下说明。
## 日志获取方法
可以通过 Android Studio 或者 `adb logcat` 获得日志。推荐使用 `adb logcat` 以获得完整的日志。
使用时可能需要开启 Android 设备的开发者模式，开启 USB 调试或无线调试，连接 USB 线或通过 WLAN 进行配对和连接。请参考 Android 调试桥（[中文](https://android-docs.cn/tools/adb) [英文](https://developer.android.com/tools/adb)）。
以下为通过 WLAN 进行配对并连接，使用 `adb logcat` 的例子。
![log Android logcat](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-android-logcat.png)
连接 `adb` 后，首先使用 `adb logcat -c` 清空之前的日志，然后运行 `adb logcat > log.txt` 即可将日志输出到 `log.txt` 。此时运行程序，直到出错，然后使用 `Ctrl + C` 结束日志输出。
以下为一个日志文件的例子。
![log Android](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-android.png)
## 日志的理解
以下 tag 是调试时需要特别关注的。
* EasyAR
EasyAR 输出的日志
* Unity
Unity 引擎在 C# 层输出的日志
* UnityPlayer
Unity 引擎在 Java/JNI 层输出的日志
* libunity
Unity 引擎在 C++ 或 IL2CPP 层输出的日志
* AndroidRuntime
Android 系统在 Java 异常未捕捉时输出的日志
* ActivityManager
Android 系统在 ANR 等情况下输出的日志
在分析错误时，经常需要弄清错误发生的条件，例如调用的函数、参数、相关的状态。
## 反馈时的注意事项
反馈时请提供未过滤 tag 的日志信息，因为有时候系统底层库会发出详细的出错原因，而这些库的 tag 在不同系统上是不同的。
此外，反馈时需要附带以下信息。
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* CPU 架构
aarch64/armeabi-v7a

---

## iOS/macOS/visionOS 上的日志分析
- 章节路径: `diagnostics/log-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-ios.html

# iOS/macOS/visionOS 上的日志分析
关于 原生(iOS/macOS) 、 Unity(iOS/macOS/visionOS) 和 Unity 编辑器(macOS) 上的日志，可参考如下说明。
## 日志获取方法
如果需要分析 iOS/visionOS 设备上的应用，则使用USB线将设备与 macOS 开发设备连接。如果需要分析 macOS 设备上的应用或程序，则这一步无需操作。
在 macOS 开发设备上，打开 `Finder -> Applications -> Utilities -> Console`。在 Console 中点击 `Start streaming`，然后运行需要分析的程序。打开应用或程序，直到 Console 中出现日志，在该日志上点右键，选择 `Show Process "<应用名>"`，即可查看该应用或程序进程的所有日志。
以下为一个例子。
![log macOS](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-macos.png)
按 `Cmd + A` 选中所有日志，然后按 `Cmd + C`，可将日志复制到剪贴板。
对于 macOS 上的程序，如果是命令行程序，也可以从终端获得日志输出。
此外，也可以通过 XCode 调试应用或程序，并从 XCode 的日志窗口获得日志。
## Unity 内置日志
在使用 Unity 开发应用时，除了平台自带的日志分析手段之外，Unity 编辑器还提供了额外的调试手段。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|macOS|\~/Library/Logs/Unity/Editor.log|
|播放器|iOS|使用 XCode 的 lldb 控制台|
|播放器|macOS|\~/Library/Logs/Company Name/Product Name/Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
## 日志的理解
在分析错误时，经常需要弄清错误发生的条件，例如调用的函数、参数、相关的状态。
## 反馈时的注意事项
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台和 CPU 架构
* iOS
arm64
* macOS
x86\_64/arm64
* visionOS
arm64

---

## 微信小程序上的日志分析
- 章节路径: `diagnostics/log-wechat.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-wechat.html

# 微信小程序上的日志分析
本文介绍了在微信小程序 AR 环境下进行日志获取和分析的完整流程。
## 使用微信小程序 vConsole
由于微信小程序 AR 只能在实机运行和调试，使用 vConsole 观察实时输出是调试的关键，基础用法可参考[微信小程序官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/usability/vConsole.html)。
### 实机调试中如何启用 vConsole
在 AR 界面点击右上角**第一个按钮** > 点击下方工具栏中的**开发调试** > 点击**打开调试** > 在弹出窗口中点击 **确定**以重启小程序。
![打开调试](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat01.png)
![重新打开后生效](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat02.png)
此后界面上会持续显示 **vConsole** 悬浮按钮。
![vConsole按钮](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat03.png)
点击 **vConsole** 按钮即可查看当前运行的所有日志：
![小程序日志](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat04.png)
### 如何区分日志来源
日志来源一般可以分为：
* **微信小程序系统日志**：通常在页面路由跳转、组件生命周期变化时触发，在 vConsole 中以蓝字显示。
* **xr-frame 日志**：由官方渲染框架打印，日志内容以 `[xr-frame]` 开头。
* **用户自定义日志**：由开发者通过 `console.log()` 等标准接口打印。
* **小程序框架错误日志**：由微信底层抛出，内容以 `MiniProgramError` 开头。
* **Mega 小程序插件日志**：由 Mega 小程序插件内部打印，日志内容以中括号包裹的类名开头（如 [MegaTracker]），目前主要在捕获异常时输出。
* **示例 1**：
![小程序日志举例1](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat05.png)
第一部分蓝字是系统日志，显示了页面路由及加载状态
第二部分以 `[xr-frame]` 开头，展示了渲染框架的生命周期信息。
第三部分是开发者自定义输出。
* **示例 2**：
![小程序日志举例2](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat06.png)
出现了 `[MegaTracker]`、`[EasyARSession(xrframe)]` 等类名开头的日志，这代表 Mega 插件捕获到了运行异常。
* **示例 3**：
![小程序日志举例3](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat07.png)
`MiniProgramError` 中出现了 `WAXRFrameRenderContext.js` 字样，说明使用 xr-frame 相关的接口或组件配置出现了问题。
* **示例 4**：
![小程序日志举例4](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat08.png)
该日志说明 mega 插件中的 `onCloudLocalization` 方法运行时出现了异常导致小程序框架抛出错误。
### Mega 小程序插件的日志格式
由 [dumpLog(signal)](../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_dumpLog_member_1_) 方法导出的日志以 `|` 分隔，内容依次是：
* **时间戳**：`ISO 8601` 标准格式，表示打印日志时的系统时间。
* **日志级别**：包括 `Info`、`Warning`、`Error`、`FatalError`。
* **类名**：以中括号包裹。
* **详细信息**：具体的日志描述。
* **调用者**：通常为 `Unspecified`（表示自然运行过程）；若为用户调用接口引发的异常则显示为 `User`。
* **运行阶段**：显示为 `Unspecified` 表示无需关注；显示其他字段则表示该异常发生在特定运行阶段。
![小程序日志](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-wechat09.png)
## 如何记录和转发日志
介绍日志的获取和导出方案。
### vConsole 导出日志
在打印日志的位置点击右侧复制按钮导出。
### Mega 小程序插件 dump log 接口
通过调用 [dumpLog(signal)](../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_dumpLog_member_1_) 接口控制导出日志流程：
* **传入 `true`**：启动记录。
* **传入 `false`**：停止记录，并返回生成的 **文件临时路径 (tempFilePath)**。
通常建议将记录逻辑与 UI 按钮绑定，在开始记录时通过 [wx.showToast()](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html) 方法提示记录开始，在记录结束时通过 [wx.shareFileMessage()](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareFileMessage.html) 方法将记录的文件通过微信聊天转发。
```
/\*\*
\* 处理 Session 记录逻辑
\* @param signal true 为开始记录，false 为结束记录并转发
\*/
dumpLog(signal: boolean): void {
// 调用接口获取路径
const logPath = session.dumpLog(signal);
// signal 为 true 时，接口返回空字符串，表示正在记录
if (logPath.length == 0) {
wx.showToast({
title: '开始记录日志',
icon: 'success',
duration: 2000
});
return;
}
// signal 为 false 时，处理返回的文件路径
wx.shareFileMessage({
filePath: logPath,
success() {
wx.showToast({
title: '日志转发成功',
icon: 'success',
duration: 2000
});
},
fail() {
wx.showToast({
title: '日志转发失败',
icon: 'error',
duration: 2000
});
}
})
}
```
>
> 这个例子演示了如何在 xr-frame 组件中使用
`> session.dumpLog()
`> 方法记录并转发日志文件，并且给出相应的 Toast 提示。
>
> **重要事项**
如果使用 Mega 时遇到定位或跟踪相关的问题而不是程序异常，除了日志外，**请务必提供当时的录屏文件和 session dump 文件**。纯日志文件仅能提供侧面参考，录屏与 dump 数据才是排查问题的**核心依据**。
## 相关主题
* [如何记录与转发 Mega AR Session 的 dump 文件](../wechat/mega/session-dump.html)。

---

## Windows 上的日志分析
- 章节路径: `diagnostics/log-windows.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/log-windows.html

# Windows 上的日志分析
关于 原生(Windows) 和 Unity 编辑器(Windows)上的日志，可参考如下说明。
## 日志获取方法
如果程序带有控制台，可以从控制台获取日志。
![log Windows](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-windows.png)
否则，需要使用 `Log.setLogFunc` 进行日志重定向，并自己提供输出日志的方法。
## Unity 内置日志
在使用 Unity 开发应用时，除了平台自带的日志分析手段之外，Unity 编辑器还提供了额外的调试手段。
Unity 日志分为 Unity 编辑器日志和 Unity 播放器日志，可以通过以下方法获取。
|Unity 环境|操作系统|日志地址|
|编辑器|Windows|%LOCALAPPDATA%\\Unity\\Editor\\Editor.log|
|播放器|Windows|%USERPROFILE%\\AppData\\LocalLow\\CompanyName\\ProductName\\Player.log|
编辑器日志也可以通过 Console 窗口右上角菜单的 Open Editor Log 命令打开。
## 日志的理解
一般来说，输出级别为 `Error` 的错误（显示为红色），是比较重要的问题，需要检查。例如下面是找不到摄像头的错误。
![log Windows error](https://doc-asset.easyar.com/develop/diagnostics/media/diagnostics-log-windows-error.png)
在分析错误时，经常需要弄清错误发生的条件，例如调用的函数、参数、相关的状态。
## 反馈时的注意事项
反馈时需要附带以下信息。
* EasyAR Sense 和 EasyAR Sense Unity Plugin 的版本号
如 4.7.0.11800-cf8e24e30
* 社区版/企业版
* 平台
Win32
* CPU 架构
x86\_64/x86

---

## 头显设备录屏：记录沉浸式 AR/MR 体验
- 章节路径: `diagnostics/recordings-headsets.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/recordings-headsets.html

# 头显设备录屏：记录沉浸式 AR/MR 体验
在使用增强现实（AR）或混合现实（MR）头显设备进行开发、测试或用户支持时，录屏是复现和分析问题的重要手段。然而，与移动设备不同，头显录屏涉及到透视（Passthrough）、注视点渲染（Foveated Rendering）等特殊技术，录屏画面通常并非完全等同于用户双眼直接所见的完整立体视图。因此，在解读录屏内容时，需特别注意其与实际人眼体验之间的差异。
## 为什么头显录屏存在视觉差异？
**用户必须特别注意**：头显设备的录屏画面并不完全等于您在镜片后看到的实际画面。如果在录屏中发现了异常，请务必结合实际感受进行描述，以免误导开发人员。
以下是主要差异点：
1. 分辨率与清晰度差异
* 录屏：通常是单眼（如左眼）1080p 或更低分辨率的视频流。
* 人眼：根据应用的不同，现代头显的单眼分辨率可达 2K 甚至更高。
* 影响：您在录屏中看到的文字、画面模糊，在头显内可能不存在；反之，您在头显内看到的微小边缘锯齿，录屏可能完全看不出来。
1. 视场角（FOV）差异
* 录屏：录制的画面通常是方形的。尤其在宽视场角设备中，边缘内容常被裁切。
* 人眼：人眼看到的画面是双眼显示的，视野更大。
* 影响：如果您的问题发生在视野边缘，录屏可能无法准确体现。
1. 注视点渲染（Foveated Rendering）影响
* 录屏：全屏视野中所有内容都会包含在内，包括低分辨率边缘区域。
* 人眼：人眼注视中心是高分辨率的，而非注视中心边缘是低分辨率的。
* 影响：您实际感觉画面很清晰，但回看录屏时发现部分区域是模糊的。这通常是正常现象，并非Bug。因此，在录屏时务必专注于要展示的部分，这将确保该区域是清晰的。
1. 帧率与刷新率影响
* 录屏：录制视频的帧率通常以 30FPS 或 60FPS 的帧率进行。
* 人眼：实际体验的屏幕刷新率可能达到 90Hz 或者 120Hz。
* 影响：非常轻微的帧率下降在录屏中可能无法察觉，但人眼会感受明显的“卡顿”或“眩晕感”。如果录屏看起来流畅但实际体验则不然，这通常是性能问题，在录屏后务必说明。
## OST 头显的特殊说明
**特别注意**：如果您使用的是 OST（Optical See-Through, 光学透视）头显，例如 Rokid、Xreal 等 AR 眼镜，使用录屏功能并不能录制到人眼看到的实景内容。
### 什么是 OST 设备？
OST 设备通过半透明的光学镜片直接将光线投射到您的眼中，虚拟内容则通过微型投影或波导叠加在视野中，让您同时看到真实世界和叠加的虚拟图像。它拍摄外部世界的摄像头仅用于空间定位，并不用于显示。由于这一机制，设备本身无法“录制”人眼所见的真实场景。
### OST 设备录屏的局限性
* 无法录制实景：OST 设备的录屏功能只录制虚拟内容层（GUI、3D 模型、UI 指针等）。
* 背景是黑的：您在电脑或手机上回放这段视频时，看到的将是纯黑色背景上的虚拟物体，完全丢失了真实环境的上下文。
* 遮挡关系丢失：如果虚拟物体应该被真实物体（如您的手、桌子）遮挡，在录屏中它们会悬浮在黑屏上，看起来像是错误的层级关系。
### 虚拟内容叠加的视觉误差问题
即使在理想环境下，OST 头显所呈现的虚拟内容与真实世界之间的对齐也不可避免地存在一定程度的视觉误差。这类误差并非总是由软件 bug 或跟踪失效引起，而往往源于设备物理特性与人类视觉系统的根本差异，部分误差在当前技术条件下无法完全消除。
在提交反馈时，注意区分以下情况：
* 光学对齐误差：
* 现象：当您移动头部时，虚拟物体似乎在“漂浮”或与真实物体的位置有微小偏差。
* 原因：用户透过光学镜片直视现实世界，而虚拟内容的渲染坐标系通常基于头部跟踪与环境理解系统（如 SLAM）构建。由于光学显示光路与用于空间定位的摄像头/IMU 之间存在物理偏移，且难以做到亚像素级联合标定，虚实对齐在边缘视野或近距离场景中尤为敏感。
* 人眼标定局限：
* 现象：虚拟物体看起来有重影（鬼影）、边缘模糊，或者感觉图像没有正确投射在空间中。
* 原因：OST 设备极度依赖精确的瞳距 (IPD) 和眼球位置标定。如果设备没有针对您的眼睛进行精确校准，或者您佩戴头盔的位置发生了偏移，光学引擎投射的光线就无法准确进入您的瞳孔。然而，即便设备存在校准，但校准过程基于有限采样点，难以精确匹配每位用户的眼球几何结构、角膜曲率及视觉感知习惯。微小的标定偏差会导致虚拟物体在深度或横向位置上出现系统性偏移。
* 个体视觉差异：
* 现象：不同用户对虚拟内容位置的主观判断可能不同。
* 原因：不同用户的视力(如近视、散光)、动态聚焦能力等都会影响观察虚拟内容叠加效果的主观判断，OST 设备可能缺乏实时眼动跟踪与个性化光学校正能力，因此无法针对每个用户动态补偿这些差异。
* 环境因素干扰：
* 现象：在明亮环境下虚拟内容变淡、看不清甚至不可见；在暗环境下虚拟内容过曝、甚至产生鬼影。
* 原因：OST 设备将微型投影或波导的虚拟光线与真实世界的环境光线直接叠加。如果真实环境过亮，会盖过微弱的虚拟光；反之亦然。这种光学伪影是 OST 设备的固有光学特性。
> **注意**
此类误差属于 OST AR 眼镜技术的固有特性，而非功能故障。在问题排查时，请区分“可修复的软件/跟踪问题”与“受硬件与生理限制的体验边界”。若用户反馈涉及轻微错位、边缘畸变或深度感知不一致，建议先确认是否处于设备标称的使用条件（如工作距离、光照范围、校准状态）内。
### 如何处理 OST 设备的反馈？
如果您在使用 OST 设备时遇到视觉问题，在排除以上设备局限带来的因素之后，您可以进行录屏进行反馈。但单纯提交录屏内容通常是不够的：
1. 配合照片：请使用手机拍摄一张您透过镜片看到的实际画面照片（称为“眼视角照片”）。这能展示虚拟物体与真实环境的相对位置。
2. 描述环境：详细描述您所处的环境（光照条件、背景颜色、是否存在动态如行人等），因为 OST 的显示效果极度依赖环境光。
## 常见头显设备的录屏方法
> **注意**
录屏过程中设备可能降低渲染帧率或分辨率，影响对流畅度和跟踪稳定性的判断。建议在复现问题后尽快录制，避免长时间运行影响结果。
### Apple Vision Pro
1. 抬头看屏幕顶部，直到看到控制中心点。专注于这一点并单击。
2. 注视并点击 控制中心 > “录制我的视野”按钮 ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-record-button.png) 开始录制。
3. 若要停止录制，打开控制中心，然后再次轻点“录制我的视野”。
4. 您的视野录制会存在“照片”App ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-photos.png) 中。
### PICO 4 Ultra Enterprise
1. 打开控制中心 > 设置 > 通用 > 投屏、录屏与截屏，在“录屏和截屏”中选择录屏模式为“空间”。
2. 短按手柄的 Home 键，在屏幕弹出的菜单中选中“录屏”按钮，扣动扳机键开始录屏。
3. 此时系统会有开始倒计时提示，立即退回至待录制应用的界面，在倒计时结束后自动开始录制。
4. 再次短按手柄的 Home 键，重复选择“录屏”按钮即可停止录制。
5. 您的录制文件默认保存在设备的“内部存储/DCIM/ScreenRecord”目录。
### Rokid AR Studio
1. 进入桌面，找到底部状态栏，点击用户头像旁边的“快捷设置”区域。
2. 在弹出的窗口中点击“录制”按钮，立即退回至待录制应用的界面。系统自动开始录制。
3. 点击 Station Pro 上 X 按钮退回桌面。再次点击“快捷设置”区域的“录制”按钮即可停止录制。
4. 您的录制文件默认保存在设备的“内部共享存储空间/ScreenRecorder”目录。
### XREAL Air2 Ultra
1. 在 Beam Pro 屏幕上下滑呼出眼镜的控制中心，点击上方的“录屏”按钮。
2. 此时系统会有倒计时提示，立即退回至待录制应用的界面。
3. 点击屏幕上方悬浮的红色“停止”按钮即可停止录制。
4. 您的录制文件默认保存在设备的“内部共享存储空间/Movies/Record”目录。
## 最佳实践建议
使用头显录屏反馈问题时，关注以下几点：
* 提交时明确标注设备型号、录屏方式及环境因素。
* 若问题涉及深度、遮挡或跟踪抖动，补充文字描述人眼实际观察到的现象，因为录屏可能无法准确呈现。
* 对于关键场景，可配合外部摄像机拍摄用户佩戴头显时的实景操作，以提供更全面的上下文。
头显录屏虽便捷，但始终是对体验的近似还原。最可靠的诊断仍需结合日志、传感器数据与用户主观反馈。有关日志采集方法，请参阅:
* [Android 日志记录](log-android.html)
* [iOS 日志记录](log-ios.html)
* [Unity 日志记录](log-windows.html)

---

## 截图与录屏：记录 AR 视觉异常的重要手段
- 章节路径: `diagnostics/recordings.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/recordings.html

# 截图与录屏：记录 AR 视觉异常的重要手段
在增强现实（AR）应用的使用过程中，您可能会遇到诸如模型错位、内容跳动、跟踪丢失、遮挡异常等视觉体验问题。由于 AR 内容的效果好坏高度依赖于设备、环境光照和算法表现，这些问题往往具有瞬时性和上下文依赖性，单纯的通过模糊的文字（如“模型飘走了”）难以准确传达问题的具体细节。因此，及时使用截图或录屏功能记录异常现象，对于后续的问题诊断、技术复现和用户体验优化至关重要。
## 为什么需要截图与录屏？
当 AR 应用的表现与预期不符时，使用截图和录屏功能具有以下关键作用：
* **精准还原问题场景**
截图能捕捉异常发生的精确瞬间（如特定的内容跳动或模型穿模），而录屏则能完整记录导致异常的整个过程和环境交互。
* **辅助开发团队技术诊断**
通过查看您捕获的视觉证据，技术支持团队或开发人员可以快速定位问题根源（例如：是设备性能问题、SLAM 跟踪丢失，还是渲染管线错误），从而避免了繁琐的猜测和反复询问。
* **保留设备环境信息**
录屏不仅包含应用内的画面，通常还会包含设备的系统状态栏（时间、电量、网络信号），这对于诊断设备过热降频或网络波动导致的加载问题至关重要。
## 常见移动设备上的操作方法
在截图或录屏前，请确保 AR 场景已经加载完毕，并且异常行为正在发生或即将发生。请尽量保持设备稳定，以便画面清晰可辨。
### 通用操作原则
* 截图：适用于捕捉静态的视觉错误（如内容穿模、模型错位）。建议连续拍摄多张，以覆盖异常变化的不同阶段。
* 录屏：适用于捕捉动态行为（如跟踪丢失导致的画面抖动、交互时的卡顿）。建议录制时长控制在 15-30 秒，聚焦于问题发生的核心过程。
### iOS 设备（iPhone/iPad）
#### 截图：
* 带 FaceID 的设备：快速同时按下和松开 电源键 + 音量上键。
* 带 Home 键的设备：快速同时按下和松开 电源键 + Home 键。
* 截图将自动保存至“照片”App ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-photos.png)。
#### 录屏：
1. 进入 设置 > 控制中心 > 更多控制，添加“录屏”。
2. 从屏幕右上角下滑打开控制中心。
3. 点击 录屏按钮 ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-record-button.png) 开始录制；点击 停止按钮 ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-record-stop-button.png) 停止录制。
4. 如需录制系统声音或麦克风音频，长按录屏按钮进行设置。
5. 录制视频保存在“照片”App ![](https://doc-asset.easyar.com/develop/diagnostics/media/ios-photos.png) 中。
> **注意**
* 录屏时确保 设置 > 控制中心 > App内访问 是打开状态。
* 在录屏时可能因性能限制导致效果下降，建议在复现问题后尽快录制，避免长时间运行影响结果。
### Android 设备（以主流品牌为例）
#### 截图：
* 通用方法：快速同时按下和松开 电源键 + 音量下键。
* 部分厂商支持手势截图（如三指下滑）或智能助手快捷方式。
* 截图将自动保存至“相册 > 截屏”中。
#### 录屏：
* 原生 Android（Android 11 及以上）：
1. 下拉通知栏，找到“屏幕录制”快捷图标（若无，可在“编辑”中添加）。
2. 点击开始录制，可选择是否包含麦克风音频。
3. 再次点击屏幕左上角的录制图标停止录制。
4. 录制视频保存在“相册 > Movies”。
* 厂商定制系统（如 Samsung One UI、HyperOS、ColorOS、OriginOS）：
1. 通常在快捷面板中提供录屏入口（若无，可点加号添加）。
2. 点击开始录制。
3. 点击屏幕上方（不同厂商可能有所不同）的停止按钮停止录制。
4. 录制视频保存在“相册 > 录屏”中。
> **提示**
具体路径示例：
* 三星：下滑手机顶帘 > 录屏工具
* 小米/Redmi：下拉通知栏 > 屏幕录制
* OPPO/Realme：滑动屏幕顶部通知栏或下拉菜单栏 > 屏幕录制
* VIVO/iQOO: 屏幕顶部右侧下滑（早期机型为底部上滑）> 超级截屏 > 录制屏幕
* 华为：屏幕顶部右侧下滑 > 屏幕录制
* 荣耀：状态栏向下滑出通知面板，继续向下滑动出整个通知面板 > 屏幕录制
> **注意**
* 部分 Android 设备在运行高负载 AR 应用时可能限制后台录屏权限，请确保录屏前关闭省电模式，并授予必要权限。
* 在录屏时可能因性能限制导致效果下降，建议在复现问题后尽快录制，避免长时间运行影响结果。
## 最佳实践建议
通过熟练掌握上述操作，您可在 AR 体验出现异常的第一时间捕获关键证据，显著提升问题沟通与解决效率。建议在提交技术支持请求时，同时提供截图/录屏、设备型号、操作系统版本、EasyAR SDK 版本及 AR 应用日志，以构建完整的故障上下文。
有关日志采集方法，请参阅:
* [Android 日志记录](log-android.html)
* [iOS 日志记录](log-ios.html)
* [Unity 日志记录](log-windows.html)

---

## 录制 EIF 数据：复现 AR 问题的高保真依据
- 章节路径: `diagnostics/simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/diagnostics/simulation.html

# 录制 EIF 数据：复现 AR 问题的高保真依据
在增强现实（AR）应用中，某些复杂的空间定位问题（如跟踪抖动、虚实错位、内容飘移等）往往难以仅通过录屏或日志完整还原。为此，我们提供了EIF数据录制功能———一种专有的高保真数据转储格式，可同步记录以下关键信息：
* 设备基本信息（型号、系统、SDK 版本等）
* 包含时间戳的摄像头图像帧
* 设备的相机内参矩阵、外参矩阵
* IMU 传感器数据
* 外部辅助输入的额外数据（如 GNSS）
## 为什么录制EIF数据至关重要？
> **重要事项**
**能够复现问题的 EIF 数据是无价的。**
EIF 数据能够完整重现问题发生时的详细上下文，使开发团队在离线环境中精确复现用户所遇场景，极大提升问题定位效率。相比录屏或日志，EIF 具备以下优势：
1. 精准复现：开发人员可在调试工具中直接回放EIF数据，重现您遇到的 Bug。
2. 底层诊断：通过全面的分析各类数据（图像、传感器、外部输入等），开发人员可以判断问题出在技术的哪个环节。
3. 节省时间：避免了漫长的沟通循环，大幅缩短从报告问题到解决问题的周期。
## 如何录制 EIF 数据
EasyAR 提供了两种 EIF 数据录制的方式。
1. 直接使用 SDK 提供的 API 接口，在您的应用中实现 EIF 数据录制的功能。
2. 使用官方提供的 Mega Toolbox App。通常适用于进行 EasyAR Mega 的开发和问题反馈。
具体操作步骤请参考我们的技术文档，获取针对您的使用方式以及设备的操作指南。
> **提示**
访问以下链接查看调用 API 接口实现应用内录制 EIF 的功能：[输入帧录制和模拟运行](../simulation/simulation.html)。
访问以下链接查看使用 Mega Toolbox App 的操作指南：[使用 Toolbox 录制手机 EIF 文件](../../mega/data-collection/simulation/toolbox.html)。
简要录制流程概览（以 Mega Toolbox App 为例）：
1. 打开 Mega Toolbox App，点击“现场定位测试&定位问题反馈数据录制”。
2. 登录您的账号，选择您的定位库，并开始测试。
3. **尝试复现您的问题**。找到一个可以稳定复现问题的操作模式（如设备朝向、浏览方式、拍摄点位等）。
4. 一切准备就绪后，点击红色“录制”按钮开始录制。
5. 问题出现后，点击红色“停止并保存”按钮。
6. 系统将自动生成一个 EIF 文件，将设备连接电脑导出至本地存储后提交。
> **注意**
EIF 文件可能较大（数百 MB 至数 GB），建议仅录制**包含问题的核心片段**（通常 10–30 秒足够）。
## 最佳实践建议
为确保您的反馈能被高效处理，请在提交时**同时包含以下四类信息**：
|信息类型|说明|
|**EIF 数据文件**|核心诊断依据，务必包含问题复现过程|
|**主观现象描述**|清晰说明您观察到的行为（如“导航箭头在向左转弯时突然跳到天花板”）|
|**录屏或截图**|辅助可视化问题，直观地展示“用户最终看到的画面是怎样的”|
|**辅助上下文信息**|包括：
• 您的设备型号与操作系统版本
• 您的应用所使用的 EasyAR SDK 的版本号
• 问题产生的环境描述（室内/室外、光照、空间大小）
• Mega 类应用需要额外提供定位库信息，可在 Unity 工具中导出
• CRS 云识别类应用需要额外提供云识别库的信息|
> **提示**
示例：“在 Apple Vision Pro（visionOS 26）上使用 EasyAR Sense Unity Plugin 4000.0.1，在室内商场进行导航，在某个位置导航路径突然发生错误。已录制 EIF 文件：`avp\_wrong\_path\_20251218.mkveif`，附录屏、环境照片及定位库信息：`MegaStudio\_ServiceInfo\_myaccount\_2025-12-18\_10-33-26.json`。”
通过提供上述完整信息包，您将显著加速问题分析与修复进程。感谢您的配合！

---

## AR 驱动的 3D 渲染
- 章节路径: `fundamentals/fundamentals.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/fundamentals/fundamentals.html

# AR 驱动的 3D 渲染
AR 应用的开发需要解决一个基础问题，就是 AR 内容的渲染。本文会以平面图像跟踪为例，描述 AR 应用的基本模块、流程和渲染实现。
## 典型的 AR 应用流程
一个典型的 AR 应用，通常是从摄像机图像中识别特定的图像、物体或场景，跟踪其位置和姿态，并按照这个位置和姿态渲染显示虚拟内容（3D 模型）的过程。
![image tracking](https://doc-asset.easyar.com/develop/fundamentals/media/fundamentals-imagetracking.jpg)
*例如上图是一个平面图形跟踪的 AR 应用*
以下为应用流程示意图。
```
flowchart TD
CameraDevice[Camera Device]
Tracker[Tracker]
Renderer[Renderer]
CameraDevice -->|Image Frame| Tracker
Tracker -->|Image Frame + Tracked Pose| Renderer
```
流程中有以下一些模块。
|模块|作用|
|物理相机|提供输入图像帧的序列。图像帧包括图像，图像生成的时间戳，有时候也可以带有摄像头在空间中的位置和姿态|
|跟踪器|从图像帧计算跟踪目标的位置和姿态。根据跟踪目标的不同，存在各种各样的跟踪器，例如平面图像跟踪器和 3D 对象跟踪器|
|渲染器|用于将相机图像和跟踪对象对应的 3D 模型渲染到屏幕上。在某些 AR 眼镜上，也可能不渲染相机图像，只渲染 3D 模型|
## 手机上的渲染
手机上的渲染分成相机画面的渲染和虚拟物体的渲染两部分。
### 相机画面的渲染
![camera image](https://doc-asset.easyar.com/develop/fundamentals/media/fundamentals-cameraimage.jpg)
相机画面渲染时，有一些需要注意的参数。
* 缩放模式
通常需要将相机画面填满整个屏幕，或者填满一个窗口，这时候会面临相机画面和屏幕/窗口的宽高比不一致的问题。
假设我们要求相机画面中心和屏幕/窗口中心对齐，保持宽高比不变，则有两种常见的缩放模式：等比缩放、等比填充。
|缩放模式|效果|
|等比缩放|在屏幕上显示所有内容，但会在左右或者上下留黑边|
|等比填充|不会有黑边，但会在左右或者上线裁掉部分画面|
* 相机图像旋转
在手机上，物理相机记录的图像通常相对于机身固定，不随屏幕显示方向变化而变化。但手机机身朝向的变化会影响到我们对于图像的上下左右方向的定义。渲染时，当前屏幕显示方向也会影响到显示的图像的方向。
通常在渲染时，需要确定一个相机图像相对于屏幕显示方向的旋转角。
* 相机图像翻转
有些情况下会用到前置摄像头，此时通常需要将画面左右翻转，以使得画面看起来像是一面镜子。
### 虚拟物体的渲染
![virtual object](https://doc-asset.easyar.com/develop/fundamentals/media/fundamentals-virtualobject.jpg)
在手机上渲染虚拟物体，需要将虚拟物体和相机画面对准。这要求我们将渲染相机和物体都放置在和真实空间完全对应的虚拟空间中，并使用物理相机相同的视场角、宽高比来进行渲染。相机画面和虚拟物体经过的透视投影变换一模一样，除了相机画面的透视投影变换大部分是发生在物理相机中，而虚拟物体的透视投影变换完全是一个计算过程。
## 头显上的渲染
头显上的渲染和手机上有一些差别，需要分两种情况。
* VST
Video See-Through，是指头显通过物理相机捕捉图像，然后在头显的屏幕上显示相机图像和虚拟内容的 AR 技术，典型代表是 Vision Pro。通常相机图像和虚拟内容的透视投影矩阵由头显提供的 SDK 进行设置，外部只需要设置虚拟内容的位置和姿态。用于跟踪的物理相机和屏幕上渲染的相机图像的相机可能在不同的位置，渲染时进行了坐标变换。
* OST
Optical See-Through，是指头显的屏幕透明，头显在屏幕上只显示虚拟内容的 AR 技术，典型代表是 HoloLens。通常虚拟内容的透视投影矩阵由头显提供的 SDK 进行设置，外部只需要设置虚拟内容的位置和姿态。用于跟踪的物理相机和屏幕上渲染的相机图像的相机可能在不同的位置，渲染时进行了坐标变换。
## 平台专用指南
AR 驱动的 3D 渲染与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [Unity 兼容性](../unity/fundamentals/unity-compatibility.html)
* [AR Session](../unity/fundamentals/session.html)
* [XR Origin](../unity/fundamentals/origin.html)
* [Target](../unity/fundamentals/target.html)
* [Camera](../unity/fundamentals/camera.html)
* [中心模式](../unity/fundamentals/center-mode.html)
* [使用Unity XR 框架](../unity/fundamentals/unity-xr.html)
* 工程配置
* [Player 工程配置](../unity/fundamentals/setup-player.html)
* [EasyAR 全局配置参考](../unity/fundamentals/setup-easyar.html)
* [示例说明](../unity/fundamentals/sample-arsession.html)
* [微信小程序](https://developers.weixin.qq.com/miniprogram/dev/framework/)
* [微信小程序 XR-Frame](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)
* [微信小程序 VisionKit](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/base.html)
* [EasyAR坐标系](../native/fundamentals/coordinates.html)
* [库加载和初始化](../native/fundamentals/initialization.html)
* [AR数据流](../native/fundamentals/dataflow.html)
* [3D空间内容展示](../native/fundamentals/contents.html)
* [在3D引擎中使用EasyAR](../native/fundamentals/3dengine.html)

---

## EasyAR 增强现实入门
- 章节路径: `getting-started/ar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/getting-started/ar.html

# EasyAR 增强现实入门
EasyAR Sense 是增强现实（Augmented Reality，AR）引擎，提供感知真实世界的能力。
EasyAR 的核心在于跟踪 （Tracking） 和渲染 （Rendering）。
* 跟踪：计算摄像机在真实世界中的位置和姿态（六自由度，6-DoF），确保虚拟对象稳定附着在目标上。
* 渲染：将 3D 模型、视频、动画等虚拟内容与真实场景融合，支持交互、碰撞和遮挡。
## EasyAR 功能概述
EasyAR 支持多种现实感知和虚实融合的能力，包括已知 2D/3D 目标的图像跟踪或者物体跟踪，以及无需标记物的运动跟踪和表面跟踪等。EasyAR 同时提供大范围的视觉定位和空间计算方案 [EasyAR Mega](../mega/intro.html)。
* EasyAR Mega
端云协同的空间计算技术，持久化的的数字孪生空间，大规模、高精度的室内外定位与虚实遮挡。
* 运动跟踪 (Motion Tracking)
无标记持续跟踪设备在三维空间中的六自由度（6DoF）位置和姿态。
* 稀疏空间地图 (Sparse Spatial Map)
设备端、小范围环境重建和视觉跟踪，小空间多人和持久化体验。
* 稠密空间地图 (Dense Spatial Map)
扫描环境生成实时 3D 网格，支持高级效果如真实碰撞和遮挡。
* 表面跟踪 (Surface Tracking)
实时检测物体表面并跟踪，支持虚拟对象放置在桌面、地面或墙面上。
* 图像跟踪 (Planar Image Tracking)
识别并跟踪平面图像，在图像上叠加虚拟内容。
* 图像云识别 (Cloud Recognition Service, CRS)
云端识别海量的平面图像，可结合本地跟踪。
* 物体跟踪 (Object Tracking)
直接从 OBJ 模型实时生成目标，识别并跟踪真实 3D 对象。
## 开发平台快速入门
EasyAR 支持 Unity, 原生平台（Android/ iOS/ windows/ macOS）， 微信小程序和 Web 平台。根据选定的开发平台，查阅对应的快速入门教程。
* [快速入门](../unity/getting-started/quickstart.html)
* [启用 EasyAR](../unity/getting-started/enable-easyar.html)
* [配置 AR 场景](../unity/getting-started/scene.html)
* [场景中的诊断信息](../unity/getting-started/diagnostics.html)
* [使用 Universal Render Pipeline（URP）](../unity/getting-started/universal-render-pipeline.html)
* [示例启动器使用说明](../unity/getting-started/sample-launcher.html)
* [选择 3D 引擎](../native/getting-started/choosing-an-engine.html)
* 快速入门
* [Android](../native/getting-started/quickstart-android.html)
* [iOS](../native/getting-started/quickstart-ios.html)
* [Windows](../native/getting-started/quickstart-windows.html)
* 启用 EasyAR
* [选择发布变种](../native/getting-started/variants.html)
* [Android](../native/getting-started/enable-easyar-android.html)
* [iOS](../native/getting-started/enable-easyar-ios.html)
* [微信小程序开发指南](../wechat/getting-started/quickstart.html)
* [快速入门](../web/getting-started/quickstart.html)

---

## EasyAR 的头显支持
- 章节路径: `headsets/headsets.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/headsets/headsets.html

# EasyAR 的头显支持
EasyAR SDK 提供了强大的跨平台 AR 功能，其设计理念同样适用于新兴的空间计算设备——头显（Headset）。本篇将介绍 EasyAR 如何支持头显设备，以及开发者可以如何利用这些功能来构建沉浸式体验。
## 术语说明
在本文档中，“头显”或 “Headset” 特指一类具备头部佩戴形态、支持沉浸式或透视式交互的计算设备，它们能够将虚拟内容呈现在用户眼前，实现增强现实（AR）或混合现实（MR）体验。这包括：
* **光学透视型头显 (Optical See-Through, OST)**：通过半透明镜片直接观看现实世界
* **视频透视型头显 (Video See-Through, VST)**：通过摄像头捕捉现实世界并以视频流的形式观看
## 头显的基本工作原理
为了更好地理解 EasyAR 对头显的支持原理，我们首先需要了解头显设备的基本工作流程：
1. **环境感知**：通过内置的多摄像头、深度传感器（如 iToF）和惯性测量单元（IMU）等，实时感知周围环境的几何结构、光照条件和物体表面。
2. **空间计算**：根据传感器数据，通过 SLAM 系统实时跟踪用户头部 6DoF 位姿（位置 + 朝向）。
3. **内容渲染与显示**：将 3D 内容（如模型、特效）根据设备位姿进行渲染，并将渲染结果投射到显示屏上。对于 VR 模式，显示的是纯虚拟画面；对于 AR/MR 模式，虚拟画面会与真实环境（VST 摄像头画面或 OST 透视背景）进行合成。
4. **交互系统**：通过手柄、手势识别、语音或眼球跟踪，接收用户指令并作出响应。
## EasyAR 支持头显的原理
EasyAR不替代头显原生的空间跟踪或渲染管线，而是以**空间计算增强**的角色与其协同工作。作为专业的 AR 算法引擎，提供多种 AR 场景的空间感知和计算能力，与设备原有的系统进行高效协同。
|职责范围|角色分工|
|头部 6DOF 跟踪、显示渲染、基础交互等|头显原生 SDK/运行时|
|图像/物体识别与跟踪、大空间定位等高级感知能力|EasyAR SDK|
EasyAR SDK 提供图像/物体识别、稀疏重建、稠密重建、大空间定位等世界感知的核心 AR 功能，负责“看懂”世界，并告诉头显的应用程序虚拟内容应该放在哪里。
EasyAR SDK 作为插件或库集成到头显的应用开发框架中（通常是 Unity或 Unreal）。它接收来自设备系统的原始数据流，进行处理和计算，然后输出一个相对于设备空间坐标系的位姿矩阵，最终由头显引擎的渲染管线将虚拟物体绘制在正确的位置。
## 支持情况与实现方式
EasyAR 对主流的头显开发平台提供了全面的支持，主要通过以下两种方式实现：
* **通过 Unity/Unreal Engine**：这是最主流和推荐的方式。头显厂商通常会提供专门的 Unity/Unreal 插件或 XR SDK。EasyAR 可以无缝接入厂商的 SDK 中使用。
* **通过原生平台 (Native)**：对于需要极致性能或特定原生开发的场景，可以使用 EasyAR 的 C++/Java/Objective-C 原生接口。这通常需要开发者自行处理与设备底层数据的接口对接。
EasyAR 已经在多个主流头显平台上通过 Unity 的方式进行了测试和验证。目前已经确认支持的设备如下：
|头显设备型号|系统/SDK 版本要求|
|Apple Vision Pro|visionOS 2 或更新版本|
|PICO 4 Ultra Enterprise|PICO Unity Integration SDK 3.1.0 或更新版本|
|Rokid AR Studio|Rokid Unity OpenXR Plugin 3.0.3 或更新版本|
|XREAL Air2 Ultra|XREAL SDK 3.1 或更新版本|
|Xrany X1|Xrany元霓 SDK|
> **注意**
Rokid AR Studio 可通过 Rokid Unity OpenXR Plugin 支持 Rokid UXR 3，但建议使用 XR Interaction Toolkit，尤其是跨设备使用。
> **重要事项**
Apple Vision Pro、PICO、XREAL 都需要其对应的企业授权才能使用，如有疑问请联系商务。
* 受 Apple Vision Pro 接口授权限制，仅支持获取了 Apple 企业 API 许可的设备。
* 受 PICO 接口授权限制，仅支持 PICO 企业版设备。
* 受 XREAL 接口授权限制，仅支持获取了企业授权的设备。
对于上述没有提及的其他厂商的头显设备，EasyAR 提供了自定义相机等的扩展接入方式。具体可以参考 [创建EasyAR头显扩展包](../unity/headsets/extension.html) 来进行接入，您可以自行完成对接。
这通常涉及以下步骤：
1. **获取设备开发权限**：申请目标头显的开发者账号和 SDK 文档。
2. **获取传感器数据流**：从设备 SDK 中获取摄像头图像（视频帧）、相机参数等必要数据。
3. **调用 EasyAR API**：使用 EasyAR 的底层 API，将获取到的传感器数据送入 EasyAR `FrameSource` 进行处理。
4. **获取并应用计算结果**：从 EasyAR 引擎中获取计算结果（相机位姿），并将其应用到您的 3D 渲染引擎中。
我们提供了详细的开发指南和示例代码，以帮助您完成这一过程。如果您在对接过程中遇到问题，欢迎在我们的开发者社区寻求技术支持。
## 可供使用的核心功能
在头显设备上，您可以充分利用 EasyAR 的全功能矩阵来构建丰富的空间应用：
* **平面图像跟踪**：识别并跟踪预设的图片，将动态视频或 3D 模型叠加在图片之上。
* **3D物体跟踪**：识别并跟踪预设的 3D 模型（如玩具、产品包装盒），并让虚拟内容与之互动。
* **稀疏空间地图**：扫描周围环境生成三维视觉地图，并提供视觉定位与跟踪功能。生成的地图可以保存或在多个设备间实时共享。
* **稠密空间地图**：扫描并生成周围环境的稠密点云地图和网格模型（Mesh），实现虚拟物体与真实物体的物理遮挡关系，极大地增强沉浸感。
* **云端图像识别**：连接 EasyAR 云端数据库，实现海量图片的识别与管理，适用于展览、教育等场景。
* **Mega 大空间定位**：城市级空间计算方案，连接 EasyAR 云定位服务，实现稳定、快速、精准的定位与跟踪，极大的突破和扩展 AR 体验的范围。
## 平台专用指南
为了帮助您快速上手特定平台，我们准备了详细的多平台集成指南。请点击下方的标签页，查看对应平台的快速入门教程。
* [简介](../unity/headsets/headsets.html)
* [使用头显样例](../unity/headsets/samples.html)
* [启用头显支持](../unity/headsets/enable-headset.html)
* 工程配置
* [Apple Vision Pro工程配置](../unity/headsets/setup-visionpro.html)
* [XREAL工程配置](../unity/headsets/setup-xreal.html)
* [其它Android设备工程配置](../unity/fundamentals/setup-player.html)
* 创建 EasyAR 头显扩展包
* [简介](../unity/headsets/extension.html)
* [为 EasyAR Sense Unity Plugin 写头显扩展](../unity/headsets/extension-imp.html)
* [运行验证（bring-up）头显扩展](../unity/headsets/extension-bring-up.html)
* [发布你的扩展包](../unity/headsets/extension-dist.html)

---

## 设备与平台支持
- 章节路径: `image-tracking/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/image-tracking/devices.html

# 设备与平台支持
本篇详细说明平面图像跟踪功能所支持的设备、操作系统、硬件要求，以及该功能同运动跟踪、自定义相机相结合使用时的相关支持情况，帮助开发者评估项目可行性并提前准备软硬件环境。
## 支持的设备和平台
EasyAR Sense 作为跨平台 AR SDK，为平面图像跟踪功能提供了广泛的操作系统和硬件支持。
### 操作系统与版本要求
|设备类型|操作系统版本|备注|
|PC|• Windows 7 及以上
• macOS Catalina 10.15 及以上|N/KN 版 Windows 需安装 Media Feature Pack 以使用相机|
|手机/平板|• Android 5.0 及以上
• iOS 12.0 及以上|包括 HarmonyOS 1.x-4.x|
|XR 头显|• Android
• visionOS 2.0 及以上|详细支持设备及系统要求参考：[头显支持](../headsets/headsets.html#supportlist)|
### CPU 架构支持
|操作系统|支持的 CPU 架构|
|Windows|x86, x86\_64|
|macOS|x86\_64, arm64 (Apple Silicon)|
|Android|armv7a, arm64-v8a|
|iOS|arm64|
### 硬件要求
平面图像跟踪功能**必需相机**，无额外传感器要求。相比其他 AR 功能（如 [表面跟踪](../surface-tracking/intro.html)），该功能对硬件依赖较低，适用于几乎所有设备。
### 兼容性说明
* **Android/iOS 未来版本**
EasyAR Sense 不依赖大量系统 API，因此新发布的 Android/iOS 版本一般可立即支持。
* **64 位架构要求**
自 2019 年起，Google Play Store 要求新提交应用需支持 64 位；中国主流应用商店也已强制执行。EasyAR 同时提供 `armv7a` 和 `arm64-v8a` 的二进制文件。
## 运动融合的设备支持
运动融合（Motion Fusion）指将平面图像跟踪与设备运动跟踪功能相结合，以提升跟踪稳定性或实现更复杂的 AR 交互。虽然平面图像跟踪本身不强制要求运动传感器，但若需启用运动融合功能，需满足以下条件：
### 运动融合硬件要求
* **必需传感器**：加速度计和陀螺仪
* **适用场景**：当目标图像从当前相机视野之中离开之时，利用设备运动数据维持虚拟物体的位姿持续性以保持稳定、连续跟踪
### 平台支持
* **iOS**: 支持 ARKit 的设备。
* **Android**: 支持 ARCore/AR Engine/EasyAR Motion Tracker 的设备。
* **Windows/macOS**: 通常无内置传感器，需外接设备或放弃运动融合。
> **提示**
对于 EasyAR 支持的 [XR 头显设备](../headsets/headsets.html#supportlist)，运动融合功能天然支持。
### 注意事项
* 平面图像跟踪与运动融合可独立使用。若仅需图像识别，无需额外传感器。
* 运动融合的具体机型列表和性能要求，请参考：[运动跟踪支持机型](../motion-tracking/devices.html)。
## 自定义相机的支持
在某些特殊场景下（如特定分辨率/帧率需求、外部视频流接入），开发者可能需要自定义相机。EasyAR 平面图像跟踪功能支持与自定义相机结合使用。
您可以参考 [自定义相机](../cameras/custom-camera.html) 中的内容建立对自定义相机的认识。目前，我们支持在 Unity 和 原生平台进行自定义相机的集成。
### 实现方式与注意事项
针对不同的平台，我们提供了相应的专题页面。
* [Unity 中的自定义相机实现](../unity/cameras/external-frame-source.html)
* [创建图像输入扩展](../unity/cameras/external-image-stream-frame-source.html)
* [创建图像和设备运动数据输入扩展](../unity/cameras/external-device-frame-source.html)
使用自定义相机时，时刻关注以下**关键限制**：
* 自定义相机需确保帧格式（如 YUV/RGB）与 EasyAR 输入要求匹配。
* 会增加开发复杂度，且可能影响性能，建议仅在标准方案无法满足时使用。
* 需自行处理相机权限、生命周期管理和帧同步。
## 最佳实践建议
平面图像跟踪功能对硬件和平台的要求相对宽松，仅需相机即可运行，适合大多数移动设备和桌面系统。开发者需关注 Android 64位打包规范，并在需要运动融合时检查设备支持情况。自定义相机虽可行，但仅建议在标准方案无法满足需求时采用。

---

## 平面图像跟踪简介
- 章节路径: `image-tracking/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/image-tracking/intro.html

# 平面图像跟踪简介
平面图像跟踪（Planar Image Tracking）用于检测与跟踪日常生活中有纹理的平面物体。所谓“平面”的物体，可以是一本书、一张名片或一幅海报这样的小物体，也可以是一面涂鸦墙这样的大型目标。这类物品或事物具有平坦表面、丰富且不重复的纹理。
本篇将概述平面图像检测与跟踪的基本原理、预期效果及平台适配方案，帮助您快速理解功能边界与开发要点。
## 基本原理
理解这些原理有助于开发者优化识别效果并规避常见问题。
### 核心流程
1. **加载预处理阶段**：
* 系统加载目标图像，从中提取大量视觉特征点，生成该图像的特征描述并插入到特征库中。
* 纹理越丰富的图像越容易识别与跟踪，您可以借助 [目标图检测工具](https://www.easyar.cn/targetcode.html) 提前检查您的目标图像的可识别度。
![](https://doc-asset.easyar.com/develop/image-tracking/media/rate-sample.png)
>
> 参考图左：纹理丰富易识别（5 星）；参考图右：元素简单、缺少纹理，不易识别（1星）。
> 我们推荐达到 4~5 星质量的图像作为您的目标图像。
>
* **实时检测跟踪阶段**：
* 相机捕获画面后，系统会分析当前画面的特征点，与目标图像的特征库进行特征匹配。
* 通过 PnP（Perspective-n-Point）算法计算图像在 3D 空间中的位姿（位置+旋转）。
* 一旦目标检测成功，系统就会进入跟踪模式。此时系统会对比连续帧的画面并分析帧与帧之间的运动，从而实现实时的跟踪过程。
* **优化机制**：
* **跟踪丢失恢复**：短暂遮挡或快速运动模糊后，系统自动重新检测目标。
* **多目标同时跟踪**：通过 `Simultaneous Number` 参数控制单个 Tracker 的并发数量，实现一个 Tracker 调用就可以同时跟踪多个目标。
### 技术限制
* 仅支持**平面图像**（非 3D 物体或动态内容）。
* 依赖环境光照，过暗或过曝会导致检测困难或跟踪易丢失。
* 检测时相机不能距离目标过远，保证画面中目标图像在画面中的比例至少有 30%。
* 多目标跟踪受限于设备性能，通常 PC 端可以同时跟踪 10 个以上目标，移动端可以同时跟踪 4\~6 个平面目标。
## 效果与预期结果
理解了图像检测与跟踪的工作机制与技术限制之后，您还需要对该功能所能达到的效果有个了解。明确这些效果有助于您在开发过程中设定合理的测试标准。
### 理想效果
* **精准叠加**：虚拟物体与图像边缘对齐。
* **快速检测**：从应用加载到检测成功超低延迟。
* **稳定跟踪**：图像旋转、移动、部分遮挡下仍可维持跟踪。
### 不理想情况与应对
|现象|原因|用户感知|解决方案预览（详见后续章节）|
|**无法识别**|图像纹理不足、过小|虚拟物体不出现|优化目标图像，使用工具检测可识别度|
|**跟踪抖动**|目标画面占比过小，可跟踪点不足|虚拟物体晃动明显|避免过于远离目标图像，跟踪模式设定 `PreferQuality`|
|**频繁丢失**|图像快速移动或完全遮挡|虚拟物体闪烁/消失|稳定移动设备/目标图像，或增大目标尺寸|
|**多图目标缺失**|受硬件性能影响|部分目标图像无法跟踪|权衡运行性能设定合理的 `Simultaneous Number` 参数|
### 预期结果验证方法
* **开发阶段**：使用 PC 摄像头通过 Unity 编辑器 Play 模式预览。
* **测试阶段**：使用官方 Sample 场景或自建测试图像，覆盖不同光照/角度/距离条件。
## 目标图像最佳实践
平面图像跟踪的效果非常依赖于目标图像的质量。为了保证识别成功率，建议在准备目标图像时遵循以下准则。
根据使用场景不同，您可以通过多种方式准备目标图像：直接用相机正视角度拍摄目标物体，或先设计图案再打印生产。无论是照片还是设计稿，都可作为模板图片。
### 基础要求
* **图像格式**：建议为 JPG 或 PNG。
* **透明通道处理**：如果图像带有透明通道，系统会按白色背景处理。若非预期效果，请避免使用透明通道。
### 核心优化点
1. **确保丰富的纹理细节**
模板图片应具有足够的细节和边缘变化，避免纯色或简单图形。
![](https://doc-asset.easyar.com/develop/image-tracking/media/texture-sample.png)
>
> 参考图左：纹理丰富的图像可被检测；参考图右：纯色图像无法检测
>
2. **避免重复性模式**
遵循重复规律的图案（如棋盘格、条纹）会降低特征点的唯一性。
![](https://doc-asset.easyar.com/develop/image-tracking/media/repeat-pattern.jpg)
>
> 参考图：重复模式图像无法被跟踪
>
3. **内容充满画面**
主体应尽可能占据整个画面，减少空白区域。
![](https://doc-asset.easyar.com/develop/image-tracking/media/size-sample.jpg)
>
> 参考图：左侧主体饱满的图像比右侧留白过多的图像更容易检测和跟踪
>
4. **控制长宽比例**
图像不宜过于狭长，短边长度至少应达到长边的 20%。
![](https://doc-asset.easyar.com/develop/image-tracking/media/too-narrow.png)
>
> 参考图：狭长图像难以跟踪
>
5. **选择合适的分辨率**
**推荐范围**：SQCIF(128×96) 到 QVGA(1280×960) 之间。
**过小**：特征点不足，识别率下降。
**过大**：生成 Target 数据时带来不必要的内存开销增长、计算时间增多。

---

## 平面跟踪与运动跟踪结合
- 章节路径: `image-tracking/motion-fusion.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/image-tracking/motion-fusion.html

# 平面跟踪与运动跟踪结合
本篇介绍如何将平面图像跟踪与设备运动跟踪功能相融合，以提升复杂场景下的跟踪稳定性和用户体验。内容包括核心原理、预期效果及潜在问题分析。
## 基本原理
**运动融合（Motion Fusion）** 结合平面图像跟踪的位姿数据和设备运动跟踪的位姿数据，实现更鲁棒的位姿估计。以下是其核心流程：
### 数据同步与互补
* **视觉跟踪**：通过图像特征点匹配计算当前帧的位姿（位置+旋转），但易受遮挡、模糊或快速移动影响。
* **运动跟踪**：利用 IMU 传感器高频输出以及视觉图像的输出获得设备运动数据，但存在累积飘移误差。
* **融合机制**：
* 将视觉跟踪的位姿与设备运动跟踪的位姿进行坐标系对齐。
* 当目标图像清晰可见、稳定运动时：以视觉跟踪为主。不断地将视觉跟踪位姿送入融合模块进行修正，以减少整个系统的累积漂移。
* 当目标图像丢失或者在画面中占比过小、快速运动时：此时视觉跟踪失效，以运动跟踪为主。根据当前的运动跟踪位姿进行融合位姿预测。
### 关键技术点
* **时间戳对齐**：将视觉帧的时间戳与运动跟踪数据对齐，避免因延迟导致抖动。
* **坐标系对齐**：根据视觉跟踪的轨迹和运动跟踪的轨迹进行坐标系对齐。
* **重定位**：图像重新出现时，视觉跟踪接管快速校正可能的累积误差，将虚拟物体“拉回”正确位置。
### 适用场景与限制
运动融合并不适合所有场景下的使用。有以下情形之一的将 **不适用** 运动融合功能：
* 目标设备不支持 ARCore/ARKit 等运动跟踪功能。详细的设备支持列表参考：[运动跟踪设备支持](../motion-tracking/devices.html)。
* 目标图像/平面物体在场景中是动态的，例如拿在手上体验的卡片。
除此之外的场景，使用运动融合将极大的提升平面图像跟踪的用户体验，包括但不限于以下使用情景：
* **快速运动**：用户手持设备快速移动，运动模糊会导致图像跟踪失效。
* **目标消失**：画面离开目标本身或者目标被动态物体（如行人）遮挡时，依然保持整个场景里虚拟内容的呈现。
* **远离目标**：用户手持设备远离导致目标图像在画面中占比过小，依然稳定持续跟踪。
* **低光照条件**：视觉跟踪性能下降，需要维持体验。
## 效果与预期结果
在场景适用的前提下，使用运动融合将比单纯的使用平面图像跟踪带来更稳定、平滑的用户体验。
### 理想效果
* **更稳定的跟踪**：虚拟物体不抖动、不跳变。
* **平滑过渡**：视觉跟踪失效时，融合位姿的变化连续自然。
* **抗干扰能力**：目标图像丢失或被遮挡、设备快速运动等情形下，虚拟物体仍能跟随设备运动持续跟踪。
### 不理想情况与应对
|现象|原因|用户感知|解决方案|
|**初始未生效**|运动跟踪需要一定时间进行初始化|在初始阶段出现内容消失|一定的 UI 提示，确保系统运动跟踪初始化完成|
|**飘移明显**|系统误差累积，且长时间无视觉校正|虚拟物体偏离原位置|引导用户缩短遮挡时间，或增加视觉重定位的提示|
|**性能下降**|长时间同时运行两个功能|帧率下降画面卡顿|正常现象，可通过接口关闭运动融合|
### 预期结果验证方法
使用支持的设备在真实场景中测试：
1. 对准图像，确认虚拟物体稳定。
2. 用手遮挡图像2秒并移动设备，观察虚拟物体是否平滑移动。
3. 移开手，确认虚拟物体快速回正且无跳变。
## 总结与最佳实践
运动融合显著提升了平面图像跟踪在许多场景下的鲁棒性，但需要设备的硬件支持且性能足够。开发者应根据目标用户设备选择性启用该功能，并在低性能设备上提供降级方案。
实时打开/关闭运动融合功能的 API 参考：
* 原生： [setResultPostProcessing](../../api/native/easyar.ImageTracker.html#n_easyar_ImageTracker_setResultPostProcessing)
* Unity：[EnableMotionFusion](../../api/unity/easyar.ImageTrackerFrameFilter.html#u_easyar_ImageTrackerFrameFilter_EnableMotionFusion)

---

## EasyAR Sense 许可证
- 章节路径: `license-sense.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/license-sense.html

# EasyAR Sense 许可证
使用 EasyAR Sense 提供的功能前，需要先获取许可证。
## 能力支持
|能力|个人版|专业版|经典版|XR License 试用版|XR License 正式版|
|平面图像跟踪|支持|支持|支持|支持|支持|
|3D物体跟踪|支持|支持|支持|支持|支持|
|表面跟踪|支持|支持|支持|支持|支持|
|云识别|支持|支持|支持|支持|支持|
|稀疏空间地图|支持|支持|支持|支持|支持|
|稠密空间地图|支持|支持|支持|支持|支持|
|运动跟踪|支持|支持|支持|支持|支持|
|Mega 大空间定位|支持|支持|支持|支持|支持|
|多目标识别与跟踪|支持|支持|支持|支持|支持|
|不同类型目标同时识别与跟踪|支持|支持|支持|支持|支持|
|自定义相机功能|受限支持|完整支持|完整支持|受限支持|完整支持|
|Unity AR Foundation 集成|受限支持|完整支持|完整支持|受限支持|完整支持|
|华为 AR Engine 集成|受限支持|完整支持|完整支持|受限支持|完整支持|
## 许可证类型比较
||个人版|专业版|经典版|XR License 试用版|XR 正式版|
|是否可以商用|不支持|支持|支持|不支持|支持|
|有效期限|永久|按月订阅|永久|永久|永久|
|水印|有|无|无|无|无|
|是否支持升级|支持升级到最新版|支持升级到最新版|支持升级到最新版|支持升级到最新版|支持升级到最新版|
> **注意**
使用个人版运行时会显示水印（使用自定义相机和头显时除外）。
使用 XR License 试用版时会显示水印（使用自定义相机和头显时除外），支持主流 XR 设备。
头显和眼镜上 **仅支持使用** XR License 试用版 或 XR 正式版。
在自定义相机或头显上使用试用产品（个人版 license、XR License 试用版或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
## 相关主题
* [EasyAR 增强现实入门](getting-started/ar.html)
* [EasyAR 的头显支持](headsets/headsets.html)

---

## 诊断与修复：应用中内容跳动和飘移的问题
- 章节路径: `mega/content-drift.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/content-drift.html

# 诊断与修复：应用中内容跳动和飘移的问题
“虚拟内容在飘”、“物体在抖动”、“位置不稳定”——这些都是开发者在 AR 应用中经常遇到的问题。内容不稳定会极大地破坏沉浸感，甚至导致用户体验不佳。
本篇将帮助您理解内容跳动和飘移的原因，并提供一套系统的排查和优化方法。
## 区分“正常抖动”与“异常飘移”
首先，我们需要建立一个合理的心理预期。在移动设备上实现高精度的 AR 跟踪，本身就充满挑战。以下情况属于**正常范围**，无法完全消除，但可以优化：
* **微小的高频抖动 (Jitter)**：
* **表现**：虚拟物体有毫米级的、细微的晃动。
* **原因**：这是由设备传感器的物理噪声、视觉跟踪算法的精度极限以及人手持设备的细微抖动共同导致的。
* **举例**：在近距离观察时（例如，将虚拟物体放在桌面上并凑近看），这种细微的抖动是正常的。
* **短暂的飘移 (Drift)**：
* **表现**：当用户快速移动或旋转设备时，虚拟物体在短暂的时间内（0.5-1秒）出现位置偏差，然后恢复。
* **原因**：设备的 SLAM 系统在快速运动时，其 IMU（惯性测量单元）的累积误差和视觉定位的延迟会导致短暂的位置飘移。
* **举例**：在动态场景中，这是可以接受的。如果物体能快速“拉回”正确位置，说明系统是有效的。
而以下情况则属于**异常问题**，需要排查和修复：
* **持续的、大幅度的位置飘移**：虚拟物体缓慢地、持续地偏离其本应在的位置，且不会恢复或过很久才恢复。
* **剧烈的跳动或闪烁**：虚拟物体在屏幕上大幅度跳动，或者时隐时现。
* **与真实物体的相对位置不一致**：虚拟物体无法稳定地“钉”在真实物体上。
> **注意**
此外，还有一个关键点需要注意：
对于使用 0DoF、3DoF 或 5DoF 模式运行的设备，其“贴合感”和“真实感”天生就弱于 6DoF 设备。当用户快速移动、转弯或上下楼梯时，虚拟物体无法完美跟随。
因此，在这些模式下出现内容“浮在空中”或“位置偏移”等现象，属于设备能力的根本限制，而非本篇所讨论的“内容跳动或飘移”故障。
关于不同 xDoF 模式的体验区别，请参考 [导航最佳实践](navigation.html#howto) 中的介绍。
## 系统性排查流程
请按照以下顺序进行排查，从最可能的原因入手。
### **步骤一：外部环境与硬件因素（无需修改代码）**
1. **物理环境检查**：
* **纹理丰富度**
您所在的测试环境是否过于单调？大面积的纯白墙、光滑地板、玻璃表面都会让视觉定位出现失败或错误。
* **动态物体**
环境中是否有大量移动的物体（如人群、行驶的车辆）？动态物体会干扰视觉定位，但这种问题往往是**短暂**的。
* **场景混淆**
环境中是否存在极易混淆的场景（如不同入口处的电梯口）？视觉相似的区域会影响定位，可能导致定位结果在相似的区域间来回跳动。这类问题可以通过预先设置合适的先验信息进行规避。
* **设备硬件检查**：
* **设备发热**
长时间运行后，设备是否严重发热？过热会导致 CPU/GPU 降频，影响设备本身 SLAM 系统的跟踪性能，是导致持续飘移最常见的原因。
* **设备性能**
部分老旧设备上受限于硬件的性能和器件精度，更容易出现尺度飘移，导致虚拟内容也跟着飘移。您可以尝试更换设备进行对比测试，帮助您判断问题是否是由设备本身限制导致。
### **步骤二：地图与定位质量分析（使用外部工具）**
1. **使用 Mega Toolbox**：
* 在相同位置运行 Mega Toolbox，观察其定位的稳定性。
* **如果 Toolbox 定位也飘移/跳动**：问题出在**地图本身**或**当前环境不适合定位**。
* **如果 Toolbox 定位稳定**：问题出在**您的应用**中。请继续步骤三。
* **使用 PC 模拟运行 EIF 数据**：
* 回放您在现场录制的 EIF 数据。
* **如果回放也飘移/跳动**：说明**场景本身不适合定位**，或**地图本身**存在问题，或录制 EIF 的设备本身的运动跟踪存在尺度飘移。
* **如果回放稳定**：说明场景本身是定位友好的，问题可能出在**您的应用**在实时运行时的设备发热、降频等因素之上。
### **步骤三：应用内部逻辑检查**
1. **姿态更新**：
* 您是否对姿态数据进行了不必要的额外平滑处理（如过度的 `Lerp` 或 `SmoothDamp`），这反而会导致延迟和飘移感。
* **通常情况下，直接使用 Mega 返回的原始 Pose 是最稳定的。**
* **坐标系匹配**：
* 确认您的虚拟物体、场景相机和 `MegaTracker` 等的节点关系正确，且没有修改过 `MegaBlocks` 下各节点本身的 `local transform` 的数值。
* 节点设置错误会导致不正确的坐标系转换，使得内容渲染出现无法预知的行为。
## 特别提醒：OST 头显设备的视觉叠加问题
在完成对定位和渲染逻辑的排查后，如果您使用的是 OST (光透视) 头显设备，还需要考虑一类特殊情况。
即便设备本身具备了良好的 6DoF 运动跟踪能力，有时仍会遇到虚拟物体与物理空间叠加的“贴合感”不佳的问题。这通常不是 Mega 定位服务的故障，而是由 OST 设备的光学原理导致的固有现象，例如光学对齐误差或人眼标定差异。
关于这类问题的详细解释和判断方法，可以参考 [OST 设备特殊说明](../diagnostics/recordings-headsets.html#ost-visual-issue) 中的介绍。
## 总结与最佳实践
经过前面的排查，您应该已经定位了导致内容跳动或飘移的根本原因。为了方便您快速回顾和采取行动，我们将常见的问题现象、可能原因和最佳实践总结在下表中。根据您的排查结果，在下表中找到对应的解决方案。
|问题类型|可能原因|最佳实践|
|**微小抖动**|传感器噪声、算法极限|此类微小抖动为正常现象，一般无需过多关注|
|**快速移动后飘移**|SLAM 延迟、算法校正|可引导用户平稳移动设备。如无法快速恢复，则需额外关注|
|**持续大范围飘移**|SLAM 故障、设备差异|可更换设备进行交叉验证|
|**剧烈跳动/闪烁**|混淆场景、定位不友好|可设置辅助先验信息，或引导用户|
|**与真实物体相对位置不一致**|定位/地图误差、代码逻辑错误|多视角测试并观察虚拟物体的位置，修复可能的代码错误|
如果经过以上排查和修复您的问题依然存在，请结合录屏、EIF 数据录制和详细日志等，通过 **[问题报告](report.html)** 的方式向我们提交详细报告。

---

## 诊断与修复：应用中内容不显示的问题
- 章节路径: `mega/content-nodisplay.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/content-nodisplay.html

# 诊断与修复：应用中内容不显示的问题
“我能看到真实世界，但虚拟内容没有出现。” 这是 AR 开发中最常见的问题之一。这个问题可能源于多个环节，从 Mega 定位本身到您的渲染逻辑都有可能。
本篇将引导您系统地排查和解决这个问题。
## 排查流程：从外部到内部
遵循“先外部，后内部”的原则，可以高效地定位问题。请按顺序执行以下步骤：
### **步骤一：使用外部工具验证 Mega 定位状态 (无需修改代码)**
在深入您的应用代码之前，首先确认 Mega 定位服务本身是否正常工作。这是最关键的一步，可以帮您判断问题是出在 Mega 定位本身还是渲染等应用开发集成问题。
1. **使用 Mega Toolbox (手机端)**
* 在您的测试手机上安装 **Mega Toolbox App** (如果尚未安装)。
* 打开 App，进入“现场定位测试”或类似功能。
* 登录您的账号并选择与您应用相同的定位库。
* 将手机带到您应用测试时无法显示内容的**相同位置**。
* **观察结果**：
* **如果 Toolbox 定位成功**（界面上状态显示 `Found`）：恭喜！ Mega 定位服务是正常的。问题出在**您的应用内部**，特别是渲染和内容显示逻辑上。请跳转到 **步骤二**。
* **如果 Toolbox 定位失败**（界面上状态显示 `NotFound` 或其他）：问题出在**定位服务本身**。请参考 [**下一节**](#troubleshooting) 进行深入分析。
* **使用 PC 端模拟运行 (如果已采集 EIF)**
* 如果您已经为该场景录制了 **EIF 数据**，可在 PC 端的 Unity 编辑器中使用 `session` 验证工具回放该数据。
* **观察结果**：
* **如果回放时定位成功**（界面上状态显示 `Found`）：问题出在您的**应用代码或设备特定环境**上。
* **如果回放时定位失败**（界面上状态显示 `NotFound` 或其他）：问题出在**定位服务本身**。请参考 [**下一节**](#troubleshooting) 进行深入分析。
### **步骤二：检查应用内部的渲染与内容逻辑**
如果步骤一确认 Mega 定位服务本身是正常的，那么问题就出在您的应用代码中。请检查以下几点：
1. **内容是否摆在正确的节点之下**：
* 您是否正确将 3D 物体摆放在工具自动生成的 `MegaBlocks` > `Block\_\*` 节点之下？
* 检查内容与 Block 节点的层级关系，以确保在运行时虚拟内容的渲染位置是正确的。
* **MegaTracker 的 Block Root 是否正确设置**：
* 展开 `AR Session`，检查 `Mega Tracker` 中的 `Block Root` 是否为工具生成的 `MegaBlocks` 节点。
* **MegaBlocks 节点是否有改动**：
* 确保没有修改 `Block\_\*` 节点的名字，且没有修改 `local transform` 属性中的任何数值。
* **事件监听是否正确**：
* 您是否修改过 `MegaTracker` 的定位回调处理逻辑？
* 您的代码是否在定位状态成功事件触发后，才执行了实例化或显示虚拟内容的操作？
* **头显渲染与透明度**：
* 您的虚拟物体是否被其他物体遮挡？检查渲染队列和 Shader。
* 如果使用了 VST (视频透视) 设备，检查您的渲染是否被正确地叠加在了视频流之上。
* 如果使用了 OST (光透视) 设备，检查内容是否因为环境光过强而看不清。
* **内容本身的问题**：
* 您实例化的预制体（Prefab）本身是否有问题？例如，模型文件丢失、Shader 错误、缩放为 0 等。尝试在场景中手动放置一个相同的物体，看它是否能正常显示。
## 常见定位失败原因分析与改善建议
如果在 **步骤一** 中发现 Mega Toolbox 也无法定位，那么需仔细查看并解决定位问题。以下是常见原因和对策：
* **原因一：地图与环境不匹配**
现场环境与采集建图时相比已经发生了巨大变化，或者体验的区域在采集时未能覆盖，或地图本身就是错误的。
**改善建议**：
* 确保您定位库中加载的地图与当前物理空间在场景上是一致的。
* 如果环境已改造（如装修、更换陈列），需要重新采集和生成地图。
* 如果采集建图时未覆盖发生问题的区域，需要通过补充更新的方式重新生成地图。
* **原因二：初始化环境不佳**
在纹理稀少的区域（如纯色墙壁、对着地面）启动应用。
**改善建议**：
* 引导用户在纹理丰富的区域启动应用，以帮助系统快速完成初始定位。
* 在应用 UI 中给出明确的提示，如“抬起手机环视左右”。
* **原因三：网络或服务问题**
网络延时导致定位服务请求超时，或者定位服务本身出现了故障、或超出了并发使用上限等。对于后者请及时与我们反馈。
* **原因四：到达算法能力边界**
Mega 定位基于先进的计算机视觉、AI 等算法，但其并不是万能的，存在一定的算法能力边界。当在某些场景或点位出现定位持续失败时，可通过录屏、录制 EIF 数据等方式与我们进行反馈，帮助我们持续改进和迭代算法。
另外，需要特别说明的是，Mega 定位需要一个过程，通常在 1-2 秒左右。考虑到现实场景的复杂性如网络拥堵、高并发、手机发热降频等情形，该时间可能会更久。因此，在应用中可以设计一个清晰的加载/等待界面，告知用户“正在定位中...”，避免用户因等待而误以为服务挂了或定位不到。
> **注意**
* 首次定位通常比后续定位慢，因为系统在初次定位成功后需要加载相应的内容。这是正常现象。
* 快速移动设备会可能导致定位丢失。请引导用户平稳移动设备。
## 总结与最佳实践
* **始终使用外部工具先行验证**：这能最快地将问题范围缩小到“定位”或“渲染”。
* **建立合理的用户预期**：通过 UI 提示，让用户知道定位需要时间，并引导他们到合适的环境。
* **关注内容逻辑**：确保您的内容绑定等设置正确。
* **善用日志**：在关键节点（如事件触发、姿态获取、响应状态）打印日志，可以帮助您快速定位代码逻辑问题。
通过以上系统性的排查，您应该能够解决绝大多数“内容不显示”的问题。如果问题依然存在，请准备好 EIF 数据和日志，通过 **[问题报告](report.html)** 的方式向我们提交详细报告。

---

## 支持的设备和平台应用
- 章节路径: `mega/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/devices.html

# 支持的设备和平台应用
EasyAR Mega 旨在提供跨平台的、一致的空间计算体验。为了实现这一目标，我们对不同的设备和平台提供了专门的支持。本章将详细说明 Mega 可以在哪些设备和平台上运行，以及不同设备所能提供的体验区别。
## 设备、平台支持概览
Mega 云定位具备广泛的接入能力，支持各类能获取摄像头图像的设备和平台。支持的情况如下：
|设备类型|操作系统|目标平台|支持情况|
|智能手机/平板|• iOS
• iPadOS
• Android|• Native
• Unity
• 微信小程序|全面支持，几乎覆盖市面所有智能手机/平板|
|XR 头显|• visionOS
• Android XR|• Unity|有限支持，参考 [头显支持](../headsets/headsets.html) 查看具体的设备支持情况|
|PC|• Windows
• macOS|• Native
• Unity|有限支持，仅用于模拟效果预览，参考 [EIF 模拟运行](../../mega/simulation-verification/simulation.html)|
|自定义设备|• Android|• Native
• Unity|有限支持，需要使用 [自定义相机](../cameras/custom-camera.html) 功能，适合深度开发者|
## 不同设备上的体验差异
虽然 Mega 云定位功能广泛支持运行于不同的平台的各种设备，但最终的用户体验还依赖云端定位结果在客户端进行融合跟踪的效果。
根据具体设备与平台的硬件条件及软件能力，我们对不同设备按照 xDoF (x Degrees of Freedom，x 自由度) 的方式进行分类。xDoF 是衡量设备融合跟踪能力的关键指标，它直接影响 Mega 的体验质量。
|设备分类|硬件要求|软件要求|体验等级|
|0DoF|除摄像头外无硬性要求|• 无|**基础**，无终端跟踪能力，虚拟内容只能贴屏显示|
|3DoF|需要有陀螺仪|• EasyAR Sense 4.7.0 及以上|**一般**，受限的终端跟踪能力，体验受到行进方向和速度影响|
|5DoF|需要有陀螺仪和加速度计|• Android 7.0 及以上
• EasyAR Sense 4.7.0 (Lib Full)|**次佳**，一定的终端跟踪能力，但在高度方向上的体验会打折|
|6DoF|需要有良好的 IMU 传感器|支持以下任意：
• Apple ARKit
• Google ARCore
• Huawei AR Engine
• EasyAR Motion Tracker
|**最佳**，完整的终端融合跟踪能力，可以应对用户的各种运动模式|
> **注意**
对于 Apple 设备，是否支持 ARKit 请参考：[ARKit 验证设备支持](https://developer.apple.com/cn/documentation/arkit/verifying_device_support_and_user_permission/)。
对于 Android 设备，是否支持 ARCore 请参考：[支持 ARCore 的设备](https://developers.google.cn/ar/devices)。
对于华为设备，是否支持 AR Engine 请参考：[AR Engine 运动跟踪支持的设备](../motion-tracking/devices-arengine.html)。
对于其他设备，是否支持 EasyAR Motion Tracker 请参考：[EasyAR 运动跟踪支持的设备](../motion-tracking/devices-easyar.html)。
对于 XR 头显设备，目前支持集成 Mega 功能的设备均具备完整的 6DoF 能力。
> **重要事项**
为了保证良好的用户体验，对于使用 EasyAR Motion Tracker 的设备，Mega 功能在运行前会进行自检。具体地，程序会判断 `MotionTrackerCameraDeviceQualityLevel` 的状态：
* ≥ `Limited`：默认 6DoF，可以手动降级成 5DoF、3DoF、0DoF
* < `Limited`：默认 5DoF，可以手动降级成 3DoF、0DoF
相关概念请参考文档：[运动跟踪简介](../motion-tracking/intro.html)。
## 微信小程序的额外说明
在微信小程序内集成 Mega，对设备的要求与原生 或 Unity 开发有所不同。
* 设备需要至少支持 **微信VisionKit V1平面接口** 才能运行。
* 支持 **微信 VisionKit V2 平面接口** 才能获得比较理想的效果。
详细的设备支持列表请参考微信小程序官方文档：[V2平面AR接口支持列表](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)
EasyAR Mega 为主流移动平台提供了开箱即用的支持。在选择目标设备时，请优先考虑支持 ARKit/ARCore/AR Engine/EasyAR Motion Tracker 的机型或特定 XR 头显设备，以确保用户获得最佳的 Mega 空间体验。

---

## Mega 常见问题
- 章节路径: `mega/faq.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/faq.html

# Mega 常见问题
在开发过程中遇到问题是在所难免的。本篇旨在帮助您快速定位并解决常见的问题。我们首先从一个常见问题列表（FAQ）开始，如果您在这里找不到答案，请参考后续章节或向我们提交问题报告。
## 常见问题解答 (FAQ)
以下是一些开发者在集成和使用 EasyAR Mega 时最常遇到的问题及其解决方案。
**Q：为什么我的应用提示 Invalid Key？**
**A**：这通常由以下几个原因导致：
1. **License 无效或过期**
2. **License 与 Bundle ID / Package Name 不匹配**
3. **头显设备需要单独的 XR License**
4. **自定义相机功能需要正式版 License**
**Q：为什么我的应用上有水印？**
**A**：这说明您使用的 License 是试用版而非正式版。
**Q：为什么我的应用上有一行倒计时提示（timeout within \* seconds）？**
**A**：这是试用产品期间的限制，使用正式版本的 EasyAR Sense 授权和正式版 EasyAR Mega 服务可以解决这个问题。
**Q：为什么我的应用打开是黑屏？**
**A**：这种情况通常会在屏幕信息或日志中打出错误原因，您可根据系统打印出的具体原因进行解决。如果无法解决，请反馈技术信息（包括日志、截图、详细的设备信息等）。
**Q：为什么我的应用无法定位，返回状态一直是 NotFound？**
**A**：这通常由以下几个原因导致：
1. **定位服务还在启动过程中**：
此时定位服务尚未完全加载完毕所有 Mega 地图，因此无法保证在某个区域能定位成功。
2. **不在地图覆盖范围内**：
确保您当前所处的物理位置，位于您所加载的 Mega 地图的覆盖区域内。
3. **模拟测试配置错误**：
不在现场运行，但 `MegaLocationInputMode` 错误设置为了 `Onsite`。
4. **环境条件不佳**：
极端的光线（过暗或过亮）、大面积的纯色墙面或地面（如白墙、抛光地板）都会影响视觉定位。
**Q：为什么我的应用无法定位，返回状态异常？**
**A**：这通常由以下几个原因导致：
1. **请求超时**：
此时系统会返回 `RequestTimeout`。
2. **请求间隔过短**：
此时系统会返回 `RequestIntervalTooLow`。
3. **其他异常错误**：
此时系统会返回 `UnknownError`。一般情况此类异常对应了连接或传输过程中的失败，或 Mega 服务本身出现了错误。可以通过 `MegaBlockLocalizationResponse.ErrorMessage` 接口获取详细信息。
**Q：为什么我的小程序申请插件使用失败？**
**A**：这是由于小程序插件不支持在微信开发者工具的“游客模式”下使用，也不支持在主体为个人的小程序上使用。请使用企业主体的微信小程序 AppId 进行申请。
**Q：为什么我的小程序授权未通过？**
**A**：您需要从开发中心获取 Mega 小程序插件许可证，并确保您使用的 AppId 与许可证中的相同。
**Q：为什么我的小程序在 XX 手机上无法使用？**
**A**：在小程序上集成 Mega 依赖微信的 VisionKit 组件，其系统要求以及设备支持列表参考 [微信文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)。
**Q：定位成功了，但虚拟内容的位置看起来有偏差或飘移？**
**A**：涉及定位效果的问题其原因往往比较复杂，可能的原因如下：
1. **建图精度问题**：
该区域的 Mega 地图本身可能存在精度误差。这通常发生在地图采集或重建阶段，请联系商务确认。
2. **初始化时的跳动**：
在定位刚开始的几秒钟，位置可能会有轻微跳动。这是由于设备的 SLAM 系统尚未完成初始化导致，在微信小程序中这个过程尤其明显（部分设备甚至会时间比较长）。
3. **环境动态变化**：
如果物理环境发生了显著变化（如移动了大型布置、增加了临时展板），可能会导致地图与现实不匹配。这种情况需要更新地图。
4. **设备系统误差**：
大多数设备设备在长时间连续运行后，其 SLAM 系统的累积误差会导致飘移。
5. **定位误差问题**：
视觉定位本身存在精度误差，通常这种误差不影响虚拟内容的视觉体验。如果误差大到有明显偏差或飘移，则需要详细的数据才能进行分析和解决。参考 [问题诊断和报告](../diagnostics/diagnostics.html) 中介绍的方法进行数据收集和反馈。
**Q：如何采集和使用 EIF 数据进行调试？**
**A**：EIF 数据是强大的调试工具。请参考以下章节：
* **如何采集**：阅读 [采集模拟运行数据](input-recording.html)，了解如何在手机或头显上录制 EIF 文件。
* **如何回放**：根据您的开发环境（Unity 或微信小程序），参考该章节中对应的回放指南。
## 寻找更具体的帮助
如果以上 FAQ 未能解决您的问题，您可以访问以下专题页面，获取更深入的解决方案：
* **[内容不显示](content-nodisplay.html)** - 专注于内容渲染的疑难杂症。
* **[内容跳动和飘移](content-drift.html)** - 深入分析内容的跳动和飘移。
* **[微信小程序集成已知问题](../wechat/mega/known-issues.html)** - 针对小程序平台的特殊问题汇总。
## 报告一个新问题
如果您遇到了以上未涵盖的、疑似 SDK 或平台本身的问题，请帮助我们改进产品。详细的操作步骤或指引，可参考阅读：[问题报告](report.html)。
**在提交报告前，确保您已准备好以下信息，这将极大地帮助我们解决问题：**
1. **问题描述**：清晰地描述您遇到的问题现象、发生频率和操作步骤。
2. **设备信息**：设备型号、操作系统版本、EasyAR SDK 版本。
3. **EIF 数据**：请务必提供能够复现问题的 **EIF 录制文件**。这是最重要的诊断依据。
4. **日志文件**：应用的完整日志（Logcat 或 Console 输出）。
5. **录屏或截图**：问题发生时的屏幕录像或截图。
请将以上信息通过 **论坛、邮箱或商务** 提交给我们。感谢您的反馈！

---

## 采集模拟运行数据
- 章节路径: `mega/input-recording.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/input-recording.html

# 采集模拟运行数据
在 Mega 应用的开发和调试过程中，直接在真实环境中反复测试不仅耗时，而且可能受限于场地、设备和网络条件。为了解决这个问题，EasyAR 提供了一套强大的模拟运行机制，其核心就是 EIF 数据文件。
本篇将指导您如何采集和回放 EIF 数据，以实现高效的功能验证、问题排查和效果预览。
## 核心概念：什么是 EIF 数据？
在开始之前，强烈建议您先阅读 [EIF 简介](../simulation/simulation.html)，以了解：
* **EIF 文件内容**：它是一个数据容器，不仅包含摄像头视频流，还同步记录了传感器数据、设备姿态、相机参数等。
* **录制与回放机制**：通过在真实环境中录制一次 EIF 文件，您就可以在开发环境中无限次地回放，完美复现当时的场景。
理解 EIF 是 “一次录制，随处回放” 的 “数字副本”，将极大提升您的开发效率。
## 采集 EIF 数据：方法与流程
采集高质量的 EIF 数据是成功模拟的第一步。请遵循 [采集 EIF 数据](../../mega/simulation-verification/recording.html) 中的基本原则，以确保数据的有效性。
根据您的目标设备，采集 EIF 的方法如下：
* 智能手机
工具：通过 Mega Toolbox App 完成。这是一个专为手机设计的辅助应用，简化了录制流程。
参考：详细的操作步骤请查阅 [手机录制 EIF 文件](../../mega/data-collection/simulation/toolbox.html)。
* XR 头显设备
工具：通过 Sample 程序完成。在头显的示例工程中集成了 EIF 录制功能。
参考：详细的操作步骤请查阅 [眼镜录制 EIF 文件](../../mega/data-collection/simulation/headsets.html)。
## 回放 EIF 数据：验证与调试
采集到 EIF 文件后，您就可以在开发环境中进行回放，无需连接真实设备，也无需亲临现场。
根据您的开发环境，回放 EIF 的方式如下：
* Unity 开发
工具：使用 `session` 验证工具。这是一个集成在 Mega `ARSession` 中的工具，可以直接加载 EIF 文件并模拟 Mega 定位会话。
参考：具体使用方法请查阅 [使用 session 验证工具模拟运行](../unity/mega/verify-session-tool.html)。
* 微信小程序开发
工具：借助 Unity 编辑器。由于微信小程序开发环境的限制，推荐您在 Unity 编辑器中回放 EIF 数据来验证内容和逻辑。
参考：具体使用方法请查阅 [在 Unity 编辑器中模拟运行](../wechat/mega/content-simulation.html)。
总之，掌握 EIF 数据的采集与回放，是高效开发 EasyAR Mega 应用的必备技能。它将开发流程从“现场调试”转变为“离线分析”，显著缩短开发周期，并使团队协作和问题复现变得更加简单。

---

## EasyAR Mega 简介
- 章节路径: `mega/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/intro.html

# EasyAR Mega 简介
EasyAR Mega 是一项端云协同的空间计算技术，旨在为整个物理世界（例如一个城市、一个园区或一个大型商场）创建持久化的、高精度的数字孪生空间。通过 EasyAR Mega，您的应用可以实现大规模、高精度的室内外定位与虚实遮挡，为用户带来前所未有的空间交互体验。
本章将从开发者的角度，简要介绍 EasyAR Mega 的核心工作原理、预期效果及平台适配指引。
> **重要事项**
非开发者用户（如产品经理、运营、测试人员等）直接前往 [Mega 使用指南](../../mega/overview.html) 了解 Mega 服务。
## 开始之前：确保定位服务就绪
在您的应用中集成 EasyAR Mega 功能前，**必须确保一个核心前提：Mega 云定位服务已准备完成**。
* **已完成现场数据采集**
* 使用指定设备采集目标区域的数据
* 使用 Mega Toolbox 采集 EIF 数据用于效果验证
* **已完成 Mega Block 建图**
* **定位服务已启用并绑定应用**
* 在开发中心将 Block 添加至 Mega 定位库中
* 获取有效的 App ID、API Key 并正确配置到您的项目中
> **重要事项**
若未完成上述步骤，应用将无法获取定位结果，表现为“始终无法触发 AR 内容”。开发前务必 [验证服务可用性](../../mega/localization/verification.html)。
## Mega 定位基本原理
与依赖卫星信号的传统 GNSS 定位不同，EasyAR Mega 基于先进的视觉定位技术。通过将用户设备实时拍摄的图像数据与预先构建的高精度三维数据进行匹配，确定出用户在物理世界中的 6DoF 位姿。根据该位姿，应用端可以在正确的物理位置上渲染叠加出虚拟内容。
**工作流程如下：**
1. **地图构建**：
* 使用专业设备（如全景相机）在目标区域进行数据采集。
![Data Capture](https://doc-asset.easyar.com/develop/mega/media/data-acquire.jpg)
* 通过 EasyAR 的建图管理后台，将采集到的数据（如 **.360** 文件）上传。
* 云端处理平台将对采集数据中的图像进行计算，使用先进的 AI 算法提取目标区域的视觉特征；并将图像与 IMU 传感器等信息融合，恢复采集时的运动轨迹（即每个时刻的相机位姿）；进而生成整个场景的三维点云、构建带纹理贴图的稠密网格。
* 最终建图系统将输出一个由 EasyAR 自定义的高精度、包含三维几何信息和视觉特征的“Mega Block 地图”。这个地图是 Mega 定位的基石。
![Mapping Process](https://doc-asset.easyar.com/develop/mega/media/mapping-procedure.jpg)
* **实时定位**：
* 用户打开应用，设备摄像头实时捕捉用户视野中的图像，并与相机内参、外参（若有）、辅助信息（若有，如 GNSS ）等一并发送给 Mega 云定位服务。
![User case](https://doc-asset.easyar.com/develop/mega/media/user-experience.jpg)
* Mega 云定位服务会提取上传图像的视觉特征，并与定位库中的 Mega Block 地图进行快速比对和匹配。
* 一旦匹配成功，系统就能以厘米级的精度计算出用户当前在地图中的确切位姿（即位置和朝向）。
* 此时，Mega 云定位会将解算好的位姿下发到应用端，并在应用端与设备本身的 SLAM 系统进行融合跟踪。
* 最终，应用端将获得一个实时定位并持续跟踪的位姿，从而让虚拟内容可以显示在物理世界中预先锚定的位置上，并跟随人的移动而持续更新。
![Localize Process](https://doc-asset.easyar.com/develop/mega/media/localization-procedure.jpg)
## 效果与预期结果
成功集成 EasyAR Mega 后，您的应用可以实现以下令人惊叹的效果：
* **厘米级精度**：相比 GNSS 的数米甚至数十米误差，Mega 定位可以提供亚米级乃至厘米级的定位精度，让虚拟内容稳定地“钉”在真实世界的特定位置上。
* **持久化空间**：虚拟内容可以被放置在物理世界的任何地方，并且所有用户在相同位置看到的内容都是一致的。
* **真实遮挡**：通过 Mega 的空间理解能力，虚拟物体可以被真实的建筑物或障碍物遮挡，极大地增强了沉浸感。
* **无 GNSS 区域工作**：在室内、地下停车场、高楼林立的城市街道或者树木茂盛的山川森林等 GNSS 信号弱或无效的区域，Mega 依然能提供稳定可靠的定位服务。
>
> 视频中是一个典型的使用 EasyAR Mega 的效果示例：
>
>
> 高精度、持久化的空间定位让虚拟内容完美的贴合在建筑表面，呈现美轮美奂的动态视频和精心设计的巨幅 3D 海报。
>
> 空间理解带来的真实遮挡，让天空中绽放的烟花、数字特效与周围环境相得益彰，没有违和感。
>
> 在先进的视觉算法加持下，整个体验无惧周围复杂、密集的人员环境，即便是在夜间也能稳定工作。
>
>
### 可能遇到的不理想情况
* **定位识别速度较慢**
>
> 在人流密集区域如大型活动的现场，由于网络延时、并发请求等情况，Mega 云定位的延时可能会比较大，用户可能会需要等待一定时间才能看到虚拟内容。
>
* **环境变化导致误差**
>
> 如果物理环境发生了剧烈变化（例如，施工围挡、季节性植被变化），可能会导致定位精度下降或丢失。Mega 地图需要定期更新以适应环境变化。
>
* **持续体验出现飘移**
>
> Mega 定位在应用端会与设备本身的 SLAM 系统进行融合跟踪，并持续开启摄像头。长时间运行可能导致设备 CPU 降频，从而引发画面卡顿或掉帧，跟踪尺度飘移等现象。
>
> **提示**
更多详细的效果异常或故障，请参考 **故障排查** 章节：
* [Mega 常见问题](faq.html)
* [内容不显示](content-nodisplay.html)
* [内容跳动和飘移](content-drift.html)
* [问题报告](report.html)
## 扩展建议
如果您在集成 EasyAR Mega 过程中遇到诸如服务故障、场景变化、业务扩容等诸多**非程序开发**的相关问题，请访问我们的 [Mega 使用指南](../../mega/overview.html)。
在该指南中，您可以找到：
* **服务创建**：查看如何创建 Mega 服务以及简单的故障排查。
* **效果优化**：学会如何预览运行效果以及收集异常数据，冷启动监测等。
* **持久运营**：了解如何应对场景变化、业务扩容以及迁移/升级等持久化运营需求。
* **业务对接**：熟悉导航路网等实用业务数据的使用。
* **参考资源**：Mega Studio、Mega Toolbox 等实用工具的操作手册。
通过本篇，希望您对 EasyAR Mega 的工作原理和效果有了清晰的认识。接下来，您可以开始着手准备您的第一个 Mega 项目了！
## 平台专用指南
EasyAR Mega 的集成方式与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [快速入门](../unity/mega/quickstart.html)
* [启用 Mega](../unity/mega/enable-mega.html)
* [AR Session 最佳实践](../unity/mega/session-best-practice.html)
* [添加跟踪目标](../unity/mega/target.html)
* [添加与实景对齐的 3D 内容](../unity/mega/content-realworld-alignment.html)
* [控制跟踪过程](../unity/mega/tracker.html)
* [使用 PC 相机的快速验证](../unity/mega/verify-pc-camera.html)
* [使用 session 验证工具模拟运行](../unity/mega/verify-session-tool.html)
* [环境遮挡](../unity/mega/occlusion.html)
* 组件参考
* [MegaTrackerFrameFilter 组件参考](../unity/mega/comp-MegaTrackerFrameFilter.html)
* [BlockHolder 组件参考](../unity/mega/comp-BlockHolder.html)
* [BlockRootController 组件参考](../unity/mega/comp-BlockRootController.html)
* [BlockController 组件参考](../unity/mega/comp-BlockController.html)
* 快速入门
* [快速运行](../wechat/mega/quickstart.html)
* [在 Unity 里使用 Mega Studio](../wechat/mega/content-unity-setup.html)
* [摆放 3D 内容](../wechat/mega/content-simple.html)
* [完整运行](../wechat/mega/fullstart.html)
* [启用 Mega](../wechat/mega/integration.html)
* 基础组件
* AR Session
* [简介](../wechat/mega/session.html)
* [流程控制](../wechat/mega/session-state.html)
* [屏幕旋转适配](../wechat/mega/session-device-orientation.html)
* [使用非现场模式](../wechat/mega/session-gnss-simulation.html)
* [平面检测异常处理](../wechat/mega/session-plane-detection-error.html)
* MegaTracker
* [简介](../wechat/mega/tracker.html)
* [服务鉴权方式](../wechat/mega/tracker-access.html)
* [传感器外部控制](../wechat/mega/tracker-external-sensor.html)
* [使用 Landmark 服务](../wechat/mega/tracker-landmark.html)
* 内容展示
* 跨越微信XR-Frame编辑器缺失
* [创建并上传标注](../wechat/mega/content-annotation-creation.html)
* [创建与实景对齐的 3D 内容](../wechat/mega/content-simulation.html)
* [模拟运行](../wechat/mega/content-simulation.html)
* [运行时3D内容加载](../wechat/mega/content-load.html)
* [环境遮挡](../wechat/mega/occlusion.html)
* [透明视频](../wechat/mega/transparent-video.html)
* 问题诊断和报告
* [已知问题与限制](../wechat/mega/known-issues.html)
* [录制 ARSession dump 文件](../wechat/mega/session-dump.html)
* [示例说明](../wechat/mega/sample.html)

---

## 我的定位库可以使用了吗？
- 章节路径: `mega/localization-verify.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/localization-verify.html

# 我的定位库可以使用了吗？
恭喜您！现在您已经对 Mega 的工作原理、适用场景、设备支持等方面有了一个了解，并已学会获取和使用 APIKey，那么您的应用已经具备了实现高精度空间定位的基础。
## 开始之前
在您开始正式编写应用逻辑之前，请确保：
1. **定位库已添加正确地图**
检查您的定位库，确保其中已经正确添加了您的应用需要使用区域的地图。
2. **SDK 配置正确**
确认您的代码中已经正确初始化了 EasyAR SDK，配置了有效的 SDK License，并且传入了有效的 Mega 服务的 API Key。
3. **地图被正确引用**
在您的场景或代码中，确保 Mega 定位模块（如 `MegaTracker` 组件）已经正确指向了您添加的地图资源。
如果以上步骤都已完成，那么您的定位库理论上已经可以正常工作了。
## 遇到问题
如果您在检查以上步骤时遇到问题，参考阅读以下文章进行解决：
* **您还没有地图**
您需要先为目标物理空间创建一张 Mega 地图。这通常包含两个步骤：数据采集和建图。参考阅读：
* [数据采集](../../mega/acquisition/intro.html)
* [建图](../../mega/mapping/intro.html)
* **您已有地图但不确定质量**
地图的精度和覆盖范围直接影响定位效果。可查看建图结果来辅助您判断。参考阅读：
* [回看采集路线](../../mega/mapping/routes.html)
* [查看建图报告](../../mega/mapping/report.html)
* [预览 3D 实景网格](../../mega/mapping/textured-mesh.html)
* **关于地图的加载与管理**
关于如何在定位库中加载以及管理建图结果，参考阅读：
* [管理定位库](../../mega/localization/database-management.html)
* [确认定位库可用](../../mega/localization/verification.html)
* **SDK License 及 APIKey**
如果遇到 License 或 APIKey 相关问题，参考阅读：
* [EasyAR Sense 许可证](../license-sense.html)
* [获取和使用APIKey](../apikey-auth.html)
当您的项目中包含了**有效且高质量**的 Mega 地图后，您的定位库就真正准备就绪了。请根据您的具体情况，参考上述文档完成地图的准备和配置工作，然后就可以开始编写激动人心的 AR 应用了！

---

## 导航场景最佳实践
- 章节路径: `mega/navigation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/navigation.html

# 导航场景最佳实践
在导航场景中，提供流畅、精准的用户体验至关重要。EasyAR Mega 提供了多种 xDoF 模式来适应不同的设备能力和环境需求。理解这些模式的差异，并结合平台特性进行选择，是构建优秀导航应用的关键。
> **提示**
参考阅读： [不同设备上的体验差异](devices.html#xdof-grade)。
## 正确选择跟踪模式
在 Mega 定位的基础上，我们可以根据设备提供的传感器能力和应用需求，选择不同的跟踪模式来增强导航体验。
对于具备 ARKit 或者 ARCore 的手机来说，您只需使用默认的 6DoF 跟踪模式，结合 Mega 空间定位即可实现稳定、平滑的连续路径导航，提供最佳的用户导航体验。
但是，针对 ARKit 或 ARCore 支持情况不够明确、或者用户群体最广泛的中低端机型，选择合适的 xDoF 模式至关重要。因为不同的 xDoF 工作模式，将直接影响终端的跟踪效果。
对于这类机型，您需要按照以下顺序优先测试、并选择它们的工作模式：
* **惯导 / 5DoF 模式**
* **描述**：它利用设备的传感器，通过 EasyAR 内建的惯导算法实现 5DoF 跟踪，在一定程度上提供稳定、平滑的连续路径导航。
* **行为**：当用户行走时，虚拟的路径指示（如地面上的箭头）会稳定地贴合在地面上，即使用户短暂地晃动或改变朝向，指示也不会发生大的跳动。但如果有高度方向上的爬升或下降时（如上下楼梯），虚拟内容将不再贴合而是浮在空中或位于地面之下。
* **要求**：需要设备具备高质量的陀螺仪和加速度计。
* **适用场景**：绝大多数室内外导航场景，作为 6DoF 不可用时的首选降级方案。
* **3DoF 模式**
* **描述**：当设备没有加速度计但有陀螺仪时，可以降级到 3DoF 模式。
* **行为**：在 3DoF 模式下，导航指示会根据设备的朝向（俯仰、偏航、滚转）进行旋转，但当用户**平移**（前进、后退、侧移）时，指示物在空间中的**位置不会更新**。它会像一个指南针一样，始终指向正确的方向，但不会跟随用户的脚步在地图上移动。
* **要求**：设备至少需要有陀螺仪。
* **适用场景**：作为 5DoF 都不可用时的降级方案。可以用于简单的方向指引，但不适合需要精确路径跟随的复杂导航。
* **0DoF 模式**
* **描述**：这是最基础的模式，几乎适用于所有设备，但用户体验也最有限。
* **行为**：在 0DoF 模式下，设备无法感知自身的任何移动或旋转。导航指示会固定在屏幕的某个位置（例如，屏幕中央的箭头），仅指示目标的**相对方向**（例如，目标在您的左前方）。
* **要求**：无特殊传感器要求。
* **适用场景**：作为最终降级方案，或用于简单的“找方向”功能，类似于传统导航中的罗盘。
**体验对比总结：**
|跟踪模式|用户移动时的行为|用户体验|推荐度|
|**6DoF**|虚拟路径稳定地跟随用户在真实空间中的各种移动|**最佳**，沉浸感强，精准|⭐⭐⭐⭐⭐|
|**5DoF (惯导)**|虚拟路径稳定地跟随用户的移动，但当高度变化时会失效|**次佳**，6DoF 失效时的降级首选|⭐⭐⭐⭐|
|**3DoF**|路径指示随设备朝向旋转，但不跟随用户移动|**一般**，可以指示方向，但缺乏空间跟随感|⭐⭐⭐|
|**0DoF**|指示固定在屏幕上，仅显示目标的方向|**基础**，仅能提供方向信息|⭐|
## 微信小程序平台的特殊说明
**重要提示：微信小程序平台的 Mega WeChat MiniProgram Plugin 尚未完全发布支持5DoF (惯导)、3DoF、0DoF 的功能。**
在微信小程序中，当前阶段主要支持的是 **6DoF** 模式的导航体验。
* **当前行为**：用户在小程序中启动基于 Mega 的导航后，如果运行的设备本身并不支持 6DoF 模式，则 `ARSession` 会无法启动，并在终端报错。
* **开发建议**：在微信小程序上规划导航功能时，请**以 6DoF 模式作为前提进行设计**。查看 [微信官方文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录) 获取设备支持列表，或者通过我们的 API 调用检查设备是否支持。
```
const easyarPlugin: easyar.EasyARWechatMiniprogramPlugin = requirePlugin("easyar-wechat-miniprogram") as easyar.EasyARWechatMiniprogramPlugin;
if (easyarPlugin.isMegaTrackerSupported() === false) {
const message = `当前设备不支持 VK v1 和 v2，请参考微信官方文档：https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html`;
wx.showModal({
title: "设备不支持",
content: message,
showCancel: false,
});
console.error(message);
}
```
## 微信小程序平台的替代方案
对于需要在微信小程序中实现拥有**完整设备支持**的导航应用的开发者，我们强烈推荐您直接使用我们的 **视＋ AR 导航** 产品。
该导航产品是专门为小程序生态优化的解决方案，具备以下优势：
* **开箱即用**：无需复杂的 Mega SDK 集成，通过简单的 API 调用即可快速接入。
* **广泛兼容**：广泛兼容各种终端设备，支持从 0DoF 到 6DoF 的几乎所有设备。
* **功能完整**：支持完整的路径规划、偏航纠正、转弯提示、数字人指引等高级导航功能。
* **配套完善**：配套完备的信息管理、路网部署、POI 调整、路算服务等实用后台和工具。
* **体验优化**：针对微信小程序的性能和交互特点进行了深度优化，确保流畅的用户体验。
**如何开始？**
请访问 **[AR 导航官方页面](https://www.sightp.com/nav.html)**，了解如何快速集成和使用我们的导航产品来构建您的小程序应用。
## 最佳实践总结
* 在 Android/iOS 设备上开发 App 或在支持 6DoF 的头显设备上，请优先使用 **Mega + 6DoF** 模式，以获得最佳导航体验。根据运行设备的实际情况，降级成 5DoF、3DoF 和 0DoF 以最大化的获得广泛的设备兼容性。
* 在 **微信小程序** 平台，现阶段仅支持在 **6DoF** 模式的设备上运行，或直接接入 **视＋ AR导航** 以实现完整的设备支持和丰富的产品功能。

---

## 问题报告与反馈
- 章节路径: `mega/report.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/mega/report.html

# 问题报告与反馈
我们非常重视您的反馈，这是帮助我们改进 EasyAR Mega 产品和服务的关键。为了让我们能够快速、准确地定位并解决您遇到的问题，请在提交报告前，花几分钟时间阅读本篇指南。
## 我们的联系方式
您可以通过以下渠道向我们提交问题报告：
* **官方开发者社区/论坛** - 推荐用于一般性问题和社区交流。
* 中文用户点击 [这里](https://answers.easyar.cn)
* 其他用户点击 [这里](https://answers.easyar.com)
* **企业微信群** - 适用于需要保密或更正式支持的企业级用户。
* 扫描下方二维码进群
![](https://doc-asset.easyar.com/develop/mega/media/wechat.png)
* **更多联系方式** - 作为备选方案。
* 获取联系方式点击 [这里](https://www.easyar.cn/view/contactus.html)
## 提交一份高质量报告的核心要素
一份包含以下信息的报告，将极大地帮助我们复现和解决问题。**信息越完整，问题解决越快。**
### **通用报告清单（所有问题都需要）**
1. **问题清晰描述**：
* 您期望实现的效果是什么？
* 实际发生了什么？（例如：应用闪退、定位失败、内容飘移）
* 问题发生的频率（必现/偶现）？在什么条件下发生？
* **设备与环境信息**：
* **设备型号**：例如，`iPhone 14 Pro`, `Samsung Galaxy S23 Ultra`, `Apple Vision Pro`。
* **操作系统版本**：例如，`iOS 17.2`, `Android 14`, `visionOS 26`。
* **EasyAR SDK 版本**：例如，`EasyAR Sense Unity Plugin v4.6.0`。
* **测试环境**：室内/室外，光照条件，是否为动态环境。
* **EIF 数据（最重要的证据）**：
* **请务必提供能够复现问题的 EIF 录制文件**。
* EIF 数据包含了问题发生时的所有传感器和图像信息，是我们诊断问题的最有力工具。请参考 [采集模拟运行数据](input-recording.html) 了解如何录制。
* **日志文件 (Log)**：
* 请提供问题发生时的完整应用日志。
* **Android**: `Logcat` 输出。
* **iOS**: `Console.app` 日志或 Xcode 控制台输出。
* **Unity**: Unity Editor 的 `Console` 日志。
* **微信小程序**：`session.dumpLog()` 得到的日志文件。
* **录屏或截图**：
* 问题发生时的屏幕录像或高清截图，这能直观地展示您所描述的现象。
* 不同设备的操作指南可参考：[手机录屏](../diagnostics/recordings.html)、[头显录屏](../diagnostics/recordings-headsets.html)。
* **Mega 定位库信息**
* 在 Unity 中导出应用所使用的 Mega 定位库的服务信息。导出方法：
![Mega Service Export](https://doc-asset.easyar.com/develop/mega/media/mega-service-export.png)
## 特定问题类型的补充清单
为了让问题定位更精准，请根据您的问题类型，额外提供以下信息：
**A. 定位失败或不稳定**
* 已尝试使用 **Mega Toolbox** 或 PC 端工具在相同位置进行验证，并说明结果。
* 已确认定位库中加载的地图与当前物理空间一致。
* 说明问题发生的大概位置（例如，商场中庭、景区门口）。
**B. 内容不显示**
* 已提供使用外部工具验证定位的结果。
* 已明确内容摆放或代码逻辑没有问题。
* 如果是渲染问题，请提供所用模型、Shader 或特效的截图或描述。
**C. 内容跳动或飘移**
* 已说明设备的移动方式（平稳移动/快速移动）。
* 已描述环境的纹理和光照情况，以及是否存在极度相似的混淆区域。
* 已说明应用内部对姿态的处理逻辑以及内容摆放正确。
**D. 微信小程序问题**
* 已提供用户在微信内开启 Mega 服务权限的截图。
* 已说明用户手机型号是否在微信官方支持列表中。
* 已提供小程序的 AppID 和具体的业务场景描述。
**E. 性能问题 (卡顿、功耗高)**
* 已说明问题发生的设备型号。
* 已提供应用运行时的 CPU/GPU 占用率或设备温度信息（如果可能）。
* 已说明 3D 内容的复杂程度（模型面数、纹理大小）。
* 已说明是否使用了多图配置。
## 使用 EasyAR Sense Unity Plugin 导出 Unity 开发信息
特别地，针对 Unity 平台的 Mega 应用开发，我们准备了更便捷的反馈信息生成工具。详细的操作步骤如下：
1. 在菜单栏打开 `EasyAR > Sense > 提问`
![提问](https://doc-asset.easyar.com/develop/mega/media/unity-question.png)
2. 在 `提问` 中提供以下信息:
* 勾选运行环境（单选），如 Android。
* 复制设备信息。在 `ARSession` 中将 `DiagnosticsController.DumpSession` 设置为 `Log`，复制一帧的输出并填写结果到设备信息框中。
![Dump session](https://doc-asset.easyar.com/develop/mega/media/unity-device-info.png)
* 勾选您的应用在使用的所有 EasyAR 功能，支持多选。
* 确定已经完成页面中的四项检查并打勾，建议在提问时描述如何在 Sample 中复现问题。
* 点击右上角的复制功能，即完成了 Unity 开发信息的收集。
![导出 Unity 开发信息](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
## 报告提交流程建议
1. **准备材料**：根据上述清单，收集 EIF、日志、截图/录屏、服务信息、开发信息等。
2. **撰写报告**：清晰描述问题，并附上所有材料。
3. **提交**：通过您选择的渠道提交报告。
4. **跟进**：我们收到报告后，会通过商务或邮件与您联系。请保持关注。
感谢您的时间和对 EasyAR Mega 产品的支持！您的每一次反馈，都在帮助我们构建更好的空间计算未来。

---

## EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系
- 章节路径: `motion-tracking/comparison.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/comparison.html

# EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系
EasyAR 的运动跟踪（Motion Tracker）利用计算机视觉和惯性同步定位和建图（VI-SLAM）技术，在更多的手机和平板上实现六自由度（6 Degrees of Freedom, 6DoF）的实时跟踪功能。
## 为什么选择使用 EasyAR 运动跟踪
EasyAR 运动跟踪功能相较系统级的运动跟踪方案(如 ARKit、ARCore、华为 AR Engine 等)有以下优点：
* 提供更广泛的设备支持能力。覆盖了约70%的主流设备，相较于其他方案机型覆盖率高出 30-60%。
* 对中低端机型专门算法优化，保证算力有限的平台也有较好的效果。
* 无需安装其他应用，而 ARCore 等其他平台都需要用户手动下载安装对应算法的应用。
## EasyAR 运动跟踪功能的特点
EasyAR 通过先进的计算机视觉识别相机图像中显著特征点并跟踪其位置变化，结合设备的惯性测量单元(IMU)数据信息，实时计算当前设备相对于真实世界的六自由度位置和姿态。渲染引擎根据返回的姿态和朝向同步渲染虚拟场景就可以保证虚拟的物体与现实环境进行贴合。
* 真实尺度
利用设备的惯导传感器和相机图像数据融合，恢复轨迹和场景真实物理尺度。
* 鲁棒准确的运动跟踪
多传感器融合算法能降低长时间跟踪的漂移，且对于光照变化、弱纹理区域和动态物体等更鲁棒。
* 快速初始化
通常仅需要设备对着应用场景平移即可实现初始化。
* 视觉重定位
在设备跟踪丢失后/跟踪不佳后快速准确地恢复设备相对于世界坐标系的位姿。
## EasyAR 运动跟踪最佳实践
虽然 EasyAR 运动跟踪针对各种挑战性场景进行优化，为了保证最佳的效果，可以引导用户遵循下列最佳实践。
* 避免快速运动，包括平移或者旋转
* 减少纹理不丰富的区域
* 保证良好的光照条件
## 在 EasyAR Motion Tracker 与平台原生的运动跟踪功能之间切换
为保证最佳效果，在部分平台，EasyAR 可能默认选择可用的平台原生的运动跟踪方案而不需要额外配置。例如在 iOS 平台上，EasyAR SDK 会优先使用ARKit的运动跟踪功能。类似的，在部分 ARCore/AR Engine 支持的安卓/鸿蒙设备上，EasyAR SDK 可能会默认使用其提供的运动功能。
## 后续步骤
* 了解 EasyAR MotionTracker 支持的机型，请查看 [Motion Tracker 支持的设备](devices-easyar.html)
* 在 EasyAR 中使用 AR Engine 的运动跟踪，请查看 [AR Engine支持的机型](devices-arengine.html)

---

## 谷歌 ARCore 与运动跟踪
- 章节路径: `motion-tracking/devices-arcore.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices-arcore.html

# 谷歌 ARCore 与运动跟踪
谷歌的 ARCore 是用于在 Android 上的增强现实引擎。其为部分 Android 机型提供包括运动跟踪在内的多项能力。在 Unity 上为保证最佳效果，在 ARCore 支持的机型上，EasyAR Sense 默认选择 ARCore 的运动跟踪功能而不是 EasyAR 内置的 `Motion Tracker` 功能。
## ARCore 支持的机型和功能
与其他的 [运动跟踪](intro.html) 功能类似，ARCore 需要设备至少具备摄像头、陀螺仪和加速度计，而且经过谷歌标定并认证才可运行。
ARCore 官方支持的机型列表需要查阅 ARCore 官方文档（[中文](https://developers.google.cn/ar/devices?hl=zh-cn) / [English](https://developers.google.com/ar/devices)）。
> **注意**
需要注意的是，在支持机型上，需要安装额外的 `Google Play Services for AR` App 才可以运行 ARCore 功能，在部分机型可能已经预装，部分机型需要用户自行安装。
## 在 EasyAR 中调用 ARCore
在 EasyAR 使用 ARCore，支持的机型并不与官方机型一致, 主要体现在部分官方支持列表内的机型 ARCore 实测效果异常。可以通过 `ARCoreCameraDevice` 的 `isAvailable` 方法判断这些有问题的机型，然后禁用 ARCore。
ARCore 除了运动跟踪之外还支持环境理解、光照估计等功能，使用 EasyAR 运动跟踪仅调用 ARCore 的运动跟踪功能，不支持其他功能。
以下是 ARCore 效果测试异常禁用的机型列表，这些设备通过 `isAvailable` 检查 ARCore 可用性均返回 `False`。
|Brand|Model Name|
|Redmi|Redmi K40|
|Redmi|Redmi K30S Ultra|
|Redmi|Redmi K40 Gaming|
|Redmi|Redmi K40 Pro|
|Redmi|Redmi K50G|
|Redmi|K30 PRO|
|Redmi|Redmi K30 Pro Zoom Edition|
|Redmi|Redmi K40S|
|Redmi|Redmi K30|
|Xiaomi|Mi 10T|
|Xiaomi|Mi 10 Ultra|
|Xiaomi|MI 9|
|Xiaomi|Mi 10 Pro|
|Redmi|Redmi K20|
|Redmi|Redmi K20|
|Xiaomi|Mi 10T Lite|
|Xiaomi|Mi 10i|
|Xiaomi|MI 9 SE|
|Xiaomi|Mi 10 lite 5G|
|Xiaomi|Xiaomi 12X|
|Xiaomi|Mi 9 Lite|
|Redmi|Redmi K20 Pro|
|Redmi|Mi 9T Pro|
|Xiaomi|Mi 10|
|Xiaomi|Mi 10 Lite zoom|
## 延伸阅读
* [运动跟踪 支持的设备](devices.html)
* [EasyAR 运动跟踪与 ARKit/ARCore/华为 AR Engine 的关系](comparison.html)

---

## 华为 AR Engine 与运动跟踪
- 章节路径: `motion-tracking/devices-arengine.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices-arengine.html

# 华为 AR Engine 与运动跟踪
华为的 AR Engine 是用于在 HarmonyOS/Android 上的增强现实应用的引擎。其为部分华为机型提供包括运动跟踪在内的多项能力。在 Unity 上，为保证最佳效果，在 AR Engine 支持的机型上，EasyAR Sense 默认选择 AR Engine 的运动跟踪功能而不是 EasyAR 内置的运动跟踪（Motion Tracker）。
> **重要事项**
这里所列的列表，是 EasyAR 实际测试并验证可用的，其他型号均不支持，注意与 AR Engine 官方支持的机型列表进行区分。
经过 EasyAR 验证通过可以正常使用 AR Engine 运动跟踪功能的机型如下:(截止 2026年 1月)
|设备型号|代号|
|Mate X5|HWALT-B|
|Mate 60 RS 非凡大师|HWALN|
|Mate 60|HWBRA|
|Mate 60 Pro|HWALN|
|Mate 60 Pro+|HWALN|
|Pura 70|HWADY|
|Pura 70 Pro+|HWHBN|
|Pura 70 Pro|HWHBN|
|Pura 70 Ultra|HWHBP|
|P50 Pocket|HWBAL|
|P50 Pro|HWJAD-Q|
|P50 Pro|HWJAD|
|P40|HWANA|
|P40 Pro|HWELS|
|P40 Pro|HWELS-P|
|P30|HWELE|
|P30 Pro|HWVOG|
|P20|HWEML|
|P20 Pro|HWCLT|
|Mate 40|HWOCE-L|
|Mate 40 Pro|HWNOH|
|Mate 40E Pro|HWNOH|
|Mate 40 Pro+|HWNOP|
|Mate 40 RS|HWNOP|
|Mate 30|HWTAS|
|Mate 30-5G版|HWTAS|
|Mate 30 Pro|HWLIO|
|Mate 30 RS 保时捷设计|HWLIO|
|Mate 30 Pro-5G版|HWLIO|
|Mate 30E Pro-5G版|HWLIO-L|
|Mate X2|HWTET|
|Mate 20|HWHMA|
|Mate 20 X|HWEVR|
|Mate 20 X-5G版|HWEVR|
|Mate X|HWTAH|
|MateXS|HWTAH|
|MateXS|HWTAH-C|
|Mate RS保时捷版|HWNEO|
|nova 8|HWANG|
|nova 8|HWANG-DL|
|nova 8 Pro|HWBRQ|
|nova 7|HWJEF|
|nova 7 Pro|HWJER|
|nova 6|HWWLZ|
|nova 6-5G版|HWWLZ|
|nova 5|HWYAL|
|nova 5|HWSPN|
|nova 5 Pro|HWSEA-A|
|nova 4|HWVCE|
|荣耀30|HWBMH|
|荣耀30S|HWCDY-H|
|荣耀30S|HWCDY|
|荣耀30 Pro|HWEBG|
|荣耀30 Pro+|HWEBG|
|荣耀V30|HWOXF|
|荣耀V30 Pro|HWOXF|
|荣耀20|HWYAL|
|荣耀20 Pro|HWYAL|
|荣耀V20|HWPCT|
|荣耀9x|HWSTK-HF|
|荣耀9x|HWHLK-H|
|MatePad Pro(MRX)|HWMRX|
|MatePad Pro 5G|HWMRX|
|MatePad Pro|HWMRX|
|MatePad Pro(WGR)|HWWGR|
|M6|HWSCM|
|M6|HWVRD|

---

## EasyAR 运动跟踪支持的设备
- 章节路径: `motion-tracking/devices-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices-easyar.html

# EasyAR 运动跟踪支持的设备
## EasyAR 运动跟踪的最低设备要求
要运行 EasyAR 运动跟踪需要满足以下必要（非充分）的要求
* 包含摄像机，加速度计和陀螺仪。
* Android 7.0 (API Level 24) 及以上。
> **注意**
如果设备缺少陀螺仪和加速度计，则无法使用运动跟踪功能，这种情况常在低端机型中相对常见(仅具备虚拟陀螺仪的机型不支持运动跟踪)。
## 保持最新的设备支持
为保持您的应用获取最新的设备支持，推荐下列方式：
* 集成最新发布的 EasyAR Sense SDK, 其内置最新的支持列表。
* SDK 在设备联网自动查询。可使用 CalibrationDownloader 联网并下载最新适配文件。
## EasyAR 运动跟踪的质量
EasyAR 根据设备本身的性能通过 Quality Level 进行分级，不同 Quality Level 的含义见下表。
|等级|说明|适用场景|
|NotSupported|设备不支持运动跟踪，可能是适配不达标或尚未适配|不可用于 AR 运动跟踪相关功能|
|Bad|设备不完全达标，尺度不稳定|有限的桌面尺度小场景|
|Limited|设备不完全达标，尺度接近准确|房间尺度中等场景，如 AR 游戏、AR 渲染、AR 导航|
|Good|设备达标，尺度准确|建筑物尺度大型场景，如 AR 游戏、AR 渲染、AR 导航、三维重建|
## 为什么设备不支持运动跟踪
新的机器设备默认并不支持运动跟踪，且列表里的手机可能存在个别机型不被支持的情况，可能的原因包括：
* 未完整适配，新机型发布，待适配。
* 硬件问题，例如部分机型并不包含陀螺仪。
* 效果验证不佳，EasyAR 通过标定确认机型运动跟踪效果不佳。
* 未联网下载最新的标定文件。
* 软件问题，例如系统升级后传感器同步出现异常被剔除。
如果您的机型不支持运动跟踪且硬件满足最低设备要求，请反馈您的设备具体型号，以便我们及时增加对您的设备的支持。
## EasyAR 运动跟踪支持的设备型号列表
EasyAR 会定期标定新发布的机型，不断增加运动跟踪支持的设备数量，更新频率正常是1次/季度。
当前 EasyAR 运动跟踪支持的机型见下表。
|设备型号|代号|Quality Level|
|Huawei Mate30 pro, HUAWEI MATE 30 PRO 5G,HUAWEI MATE 30 RS PORSCHE DESIGN|HWLIO|Good|
|Huawei Mate30 pro, HUAWEI MATE 30 PRO 5G,HUAWEI MATE 30 RS PORSCHE DESIGN|HWLIO-L|Good|
|hauwei Mate30e pro||Good|
|Huawei Mate30,HUAWEI MATE 30 5G|HWTAS|Good|
|Huawei P20|HWEML|Good|
|Huawei P30 pro|HWVOG|Good|
|Huawei P30|HWELE|Good|
|Huawei P30 lite / nova 4e|HWMAR|Good|
|Huawei P40|HWANA|Good|
|Huawei P40 4G||Good|
|honor Magic V Flip||Good|
|honor Magic V|HNMGI|Good|
|Honor Magic V||Good|
|Honor Magic V2||Good|
|Honor Magic VS||Good|
|Honor Magic VS2||Good|
|Honor Magic V3||Good|
|Honor Magic VS3||Good|
|Huawei P40 pro|HWELS|Good|
|Huawei P40 pro+|HWELS-P|Good|
|Huawei Mate40E||Good|
|Huawei Mate40|HWOCE-L|Good|
|Huawei Mate40 Pro|HWNOH|Good|
|Huawei Mate40 Pro+ / Huawei Mate 40 RS Porsche Design|HWNOP|Good|
|Mate50.Legacy data|HWCET|Good|
|Mate 50E. Legacy data|HWCET-QL|Good|
|TD Tech M40||Good|
|Mate 50 Pro. Legacy data|HWDCO|Good|
|Mate 60. Legacy data|HWBRA|Good|
|Mate 60 Pro|HWALN|Good|
|Mate 70||Good|
|Mate 70 Pro||Good|
|Mate 70 Pro+||Good|
|Huawei P50|HWABR-Q|Good|
|Huawei P50E|HWABR-QL|Good|
|TD Tech P50||Good|
|Huawei P50 Pocket|HWBAL|Good|
|Huawei P50 Pro|HWJAD|Good|
|Huawei P50 Pro|HWJAD-Q|Good|
|Huawei P60|HWLNA|Good|
|Huawei P60 Art||Good|
|Huawei P60 Pro|HWMNA|Good|
|Huawei Pura70||Good|
|Huawei Pura 70||Good|
|Huawei Pura 70Pro||Good|
|Huawei Pura 70 Pro||Good|
|Huawei Pura 70 Pro+||Good|
|Huawei Pura 70 Ultra||Good|
|Huawei Pura 80|hedy|Good|
|Huawei Pura 80 Pro|Lamarr|Good|
|Huawei Pura 80 Ultra|LamarrU|Good|
|Huawei Pura X||Good|
|Huawei Pocket||Good|
|Huawei Pocket 2||Good|
|Huawei nova9 SE|HWJLN-Q|Good|
|Huawei nova9 Pro|HWRTE|Good|
|Huawei nova9|HWNAM|Limited|
|Huawei nova10 pro|HWGLA-Q|Limited|
|Huawei nova10|HWNCO-Q|Limited|
|Huawei nova10 se|HWBNE-Q|Limited|
|Huawei nova 10Z|HWCHA-H|Limited|
|Huawei nova11|HWFOA|Limited|
|Huawei nova11SE||Good|
|Huawei nova11 Pro ultra|HWGOA|Limited|
|Huawei nova12||Good|
|Huawei nova12 Pro||Good|
|Huawei nova12 Ultra||Good|
|Huawei nova13||Good|
|Huawei nova13 Pro||Good|
|Huawei nova14||Good|
|Huawei nova14 Pro||Good|
|Huawei nova14 Ultra||Good|
|Huawei nova4|HWVCE|Good|
|Huawei Honor V20 / HONOR View20|HWPCT|Good|
|Huawei Honor 20 /Honor 20 pro /nova 5T|HWYAL|Good|
|Huawei Honor 20s||Good|
|Huawei Honor 10i||Good|
|Huawei Honor 20i||Good|
|Honor 30 pro / Honor 30 pro+|HWEBG|Good|
|Honor 30 pro+||Good|
|Honor 30|HWBMH-N|Good|
|Honor 30|HWBMH|Good|
|Honor 30|HWBMH-L|Good|
|Honor 30s|HWCDY|Good|
|Honor 30s|HWCDY-H|Good|
|Honor 30 lite|HWMXW|Bad|
|Honor V40|HWYOK|Bad|
|Honor V40|HWALA|Bad|
|Honor 50||Good|
|Honor 50E|HNJLH|Good|
|Honor 60||Good|
|Honor 60 SE||Good|
|Honor 60 Pro||Good|
|Honor 70||Good|
|Honor 70 Pro||Good|
|Honor 80||Good|
|Honor 80 Pro||Good|
|Honor 80 Pro zhipingban||Good|
|Honor 80 SE||Good|
|Honor 80 GT||Good|
|Honor 90||Good|
|Honor 90Pro||Good|
|Honor 90GT||Good|
|Honor 100||Good|
|Honor 100 Pro||Good|
|Honor 200||Good|
|Honor 200 Pro||Good|
|Honor GT||Good|
|Honor GT Power||Good|
|Honor 300||Good|
|Honor 300 Pro||Good|
|Honor 300 Ultra||Good|
|Honor 400||Good|
|Honor 400 Pro||Good|
|Honor play|HWCOR|Good|
|Huawei NZONE S7||Good|
|Huawei NZONE S7 Pro||Good|
|Huawei NZONE S7 Pro+||Good|
|Honor 8A 2020|HWJAT-M|Good|
|Honor note 10|HWRVL|Good|
|honor 50 Lite|HNNTN|Good|
|honor 60 SE|HNGIA|Good|
|honor X30|HNANY|Good|
|honor X30 Max|HNKKG|Good|
|honor X40||Good|
|honor X40 GT||Good|
|honor X50|Ali|Good|
|honor X50 GT||Good|
|honor X60||Good|
|honor X60 Pro||Good|
|honor X60 GT||Good|
|honor X70||Good|
|honor Play 30Plus|HNCMA|Bad|
|honor Play 40||Good|
|honor Play 40 Plus||Good|
|honor Play 50 Plus||Good|
|honor Play 60 Plus||Good|
|honor Play 70 Plus||Good|
|Huawei Y9a||Good|
|Honor Play 4 Pro 5G|HWOXP|Bad|
|Honor Play 5||Good|
|Honor Play 5T||Good|
|Honor Play 5T Pro||Good|
|Honor Play 6T||Good|
|Honor Play 6T Pro||Good|
|Honor Play 6C||Good|
|Honor Play 7T||Good|
|Honor Play 9C|Nick|Bad|
|Honor Play 9T Pro||Good|
|Honor Play 10C||Good|
|Huawei Mate Xs|HWTAH|Good|
|Huawei Mate Xs|HWTAH-C|Good|
|Huawei Mate XT||Good|
|Huawei Mate Xs2|HWPAL|Good|
|Huawei Mate X2|HWTET|Good|
|Huawei Mate X3|HWALT|Good|
|Huawei Mate X5|HWALT-B|Good|
|Huawei Mate X6||Good|
|Honor X10 5G|HWTEL|Good|
|Honor X10 5G|HWTEL-H|Good|
|Honor X10 Max 5G|HWKKG|Bad|
|Huawei MatePad Pro / MatePad Pro 5G /MatePad Pro wifi|HWMRX|Good|
|Huawei MatePad 11 (2021)|HWDBY|Limited|
|Huawei MatePad Pro 12.6 (2021)|HWWGR|Good|
|Huawei MatePad Pro 11 (2022)|HWGOT|Good|
|Huawei MatePad 10.8|HWSCMR|Good|
|Huawei MatePad Pro 10.8 (2021)|HWMRR|Good|
|Huawei MatePad 10.4|HWBAH|Good|
|Huawei MatePad 10.4|HWBAH3|Good|
|Huawei MediaPad M6 10.8|HWSCM|Good|
|Huawei MediaPad M6 8.4|HWVRD|Good|
|nova 5z / nova 5i pro|HWSPN|Good|
|vivo 5i||Good|
|Huawei nova 5|HWSEA-A|Good|
|nova 5 pro||Good|
|Huawei nova 6 / nova 6 5G|HWWLZ|Good|
|Huawei nova 7 5G|HWJEF-N|Good|
|Huawei nova 7 5G|HWJEF|Good|
|Huawei nova 7 pro 5G|HWJER|Good|
|Huawei nova 8 Pro|HWBRQ|Good|
|Huawei nova 8|HWANG|Good|
|Huawei nova 8|HWANG-DL|Good|
|Huawei Y Max/ Enjoy max|HWARS|Good|
|Huawei Y Max/ Enjoy max|HWARS-Q|Good|
|Huawei MediaPad M5 Lite 8|HWJDN2|Good|
|Huawei MediaPad M5 10 / pro|HWCMR|Good|
|Huawei MediaPad M5 8|HWSHT|Good|
|honor 50|HNNTH|Good|
|honor 50 Pro|HNRNA|Good|
|honor 60|HNLSA|Good|
|honor 60 Pro|HNTNA|Good|
|honor 70|HNFNE|Good|
|honor 70 pro|HNSDY|Good|
|honor 70 pro+|HNHPB|Good|
|honor X20|HNNTN|Bad|
|honor X20 SE|HNCHL|Bad|
|honor Magic 3|HNELZ|Bad|
|honor Magic 3 Pro||Good|
|honor Magic 3 Pro+||Good|
|honor Magic 4 lite / X9 5G|HNANY-Q|Good|
|honor Magic 4|HNLGE|Good|
|honor Magic 4 Pro||Good|
|honor Magic 4 ultimate||Good|
|Honor Magic 5|HWPGT|Good|
|Honor Magic 5 Pro||Good|
|Honor Magic V5|Maybach|Good|
|Mi Pad 6S Pro|sheng|Good|
|Honor Magic 6|HNBVL|Good|
|Honor Magic 6 Pro||Good|
|Honor Magic 6 Lite||Good|
|Honor Magic 7||Good|
|Honor Magic 7 Pro||Good|
|Honor Magic 7 Pro RSR||Good|
|Huawei honor V30 / V30 Pro / HONOR View30 / View30 Pro|HWOXF|Good|
|Huawei honor V40||Good|
|Huawei honor V purse||Good|
|Huawei Enjoy 50||Good|
|Huawei Enjoy 50 Pro||Good|
|Huawei Enjoy 50Z||Good|
|Huawei Enjoy 60X|HWSTG|Limited|
|Huawei Enjoy 60||Good|
|Huawei Enjoy 60 Pro||Good|
|Huawei Enjoy 70||Good|
|Huawei Enjoy 70 Pro||Good|
|Huawei Enjoy 70Z||Good|
|Huawei Enjoy 70S||Good|
|Huawei Enjoy 80||Good|
|Huawei Enjoy 20 5G|HWWKG|Bad|
|Huawei Enjoy 20 5G|HNKOZ-S|Bad|
|Huawei Enjoy 20 Plus 5G||Good|
|Huawei Enjoy Z 5G / Enjoy 20 Pro|HWDVC|Bad|
|Huawei Enjoy Z 5G / Enjoy 20 Pro|HWDVC-M|Bad|
|Honor Play 4T||Good|
|Honor Play 4T Pro||Good|
|Honor Play 4||Good|
|Honor Play 4 Pro||Good|
|Honor 9X / Huawei Enjoy 10 Plus / Huawei P Smart Z|HWSTK-HF|Good|
|Honor 9X Pro|HWHLK-H|Good|
|Huawei Mate 20|HWHMA|Good|
|Huawei Mate 20 X / Huawei Mate 20 X 5G|HWEVR|Good|
|Huawei HonorV10 / Honor View 10|HWBKL|Good|
|Huawei Enjoy 9 plus|HWJKM-H|Good|
|Huawei Enjoy 9 plus|HWJKM-HM|Good|
|Huawei honor 7A|HWAUM-Q|Good|
|Huawei Honor 9|HWSTF|Good|
|Huawei Mate 10 / Huawei Mate 10 Porsche Design|HWALP|Limited|
|Huawei Mate 10 pro|HWBLA|Good|
|Huawei nova 2s|HWHWI|Limited|
|Huawei nova 2 plus|HWBAC|Limited|
|Huawei nova 2s|HWHWI|Limited|
|Huawei nova 2|HWPIC|Limited|
|Huawei Mate9|HWMHA|Limited|
|Huawei Mate9 Pro|HWLON|Limited|
|Huawei P10|HWVTR|Limited|
|Huawei P10 plus|HWVKY|Limited|
|honor magic|HWNTS|Limited|
|honor V9|HWDUK|Limited|
|Huawei P9 Plus|HWVIE|Limited|
|Huawei P9|HWEVA|Limited|
|Huawei P20 lite|HWANE|Limited|
|Huawei HonorV10 / Honor View 10|HWBKL|Bad|
|Huawei Enjoy 9 plus|HWJKM-H|Bad|
|Huawei Enjoy 9 plus|HWJKM-HM|Bad|
|Huawei Honor 9|HWSTF|Bad|
|Huawei honor 7A|HWAUM-Q|Bad|
|Huawei Mate 10 / Huawei Mate 10 Porsche Design|HWALP|Bad|
|Huawei Mate 10 pro|HWBLA|Bad|
|Huawei nova 2s|HWHWI|Bad|
|Huawei nova 2 plus|HWBAC|Bad|
|Huawei nova 2s|HWHWI|Bad|
|Huawei nova 2|HWPIC|Bad|
|Huawei Mate9|HWMHA|Bad|
|Huawei Mate9 Pro|HWLON|Bad|
|Huawei P10|HWVTR|Bad|
|Huawei P10 plus|HWVKY|Bad|
|honor magic|HWNTS|Bad|
|honor V9|HWDUK|Bad|
|Huawei P9 Plus|HWVIE|Bad|
|Huawei P9|HWEVA|Bad|
|Huawei P20 lite|HWANE|Bad|
|Huawei nova|HWCAN|Bad|
|Huawei nova|HWCAZ|Bad|
|Huawei nova plus|HWMLA|Bad|
|Huawei P10 lite /Nova Youth|HWWAS-H|Bad|
|Honor V8|HWKNT|Bad|
|Honor 8|HWFRD|Bad|
|Honor V8 max / Honor note8|HWEDI|Bad|
|Honor 8X|HWJSN-HM|Limited|
|Huawei Honor 7|HWPLK|Bad|
|Huawei Mate 8|HWNXT|Bad|
|Huawei P20 Pro|HW-01K|Good|
|Huawei P20 Pro|HWCLT|Good|
|Huawei Honor 10|HWCOL|Good|
|Huawei nova 3i|HWINE|Good|
|HUAWEI Y9 2019 /enjoy 8Plus|HWJKM-H|Good|
|HUAWEI Y9 2019 /enjoy 8Plus|HWFLA-H|Good|
|enjoy 9 Plus||Good|
|enjoy 9S||Good|
|HUAWEI Y9s / Y9 2019 Prime 2019 / enjoy 10 Plus|HWSTK-HF|Good|
|HUAWEI enjoy 10 Enjoy 10||Good|
|Huawei Enjoy 10E enjoy 10E|HWMED|Bad|
|Huawei Enjoy 10S enjoy 10S|HWAQM|Bad|
|Huawei Enjoy 10S enjoy 10S|HWAQM-HF|Bad|
|Huawei Enjoy 10S enjoy 10S|HWJSN-H|Good|
|Huawei honor 8X max|HWARE-QC|Good|
|Huawei honor 8X max|HWARE-Q|Good|
|Huawei Mate 20 Pro /Huawei Mate 20 RS|HWLYA|Good|
|Huawei PORSCHE DESIGN HUAWEI Mate RS|HWNEO|Good|
|Huawei nova 3|HWPAR|Good|
|Huawei Mate 20 lite / MAIMANG 7|HWSNE|Good|
|Huawei MAIMANG 9|HWTNN|Bad|
|Huawei MAIMANG 10|TYH612M|Bad|
|Huawei Honor Magic 2|HWTNY|Good|
|Galaxy S8|SC-02J|Good|
|Galaxy S8|SCV36|Good|
|Galaxy S8|dreamqltecan|Good|
|Galaxy S8|dreamqltechn|Good|
|Galaxy S8|dreamqltecmcc|Good|
|Galaxy S8|dreamqltesq|Good|
|Galaxy S8|dreamqlteue|Good|
|Galaxy S8|dreamlte|Good|
|Galaxy S8|dreamlteks|Good|
|Galaxy S8|dreamlteskt|Good|
|Galaxy S8|dreamqlteue|Good|
|Galaxy S8 Lite|dreamliteqltechn|Good|
|Galaxy Note8|SC-01K|Good|
|Galaxy Note8|SCV37|Good|
|Galaxy Note8|greatqlte|Good|
|Galaxy Note8|greatqltechn|Good|
|Galaxy Note8|greatqltecmcc|Good|
|Galaxy Note8|greatqltecs|Good|
|Galaxy Note8|greatqlteue|Good|
|Galaxy Note8|greatlte|Good|
|Galaxy Note8|greatlte|Good|
|Galaxy Note8|greatlteks|Good|
|Galaxy Note8|greatlteks|Good|
|Galaxy Note9|crownqltecmcc|Good|
|Galaxy S8+|SCV35|Good|
|Galaxy S8+|SC-03J|Good|
|Galaxy S8+|dream2qltecan|Good|
|Galaxy S8+|dream2qltechn|Good|
|Galaxy S8+|dream2qltecmcc|Good|
|Galaxy S8+|dream2qltesq|Good|
|Galaxy S8+|dream2qlteue|Good|
|Galaxy S8+|dream2lte|Good|
|Galaxy S8+|dream2lteks|Good|
|Galaxy S8+|dream2lteskt|Good|
|Galaxy S8+|dream2qlteue|Good|
|Galaxy Note10+ 5G|d2xq|Good|
|Galaxy Note10+ 5G|d2xq2|Good|
|Galaxy Note10+ 5G|d2x|Good|
|Galaxy Note10+ 5G|d2xq|Good|
|Galaxy Note10+|d2s|Good|
|Galaxy Note10+|SCV45|Good|
|Galaxy Note10+|SC-01M|Good|
|Galaxy Note10+|d2xq|Good|
|Galaxy Note10 5G|d1x|Good|
|Galaxy Note10|d1q|Good|
|Galaxy Note10|d1|Good|
|Galaxy Note10 Lite|r7|Good|
|Samsung Galaxy Z Flip 5G|bloomxq|Good|
|Samsung Galaxy Z Flip 5G|bloomq|Good|
|Samsung Galaxy Z Flip 3||Good|
|Samsung Galaxy Z Flip 4||Good|
|Samsung Galaxy Z Flip 5||Good|
|Samsung W20 5G|zodiac|Good|
|Samsung W21 5G||Good|
|Samsung W22 5G||Good|
|Samsung W23 5G||Good|
|Samsung W23 Flip||Good|
|Samsung W24 5G||Good|
|Samsung W24 Flip||Good|
|Samsung W25 5G||Good|
|Samsung W25 Flip||Good|
|Samsung Galaxy Tab S6|gts6l|Good|
|Samsung Galaxy Tab S6|gts6lwifi|Good|
|Samsung Galaxy Tab S6 5G|gts6x|Good|
|Samsung Galaxy Tab S6 lite|gta4xl|Good|
|Samsung Galaxy Tab S6 lite|gta4xlwifi|Good|
|Samsung Galaxy F62|f62|Good|
|Samsung Galaxy F22|f22|Good|
|Galaxy S10 5G|beyondxq|Good|
|Galaxy S10 5G|beyondx|Good|
|Galaxy S10|beyond1|Good|
|Galaxy S10|beyond1q|Good|
|Galaxy S10|SCV41|Good|
|Galaxy S10|SC-03L|Good|
|Galaxy S10 lite|r5q|Good|
|Galaxy S10+ Olympic Games Edition|SC-05L|Good|
|Galaxy S10+|beyond2|Good|
|Galaxy S10+|beyond2q|Good|
|Galaxy S10+|SCV42|Good|
|Galaxy S10+|SC-04L|Good|
|Galaxy S10e|beyond0|Good|
|Galaxy S10e|beyond0q|Good|
|Galaxy S20+ / S20+ 5G|y2s|Good|
|Galaxy S20+ / S20+ 5G|y2q|Good|
|Galaxy S20+ / S20+ 5G|SCG02|Good|
|Galaxy S20+ / S20+ 5G|SC-52A|Good|
|Galaxy S20 Ultra / S20 Ultra 5G|z3q|Good|
|Galaxy S20 Ultra / S20 Ultra 5G|SCG03|Good|
|Galaxy S20 Ultra / S20 Ultra 5G|z3s|Good|
|Samsung Galaxy Xcover 5|xcover5|Good|
|Samsung Galaxy Xcover 6 pro|xcoverpro2|Good|
|Samsung Galaxy Z Fold2 5G|f2q|Good|
|Samsung Galaxy S20 FE|r8s|Good|
|Samsung Galaxy S20 FE 2022||Good|
|Samsung Galaxy S20 FE 5G|r8q|Good|
|zhifubao cloud XR|cic\_cloud|Good|
|Galaxy Fold /Fold 5G|winner|Good|
|Galaxy Z Flip3 5G|b2q|Good|
|Galaxy Z Fold2 5G||Good|
|Galaxy Z Flip3 5G|b2q|Good|
|Galaxy Z Fold3 5G|q2q|Good|
|Galaxy Z Flip4 5G|b4q|Good|
|Galaxy Z Fold4 5G|q4q|Good|
|Galaxy Z Fold5 5G|q5q|Good|
|Galaxy Z Fold6 5G|q6q|Good|
|Galaxy Z Fold7 5G|q7q|Good|
|Galaxy Z Flip5 5G|b5q|Good|
|Galaxy Z Flip6 5G|b6q|Good|
|Galaxy Z Flip7 5G|b7q|Good|
|Galaxy Z Flip7 5G|b7s|Good|
|Galaxy Z Flip7 5G|b7r|Good|
|Samsung Galaxy Tab A8 10.5|gta8|Good|
|Samsung Galaxy Tab A8 10.5|gta8wifi|Good|
|Samsung Galaxy Tab A7 10.4 (2020)|gta4l|Good|
|Samsung Galaxy Tab A7 10.4 (2020)|gta4lwifi|Good|
|Samsung Galaxy Tab Active3|gtactive3|Good|
|Samsung Galaxy Tab Active3|gtactive3wifi|Good|
|Galaxy S20 / S20 5G|x1s|Good|
|Galaxy S20 / S20 5G|SC-51A|Good|
|Galaxy S20 / S20 5G|SC51Aa|Good|
|Galaxy S20 / S20 5G|SCG01|Good|
|Galaxy S20 / S20 5G|x1q|Good|
|Galaxy S20 / S20 5G|SCG01|Good|
|Samsung Galaxy Note20|c1s|Good|
|Samsung Galaxy Note20 5G|c1q|Good|
|Samsung Galaxy Note20 Ultra 5G|c2s|Good|
|Samsung Galaxy Note20 Ultra 5G|c2q|Good|
|Samsung Galaxy Note20 Ultra 5G|SCG06|Good|
|Samsung Galaxy S21 5G|o1q|Good|
|Samsung Galaxy S21 5G|o1s|Good|
|Samsung Galaxy S21 5G|SCG09|Good|
|Samsung Galaxy S21 5G|SC-51B|Good|
|Samsung Galaxy S21 Ultra 5G|p3q|Good|
|Samsung Galaxy S21 Ultra 5G|p3s|Good|
|Samsung Galaxy S21 Ultra 5G|SC-52B|Good|
|Samsung Galaxy S21+ 5G|t2q|Good|
|Samsung Galaxy S21+ 5G|t2s|Good|
|Samsung Galaxy S21+ 5G|SCG10|Good|
|Samsung Galaxy S21 FE 5G|r9q|Good|
|Samsung Galaxy S21 FE 5G|r9s|Good|
|Samsung Galaxy S22 5G|r0q|Good|
|Samsung Galaxy S22 5G|r0s|Good|
|Samsung Galaxy S22+ 5G|g0q|Good|
|Samsung Galaxy S22+ 5G|t2s|Good|
|Samsung Galaxy S22+ 5G|g0s|Good|
|Samsung Galaxy S22 Ultra 5G|b0q|Good|
|Samsung Galaxy S22 Ultra 5G|b0s|Good|
|Samsung Galaxy S23|dm1q|Good|
|Samsung Galaxy S23|dm2q|Good|
|Samsung Galaxy S23|dm3q|Good|
|Samsung Galaxy S23|r11q|Good|
|Samsung Galaxy S23 Plus||Good|
|Samsung Galaxy S23 Ultra||Good|
|Samsung Galaxy S23 FE||Good|
|Samsung Galaxy S24|e1q|Good|
|Samsung Galaxy S24 Plus|e2q|Good|
|Samsung Galaxy S24 pro|e3q|Good|
|Samsung Galaxy S25|pa1q|Good|
|Samsung Galaxy S25 Plus|pa2q|Good|
|Samsung Galaxy S25 Edge|psq|Good|
|Samsung Galaxy S25 Ultra|pa3q|Good|
|Samsung Galaxy A6s|Phoenix|Good|
|Samsung Galaxy M62|m62|Good|
|Samsung Galaxy M51|m51|Good|
|Samsung Galaxy A13 5G|a13x|Good|
|Samsung Galaxy A73 5G|a73xq|Good|
|Samsung Galaxy A42 5G|a42xq|Good|
|Samsung Galaxy A42 5G|a42xuq|Good|
|Samsung Galaxy F41 / Galaxy M21s|f41|Good|
|Samsung Galaxy M31 Prime|m31|Good|
|Galaxy A52s 5G||Good|
|Samsung Galaxy A71 /A71 5G|a71|Good|
|Samsung Galaxy A71 /A71 5G|a7x|Good|
|Galaxy A Quantum|a71x|Good|
|Samsung Galaxy A51 /A51 5G|a51|Good|
|Samsung Galaxy A51 /A51 5G|a5x|Good|
|Samsung Galaxy A31|a31|Good|
|Samsung Galaxy A23|a23|Good|
|Samsung Galaxy A41|a41|Good|
|Samsung Galaxy M23|m23xq|Good|
|Samsung Galaxy M21|m21|Good|
|Samsung Galaxy M33|m33x|Good|
|Samsung Galaxy M31|m31|Good|
|Samsung Galaxy M31 5G|a32x|Good|
|Samsung Galaxy M13 5G|a13x|Good|
|Samsung Galaxy Z Flip|SCV47|Good|
|Samsung Galaxy Z Flip|bloomq|Good|
|Samsung Galaxy Xcover Pro|xcoverpro|Good|
|Samsung Galaxy M10s|m10s|Good|
|Samsung Galaxy Tab Active Pro|gtactivexl|Good|
|Samsung Galaxy Tab Active Pro|gtactivexlwifi|Good|
|Samsung Galaxy A33|a33x|Good|
|Samsung Galaxy A30s|a30s|Good|
|Samsung Galaxy M40|m40|Good|
|Samsung Galaxy M42|a42xq|Good|
|Samsung Galaxy M52|m52xq|Good|
|Samsung Galaxy M53|m53xq|Good|
|Samsung Galaxy M53|m53x|Good|
|Samsung Galaxy F42 5G|f42x|Good|
|Samsung Galaxy M30|m30|Good|
|Samsung Galaxy M30s|m30s|Good|
|Samsung Galaxy M31s|m31s|Good|
|Samsung Galaxy M32|m32|Good|
|Samsung Galaxy M32 5G|a32x|Good|
|Galaxy A9s|a9y18qltechn|Good|
|Galaxy A8(2018)|jackpotlte|Good|
|Galaxy A8(2018)|jackpotltecan|Good|
|Galaxy A8(2018)|jackpotlteks|Good|
|Galaxy A8+(2018)|jackpot2lte|Good|
|Samsung Galaxy Tab S7 FE|gts7xllitewifi|Good|
|Samsung Galaxy Tab S7 FE|gts7xllite|Good|
|Samsung Galaxy Tab S7 / Samsung Galaxy Tab S7 5G|gts7l|Good|
|Samsung Galaxy Tab S7 / Samsung Galaxy Tab S7 5G|gts7lwifi|Good|
|Samsung Galaxy Tab S7+ / Galaxy Tab S7+ 5G|gts7xl|Good|
|Samsung Galaxy Tab S7+ / Galaxy Tab S7+ 5G|gts7xlwifi|Good|
|Samsung Galaxy Tab S8|gts8wifi|Good|
|Samsung Galaxy Tab S8|gts8|Good|
|Samsung Galaxy Tab S8+|gts8pwifi|Good|
|Samsung Galaxy Tab S8+|gts8p|Good|
|Samsung Galaxy Tab S8 Ultra|gts8uwifi|Good|
|Samsung Galaxy Tab S8 Ultra|gts8u|Good|
|Samsung Galaxy M20|m20|Good|
|Samsung Galaxy M20|m20lte|Good|
|Samsung Galaxy A80|r1q|Good|
|Samsung Galaxy A42 5G|a42xq|Good|
|Samsung Galaxy A52 5G|a52xq|Good|
|Samsung Galaxy A52||Good|
|Samsung Galaxy A72|a72q|Good|
|Samsung Galaxy A60|a60q|Good|
|Samsung Galaxy A50|a50|Good|
|Samsung Galaxy A40|a40|Good|
|Samsung Galaxy A40s|a30c|Good|
|Samsung Galaxy A30|a30|Good|
|Samsung Galaxy A20e|a20e|Good|
|Samsung Galaxy A20|a20p|Good|
|Samsung Galaxy A20|a20|Good|
|Samsung Galaxy A22|a22|Good|
|Samsung Galaxy A22|a22x|Good|
|Samsung Galaxy A22s|a22x|Good|
|Samsung Galaxy A21s|a21s|Good|
|Samsung Galaxy A21|a21|Good|
|Samsung Galaxy A23 5G|a23xq|Good|
|Samsung Galaxy Tab S5e|gts4lv|Good|
|Samsung Galaxy Tab S5e|gts4lvwifi|Good|
|Samsung Galaxy Tab S5e|gts4lvwifichn|Good|
|Samsung Galaxy A8s|a8sqlte|Good|
|Samsung Galaxy A8s|a8sqltechn|Good|
|Samsung Galaxy A9 (2018)|a9y18qlte|Good|
|Samsung Galaxy A9 (2018)|a9y18qltekx|Good|
|Samsung Galaxy A9 (2018)|a9y18qltechn|Good|
|Samsung Galaxy A8+ (2018)|jackpot2lte|Good|
|Samsung Galaxy C7|c7ltechn|Good|
|Samsung Galaxy C7|c7proltechn|Good|
|Samsung Galaxy C7 Pro|c7prolte|Good|
|Samsung Galaxy C7 Pro|c7proltechn|Good|
|Samsung Galaxy C8|jadeltechn|Good|
|Samsung Galaxy C8|jadeltecmcc|Good|
|Samsung Galaxy C9 Pro|c9lte|Good|
|Samsung Galaxy C9 Pro|c9ltechn|Good|
|Samsung Galaxy C7 Pro|c7prolte|Good|
|Samsung Galaxy C7 Pro|c7proltechn|Good|
|Samsung Galaxy C55|m55xq|Good|
|Samsung Galaxy A51 5G UW|a51xq|Limited|
|Samsung Galaxy A51 5G UW|a51x|Limited|
|Samsung Galaxy A53 5G|a53x|Good|
|Samsung Galaxy A55 5G||Good|
|Samsung Galaxy A56 5G||Good|
|Samsung Galaxy A54 5G||Good|
|Samsung Galaxy F52 5G|f52x|Good|
|Samsung Galaxy A20s|a20s|Good|
|Samsung Galaxy A50s|a50s|Limited|
|Galaxy A90 5G|r3q|Good|
|Samsung Galaxy A8s|a8sqlte|Good|
|Samsung Galaxy A8s|a8sqltechn|Good|
|Samsung Galaxy A70|a70q|Limited|
|Samsung Galaxy A70s|a70s|Limited|
|Samsung Galaxy Quantum2|a82xq|Limited|
|Samsung Galaxy A9 star|astarqltechn|Bad|
|Samsung Galaxy A9 star|astarqltecmcc|Bad|
|Samsung Galaxy A9 star Lite|a6pltechn|Bad|
|Samsung Galaxy A9 star Lite|a6pltecmcc|Bad|
|Samsung Galaxy A7 (2018)|a7y18lte|Bad|
|Samsung Galaxy A7 (2018)|a7y18lteks|Bad|
|Galaxy S7|herolte|Good|
|Galaxy S7|heroltebmc|Good|
|Galaxy S7|heroltektt|Good|
|Galaxy S7|heroltelgt|Good|
|Galaxy S7|herolteskt|Good|
|Galaxy S7|heroqlteacg|Good|
|Galaxy S7|heroqlteaio|Good|
|Galaxy S7|heroqlteatt|Good|
|Galaxy S7|heroqltecctvzw|Good|
|Galaxy S7|heroqltechn|Good|
|Galaxy S7|heroqltelra|Good|
|Galaxy S7|heroqltemtr|Good|
|Galaxy S7|heroqltechn|Good|
|Galaxy S7|heroqltespr|Good|
|Galaxy S7|heroqltetfnvzw|Good|
|Galaxy S7|heroqltetmo|Good|
|Galaxy S7|heroqlteue|Good|
|Galaxy S7|heroqlteusc|Good|
|Galaxy S7|heroqltevzw|Good|
|Galaxy S7 Edge|SC-02H|Good|
|Galaxy S7 Edge|SCV33|Good|
|Galaxy S7 Edge|hero2qlteatt|Good|
|Galaxy S7 Edge|hero2qltecctvzw|Good|
|Galaxy S7 Edge|hero2qltechn|Good|
|Galaxy S7 Edge|hero2qltespr|Good|
|Galaxy S7 Edge|hero2qltetmo|Good|
|Galaxy S7 Edge|hero2qlteue|Good|
|Galaxy S7 Edge|hero2qlteusc|Good|
|Galaxy S7 Edge|hero2qltevzw|Good|
|Galaxy S7 Edge|hero2lte|Good|
|Galaxy S7 Edge|hero2ltebmc|Good|
|Galaxy S7 Edge|hero2ltektt|Good|
|Galaxy S7 Edge|hero2ltelgt|Good|
|Galaxy S7 Edge|hero2lteskt|Good|
|Galaxy S7 Edge|herolte|Good|
|Galaxy S7 Edge|heroltebmc|Good|
|Galaxy S7 Edge|heroltektt|Good|
|Galaxy S7 Edge|herolteskt|Good|
|Galaxy S7 Edge|heroqlteacg|Good|
|Galaxy S7 Edge|heroqlteaio|Good|
|Galaxy S7 Edge|heroqlteatt|Good|
|Galaxy S7 Edge|heroqltecctvzw|Good|
|Galaxy S7 Edge|heroqltechn|Good|
|Galaxy S7 Edge|heroqltelra|Good|
|Galaxy S7 Edge|heroqltemtr|Good|
|Galaxy S7 Edge|heroqltespr|Good|
|Galaxy S7 Edge|heroqltetfnvzw|Good|
|Galaxy S7 Edge|heroqltetmo|Good|
|Galaxy S7 Edge|heroqlteue|Good|
|Galaxy S7 Edge|heroqlteusc|Good|
|Galaxy S7 Edge|heroqltevzw|Good|
|Galaxy Note9|SC-01L|Good|
|Galaxy Note9|SCV40|Good|
|Galaxy Note9|SCV40\_jp\_kdi|Good|
|Galaxy Note9|SM-N960D|Good|
|Galaxy Note9|SM-N960J|Good|
|Galaxy Note9|crownqltechn|Good|
|Galaxy Note9|crownqltecmcc|Good|
|Galaxy Note9|crownqltecs|Good|
|Galaxy Note9|crownqltesq|Good|
|Galaxy Note9|crownqlteue|Good|
|Galaxy Note9|crownlte|Good|
|Galaxy Note9|crownlteks|Good|
|Galaxy S9|SC-02K|Good|
|Galaxy S9|SCV38|Good|
|Galaxy S9|starqltechn|Good|
|Galaxy S9|starqltecmcc|Good|
|Galaxy S9|starqltecs|Good|
|Galaxy S9|starqltesq|Good|
|Galaxy S9|starqlteue|Good|
|Galaxy S9 +|SC-03K|Good|
|Galaxy S9 +|SCV39|Good|
|Galaxy S9 +|star2qltechn|Good|
|Galaxy S9 +|star2qltecs|Good|
|Galaxy S9 +|star2qltesq|Good|
|Galaxy S9 +|star2qlteue|Good|
|Galaxy S9 +|star2lte|Good|
|Galaxy S9 +|star2lteks|Good|
|Galaxy S9 +|starlte|Good|
|Galaxy S9 +|starlteks|Good|
|Galaxy A5(2017)|a5y17lte|Good|
|Galaxy A5(2017)|a5y17ltecan|Good|
|Galaxy A5(2017)|a5y17ltektt|Good|
|Galaxy A5(2017)|a5y17ltelgt|Good|
|Galaxy A5(2017)|a5y17lteskt|Good|
|Galaxy A7(2017)|a7y17lte|Good|
|Galaxy A7(2017)|a7y17lteskt|Good|
|Galaxy Tab S4|gts4llte|Good|
|Galaxy Tab S4|gts4llteatt|Good|
|Galaxy Tab S4|gts4lltechn|Good|
|Galaxy Tab S4|gts4lltekx|Good|
|Galaxy Tab S4|gts4lltespr|Good|
|Galaxy Tab S4|gts4lltetmo|Good|
|Galaxy Tab S4|gts4llteusc|Good|
|Galaxy Tab S4|gts4lltevzw|Good|
|Galaxy Tab S4|gts4lwifi|Good|
|Galaxy Tab S4|gts4lwifichn|Good|
|Galaxy J5|j5y17lte|Good|
|Galaxy J5|j5y17ltedx|Good|
|Galaxy J5|j5y17ltektt|Good|
|Galaxy J5|j5y17ltelgt|Good|
|Galaxy J5|j5y17lteskt|Good|
|Galaxy J5|j5y17ltextc|Good|
|ZTE Axon 10 pro 5G|P855A21|Good|
|ZTE Axon 10 pro|P855A01|Good|
|ZTE Axon 10 pro|P855A02|Good|
|ZTE Axon 10 pro|P855A03|Good|
|ZTE Axon 10 pro|P855A03\_NA|Good|
|ZTE Axon 10s pro 5G|P865A02|Good|
|ZTE nubia Play|NX651J|Good|
|ZTE Axon 11|P671A13|Good|
|ZTE Axon 11|P671A11|Good|
|ZTE Axon 11 5G|P725A12|Good|
|ZTE Axon 11 5G|P725A11|Good|
|ZTE Axon 9 Pro|P845A01|Good|
|ZTE Axon 9 Pro|P845A02|Good|
|ZTE Axon 20 5G / Axon 20 5G Extreme|P725A02|Good|
|ZTE Axon 40||Good|
|ZTE Axon 40 Ultra||Good|
|ZTE Axon 40 Pro||Good|
|ZTE S30 SE|P633S01|Good|
|ZTE S30|P653S07|Good|
|ZTE S30 Pro|P768A02|Good|
|ZTE nubia Z20|NX627J|Good|
|ZTE nubia Z20|NX627J-EEA|Good|
|ZTE nubia Z30 Pro||Good|
|ZTE nubia Z40 Pro||Good|
|ZTE nubia||Good|
|ZTE nubia X|NX616J|Good|
|ZTE Blade X1 5G|Z6750|Good|
|ZTE Blade 11 Prime||Good|
|ZTE Red Magic 6 Pro||Good|
|ZTE Red Magic 6||Good|
|ZTE Red Magic 6s / Red Magic 6s Pro|NX669J-S|Good|
|ZTE Red Magic 6s / Red Magic 6s Pro|NX669J-EEA|Good|
|ZTE Red Magic 6s / Red Magic 6s Pro|NX669J-UN|Good|
|ZTE Red Magic 7|NX679J-EEA|Good|
|ZTE Red Magic 7 pro|NX709J-EEA|Good|
|ZTE Red Magic 7s||Good|
|ZTE Red Magic 7s pro||Good|
|ZTE Red Magic 9s pro||Good|
|ZTE Voyage 20 Pro|P653S11|Good|
|ZTE Red Magic 6R||Good|
|ZTE Blade V40||Good|
|ZTE Blade V30|P618F05|Good|
|ZTE Blade V30 vita|P963F06|Good|
|ZTE Blade V30 vita|P963F06\_A|Good|
|ZTE Blade 20 5G|P653S06|Good|
|ZTE Blade V10|P671F20|Good|
|ZTE Blade V10 Vita|P963F01|Good|
|ZTE Blade V10 Vita RU|P963F01D|Good|
|ZTE Axon 30 / 30 Pro 5G|P875A02|Good|
|ZTE Axon 30 / 30 Pro 5G|P875A12|Good|
|ZTE Axon 30 / 30 Pro 5G|P870A01|Good|
|ZTE Axon 30 Ultra|P875A11|Good|
|ZTE nubia Red Magic 5G|NX659J-EEA|Good|
|ZTE nubia Red Magic 5G|NX659J-RU|Good|
|ZTE nubia Red Magic 5G|NX659J-UN|Good|
|ZTE nubia Red Magic 5s|NX659J|Good|
|ZTE Red Magic 5G lite|NX651J-EEA|Good|
|ZTE nubia Red Magic mars rng /Red Magic mars|NX619J|Good|
|ZTE nubia Red Magic mars rng /Red Magic mars|NX619J-EEA|Good|
|ZTE nubia Red Magic 3s|NX629J\_V1S|Good|
|ZTE nubia Red Magic 3|NX629J|Good|
|ZTE nubia Red Magic 3|NX629J-EEA|Good|
|ZTE Blade V9|P450L10|Bad|
|ZTE Blade V9|P840F03|Bad|
|ZTE Blade V9|P450F10|Bad|
|ZTE Axon 7|ailsa\_ii|Bad|
|ZTE nubia Z17 mini|NX569J|Bad|
|ZTE nubia Z17|NX563J|Bad|
|ZTE nubia Z17s|NX595J|Bad|
|ZTE nubia Z17 lite|NX591J|Bad|
|ZTE nubia Z17 miniS|NX589J|Bad|
|ZTE nubia Z11 mini|NX529J|Bad|
|ZTE nubia M2|NX551J|Bad|
|ZTE nubia Z9 Max|NX510J|Bad|
|ZTE nubia Z9 Max|NX518J|Bad|
|ZTE nubia Z18 mini|NX611J|Bad|
|ZTE nubia Z11 mini S|NX549J|Bad|
|ZTE Blade V8|ZTE\_BLADE\_V0800|Bad|
|ZTE Blade V8 mini|ZTE\_BLADE\_V0850|Bad|
|ZTE Blade V8 Lite / Blade V8 SE|ZTE\_BLADE\_V0820|Bad|
|ZTE nubia Z50|PQ82A01|Good|
|ZTE nubia z50 ultra||Good|
|ZTE nubia z60||Good|
|ZTE nubia z60 pro||Good|
|ZTE nubia Hongmo9||Good|
|OPPO Reno|OP47DD|Good|
|OPPO Reno|OP47DDL1|Good|
|OPPO Reno|OP46B1|Good|
|OPPO Reno 10X|OP4847L1|Good|
|OPPO Reno 10X|OP4845|Good|
|OPPO Reno 10X|OP4845L1|Good|
|OPPO Reno 10X|OP4847|Good|
|OPPO Reno 10X|OP46C3|Good|
|OPPO Reno A|OP47CFL1|Good|
|OPPO realme X|RMX1901CN|Good|
|OPPO realme Pad||Good|
|OPPO realme X3|RMX2081L1|Good|
|OPPO realme X3|RMX2083L1|Good|
|OPPO realme X3|RMX2085L1|Good|
|OPPO realme X3 SuperZoom|RMX2086L1|Good|
|OPPO realme X2 pro|RMX1931CN|Good|
|OPPO realme X2 pro|RMX1931L1|Good|
|OPPO realme XT|RMX1921|Good|
|OPPO realme XT|RMX1921L1|Good|
|OPPO realme XT|RMX1922|Good|
|oppo Realme 6|RMX2001L1|Good|
|oppo Realme 6|RMX2003L1|Good|
|oppo Realme 6s / Realme Narzo|RMX2002L1|Good|
|oppo Realme 7 Pro|RMX2170L1|Good|
|oppo Realme 7|RMX2151|Good|
|oppo Realme 7 5G|RMX2111L1|Good|
|oppo Realme 7i / Realme Narzo 20|RE50C1|Good|
|oppo Realme 6 pro|RMX2061L1|Good|
|oppo Realme 6 pro|RMX2063L1|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2040|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2030|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2041|Good|
|oppo Realme 6i / Realme Narzo 10|RMX2042|Good|
|oppo Realme 3 pro|RMX1851|Good|
|oppo Realme Narzo 10A|RMX2020|Good|
|oppo Realme Narzo 20A|RMX2050|Good|
|oppo Realme Narzo 20 Pro||Good|
|oppo Realme Narzo 30|RMX2156L1|Good|
|oppo Realme Narzo 30A|RMX3171|Good|
|oppo Realme Narzo 30 5G|RE513CL1|Good|
|oppo Realme Narzo 30 Pro 5G / Realme Q2|RMX2117L1|Good|
|oppo Realme Narzo 50|RMX3286|Good|
|oppo Realme Narzo 50A|RMX3430|Good|
|oppo Realme Narzo 50i|RMX3235|Good|
|oppo Realme GT 5G|RMX2202L1|Good|
|oppo Realme 9||Good|
|oppo Realme 9 speed||Good|
|oppo Realme GT Neo Flash|RE5469|Good|
|oppo Realme GT Master||Good|
|oppo Realme GT Master Explorer||Good|
|oppo Realme GT Neo2||Good|
|oppo Realme GT Neo2T||Good|
|oppo Realme GT 2||Good|
|oppo Realme 10||Good|
|oppo Realme 10s||Good|
|oppo Realme 10 Pro||Good|
|oppo Realme 10 Pro Plus||Good|
|oppo Realme 11||Good|
|oppo Realme 11 Pro||Good|
|oppo Realme 11 Pro Plus||Good|
|oppo Realme 12 Pro||Good|
|oppo Realme 12 Pro Plus||Good|
|oppo Realme 12||Good|
|oppo Realme 12X||Good|
|oppo Realme 13||Good|
|oppo Realme 13 Pro||Good|
|oppo Realme 13 Pro+||Good|
|oppo Realme 14||Good|
|oppo Realme 14 Pro||Good|
|oppo Realme 14 Pro Plus||Good|
|oppo Realme 15||Good|
|oppo Realme 15 Pro||Good|
|oppo Realme 15T||Good|
|OPPO realme V3||Good|
|OPPO realme V5||Good|
|OPPO realme V11||Good|
|OPPO realme V15||Good|
|OPPO realme V20||Good|
|OPPO realme V23i||Good|
|OPPO realme V30||Good|
|OPPO realme V30T||Good|
|OPPO realme V50||Good|
|OPPO realme V50S||Good|
|OPPO realme V60||Good|
|OPPO realme V60S||Good|
|OPPO realme V60 Pro||Good|
|OPPO realme V70||Good|
|OPPO realme V70S||Good|
|OPPO Reno ACE|OP4A89|Good|
|OPPO Reno ACE2|OP4AD9|Good|
|OPPO Reno Z|OP48A1|Good|
|OPPO Reno Z|OP48A1L1|Good|
|OPPO Reno Z|OP4699|Good|
|OPPO Reno 5G|OP46C7|Good|
|oppo Find X /Find X Lamborghini||Good|
|OPPO Reno 2|OP4B83L1|Good|
|OPPO Reno 2|OP4A57|Good|
|OPPO Reno 2 F||Good|
|OPPO Reno 2 Z|OP4B65L1|Good|
|OPPO Reno 2 Z|OP4A43|Good|
|OPPO Reno 3|OP4B9EL1|Good|
|OPPO Reno 3 5G china|OP4ADD|Good|
|OPPO Reno 3 A|OP4BAFL1|Good|
|OPPO F21 Pro||Good|
|OPPO F19||Good|
|OPPO F19 pro|OP4F43L1|Good|
|OPPO F19 pro+||Good|
|OPPO F19s||Good|
|OPPO F17 pro|OP4C51L1|Good|
|OPPO F17||Good|
|OPPO Reno 3 Youth 5G|OP4AB5|Good|
|OPPO Reno 3 Pro 5G china|OP4A9D|Good|
|OPPO Reno 3 Pro|OP4C5FL1|Good|
|OPPO Reno 3 Pro|OP4C2DL1|Good|
|OPPO Reno 4||Good|
|OPPO Reno 4F||Good|
|OPPO Reno 4Z||Good|
|OPPO Reno 4Lite||Good|
|OPPO Reno 4SE||Good|
|OPPO Reno 4 pro||Good|
|OPPO Reno 5 pro||Good|
|OPPO Reno 5 pro+|OP4EA7|Good|
|OPPO Reno 5 4G & 5G|OP4EA3|Good|
|OPPO Reno 5 4G & 5G|OP4F0BL1|Good|
|OPPO Reno 5 4G & 5G|OP4F1FL1|Good|
|OPPO Reno 5 4G & 5G|OP4F25L1|Good|
|OPPO Reno 5|OP4F1BL1|Good|
|OPPO Reno 5|OP4E8F|Good|
|OPPO Reno 5A|OP4F2BL1|Good|
|OPPO Reno 5F/5Lite|OP4F43L1|Good|
|OPPO Reno 5Z|OP4F4DL1|Good|
|OPPO Reno 5Z|OP4EB7|Good|
|OPPO Reno 5K|OP4E59|Good|
|OPPO Reno 6||Good|
|OPPO Reno 6 Pro||Good|
|OPPO Reno 6 Pro+|OP4EC1|Limited|
|OPPO Reno 6Z||Good|
|OPPO pad||Good|
|OPPO Reno 7SE||Good|
|OPPO Reno 7||Good|
|OPPO Reno 7 Pro|OP52E1L1|Good|
|OPPO Reno 7 Z 5G||Good|
|OPPO Pad Air||Good|
|OPPO Reno 8||Good|
|OPPO Reno 8 Pro||Good|
|OPPO Reno 8 Pro+||Good|
|OPPO Reno 9||Good|
|OPPO Reno 9 Pro||Good|
|OPPO Reno 9 Pro Plus||Good|
|OPPO Reno 10||Good|
|OPPO Reno 11||Good|
|OPPO Reno 11 Pro||Good|
|OPPO Reno 12||Good|
|OPPO Reno 12 Pro||Good|
|OPPO Reno 13||Good|
|OPPO Reno 13 Pro||Good|
|OPPO Reno 14||Good|
|OPPO Reno 14 Pro||Good|
|OPPO A72 5G||Good|
|OPPO A72|OP4C72L1|Good|
|OPPO A12 /A11k||Good|
|OPPO A53 5G|OP4F53L1|Good|
|OPPO A1 Pro|OP5613|Limited|
|OPPO A5 Pro||Good|
|OPPO A93s||Good|
|OPPO A93|OP4C51L1|Good|
|OPPO A95 5G||Good|
|OPPO A95/Reno 6Lite||Good|
|OPPO A96||Good|
|OPPO A97||Good|
|OPPO A56/A56s||Good|
|OPPO A55/A55s||Good|
|OPPO A52|OP4C77L1|Good|
|OPPO A52|OP4C7BL1|Good|
|OPPO A52|OP4AE7|Good|
|OPPO A58|OP526D|Good|
|OPPO A92s|OP4ABB|Good|
|OPPO A91|OP4ACF|Good|
|OPPO A74 5G||Good|
|OPPO A74||Good|
|OPPO A12||Good|
|OPPO A31||Good|
|OPPO A35|OP4E7B|Good|
|OPPO A9X|PCEM00|Good|
|OPPO K5|OP4AA7|Good|
|OPPO K3|OP4679|Good|
|OPPO K3|OP486B|Good|
|OPPO K1|PBCM30|Good|
|OPPO realme X youth|RMX1851CN|Good|
|OPPO realme Q|RMX1971CN|Good|
|OPPO realme C11 2021|RMX3231|Good|
|OPPO realme V5 5G|RMX2111CN|Good|
|OPPO realme V5 5G|RMX2112CN|Good|
|OPPO realme V23|RE5487|Good|
|OPPO realme U1|RMX1831|Good|
|OPPO realme U1|RMX1833|Good|
|OPPO realme V25|RE547D|Good|
|OPPO realme V25 Pro ??|RMX3143|Good|
|OPPO realme Q3???|RMX3142|Good|
|oppo Realme V13|RE5081|Good|
|oppo Realme Q3i||Good|
|oppo Realme Q3 Pro Carnival Edition|RE811C|Good|
|oppo Realme C35|RMX3511|Good|
|OPPO A5 2020||Good|
|OPPO A9 2020|OP4B80L1|Good|
|OPPO A9 2020|OP46F1|Good|
|OPPO A7X|PBBM00|Good|
|OPPO A7X|PBBT00|Good|
|OPPO A8|PDBM00|Bad|
|OPPO A8|PDBT00|Bad|
|OPPO K7X||Good|
|OPPO K9x|OPD2A0|Good|
|OPPO K9 5G|OP4E9F|Good|
|OPPO K9s||Good|
|OPPO K9 Pro|OP5245|Limited|
|OPPO K9 Pro|PEYM00|Limited|
|OPPO K10||Good|
|OPPO K10 Pro||Good|
|OPPO K11x||Good|
|OPPO K12X||Good|
|OPPO K12||Good|
|OPPO K12 Plus||Good|
|OPPO K12S||Good|
|OPPO K13||Good|
|OPPO K13 Turbo||Good|
|OPPO A11|A11|Bad|
|OPPO A11|OP4A4D|Bad|
|OPPO A11|A11w|Bad|
|OPPO A11|OP4A4D|Bad|
|OPPO A11X|A11|Good|
|OPPO A11X|OP4A54|Good|
|OPPO A3|PADM00|Good|
|OPPO A2||Good|
|OPPO A2 Pro||Good|
|OPPO A2m||Good|
|OPPO A2x||Good|
|OPPO A3|CPH1837|Good|
|OPPO A3m||Good|
|OPPO A3x||Good|
|OPPO A3i||Good|
|OPPO A3 Pro||Good|
|OPPO A3s|CPH1803|Good|
|OPPO A3s|CPH1853|Good|
|OPPO A5x||Good|
|OPPO A5||Good|
|OPPO A1||Good|
|oppo Find X2|OP4BA1L1|Good|
|oppo Find X2|OP4A77|Good|
|oppo Find X2 lite|OP4C41L1|Good|
|oppo Find X2 Neo|OP4C2DL1|Good|
|oppo Find X2 pro / X2 pro Lamborghini|OP4BA2L1|Good|
|oppo Find X2 pro / X2 pro Lamborghini|OP4A7A|Good|
|OPPO Find X3 lite||Good|
|OPPO Find X3 neo||Good|
|OPPO Find X3|OP4E5D|Good|
|OPPO Find N||Good|
|OPPO Find N2||Good|
|OPPO Find N3||Good|
|OPPO Find N5||Good|
|OPPO F11 pro|OP4863|Good|
|OPPO F15||Good|
|OPPO Find X3 pro|OP4F57L1|Good|
|OPPO Find X3 pro|OP4E3F|Good|
|OPPO Find X5|PFFM10|Good|
|OPPO Find X5 lite||Good|
|OPPO Find X5 pro||Good|
|OPPO Find X6||Good|
|OPPO Find X6 Pro||Good|
|OPPO Find X7|OP5661FL1|Good|
|OPPO Find X7 Ultra|OP565FL1|Good|
|OPPO Find X8||Good|
|OPPO Find X8S||Good|
|OPPO Find X8S plus||Good|
|OPPO Find X8 Ultra||Good|
|OPPO realme X2|RMX1991CN|Good|
|OPPO realme X2|RMX1992L1|Good|
|OPPO realme X2|RMX1993L1|Good|
|realme V3|RMX2200CN|Good|
|OPPO realme X50 5G|RMX2025CN|Good|
|OPPO realme X50 5G|RMX2051CN|Good|
|OPPO realme X50 5G|RMX2144L1|Good|
|OPPO realme X50 5G|RE5477|Good|
|OPPO realme X50m 5G|RE508C|Good|
|OPPO realme X50m 5G|RMX2141CN|Good|
|OPPO realme X50m 5G|RMX2142CN|Good|
|OPPO realme X50t 5G|RE508C|Good|
|OPPO realme X50t 5G|RMX2142CN|Good|
|OPPO realme 8 pro|RMX3081L1|Good|
|OPPO realme 8|RMX3085L1|Good|
|OPPO realme 8i||Good|
|OPPO realme 8S||Good|
|OPPO realme 8 5G||Good|
|OPPO realme 9 pro|RMX3471|Good|
|OPPO realme 9 pro+|RMX3392|Good|
|OPPO realme X7 5G|RMX3092L1|Limited|
|OPPO realme X7 5G|RMX2176CN|Limited|
|OPPO realme X7 pro|RMX2121CN|Limited|
|OPPO realme X7 pro|RMX3115|Limited|
|OPPO realme X7 pro|RMX3115|Good|
|OPPO realme X7 Max 5G|RMX3031L1|Good|
|OPPO realme X7 pro Ultra|RMX3116CN|Good|
|OPPO realme X7 pro Ultra|RMX3115CN|Good|
|OPPO realme gt neo5|RMX3706|Good|
|OPPO realme gt neo5|RMX3708|Good|
|OPPO realme gt neo5|RMX3700|Limited|
|OPPO realme neo7||Good|
|OPPO realme neo7 Turbo||Good|
|OPPO realme neo7x||Good|
|OPPO realme X50 pro 5G|RMX2076L1|Good|
|OPPO realme X50 pro 5G|RMX2071CN|Good|
|OPPO realme X50 pro 5G|RMX2075L1|Good|
|OPPO realme X50 pro Play|RMX2072CN|Good|
|OPPO realme 5 / 5s|RMX1911L1|Good|
|OPPO realme 5 / 5s|RMX1911|Good|
|OPPO realme 5 / 5s|RMX1915|Good|
|OPPO realme 5 / 5s|RMX1919|Good|
|OPPO realme 5 / 5s|RMX1925|Good|
|OPPO realme 5 / 5s|RMX1926|Good|
|OPPO realme 5i|RMX2030|Good|
|OPPO realme 5 Pro|RMX1971|Good|
|OPPO realme 5 Pro|RMX1973|Good|
|OPPO realme 5 Pro|RMX1971L1|Good|
|OPPO realme V11 5G|RMX3121CN|Good|
|OPPO realme V11 5G|RMX3122CN|Good|
|OPPO realme V15 5G|RMX3092CN|Good|
|OPPO realme V15 5G|RMX3093CN|Good|
|oppo Realme Narzo 30 Pro|RMX3161|Good|
|oppo Realme GT Neo|RMX3031CN|Limited|
|oppo Realme Q2||Good|
|oppo Realme Q2 Pro||Good|
|oppo Realme Q3 5G|RMX3161CN|Good|
|oppo Realme Q3s|RE548B|Good|
|oppo Realme Q3s|RE548BL1|Good|
|oppo Realme Q3 Pro 5G|RMX2205CN|Good|
|oppo Realme Q5||Good|
|oppo Realme Q5 Pro 5G/Realme GT Neo 3T||Good|
|oppo Realme GT2|RE5471|Good|
|oppo Realme GT2|RE58B2L1|Good|
|oppo Realme GT2|RE5465|Good|
|oppo Realme GT2 Pro||Good|
|oppo Realme GT Neo3||Good|
|oppo Realme GT Neo5||Good|
|oppo Realme GT Neo5SE||Good|
|oppo Realme GT Neo6||Good|
|oppo Realme GT Neo6SE||Good|
|oppo Realme GT 5||Good|
|oppo Realme GT 5 Pro||Good|
|oppo Realme GT 6||Good|
|oppo Realme GT 7 Pro||Good|
|oppo Realme GT 7 SE||Good|
|oppo Realme GT 7||Good|
|OPPO R17 Pro / RX17 Pro|PBDM00|Good|
|OPPO R17 Pro / RX17 Pro|PBDT00|Good|
|OPPO R17 Pro / RX17 Pro|CPH1877|Good|
|OPPO R17|CPH1879|Good|
|OPPO R17|PBEM00|Good|
|OPPO R17|PBET00|Good|
|OPPO R17 NEO / OPPO AX7 pro|CPH1893|Good|
|OPPO R15|PACT00|Bad|
|OPPO R15|PACM00|Bad|
|OPPO R15|PAAM00|Bad|
|OPPO R15|PAAT00|Bad|
|OPPO R15|CPH1835|Bad|
|OPPO R15X|PBCM10|Bad|
|OPPO R15X|PBCT10|Bad|
|OPPO R15 pro|CPH1831|Bad|
|OPPO R15 pro|CPH1833|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11Plus|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11sPlus|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11Plusk|Bad|
|OPPO R11 /R11Plus/R11Pluskt/R11Plusk/R11s/R11splus|R11s|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|R9|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|R9Plus|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|R9PlusA|Bad|
|OPPO R9m /R9Plus/R9PlusA/R9tm/R9t|X9079|Bad|
|OPPO R9s/R9sPlus/R9sk|R9s|Bad|
|OPPO R9s/R9sPlus/R9sk|R9sPlus|Bad|
|OPPO R9s/R9sPlus/R9sk|CPH1611|Bad|
|OPPO R9s/R9sPlus/R9sk|R9sk|Bad|
|OPPO R9s/R9sPlus/R9sk|CPH1607|Bad|
|OPPO A59s|A59|Bad|
|vivo IQOO Pro 5G|PD1916|Good|
|vivo IQOO Pro 5G|PD1916F|Good|
|vivo IQOO|PD1824|Good|
|vivo IQOO|PD1824BA|Good|
|vivo IQOO|V1824BA|Good|
|vivo IQOO|V1824A|Good|
|vivo IQOO Neo|PD1936|Good|
|vivo IQOO Neo|PD1936F|Good|
|vivo IQOO Neo|PD1914|Good|
|vivo IQOO Neo|PD1914F|Good|
|vivo IQOO Pro|PD1922|Good|
|vivo IQOO Pro|PD1922F|Good|
|vivo IQOO 3|PD1955F|Good|
|vivo iQOO Neo3|PD1981|Good|
|vivo iQOO Neo3|PD1981F|Good|
|vivo IQOO 3 5G|I1928|Good|
|vivo IQOO 3 5G|I1927|Good|
|vivo IQOO 3 5G|PD1955|Good|
|vivo IQOO 3 PRO 5G|PD2024|Good|
|vivo IQOO 5 5G|PD2024F|Good|
|vivo IQOO 5 5G|PD2024|Good|
|vivo IQOO 5 pro|PD2025F|Good|
|vivo IQOO 5 pro|PD2025|Good|
|vivo IQOO 8 Pro|PD2141|Good|
|vivo IQOO 8|PD2136|Good|
|vivo IQOO 9|PD2171|Good|
|vivo IQOO 9 Pro|PD2172|Good|
|vivo IQOO 9 SE|2019|Good|
|vivo IQOO 9T|I2201|Good|
|vivo IQOO 10|PD2217|Good|
|vivo IQOO 10 Pro|PD2218|Good|
|vivo IQOO 12 Pro||Good|
|vivo IQOO 12||Good|
|vivo IQOO 13||Good|
|vivo IQOO 7||Good|
|vivo IQOO 11|PD2243|Good|
|vivo IQOO 11 Pro|PD2254|Good|
|vivo IQOO 11S|PD2304|Good|
|vivo IQOO neo5||Good|
|vivo IQOO neo5 Lite|PD2118|Good|
|vivo IQOO neo5 SE|PD2157|Good|
|vivo s10E|PD2130|Good|
|vivo s10|PD2121|Good|
|vivo s12|PD2162|Good|
|vivo s12|PD2163|Good|
|vivo S10||Good|
|vivo S10 Pro||Good|
|vivo S15||Good|
|vivo S15 Pro||Good|
|vivo s15|PD2203|Good|
|vivo s15|PD2207|Good|
|vivo s15|PD2190|Good|
|vivo s16|PD2244|Good|
|vivo s16|PD2245|Good|
|vivo s16|PD2239|Good|
|vivo s16 pro||Good|
|vivo S17|PD2283|Good|
|vivo S17T|PD2282|Good|
|vivo S17 Pro|PD2284|Good|
|vivo S17E|PD2285|Good|
|vivo S18||Good|
|vivo S18 Pro||Good|
|vivo S18E||Good|
|vivo S19||Good|
|vivo S19 Pro||Good|
|vivo S20||Good|
|vivo S20 Pro||Good|
|vivo S30||Good|
|vivo S30 Pro Mini||Good|
|vivo S12||Good|
|vivo S12 Pro||Good|
|vivo IQOO neo5s|PD2154|Limited|
|vivo IQOO neo6|PD2196|Good|
|vivo IQOO neo6 SE Neo 6 SE|PD2199|Good|
|vivo IQOO neo7|PD2231|Good|
|vivo IQOO neo7|PD2232|Good|
|vivo IQOO neo7|PD2238|Good|
|vivo IQOO neo8|PD2301|Good|
|vivo IQOO neo8|PD2302|Good|
|vivo IQOO neo9||Good|
|vivo IQOO neo9S||Good|
|vivo IQOO neo9 Pro||Good|
|vivo IQOO neo9S Pro Plus||Good|
|vivo IQOO neo10 pro||Good|
|vivo IQOO neo10||Good|
|vivo IQOO neo10 pro plus||Good|
|vivo T1 Pro|PD2123|Good|
|vivo T1|PD2115|Good|
|vivo T2||Good|
|vivo X70|PD2133|Good|
|vivo X70|PD2132|Good|
|vivo X70 Pro|PD2134|Good|
|vivo X70 Pro+|PD2145|Good|
|vivo X70 Pro+|PD2114|Good|
|vivo X fold 5||Good|
|vivo X fold|PD2178|Good|
|vivo X note|PD2170|Good|
|vivo X80||Good|
|vivo X80 Pro+||Good|
|vivo X80 Pro|PD2186|Good|
|vivo iqoo z6|PD2220|Good|
|vivo iqoo z6|PD2164U|Good|
|vivo X90|PD2241|Good|
|vivo X90|PD2242|Good|
|vivo X90|PD2227|Good|
|vivo X90S|PD2241|Good|
|vivo X100|PD2309|Limited|
|vivo X100 Pro||Good|
|vivo X100S||Good|
|vivo X100S Pro||Good|
|vivo X100 Ultra||Good|
|vivo X200||Good|
|vivo X200S||Good|
|vivo X200 Pro||Good|
|vivo X200 Pro Mini||Good|
|vivo X Fold 3||Good|
|vivo X Fold 3 Pro||Good|
|vivo S6 5G|PD1962|Good|
|vivo S6 5G|PD1962B|Good|
|vivo S7|PD2020|Good|
|vivo S7|PD2080|Good|
|vivo S7e|PD2031|Good|
|vivo S7e|PD2031EA|Good|
|vivo Z6|PD1963|Good|
|vivo Z6 5G|V1963A|Good|
|vivo Z6 5G|3PD1963|Good|
|vivo V20 2021|2040|Good|
|vivo V21e 5G|2055|Good|
|vivo V23e||Good|
|vivo V20|2025|Good|
|vivo S10e||Good|
|vivo V15 pro|1818|Good|
|vivo V15 pro|1818N|Good|
|vivo V15|1819N|Good|
|vivo V15|1819|Good|
|vivo V21 5G|2050|Good|
|vivo Y95|1807|Good|
|vivo Y95|1807N|Good|
|vivo V9 pro|1851|Good|
|vivo V9 6GB|1723CF|Good|
|vivo V9|1727ID|Good|
|vivo Y71|PD1731D|Good|
|vivo Y71|1801|Good|
|vivo V9 Youth / Y85|1727|Good|
|vivo V9 Youth / Y85|1726|Good|
|vivo Y7s|PD1913|Good|
|vivo Y20 2021||Good|
|vivo IQOO Z3||Good|
|vivo IQOO Y31s 5G||Good|
|vivo IQOO z5x||Good|
|vivo IQOO U3|PD2061|Good|
|vivo IQOO U5E||Good|
|vivo IQOO U5|PD2197|Bad|
|vivo Y70s|PD2002|Good|
|vivo Y70t||Good|
|vivo Y71t||Good|
|vivo Y72 5G||Good|
|vivo Y76s|PD2156|Good|
|vivo Y74s||Good|
|vivo Y50t/ IQOO U1|PD2023|Bad|
|vivo iqoo u1x|PD2065|Bad|
|vivo Y76|PD2156|Good|
|vivo Y76|PD2156U|Good|
|vivo Y77|PD2219|Good|
|vivo Y77|PD2224|Good|
|vivo Y77|PD2278|Good|
|vivo Y78|PD2271|Good|
|vivo Y78|PD2279|Good|
|vivo Y78T||Good|
|vivo Y81|PD1732|Good|
|vivo Y89|PD1730E|Good|
|vivo Y91|PD1818C|Good|
|vivo Y93|PD1818|Bad|
|vivo Y93 Standard|PD1818B|Bad|
|vivo Y93S|PD1818C|Bad|
|vivo Y97|PD1813|Bad|
|vivo Z3|PD1813B|Limited|
|vivo Y50|PD1965|Good|
|vivo Y50 5G|PD2443|Good|
|vivo Y51|Y51|Good|
|vivo Y55 5G|PD2164|Good|
|vivo Y55 5G|PD2279|Good|
|vivo Y53s||Good|
|vivo Y52 5G||Good|
|vivo Y52|PD2057|Good|
|vivo Y52|PD2106|Good|
|vivo T1x|PD2123|Good|
|vivo Y3|PD1901|Bad|
|vivo Y3|PD1930|Bad|
|vivo Y5 S|PD1934A|Good|
|vivo Y7S|PD1913|Bad|
|vivo Y73|PD1731C|Good|
|vivo Y73|PD2031|Good|
|vivo Y73|PD2164UC|Good|
|vivo Y100||Good|
|vivo Y100i||Good|
|vivo Y100T||Good|
|vivo Y100 GT||Good|
|vivo Y200i||Good|
|vivo Y200||Good|
|vivo Y200 GT||Good|
|vivo Y200T||Good|
|vivo Y300||Good|
|vivo Y300 pro||Good|
|vivo Y300T||Good|
|vivo Y12||Good|
|vivo Y85A|PD1730|Limited|
|vivo Y31S|PD2054|Bad|
|vivo Y31S|PD2068|Bad|
|vivo Y31S|PD2092|Bad|
|vivo Y30|PD2036|Bad|
|vivo Y32|PD2158|Bad|
|vivo Y32|PD2168|Bad|
|vivo Y32|PD2180|Bad|
|vivo Y32t||Good|
|vivo Y33|PD2166|Limited|
|vivo Y33|PD2317|Limited|
|vivo Y31||Good|
|vivo Y35|PD2205|Limited|
|vivo Y37||Good|
|vivo Y37 Pro||Good|
|vivo Y37T|PD2443|Limited|
|vivo Y37C||Good|
|vivo Y36|PD2318|Limited|
|vivo Y36t|PD2327|Limited|
|vivo IQOO Z5 Pro / Z5||Good|
|vivo IQOO Z6 Pro|I2126|Limited|
|vivo IQOO Z6|I2203|Limited|
|vivo IQOO Z6|I2208|Limited|
|vivo IQOO Z6|I2206|Limited|
|vivo IQOO Z6|I2127|Limited|
|vivo IQOO Z6|I2126|Limited|
|vivo IQOO Z6x||Good|
|vivo IQOO Z7||Good|
|vivo IQOO Z7X||Good|
|vivo IQOO Z7i||Good|
|vivo IQOO Z8X||Good|
|vivo IQOO Z8||Good|
|vivo IQOO Z9||Good|
|vivo IQOO Z9 Turbo||Good|
|vivo IQOO Z9X||Good|
|vivo IQOO Z10||Good|
|vivo IQOO Z10 Turbo+||Good|
|vivo IQOO Z10X||Good|
|vivo Z5i|PD1941|Good|
|vivo Z5|PD1921|Good|
|vivo Z5x|PD1911|Good|
|vivo Z5x|PD1919|Good|
|vivo Z5x|PD1990|Good|
|vivo Z5x 2020|PD2020|Good|
|vivo Z1 pro|1951|Good|
|vivo Y9s|PD1945|Bad|
|vivo S1|PD1831|Good|
|vivo S1 Pro|PD1832|Good|
|vivo X27|PD1829|Good|
|vivo X27|PD1838|Good|
|vivo X27 pro|PD1836|Good|
|vivo X30 /X30 pro|PD1938|Good|
|vivo X50|PD2001|Good|
|vivo X50|2004|Good|
|vivo X50 pro+|PD2011|Good|
|vivo X50 pro|PD2005|Good|
|vivo X60t||Good|
|vivo X60 5G||Good|
|vivo X60|PD2046|Good|
|vivo X60|PD2059|Good|
|vivo X60|PD2085|Good|
|vivo X60|PD2047|Good|
|vivo X60|PD2120|Good|
|vivo X60t Pro+||Good|
|vivo X51||Good|
|vivo X60 Pro 5G||Good|
|vivo X60 Pro+ 5G|PD2056|Good|
|vivo S9|PD2072|Good|
|vivo S9e|PD2048|Good|
|vivo S5|PD1932|Good|
|vivo S1 Prime|1920|Good|
|vivo S1 Prime|1937|Good|
|vivo V20 SE|2023|Good|
|vivo V23 5G|2130|Good|
|vivo V23 Pro 5G|2132|Good|
|vivo NEX S|PD1805|Good|
|vivo NEX 2|PD1821|Good|
|vivo X50 lite|1937|Good|
|vivo X50 lite|1920|Good|
|vivo G1|PD1962|Good|
|vivo G1|PD1962B|Good|
|vivo G2|PD2318|Good|
|vivo G3|PD2443|Good|
|vivo NEX 3|PD1923|Good|
|vivo NEX 3 5G|PD1924|Good|
|vivo NEX 3 5G|1913|Good|
|vivo NEX 5||Good|
|vivo NEX 3S|PD1950|Good|
|vivo Y10|PD2140|Bad|
|vivo Y10|PD2168|Bad|
|vivo Y10|PD2180|Bad|
|vivo X20A/X20|PD1709|Limited|
|vivo X20Plus|PD1710|Limited|
|vivo X20Plus UD|PD1721|Limited|
|vivo X23|PD1809|Good|
|vivo X23|PD1816|Good|
|vivo X21 /X21A|1725|Limited|
|vivo X21 /X21A|PD1728|Limited|
|vivo X21UD|PD1728UD|Limited|
|vivo X21i|PD1801|Limited|
|vivo X21s|PD1814|Limited|
|vivo X21s|1804|Limited|
|vivo X21s|1806|Limited|
|vivo X21s|1814|Limited|
|vivo X9|PD1616|Bad|
|vivo X9i|PD1624|Bad|
|vivo X9s plus|PD1635|Bad|
|vivo X9Plus|PD1619|Bad|
|vivo X9s|PD1616B|Bad|
|vivo V3Max|V3Max|Bad|
|vivo V3Max A|PD1523|Bad|
|vivo V3Max +A|PD1523B|Bad|
|vivo NEX A|PD1806B|Good|
|vivo NEX Dual Display Edition|PD1806|Good|
|vivo pad||Good|
|Mi Note 10 / MI CC9 Pro/ Note 10 Pro|tucana|Good|
|Mi Note 10 / MI CC9 Pro/ Note 10 Pro|sweet|Good|
|MI note 10 lite|toco|Good|
|MI 10|umi|Good|
|MI 10 lite 5|monet|Good|
|Mi lite 5G|monet|Good|
|Mi 10T lite|gauguin|Good|
|MI 10T / Mi 10T Pro|apollo|Good|
|Mi 10i 5G|gauguininpro|Good|
|Mi Mix Fold|cetus|Good|
|Mi Mix Fold 3||Good|
|Mi Mix Fold 4||Good|
|Mi Mix Flip|ruyi|Good|
|MI 10 Pro|cmi|Good|
|MI 10 lite zoom / F Mi 10 Lite 5G|vangogh|Good|
|Mi 10 Ultra|cas|Good|
|Mi 10s|thyme|Good|
|Mi civi|mona|Good|
|Mi civi 1s|zijin|Good|
|Mi civi 2|ziyi|Good|
|Mi civi 3|yuechu|Good|
|Mi civi 4 pro|chenfeng|Good|
|Mi civi 5 pro||Good|
|Mi 11|venus|Good|
|Mi 11T|amber|Good|
|Mi 11T Pro|vili|Good|
|Mi 11 Lite 5G NE|lisa|Good|
|Mi 11 Lite 5G|renoir|Good|
|Mi 11 Lite|courbet|Good|
|Mi 11 Pro|mars|Good|
|Mi 11 Ultra|star|Good|
|Mi 12|cupid|Good|
|Mi 12X|psyche|Good|
|Mi 12 Pro|zeus|Good|
|Mi 12 Pro|daumier|Good|
|Mi 12 Lite|taoyao|Good|
|Mi 11i HyperCharge|pissarroinpro|Good|
|Mi Mix Fold 2|zizhan|Good|
|Mi 12s|mayfly|Good|
|Mi 12S Ultra|thor|Good|
|Mi 12S Pro|unicorn|Good|
|Mi 13|fuxi|Good|
|Mi 13R||Good|
|Mi 13 5G|breeze|Bad|
|Mi 13C|gale|Bad|
|Mi 13|ishtar|Bad|
|Mi 13T||Good|
|Mi 13T Pro||Good|
|Mi 13 Pro|nuwa|Bad|
|Mi 13 lite|ziyi|Bad|
|Mi 14|houji|Bad|
|Mi 14T|degas|Bad|
|Mi 14T pro|rothko|Bad|
|Mi 14 Pro|shennong|Good|
|Mi 14 Ultra|aurora|Good|
|Mi 15 Ultra|xuanyuan|Good|
|Mi 15||Good|
|Mi 15 Pro||Good|
|Mi 15S Pro|dijun|Good|
|Mi 17||Good|
|Mi 17 Pro||Good|
|Mi 17 Pro Max||Good|
|Mi 17 Ultra||Good|
|Mi Pad 6||Good|
|Mi Pad 6S Pro|sheng|Good|
|Mi Pad 7|uke|Good|
|Mi pad 7||Good|
|Mi Pad 7 Pro|muyu|Good|
|Mi pad 7 Pro||Good|
|MI CC 9 Meitu Edition|vela|Good|
|MI CC 9e|laurus|Good|
|xiaomi MI 9 pro 5G|crux|Good|
|xiaomi MI 9|cepheus|Good|
|xiaomi MI 9 se|grus|Good|
|xiaomi REDMI k20 /Mi 9T|davinci|Good|
|xiaomi REDMI k20 /Mi 9T|davincin|Good|
|xiaomi REDMI k20 /Mi 9T|davinciin|Good|
|Mi 9T pro|raphaelin|Good|
|xiaomi REDMI k20 pro|raphael|Good|
|xiaomi REDMI k20 pro|raphaelin|Good|
|xiaomi REDMI k20 pro|raphaels|Good|
|Xiaomi Redmi 10X Pro 5G|bomb|Good|
|Xiaomi Redmi 10X Pro 5G|banana|Good|
|Xiaomi Redmi 10X 5G|atom|Good|
|Xiaomi Redmi 10X 5G|apricot|Good|
|Xiaomi Redmi 9T|lime|Good|
|Xiaomi Redmi 9|galahad|Good|
|Xiaomi Redmi 9A|dandelion|Good|
|Xiaomi Redmi 10X 4G|merlin|Bad|
|xiaomi REDMI k40 Gaming|ares|Good|
|xiaomi REDMI k40s|munch|Good|
|xiaomi REDMI k40 Pro||Good|
|xiaomi REDMI k40 Pro Plus||Good|
|Redmi A3|blue|Good|
|Redmi A3 Pro||Good|
|Redmi A5|serenity|Good|
|Redmi 12C|earth|Good|
|Redmi 12C|aether|Good|
|Redmi 13C|gale|Good|
|Redmi 13C|gust|Good|
|Redmi 14C|pond|Good|
|Redmi 14C|2409BRN2CC|Good|
|Redmi 14R 5G||Good|
|Redmi 15|spring|Good|
|Redmi 15 5G||Good|
|Redmi 15T|goya|Good|
|Redmi 15T Pro||Good|
|xiaomi POCO F3 GT|aresin|Good|
|xiaomi POCO F4 GT|ingres|Good|
|xiaomi POCO F4|munch|Good|
|xiaomi POCO F4 Pro|matisse|Good|
|xiaomi POCO F7|onyx|Good|
|xiaomi POCO F7 Pro|zorn|Good|
|xiaomi POCO F7 Ultra|miro|Good|
|xiaomi REDMI k50 Gaming|ingres|Good|
|xiaomi REDMI k50|rubens|Good|
|xiaomi REDMI k50i|xagain|Good|
|xiaomi REDMI k50 pro|matisse|Good|
|xiaomi REDMI k50 ultra|diting|Good|
|xiaomi REDMI k40 pro / REDMI k40 pro+ / Mi 11i|haydn|Good|
|xiaomi REDMI k40 / POCO F3|alioth|Good|
|Xiaomi Redmi K60|mondrian|Good|
|Xiaomi Redmi K60 Pro|socrates|Good|
|xiaomi Redmi K60 Ultra|corot|Good|
|Xiaomi Redmi K60E|rembrandt|Good|
|xiaomi Redmi K70|corot|Good|
|xiaomi Redmi K70 Pro||Good|
|xiaomi Redmi K70 Ultra||Good|
|xiaomi Redmi K70E||Good|
|xiaomi Redmi K80 Pro|miro|Good|
|xiaomi Redmi K80||Good|
|xiaomi REDMI k30|phoenix|Good|
|xiaomi REDMI k30 Ultra|cezanne|Good|
|xiaomi REDMI k30 5G /K30i|picasso|Good|
|xiaomi REDMI k30S Ultra|apollo|Good|
|xiaomi REDMI k30 pro / Poco F2 Pro|lmi|Good|
|xiaomi REDMI k30 pro / Poco F2 Pro|lmiin|Good|
|xiaomi REDMI k30 pro zoom Edition|lmipro|Good|
|xiaomi REDMI k30 pro zoom Edition|lmiinpro|Good|
|Xiaomi Pad 5|nabu|Good|
|Xiaomi Pad 5 Pro|elish|Good|
|Xiaomi Pad 5 Pro 5G|enuma|Good|
|xiaomi 11X|aliothin|Good|
|xiaomi 11X pro|haydnin|Good|
|xiaomi 11i||Good|
|xiaomi Mix 4|odin|Good|
|xiaomi Mix4||Good|
|Xiaomi Redmi Note 10 Pro/ max|sweet|Good|
|Xiaomi Redmi Note 10 Pro/ max|sweetin|Good|
|Xiaomi Redmi Note 10 Pro/ max|chopin|Good|
|Xiaomi Redmi Note 10|sunny|Good|
|Xiaomi Redmi Note 10s|maltose|Good|
|Xiaomi Redmi Note 10s|rosemary|Good|
|Xiaomi Redmi Note 10s|secret|Good|
|Xiaomi Redmi Note 10 5G|camellia|Good|
|Xiaomi Redmi Note 10 5G|camellian|Good|
|Xiaomi Redmi Note 10T 5G|camellia|Good|
|Xiaomi Redmi Note 11 / 11T|evergo|Good|
|Xiaomi Redmi Note 11s|fleur|Good|
|Xiaomi Redmi Note 11s|miel|Good|
|Xiaomi Redmi Note 11s|opal|Good|
|Xiaomi Redmi Note 11E|light|Good|
|Xiaomi Redmi Note 11E Pro|veux|Good|
|Xiaomi Redmi Note 11T Pro|xaga|Good|
|Xiaomi Redmi Note 11T Pro+|xagapro|Good|
|Xiaomi Redmi Note 11 Pro|pissarro|Good|
|Xiaomi Redmi Note 11 Pro|viva|Good|
|Xiaomi Redmi Note 11 Pro|vida|Good|
|Xiaomi Redmi Note 11 Pro+|pissarropro|Good|
|Xiaomi Redmi Note 11 Pro+|peux|Good|
|Xiaomi Redmi Note 12 5G|sunstone|Limited|
|Xiaomi Redmi Note 12 Tansuozhe|rubyplus|Limited|
|Xiaomi Redmi Note 12 Pro jisuban|redwood|Limited|
|Xiaomi Redmi Note 12 5G Pro|ruby|Good|
|Xiaomi Redmi Note 12 +|rubypro|Good|
|Xiaomi Redmi Note 12 Pro jisuban|marble|Good|
|Xiaomi Redmi Note 12T Pro||Good|
|Xiaomi Redmi Note 13||Good|
|Xiaomi Redmi Note 13 Pro||Good|
|Xiaomi Redmi Note 13 Pro Plus||Good|
|Xiaomi Redmi Note 13R||Good|
|Xiaomi Redmi Note 13R Pro|peridot|Good|
|Xiaomi Redmi Note 14 5G||Good|
|Xiaomi Redmi Note 14||Good|
|Xiaomi Redmi Note 14 Pro||Good|
|Xiaomi Redmi Note 14 Pro+||Good|
|Xiaomi Redmi Note 14S||Good|
|Xiaomi Redmi Note 15||Good|
|Xiaomi Redmi Note 15 Pro||Good|
|Xiaomi Redmi Note 15 Pro Plus||Good|
|Xiaomi Redmi Turbo 3||Good|
|Xiaomi Redmi Pad Pro||Good|
|Xiaomi Redmi Turbo 4||Good|
|Xiaomi Redmi Turbo 4 Pro||Good|
|xiaomi REDMI Note 7 Pro|violet|Good|
|xiaomi REDMI Note 7|lavender|Good|
|xiaomi REDMI Note 8|ginkgo|Good|
|xiaomi REDMI Note 8 pro|begonia|Good|
|xiaomi REDMI Note 8 pro|begoniain|Good|
|Redmi Note 8T|willow|Good|
|Redmi Note 8 2021|biloba|Good|
|Poco C3|angelicain|Good|
|Poco X2|phoenixin|Good|
|Poco X3|karna|Good|
|Poco X3 NFC|surya|Good|
|Poco X3 Pro|bhima|Good|
|Poco X3 Pro|vayu|Good|
|Poco X3 GT|chopin|Good|
|Poco X4 Pro|peux|Good|
|Poco X4 Pro|veux|Good|
|Xiaomi Poco M2 Pro|gram|Good|
|Xiaomi Poco M3 Pro / Redmi Note 10T 5G|camelliain|Good|
|Xiaomi Poco M3||Good|
|Xiaomi Poco M3 Pro 5G|camellian|Good|
|Xiaomi Poco M3 Pro 5G|camellia|Good|
|Xiaomi Poco M4 Pro 5G|miel|Good|
|Xiaomi Poco M4 Pro 5G|fleur|Good|
|Xiaomi Poco M4 Pro 5G|evergreen|Good|
|Xiaomi Poco M4 Pro 5G|evergo|Good|
|Redmi Note 9 / Redmi 10X 4G|merlin|Good|
|Redmi Note 9 / Redmi 10X 4G|merlinin|Good|
|Redmi Note 9 5G|cannon|Good|
|Redmi Note 9 Pro|joyeuse|Good|
|Redmi Note 9 Pro|lime|Good|
|Redmi Note 9 Pro / Redmi Note 9s / redmi Note 10 lite|curtana|Good|
|Redmi Note 9 Pro 5G|gauguinpro|Good|
|Redmi Note 9 Pro Max|excalibur|Good|
|Redmi Note 9T 5G|cannong|Good|
|Redmi Note 11/ Pro|selenes|Good|
|Redmi Note 11/ Pro|spes|Good|
|Redmi Note 11/ Pro|spesn|Good|
|Redmi Note 11/ Pro|evergo|Good|
|Redmi Note 11/ Pro|light|Good|
|Redmi Note 11/ Pro|miel|Good|
|Redmi Note 11/ Pro|fleur|Good|
|Redmi Note 11/ Pro|secret|Good|
|Redmi Note 11/ Pro|opal|Good|
|Redmi Note 11/ Pro|pissarro|Good|
|Redmi Note 11/ Pro|viva|Good|
|Redmi Note 11/ Pro|vida|Good|
|Redmi Note 11/ Pro|peux|Good|
|Redmi Note 11/ Pro|pissarropro|Good|
|Redmi Note 11/ Pro|xaga|Good|
|Redmi Note 11/ Pro|xagapro|Good|
|Redmi Note 12/ Pro|tapas|Good|
|Redmi Note 12/ Pro|topaz|Good|
|Redmi Note 12/ Pro|sunstone|Good|
|Redmi Note 12/ Pro|sky|Good|
|Redmi Note 12/ Pro|ocean|Good|
|Redmi Note 12/ Pro|sea|Good|
|Redmi Note 12/ Pro|sweet|Good|
|Redmi Note 12/ Pro|ruby|Good|
|Redmi Note 12/ Pro|rubypro|Good|
|Redmi Note 12/ Pro|rubyplus|Good|
|Redmi Note 12/ Pro|redwood|Good|
|Redmi Note 12/ Pro|pearl|Good|
|Redmi Note 12R|sky|Good|
|Redmi Note 12R|river|Good|
|Redmi Note 12C|earth|Good|
|Redmi Note 11/ Pro|veux|Good|
|Black Shark 3 / 3s|klein|Good|
|Black Shark 3 Pro|mobius|Good|
|Xiaomi Black Shark 5 Pro / 5Rs|katyusha|Good|
|Xiaomi Black Shark 5 Pro / 5Rs|kaiser|Good|
|Xiaomi Black Shark 5|patriot|Good|
|Xiaomi Black Shark 2 Pro|darklighter|Good|
|Xiaomi Black Shark 2|skywalker|Good|
|Xiaomi Black Shark Helo / Shark 1s|bullhead|Good|
|Xiaomi Black Shark|shark|Good|
|Xiaomi Black Shark 4 Pro / 4s Pro|penrose|Good|
|Xiaomi Black Shark 4 / 4|kaiser|Good|
|xiaomi MI 6|sagit|Bad|
|xiaomi note2|scorpio|Bad|
|xiaomi Max2|oxygen|Bad|
|xiaomi mix|lithium|Bad|
|xiaomi note3|jason|Limited|
|xiaomi MIX 2|chiron|Bad|
|xiaomi MIX FLIP||Good|
|Mi 5C|meri|Limited|
|Mi 5X /Xiaomi Mi A1|tiffany|Limited|
|xiaomi Max|helium|Bad|
|xiaomi redmi Note 5 /Note 5 pro|whyred|Bad|
|xiaomi Redmi Y1 / Note 5A|ugg|Bad|
|xiaomi redmi 5Plus|vince|Bad|
|xiaomi redmi 5|rosy|Bad|
|REDMI 6 PRO|sakura\_india|Limited|
|REDMI 6 PRO|sakura|Limited|
|Mi A3|laurel\_sprout|Limited|
|Mi 6X|wayne|Limited|
|Mi A2|jasmine\_sprout|Limited|
|Mi A2 lite|daisy\_sprout|Limited|
|Mi Pad 4 /4 plus|clover|Limited|
|Mi Max 3|nitrogen|Bad|
|xiaomi redmi note 4|mido|Bad|
|xiaomi redmi note 4|nikel|Bad|
|Xiaomi Redmi 4X|santoni|Bad|
|Xiaomi Redmi 4|prada|Bad|
|Xiaomi Redmi 4 Pro|markw|Bad|
|Mi 5s|capricorn|Bad|
|Mi 5s plus|natrium|Bad|
|xiaomi POCO F1|beryllium|Good|
|xiaomi MI 8|dipper|Good|
|xiaomi MIX 3 5G|andromeda|Good|
|xiaomi MIX 3|perseus|Good|
|xiaomi MIX 2S|polaris|Good|
|xiaomi MI 8 SE|sirius|Good|
|xiaomi MI 8 lite|platina|Good|
|xiaomi MI 8 Explorer Edition|ursa|Good|
|xiaomi MI 8 Pro / MI 8 UD|equuleus|Good|
|oneplus 7pro|OnePlus7Pro|Good|
|oneplus 7pro|OP7ProNRSpr|Good|
|oneplus 7pro|OnePlus7ProTMO|Good|
|oneplus 7pro 5G|OnePlus7ProNR|Good|
|oneplus 7|OnePlus7|Good|
|OnePlus Z|OnePlusZ|Good|
|OnePlus Z|OnePlusNord|Good|
|oneplus 7T|OnePlus7T|Good|
|oneplus 7T|OnePlus7TTMO|Good|
|oneplus 7T Pro|OnePlus7TPro|Good|
|oneplus 7T Pro 5G|OnePlus7TProNR|Good|
|oneplus 8|OnePlus8|Good|
|oneplus 8T 5G|OnePlus8TMO|Good|
|oneplus 8T 5G|OnePlus8VZW|Good|
|OnePlus 8 Pro|OnePlus8Pro|Good|
|OnePlus 8 Pro|OnePlus8ProNR|Good|
|OnePlus Nord|Nord|Good|
|OnePlus Nord CE|OnePlusNordCE|Good|
|OnePlus Nord CE 2|OnePlusNordCE2|Good|
|OnePlus Nord CE 3||Good|
|OnePlus Nord CE 3 Lite||Good|
|OnePlus Nord CE 4||Good|
|OnePlus Nord CE 4 Lite||Good|
|OnePlus Nord CE 5||Good|
|OnePlus Nord 5||Good|
|OnePlus Nord N200|OnePlusN200|Good|
|OnePlus Nord N200|OnePlusN200TMO|Good|
|OnePlus Nord 2T|OP557AL1|Good|
|OnePlus Nord 2|OP515BL1|Good|
|OnePlus Nord N10 5G|OnePlusN10|Good|
|OnePlus Nord N10 5G|OnePlusN10METRO|Good|
|OnePlus Nord N10 5G|OnePlusN10TMO|Good|
|OnePlus Nord N100|OnePlusN100|Good|
|OnePlus Nord N100|OnePlusN100METRO|Good|
|OnePlus Nord N100|OnePlusN100TMO|Good|
|OnePlus 8T|OnePlus8T|Good|
|OnePlus 8T+ 5G|OnePlus8TTMO|Good|
|OnePlus 9 Pro|OnePlus9Pro|Good|
|OnePlus 9 Pro|OnePlus9ProTMO|Good|
|OnePlus 9|OnePlus9|Good|
|OnePlus 9|OnePlus9TMO|Good|
|OnePlus 9R|OnePlus9R|Good|
|OnePlus 9RT|OnePlus9RT|Good|
|OnePlus 9RT|OP5154L1|Good|
|OnePlus 9RT|OP5155L1|Good|
|OnePlus 10 Pro|OP516FL1|Good|
|OnePlus 10 Pro|OP516EL1|Good|
|OnePlus 10R / Ace|OP5566L1|Good|
|OnePlus 10R / Ace|OP5565|Good|
|OnePlus 11|OP591BL1|Good|
|OnePlus 11|CPH2447|Good|
|OnePlus 11|CPH2449|Good|
|OnePlus 11|CPH2451|Good|
|OnePlus 12|PJD110|Good|
|OnePlus 12|CPH2573|Good|
|OnePlus 12|CPH2581|Good|
|OnePlus 12|CPH2583|Good|
|OnePlus 13|CPH2649|Limited|
|OnePlus 13|CPH2653|Limited|
|OnePlus 13|CPH2655|Limited|
|OnePlus 13R|CPH2645|Limited|
|OnePlus 13R|CPH2647|Limited|
|OnePlus 13R|CPH2691|Limited|
|OnePlus 13T|CPH2723|Limited|
|OnePlus Open|CPH2551|Limited|
|OnePlus Ace 3|PJE110|Good|
|OnePlus Ace 3|CPH2585|Good|
|OnePlus Ace 3|CPH2609|Good|
|OnePlus Ace 3|CPH2611|Good|
|OnePlus Ace 3|OP5CF9L1|Good|
|OnePlus Ace 5|PKG110|Good|
|OnePlus Ace 5|PLC110|Good|
|OnePlus Ace 5 Pro|PKR110|Good|
|OnePlus Ace 3V|PJF110|Good|
|OnePlus Ace 3 Pro|PJX110|Good|
|OnePlus Ace 2, 11R|PHK110|Good|
|OnePlus Ace 2, 11R|CPH2487|Good|
|OnePlus Ace 2, 11R|PHP110|Good|
|OnePlus Ace 2, 11R|OP5927|Good|
|OnePlus Ace 2 Pro|PJA110|Good|
|OnePlus Ace Racing|OP5911|Good|
|OnePlus Ace Pro|OP5551L1|Good|
|OnePlus Ace Pro|PGP110|Good|
|OnePlus|OnePlus3T|Good|
|OnePlus|OnePlus5T|Good|
|OnePlus|OnePlus5|Good|
|OnePlus|OnePlus6TSingle|Good|
|OnePlus|OnePlus6T|Good|
|OnePlus|OnePlus6|Good|
|sony Xperia XZ1|701SO|Good|
|sony Xperia XZ1|G8341|Good|
|sony Xperia XZ1|G8342|Good|
|sony Xperia XZ1|G8343|Good|
|sony Xperia XZ1|SO-01K|Good|
|sony Xperia XZ1|SOV36|Good|
|sony Xperia XZ1C|G8441|Good|
|sony Xperia 1|802SO|Good|
|sony Xperia 1|J8110|Good|
|sony Xperia 1|J8170|Good|
|sony Xperia 1|J9110|Good|
|sony Xperia 1|J9180|Good|
|sony Xperia 1|SO-03L|Good|
|sony Xperia 1|SOV40|Good|
|sony Xperia 1 II|SO-51A|Good|
|sony Xperia 1 II|SOG01|Good|
|sony Xperia 1 II|XQ-AT51|Good|
|sony Xperia 1 II|XQ-AT52|Good|
|sony Xperia 1 II|XQ-AT72|Good|
|sony Xperia 1 III||Good|
|sony Xperia 1 IV|A201SO|Good|
|sony Xperia 1 IV|SO-51C|Good|
|sony Xperia 1 IV|SOG06|Good|
|sony Xperia 1 IV|XQ-CT54|Good|
|sony Xperia 1 IV|XQ-CT72|Good|
|sony Xperia 1 V|XQ-DQ72|Good|
|sony Xperia 1 VI|XQ-EC72|Good|
|sony Xperia XZ Premium|G8141|Good|
|sony Xperia XZ Premium|G8142|Good|
|sony Xperia XZ Premium|G8188|Good|
|sony Xperia XZ Premium|SO-04J|Good|
|sony Xperia XZ1 Compact|G8441|Good|
|sony Xperia XZ1 Compact|SO-02K|Good|
|sony Xperia 5|901SO|Good|
|sony Xperia 5|J8210|Good|
|sony Xperia 5|J8270|Good|
|sony Xperia 5|J9210|Good|
|sony Xperia 5|SO-01M|Good|
|sony Xperia 5|SOV41|Good|
|sony Xperia 5 V|XQ-DE72|Good|
|sony Xperia 5 II|A002SO|Good|
|sony Xperia 5 II|SOG02|Good|
|sony Xperia 5 II|XQ-AS52|Good|
|sony Xperia 5 II|XQ-AS72|Good|
|sony Xperia 5 III||Good|
|sony Xperia 10 plus|I3213|Good|
|sony Xperia 10 plus|I3223|Good|
|sony Xperia 10 plus|I4213|Good|
|sony Xperia 10 plus|I4293|Good|
|sony Xperia 10|I3113|Good|
|sony Xperia 10|I3123|Good|
|sony Xperia 10|I4113|Good|
|sony Xperia 10|I4193|Good|
|sony Xperia 10 II|A001SO|Good|
|sony Xperia 10 II|SO-41A|Good|
|sony Xperia 10 II|SOV43|Good|
|sony Xperia 10 II|XQ-AU42|Good|
|sony Xperia 10 II|XQ-AU51|Good|
|sony Xperia 10 II|XQ-AU52|Good|
|sony Xperia 10 III|SO-52B|Good|
|sony Xperia 10 III|SOG04|Good|
|sony Xperia 10 IV|SO-52B|Good|
|sony Xperia 10 IV|SOG04|Good|
|sony Xperia 10 V|XQ-DC72|Good|
|sony Xperia 10 VI|XQ-ES72|Good|
|sony Xperia Pro|XQ-AQ52|Good|
|sony Xperia Pro|XQ-AQ62|Good|
|sony Xperia Pro|MK16a|Good|
|sony Xperia Pro-I|XQ-BE42|Good|
|sony Xperia Pro-I|XQ-BE52|Good|
|sony Xperia Pro-I|XQ-BE62|Good|
|sony Xperia Pro-I|XQ-BE72|Good|
|Xperia XZ3|801SO|Good|
|Xperia XZ3|H8416|Good|
|Xperia XZ3|H9493|Good|
|Xperia XZ3|SO-01L|Good|
|Xperia XZ3|SOV39|Good|
|Xperia XZ3|akatsuki|Good|
|Xperia XZ2|702SO|Good|
|Xperia XZ2|H8216|Good|
|Xperia XZ2|H8266|Good|
|Xperia XZ2|H8276|Good|
|Xperia XZ2|H8296|Good|
|Xperia XZ2|SOV37|Good|
|Xperia XZ2|SO-03K|Good|
|Xperia XZ2 Premium|H8116|Good|
|Xperia XZ2 Premium|H8166|Good|
|Xperia XZ2 Premium|SO-04K|Good|
|Xperia XZ2 Premium|SOV38|Good|
|Xperia XZ2 Compact|H8314|Good|
|Xperia XZ2 Compact|H8324|Good|
|Xperia XZ2 Compact|SO-05K|Good|
|Asus ROG Phone ll|ASUS\_I001\_1|Good|
|Asus ROG Phone 3|ASUS\_I003\_1|Good|
|Asus ROG Phone 3|ASUS\_I003|Good|
|Asus ROG Phone|ASUS\_Z01QD\_1|Good|
|Asus ROG Phone 5 / 5 Pro|ASUS\_I005\_1|Good|
|Asus ROG Phone 5s / 5s Pro|ASUS\_I005\_1|Good|
|Asus ZenFone 6|ASUS\_T00G|Good|
|Asus ZenFone 6|ASUS\_Z002|Good|
|Asus ZenFone 6|ASUS\_I01WD|Good|
|Asus ZenFone 7 / 7 Pro|ASUS\_I002D|Good|
|Asus ZenFone 8 Flip|ASUS\_I004D|Good|
|Asus ZenFone 8/ ASUS 8Z|ASUS\_I006D|Good|
|Asus ZenFone 5z|ASUS\_Z01R\_1|Good|
|Asus ZenFone 5 Lite|ASUS\_X017D\_1|Good|
|Asus ZenFone 5 Lite|ASUS\_X017D\_2|Good|
|Asus ZenFone 5|ASUS\_X00QD|Good|
|Asus ZenFone 5|ASUS\_T00K|Good|
|Asus ZenFone 5|ASUS\_T00J1|Good|
|Asus ZenFone 5|ASUS\_T00F1|Good|
|Asus ZenFone 5|ASUS\_T00F|Good|
|Asus Zenfone 3s Max ZC521TL|ASUS\_X00G\_1|Good|
|Asus ZenFone 4|ASUS\_T00I|Good|
|Asus ZenFone 4|ASUS\_Z01KDA|Good|
|Asus ZenFone 4|ASUS\_T00Q|Good|
|Asus ZenFone 4|ASUS\_Z01KD\_1|Good|
|Asus ZenFone 4|ASUS\_Z01KD\_2|Good|
|Asus ZenFone 4|ASUS\_Z01KD\_3|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_1|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_2|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_4|Good|
|Asus ZenFone 4 Max|ASUS\_X00HD\_5|Good|
|Asus ZenFone 4 Max|ASUS\_X00ID|Good|
|Asus ZenFone 4 Max|ASUS\_X00IDB|Good|
|Asus ZenFone 4 Max|ASUS\_X00IDC|Good|
|Asus Zenfone 4 Pro|ASUS\_Z01GD\_1|Good|
|Asus Zenfone 4 Pro|ASUS\_Z01GD\_1|Good|
|Asus Zenfone 4 Selfie|ASUS\_X00LD\_1|Good|
|Asus Zenfone 4 Selfie Lite|ASUS\_X00HD\_3|Good|
|Asus Zenfone 4 Selfie Pro|ASUS\_Z01M\_1|Good|
|Asus ZenFone Max M2|ASUS\_X01A\_1|Good|
|Asus ZenFone Max Pro M2|ASUS\_X01BD\_2|Good|
|Asus ZenFone Max Pro M2|ASUS\_X01BD\_1|Good|
|Asus ZenFone Max Plus M2 /Zenfone Max Shot|ASUS\_A001D\_1|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_1|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_2|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_3|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_5|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_6|Good|
|Asus ZenFone Live L2|ASUS\_X00R\_7|Good|
|Asus ZenFone AR|ASUS\_A002\_1|Good|
|Asus ZenFone AR|ASUS\_A002|Good|
|Asus ZenFone Ares|ASUS\_A002\_2|Good|
|Asus ROG Phone|ASUS\_Z01QD\_1|Good|
|Lenovo Z6 Pro 5G|cream|Good|
|Lenovo Z6 Pro / Z6|zippo|Good|
|Lenovo Y90||Good|
|Lenovo Legion 2 Pro / Legion Duel 2||Good|
|Lenovo Legion Pro /Lenovo Legion Phone Duel|moba|Good|
|Lenovo Tab P11|J606F|Good|
|Lenovo Tab P11|J606L|Good|
|Lenovo Tab P11 Plus|TB-J616F|Good|
|Lenovo Tab P11 Plus|TB-J616X|Good|
|Lenovo Tab P11 Pro|J706F|Good|
|Lenovo Tab P11 Pro|J706L|Good|
|Lenovo Tab P11 5G|J607Z|Good|
|Lenovo Tab P12 Pro|Q706F|Good|
|Lenovo Tab P12 Pro|Q706Z|Good|
|Lenovo Tab 11|YT-J706X|Good|
|Lenovo Yoga Tab 13|K606F|Good|
|Lenovo Yoga Tab 11|YT-J706F|Good|
|Lenovo Yoga Tab 11|YT-J706X|Good|
|Lenovo Pad Pro||Good|
|Lenovo Pad Plus||Good|
|Lenovo Pad||Good|
|Lenovo Legion Y700|TB-9707F|Good|
|Lenovo K10|X6C6F|Good|
|Lenovo K10|X6C6L|Good|
|Lenovo K10|X6C6X|Good|
|Lenovo K10|X6C6NBF|Good|
|Lenovo K10|X6C6NBL|Good|
|Lenovo K10|X6C6NBX|Good|
|Lenovo K13 Note|capri|Good|
|Lenovo K13 Pro|caprip|Good|
|Lenovo Y70|halo|Good|
|Lenovo Tab M10 FHD Plus|X606F|Bad|
|Lenovo Tab M10 FHD Plus|X606M|Bad|
|Lenovo Tab M10 FHD Plus|X606X|Bad|
|Lenovo Tab M10 FHD Plus|X616F|Bad|
|Lenovo Tab M10 FHD Plus|X616M|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306FC\_PRC|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306NC\_PRC|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306V|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306X|Bad|
|Lenovo Tab M10 HD (2nd Gen) PRC|X306XA|Bad|
|Lenovo Tab M10 Plus 3rd Gen|TB125FU|Bad|
|Lenovo Tab M10 Plus 3rd Gen|X606X|Bad|
|Lenovo Tab M10 Plus 3rd Gen|X616F|Bad|
|Lenovo Tab M10 Plus 3rd Gen|X616M|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306F|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306FA|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306V|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306X|Bad|
|Lenovo Tab M10 HD (2nd Gen)|X306XA|Bad|
|Lenovo Tab M10 5G|TB-X607Z|Bad|
|Lenovo Tab M10 Plus|X606V|Bad|
|Lenovo Z5s|jd2019|Good|
|Lenovo Z5 Pro|zap|Good|
|Lenovo Z5 Pro|heart|Good|
|Lenovo A6 Note|Lenovo\_A6\_Note|Good|
|Lenovo S5 Pro|sprout|Good|
|Nokia 8 Sirocco|A1N|Good|
|Nokia 8 Sirocco|A1N\_sprout|Good|
|Nokia 8.3 5G||Good|
|Nokia 8 V 5G UW|RAV\_VZW|Good|
|Nokia 3.4||Good|
|Nokia X20||Good|
|Nokia X10||Good|
|Nokia G20||Good|
|Nokia XR20|TTG|Good|
|Nokia XR20|TTG\_sprout|Good|
|Nokia G50|PHR|Good|
|Nokia G50|PHR\_sprout|Good|
|Nokia X100|TTG|Good|
|Nokia 9|AOP\_sprout|Good|
|Nokia 9|AOP|Good|
|Nokia 7.1|CTL\_sprout|Good|
|Nokia 7.2|DDVA\_sprout|Good|
|Nokia 7.2|DDV\_sprout|Good|
|Nokia 3.1C /Nokia 3.1A|EAG|Good|
|Nokia 7 plus|B2N|Good|
|Nokia 7 plus|B2N\_sprout|Good|
|Nokia 5.1 plus / Nokia X5|PDA|Good|
|Nokia 5.4||Good|
|Nokia 6.1 plus / Nokia X6|DRG|Good|
|Nokia 6.1 plus / Nokia X6|DRG\_sprout|Good|
|Nokia 6.1|PL2|Good|
|Nokia 6.1|PL2\_sprout|Good|
|Nokia 6.2|SLDA\_sprout|Good|
|Nokia 6.2|SLD\_sprout|Good|
|Nokia X71|TAS|Good|
|Nokia 8|NB1|Good|
|Nokia 8.1 / Nokia X7|PNX\_sprout|Good|
|Nokia 8.1 / Nokia X7|PNXN|Good|
|Nokia 8.1 / Nokia X7|PNX|Good|
|Moto g(6)|ali|Good|
|Moto g(6)|ali\_n|Good|
|moto g7|river|Good|
|moto g7|river\_n|Good|
|moto g7 optimo maxx|ocean|Good|
|moto g(7) play|channel|Good|
|moto g(7) plus|lake|Good|
|moto g(7) plus|lake\_n|Good|
|moto g(7) power|ocean\_n|Good|
|moto g(8) play|lima|Good|
|moto g(8) plus|doha|Good|
|moto g(8) plus|doha\_n|Good|
|moto g(8) power|sofiar|Good|
|moto g(8) power lite|blackjack|Good|
|moto g Stylus|sofiap|Good|
|moto g power|sofia|Good|
|Moto One Hyper|def|Good|
|Moto One Macro|lima|Good|
|Moto One Zoom|parker|Good|
|Moto One Action|troika|Good|
|Moto One Action|troika\_sprout|Good|
|Moto One Vision / P50|kane\_sprout|Good|
|Moto One / P30 Play|deen\_sprout|Good|
|Moto One Power/ P30 Note|chef\_sprout|Good|
|Moto z3 play|beckham|Good|
|Moto z4|foles|Good|
|Moto P50|kane|Good|
|Moto Edge|racer|Good|
|Moto G60s|lisbon|Good|
|Moto G82|rhodep|Good|
|Moto Edge 20|berlin|Good|
|Moto Edge 20 lite|kyoto|Good|
|Moto Edge 20 Pro|pstar|Good|
|Moto Edge 30|dubai|Good|
|Moto Edge 30 Pro|hiphi|Good|
|Moto Edge plus|burton|Good|
|Moto G pro|sofiap\_sprout|Good|
|Moto G fast|rav|Good|
|Moto One Vision plus|doha\_n|Good|
|Moto One fusion+|liber|Good|
|Moto One fusion|astro|Good|
|moto g 5G plus /motorola one 5G /motorola one 5G UW|nairo|Good|
|moto g 5G|kiev|Good|
|moto g9 / moto g(9) play|guamp|Good|
|moto g9 plus|odessa|Good|
|moto razr|olson|Good|
|moto razr 5G/moto razr 2020|smith|Good|
|Moto one|deen\_sprout|Good|
|Moto one|deen\_sprout\_n|Good|
|Moto one 5G Ace|kiev|Good|
|Moto one 5G / 5G UW|nairo|Good|
|Moto one 5G UW Ace|kievv|Good|
|Moto Defy 2021|umts\_jordan|Good|
|Moto Defy 2021|bathena|Good|
|Moto Defy Pro|XT560|Good|
|moto G Stylus (2021)|minsk|Good|
|moto G Stylus (2022)|tonga|Good|
|moto G Stylus 5G|denver|Good|
|moto G power (2021)|borneo|Good|
|moto Edge X30|hiphic|Good|
|moto Edge S /G100|nio|Good|
|moto Edge(2021)|berlna|Good|
|moto G200 5G / edge S30|xpeng|Good|
|moto G100|nio|Good|
|moto G71|corfur|Good|
|moto G50 5G|saipan|Good|
|moto G51 /G51 5G|cypfq|Good|
|moto G50|ibiza|Good|
|moto G60|hanoip|Good|
|moto G40 Fusion|hanoip|Good|
|moto G41|corfu|Good|
|moto G31|coful|Good|
|moto G30|caprip|Good|
|moto G20|java|Good|
|moto G22|hawaiip|Good|
|moto G10 / G10 power|capri|Good|
|moto E7 Power|malta|Good|
|moto Tab G70|mototabg70|Good|
|moto Tab G70|mototabg70LTE|Good|
|Moto g(6) plus|evert|Good|
|Moto g(6) plus|evert\_n|Good|
|Moto g(6) plus|evert\_nt|Good|
|Moto Z(3)|messi|Good|
|Moto Z2 Force|nash|Good|
|Moto X4|payton|Good|
|Moto X4|payton\_sprout|Good|
|Moto G5S Plus|sanders|Good|
|Moto G5S Plus|sanders\_n|Good|
|Moto G5S Plus|sanders\_nt|Good|
|LG V50S ThinQ / G8X ThinQ|mh2lm|Good|
|LG W30 Pro|Neo4LM|Good|
|LG W30|LM-X440ZMW|Good|
|LG W30|LM-X440ZM|Good|
|LG W30|LM-X440IM|Good|
|LG W10|LMX130IM|Good|
|LG W10 Alpha|Neo2ALP|Good|
|LG V50 ThinQ|flashlm|Good|
|LG V50 ThinQ|flashlmdd|Good|
|LG VELVET|caymanslm|Good|
|LG VELVET|mcaymanlm|Good|
|LG Q61|mdh40lm|Good|
|LG Q92|acelm|Good|
|LG WING|winglm|Good|
|LG VELVET / LG Velvet 5G UW|caymanlm|Good|
|LG V60S ThinQ 5G / V60S ThinQ 5G UW|timelm|Good|
|LG G8S ThinQ / G8S|betalm|Good|
|LG G8X ThinQ|mh2lm|Good|
|LG G8 ThinQ / G8|alphaamz|Good|
|LG G8 ThinQ / G8|alphalm|Good|
|LG G8 ThinQ / G8|alphaplus|Good|
|LG Q9 /G7 Fit|falcon|Good|
|LG K61|mdh40lm|Good|
|LG V40 ThinQ|judypn|Good|
|LG G7 one|phoenix\_sprout|Good|
|LG Q8 (2018)|anna|Good|
|LG Q8 (2018)|cv7an|Good|
|Meizu 15|M15|Bad|
|Meizu 15|MX15|Bad|
|Meizu 15|15|Bad|
|Meizu 15 Plus|15PLus|Bad|
|Meizu 15 Lite|15Lite|Bad|
|Meizu 16 PLus|16PLus|Bad|
|Meizu 16 PLus|16|Bad|
|Meizu 16X|16X|Bad|
|Meizu 18|m2181|Good|
|Meizu note 8|meizunote8|Good|
|Meizu note 8|M1822|Good|
|Meizu M8|MeizuM8|Good|
|Meizu M8lite|M8lite|Good|
|Meizu 20|m2381|Good|
|Meizu 20|M381Q|Good|
|Meizu 20|meizu20|Good|
|Meizu 20 Pro|m2391|Good|
|Meizu 20 Pro|M391Q|Good|
|Meizu 20 Pro|meizu20Pro|Good|
|Meizu 21 Pro|m2481|Good|
|Meizu pro6s / pro6|PRO6|Bad|
|Meizu M6|meizu\_M6|Bad|
|Meizu M6 Note|M6Note|Bad|
|Meizu M6T|MeizuM6T|Bad|
|Meizu M6s|MeizuM6s|Bad|
|Meizu M6s|MeizumbluS6|Bad|
|Meizu Pro 6 plus|PRO6Plus|Bad|
|Meizu U20|U20|Bad|
|Meizu U20|MeizuU20|Bad|
|Meizu S6|MeizuS6|Bad|
|Meizu Pro 7|PRO7S|Bad|
|Meizu Pro 7|PRO7H|Bad|
|Meizu Pro 7 plus|PRO7Plus|Bad|
|Meizu Pro 7 plus|PRO7S|Bad|
|Meizu MX16|MX16|Good|
|Meizu 16T|meizu16T|Good|
|Meizu 16s pro|meizu16sPro|Good|
|Meizu 16s pro|16s|Good|
|Meizu 16Xs|16Xs|Good|
|Meizu 16Xs|meizu16Xs|Good|
|Meizu 17|meizu17|Good|
|Meizu 17 Pro|meizu17Pro|Good|
|Meizu 18|meizu18|Good|
|Meizu 18 Pro|meizu18Pro|Good|
|Meizu 18x|meizu18X|Good|
|Meizu 18s|meizu18s|Good|
|Meizu 18s Pro|meizu18sPro|Good|
|Meizu note9|meizunote9|Good|
|Meizu note9|Note9|Good|
|Meizu note9|meizuZero|Good|
|Meizu 16th|16th|Limited|
|Meizu 16th Plus|16thPlus|Limited|
|Meitu M8s|MayaS|Good|
|Meitu T9|Melody|Good|
|Meitu T9|Tiffany|Good|
|Meitu V6|Vivian|Good|
|Meitu T8s|VictoriaS|Good|
|Meitu T8|Victoria|Bad|
|Meitu M8|Maya|Bad|
|Smartisan N3|oscar|Bad|
|Smartisan R1|trident|Bad|
|Smartisan Pro 2S|ocean|Bad|
|Smartisan nut pro|odin|Bad|
|Smartisan pro 2|oxford|Bad|
|Smartisan pro 2|osborn|Bad|
|Smartisan Pro 3|delta|Good|
|Smartisan M1|surabaya|Bad|
|Smartisan M1L|colombo|Bad|
|le 2 X528|le\_s2\_cm|Bad|
|le S3|le\_s2\_na|Bad|
|le Pro3|le\_zl1|Bad|
|MAGNEO|MAGNEO|Bad|
|LGE G6|lucye|Good|
|LGE Q6|mh|Limited|
|LGE Q6|mhn|Limited|
|LGE Q6|flame|Good|
|Google Pixel 4 XL|coral|Good|
|Google Pixel 4a|sunfish|Good|
|Google Pixel 4a(5G)|bramble|Good|
|Google Pixel 5|redfin|Good|
|Google Pixel 5a 5G|barbet|Good|
|Google Pixel 6|oriole|Good|
|Google Pixel 6 Pro|raven|Good|
|Google Pixel 6a|bluejay|Good|
|Google Pixel 9|tokay|Good|
|Google Pixel 9 Pro|caiman|Good|
|Google Pixel 9 Pro Large|komodo|Good|
|Google Pixel 9 fold|comet|Good|
|Google Pixel 9a|tegu|Good|
|Pixel Fold|passport|Good|
|Wiko View 3 Pro|W-P611|Good|
|Wiko View 3|W-P311|Good|
|Wiko Y80|W-V720|Good|
|Stylo 5|cv7as|Good|
|Google Pixel|sailfish|Good|
|Google Pixel XL|marlin|Good|
|Infinix note 6|Infinix-X610|Good|
|Infinix note 7|Infinix-X690|Good|
|Infinix note 7|Infinix-X690B|Good|
|Infinix note 7|Infinix-X690C|Good|
|Infinix SMART 5|Infinix-X657|Good|
|Infinix SMART 5|Infinix-X657B|Good|
|Infinix SMART 5|Infinix-X657C|Good|
|Infinix SMART 5|Infinix-X688C|Good|
|Infinix note 10 pro|Infinix-X695|Good|
|Infinix note 10 pro|Infinix-X695D|Good|
|Infinix note 10 pro NFC|Infinix-X695C|Good|
|Infinix note 11s|Infinix-X698|Good|
|Infinix note 11 Pro|Infinix-X697|Good|
|Infinix note 11|Infinix-X663B|Good|
|Infinix note 11i|Infinix-X693|Good|
|Infinix note 12|Infinix-X670|Good|
|Infinix note 12|Infinix-X672|Good|
|Infinix note 12|Infinix-X663C|Good|
|Infinix note 12|Infinix-X663D|Good|
|Infinix note 12i|Infinix-X6819|Good|
|Infinix note 8|Infinix-X692|Good|
|Infinix Hot 10|Infinix-X682B|Good|
|Infinix Hot 10|Infinix-X682C|Good|
|Infinix zero 8|Infinix-X687|Good|
|Infinix zero 8i|Infinix-X687B|Good|
|Infinix S5|Infinix-X652|Good|
|Infinix S5|Infinix-X652A|Good|
|Infinix S5 pro|Infinix-X660|Good|
|Infinix HOT 9 Pro|Infinix-X655F|Good|
|Infinix S4|Infinix-X626|Good|
|Infinix S4|Infinix-X626B|Good|
|Infinix S4|Infinix-X626B-LTE|Good|
|Infinix zero 5G|Infinix-X6815|Good|
|Kyocera TORQUE G04|KYV46|Good|
|Kyocera GRATINA|KYV48|Good|
|Fujitsu F-51A / ARROWS 5G|F51A|Good|
|Fujitsu F-52A|F52A|Good|
|LitByLeia Lume Pad|LPD10-11|Good|
|LitByLeia Lume Pad|LPD10-10W|Good|
|LitByLeia Lume Pad|LPD10-11W|Good|
|Zebra ET51S|ET51S|Good|
|Zebra ET56S|ET56S|Good|
|Zebra TC52|TC52|Good|
|Zebra TC52X|TC52X|Good|
|Zebra TC57|TC57|Good|
|Zebra TC57X|TC57X|Good|
|Zebra TC72|TC72|Good|
|Zebra TC77|TC77|Good|
|Zebra TC26|TC26|Good|
|Zebra TC21|TC21|Good|
|Zebra EC50|EC50|Good|
|Zebra EC55|EC55|Good|
|Zebra TC8000|TC8000|Good|
|Sharp Aquos R3|SG808SH|Good|
|Sharp Aquos R3|SH-04L|Good|
|Sharp Aquos R3|SH-R10|Good|
|Sharp Aquos R3|NAX|Good|
|Sharp AQUOS R5G|SH-51A|Good|
|Sharp AQUOS R5G|SG908SH|Good|
|Sharp AQUOS R5G|Banagher|Good|
|Sharp sense3|PCZ-u|Good|
|Sharp sense3|SH-M12|Good|
|Sharp sense3|SH-02M|Good|
|Sharp sense3|PCZ|Good|
|Sharp sense3 basic|SG907SH|Good|
|Sharp sense3 basic|VIF|Good|
|Sharp sense3 plus|OBY|Good|
|Sharp sense3 plus|SH-RM11|Good|
|Sharp sense3 plus|SH-M11|Good|
|Sharp sense3 plus|SG901SH|Good|
|Sharp Aquos V|VGO|Good|
|Sharp AquosR2 compact|SH-M09|Good|
|Sharp AquosR2 compact|SG803SH|Good|
|Sharp Aquos S7|vespa\_sprout|Good|
|Sharp Aquos V|VGO|Good|
|Sharp Aquos zero5G basic / Aquos zero5G basic DX|SGA002SH|Good|
|Sharp Aquos zero5G basic / Aquos zero5G basic DX|OJ6|Good|
|Sharp Aquos zero2|SG906SH|Good|
|Sharp Aquos zero2|SH-01M|Good|
|Sharp Aquos zero2|SH-M13|Good|
|Sharp Aquos zero2|SH-Z20|Good|
|Sharp Aquos zero2|QDA|Good|
|Sharp Aquos zero|SG801SH|Good|
|Sharp Aquos zero|SH-Z10|Good|
|Sharp Aquos zero|SH-Z10A|Good|
|Sharp Aquos zero|SH-M10|Good|
|Tecno Camon 18i|TECNO-CG6|Good|
|Tecno Camon 18 Premier|TECNO-CH9|Good|
|Tecno Camon 18 Premier|TECNO-CH9n|Good|
|TECNO CAMON 18 P|TECNO-CH7|Good|
|TECNO CAMON 18 P|TECNO-CH7n|Good|
|TECNO CAMON 17 Pro|TECNO-CG8|Good|
|TECNO CAMON 17 Pro|TECNO-CG8h|Good|
|TECNO CAMON 16 Pro|TECNO-CE8|Good|
|TECNO CAMON 16 Premier|TECNO-CE8|Good|
|TECNO Camon 12 Pro|TECNO-CC9|Good|
|TECNO Phantom 9|TECNO-AB7|Good|
|TECNO Phantom X|TECNO-AC8|Good|
|TECNO POVA 2 not stable|TECNO-LE7|Good|
|TECNO POVA 2 not stable|TECNO-LE7n|Good|
|TECNO POVA 5G not stable|TECNO-LE8|Good|
|Umx(Ultimate Mobile Experience)|U3AR|Good|
|General Mobile GM 9 Plus|GM9PLUS\_s|Good|
|HTC Desire 21 Pro 5G|htc\_thudugl|Good|
|HTC Desire 20+|htc\_srcdugl|Good|
|HTC U20 5G|htc\_flhdugl|Good|
|HTC Desire 20 Pro|htc\_bymdugl|Good|
|TCL 10 5G UW|Seattle\_VZW|Good|
|TCL 10 5G|Seattle|Good|
|TCL 10 Plus|Boston|Good|
|TCL 10 Pro|T1\_PRO|Good|
|TCL 10 SE|Oakland|Good|
|TCL 10L|T1\_LITE|Good|
|TCL 10L|T1\_LITE|Good|
|TCL 20 5G|Irvine|Good|
|TCL 20 pro 5G|Ottawa|Good|
|TCL 20L|Richland|Good|
|TCL 20L+|Richland\_Pro|Good|
|TCL FFALCON FF1||Good|
|Vsmart live 4|cassia|Good|
|Vsmart Aris Pro|jacarandapro|Good|
|RED HydrogenONE|HydrogenONE|Good|
|Nexus 6P|angler|Good|
|Google Pixel 3|blueline|Good|
|Google Pixel 3a XL|bonito|Good|
|Google Pixel 3 XL|crosshatch|Good|
|Borqs Falcon|falcon|Good|
|Google Pixel 3a|sargo|Good|
|Google Pixel 2 XL|taimen|Good|
|Google Pixel 2|walleye|Good|
|BQ Aquaris X2|zangya\_sprout|Good|
|BQ Aquaris X2 Pro|zangyapro\_sprout|Good|
|glass kuak|bengal|Good|
|glass kuak|bengal\_global|Good|
|glass kuak|pluto|Good|
|glass kuak|pluto\_global|Good|

---

## 运动跟踪支持的设备
- 章节路径: `motion-tracking/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/devices.html

# 运动跟踪支持的设备
如果一个设备（手机、眼镜或头显）通过硬件或软件方案具有真实尺度的六自由度运动跟踪能力，我们称其为运动跟踪设备。这些设备包括但不限于可以运行 EasyAR 运动跟踪、 ARCore/ ARKit、华为 AR Engine 的设备，或具有六自由度跟踪能力的眼镜。
EasyAR 运动融合可以让图像和物体跟踪摆脱抖动困扰，跟踪稳定，并且可以在离开相机视野之后继续跟踪。
## 不同平台的运动跟踪方案的选择
部分操作系统或厂商通过系统原生的 AR SDK 提供类似的运动跟踪功能，如苹果 ARKit,谷歌 ARCore 和华为 AR Engine 等。
为保证最佳效果，在部分平台，EasyAR 自动选择当前可用的平台原生的运动跟踪方案而不需要额外配置。例如在 iOS 平台上，EasyAR 会优先调用 ARKit 的运动跟踪功能。需要进一步了解，请参阅[EasyAR运动跟踪与平台原生运动方案的关系](comparison.html)。
EasyAR 的运动跟踪解决方案，目前支持的设备包括主流的智能手机和平板电脑。EasyAR 的运动跟踪功能目前暂不支持 AR/MR 眼镜等可穿戴设备。如果这些设备本身支持六自由度的运动跟踪功能，开发者可以通过自定义相机接入 EasyAR 并与的其他功能联合使用。
对于微信小程序开发者，由于平台限制无法直接使用上述任何的运动跟踪方案，可以参阅微信小程序提供的类似[运动跟踪](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)功能。
## 延伸阅读
了解运动跟踪支持的具体机型
* [EasyAR 运动跟踪支持的设备](devices-easyar.html)
* [ARCore 运动跟踪支持的设备](devices-arcore.html)
* [AR Engine 运动跟踪支持的设备](devices-arengine.html)
* [微信小程序支持的设备](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)

---

## 什么是运动跟踪功能？
- 章节路径: `motion-tracking/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/intro.html

# 什么是运动跟踪功能？
## 运动跟踪功能介绍
AR 的运动跟踪功能泛指通过计算机视觉和传感器融合算法，实时跟踪设备（手机、平板、智能眼镜）相对于环境的六自由度位置和朝向的功能。部分厂商或操作系统原生的混合现实 SDK 提供类似的运动跟踪功能，如苹果 [ARKit](https://developer.apple.com/augmented-reality/arkit/),谷歌的 [ARCore](https://developers.google.com/ar),华为的 [AR Engine](https://developer.huawei.com/consumer/en/hms/huawei-arengine/) 等。在部分智能眼镜上，厂商提供类似的运动跟踪功能。在微信小程序平台上，微信开放了功能与运动跟踪相似的[6DoF AR 能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)。
通过厂商或操作系统支持的设备占比相对较低，为了使得更多机型支持运动跟踪功能， EasyAR 的运动跟踪（Motion Tracker）利用计算机视觉、惯性同步定位和建图（VI-SLAM）技术，在更多的机型上实现六自由度的实时跟踪。
![Motion Tracking](https://doc-asset.easyar.com/develop/motion-tracking/media/motion-tracking.png)
## 后续步骤
* 了解 [EasyAR 运动跟踪支持的设备](devices.html)
* 了解 [EasyAR 运动跟踪与 EasyAR 其他模块的关系](motion-tracking-and-easyar.html)
* 了解 [EasyAR 运动跟踪与ARKit/ARCore/华为AR Engine的关系](comparison.html)

---

## 为其他功能提供数据的运动跟踪
- 章节路径: `motion-tracking/motion-tracking-and-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/motion-tracking/motion-tracking-and-easyar.html

# 为其他功能提供数据的运动跟踪
运动跟踪是增强现实与环境交互的基础功能之一。运动跟踪组件在提供这项功能的同时可以为其他功能提供输入帧数据，同时具有运动跟踪和摄像头控制的功能。
运动跟踪与 EasyAR 其他功能的关系主要有以下几种情况：
* 部分 EasyAR 的功能必须依赖运动跟踪功能。
* 功能不完全依赖运动跟踪，但是在支持运动跟踪的机型上效果更好。
* 部分功能独立于运动跟踪即可工作。
|EasyAR 功能|是否依赖运动跟踪功能|
|平面检测|是|
|稀疏空间地图|是|
|稠密空间地图|是|
|图片跟踪|否|
|3D 物体识别|否|
|表面跟踪|否|
|EasyAR Mega|否|
> **注意**
EasyAR Mega 功能并不依赖运动跟踪功能，但是在支持运动跟踪功能的设备上可以体验最优的 Mega 效果。
> **注意**
图片跟踪可以不依赖运动跟踪独立运行，也可以联合运动跟踪实现融合跟踪的效果。详情参见 [运动融合|扩展跟踪](../image-tracking/motion-fusion.html)
> **注意**
物体跟踪可以不依赖运动跟踪独立运行，也可以联合运动跟踪实现融合跟踪的效果。详情参见 [运动融合|扩展跟踪](../object-tracking/motion-fusion.html)
## 相关主题
* [运动跟踪](intro.html)
* [摄像头和输入扩展](../cameras/cameras.html)

---

## 在 3D 引擎中使用 EasyAR
- 章节路径: `native/fundamentals/3dengine.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/3dengine.html

# 在 3D 引擎中使用 EasyAR
在 3D 引擎中使用 EasyAR，需要渲染相机画面和虚拟物体。渲染虚拟物体需要和相机画面对准。相机画面渲染时，图像生成时和显示时的一些参数可能不匹配，例如物理相机的位置、朝向、画幅、宽高比等和显示器画面可能不同，在渲染时需要考虑。如果需要将 EasyAR 接到没有支持的 3D 引擎上，需要特别注意以下细节。
## 相机画面边界填充的剪裁
图像的剪裁、转置和编码都需要较大的计算量，出于减少计算和降低延迟的考虑，一般会使用比较原始的格式。为了方便视频编码，物理相机输出的图像经常会对齐到 8x8、16x16、32x32、64x64 这样的方格上，例如有些手机上选择 1920x1080 的分辨率，输出的图像可能变成 1920x1088，就是由于 1080 不是 64 的倍数。
![image with padding](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-crop.png)
这就要求在渲染的时候去掉这些多余的填充部分。有多种可能的做法：一种是在将图像上传到显存时指定宽度，例如 OpenGL 中可以使用`glPixelStorei(GL\_PACK\_ROW\_LENGTH, ...)`实现；一种是在 fragment shader 中手动计算 UV 坐标，并在从图像采样时将超过的部分截断。
## 跟随屏幕旋转方向渲染
在手机上，物理相机记录的图像通常相对于机身固定，不随屏幕显示方向变化而变化。但手机机身朝向的变化会影响到我们对于图像的上下左右方向的定义。渲染时，当前屏幕显示方向也会影响到显示的图像的方向。
通常在渲染时，需要确定一个相机图像相对于屏幕显示方向的旋转角。
如果我们用 \\(\\theta\_{screen}\\) 表示屏幕图像相对于屏幕自然方向顺时针旋转的弧度，\\(\\theta\_{phycam}\\) 表示物理相机图像要正确显示在自然方向的屏幕上需要顺时针旋转的弧度，\\(\\theta\\) 表示物理相机图像显示在当前屏幕上需要顺时针旋转的弧度。
对于后置摄像头，有
\\[
\\theta = \\theta\_{phycam} - \\theta\_{screen}
\\]
例如，Android 手机上，在自然方向使用手机时，\\(\\theta\_{screen} = 0, \\theta\_{phycam} = \\frac{\\pi}{2}\\)，则 \\(\\theta = \\frac{\\pi}{2}\\)。
对于前置摄像头，如果在旋转完成后，进行左右方向翻转，则有
\\[
\\theta = \\theta\_{phycam} + \\theta\_{screen}
\\]
> **注意**
当屏幕图像旋转时，需要在旋转发生后的第一帧立刻重新计算 \\(\\theta\\)，否则可能出现瞬间的屏幕图像方向不正常。
## 相机背景和虚拟物体的渲染
在手机上渲染虚拟物体，需要将虚拟物体和相机画面对准。这要求我们将渲染相机和物体都放置在和真实空间完全对应的虚拟空间中，并使用物理相机相同的视场角、宽高比来进行渲染。相机画面和虚拟物体经过的透视投影变换几乎一模一样，只有一点区别，即相机画面的透视投影变换大部分是发生在物理相机中，而虚拟物体的透视投影变换完全是一个计算过程。
以下均采用 OpenGL 惯例，使用其他惯例，需要进行相应的坐标轴映射。假设相机坐标系的坐标轴定义如下：x 轴指向右，y 轴指向上，z 轴出屏幕向外。剪裁坐标系的坐标轴定义如下：x 轴指向右，y 轴指向上，z 轴出屏幕向外，w 轴为虚拟轴。
此时，渲染相机画面需要的透视投影变换矩阵如下：
\\[
P\_i=\\left(
\\begin{array}{cccc}
(-1)^{\\text{flip}} & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & 1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
\\cos (-\\theta ) & -\\sin (-\\theta ) & \\phantom{0} & \\phantom{0} \\\\
\\sin (-\\theta ) & \\cos (-\\theta ) & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
s\_x & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & s\_y & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)
\\]
其中：`flip`是指画面是否左右翻转，翻转时值为 1，不翻转时值为 0；\\(\\theta\\) 是图像沿顺时针旋转角，单位为弧度； \\(s\_x\\) 、 \\(s\_y\\) 是缩放系数，用于进行等比缩放或等比填充，它们随 \\(\\theta\\) 变化。此变换矩阵首先对相机图像进行缩放，然后进行旋转，最后进行翻转。渲染时应使用一个矩形铺满屏幕，例如在 OpenGL 中，可以将矩形的顶点放在 \\((-1, -1, 0)\\) 、 \\((1, -1, 0)\\) 、 \\((1, 1, 0)\\) 、 \\((-1, 1, 0)\\) ，UV 坐标设置在对应的四个角上，然后使用此透视投影矩阵渲染。
渲染虚拟物体需要的透视投影矩阵如下：
\\[
P=P\_i\\left(
\\begin{array}{cccc}
1 & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & 1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -\\frac{f+n}{f-n} & -\\frac{2 f n}{f-n} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
\\frac{2}{w} & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\frac{2}{h} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & -1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
f\_x & \\phantom{0} & c\_x & \\phantom{0} \\\\
\\phantom{0} & f\_y & c\_y & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & 1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 & \\phantom{0} & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & -1 & \\phantom{0} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & \\phantom{0} & 1 \\\\
\\end{array}
\\right)
\\]
其中： \\(n\\) 、 \\(f\\) 是通常 3D 渲染的透视投影矩阵中使用的近裁和远裁参数； \\(w\\) 、 \\(h\\) 是相机图像的像素宽高； \\(f\_x\\) 、 \\(f\_y\\) 、 \\(c\_x\\) 、 \\(c\_y\\) 为相机模型中常用的内参，其中 \\(f\_x\\) 、 \\(f\_y\\) 是像素焦距， \\(c\_x\\) 、 \\(c\_y\\) 为主点像素位置。此投影投影矩阵依次进行如下变换：相机内参的透视投影变换（由于 OpenCV 中图像坐标系 y、z 轴方向和 OpenGL 相机坐标系相反，进行了两次坐标系变换），从图像像素坐标系转换到图像矩形坐标系的变换，近裁和远裁的变换，渲染相机画面时的透视投影变换。
经过整理，可得
\\[
P=P\_i\\left(
\\begin{array}{cccc}
\\frac{2 f\_x}{w} & \\phantom{0} & 1-\\frac{2 c\_x}{w} & \\phantom{0} \\\\
\\phantom{0} & \\frac{2 f\_y}{h} & -1+\\frac{2 c\_y}{h} & \\phantom{0} \\\\
\\phantom{0} & \\phantom{0} & -\\frac{f+n}{f-n} & -\\frac{2 f n}{f-n} \\\\
\\phantom{0} & \\phantom{0} & -1 & \\phantom{0} \\\\
\\end{array}
\\right)
\\]
从上述过程可知，渲染通常需要分两次进行，一次渲染相机画面，一次渲染虚拟物体，虚拟物体覆盖在相机画面之上。
有些 3D 引擎中将透视投影矩阵表示为横向视场角、宽高比等参数，如果不考虑旋转、翻转，忽略主点偏移，是可以计算的，其中横向视场角 \\(\\alpha=2 arctan{\\frac{w}{2 f\_x}}\\) ，宽高比 \\(r=\\frac{w}{h}\\) 。
需要注意这个过程中没有考虑相机畸变的情况，因为目前大部分手机的相机畸变非常轻微。

---

## 3D 空间内容展示
- 章节路径: `native/fundamentals/contents.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/contents.html

# 3D 空间内容展示
使用 AR 时，通常需要展示虚拟物体。在简单的测试示例中，可以使用简单的几何体，但要面向消费者开发时，一般需要显示高精度的3D 模型和动画，并可能会在点击模型结点时触发事件和交互。
## 模型
当前比较流行的 3D 模型，一般由三角形网格（triangle mesh）构成。为了让模型看起来真实，我们需要为每个三角形赋予材质 （material）。材质通常实现某种光照模型，其内容由贴图和光照模型参数构成。
* 贴图（texture）决定三角形中每个点的基础颜色，所有三角形的贴图会放在一张或多张漫反射贴图中。在一些进阶用法中，还可以使用贴图表示每个点的法线方向或者其他参数。
* 光照模型（lighting model）定义物体如何与光线交互，常见的有 PBR。光照模型通常使用 shader 来实现。PBR 光照模型的参数有颜色、金属度、粗糙度等。
在应用开发中，一般不会直接在 OpenGL / Metal / Vulkan / Direct3D 上加载 3D 模型，而是使用 3D 引擎来进行加载。3D 引擎会要求使用一些特定的 3D 模型格式，例如历史悠久、较为可读的obj / mtl 格式，以及目前比较流行的 glTF 格式。
## 动画
为了让模型运动，需要使用骨骼动画。骨骼是指的 3D 模型中做刚体运动时保持一致运动的大块模型结点。
显示动画，需要在运行时不断更新模型结点的位置和姿态（变换矩阵）。大部分 3D 引擎会提供动画功能，只需要在动画制作软件中编辑好动画，并以 3D 引擎支持的格式导出，即可在 3D 引擎中使用。上述 glTF 格式也包含动画的功能。
## 交互
用户点击模型结点时，有时候需要触发事件和交互。一般会对骨骼动画中的骨骼进行命名，并使用碰撞检测或射线检测，在点击时触发事件，返回被点击的骨骼名称。事件的处理，可以使用脚本或者应用代码来进行。
> **注意**
如果您缺少 3D 引擎的使用经验，强烈建议您考虑使用 Unity 来开发您的应用。EasyAR Sense Unity Plugin 对 Unity 有较好的支持，如果您使用其他的 3D 引擎，可能会面临支持和可用资源较少的问题。

---

## EasyAR 坐标系
- 章节路径: `native/fundamentals/coordinates.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/coordinates.html

# EasyAR 坐标系
3D 程序中，坐标系的定义非常重要。如果没有特别说明，则采用以下惯例。
* 向量均为列向量。
* 矩阵均采用 row-major。（OpenGL 为 column-major）
* 坐标系均采用右手坐标系。(与 OpenGL 一致)
* 坐标系如果存在物理标尺，则单位使用米。
* 世界坐标系的 Y 轴负方向为重力方向。
* 设备坐标系的 X 轴向右，Y 轴向上，Z 轴为屏幕向外；对于屏幕可以旋转的设备，右和上的定义以其默认方向为准，特别的，Android 的默认方向遵循系统定义。（眼镜和部分平板的横屏放置为默认方向，手机和部分平板竖屏放置为默认方向），iOS 的默认方向为竖屏放置。（与 Android 和 iOS 的 IMU 说明中的定义一致）
## 物体跟踪的 pose
平面图像跟踪（[ImageTracker](../../../api/native/easyar.ImageTracker.html)）和3D物体跟踪（[ObjectTracker](../../../api/native/easyar.ObjectTracker.html)）的物体 pose 存放在 [pose](../../../api/native/easyar.TargetInstance.html#n_easyar_TargetInstance_pose)，表示当前被跟踪的 target 相对于 camera 的位姿。其中 camera 坐标系与 target 坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，指的是相机图像中的右和上，可能和设备自然方向的可能不同。）数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。
pose 可写成：
\\[
P = \\left(
\\begin{array}{cccc}
p\_{11} & p\_{12} & p\_{13} & p\_{14} \\\\
p\_{21} & p\_{22} & p\_{23} & p\_{24} \\\\
p\_{31} & p\_{32} & p\_{33} & p\_{34} \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)
\\]
如果 3D 引擎采用了其他的坐标轴定义，则在 3D 引擎中设置变换矩阵时需要考虑，例如 camera 坐标系和 target 坐标系的 z 方向均相反时，应设置 3D 引擎的 target 结点变换矩阵值为：
\\[
\\left(
\\begin{array}{cccc}
1 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 \\\\
0 & 0 & -1 & 0 \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
p\_{11} & p\_{12} & p\_{13} & p\_{14} \\\\
p\_{21} & p\_{22} & p\_{23} & p\_{24} \\\\
p\_{31} & p\_{32} & p\_{33} & p\_{34} \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 \\\\
0 & 0 & -1 & 0 \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)=\\left(
\\begin{array}{cccc}
p\_{11} & p\_{12} & -p\_{13} & p\_{14} \\\\
p\_{21} & p\_{22} & -p\_{23} & p\_{24} \\\\
-p\_{31} & -p\_{32} & p\_{33} & -p\_{34} \\\\
0 & 0 & 0 & 1 \\\\
\\end{array}
\\right)
\\]
## 运动跟踪的 transform
表面跟踪（[SurfaceTracker](../../../api/native/easyar.SurfaceTracker.html)） 的 [transform](../../../api/native/easyar.SurfaceTrackerResult.html#n_easyar_SurfaceTrackerResult_transform) 和运动跟踪（[MotionTrackerCameraDevice](../../../api/native/easyar.MotionTrackerCameraDevice.html)）、ARKit（[ARKitCameraDevice](../../../api/native/easyar.ARKitCameraDevice.html)）、ARCore（[ARCoreCameraDevice](../../../api/native/easyar.ARCoreCameraDevice.html)）的 [cameraTransform](../../../api/native/easyar.InputFrame.html#n_easyar_InputFrame_cameraTransform)，表示 camera 相对于世界坐标系的变换。其中 camera 坐标系与世界坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，在移动设备上指设备自然方向的右和上。）世界坐标系的 y 轴向上（与重力方向相反），原点由运动跟踪系统决定。数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。
## 稀疏空间地图和 Mega 中的 pose
稀疏空间地图 [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html) 的 [getMapPose](../../../api/native/easyar.SparseSpatialMapResult.html#n_easyar_SparseSpatialMapResult_getMapPose)和 Mega 中的 [pose](../../../api/native/easyar.MegaTrackerBlockInstance.html#n_easyar_MegaTrackerBlockInstance_pose)，表示地图 block 在 camera 坐标系中的位置和姿态。其中 camera 坐标系与世地图 block 坐标系均为右手坐标系。camera 坐标系的原点为相机光心，x 轴正方向为右，y 轴正方向为上，z 轴正方向为光线进入相机（出屏幕）的方向。（其中的右和上，在移动设备上指设备自然方向的右和上。）地图 block 坐标系的 y 轴向上（与重力方向相反），原点由地图 block 数据决定。数据的排列方式为 row-major，与 OpenGL 的 column-major 相反。

---

## AR 数据流
- 章节路径: `native/fundamentals/dataflow.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/dataflow.html

# AR 数据流
本文介绍了 EasyAR Sense 中的数据流。EasyAR Sense 中使用组件化 API，组件之间通过数据流来连接。
## 输入输出数据
![fundamentals dataflow input output](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-input-output.png)
[InputFrame](../../../api/native/easyar.InputFrame.html)：输入帧。包含图像、camera 参数、时间戳、相机相对于世界坐标系的变换和跟踪状态。其中，camera 参数、时间戳、相机相对于世界坐标系的变换和跟踪状态均为可选，但特定的算法组件会对输入有特定的要求。
[OutputFrame](../../../api/native/easyar.OutputFrame.html)：输出帧。包含输入帧和同步处理组件的输出结果。
[FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html)：反馈帧。包含一个输入帧和一个历史输出帧，用于 [ImageTracker](../../../api/native/easyar.ImageTracker.html) 等反馈式同步处理组件。
## Camera组件
[CameraDevice](../../../api/native/easyar.CameraDevice.html)：Windows、Mac、iOS、Android 上的默认摄像头。
[ARKitCameraDevice](../../../api/native/easyar.ARKitCameraDevice.html)：iOS 上的 ARKit 默认实现。
[ARCoreCameraDevice](../../../api/native/easyar.ARCoreCameraDevice.html)：Android 上的 ARCore 默认实现。
[MotionTrackerCameraDevice](../../../api/native/easyar.MotionTrackerCameraDevice.html)：实现运动跟踪，通过多传感器融合解算设备的 6DoF 坐标。(只支持 Android )
[ThreeDofCameraDevice](../../../api/native/easyar.ThreeDofCameraDevice.html)：在默认摄像头的基础上，增加了 3DoF 的方向。
[InertialCameraDevice](../../../api/native/easyar.InertialCameraDevice.html)：在默认摄像头的基础上，增加了 3DoF 的方向和平面的基于惯性估计的平移。
custom camera device：自定义摄像头实现。
## 算法组件
反馈式同步处理组件：需要每帧跟着摄像机图像输出结果，并且需要上一帧处理结果用于避免相互干扰。
* [ImageTracker](../../../api/native/easyar.ImageTracker.html)：实现了平面图像的检测和跟踪。
* [ObjectTracker](../../../api/native/easyar.ObjectTracker.html)：实现了 3D 物体的检测和跟踪。
同步处理组件：需要每帧跟着摄像机图像输出结果。
* [SurfaceTracker](../../../api/native/easyar.SurfaceTracker.html)：实现了对环境表面的跟踪。
* [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html)：实现了稀疏空间地图，提供了扫描物理空间同时生成点云地图并进行实时定位的能力。
* [MegaTracker](../../../api/native/easyar.MegaTracker.html)：实现了 Mega 空间定位。
异步处理组件：不需要每帧跟着摄像机图像输出结果。
* [CloudRecognizer](../../../api/native/easyar.CloudRecognizer.html)：实现了云识别。
* [DenseSpatialMap](../../../api/native/easyar.DenseSpatialMap.html)：实现了稠密空间地图，可用于实现碰撞、遮挡等效果。
## 组件的可用性检查
所有的组件均有 isAvailable 函数，可用于判断该组件是否可用。
组件不可用的情况有
* 当前操作系统上没有实现。
* 组件所需要的依赖不存在，例如 ARKit、ARCore。
* 组件在当前版本（variant）上不存在，例如一些精简版本中某些功能不存在。
* 组件在当前 License 下不可用。
使用组件之前务必要判断组件是否可用，并进行相应的 fallback 或者提示。
## 数据流
组件的连接方式如下图所示。
![fundamentals dataflow](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow.png)
有一种特殊的输入为反馈式帧的用法，如下图所示。
![fundamentals dataflow feedback](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-feedback.png)
## 数据流辅助类
数据流的发出和接收端口，各组件需要包含这些端口
* [SignalSink](../../../api/native/easyar.SignalSink.html) / [SignalSource](../../../api/native/easyar.SignalSource.html)：接收/发出一个信号(无数据)。
* [InputFrameSink](../../../api/native/easyar.InputFrameSink.html) / [InputFrameSource](../../../api/native/easyar.InputFrameSource.html)：接收/发出一个 [InputFrame](../../../api/native/easyar.InputFrame.html)。
* [OutputFrameSink](../../../api/native/easyar.OutputFrameSink.html) / [OutputFrameSource](../../../api/native/easyar.OutputFrameSource.html)：接收/发出一个 [OutputFrame](../../../api/native/easyar.OutputFrame.html)。
* [FeedbackFrameSink](../../../api/native/easyar.FeedbackFrameSink.html) / [FeedbackFrameSource](../../../api/native/easyar.FeedbackFrameSource.html)：接收/发出一个 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html)。
数据流的分支和合并
* [InputFrameFork](../../../api/native/easyar.InputFrameFork.html)：将一个 [InputFrame](../../../api/native/easyar.InputFrame.html) 分成多个并行发出。
* [OutputFrameFork](../../../api/native/easyar.OutputFrameFork.html)：将一个 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 分成多个并行发出。
* [OutputFrameJoin](../../../api/native/easyar.OutputFrameJoin.html)：将多个 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 合并成一个，并将所有的结果合并到 Results 中。需要注意其多个输入的连接不应该在有数据流入的同时进行，否则可能会陷入不能输出的状态。（推荐在 Camera 启动之前完成数据流连接。）
* [FeedbackFrameFork](../../../api/native/easyar.FeedbackFrameFork.html)：将一个 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html) 分成多个并行发出。
数据流的限流和缓存
* [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html)：接收并发出 [InputFrame](../../../api/native/easyar.InputFrame.html)，但一次只发出一个，只有在接收到一个触发信号后才会发出下一个 [InputFrame](../../../api/native/easyar.InputFrame.html)，接收到多个 [InputFrame](../../../api/native/easyar.InputFrame.html) 时，后续的 [InputFrame](../../../api/native/easyar.InputFrame.html) 可能会覆盖前面的 [InputFrame](../../../api/native/easyar.InputFrame.html)。
* [OutputFrameBuffer](../../../api/native/easyar.OutputFrameBuffer.html)：接收 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 并缓存，等待用户轮询，接收到 [OutputFrame](../../../api/native/easyar.OutputFrame.html) 的时候可以发出一个信号。
* 将 [OutputFrameBuffer](../../../api/native/easyar.OutputFrameBuffer.html) 发出的信号接到 [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html) 上，即可完成整个限流过程。
数据流的转换
* [InputFrameToOutputFrameAdapter](../../../api/native/easyar.InputFrameToOutputFrameAdapter.html)：可以将一个 [InputFrame](../../../api/native/easyar.InputFrame.html) 直接包装成 [OutputFrame](../../../api/native/easyar.OutputFrame.html)，用于渲染显示。
* [InputFrameToFeedbackFrameAdapter](../../../api/native/easyar.InputFrameToFeedbackFrameAdapter.html)：可以将一个 [InputFrame](../../../api/native/easyar.InputFrame.html) 和一个 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html) 包装成 [FeedbackFrame](../../../api/native/easyar.FeedbackFrame.html)，用于反馈式同步处理组件。
## InputFrame数量的限制
[CameraDevice](../../../api/native/easyar.CameraDevice.html) 可以设置 bufferCapacity，即发出 [InputFrame](../../../api/native/easyar.InputFrame.html) 的最大数量，当前的默认值为8。
自定义摄像头可以使用 [BufferPool](../../../api/native/easyar.BufferPool.html) 实现。
各组件需要的 [InputFrame](../../../api/native/easyar.InputFrame.html) 数量，参考各组件的 API 文档。
如果 [InputFrame](../../../api/native/easyar.InputFrame.html) 数量不足，可能造成数据流卡住，导致渲染卡住。
如果 [InputFrame](../../../api/native/easyar.InputFrame.html) 数量不足，也可能出现第一次启动渲染不卡住但切换到后台或暂停/启动各组件后渲染卡住的情况，测试时需要注意覆盖。
## 连接和断开连接
不推荐在数据流运行过程中连接和断开连接。
如果需要在运行过程中进行连接和断开连接，需要注意只能在割边（去掉这条边后数据流会一分为二）上进行，不能在环的边（这里的环指的是将数据流看作无向图时边构成的环）上、 [OutputFrameJoin](../../../api/native/easyar.OutputFrameJoin.html) 的输入或者 [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html) 的 sideInput 上进行，否则可能会陷入数据流卡在 [OutputFrameJoin](../../../api/native/easyar.OutputFrameJoin.html) 和 [InputFrameThrottler](../../../api/native/easyar.InputFrameThrottler.html) 等结点无法输出的状态。
算法组件均有 start/stop 功能，在 stop 的时候，帧将不会被处理，但仍然会从组件中输出，只是不带有结果。
## 典型用法
以下为单个 [ImageTracker](../../../api/native/easyar.ImageTracker.html) 的用法，可用于识别、跟踪不重复的平面识别图。
![fundamentals dataflow single ImageTracker](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-single-ImageTracker.png)
以下为单个 [ImageTracker](../../../api/native/easyar.ImageTracker.html) 的用法，可用于识别、跟踪重复的平面识别图。
![fundamentals dataflow multiple ImageTracker](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-multiple-ImageTracker.png)
以下为 [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html) 的用法，可用于实现稀疏空间地图建图和定位、跟踪。
![fundamentals dataflow SparseSpatialMap](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-SparseSpatialMap.png)
以下为 [SparseSpatialMap](../../../api/native/easyar.SparseSpatialMap.html) 和 [DenseSpatialMap](../../../api/native/easyar.DenseSpatialMap.html) 同时使用的用法，可用于实现稀疏空间地图建图、定位、跟踪和稠密空间地图生成。
![fundamentals dataflow Sparse-DenseSpatialMap](https://doc-asset.easyar.com/develop/native/fundamentals/media/fundamentals-dataflow-Sparse-DenseSpatialMap.png)

---

## 库加载和初始化
- 章节路径: `native/fundamentals/initialization.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/initialization.html

# 库加载和初始化
在使用 EasyAR Sense 的功能之前，需要进行初始化。初始化时，EasyAR Sense 会建立一些必要的环境，并验证 License Key。
## 非 Android 平台
对于 iOS/macOS/visionOS/Windows 平台，一般通过编译时动态链接来实现库的加载，参考示例添加对 EasyAR 库的引用，并在需要时添加 EasyAR 库的头文件即可。
初始化只需要调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_System_String_) 并传入 license key 即可。
## Android 平台
对于 Android 平台，一般是通过 java.lang.System.loadLibrary 来进行动态库的加载。
初始化只需要调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_android_app_Activity_System_String_) 并传入当前 Activity 和 License Key 即可，其中会自动调用 java.lang.System.loadLibrary。
如果您需要将 libEasyAR.so 放在非默认位置（例如需要在运行过程中动态下载），则您需要改为调用 [initialize](../../../api/native/easyar.Engine.html#n_easyar_Engine_initialize_android_app_Activity_System_String_System_String_) 并传入当前 Activity、License Key 和 libEasyAR.so 存放路径。
如果您有更复杂的需求，可以将加载 libEasyAR.so，设置 Activity 和验证 License Key 三个步骤分开进行。您可以先调用 [loadLibraries](../../../api/native/easyar.Engine.html#n_easyar_Engine_loadLibraries_System_String_)，再调用[setupActivity](../../../api/native/easyar.Engine.html#n_easyar_Engine_setupActivity)，再调用 [initializeKey](../../../api/native/easyar.Engine.html#n_easyar_Engine_initializeKey)。

---

## 在进行增强现实开发前选择一款 3D 引擎
- 章节路径: `native/getting-started/choosing-an-engine.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/choosing-an-engine.html

# 在进行增强现实开发前选择一款 3D 引擎
AR 开发的第一步是选择合适的 3D 引擎，这一章介绍为什么需要 3D 引擎、AR 开发中常见的 3D 引擎及各自优缺点。
## 为什么 AR 需要 3D 引擎
增强现实并不是简单地在相机画面上叠加 2D 或 3D 图像，而是一个实时三维系统，其核心能力可能还包括：
* 真实相机建模
为了渲染的虚拟物体看起来在现实中更真实，需要根据实际相机画面使用的参数（例如内外参，畸变模型等）调整用于渲染的 3D 引擎中的摄像机的投影矩阵。
* 空间坐标系统管理
统一管理设备、环境、AR 内容等之间的位置和姿态，负责世界坐标、相机坐标、设备坐标之间的选择、设置和转换。
* 实时三维渲染
根据实时估计的场景深度或重建的网格实现虚拟物体和环境的真实遮挡效果，根据光照估计算法模拟阴影，实现逼真的虚实融合效果。
* 资源与生命周期管理
管理虚拟的 AR 资源、内容，覆盖其加载、展示、卸载等生命周期管理。
这些能力构成了典型 3D 引擎的核心职责。因此根据具体的项目需求，选择合适的 3D 引擎是快速实现 AR 效果的必要前提之一。
## 常见的 3D 引擎
EasyAR 支持多种 3D 引擎，包括常见的 3D 引擎如 Unity，Unreal 或者原生开发(Native)。 EasyAR 提供 Unity 和 Native 的样例及开发文档。
### Unity
Unity 定位通用实时 3D 引擎， 是当前大多数 AR 开发者的第一选择。Unity 原生支持 Windows/ macOS 以及 iOS / Android / visionOS 等跨平台开发。 Unity 生态成熟，文档与示例完善。
### Native
相较于使用 Unity 等高层封装引擎，直接基于原生图形 API（如 OpenGL、Vulkan、Metal）进行 AR 开发的优势可概括如下：系统依赖少，运行环境可极度精简，可深度定制相机模型及底层算法。原生 API 开发，工程成本和维护成本高，缺乏成熟编辑器与调试工具，迭代效率低，跨平台难度大，不利于产品级快速交付，通常用于一些简单功能的实现。
### Web
Web 无需安装，基于浏览器即可使用，分发和触达成本极低。 天然跨平台，适合快速上线与大规模用户访问。 开发门槛相对较低，前端生态成熟。
目前 Web 在 AR 应用中仍然较为受限，主要体现在性能受浏览器与安全沙箱限制对运动跟踪、遮挡、精确光照等 AR 核心能力支持不足，设备能力访问受限，稳定性和一致性难以保障。
因此 Web AR 适合“轻量展示与营销”，不适合高精度、强交互的复杂 AR 应用。
## 延伸阅读
* [Android Native 快速入门](quickstart-android.html)
* [iOS Native 快速入门](quickstart-ios.html)
* [Windows Native 快速入门](quickstart-windows.html)
* [Unity 快速入门](../../unity/getting-started/quickstart.html)

---

## 在 Android 应用中启用 EasyAR 功能
- 章节路径: `native/getting-started/enable-easyar-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/enable-easyar-android.html

# 在 Android 应用中启用 EasyAR 功能
本章介绍如何在 Android Studio 中配置 EasyAR 的 Android 工程，无需使用 Unity 等 3D 引擎。
## 准备工作
开始之前，您需要准备：
* 最新版本的 Android Studio
* JDK 8/11/17
* Android Gradle Plugin 4.0 或以上
* Android NDK r28 或以上
* 获取 EasyAR 授权许可证
* 选择 EasyAR Sense [发布版本并下载](variants.html)
> **注意**
并非所有安卓设备均支持 EasyAR Sense 的所有功能，部分功能依赖额外硬件或配置，具体可查阅对应功能支持的设备列表。
## 导入 EasyAR Sense for Android
本节介绍如何在**非 Unity 的 Android 工程**中导入 EasyAR Sense SDK。 EasyAR Sense 提供 Java 和 C++ API，并支持 Kotlin，您可以使用最习惯的语言进行开发。
由于不同 IDE 的配置方式可能存在差异，这里仅说明**基于 Android Studio + Gradle 的典型配置方式**。
### 选择 API 使用方式
EasyAR Sense for Android 提供两种 API 使用方式：
* 仅使用 Java API
* 使用 Java 和 C++ API
请根据项目需求选择其中一种进行配置。
#### 仅使用 Java API
当仅使用 EasyAR 的 Java API 时，**无需配置 NDK**。
将 `EasyAR.aar` 放入`app/libs/` 或 Gradle 指定目录。
#### 使用 Java 和 C++ API
当需要同时使用 EasyAR 的 C++ API 时，需要同时配置 Java 依赖与原生库。
* Java 层文件
将 `EasyAR.jar` 放入 `app/libs/` 或 Gradle 指定路径。
* 原生库（`.so`）
将 EasyAR 提供的原生库按 ABI 放入以下路径或 Gradle 指定路径。
```
app/src/main/jniLibs/
├── armeabi-v7a/
│ └── libEasyAR.so
└── arm64-v8a/
└── libEasyAR.so
```
* C++ 头文件
将 EasyAR SDK 中 `include` 目录下的 `easyar` 文件夹拷贝到以下路径或 `Android.mk`/`CMakeLists.txt` 指定路径。
```
app/src/main/jni/easyar/
```
头文件路径需在 `Android.mk` 或 `CMakeLists.txt` 中显式指定。
### Gradle 配置说明
当您使用 C++ API 时，需要在 Gradle 中启用 Native Build, **仅适用 Java API 无需配置**。 您可以使用 ndk-build（Android.mk）进行配置。
在 `app/build.gradle` 中添加：
```
android {
externalNativeBuild {
ndkBuild {
path "src/main/jni/Android.mk"
}
}
}
```
>
> 如果使用 CMake，请参考
[> Google 官方文档
](https://developer.android.google.cn/studio/projects/add-native-code.html)> 进行配置。
>
### NDK 配置
#### 声明 EasyAR 为预编译库
```
include $(CLEAR\_VARS)
# 确保该路径指向 jniLibs 中当前 ABI 目录
LOCAL\_PATH := $(LOCAL\_PATH\_TOP)/../jniLibs/$(TARGET\_ARCH\_ABI)
LOCAL\_MODULE := EasyAR
LOCAL\_SRC\_FILES := libEasyAR.so
include $(PREBUILT\_SHARED\_LIBRARY)
```
#### 链接 EasyAR 与系统库
```
LOCAL\_SHARED\_LIBRARIES += EasyAR
# OpenGL ES（必需）
LOCAL\_LDLIBS += -lGLESv3
```
>
> EasyAR 运行至少需要 OpenGL ES 2.0，推荐使用 OpenGL ES 3.0（GLESv3）。
>
### 指定 ABI 架构
在 `app/build.gradle` 中显式指定 ABI，避免无效架构被打包：
```
android {
defaultConfig {
ndk {
abiFilters "armeabi-v7a", "arm64-v8a"
}
}
}
```
如果只需要其中一种架构，可只保留对应项。
### AndroidManifest 权限配置
EasyAR Sense 需要以下权限，缺失将导致初始化失败或黑屏：
```
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
```
完整示例：
```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
package="cn.easyar.samples.helloar">
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.INTERNET" />
</manifest>
```
### 初始化 EasyAR
在应用启动时调用 `Engine.initialize` 进行初始化。
示例（Java）：
```
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
Engine.initialize(this, key);
}
```
> **注意**
初始化必须在使用 EasyAR 相关功能之前完成。
## 额外配置
在 Android 平台上，根据系统版本及所使用的功能不同，可能还需要注意以下配置和限制。
### 配置使用 ARCore
如果项目中使用 **ARCore**，请参考其官方文档完成 `AndroidManifest.xml` 和 `build.gradle` 的相关配置。
此外，在初始化 EasyAR 之前，必须显式加载 ARCore 的原生库：
```
System.loadLibrary("arcore\_sdk\_c");
```
> **注意**
使用 **ARCore v1.19.0 之前的版本**时，在 **Android 11** 上将无法被检测到。
这是由于 Android 11 开始引入了应用可见性限制，需要在 `AndroidManifest.xml` 中声明 ARCore 包名。
```
<queries>
<package android:name="com.google.ar.core" />
</queries>
```
### 配置混淆（ProGuard）
如果对 Java 代码启用混淆，需要 **排除 `cn.easyar` 命名空间**。
EasyAR Sense 在运行时会通过 JNI 使用 **类名反射获取 Java 类型**。
如果 `cn.easyar` 下的类被混淆或重命名，可能导致未定义行为。
#### 基本规则
```
-keep class cn.easyar.\*\* { \*; }
```
#### 推荐的精确规则
```
-dontwarn javax.annotation.Nonnull
-dontwarn javax.annotation.Nullable
-keepattributes \*Annotation\*
-keep class cn.easyar.RefBase { native <methods>; }
-keepclassmembers class cn.easyar.\* {
<fields>;
protected <init>(long, cn.easyar.RefBase);
}
-keep,allowobfuscation interface cn.easyar.FunctorOf\* { \*; }
-keep class cn.easyar.Buffer { native <methods>; }
-keep class cn.easyar.Engine { native <methods>; }
-keep class cn.easyar.JniUtility { native <methods>; }
-keep class cn.easyar.engine.\*\* { \*; }
-keep class cn.easyar.CameraParameters
-keep interface cn.easyar.FunctorOfVoidFromInputFrame
```
上述 ProGuard 规则 **已包含在 EasyAR 的 aar 库中**，通常无需重复配置。
### Scoped Storage
Android 10 开始引入的 **Scoped Storage（分区存储）** 机制，会对部分依赖文件路径的 API 造成影响。这是由于 /sdcard 下的非媒体路径（如自定义目录）在 Android 10 上无法直接访问所致。对 EasyAR 的影响体现在部分需要传入文件路径的 API（如录屏）在 Android 10 上，不支持直接读写媒体路径，但是在 Android 11 上可以正常工作。
**解决方式**：
* 简便方案（Android 10）
在 `AndroidManifest.xml` 中禁用 Scoped Storage：
```
<application
android:requestLegacyExternalStorage="true"
... >
</application>
```
* 推荐方案
* 仅使用应用内部存储
* 或通过 MediaStore 与媒体路径进行数据交换
### Android Gradle Plugin 与 NDK
自 NDK r22 起，默认使用 LLD 链接器，并需要配合 `llvm-strip` 使用；这与 Android Gradle Plugin 4.0 以下版本内置的 `strip` 工具不兼容。
**解决方式**:
* 升级至 **Android Gradle Plugin 4.0 或以上**
* 或在 `packagingOptions` 中使用 `doNotStrip` 禁用 stripping（不推荐）
### Windows 路径长度限制
在 Windows 系统上，如果工程中任意文件（包括构建过程中生成的临时文件）的**绝对路径长度超过 260 个字符**，
可能会导致 Android Studio 构建失败。
**解决方式**：
* 将工程放置在更短路径下（例如 `C:\\user\\project`）
* 避免过深的目录层级
## 延伸阅读
* [EasyAR Mega 支持的设备](../../mega/devices.html)
* [图像跟踪支持的设备](../../image-tracking/devices.html)
* [运动跟踪支持的设备](../../motion-tracking/devices.html)
* [稀疏空间地图支持的设备](../../sparse-spatial-mapping/devices.html)
* [稠密空间地图支持的设备](../../dense-spatial-mapping/devices.html)
* [运动跟踪与 EasyAR 其他模块的关系](../../motion-tracking/motion-tracking-and-easyar.html)

---

## 在 iOS 应用中启用 EasyAR 功能
- 章节路径: `native/getting-started/enable-easyar-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/enable-easyar-ios.html

# 在 iOS 应用中启用 EasyAR 功能
本章介绍如何在 Xcode 中配置 EasyAR 的 iOS 工程 ， 而不需使用 Unity 等 3D 引擎。
## 准备工作
开始之前，您需要准备：
* Xcode 16 或更新版本
* 获取 EasyAR 授权许可证
* 选择 EasyAR Sense [发布版本并下载](variants.html)
## 使用 Objective-C 启用 EasyAR
1. 添加 Frameworks
在 `Frameworks, Libraries, and Embedded Content` 中添加 `easyar.xcframework`。
![addxframework1](https://doc-asset.easyar.com/develop/native/getting-started/media/xfframework.png)
2. 禁用 Bitcode
EasyAR 不使用 bitcode 也不提供 bitcode 兼容性, 需要在配置中禁用 bitcode。
![disablebitcode2](https://doc-asset.easyar.com/develop/native/getting-started/media/disablebitcode.png)
3. 初始化 EasyAR
使用 `easyar\_Engine` 的 `initialize:` 方法来初始化 EasyAR 。您可以添加初始化代码如下
```
[easyar\_Engine initialize:key];
```
4. 隐私配置
由于 AR 要使用摄像头，隐私配置需要添加 `Privacy - Camera Usage Description`，
![campermission](https://doc-asset.easyar.com/develop/native/getting-started/media/camerapermission.png)
如果要使用录屏功能，隐私配置需要添加 `Privacy - Microphone Usage Description`，
![microphonepermission](https://doc-asset.easyar.com/develop/native/getting-started/media/mcpermission.png)
## 通过 Swift API 启用 EasyAR
EasyAR Sense Swift API 是以源代码形式提供的，这样可以提供最好的兼容性（苹果从 Swift 5 开始提供 ABI 兼容）。
使用 EasyAR Sense Swift API 需要首先创建一个 framework 工程，然后将 framework target 嵌入到你的工程中。
### 创建 EasyARSwift framework 工程
1. 创建一个 Cocoa Touch Framework 类型的新工程并命名为 `EasyARSwift`
你可以选择将 EasyARSwift 工程嵌入到你的 app 工程里面或创建独立的工程。
![embedprj](https://doc-asset.easyar.com/develop/native/getting-started/media/embedproject.png)
2. 导入EasyAR Swift 代码到 EasyARSwift 工程
![embedswiftcode2](https://doc-asset.easyar.com/develop/native/getting-started/media/embedproject.png)
XCode 自动生成的 EasyARSwift.h 文件并没有被使用，可以安全删除。
3. 在 build settings 中配置 `Objective-C Bridging Header`
![bridgeheader](https://doc-asset.easyar.com/develop/native/getting-started/media/bridgingheader.png)
> **注意**
这个选项在导入 swift 文件之前不会显示在 XCode 选项中，所以请一定先导入 Swift 代码再进行配置更改。
4. 导入 `easyar.xcframework` 到 EasyARSwift 工程中
![addxframework3](https://doc-asset.easyar.com/develop/native/getting-started/media/xfframework.png)
5. 关闭 Bitcode
EasyAR 不使用 bitcode 也不提供 bitcode 兼容性, 需要保证在配置中禁用 bitcode。
![disablebitcode](https://doc-asset.easyar.com/develop/native/getting-started/media/disablebitcode.png)
6. Deployment Target
根据您的 app 工程修改 `deployment target`，保证 EasyARSwift 工程的 `deployment target`比 app 工程的小或相等。
![setdeploytarget](https://doc-asset.easyar.com/develop/native/getting-started/media/setdeploytarget.png)
### 嵌入和使用 EasyARSwift framework
1. 在工程中嵌入 EasyARSwift framework
![embedswiftfw](https://doc-asset.easyar.com/develop/native/getting-started/media/embedsffw.png)
![embedswiftfw2](https://doc-asset.easyar.com/develop/native/getting-started/media/embedsffw2.png)
2. 在 Swift 源代码中 `import EasyARSwift`
![importeasyswift](https://doc-asset.easyar.com/develop/native/getting-started/media/importeasyswift.png)
代码书写方式可以参考 `HelloARSwift` 样例中的代码或 API Reference 。

---

## 运行 EasyAR Android 样例
- 章节路径: `native/getting-started/quickstart-android.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-android.html

# 运行 EasyAR Android 样例
本文介绍如何运行 EasyAR 提供的原生 Android 样例。这里以 HelloAR 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下环境：
* Android Studio 2025.1.2 或更高版本
* JDK 17
* Android NDK r28
* Android 手机
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key，注意包名与样例一致，如 HelloAR 应为 `cn.easyar.samples.helloar`
## 导入并编译样例
1. 在 Android Studio 菜单依次选择 `File -> New -> Import Project...`，选择样例所在目录导入，等待 Android Studio 完成下载和配置。
![importhelloar](https://doc-asset.easyar.com/develop/native/getting-started/media/android-studio-import-hello-ar.png)
2. 设置许可证（License Key）
根据路径找到 ARActivity.java，按照代码提示填入开发中心获取的 License Key。
![fillkey](https://doc-asset.easyar.com/develop/native/getting-started/media/android_hello_ar_fill_in_key.png)
1. 编译并运行
连接手机到电脑上，点击运行按钮，按提示在手机上运行。
![buildandrun](https://doc-asset.easyar.com/develop/native/getting-started/media/android-build-run.png)
HelloAR 实现了对平面图像的识别跟踪并叠加虚拟物体的功能。样例中识别图像在 `assets/sightplus` 路径下找到。
HelloAR 样例的运行效果如下。
![rungif](https://doc-asset.easyar.com/develop/native/getting-started/media/android-helloar.gif)
## 相关阅读
* [运行 EasyAR iOS 样例](quickstart-ios.html)
* [运行 EasyAR Windows 样例](quickstart-windows.html)

---

## 运行 EasyAR 的 iOS 样例
- 章节路径: `native/getting-started/quickstart-ios.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-ios.html

# 运行 EasyAR 的 iOS 样例
本文介绍如何运行 EasyAR 提供的原生 iOS 样例。这里以 HelloAR 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下环境：
* Xcode 16 或更高版本
* ARM64 CPU 的 iPhone 或 iPad 真机
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key，注意包名与样例一致，如 HelloAR 为 `cn.easyar.samples.helloar`
## 导入并编译样例
1. 使用 Xcode 打开下载解压的样例，如 `helloar.xcodeproj`
![openiossample](https://doc-asset.easyar.com/develop/native/getting-started/media/openiossample.png)
2. 设置许可证（License Key）
根据路径找到 `ViewController.m`，按照代码提示填入开发中心获取的 License Key。
![xcodefillkey](https://doc-asset.easyar.com/develop/native/getting-started/media/ios-fill-key.png)
3. 编译并运行
连接手机到电脑上，点击运行按钮，按提示在 iPhone /iPad 上运行样例。
HelloAR 实现了对平面图像的识别跟踪并叠加虚拟物体的功能，摄像头对准识别图（在 `assets` 文件夹下也可以找到）即可体验效果。
![namecard](https://doc-asset.easyar.com/develop/unity/headsets/media/namecard.jpg)
## 相关阅读
* [运行 EasyAR 安卓样例](quickstart-android.html)
* [运行 EasyAR Windows 样例](quickstart-windows.html)

---

## 运行 EasyAR Windows 样例
- 章节路径: `native/getting-started/quickstart-windows.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/quickstart-windows.html

# 运行 EasyAR Windows 样例
本文介绍如何运行 EasyAR 提供的原生 Windows 样例。这里以 HelloARQt 为例，介绍如何运行样例，其他样例使用方法可以参考本文。
## 准备工作
* 开始之前，请确保准备以下内容
* Visual Studio 2022 或更高版本 (有 `.vcxproj` 工程的样例)
* CMake 3.8 或更高版本 (有 `CMakeLists.txt` 的样例)
* Qt 5.4 或更高版本 (Qt 样例)
* (USB) 摄像头，插入状态并可以正常工作。
* 下载 [EasyAR Sense 原生样例](https://www.easyar.cn/view/download.html) 并解压
* 在 EasyAR 开发中心（[中文站点](https://www.easyar.cn/view/login.html) / [English Site](https://www.easyar.com/view/login.html) ）获取 License Key
> **注意**
请确保 Visual Studio 的 C++ 支持库已经安装，这些在 Visual Studio 的默认安装情况下不会自动安装。
## 编译运行 EasyAR 的 Windows 的样例
以下以 HelloARQt 为例介绍如何编译运行 EasyAR 官方 Windows 的样例。
1. 打开 CMake，指定 `where is the source code` 目录为下载解压的样例目录，设置 binary 文件的路径。
2. 点击 `Configure`, 在弹出的窗口中，选择系统的 Visual Studio 版本。如果某些路径（如 Qt）没有自动设置报错，需要手动修改，重新 `Configure`，直至没有错误。
![sample1](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample1.png)
3. 点击 `Generate`，生成工程文件。
![sample2](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample2.png)
4. 点击 `Open Project`，在 Visual Studio 中打开工程。
![sample3](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample3.png)
5. 在 Visual Studio 点击运行，在运行窗口的输入框里填写官网获取的 License Key，点击 `Start` 运行样例。
![sample4](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample4.png)
## 常见问题
1. 如果运行时提示找不到 Qt，解决方案是添加 Qt 路径到 PATH 环境变量，注销并重新登录计算机。
2. 上面介绍的 HelloARQt 是**运行时**输入 License Key ，但是也有样例需要在**运行前**填写许可证，通常在 `initialize` 代码处，如 HelloAR 样例的 License 在 `main.cc` 中填写。
![sample5](https://doc-asset.easyar.com/develop/native/getting-started/media/win_sample5.png)
## 相关阅读
* [运行 EasyAR 安卓样例](quickstart-android.html)
* [运行 EasyAR iOS 样例](quickstart-ios.html)

---

## 选择 EasyAR Sense 发布版本
- 章节路径: `native/getting-started/variants.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/getting-started/variants.html

# 选择 EasyAR Sense 发布版本
在原生开发前，需要您在官网注册并获取授权许可证，然后选择[下载对应的发布版本](https://www.easyar.cn/view/download.html)。
EasyAR Sense 分为社区版和企业版，两者授权不同，下载时需要按照许可证选择对应的文件。
* **Sense 社区版**：支持个人版、专业版、经典版的许可证。
* **Sense 企业版**：支持企业版许可证。
您下载的社区版或企业版 EasyAR Sense 均有多个发布版本，主要区别是包含的功能差异，您可以根据实际需要选择相应的发布版本。
* 社区版发布版的不同
* 社区版（Community）
包含运动跟踪、稀疏空间地图、稠密重建地图、物体跟踪、表面跟踪、平面检测等基础 AR 功能。
* 社区 R 版（CommunityR）
在社区版的基础上，额外支持 Recorder 和 VideoPlayer 功能。
* 社区 Full 版（CommunityFull）
在社区版的基础上，支持安卓平台的惯性导航功能。
* 企业版发布版的不同
* 企业（Enterprise）
包含运动跟踪、稀疏空间地图、稠密重建地图、物体跟踪、表面跟踪、平面检测等基础 AR 功能，包含企业定制功能。
* 企业 Full 版（EnterpriseFull）
在企业版的基础上，支持 Android 平台的惯性导航功能。
> **注意**
Full 版本（社区版/企业版）加入惯性导航功能，主要用于 Mega 上一些不支持 6DoF 运动跟踪功能的设备。由于包体增加比较明显，如您的应用不依赖 Mega，通常不需要 Full 版本。
## 相关阅读
[EasyAR Sense 授权许可](../../license-sense.html)

---

## EasyAR Sense 1.0 发行说明
- 章节路径: `native/release-notes/release-notes-1_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_0.html

# EasyAR Sense 1.0 发行说明
## 1.0.1
2015-10-21
EasyAR 1.0.1 修复了一些 bug，增强了用户体验。
从这个版本开始 sample 代码和 SDK 将分开打包，在网站上通过不同链接下载 （sample code 也有部分更新）。
自 EasyAR 1.0.0 版本开始的详细更新内容如下。
>
> + 添加更明显的错误信息输出
>
> + 添加使用必读
>
> * 修正在某些情况下启动速度慢的问题
>
> * 修正跟踪很容易丢失的问题
>
> * 修正在某些情况下 unity 编辑器中初始化失败的情况（即使已经填写正确的 Key）
>
> * 提升运行效率
>
> * 将示例代码单独打包
>
> * 其它修正
>
## 1.0.0
2015-10-14
EasyAR SDK 正式版本开放下载！

---

## EasyAR Sense 1.1 发行说明
- 章节路径: `native/release-notes/release-notes-1_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_1.html

# EasyAR Sense 1.1 发行说明
## 1.1.0
2015-11-29
EasyAR 1.1.0 对视频播放功能和 Unity 的支持做了大量改进，完整支持 Unity 5，增强了用户体验。
同时，这个版本增加了包括 Unity 端和本地端的大量可直接运行的样例。这些样例演示了各种 target 的创建方式和包含流媒体和透明视频在内的视频播放，以及更加高级的实时 target 创建和 AR 涂涂乐。
从这个版本开始 Unity 的 sample 代码和 SDK 将分开打包，在网站上通过不同链接下载。
样例中大多数 marker 都可以使用“视+”通过云识别来玩。这里面许多是有趣的 AR 游戏。下载
视+（ [http://www.sightp.com](http://www.sightp.com) ），一起来玩吧！
自 EasyAR 1.0.1 版本开始的详细更新内容如下。
>
> + 添加更多完整实例（单独的压缩包）
>
> + 添加透明视频支持
>
> + 完整支持 Unity 5
>
> + Unity: 添加/改善许多接口
>
> + Unity: 添加获取同步 Frame 的接口
>
> + Unity: 添加设置 Target 或 Augmenter 为世界中心的选项（该选项可在 Augmenter 物体上找到）
>
> + Unity: 开放 ARBuilder 脚本，提供从头构建 EasyAR 的参考实现
>
> * 更加完善的视频播放支持（接口有变化）
>
> * 更加完善的前置摄像头和动态摄像头切换支持
>
> * Unity: 完善 ImageTarget 在 Inspector 面板中的设置
>
> * Unity: 完善错误信息显示和新手导引
>
> * Unity: 修正 Target transform 变化后的显示
>
> * Unity5: 修正 iOS 上白屏问题
>
> * 其它修正和完善
>
> * 将 Unity 示例单独打包
>

---

## EasyAR Sense 1.2 发行说明
- 章节路径: `native/release-notes/release-notes-1_2.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_2.html

# EasyAR Sense 1.2 发行说明
## 1.2.1
2016-02-19
EasyAR 1.2.1 主要修复了 1.2.0 的一个使用问题，同时对跟踪算法做了一部分优化。这个问题只有在不正确的设置了 target 的 size 的时候才会出现，这个版本将可以容许这样的输入。
自 EasyAR 1.2.0 版本开始的详细更新内容如下。
>
> * 修正当输入 size 比例不正确的时候的闪烁和难以识别问题
>
> * 优化跟踪算法
>
## 1.2.0
2016-02-05
EasyAR 1.2.0 有两个使用体验上的显著改进。
1. 跟踪稳定性大幅提升，跟踪过程更加准确和鲁棒。
2. Unity3D 用户将不再需要在 Windows 系统中安装 Visual C++ 2015 RedistributablePackage。很多 Windows8.1 的用户将从中受益。
自 EasyAR 1.1.0 版本开始的详细更新内容如下。
>
> + 大幅提升跟踪稳定性和准确性
>
> + Unity: 移除 Visual C++运行时库依赖
>
> + Unity: 添加对 Unity 5.3+ OpenGLCore 的支持
>
> + Unity: 添加更多针对首次使用的引导
>
> + Unity: 添加关闭显示视频不支持信息的选项
>
> * 修正某些情况下 iOS 视频播放黑屏
>
> * 修正某些 Android 设备视频播放不正常
>
> * Unity: 微调整某些接口
>
> * Unity: 修正 invalid aabb
>
> * Unity: 修正 Unity 5 使用 prefab 创建场景灰屏
>
> * Unity: 修正 postbuild 脚本对 Unity 4.7 的兼容性
>
> * 其它修正和完善
>
> * 在发布包中添加一个 Unity 样例
>

---

## EasyAR Sense 1.3 发行说明
- 章节路径: `native/release-notes/release-notes-1_3.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-1_3.html

# EasyAR Sense 1.3 发行说明
## 1.3.1
2016-07-29
EasyAR 1.3.1 主要修复了某些 Android 设备的兼容性问题，并增加了中文路径（json 文件和图像路径）支持。
自 EasyAR 1.3.0 版本开始的详细更新内容如下。
>
> + 添加中文路径支持
>
> + 添加 json 文件中对"meta"数据的支持
>
> * 修正 UTF-8-BOM 编码的 json 文件解析
>
> * 修正在某些 Android 设备（Nexus 5s/6）上的 camera 显示问题
>
## 1.3.0
2016-05-28
EasyAR 1.3.0 增加了一些新特性并有很多改进，主要集中在这几方面：
1. 支持多目标。
EasyAR 现在可以支持同时跟踪多个目标。可以使用一个 tracker 进行多目标同时跟踪，也可以在不同 tracker 中加载不同的 target 来同时跟踪。EasyAR 支持运行时动态修改最大跟踪目标个数。更多使用细节请参考 [EasyAR Multi-Target](../../image-tracking/intro.html) 。
2. 接口修改，使用更加灵活。
这个版本和之前版本相比，一部分接口有所调整，但整体框架没有太大的变动。你现在可以像搭积木一样使用 EasyAR 的 Unity 基础 prefab，这个版本中也添加了很多预先搭好的模块以供参考。
3. 优化检测和跟踪，减少抖动。
4. 性能优化和降低功耗。
详细更新内容如下：
>
> + 添加多目标支持
>
> + 添加多目标的典型样例
>
> + 添加同时跟踪目标和识别二维码的样例
>
> + 提升检测和跟踪效果，减少抖动
>
> + 优化算法降低功耗
>
> + 添加直接画到 texture 的接口
>
> + 添加显式水平翻转相机输入的接口
>
> + 添加禁止 Android 自动旋转检测的接口
>
> + 添加设置外部旋转的接口
>
> + Unity: 优化渲染效率
>
> + Unity: 添加多个组合了基础 prefab 的常用 prefab
>
> + Unity: 添加 EasyARBehaviour，用以输入 key 并进行初始化，并显式处理 pause/resume/quit 事件
>
> + Unity: 添加显示/隐藏 RealityPlane 的选项
>
> + Unity: 添加使用索引打开 camera 的接口
>
> + Unity: 添加对自定义硬件设置旋转偏移的接口
>
> + Unity: 修改 AugmentedTarget 接口，支持在 FrameUpdate 事件中进行自定义的姿态滤波
>
> + Unity: 修改 Target 事件处理接口
>
> * 调整部分接口
>
> * 修正切换场景时的内存泄漏
>
> * 修正在暂停并恢复之后找到虚假的目标
>
> * 修正使用透明 PNG 图像的 target 检测
>
> * 修正因 key 中的空格导致的初始化失败
>
> * 修正 iOS 和 mac 某些分辨率下 camera 显示错误
>
> * 修正 native iOS 样例在切换到后台时崩溃
>
> * Unity: 修正在图像高比宽大的时候 ImageTarget mesh 显示错误
>
> * Unity: 修正在 OnFound 事件中重置 target
>
> * Unity: 修正 camera 打开之后有可能出现的白色帧
>
> * Unity: 修正 Augmenter 中心模式下的 TargetOnTheFly 和 Coloring3D 样例
>
> * Unity: 修正 TargetOnTheFly 样例在某些情况下崩溃的问题
>

---

## EasyAR Sense 2.0 发行说明
- 章节路径: `native/release-notes/release-notes-2_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_0.html

# EasyAR Sense 2.0 发行说明
## 2.0.0
2017-05-29
从 SDK 2.0 版本开始，EasyAR 将有两个产品，EasyAR SDK 和 EasyAR CRS (云识别服务)。EasyAR SDK 将有两个子版本，EasyAR SDK Basic 和 EasyAR SDK Pro。
EasyAR SDK 2.0 Pro 是个全新版本的 SDK，除了拥有 EasyAR SDK Basic 所有功能之外，还有更多激动人心的特性。EasyAR SDK Pro 是收费的 SDK，关于费用定价、付款方式等详细信息可以在 EasyAR 网站上查看。EasyAR SDK Pro 同时提供免费试用，试用期间 APP 每天的启动次数将会受限。
EasyAR SDK Pro 有这些全新特性：
1. 3D 物体跟踪
对日常生活中的常见有纹理 3D 物体进行实时识别与跟踪。
2. SLAM
单目实时 6 自由度相机姿态跟踪。
3. 录屏
高效易用的录屏功能。
EasyAR CRS 是云端图像识别服务，现在已经开放使用，可以在云端动态管理识别图，在 SDK 中使用对应 API 可以使用云服务识别云端存储的识别图，并从云端获取和识别图相关联的数据信息。EasyAR CRS 是收费服务，关于费用定价、付款方式等详细信息可以在 EasyAR 网站上查看。EasyAR CRS 同时提供免费试用，可以零成本测试相关功能。
EasyAR SDK 2.0 Basic 是 EasyAR SDK 1.x 的升级版。这个版本可以免费商用。EasyAR 1.x 的所有功能仍旧可以在这个版本中找到，我们没有添加任何限制或水印。EasyAR SDK 2.0 Basic 有许多改进，主要集中在这几方面：
1. 工作流和 API 改变
EasyAR 处在演化过程中，新的工作流将有更多的灵活性。我们正在完善的 EasyAR 一站式解决方案也将带给 2.0 越来越多的灵活性。这个改变在 Unity API 中表现的并不很明显，不过有些组件的名字已经变化。
2. 全新的编程语言支持
EasyAR SDK 现在导出了纯 C 接口，赋予开发者更大的自由空间。同时我们添加了对很多编程语言的支持，包括 C/C++11/traditional C++/Java for Android/Objective-C for iOS。所有的语言都有一个样例来演示基本的使用方式。我们会在未来的小版本升级中添加更多的语言支持。
3. 云识别支持
EasyAR SDK 现在内置云识别支持。
4. 许多改进、bug 修复和兼容性提升
我们提升了二维码的检测效果，调整了很多 API 以达到更高的灵活度。这个版本修复了许多 bug，包括在部分 Android 机型上显示不正确的问题和一些内存相关的问题。同时我们还提升了 EasyAR SDK 与 AMD CPU 的兼容性以及与 Unity3D、Google VR SDK 等第三方 SDK 的兼容性。
详细更新内容如下：
>
> ++ 全新的编程语言支持：C/C++11/traditional C++/Java for Android/Objective-C for iOS
>
> ++ 所有编程语言和不同 IDE 的 sample
>
> ++ 工作流和 API 变化
>
> ++ 云识别
>
> ++ 3D 跟踪 (pro)
>
> ++ SLAM (pro)
>
> ++ 录屏 (pro)
>
> + SDK API 导出为 C 接口，更容易在所有平台上导入其他语言
>
> + 添加 camera 权限申请 API
>
> + 添加 camera 缩放 API
>
> + 提升二维码检测效果
>
> + 优化内存使用
>
> + Unity: 添加默认的 found/lost 行为
>
> + Windows: DLL 将不再依赖于 CRT
>
> + Windows: 添加两个样例：一个关于如何使用 API，另一个演示在 Qt5 中的集成
>
> + Android: 添加 native 库文件的自定义加载路径和选择性加载支持
>
> - Unity: 删除了大部分非 behaviour API（所有功能被移动到了 behaviour 中）
>
> * 修复对 AMD CPU 的兼容性
>
> * 修复某些情况下渲染 camera 图像导致的 GL 状态污染
>
> * 修复视频播放前的黑色块
>
> * Unity: 修复 Unity 4.x 中 target 加载状态总是返回 true
>
> * Unity: 修复 Unity 5.0.0 和部分其他版本中屏幕闪烁
>
> * Windows: 修复某些情况下窗口关闭时崩溃
>
> * Android: 修复某些情况下调用 close 之后 camera 延迟关闭
>
> * Android: 修复从 native 线程中调用 camera API 崩溃
>
> * Android: 修复内存抖动和频繁 GC
>
> * Android: 修复在某些设备上 camera 的显示
>
> * Android: 修复某些类型 PNG 图像的加载和跟踪问题
>
> * iOS: 修复某些情况下关闭 camera 随机崩溃
>
> * iOS: 修复由于不兼容的 RTTI 配置导致的在与某些 SDK（比如 Google VR SDK）一起使用时出现的未被处理的异常（通常是 domain error）
>
> * iOS: 修复视频播放位置的时间单位
>

---

## EasyAR Sense 2.1 发行说明
- 章节路径: `native/release-notes/release-notes-2_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_1.html

# EasyAR Sense 2.1 发行说明
## 2.1.0
2017-09-08
EasyAR SDK 2.1.0 增加了一些新特性，并针对使用稳定性做了增强，主要集中在这几方面：
1. 新的编程语言支持。
EasyAR 现在支持使用 iOS 的 Swift 和 Android 的 Kotlin 进行编程。我们同时添加了在 EasyAR SDK 中使用 Swift 和 Kotlin 的样例。
2. Android arm64 支持。
EasyAR SDK 将从 2.1 版本开始添加 Android arm64-v8a 架构的文件。
3. Bug 修复和稳定性增强。
我们修复了一些由 EasyAR SDK 2.0 版本引入的 bug，包括调用 ImageTarget.setupAll 时产生的 local reference table overflow 以及 iOS 11 视频播放失败。我们同时修复了 camera 图像在屏幕上显示色彩失真的一个长期存在的问题。
详细更新内容如下：
>
> + 添加新的编程语言支持：Swift for iOS
>
> + 添加 Android 使用的 arm64-v8a 库文件
>
> + 添加新接口（Buffer），实现在 Android Java API 中访问图像数据
>
> + 添加 Android Kotlin 样例
>
> + 添加 iOS dynamic framework 样例
>
> * All: 所有接口都不会抛出异常
>
> * All: 修复 camera 图像在屏幕显示的色彩失真
>
> * Unity: 修复 iOS Unity 录屏后的系统杂音
>
> * Unity: 如果 OnPreRender 中修改了 RevertBackfacing，会在 OnPostRender 中重置
>
> * Unity: 添加 ObjectTargetBaseBehaviour 中缺失的 LoadList*接口
>
> * Unity: 默认不在 AndroidManifest 中添加音频权限
>
> * Unity: 修改容易产生误导的错误信息，"EasyAR is running on an unsupported graphics device" 改为 "EasyAR is running with an unsupported graphics API"
>
> * Android: Engine API 已经可以替换 cn.easyar.engine.EasyAR。cn.easyar.engine.EasyAR 已经弃用并将在今后版本中移除
>
> * Android: 修复调用 ImageTarget.setupAll 配置大量 target 时可能产生的 local reference table overflow
>
> * Android: 修复在 Android 平板和眼镜上 SLAM 不正常的漂移
>
> * Android: 修复在某些罕见 Android 设备上拒绝 camera 权限导致的崩溃
>
> * Android: 改善在某些罕见 Android 设备上的 camera 分辨率选择策略
>
> * iOS: 修复 iOS 11 视频播放
>
> * iOS: framework 将不会再包含签名
>
> * iOS: 修复在某些设备上的某些分辨率下 camera 显示问题
>
> * iOS: 修复录屏内存泄漏
>
> * Sample: 重命名 Unity 样例代码的文件名和 namespace，划分样例代码和 SDK 的明确边界
>
> * Sample: 删除 HelloARCloud 样例中的本地目标
>
> * Sample: 改善 Android/iOS HelloARQRCode 样例中 QR Code 检测到之后的信息显示
>
> * Sample: 在 iOS Unity 上默认打开 IL2CPP
>
> * 其它修正和完善
>

---

## EasyAR Sense 2.2 发行说明
- 章节路径: `native/release-notes/release-notes-2_2.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_2.html

# EasyAR Sense 2.2 发行说明
## 2.2.1
2018-10-24
EasyAR SDK 2.2.1 修复了在 Android 8、iPhone XS/XS Max 以及 Unity 2018 上的一些兼容性问题。
详细更新内容如下：
>
> + 提升 EasyAR CRS 连接的安全性
>
> * 修复了在 Android 8 及新版本上 ARSceneTracker 停止时崩溃
>
> * 修复了在 Unity 2018 上使用 Android/iOS/Mac 发布黑屏
>
> * 修复了在 iPhone XS/XS Max 上的崩溃
>
## 2.2.0
2018-03-06
EasyAR SDK 2.2.0 对图像跟踪做了大幅改进。这个版本中 ImageTracker 变得更加稳定，跟踪不易丢失，同时姿态的抖动也有所减弱。算法默认将以最高质量模式运行，可以通过选择 ImageTracker 的不同模式来平衡跟踪运行效率和质量。
详细更新内容如下：
>
> + 优化图像跟踪算法
>
> + 添加 ImageTracker 模式选择的接口
>
> * 修复在 Java 接口中使用非 ASCII 字符造成的崩溃
>
> * 修复某些类型 PNG 图像在某些硬件下的加载和跟踪问题
>
> * 修复在使用多个 camera 实例的时候，某些情况下 camera 打开失败
>
> * 修复在经打开的 camera 在未关闭的情况下再次调用打开接口时崩溃
>
> * 修复录屏缩放模式无效
>
> * 修复在某些情况下录屏关闭时崩溃
>

---

## EasyAR Sense 2.3 发行说明
- 章节路径: `native/release-notes/release-notes-2_3.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-2_3.html

# EasyAR Sense 2.3 发行说明
## 2.3.0
2018-10-24
EasyAR SDK 2.3.0 对图像跟踪的抖动问题做了大幅改进。这个版本同时包含对 Android 8、iPhone XS/XS Max 以及 Unity 2018 的一些兼容性修复。
详细更新内容如下：
>
> + 优化图像跟踪算法
>
> + 提升 EasyAR CRS 连接的安全性
>
> * 修复了在 Android 8 及新版本上 ARSceneTracker 停止时崩溃
>
> * 修复了在 Unity 2018 上使用 Android/iOS/Mac 发布黑屏
>
> * 修复了在 iPhone XS/XS Max 上的崩溃
>

---

## EasyAR Sense 3.0 发行说明
- 章节路径: `native/release-notes/release-notes-3_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-3_0.html

# EasyAR Sense 3.0 发行说明
## 3.0.1
2019-07-26
EasyAR SDK 3.0.1 修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> * 增加 Windows 上对摄像头的 YUY2 和 I420 像素格式的支持，减少出现黑屏的情况
>
> * 修正 Objective-C 示例中的 Renderer 的多个实例状态不独立，导致第二次进入时会在 glDrawArrays 处崩溃的问题
>
> * 增加对每通道 16 位的 png 图片的支持
>
> * 修正 Unity HelloAR_Coloring3D 示例在非 OpenGLES 和屏幕旋转等情况下贴图坐标出错的问题
>
> * 修正 Unity 示例默认不自动调焦的问题
>
> * 修正 Unity 示例中运行的一瞬间模型仍然显示，之后才消失的问题
>
> * 去除 Unity 示例初始化成功界面提示
>
> * 在 Unity 示例中增加对第二摄像头的支持(例如：在 Windows/Mac 上内置摄像头之外的 USB 摄像头)
>
> * 将 ExternalCamera 改名为 CustomCamera 以减少歧义
>
## 3.0.0
2019-07-07
EasyAR SDK 3.0 是 EasyAR SDK 2.x 的升级版。EasyAR SDK 3.0 有许多改进，主要集中在这几方面：
1. 更灵活的基于数据流的组件化 API
EasyAR 的 API 在 3.0 版本中，对原有 API 按照数据流进行了组件化的组织，使得 EasyAR 可以更容易与其他系统进行对接，以满足更为灵活的需求。
在此基础上，实现了外部摄像头接入和外部算法接入。
扩展 Camera 接口支持接收图片帧用于 AR 识别和跟踪。AR 展示将不依赖于手机自带摄像头，只要设备能够检测到外部摄像头并获取到视频流，就可以通过将视频流转成图片帧的方式传入 EasyAR SDK 用于 AR 应用，从而帮助 EasyAR 开发者为 AR/VR/MR 眼镜、无人机以及 USB 设备开发应用。
新的 API 支持开发者接入 EasyAR SDK 自有算法（ImageTracker 等）以外的其他算法，提供更灵活的能力扩展。
2. 编程语言和平台支持
增加了 C# for .Net/Mono 支持。
将 C++11 接口升级到 C++17，采用 std::optional 来明确参数和返回值的可空性。
将 Kotlin 和 Swift 接口升级到最新版本，并改善对 Optional 的支持。
增加了 Android ARM64 支持。
非 OpenGLES2 的渲染 API 支持(除 VideoPlayer 和 Recorder 以外实现渲染 API 中立)。
3. 表面跟踪
针对小型 AR 交互游戏、AR 短视频拍摄以及产品放置展示等应用场景，EasyAR SDK 3.0 增加 Surface Tracking 功能，使用检测任意表面特征点计算跟踪，不需要消耗时间寻找平面，实现更快速的表面贴合及姿态跟踪。
4. Image Target Data 生成
支持在原生及 Unity 应用中将待识别的图片提前生成一个数据包，用于识别跟踪，提高识别图加载速度。
5. 降低包体大小
通过架构的结构性改进和功能裁剪，减小了 SDK 的包体大小。
当前版本中去除了二维码扫描等冗余功能，以换取更小的包体。
6. 许多改进、bug 修复和兼容性提升
详细更新内容如下：
>
> ++ 更灵活的基于数据流的组件化 API
>
> ++ 表面跟踪
>
> + Image Target Data 生成
>
> + 编程语言支持：C# for .Net/Mono 支持
>
> + 编程语言支持：C++11 升级到 C++17
>
> + 编程语言支持：Kotlin/Swift 升级并支持 Optional
>
> + Unity 插件重写并开源，底层 API 与非 Unity 统一
>
> + Unity 插件涂涂乐示例新增截取静态图像绘制小熊的功能
>
> + Unity 插件新增 key 填错等 UI 提示
>
> + Android ARM64 支持
>
> + 非 OpenGLES2 的渲染 API 支持(除 VideoPlayer 和 Recorder 以外实现渲染 API 中立)
>
> + 外部摄像头接入
>
> + 外部算法接入
>
> + 降低包体大小
>
> - 二维码识别功能移除
>
> - 渲染器移除，改为提供各平台示例渲染代码
>
> * 支持从内存加载识别图
>
> * CloudRecognizer 支持 https(Android 和 iOS 上)
>
> * Android CameraDevice 增加对 Camera2 的支持
>
> * 修正 Android 9.0 上录屏崩溃的问题
>
> * 支持 Unity 5.6, 2017.4, 2018.4, 2019.1，去除对 5.6 以下版本的支持
>
> * 去除对 iOS 7 及以下版本的支持
>
> * Unity 插件使用 CommandBuffer 绘制相机背景
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 3.1 发行说明
- 章节路径: `native/release-notes/release-notes-3_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-3_1.html

# EasyAR Sense 3.1 发行说明
## 3.1.0
2020-01-14
EasyAR Sense 3.1.0 从 4.0.0 中反向移植了许多设计优化和问题修复。
EasyAR Sense Unity 插件也更新到新版本，有了巨大提升。
详细更新内容如下：
EasyAR Sense
>
> + CameraDevice 增加了获得 camera 数量、索引，获得 camera 前后位置的功能（Mac 不支持）和以指定前后位置打开 camera 的功能
>
> + 增加了各组件汇报占用的 camera buffer 需求的功能，用于 CameraDevice.setBufferCapacity
>
> * 编程语言支持：Swift 升级到 Swift 5
>
> * 不再区分 Basic 和 Pro 二进制包
>
> * CloundRecognitionService 从使用 AppKey 改为使用 ApiKey
>
> * 修正 iOS 上只能使用有限种类分辨率的问题，使得 iPad 上能够使用最大视野
>
> * 修正部分 iPad 设备上 camera 分辨率较高时会崩溃的问题
>
> * 修正 Google Play Store Android App Bundle 支持
>
> * 修正 ImageTracker.unloadTarget 和 ObjectTracker.unloadTarget 无法卸载 target 的问题
>
> * 修复了一些稳定性问题
>
Unity Plugin for EasyAR Sense 3.1.0
>
> ++ 恢复类似 Sense 2.3 的接口设计和行为，并有非常多改进
>
> + 添加严重出错情况的弹出消息（可在 EasyARController 上关闭）
>
> + Components: 大多数组件可以使用 Unity 组件的 enabled 来控制 start/stop
>
> + Component ARSenssion: AR 入口，控制 center mode，具备支持外部设备的能力，比如自定义相机及 AR 眼镜
>
> + Component ARAssembly: 展示 EasyAR Sense 组件化 API 的组装过程，支持所有 EasyAR Sense 的组件
>
> + Component ImageTargetController: 改善对不同类型输入的支持，可以从本地文件系统或 web URL 加载图像和.etd 文件
>
> + Component CameraImageRenderer: camera 图像渲染可由 disable 该组件来关闭
>
> + Scene: 添加 target gizmo，可在 Unity 编辑器中显示 target 细节
>
> + Asset: 添加全局服务配置及 gizmo 控制选项
>
> + Window: 添加生成 image target data（.etd 文件）的窗口
>
> + Window: 添加菜单跳转到 license key 设置界面和其他全局配置
>
> * 修复目标跟踪存在一帧延迟的问题
>
> * 修复阻塞式 target 加载，减少 target 加载时间
>
> * 修复 target size 获取
>
> * 许多其他改进及 bug 修复
>
Samples of Unity Plugin for EasyAR Sense 3.1.0
>
> ++ 添加回所有 Sense 2.3 的 sample
>
> + 添加 sample 启动器，可以通过启动器加载所有 samples
>
> + 添加屏幕上显示的组件状态信息，覆盖所有 sample
>
> + 添加展示 AR 眼镜支持的 sample
>
> + 添加表面跟踪与图像跟踪同时使用的 sample
>
> + 添加获取 camera 图像贴图和控制 camera 显示的 sample
>
> + 添加修改视频 aspect ratio （Unity VideoPlayer 功能） 适配 image target 的 sample
>
> + 添加展示从图像扩展跟踪的 sample
>
> + 云识别 sample 现在使用本地缓存，并在跟踪状态下停止云端识别，以覆盖常见的使用场景
>
> + 优化 coloring3D sample，修复 bug
>

---

## EasyAR Sense 4.0 发行说明
- 章节路径: `native/release-notes/release-notes-4_0.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_0.html

# EasyAR Sense 4.0 发行说明
## 4.0.1
2020-05-13
EasyAR Sense 4.0.1 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + CloudRecognizer 状态回调增加“到达访问额度”状态
>
> + 增加输入帧录制和播放功能，用于调试
>
> + 增加 MotionTracking 适配机型
>
> * 修正 MotionTracking 中的内存泄露问题
>
> * MotionTracking 的相机对焦模式改为自动对焦
>
> * 修正 SparseSpatialMapManager.load 出错时会崩溃的问题
>
> * 修正 Android HelloARMotionTracking 示例摄像机图像不更新的问题
>
> * 修复了一些稳定性问题
>
## 4.0.0
2019-12-30
EasyAR 已经成长为一个大家族，从版本 4 开始，过去被大家熟知的 EasyAR SDK 将被赋予一个新的名字：EasyAR Sense。EasyAR Sense 提供感知真实世界的能力。这个版本包含了所有 3.0 的功能。
EasyAR Sense 是一个独立 SDK，它不依赖于非系统组件或是像 Unity3D 这样的工具，可以提供灵活的基于数据流的组件化 API。
而关于 Unity 的支持，EasyAR Sense Unity Plugin 是一个非常薄的封装，用于在 Unity 中暴露 EasyAR Sense 的功能。EasyAR Sense Unity Plugin 的所有代码经过良好的接口设计且都是开源的。你可以直接使用这个插件来快速创建 AR 体验，也可以参考插件代码来更加灵活和自定义的使用 EasyAR Sense 接口和功能，或是创建属于自己的 Unity 插件。
EasyAR Sense 4.0 带来了这些全新特性：
1. 稀疏空间地图 Sparse Spatial Map
稀疏空间地图提供了扫描物理空间同时生成点云地图并进行实时定位的能力，开发者可以快速基于现实空间创建应用，如 AR 说明书以及 AR 导航导览等。在点云地图上部署的虚拟内容，同时也会被持久化放置在现实空间中，实现虚拟世界和物理世界的连接。此外，多人 AR 互动也能在此基础上实现。
2. 稠密空间地图 Dense Spatial Map
虚拟内容与物理世界产生交互碰撞，AR 体验才更加逼真。EasyAR Sense 4.0 支持实时重建环境的稠密空间地图，可以实现碰撞、遮挡等效果，从而构建更真实的 AR 体验。
3. 运动跟踪 Motion Tracking
提供多传感融合的方式解算位置和姿态，降低了相机运动带来的漂移，让虚拟物体在空间更加稳定。同时提供重定位功能，在跟踪丢失后可以恢复定位。使用运动跟踪的应用，不依赖于 ARCore，也不需要最终用户通过 Google 服务框架安装 ARCore 服务。
4. ARKit/ARCore 支持
支持在 iOS 上使用 ARKit，在 Android 上使用 ARCore，并可以与 EasyAR Sense 的其他功能一起使用。
EasyAR Sense Unity 插件同样获得了巨大提升，主要集中在这几方面：
1. 连贯的设计演化
EasyAR Sense 1/2/3 的 Unity 插件的所有功能和优点都在这个版本中保留了下来。
这个版本的插件尽可能多的使用了 Unity 本身的功能，比如使用 OnEnable/OnDisable 来控制 start/stop。大多数 EasyAR Sense 功能都可以不需要写脚本直接工作。
所有 EasyAR Sense 4.0 的新功能都已经支持，许多 bug 也已经修复。
2. 编辑器体验优化
编辑器中可以显示 image target 的 gizmo，以更好的体验替代过去版本中编辑模式下自动生成的 mesh。
严重错误（比如 license key 验证失败）会通过弹出消息在屏幕上显示，用于帮助 debug。
除 API 外，提供了 Unity 工具窗口来生成 image target data。
3. 更多样例，覆盖更多细节 API
添加了展示所有新功能以及不同算法组合工作的样例。
添加了 AR 眼镜支持的样例，预先标定了两款 AR 眼镜：影创 Action One 及 EPSON BT-350。
社区中许多关于“如何使用”的问题在这些样例中都有解答。感谢大家的反馈！
EasyAR Sense 4.0 提供免费个人版、月付费专业版和定制化功能企业版三种订阅模式。
功能、定价、付款方式等的详细信息可以在 [产品页面](https://www.easyar.cn/view/sdk.html) 及 [价格页面](https://www.easyar.cn/price.html) 了解。

---

## EasyAR Sense 4.1 发行说明
- 章节路径: `native/release-notes/release-notes-4_1.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_1.html

# EasyAR Sense 4.1 发行说明
## 4.1.0
2020-07-16
EasyAR Sense 4.1.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + MotionTrackerCameraDevice 支持点击碰撞和获取局部点云功能
>
> + CloudRecognizer 支持单次扫描
>
> + API 文档支持交叉引用链接
>
> - 拆分 Unity Plugin 文档
>
> - 去除 ImageTarget.setupAll 和 ObjectTarget.setupAll，并增加了 Android 和 iOS 上使用 JSON 加载 ImageTarget 的示例代码
>
> * 修正 Android 上 CameraDevice(Camera1).setSize 中与 buffer 数量相关的多线程 race condition(造成摄像机画面显示不正常)
>
> * 修正 Android 上 CameraDevice(Camera2).supportedSize 返回数值错误的问题
>
> * 修正 Android 上 CameraDevice.supportedFrameRateRangeLower 和 CameraDevice.supportedFrameRateRangeUpper 崩溃的问题
>
> * 修正 SparseSpatialMap 上传和下载超过 1MB 地图时数据损坏的问题
>
> * CameraDevice.setSize 不再修改 CameraParameters，只在 InputFrame 生成时进行根据图像大小重新计算 CameraParameters
>
> * 修正 Swift binding 在 XCode 11.4 和之后版本上运行崩溃的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.2 发行说明
- 章节路径: `native/release-notes/release-notes-4_2.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_2.html

# EasyAR Sense 4.2 发行说明
## 4.2.0
2021-01-25
EasyAR Sense 4.2.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
>
> + 增加 iOS 不带录屏和视频播放器功能版本，以满足部分应用的 AppStore 隐私政策合规要求
>
> + 增加 MacOS 上的 framework 版本
>
> + FrameRecorder 播放时增加暂停/继续和获取总播放时间、当前播放时间、初始屏幕旋转方向、是否已完成的功能
>
> + 将 Android 的 CameraDevice 实现提取到了 HelloARCustomCamera 示例中，便于进行修改
>
> + 在 Android 的 aar 库中增加了 ProGuard 规则，不再需要手动指定
>
> + 在 MotionTracking 中优化了平面检测，提升了跟踪鲁棒性和重定位能力
>
> + 增加 MotionTracker 标定参数网络更新功能(CalibrationDownloader)
>
> + 增加 MotionTracking 适配机型
>
> + 增加 CameraDeviceSelector.getFocusMode 以在使用 SurfaceTracking 或 MotionTracking 时获得推荐的对焦模式
>
> + 增加 Storage.setAssetDirPath 以设置加载 image target 等文件时的根目录
>
> + 增加 Log.setLogFuncWithScheduler 以在无法或不便保证线程安全时使用自定义日志函数
>
> * Android 平台示例均升级到 Android 11 (API Level 30)目标
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.3 发行说明
- 章节路径: `native/release-notes/release-notes-4_3.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_3.html

# EasyAR Sense 4.3 发行说明
## 4.3.0
2021-04-07
EasyAR Sense 4.3.0 增加了一些小功能，修复了一些兼容性问题。
详细更新内容如下：
>
> + 增加 MotionTrackerCameraDevice.getQualityLevel，用于获取设备的 MotionTracking 适配质量
>
> + 增加 MotionTrackerCameraDevice.setTrackingMode，用于支持不同的跟踪模式
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ARCoreCameraDevice 在 Android 11 上的兼容性说明
>
> * 在 MotionTracking 中优化了 hittest
>
> * 在 MotionTracking 中提升了大场景下鲁棒性
>
> * 在 DenseSpatialMap 中减小了 block size，提升 incremental update 的性能
>
> * 升级 XCode 版本到 12，iOS 最低版本到 9.0
>
> * 升级 Android Gradle Plugin 版本到 4.1.0，NDK 到 r22
>
> * 修复 Android 平台上 HelloARRecording 示例对 Android 10 和 Android 11 的兼容性问题
>
> * 修复 Android 平台上 CameraDevice 使用 camera2 时有时候退出时会崩溃的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.4 发行说明
- 章节路径: `native/release-notes/release-notes-4_4.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_4.html

# EasyAR Sense 4.4 发行说明
## 4.4.0
2021-10-28
EasyAR Sense 4.4.0 增加了对 EasyAR Cloud SpatialMap 的支持，另外还增加了一些小功能，修复了一些问题。
[EasyAR Cloud SpatialMap](https://www.easyar.cn/cloudspatialmap.html) 提供城市级 AR 云方案，通过灵活的采集方案、稳定的建图定位能力及完善的工具链，为文旅、商圈、教育、工业等众多行业进行 AR 数字化赋能。
详细更新内容如下：
>
> ++ 增加 CloudLocalizer，用于支持 EasyAR Cloud SpatialMap
>
> + 增加 RealTimeCoordinateTransform，用于 EasyAR 运动融合
>
> + iOS 和 MacOS 中的 framework 改为以 xcframework 的形式组织
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ARKit/ARCore 对焦控制接口 ARCoreCameraDevice.setFocusMode、ARKitCameraDevice.setFocusMode
>
> + 增加加速度计接口 Accelerometer
>
> - 去除 iOS 上的 static framework，请改为使用 dynamic framework
>
> - 去除 MacOS 上的 bundle，请改为使用 framework 或者 dylib
>
> - C++03 接口已过时，会在将来删除，请改为使用 C++17 或者 C 接口，示例已删除
>
> * 将 Android 示例中的 jcenter 改为 mavenCentral，以应对 jcenter 关闭
>
> * 修复 MotionTracking 在反复进出时可能崩溃的问题
>
> * 修复 MotionTracking 在部分设备上卡死的问题
>
> * 优化 iOS 示例发布包大小
>
> * 修复 ImageTracking 有时候识别到后马上丢失的问题
>
> * 修复 ImageTracking 在 Android 上部分识别图加载失败无法用于跟踪的问题
>
> * 修复 ImageTarget.save 在 MacOS 上 Unicode 字符路径无法使用问题
>
> * 修复 CameraDevice 设置的回调在调用 open 之后会失效的问题
>
> * 修复 CameraDevice 在 Android 上调用 start 之后设置的回调无法被触发的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.5 发行说明
- 章节路径: `native/release-notes/release-notes-4_5.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_5.html

# EasyAR Sense 4.5 发行说明
## 4.5.0
2022-03-04
EasyAR Sense 4.5.0 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 网络相关功能增加超时时间参数(CalibrationDownloader.download、CloudLocalizer.resolve、CloudRecognizer.resolve、SparseSpatialMapManager.host、SparseSpatialMapManager.load)
>
> + Image 增加 pixelWidth 和 pixelHeight 用于支持摄像机图像的 padding
>
> + 增加 MotionTracking 适配机型
>
> - 结束 Android 4.x 支持，最低支持版本为 5.0
>
> - 移除 C++03 接口
>
> - 停止获取 Android Build Serial 以满足 PlayStore Families Policy Requirements
>
> * Recorder、VideoPlayer 和各示例的 OpenGLES 2.0 升级为 3.0
>
> * 升级编译 SDK 的工具版本：XCode 13
>
> * 升级编译 SDK 的工具版本：Android Gradle Plugin 7.0.0，NDK r23
>
> * 升级各示例依赖的工具版本
>
> * 修正 ARCoreCameraDevice 在部分机型上出现的花屏等问题
>
> * 修正 CameraDevice 在 iPhone 上前置摄像头使用 setFocusMode 时崩溃的问题
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.6 发行说明
- 章节路径: `native/release-notes/release-notes-4_6.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_6.html

# EasyAR Sense 4.6 发行说明
## 4.6.1
2023-03-24
EasyAR Sense 4.6.1 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 增加 MotionTracking 适配机型
>
> * 修正 MotionTrackerCameraDevice 的 hitTestAgainstPointCloud、hitTestAgainstHorizontalPlane、getLocalPointsCloud 无返回结果的问题
>
## 4.6.0
2023-02-13
EasyAR Sense 4.6.0 增加了一些小功能，修复了一些问题。
详细更新内容如下：
>
> + 增加 MegaTracker，集成 CloudLocalizer 和 RealTimeCoordinateTransform，下个版本将删除 RealTimeCoordinateTransform
>
> + 增加 CloudLocalizer.resolve 参数以支持辅助邻近位置和指南针读数输入
>
> + 增加 Accelerometer.output 以配合 MegaTracker 输入
>
> + 增加 MotionTrackerCameraDeviceTrackingMode.LargeScale 模式降低大空间跑飞概率
>
> + 增加 MotionTracking 跟踪稳定性
>
> + 增加 MotionTracking 适配机型
>
> + 增加 ImageTracker.setResultPostProcessing、ObjectTracker.setResultPostProcessing、SparseSpatialMap.setResultPoseType 以集成 RealTimeCoordinateTransform 功能
>
> + 增加 ARCore 机型列表以判断设备是否支持 ARCore，HelloARMotionTracking 示例增加 ARCore 下载引导
>
> + 增加 MacOS arm64 的支持
>
> - 移除 iOS armv7 空库
>
> - 结束 iOS 9.x-10.x 支持，最低支持版本为 11.0
>
> - 停止获取 Android SSAID(ANDROID_ID)以满足中国大陆监管要求。请受到影响的用户尽快升级。同时，从 EasyAR Sense 4.6.0 开始，将无法连接按日活计费的 CRS 服务，请迁移到按调用次数计费模式
>
> * 优化 CloudLocalizer 接口，修正对相机旋转方向的处理
>
> * 修改 CloudLocalizerStatus 错误值定义
>
> * 简化 TargetInstance 和 TargetStatus
>
> * 修正 Java binding 中回调的参数没有自动释放的问题
>
> * 升级编译 SDK 的工具版本：Android Gradle Plugin 7.2.0，NDK r25
>
> * 升级编译 SDK 的工具版本：XCode 14
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 4.7 发行说明
- 章节路径: `native/release-notes/release-notes-4_7.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes-4_7.html

# EasyAR Sense 4.7 发行说明
## 4.7.0
2025-10-20
EasyAR Sense 4.7.0 增加了一些功能，修复了一些问题。
版本
>
> + 增加 CommunityR 版本，支持视频播放、录屏功能，取消 NR 版本，其他版本不再支持视频播放、录屏功能
>
> + 增加 visionOS 支持
>
> + 增加 aar 的 C++ prefab 支持
>
> * 升级编译 SDK 的工具版本：Android build tools 36，NDK r28，兼容 Android 16KiB 内存页大小
>
> * 升级编译 SDK 的工具版本：XCode 16.1
>
> - 结束 iOS 11.x-14.x 支持，最低支持版本为 15.0
>
> - 结束 macOS 10.x 支持，最低支持版本为 11.0
>
MEGA
>
> + 增加 MegaLandmarkFilter 用于支持 EasyAR Mega Landmark 的 VPS 云定位
>
> + MegaTracker 支持新协议版本
>
> + MegaTracker 运行时支持切换定位库
>
> + 服务器唤醒中定义单独枚举项
>
> + MegaTracker 增加同步获得输出 pose 的功能
>
> + MegaTracker 增加 setResultAsyncMode 接口，适应 RTCT 的修改
>
> + 支持使用 API Token 访问 Mega 服务
>
算法
>
> + 支持使用 API Token 访问 CRS 服务
>
> + InputFrame 增加了一些不兼容的检查
>
> + InputFrame 增加 CameraTransformType 字段
>
> + CameraParameters 增加鱼眼等相机模型
>
> + ImageTracker ObjectTracker SparseSpatialMap 增加同步访问结果模式
>
> * 将 RealTimeCoordinateTransform 集成在各个 Tracker 中，改进其稳定性
>
> * 修正 MotionTrackerCameraDevice 在某些情况下会崩溃的问题
>
设备
>
> + 增加 ThreeDofCameraDevice 用于支持 3DoF 的相机
>
> + 增加 InertialCameraDevice 用于支持惯性导航
>
> + 增加 VisionOSARKitCameraDevice 用于支持 visionOS 上的 ARKit 相机
>
> + 增加 Gyroscope Magnetometer AttitudeSensor 用于获取传感器数据
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获取帧率的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice 获取摄像机图像大小的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获得摄像机类型和旋转方向 的功能
>
> + 增加 CameraDevice 获得旋转方向的功能
>
> + 增加 MotionTrackerCameraDevice 获得摄像机类型、旋转方向、大小、帧率的功能
>
> + 增加对一些 AR 眼镜的支持(请参考 EasyAR Sense Unity Plugin 文档)
>
> + ARKitCameraDevice 增加帧率设置
>
> + 各种 CameraDevice 删除获得 InputFrameSourceType 功能
>
> + 升级 ARCore 机型列表
>
> + 升级 MotionTrackerCameraDevice 机型列表
>
> + Android 上 camera2 获取系统内参
>
> + iOS 支持 CameraDevice 获取内参(可能部分老手机不支持)
>
杂项
>
> + 增加 VideoInputFrameRecorder 和 VideoInputFramePlayer 用于 EIF MKV 格式调试数据录制和播放(Windows 上只支持播放，Android 上只支持录制)
>
> + 增加 EventDumpRecorder 用于 EED 格式调试数据录制，EED(EasyARSense Event Dump)文件可用于记录日志、输出帧状态、定位请求、IMU、GPS 等数据
>
> + Log 增加 logMessage
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NORTTI
> 选项用于禁用 RTTI
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常
>
> + 在 C++导出接口实现中增加
> EASYAR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常 throw
>
> * 修复了一些稳定性问题
>

---

## EasyAR Sense 发行说明
- 章节路径: `native/release-notes/release-notes.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/native/release-notes/release-notes.html

# EasyAR Sense 发行说明
EasyAR 是灵活好用的增强现实引擎。
EasyAR Sense 提供感知真实世界的能力，支持平面图像跟踪、3D 物体跟踪、表面跟踪、运动跟踪和稀疏空间地图、稠密空间地图、Mega。
EasyAR Sense 是一个独立 SDK，它不依赖于非系统组件或是像 Unity3D 这样的工具，可以提供灵活的基于数据流的组件化 API。
EasyAR Sense 4.0 提供免费个人版、月付费专业版、一次性付费经典版和定制化功能企业版四种订阅模式。
## 历史版本
[4.7](release-notes-4_7.html)
[4.6](release-notes-4_6.html)
[4.5](release-notes-4_5.html)
[4.4](release-notes-4_4.html)
[4.3](release-notes-4_3.html)
[4.2](release-notes-4_2.html)
[4.1](release-notes-4_1.html)
[4.0](release-notes-4_0.html)
[3.1](release-notes-3_1.html)
[3.0](release-notes-3_0.html)
[2.3](release-notes-2_3.html)
[2.2](release-notes-2_2.html)
[2.1](release-notes-2_1.html)
[2.0](release-notes-2_0.html)
[1.3](release-notes-1_3.html)
[1.2](release-notes-1_2.html)
[1.1](release-notes-1_1.html)
[1.0](release-notes-1_0.html)
## 4.7.0
2025-10-20
版本
>
> + 增加 CommunityR 版本，支持视频播放、录屏功能，取消 NR 版本，其他版本不再支持视频播放、录屏功能
>
> + 增加 visionOS 支持
>
> + 增加 aar 的 C++ prefab 支持
>
> * 升级编译 SDK 的工具版本：Android build tools 36，NDK r28，兼容 Android 16KiB 内存页大小
>
> * 升级编译 SDK 的工具版本：XCode 16.1
>
> - 结束 iOS 11.x-14.x 支持，最低支持版本为 15.0
>
> - 结束 macOS 10.x 支持，最低支持版本为 11.0
>
MEGA
>
> + 增加 MegaLandmarkFilter 用于支持 EasyAR Mega Landmark 的 VPS 云定位
>
> + MegaTracker 支持新协议版本
>
> + MegaTracker 运行时支持切换定位库
>
> + 服务器唤醒中定义单独枚举项
>
> + MegaTracker 增加同步获得输出 pose 的功能
>
> + MegaTracker 增加 setResultAsyncMode 接口，适应 RTCT 的修改
>
> + 支持使用 API Token 访问 Mega 服务
>
算法
>
> + 支持使用 API Token 访问 CRS 服务
>
> + InputFrame 增加了一些不兼容的检查
>
> + InputFrame 增加 CameraTransformType 字段
>
> + CameraParameters 增加鱼眼等相机模型
>
> + ImageTracker ObjectTracker SparseSpatialMap 增加同步访问结果模式
>
> * 将 RealTimeCoordinateTransform 集成在各个 Tracker 中，改进其稳定性
>
> * 修正 MotionTrackerCameraDevice 在某些情况下会崩溃的问题
>
设备
>
> + 增加 ThreeDofCameraDevice 用于支持 3DoF 的相机
>
> + 增加 InertialCameraDevice 用于支持惯性导航
>
> + 增加 VisionOSARKitCameraDevice 用于支持 visionOS 上的 ARKit 相机
>
> + 增加 Gyroscope Magnetometer AttitudeSensor 用于获取传感器数据
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获取帧率的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice 获取摄像机图像大小的功能
>
> + 增加 ARCoreCameraDevice ARKitCameraDevice ThreeDofCameraDevice 获得摄像机类型和旋转方向 的功能
>
> + 增加 CameraDevice 获得旋转方向的功能
>
> + 增加 MotionTrackerCameraDevice 获得摄像机类型、旋转方向、大小、帧率的功能
>
> + 增加对一些 AR 眼镜的支持(请参考 EasyAR Sense Unity Plugin 文档)
>
> + ARKitCameraDevice 增加帧率设置
>
> + 各种 CameraDevice 删除获得 InputFrameSourceType 功能
>
> + 升级 ARCore 机型列表
>
> + 升级 MotionTrackerCameraDevice 机型列表
>
> + Android 上 camera2 获取系统内参
>
> + iOS 支持 CameraDevice 获取内参(可能部分老手机不支持)
>
杂项
>
> + 增加 VideoInputFrameRecorder 和 VideoInputFramePlayer 用于 EIF MKV 格式调试数据录制和播放(Windows 上只支持播放，Android 上只支持录制)
>
> + 增加 EventDumpRecorder 用于 EED 格式调试数据录制，EED(EasyARSense Event Dump)文件可用于记录日志、输出帧状态、定位请求、IMU、GPS 等数据
>
> + Log 增加 logMessage
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NORTTI
> 选项用于禁用 RTTI
>
> + 在 C++导出接口回调中增加
> EASYAR_FUNCTOR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常
>
> + 在 C++导出接口实现中增加
> EASYAR_EXCEPTION_MODE_NOEXCEPTION
> 选项用于禁用异常 throw
>
> * 修复了一些稳定性问题
>

---

## 3D 物体跟踪简介
- 章节路径: `object-tracking/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/object-tracking/intro.html

# 3D 物体跟踪简介
除了平面物体外，EasyAR 同时也提供对 3D 物体的跟踪功能。本篇将介绍 3D 物体跟踪的核心原理、预期效果及潜在限制，帮助开发者理解该技术的适用场景。
## 基本原理
3D 物体跟踪通过识别和跟踪真实世界中的三维物体（如玩具、雕塑、工业零件）来实现 AR 内容叠加。其核心流程如下：
### 技术流程
1. **模型准备**：开发者提供待跟踪物体的 3D 模型文件（Wavefront OBJ 格式），系统在本地加载模型，并提取模型不同视角下的视觉特征，生成唯一特征库。
2. **实时匹配**：摄像头捕获现实场景后，系统逐帧分析画面中的视觉特征，与预存的模型特征库进行匹配。
3. **位姿计算**：通过匹配点计算物体在 3D 空间中的 6DoF 位姿，驱动虚拟内容与物体精准对齐。
4. **持续跟踪**：即使物体部分遮挡或移动，系统仍可通过剩余可见特征点维持跟踪。
### 核心机制
* **本地处理**：所有计算都在设备端完成，模型和内容由开发者管理，保障离线可用性。
* **纹理依赖**：物体表面需具备丰富的纹理或几何细节，纯色或光滑表面（如玻璃、金属）难以跟踪。
* **模型格式**：仅支持 OBJ 格式，需包含 MTL 材质文件和至少一张纹理贴图（JPEG/PNG），且文件路径必须为相对路径（禁止绝对路径或空格）。
### 技术限制
* **物体类型**：仅支持刚性物体（不变形），几何结构以凸为主（没有大量孔洞结构）。
* **尺寸范围**：物体尺寸建议在 10cm 至 2m 之间，过小或过大会影响自然体验距离下的物体可见性。
* **环境要求**：依赖光照条件，过暗或过曝会导致检测困难或跟踪丢失。
## 效果与预期结果
物体跟踪功能依赖物体本身的纹理进行视觉特征匹配，因此其所能达到的效果也会存在一些限制。明确这些效果有助于您在开发过程中设定合理的测试标准。
### 理想效果
* **精准绑定**：虚拟内容与 3D 物体边缘对齐。
* **实时响应**：从模型加载到检测成功的超低延迟。
* **抗遮挡**：物体被部分遮挡（如30%）时，仍可维持跟踪。
* **多角度支持**：物体旋转 360° 或从不同视角观察时，虚拟内容持续跟随。
### 不理想情况与应对
|现象|原因|用户感知|解决方案预览（详见后续章节）|
|**无法识别**|模型纹理不足、路径错误、文件编码非 UTF-8|虚拟内容不出现|优化模型纹理，检查文件格式与路径|
|**跟踪抖动**|光照变化剧烈、物体表面反光|虚拟物体晃动明显|控制光照，避免反光表面|
|**频繁丢失**|物体快速移动或完全遮挡|虚拟物体闪烁/消失|增大模型尺寸，或结合运动融合|
|**加载失败**|OBJ/MTL 文件格式错误、缺少纹理贴图|无法初始化跟踪器|验证模型规格，参考官方样例|
### 预期结果验证方法
* **开发阶段**：使用 `HelloARObjectTracking` 样例，导入官方测试模型（并制作实体）验证基础功能。
* **测试阶段**：在真实环境中测试不同光照、角度、遮挡条件下的跟踪稳定性。
## 总结与扩展
3D 物体跟踪通过本地处理模型的视觉特征实现，适合需要针对非平面物体的离线场景 AR 应用。开发者需确保模型符合格式规范，并关注环境与物体纹理质量。[下一章](model-requirements.html) 将详解模型准备与优化技巧。

---

## 3D 模型准备与优化
- 章节路径: `object-tracking/model-requirements.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/object-tracking/model-requirements.html

# 3D 模型准备与优化
本文将详细讲解如何准备符合 EasyAR 要求的 3D 模型，涵盖格式规范、工具推荐及常见问题排查，帮助开发者从源头提升跟踪成功率。
## 模型格式与规范
EasyAR 3D 物体跟踪仅支持 **Wavefront OBJ** 格式。使用时需遵循以下要求和规范。
### 模型文件结构
一个完整的 3D 模型**必须包含**以下文件：
* **.obj文件**：几何模型数据（包含顶点、面、UV 坐标等）。
* **.mtl文件**：材质定义（颜色、纹理贴图路径）。
* **纹理贴图**：至少一张 JPEG 或 PNG 格式的图片（建议分辨率512×512至2048×2048）。
### 文件要求
* 所有文件必须放在**同一文件夹**内，且使用**相对路径**引用（如 `texture.jpg`），禁止绝对路径（如 `C:\\Models\\texture.jpg`）。
* 文件名以及文件内部的路径**禁止包含空格**，建议使用英文或数字。
* 文件编码格式必须为 **UTF-8**（避免乱码导致加载失败）。
### OBJ（.obj）文件最低要求
* 必须包含 `vertex`
几何顶点，用 \\((x, y, z [, w])\\) 坐标表示。\\(w\\) 为可选项，默认为1.0。顶点的色彩参数不是必须的，如果提供了色彩参数系统并不会加载。
* 必须包含 `texture coordinates`
纹理坐标，用 \\((u, v [,w])\\) 坐标表示，\\(w\\) 为可选项，默认为0。通常情况下，\\(u\\) 和 \\(v\\) 的取值应该是在0至1之间。对于小于0或者大于1的情形，系统默认会以 `REPEAT` 模式进行处理，即坐标的整数部分被忽略，然后构建一个无限复制的模式（与 `OpenGL` 中的 `GL\_REPEAT` 处理方式相同）。
* 必须包含 `face`
面元素，应当至少包含顶点的索引，以及顶点的纹理坐标的索引。超过3个顶点的多边形（如四边形）面片结构同样支持。
* 必须包含 `mtllib`
材质文件的引用，要求至少指定一个外部 MTL 材质文件，文件路径必须是相对路径，不能是绝对路径。
* 必须包含 `usemtl`
模型元素所引用的材质需指定材质名字，这个材质名字应当与外部 MTL 材质文件中定义的材质名字保持一致。
### MTL（.mtl）文件最低要求
* 一个 MTL 文件中应当定义至少一个材质。
* 纹理贴图是必须的。
通常情况下，只需要指定环境光或者漫反射的纹理贴图（`map\_Ka`、`map\_Kd`）;
纹理贴图的路径必须是相对路径，不能是绝对路径；
* 纹理贴图的其他可选参数不是必须的，如果提供了系统并不会采用。
## 模型准备
您可以通过多种方式来准备符合规范的 OBJ 格式模型文件。
1. 从已有模型中导出
使用 **Autodesk Maya / 3ds Max** 等专业工具，导入现有 FBX 或其他格式的模型，导出时选择 “OBJ Export”，并确保 “Materials” 和 “UVs” 选项启用。
2. 创建全新的模型
使用 **Autodesk Maya / 3ds Max** 等建模工具创建/绘制 3D 模型并输出为 OBJ 格式。
3. 扫描真实物体并进行 3D 重建
使用 **Autodesk ReCap**、**Bentley ContextCapture** 等三维扫描建模软件，或者激光扫描仪对真实物体进行 3D 重建，并将重建结果导出为 OBJ 格式。
> **重要事项**
模型贴图必须准确还原真实物体的视觉特征，否则识别与跟踪功能将无法正常工作。
## 模型最佳实践
以下列出一些常见的在准备模型时会遇到的问题和例子，供您快速参考以便检查。
1. **确保丰富的纹理细节**
模型的贴图应当具有丰富的纹理细节。
![](https://doc-asset.easyar.com/develop/object-tracking/media/hexagon.png)
![](https://doc-asset.easyar.com/develop/object-tracking/media/biscuit.png)
>
> 参考图左：可以被 EasyAR 检测和跟踪。参考图右： 无法检测和跟踪，纹理太少。
>
2. **模型的形状**
模型支持不同的形状，但主体结构是凸的。
![](https://doc-asset.easyar.com/develop/object-tracking/media/hexagon.png)
![](https://doc-asset.easyar.com/develop/object-tracking/media/deer.png)
>
> 这两个物体都可以被 EasyAR 检测和跟踪。
>
3. **检查文件内引用路径**
模型文件内引用的路径必须是相对路径，不能是绝对路径。
![](https://doc-asset.easyar.com/develop/object-tracking/media/file-good-path.png)
![](https://doc-asset.easyar.com/develop/object-tracking/media/file-wrong-path.png)
>
> 右侧的模型无法被加载，因为 EasyAR 找不到使用了绝对路径的文件。
>
模型文件内引用的路径不能有空格或特殊字符。
![](https://doc-asset.easyar.com/develop/object-tracking/media/file-good-path.png)
![](https://doc-asset.easyar.com/develop/object-tracking/media/file-with-blank.png)
>
> 右侧的模型无法被加载，因为引用的路径中包含了空格。
>
1. **检查文件的编码格式**
模型文件应该使用 UTF-8 编码格式。
![](https://doc-asset.easyar.com/develop/object-tracking/media/file-utf8.png)
![](https://doc-asset.easyar.com/develop/object-tracking/media/file-wrong-encoding.png)
>
> 右侧的模型无法被加载，因为其文件编码的问题导致读取时解码错误。
>
2. **检查模型法向**
模型面片的法向量的正向应遵循右手准则。
![](https://doc-asset.easyar.com/develop/object-tracking/media/cube.png)
![](https://doc-asset.easyar.com/develop/object-tracking/media/cube-wrong-normal-outside.png)
![](https://doc-asset.easyar.com/develop/object-tracking/media/cube-wrong-normal-inside.png)
>
> 第二个立方体中阴影部分的面片的法向量是负值取向。这种面片在 EasyAR 中会当成不可见面处理。如果从模型内部看出去，会显示成第三个立方体的样子。
> 模型应当避免一切法向量负值取向的面片。
>
3. **模型面片数量**
模型面片的数量在保证物体几何形状的前提下应尽可能少，通常不应超过 100,000 个三角面片。过多的面片数量会导致：
* 模型加载时间过长，影响应用在启动的用户体验
* 面片纹理投影的计算量增加，影响应用在跟踪时的帧率
3D 模型的质量直接决定跟踪成功率。开发者需严格遵循格式规范，重点优化纹理细节，并确保文件格式无误。

---

## 物体跟踪与运动跟踪结合
- 章节路径: `object-tracking/motion-fusion.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/object-tracking/motion-fusion.html

# 物体跟踪与运动跟踪结合
本篇介绍如何将 3D 物体跟踪与设备运动跟踪功能相融合，以提升复杂场景下的跟踪稳定性和用户体验。内容包括核心原理、预期效果及潜在问题分析。
## 基本原理
**运动融合（Motion Fusion）** 结合 3D 物体跟踪的位姿数据和设备运动跟踪的位姿数据，实现更鲁棒的位姿估计。以下是其核心流程：
### 数据同步与互补
* **视觉跟踪**：通过图像特征点匹配计算当前帧的位姿（位置+旋转），但易受遮挡、模糊或快速移动影响。
* **运动跟踪**：利用 IMU 传感器高频输出以及视觉图像的输出获得设备运动数据，但存在累积飘移误差。
* **融合机制**：
* 将视觉跟踪的位姿与设备运动跟踪的位姿进行坐标系对齐。
* 当目标物体清晰可见、稳定运动时：以视觉跟踪为主。不断地将视觉跟踪位姿送入融合模块进行修正，以减少整个系统的累积漂移。
* 当目标物体丢失或者在画面中占比过小、快速运动时：此时视觉跟踪失效，以运动跟踪为主。根据当前的运动跟踪位姿进行融合位姿预测。
### 关键技术点
* **时间戳对齐**：将视觉帧的时间戳与运动跟踪数据对齐，避免因延迟导致抖动。
* **坐标系对齐**：根据视觉跟踪的轨迹和运动跟踪的轨迹进行坐标系对齐。
* **重定位**：目标物体重新出现时，视觉跟踪接管快速校正可能的累积误差，将虚拟物体“拉回”正确位置。
### 适用场景与限制
运动融合并不适合所有场景下的使用。有以下情形之一的将 **不适用** 运动融合功能：
* 目标设备不支持 ARCore/ARKit 等运动跟踪功能。详细的设备支持列表参考：[运动跟踪设备支持](../motion-tracking/devices.html)。
* 目标物体在场景中是动态的，例如拿在手上的玩具、手办。
除此之外的场景，使用运动融合将极大的提升 3D 物体跟踪的用户体验，包括但不限于以下使用情景：
* **快速运动**：用户手持设备快速移动，运动模糊会导致视觉跟踪失效。
* **目标消失**：画面离开目标本身或者目标被动态物体（如行人）遮挡时，依然保持整个场景里虚拟内容的呈现。
* **远离目标**：用户手持设备远离导致目标物体在画面中占比过小，依然稳定持续跟踪。
* **低光照条件**：视觉跟踪性能下降，需要维持体验。
## 效果与预期结果
在场景适用的前提下，使用运动融合将比单纯的使用 3D 物体跟踪带来更稳定、平滑的用户体验。
### 理想效果
* **更稳定的跟踪**：虚拟物体不抖动、不跳变。
* **平滑过渡**：视觉跟踪失效时，融合位姿的变化连续自然。
* **抗干扰能力**：目标物体丢失或被遮挡、设备快速运动等情形下，虚拟物体仍能跟随设备运动持续跟踪。
### 不理想情况与应对
|现象|原因|用户感知|解决方案|
|**初始未生效**|运动跟踪需要一定时间进行初始化|在初始阶段出现内容消失|一定的 UI 提示，确保系统运动跟踪初始化完成|
|**飘移明显**|系统误差累积，且长时间无视觉校正|虚拟物体偏离原位置|引导用户缩短遮挡时间，或增加视觉重定位的提示|
|**性能下降**|长时间同时运行两个功能|帧率下降画面卡顿|正常现象，可通过接口关闭运动融合|
### 预期结果验证方法
使用支持的设备在真实场景中测试：
1. 对准目标物体，确认虚拟物体稳定。
2. 用手遮挡物体2秒并移动设备，观察虚拟物体是否平滑移动。
3. 移开手，确认虚拟物体快速回正且无跳变。
## 总结与最佳实践
运动融合显著提升了 3D 物体跟踪在许多场景下的鲁棒性，但需要设备的硬件支持且性能足够。开发者应根据目标用户设备选择性启用该功能，并在低性能设备上提供降级方案。
实时打开/关闭运动融合功能的 API 参考：
* 原生： [setResultPostProcessing](../../api/native/easyar.ObjectTracker.html#n_easyar_ObjectTracker_setResultPostProcessing)
* Unity：[EnableMotionFusion](../../api/unity/easyar.ObjectTrackerFrameFilter.html#u_easyar_ObjectTrackerFrameFilter_EnableMotionFusion)

---

## EasyAR 开发简介
- 章节路径: `overview.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/overview.html

# EasyAR 开发简介
EasyAR 让 AR 开发变得简单高效。使用 EasyAR，您可以轻松地将增强现实功能集成到各种平台的应用中。
## EasyAR 产品概览
EasyAR 为 AR 开发提供了三大产品：`EasyAR Mega`、`EasyAR CRS`（Cloud Recognition Service）和 `EasyAR Sense`。
* `EasyAR Mega` 是大场景空间识别定位服务，提供大规模场景和复杂物体的 AR 能力。
* `EasyAR CRS` 是高性能云端图像识别服务，提供传统图像识别 AR 能力。
* `EasyAR Sense` 是增强现实 SDK，提供跨平台的 AR 集成能力。
下图从产品结构上做了细分：
```
block
columns 1
block:groupTitle
Title["EasyAR 产品结构简图"]
end
block:groupTool
Tool["工作流工具"]
MegaToolbox["Mega Toolbox"]
MegaStudio["Mega Studio"]
space
end
block:groupSDK
SDK["SDK"]
Sense["Sense"]
SenseUnity["Sense<br>Unity Plugin"]
MegaWeChat["Mega<br>WeChat MiniProgram Plugin"]
end
block:groupService
Service["云服务"]
Mega["Mega<br>Service"]
SpatialMap["SpatialMap<br>Service"]
CRS["Cloud Recognition<br>Service"]
end
style groupTitle fill:none,stroke:none,stroke-width:0px
style Title fill:none,stroke:none,stroke-width:0px
style Tool fill:none,stroke:none,stroke-width:0px
style SDK fill:none,stroke:none,stroke-width:0px
style Service fill:none,stroke:none,stroke-width:0px
```
* **云服务**提供大规模识别定位能力
* **Mega Service**：`EasyAR Mega` 的核心部件。
* **SpatialMap Service**：为 `EasyAR Sense` 的稀疏空间地图提供云端支持的服务。
* **Cloud Recognition Service**：`EasyAR CRS` 的核心部件。
* **SDK** 提供丰富的本地功能，并利用**云服务**提供更加强大的能力
* **Sense**：`EasyAR Sense` 的核心 SDK。
* **Sense Unity Plugin**： `EasyAR Sense` 的 Unity 插件。
* **Mega WeChat MiniProgram Plugin**：`EasyAR Mega` 的微信小程序插件。
* **工作流工具**提供可视化的管理和测试工具
* **Mega Toolbox**：`EasyAR Mega` 的可视化采集和测试工具。
* **Mega Studio**：`EasyAR Mega` 的可视化编辑和管理工具。
在开发 AR 应用时，可能会同时使用一个或多个产品模块以满足不同场景下的功能需求。
>
> 比如：
>
>
> 开发涂涂乐应用时，可以使用
> Sense Unity Plugin
> 在 Unity 中开发跨平台应用，跟踪图像并渲染 3D 模型。
>
> 开发 Live 照片应用时，可以使用
> Sense
> 开发 Android 和 iOS 原生应用识别跟踪照片并播放视频；或使用
> Cloud Recognition Service
> 提供海量照片的云端识别服务，并在微信小程序中直接调用该服务接口实现照片识别功能。
>
> 开发 AR 导航应用时，可以使用
> Mega Service
> 来实现大场景定位；使用
> Sense Unity Plugin
> 在 Unity 中调用 EasyAR Mega 的接口和 EasyAR Sense 的运动跟踪功能实现 AR 导航能力；使用
> Mega Studio
> 来加载真实世界模型并辅助导航路线的摆放；使用
> Mega Toolbox
> 来快速验证定位跟踪效果。
>
>
`EasyAR Mega` 提供了这些 AR 能力，可以用于构建各种手机应用、微信小程序等多种平台的 AR 应用：
* **Mega 固定空间**：适用于 AR 导航、文旅导览、地标秀、大空间游戏等大空间场景。
* **Mega 复杂物体**：适用于 AR 文物讲解、工厂培训、AR 手办特效、车展营销等复杂物体。
`EasyAR CRS` 提供了这些 AR 能力，可以用于构建各种手机应用、微信小程序、Web 应用等多种平台的 AR 应用：
* **图像云识别**：适用于AR 绘本、文创产品、TCG 卡牌、Live 照片等大规模图像识别场景。
`EasyAR Sense` 提供了这些 AR 能力，可以用于构建手机、XR 头显、PC 等多种平台的 AR 应用：
* **运动跟踪**：适用于 AR 空间画笔、远程协作等场景。
* **平面检测**：适用于 AR 商品展示、虚拟装饰等场景。
* **稀疏空间地图（房间级锚点）**：适用于小空间交互和游戏等场景。
* **稠密空间地图（网格化）**：适用于环境交互游戏等场景。
* **表面跟踪（无尺度锚定）**：适用于 AR 空间特效等场景。
* **图像跟踪**：适用于 AR 卡片、涂涂乐、品牌营销等场景。
* **物体跟踪**：适用于 AR 地球仪等场景。
此外，`EasyAR Sense` 可集成并使用以下云端或高级能力：
* **Mega 固定空间**
* **Mega 复杂物体**
* **图像云识别**
## 开发不同平台的 AR 应用
使用 EasyAR 可以在不同平台上开发 AR 应用。
### Unity （推荐）
使用 Unity 开发 AR 应用是比较推荐的一种方式。使用 Unity 可以高效地开发跨平台 3D 内容和交互。
![alt text](https://doc-asset.easyar.com/develop/media/unity.png)
使用 Unity 开发的 AR 应用可以使用以下功能：
* `EasyAR Mega` 的全部功能
* `EasyAR CRS` 的全部功能
* `EasyAR Sense` 的全部功能
使用 Unity 开发的 AR 应用可以发布到以下设备和平台：
* Android 手机和平板等设备
* iOS 手机和平板
* 各类 XR 头显
* Windows 电脑
* macOS 电脑
### 微信小程序
在 [微信小程序](https://developers.weixin.qq.com/miniprogram/dev/framework/) 平台上，可以使用 **Mega WeChat MiniProgram Plugin** 或 **Cloud Recognition Service** 接口开发微信 AR 应用。在小程序上，可以使用 [XR-Frame](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/) 进行 3D 渲染和交互开发。另外也可以使用其它 Web 3D 引擎（如 [PlayCanvas](https://playcanvas.com/) 或 [Three.js](https://threejs.org/)）进行开发，但是需要较为复杂的额外适配工作。
![alt text](https://doc-asset.easyar.com/develop/media/wechat.png)
微信小程序平台上的 AR 应用可以使用以下功能：
* `EasyAR Mega` 的全部功能（仅支持 XR-Frame）
* `EasyAR CRS` 的全部功能
* 运动跟踪[1](#fn:1)
* 平面检测[1](#fn:1)
* 图像跟踪[1](#fn:1)（不能与 `EasyAR Mega` 同时使用）
* 物体跟踪[1](#fn:1)（不能与 `EasyAR Mega` 同时使用）
在微信平台上，我们还为 [AR 导航](https://www.sightp.com/nav.html) 和 [AR 文旅](https://www.sightp.com/tourism.html) 提供了成熟的解决方案。如有需求请联系 EasyAR 商务。
### 原生应用
直接使用原生接口开发 AR 应用也是可以的，但并不推荐。主要原因是通常 AR 所需的 3D 内容和交互在不使用 3D 引擎的情况下实现起来比较复杂，且内容制作效率很低。一般只有在绘制简单几何体或播放视频这些简单内容时才建议使用。
![alt text](https://doc-asset.easyar.com/develop/media/native.png)
使用原生接口开发的 AR 应用可以使用以下功能：
* `EasyAR Mega` 的全部功能
* `EasyAR CRS` 的全部功能
* `EasyAR Sense` 的全部功能
使用原生接口开发的 AR 应用可以发布到以下设备和平台：
* Android 手机和平板等设备
* iOS 手机和平板
* 各类 XR 头显[2](#fn:2)
* Windows 电脑
* macOS 电脑
### 搭建自己的 AR 平台
如果您研发了一款 3D 引擎，或是希望在某款 EasyAR 尚未提供支持的 3D 引擎中使用 EasyAR，可以使用 `EasyAR Sense` 的原生 SDK 在您的 3D 引擎中集成 EasyAR 功能。这个过程通常需要较强的 C/C++ 开发经验，以及对 3D 引擎实现的充分理解和控制力。一般来说，我们建议不希望在应用中引入 Unity 的企业考虑这种方式。
使用这种方式搭建的 AR 平台或应用可以使用以下功能：
* `EasyAR Mega` 的全部功能
* `EasyAR CRS` 的全部功能
* `EasyAR Sense` 的全部功能
使用这种方式搭建的 AR 平台或应用可以发布到以下设备和平台：
* Android 手机和平板等设备
* iOS 手机和平板
* 各类 XR 头显[2](#fn:2)
* Windows 电脑
* macOS 电脑
### Unreal
EasyAR 的 Unreal 支持尚处于实验阶段，如有需求可以联系 EasyAR 商务商讨定制开发事宜。
![alt text](https://doc-asset.easyar.com/develop/media/unreal.png)
与此同时，如果您或您的团队有较好的 C/C++ 开发经验，尤其是对 Unreal 引擎渲染管线和插件开发有一定了解，可以考虑使用 `EasyAR Sense` 的原生 SDK 在 Unreal 引擎中集成 EasyAR 功能。
## 从这里开始
* [EasyAR 增强现实入门](getting-started/ar.html)
* [Unity 开发快速入门](unity/getting-started/quickstart.html)
* [微信小程序开发快速入门](wechat/getting-started/quickstart.html)
* [原生开发入门](native/getting-started/choosing-an-engine.html)
* [Web 开发入门](web/getting-started/quickstart.html)
* [初见 Mega](../mega/overview.html)
* [基础组件](fundamentals/fundamentals.html)
* [摄像头和输入扩展](cameras/cameras.html)
* [XR 头显](headsets/headsets.html)
* [输入帧录制和模拟运行](simulation/simulation.html)
* [问题诊断和报告](diagnostics/diagnostics.html)
* [Mega （固定空间和复杂物体）](mega/intro.html)
* [运动跟踪](motion-tracking/intro.html)
* [平面检测](plane-detection/intro.html)
* [稀疏空间地图（房间级空间锚点）](sparse-spatial-mapping/intro.html)
* [稠密空间地图（网格化）](dense-spatial-mapping/intro.html)
* [表面跟踪（无尺度锚定）](surface-tracking/intro.html)
* [图像跟踪](image-tracking/intro.html)
* [图像云识别](cloud-recognition/intro.html)
* [物体跟踪](object-tracking/intro.html)
* [EasyAR Sense 支持的设备和平台](devices-sense.html)
* [EasyAR Mega 支持的设备和平台](mega/devices.html)
* [EasyAR CRS 支持的设备和平台](devices-crs.html)
* [EasyAR 支持的 XR 头显](headsets/headsets.html)
1. 由微信 [VisionKit](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/base.html) 提供支持。[↩](#fnref:1)[↩](#fnref:2)[↩](#fnref:3)[↩](#fnref:4)
2. 要让原生应用支持头显通常还需要设备厂商提供专门的 SDK 支持。除 Apple Vision Pro 外，大部分设备厂商并未在原生 SDK 中公开对接 EasyAR 所需的接口和数据。[↩](#fnref:5)[↩](#fnref:6)

---

## 平面检测支持的设备和平台
- 章节路径: `plane-detection/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/plane-detection/devices.html

# 平面检测支持的设备和平台
本章节介绍平面检测功能支持的设备硬件要求和支持的开发平台。
## 平面检测支持的设备
平面检测支持 Android，需要设备本身支持 6DoF 的 EasyAR Motion Tracker 开启时才生效。
如果要使用 ARKit 或 ARCore 等平面检测功能，无法通过 EasyAR 单独实现，在 Unity 上可以通过 [AR Foundation](../unity/fundamentals/arfoundation.html) 联合 EasyAR 实现，Native 开发上可以使用自定义相机同时使用 EasyAR 和 ARKit/ARCore。
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上的 Unity 或者原生上使用平面检测功能。需要注意的是是录制 EIF 的设备同样支持运动跟踪功能。
## 延伸阅读
* [运动跟踪与EasyAR其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker支持的设备](../motion-tracking/devices-easyar.html)

---

## EasyAR 平面检测
- 章节路径: `plane-detection/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/plane-detection/intro.html

# EasyAR 平面检测
EasyAR 平面检测是在运行 EasyAR 运动跟踪时，自动检测环境中的水平面或者竖直面，提供虚拟物体放置等功能。
## EasyAR 平面检测原理
EasyAR 平面检测（Plane Detection）是在 **运行 EasyAR 运动跟踪（Motion Tracker）过程中同步** 自动完成的一种简单的环境理解能力。系统基于设备摄像头和惯性传感器获取的时空信息，对真实环境进行连续建模，从而识别并跟踪环境中的水平面与竖直面，为虚拟物体放置、交互对齐和空间理解提供基础支持。
![planedetection](https://doc-asset.easyar.com/develop/plane-detection/media/plane-detection.png)
具体的流程为：
1. 运动跟踪
在运动跟踪运行期间，EasyAR 持续获取以下两类核心数据来自 RGB 摄像头的连续图像帧、加速度计和陀螺仪的数据。系统通过视觉–惯性融合算法估计设备在世界坐标系中的连续六自由度位置和姿态，为后续的空间建模与平面分析提供稳定、低漂移的相机轨迹。
2. 特征点检测和三角化
在位姿估计的基础上，EasyAR 从图像序列中提取并跟踪稳定的视觉特征点（如角点或纹理显著区域），并通过多视几何方法将这些特征点三角化，恢复其在三维空间中的位置，形成一个局部三维点云表示。
3. 平面候选区域生成
在获得三维点云后，系统对点云进行几何分析，以发现可能属于同一平面的点集。通过与重力方向的关系判断，系统可以区分不同类型的平面候选：
* 水平面：法向量与重力方向近似平行（如地面、桌面）；
* 竖直面：法向量与重力方向近似垂直（如墙面、立柱）。
* 平面跟踪与检测
EasyAR 会在连续帧中对已检测到的平面进行验证和更新：
* 判断新观测到的三维点是否支持已有平面模型；
* 根据观测一致性动态调整平面范围、边界和置信度；
* 剔除短暂出现或不稳定的平面候选。
只有在几何一致性和时间稳定性均满足要求时，结果才会被为“可用平面”。
* 平面坐标系与虚拟内容对齐
一旦平面被确认，您可基于平面检测结果实现更真实的 AR 效果：
* 在平面上放置虚拟物体，实现真实尺度和方向的对齐；
* 进行射线投射（Hit Test），将屏幕点击映射到真实平面位置；
* 实现基于平面的交互逻辑，如物体吸附、移动和遮挡判断。
由于平面与运动跟踪系统共享同一世界坐标系，虚拟物体在用户移动设备时能够保持稳定、连续的空间一致性。
平面检测依赖于运动跟踪提供的稳定位姿和空间结构，而平面检测结果反过来也可用于增强环境理解能力，例如辅助内容放置和交互设计。二者共同构成 EasyAR 空间感知能力的核心基础，但在系统架构上相互解耦，平面检测不会改变运动跟踪本身的位姿估计结果。
## 最佳实践
为了保证用户使用平面检测的效果，遵循以下实践能提升用户体验。
* 引导用户缓慢移动，避免静止不动、快速运动或者原地旋转。
* 避免无纹理、纯色、镜面等视觉难以识别的平面。
> **注意**
平面检测是 EasyAR 识别环境中水平或竖直平面的功能，表面跟踪并不检测或者识别场景中的平面结构，需要进行区分。
## 延伸阅读
* [平面检测支持的设备](devices.html)

---

## 录制 EIF 文件并用于模拟运行
- 章节路径: `simulation/simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/simulation/simulation.html

# 录制 EIF 文件并用于模拟运行
**EIF 文件（EasyAR Input Frame file）** 是 EasyAR Sense 用来存储一系列输入帧数据的文件格式。本文主要描述如何录制 EIF 文件并用于模拟运行。
## EIF 文件和内容
EIF 文件根据不同的录制方式，存在两个实现：
* 原始 EIF 格式（通常扩展名为.eif）
原始的 EIF 文件以 EasyAR 内部定义的数据结构逐帧存储输入帧数据，包括图像和附加信息（如 camera 参数和跟踪状态等）。这种格式不做视频压缩，而是逐帧编码（例如 JPEG 图像数据），适合精确回放。
* EIF MKV 格式（通常扩展名为.mkveif）
基于 MKV 封装的视频格式，在此基础上将输入帧的信息编码进 MKV 容器。视频编码使用 H.264 来压缩图像数据，同时保留输入帧其他元数据（如 IMU 传感器数据、定位数据等）作为流或附加轨道。这样可以显著减少文件体积，并便于标准视频流处理。
> **注意**
EIF MKV 格式目前只支持 Android/iOS/macOS/visionOS 上的录制和 Windows/macOS 上的回放，传统 EIF 格式无此限制。
## EIF 录制和回放
EasyAR 提供了录制和回放的一整套机制，主要通过以下组件控制：
* InputFrameRecorder / InputFramePlayer
* 用途
对应于原始 EIF 格式的录制和回放组件。
* 特点
录制过程中，所有传入的输入帧都会被序列化保存，包括图像、参数、跟踪状态等。
* VideoInputFrameRecorder / VideoInputFramePlayer
* 用途
对应于 EIF MKV 格式的录制和回放组件。
* 特点
录制时支持更多传感器数据流（如陀螺仪、加速度计、定位数据等），并将其一起封装入 EIF MKV 文件。播放端可选择输出这些数据，方便在 PC 端完整模拟录制时的各种输入。
## 使用 EIF 模拟运行的原理和可达到的效果
将录制好的 EIF 文件作为输入数据源，相当于把物理摄像头及其相关传感器在运行时的完整数据流“重播”给 AR 引擎。通过模拟输入帧序列：
* AR 引擎认为它仍然在获取物理摄像头的数据
回放输出的每一帧都具有原始时间戳、相机参数和跟踪状态，驱动算法像运行实时数据一样处理这些帧。
* 可以在非设备环境（如 PC 或 Unity 编辑器）复现真实运行时行为
这样你无需实机即可调试视觉跟踪、空间地图等功能，可以在 Windows/Mac 上模拟运行 Mega 等功能。
使用 EIF 模拟运行可达到的效果：
* 重现真实的数据流转过程
即便在没有摄像头的情况下，也可以像真实运行一样驱动 AR 功能，如平面图像跟踪、空间定位、稠密地图生成等。
* 便于开发调试与诊断
录制的 EIF 文件可用于分析跟踪失败原因、验证 AR 算法在特定输入上的行为或性能波动。
* 跨平台回放
在不同平台之间传输 EIF 文件，在 PC 上复现手机上录制的 AR Session 行为，无需设备即可调试。
## 后续步骤
* [录制EIF数据：复现AR问题的高保真依据](../diagnostics/simulation.html)
## 平台专用指南
录制 EIF 文件并用于模拟运行与平台紧密相关。请根据您的目标平台，参考以下指南进行开发：
* [Unity AR 模拟运行](../unity/simulation/simulation.html)
* [录制 EIF 文件](../unity/simulation/recording.html)
* [使用 EIF 文件模拟运行](../unity/simulation/playback.html)
* [使用 Session 验证工具播放 EIF 文件](../unity/simulation/tool.html)

---

## EasyAR 稀疏空间地图与 ARKit/ARCore 的区别
- 章节路径: `sparse-spatial-mapping/comparison.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/comparison.html

# EasyAR 稀疏空间地图与 ARKit/ARCore 的区别
EasyAR 稀疏空间地图用于扫描用户周围小范围环境（房间级别），建立视觉地图并导出，可用于多个设备间实时共享，实现多人互动、持久化等功能。类似的方案还包括 ARKit 提供的 ARWorldMap 和 ARCore 提供的 Cloud Anchors。
* ARWorldMap 支持将扫描场景序列化、持久化重定位，可以实现在 iOS 平台上的持久化、多人共享体验。
* Cloud Anchors 将用户扫描环境数据上传到 Google Cloud 上，通过重定位实现多人共享 AR 体验。
EasyAR 稀疏空间地图实现了离线、跨平台、高度自由的地图管理，更适合以下场合：
* 需要完全离线运行的场景（工厂小范围、地下室、展览馆无网环境）。
* 要跨 iOS/Android 等多平台共享同一套地图。
* 开发者希望自己完全掌控地图数据。
> **注意**
如果要扫描和重建的区域超过 100 平方米或者场景光照、季节等变化较大，建议升级至 [EasyAR Mega](../mega/intro.html) 功能。
## 延伸阅读
* [ARKit ARWorldMap](https://developer.apple.com/documentation/arkit/arworldmap)
* [ARCore Cloud Anchors](https://developers.google.com/ar/develop/cloud-anchors)

---

## 稀疏空间地图支持的设备和平台
- 章节路径: `sparse-spatial-mapping/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/devices.html

# 稀疏空间地图支持的设备和平台
本章节介绍稀疏空间地图功能 (Sparse Spatial Map) 支持的设备硬件要求和开发平台。
## 稀疏空间地图支持的设备
稀疏空间地图支持 iOS/Android/鸿蒙以及部分头显平台。硬件上，需要设备本身支持 6DoF 的[运动跟踪](../motion-tracking/intro.html)功能。
稀疏空间地图可用的运动跟踪类型包括：
* EasyAR 运动跟踪（Motion Tracker）
* 谷歌 ARCore
* 苹果 ARKit
* 华为 AR Engine
* 六自由度跟踪能力的头显或眼镜
通过录制 [EIF 文件](../simulation/simulation.html)并重放的机制，可以在 PC 上通过 Unity 或者原生使用稀疏空间地图功能。需要注意的是录制 EIF 的设备必须支持运动跟踪功能。
如果您的设备支持运动跟踪功能，可以参照 [自定义相机](../cameras/custom-camera.html) 的方式接入 EasyAR 并使用稀疏空间地图功能。
## 延伸阅读
* [运动跟踪与 EasyAR 其他功能](../motion-tracking/motion-tracking-and-easyar.html)
* [运动跟踪支持的设备](../motion-tracking/devices.html)
* [EasyAR Motion Tracker支持的设备](../motion-tracking/devices-easyar.html)
* [华为 AR Engine支持的设备](../motion-tracking/devices-arengine.html)

---

## EasyAR 稀疏空间地图
- 章节路径: `sparse-spatial-mapping/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/sparse-spatial-mapping/intro.html

# EasyAR 稀疏空间地图
EasyAR 稀疏空间地图（Sparse Spatial Map）用于扫描用户周围小范围环境（房间级别），生成环境的三维视觉地图并提供视觉定位跟踪功能。适用于开发持久化 AR 应用或多人互动 AR 应用。
## EasyAR 稀疏空间地图原理
EasyAR 稀疏空间地图在运动跟踪的基础上，在设备端利用计算机视觉算法，分析摄像头数据的特征建立环境的空间三维地图。用户可以保存视觉地图或多个设备间实时共享。当其他设备加载相应地图，并在加载地图中通过定位确定设备相对于地图的位置和姿态，从而开发持久化 AR 应用或多人互动 AR 应用。
稀疏空间地图目前需要稳定的运动跟踪系统（例如 EasyAR Motion Tracker、ARCore、ARKit）提供六自由度的位置和姿态用于建图中及定位成功后的持续跟踪。在建图过程中，稀疏空间地图利用相机图像和对应位姿构建环境1:1的视觉地图。定位过程中，当视觉定位成功后，设备相对地图的位姿通过运动跟踪系统持续更新。
EasyAR 稀疏空间地图支持加载多个地图，在多个地图中定位并返回对应地图的 ID 和设备相对于该地图的位置和姿态。
![ssmintro](https://doc-asset.easyar.com/develop/sparse-spatial-mapping/media/sparsespatialmap-intro.png)
## 建图最佳实践
在创建稀疏空间地图时，你需要充分考虑用户会在什么地点、视角下进行定位，以此来优化建图的过程。建图时尽量覆盖到所有的可能定位所在视角，包括观察的角度和距离。
以下是提高建图效果的最佳实践：
* 尽量相对于被扫描区域、场景做平移运动或缓慢旋转。
* 尽可能充分移动扫描覆盖用户可能定位的位置。
* 尽量在具备丰富、稳定且静止的视觉特征区域进行建图。
* 单个地图范围不超过 1000 平方米。
* 建图设备到场景距离应小于 10 米。
在扫描建图时需要避免以下情况：
* 避免在大片的无视觉特征区域进行建图，如白墙。
* 避免在大片的反光材质区域进行建图，如玻璃、镜面物体。
* 避免在重复性的纹理区域建图。
建图完成后，可以在建立的稀疏空间地图中测试定位，检查定位的成功率和精度，若发现效果不理想，考虑重新建立更完整地图。
## 定位最佳实践
为了保证用户使用稀疏空间地图的定位效果，遵循以下实践能提高成功率并提升用户体验。
* 引导用户在地图对应的场景中进行定位，例如给出目标场景的预览图，帮助用户找到目标场景。
* 引导用户缓慢移动设备从多个角度尝试进行定位。
* 避免无视觉特征、镜面、含重复纹理的区域进行定位。
## 定位失败的常见原因
用户定位的环境与地图构建的环境存在较大差异时，可能将导致定位失败，如：
* 视角变化
确保建图尽可能覆盖潜在定位角度。如果定位的角度和最接近建图角度差别超过 45°，定位成功率会大幅下降。
* 光照差异
建图光照和定位光照相近情况下，定位成功率最高。例如尽量避免在白天建图后，在漆黑的夜晚尝试定位。
* 距离变化
建图时移动手机并覆盖不同距离的位置。例如距离目标 1 米附近的位置建图后，在距离 10 米的地方尝试定位容易失败。
## 延伸阅读
* [稀疏空间地图支持的设备](devices.html)
* [稀疏空间地图与 ARKit/ARCore 区别](comparison.html)

---

## 表面跟踪支持的设备和平台
- 章节路径: `surface-tracking/devices.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/surface-tracking/devices.html

# 表面跟踪支持的设备和平台
表面跟踪功能支持 Android 和鸿蒙系统的手机及平板，不支持 PC、MR 头显、可穿戴眼镜。 开发者可以通过 Unity 或 Native 进行开发。
## 额外的硬件要求
除了摄像头之外，表面跟踪还需要设备支持陀螺仪或加速度计。
> **注意**
虚拟的陀螺仪、自定义相机等均不可用表面支持功能。

---

## EasyAR 表面跟踪
- 章节路径: `surface-tracking/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/surface-tracking/intro.html

# EasyAR 表面跟踪
EasyAR 表面跟踪（Surface Tracking）实现轻量级的持续跟踪设备相对于空间中选定表面点的位置和姿态的能力，可用于小型 AR 交互游戏、AR 短视频拍摄以及产品放置展示等场景。
## EasyAR 表面跟踪的原理
为了在真实空间和虚拟空间之间建立对应关系，表面跟踪利用了设备摄像头和惯性测量单元的数据。
表面跟踪首先通过摄像头图像识别环境表面（不一定是平面上）的显著特征，使用连续图像帧和传感器数据跟踪这些特征的位置。启动时虚拟物体默认被放置在屏幕中间附近的特征点表面，并将虚拟物体的位置视为世界坐标系的原点。
虚拟物体同样被放置在相应的特征点的位置并持续跟踪。在移动设备期间，相机图像中的特征深度不断更新，虚拟物体持续贴合在相应的特征点表面。如果虚拟物体所对应的特征点丢失，系统自动选择新的特征点并输出设备相对于该特征点的位置和姿态。
> **注意**
表面跟踪的特征丢失，可能导致虚拟物体的位置发生漂移，如果持续跟踪固定位置推荐使用[运动跟踪](../motion-tracking/intro.html)。
## 表面跟踪与运动跟踪对比
与[运动跟踪](../motion-tracking/intro.html)相比， 表面跟踪无需设备标定、支持更多机型，无需初始化即可运行。但是表面跟踪并不提供真实尺度，只能放置一个虚拟物体，且虚拟物体的底部要放置在坐标系原点。
|对比维度|表面跟踪|[运动跟踪](../motion-tracking/intro.html)|
|设备标定要求|无需设备标定|需要设备标定|
|机型支持范围|支持更多机型|对硬件能力要求较高，支持机型相对有限|
|空间尺度|不提供真实世界尺度|提供真实尺度的位姿|
|初始化流程|无需初始化即可运行|通常需要初始化过程|
|虚拟物体数量|仅支持放置一个虚拟物体|可支持多个虚拟物体|
|虚拟物体放置约束|虚拟物体底部必须放置在坐标系原点|虚拟物体可放置在任意空间位置|
|适用场景|轻量级 AR 展示、快速体验|高精度 AR、空间交互、导航与测量|
> **注意**
表面跟踪尽量保持虚拟物体贴合在环境的表面上（可能是不平物品表面或者平坦的地面、墙面），但是并不检测环境中是否存在平面。如果需要检测环境中水平面或垂直面功能，请查阅 [平面检测功能](../plane-detection/intro.html)。
## 延伸阅读
* [表面跟踪支持的设备](devices.html)

---

## CameraDeviceFrameSource 组件参考
- 章节路径: `unity/cameras/comp-CameraDeviceFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/comp-CameraDeviceFrameSource.html

# CameraDeviceFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.CameraDeviceFrameSource.html)
>
探索 CameraDeviceFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/comp-CameraDeviceFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Camera Open Method**|打开物理相机时使用的方法。 选项：
* PreferredType（默认）：按照摄像头设备类型打开摄像头设备，如果没有匹配的类型则会尝试打开第一个摄像头设备。
* DeviceIndex：按照摄像头索引打开摄像头设备。
* SpecificType：按照精确的摄像头设备类型打开摄像头设备，如果没有匹配的类型则会失败。在 Mac 上，摄像头类型无法判别。|
|*Type*|Camera Open Method 是 PreferredType 或 SpecificType 时显示。
打开物理相机时使用的摄像头类型。选项：
* Back（默认）：后置摄像头。
* Front：前置摄像头。
* Unknown：未知位置。|
|*Index*|Camera Open Method 是 DeviceIndex 时显示。
打开物理相机时使用的设备索引。|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Default：使用默认值，实际选择与使用的 AR 功能有关。
* Input：使用指定值。选择 Input 时可选项：
* Normal：常规对焦模式，在这个模式下需要调用 [AutoFocus()](../../../api/unity/easyar.CameraDeviceFrameSource.html#u_easyar_CameraDeviceFrameSource_AutoFocus) 来触发对焦。
* Continousauto：连续自动对焦模式。
* Infinity：无穷远对焦模式。
* Macro：微距对焦模式。在这个模式下需要调用 [AutoFocus()](../../../api/unity/easyar.CameraDeviceFrameSource.html#u_easyar_CameraDeviceFrameSource_AutoFocus) 来触发对焦。
* Medium：中等距离对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Desired Camera Preference*|期望的 [CameraDevicePreference](../../../api/unity/easyar.CameraDevicePreference.html)。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* PreferObjectSensing：对图像跟踪和物体跟踪进行优化。
* PreferSurfaceTracking：对表面跟踪进行优化。
* PreferMotionTracking：对运动跟踪进行优化。|
|*Desired Android Camera Api*|期望的 Android Camera API。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Camera1：Android Camera1 API。
* Camera2：Android Camera2 API。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，如未设置会使用 Camera.main。|

---

## InertialCameraDeviceFrameSource 组件参考
- 章节路径: `unity/cameras/comp-InertialCameraDeviceFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/comp-InertialCameraDeviceFrameSource.html

# InertialCameraDeviceFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
>
探索 InertialCameraDeviceFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/comp-InertialCameraDeviceFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## ThreeDofCameraDeviceFrameSource 组件参考
- 章节路径: `unity/cameras/comp-ThreeDofCameraDeviceFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/comp-ThreeDofCameraDeviceFrameSource.html

# ThreeDofCameraDeviceFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
>
探索 ThreeDofCameraDeviceFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/comp-ThreeDofCameraDeviceFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## 创建图像和设备运动数据输入扩展
- 章节路径: `unity/cameras/external-device-frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-device-frame-source.html

# 创建图像和设备运动数据输入扩展
通过创建图像和设备运动数据输入扩展，开发者可以为 EasyAR Sense 扩展自定义的相机实现，从而支持特定的头显设备或其它输入设备。以下内容介绍了创建图像和设备运动数据输入扩展的步骤和注意事项。
## 开始之前
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
* 阅读 [外部帧数据源](external-frame-source.html) 了解创建外部帧数据源所需详细接口说明。
* 阅读 [外部输入帧数据](external-input-frame.html) 了解相机帧数据和渲染帧数据。
## 创建外部帧数据源类
* 如果需要创建 6DoF 设备输入扩展，继承 [ExternalDeviceMotionFrameSource](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html)
* 如果需要创建 3DoF 设备输入扩展，继承 [ExternalDeviceRotationFrameSource](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html)
它们都是 [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html) 的子类，文件名应与类名相同。
例如，创建一个 6DoF 设备输入扩展：
```
public class MyFrameSource : ExternalDeviceMotionFrameSource
{
}
```
在创建头显扩展时，可以使用 `com.easyar.sense.ext.hmdtemplate` 模板，在模板基础上进行修改。这个模板在从 EasyAR 网站下载获得的 Unity 插件压缩包内。
## 设备定义
重写 [IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD) 来定义设备是否是头显。
例如，在头显上设为 true。
```
public override bool IsHMD { get => true; }
```
重写 [Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display) 来定义设备的显示。
例如，在头显上默认的显示 [Display.DefaultHMDDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultHMDDisplay) 信息，这会定义显示旋转为 0。
```
protected override IDisplay Display => easyar.Display.DefaultHMDDisplay;
```
## 可用性
重写 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 来定义设备是否可用。
例如，[RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override Optional<bool> IsAvailable => Application.platform == RuntimePlatform.Android;
```
如果 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 在 session 组装时无法判断，可以重写 [CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程来阻塞组装过程，直到确定是否可用为止。
## session 原点
重写 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 来定义设备 SDK 定义的原点类型。
如果 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom)，还需要重写 [Origin](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_Origin) 。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override DeviceOriginType OriginType =>
#if EASYAR\_HAVE\_ROKID\_UXR
hasUXRComponents ? DeviceOriginType.None :
#endif
DeviceOriginType.XROrigin;
```
## 虚拟摄像机
如果 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom) 或 [None](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_None)，需要重写 [Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera) 来提供虚拟摄像机。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override Camera Camera => hasUXRComponents ? (cameraCandidate ? cameraCandidate : Camera.main) : base.Camera;
```
## 物理相机
使用 [DeviceFrameSourceCamera](../../../api/unity/easyar.DeviceFrameSourceCamera.html) 类型重写 [DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 以提供设备物理相机信息。这个数据会在输入相机帧数据时使用。[CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须完成创建。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
private DeviceFrameSourceCamera deviceCamera;
protected override List<FrameSourceCamera> DeviceCameras => new List<FrameSourceCamera> { deviceCamera };
{
var imageDimensions = new int[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetImageDimensions(imageDimensions);
size = new Vector2Int(imageDimensions[0], imageDimensions[1]);
deviceCamera = new DeviceFrameSourceCamera(CameraDeviceType.Back, 0, size, new Vector2(50, 50), new DeviceFrameSourceCamera.CameraExtrinsics(Pose.identity, true), AxisSystemType.Unity);
started = true;
}
```
重写 [CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 来提供相机帧开始输入的标识。
例如：
```
protected override bool CameraFrameStarted => started;
```
## session 启动和停止
重写 [OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_) 然后做 AR 独有的初始化工作。需要确保先调用 base.OnSessionStart。
例如：
```
protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
StartCoroutine(InitializeCamera());
}
```
这里是适合打开设备相机（比如 RGB 相机或 VST 相机等）的位置，尤其是如果这些相机没有被设计成要一直打开时。同时这里也是适合获取整个生命周期内不会变化的标定数据的位置。有时在这些数据可以被获取前可能需要等待设备准备好或等待数据更新。
同时，这里也是一个适合启动数据输入循环的位置。也可以在 [Update()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) 或其它方法中写这个循环，尤其是当数据需要在 Unity 执行顺序的某个特殊时间点获取的时候。在 session 准备好（ready）之前不要输入数据。
如果需要，也可以忽略启动过程并在每次更新时做数据检查，这完全取决于具体需求。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
private IEnumerator InitializeCamera()
{
yield return new WaitUntil(() => (RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() >= RokidTrackingStatus.Detecting && (RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() < RokidTrackingStatus.Tracking\_Paused);
var focalLength = new float[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetFocalLength(focalLength);
var principalPoint = new float[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetPrincipalPoint(principalPoint);
var distortion = new float[5];
RokidExtensionAPI.RokidOpenXR\_API\_GetDistortion(distortion);
var imageDimensions = new int[2];
RokidExtensionAPI.RokidOpenXR\_API\_GetImageDimensions(imageDimensions);
size = new Vector2Int(imageDimensions[0], imageDimensions[1]);
var cameraParamList = new List<float> { focalLength[0], focalLength[1], principalPoint[0], principalPoint[1] }.Concat(distortion.ToList().GetRange(1, 4)).ToList();
cameraParameters = CameraParameters.tryCreateWithCustomIntrinsics(size.ToEasyARVector(), cameraParamList, CameraModelType.OpenCV\_Fisheye, CameraDeviceType.Back, 0).Value;
deviceCamera = new DeviceFrameSourceCamera(CameraDeviceType.Back, 0, size, new Vector2(50, 50), new DeviceFrameSourceCamera.CameraExtrinsics(Pose.identity, true), AxisSystemType.Unity);
RokidExtensionAPI.RokidOpenXR\_API\_OpenCameraPreview(OnCameraDataUpdate);
started = true;
}
```
重写 [OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop) 并释放资源，需要确保调用 base.OnSessionStop。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected override void OnSessionStop()
{
base.OnSessionStop();
RokidExtensionAPI.RokidOpenXR\_API\_CloseCameraPreview();
started = false;
StopAllCoroutines();
cameraParameters?.Dispose();
cameraParameters = null;
deviceCamera?.Dispose();
deviceCamera = null;
}
```
## 输入相机帧数据
在获取相机帧数据更新后，调用 [HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Pose_easyar_MotionTrackingStatus_) / [HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Quaternion_) 来输入相机帧数据。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
private static void OnCameraDataUpdate(IntPtr ptr, int dataSize, ushort width, ushort height, long timestamp)
{
if (!instance) { return; }
if (ptr == IntPtr.Zero || dataSize == 0 || timestamp == 0) { return; }
if (timestamp == instance.curTimestamp) { return; }
instance.curTimestamp = timestamp;
RokidExtensionAPI.RokidOpenXR\_API\_GetHistoryCameraPhysicsPose(timestamp, positionCache, rotationCache);
var pose = new Pose
{
position = new Vector3(positionCache[0], positionCache[1], -positionCache[2]),
rotation = new Quaternion(-rotationCache[0], -rotationCache[1], rotationCache[2], rotationCache[3]),
};
// NOTE: Use real tracking status when camera exposure if possible when writing your own device frame source.
var trackingStatus = ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus()).ToEasyARStatus();
var size = instance.size;
var pixelSize = instance.size;
var pixelFormat = PixelFormat.Gray;
var yLen = pixelSize.x \* pixelSize.y;
var bufferBlockSize = yLen;
var bufferO = instance.TryAcquireBuffer(bufferBlockSize);
if (bufferO.OnNone) { return; }
var buffer = bufferO.Value;
buffer.tryCopyFrom(ptr, 0, 0, bufferBlockSize);
using (buffer)
using (var image = Image.create(buffer, pixelFormat, size.x, size.y, pixelSize.x, pixelSize.y))
{
instance.HandleCameraFrameData(instance.deviceCamera, timestamp \* 1e-9, image, instance.cameraParameters, pose, trackingStatus);
}
}
```
> **小心**
不要忘记在使用后执行 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 或通过 `using` 等机制释放 [Image](../../../api/unity/easyar.Image.html) 、[Buffer](../../../api/unity/easyar.Buffer.html) 以及其它相关数据。否则会出现严重内存泄漏，buffer pool 获取 buffer 也可能会失败。
## 输入渲染帧数据
在设备数据准备好之后，每个渲染帧调用 [HandleRenderFrameData(double, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Pose_easyar_MotionTrackingStatus_) / [HandleRenderFrameData(double, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Quaternion_) 来输入渲染帧数据。
例如， [RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html) 中的实现方式如下：
```
protected void LateUpdate()
{
if (!started) { return; }
if ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() < RokidTrackingStatus.Detecting) { return; }
if ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus() >= RokidTrackingStatus.Tracking\_Paused) { return; }
InputRenderFrameMotionData();
}
private void InputRenderFrameMotionData()
{
var timestamp = RokidExtensionAPI.RokidOpenXR\_API\_GetCameraPhysicsPose(positionCache, rotationCache);
var pose = new Pose
{
position = new Vector3(positionCache[0], positionCache[1], -positionCache[2]),
rotation = new Quaternion(-rotationCache[0], -rotationCache[1], rotationCache[2], rotationCache[3]),
};
if (timestamp == 0) { return; }
HandleRenderFrameData(timestamp \* 1e-9, pose, ((RokidTrackingStatus)RokidExtensionAPI.RokidOpenXR\_API\_GetHeadTrackingStatus()).ToEasyARStatus());
}
```
## 后续步骤
* 创建 [头显扩展包](../headsets/extension.html)
## 相关主题
* [帧数据源和运行时选取过程](frame-source.html)
* [AR Session](../fundamentals/session.html)
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)

---

## Unity 中的自定义相机实现 —— 外部帧数据源
- 章节路径: `unity/cameras/external-frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-frame-source.html

# Unity 中的自定义相机实现 —— 外部帧数据源
通过外部帧数据源（[ExternalFrameSource](../../../api/unity/easyar.ExternalFrameSource.html)），开发者可以为 EasyAR Sense 扩展自定义的相机实现，从而支持特定的头显设备或其它输入设备。以下内容介绍了外部帧数据源的类型结构及接口定义。
## 开始之前
* 了解 [自定义相机](../../cameras/custom-camera.html) 的基本概念。
* 了解 [帧数据源](frame-source.html) 的基本概念、类型以及运行时的选取方法。
## 外部帧数据源类型
```
---
config:
class:
hideEmptyMembersBox: true
---
classDiagram
class FrameSource {
<<abstract>>
}
class ExternalFrameSource {
<<abstract>>
}
class ExternalDeviceFrameSource {
<<abstract>>
}
class ExternalDeviceMotionFrameSource:::EasyAR {
<<abstract>>
}
class ExternalDeviceRotationFrameSource:::EasyAR {
<<abstract>>
}
class ExternalImageStreamFrameSource:::EasyAR {
<<abstract>>
}
ExternalFrameSource --|> FrameSource
ExternalDeviceFrameSource --|> ExternalFrameSource
ExternalDeviceMotionFrameSource --|> ExternalDeviceFrameSource
ExternalDeviceRotationFrameSource --|> ExternalDeviceFrameSource
ExternalImageStreamFrameSource --|> ExternalFrameSource
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
```
上图展示了外部帧数据源的类型结构。
根据输入数据的不同，外部帧数据源可以分为两大类：
* 图像和设备运动数据输入扩展
* 通过继承 [ExternalDeviceMotionFrameSource](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html) 实现：设备及设备 SDK 提供 6DoF 运动跟踪功能。虚拟摄像机的 transform 及其它控制由设备 SDK 完成。
* 通过继承 [ExternalDeviceRotationFrameSource](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html) 实现：设备及设备 SDK 提供 3DoF 旋转跟踪功能。虚拟摄像机的 transform 及其它控制由设备 SDK 完成。
* 图像输入扩展
* 通过继承 [ExternalImageStreamFrameSource](../../../api/unity/easyar.ExternalImageStreamFrameSource.html) 实现：仅提供图像输入。虚拟摄像机的 transform 及其它控制由 EasyAR 完成。
接入这几种外部帧数据源时，可以使用的 AR 功能有所不同：
* 图像和设备运动数据输入扩展 [ExternalDeviceMotionFrameSource](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html)
* Mega
* 运动跟踪（由设备自身提供）
* 稀疏空间地图
* 稠密空间地图
* 图像跟踪（支持运动融合）
* 图像云识别
* 物体跟踪（支持运动融合）
* 图像和设备运动数据输入扩展 [ExternalDeviceRotationFrameSource](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html)
* Mega
* 图像跟踪（不支持运动融合）
* 图像云识别
* 物体跟踪（不支持运动融合）
* 图像输入扩展 [ExternalImageStreamFrameSource](../../../api/unity/easyar.ExternalImageStreamFrameSource.html)
* 图像跟踪（不支持运动融合）
* 图像云识别
* 物体跟踪（不支持运动融合）
## 外部帧数据源接口定义
创建外部帧数据源时，必须实现相关接口。下面介绍了这些接口的定义及使用方法。
### 设备定义
* [FrameSource.IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD)：`定义是否为头显`
在且仅在头显设备上设为 true。
如果设备是头显，诊断信息将显示在摄像机前的 3D 板子而非屏幕上。部分 AR 功能在头显设备上运行会有些许不同。
* [FrameSource.Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display)：`定义显示系统`
提供当前显示的旋转等信息。
可以使用 [Display.DefaultSystemDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultSystemDisplay) 或 [Display.DefaultHMDDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultHMDDisplay) 来获取默认的显示信息。
通常在头显上可以使用 [Display.DefaultHMDDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultHMDDisplay)。
无额外设置。
* [FrameSource.IsCameraUnderControl](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsCameraUnderControl)：必须设置为 true。
### 可用性
* [FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable)：`可用性（Availability）`
用于判断 frame source 是否可以使用。
如果一个 frame source 在当前运行设备或环境下不可用，该数值应为 false。
如果该数值等于 Optional<bool>.Empty，[FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程会被调用，应在协程结束前更新 [FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable)。
可用性接口会在 session 组装时使用，不可用的组件将不会被选择且它的方法在 session 运行时不会被调用。
* [FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability)（可选）：`检查 frame source 是否可用的协程`
[FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 等于 Optional<bool>.Empty 时会被调用。在该协程结束前，session 的组装过程会被阻塞。
### session 原点
* [ExternalDeviceFrameSource.OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType)：`原点类型`
* [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin)：设备 SDK 使用 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 作为原点。
* [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom)：设备 SDK 使用自定义的原点。
需指定 [ExternalDeviceFrameSource.Origin](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_Origin)。
* [None](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_None)：设备 SDK 未定义原点。
这时原点将会自动从场景中选择或创建，但不会移动。
session 将只支持 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式。应用开发者必须对于他们如何摆放虚拟物体十分小心，因为所有 target 及 target 下的内容永远都会在 Unity 坐标系中移动，用户的部分内容（比如物理系统）将无法正常工作。所有放在 Unity 世界坐标系下的物体在任何配置下都永远不可能显示在正确的位置。
* [ExternalDeviceFrameSource.Origin](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_Origin)：`原点物体`
在且仅在 [ExternalDeviceFrameSource.OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 为 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom) 时定义自己的原点，其它时候不需要重新定义。
无。
### 虚拟摄像机
* [FrameSource.Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera)：`虚拟摄像机`
摄像机不受 session 控制，摄像机的 transform 和投影矩阵以及图像背景渲染应由外部代码控制。
仅在头显上该摄像机会被使用，用于将一些诊断文字展示在眼前。
在 [ExternalDeviceFrameSource.OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin) 时不需要定义，EasyAR 会自动使用 Unity XR 框架中定义的相机。
* [FrameSource.Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera)：`虚拟摄像机`
摄像机会受 session 控制，外部代码不能修改摄像机的 transform 和投影矩阵。
在头显上，该摄像机会用于将一些诊断文字展示在眼前。
### 物理相机
* [FrameSource.DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras)：`物理相机参数`
提供相机帧数据的物理相机。如果相机帧数据由多个相机提供，列表中需要包含所有物理相机。
需要确保在 [FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时可以获取到正确的物理相机参数。
* [FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted)：`相机帧是否开始输入`
在物理相机准备好并可以输入数据到 EasyAR 之后返回 true，物理相机停止运行后返回 false。在 [FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 false 时，EasyAR 不会工作。[FrameSource.CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须保证 [FrameSource.DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 数据可以访问且不间断地向 EasyAR 输入相机帧数据。在 EasyAR 检查到相机帧连续长时间无输入后会弹出警告，辅助用户判断功能无响应时进行问题解耦。
物理相机参数需要与真实设备相机相同。
* [FrameSourceCamera.CameraType](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraType)：`物理相机类型`
一般非前置相机的情况，比如头显上，选择后置相机。
* [FrameSourceCamera.CameraOrientation](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraOrientation)：`物理相机图像在设备的自然方向上显示时需要顺时针旋转的角度`
范围为 [0, 360)。
* [FrameSourceCamera.FrameSize](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameSize)：`图像尺寸`
* [FrameSourceCamera.FrameRateRange](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameRateRange)：`帧率范围`
定义 x 为帧率范围下界 y 为帧率范围上界。
* [DeviceFrameSourceCamera.AxisSystem](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_AxisSystem)：`头/物理相机 pose 以及物理相机外参使用的坐标轴系统`
所有矩阵必须使用相同的坐标轴系统。如果使用的数据定义不符合已知的系统，需要在传给 EasyAR 之前进行坐标轴变换。
* [DeviceFrameSourceCamera.Extrinsics](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_Extrinsics)：`物理相机外参`
一般是标定的矩阵。其坐标轴应符合 [DeviceFrameSourceCamera.AxisSystem](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_AxisSystem) 定义。如果外参的坐标轴定义与实际 pose 的坐标轴定义不同或它们不符合 [DeviceFrameSourceCamera.AxisSystem](../../../api/unity/easyar.DeviceFrameSourceCamera.html#u_easyar_DeviceFrameSourceCamera_AxisSystem) 的定义，需要在设置这个数值之前进行坐标轴变换。
物理相机参数需要与真实设备相机相同。如果是通过视频文件等输入，需要与录制视频时的物理相机或等价相机模型参数相同。
* [FrameSourceCamera.CameraType](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraType)：`物理相机类型`
一般非前置相机的情况，比如头显上，选择后置相机。
* [FrameSourceCamera.CameraOrientation](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_CameraOrientation)：`物理相机图像在设备的自然方向上显示时需要顺时针旋转的角度`
范围为 [0, 360)。
* [FrameSourceCamera.FrameSize](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameSize)：`图像尺寸`
* [FrameSourceCamera.FrameRateRange](../../../api/unity/easyar.FrameSourceCamera.html#u_easyar_FrameSourceCamera_FrameRateRange)：`帧率范围`
定义 x 为帧率范围下界 y 为帧率范围上界。
### session 启动和停止
* [FrameSource.OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_)：`处理 session 启动事件`
在 session 组装时选择了这个 frame source 时有效。
可以用于延迟初始化，在这个方法中进行 AR 独有的初始化工作。
* [FrameSource.OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop)：`处理 session 停止事件`
在 session 组装时选择了这个 frame source 时有效。
可以在这个方法中销毁 [FrameSource.OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_) 以及 session 运行中创建的资源并恢复内部状态。在 session 销毁之前这个方法会被保证调用。如果 frame source 在 session 之前销毁，它将不会被调用，且 session 将进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态。
### 输入帧
* [ExternalDeviceMotionFrameSource.HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Pose_easyar_MotionTrackingStatus_)：`输入相机帧数据`
* [ExternalDeviceRotationFrameSource.HandleCameraFrameData(DeviceFrameSourceCamera, double, Image, CameraParameters, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleCameraFrameData_easyar_DeviceFrameSourceCamera_System_Double_easyar_Image_easyar_CameraParameters_UnityEngine_Quaternion_)：`输入相机帧数据`
可以在任何线程调用，只要设备 SDK 的 API 都是线程安全的即可。
这些数据需要与物理相机传感器曝光时的数据一致。建议输入 30 或 60 fps 的数据。最小可接受帧率为 2，但部分算法响应时间会受影响。只要可以获取，建议输入彩色数据，这对 Mega 的效果是有帮助的。
为实现最佳效率，可以设计整个数据链条让原始 YUV 数据直接通过共享内存透传，并直接使用数据指针传入 EasyAR，并注意数据所有权。
* [ExternalDeviceMotionFrameSource.HandleRenderFrameData(double, Pose, MotionTrackingStatus)](../../../api/unity/easyar.ExternalDeviceMotionFrameSource.html#u_easyar_ExternalDeviceMotionFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Pose_easyar_MotionTrackingStatus_)：`输入渲染帧数据`
* [ExternalDeviceRotationFrameSource.HandleRenderFrameData(double, Quaternion)](../../../api/unity/easyar.ExternalDeviceRotationFrameSource.html#u_easyar_ExternalDeviceRotationFrameSource_HandleRenderFrameData_System_Double_UnityEngine_Quaternion_)：`输入渲染帧数据`
需要确保在设备数据准备好之后每个渲染帧调用，不能跳帧。这些数据需要与驱动同一帧内当前 Unity 虚拟摄像机的数据一致。
* [ExternalImageStreamFrameSource.HandleCameraFrameData(double, Image, CameraParameters)](../../../api/unity/easyar.ExternalImageStreamFrameSource.html#u_easyar_ExternalImageStreamFrameSource_HandleCameraFrameData_System_Double_easyar_Image_easyar_CameraParameters_)：`输入相机帧数据`
可以在任何线程调用，只要设备 SDK 的 API 都是线程安全的即可。
这些数据需要与物理相机传感器曝光时的数据一致。建议输入 30 或 60 fps 的数据。最小可接受帧率为 2，但部分算法响应时间会受影响。只要可以获取，建议输入彩色数据，这对 Mega 的效果是有帮助的。
为实现最佳效率，可以设计整个数据链条让原始 YUV 数据直接通过共享内存透传，并直接使用数据指针传入 EasyAR，并注意数据所有权。
* [ExternalFrameSource.TryAcquireBuffer(int)](../../../api/unity/easyar.ExternalFrameSource.html#u_easyar_ExternalFrameSource_TryAcquireBuffer_System_Int32_)：`尝试从内存池中获取内存块`
这个内存块通常用于存储相机帧的图像数据并输入 EasyAR。
* [ExternalFrameSource.ReceivedFrameCount](../../../api/unity/easyar.ExternalFrameSource.html#u_easyar_ExternalFrameSource_ReceivedFrameCount)：`EasyAR 获取到的相机帧计数`
EasyAR 会用它来检查设备相机帧输入的健康情况。可以在调试中使用，如果这个数值停止增长，通常说明设备停止向 EasyAR 输入数据。
### Unity 消息
在脚本中使用以下消息时，需要注意确保基类实现被调用：
* [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html)
* [OnApplicationPause(Boolean)](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnApplicationPause.html)
* [OnDestroy()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnDestroy.html)
## 后续步骤
* 阅读 [外部输入帧数据](external-input-frame.html) 了解相机帧数据和渲染帧数据
* 创建 [图像和设备运动数据输入扩展](external-device-frame-source.html)
* 创建 [图像输入扩展](external-image-stream-frame-source.html)
## 相关主题
* [AR Session](../fundamentals/session.html)
* [Camera](../fundamentals/camera.html)
* [XR Origin](../fundamentals/origin.html)
* [中心模式](../fundamentals/center-mode.html)
* [EasyAR 的头显支持](../../headsets/headsets.html)

---

## 创建图像输入扩展
- 章节路径: `unity/cameras/external-image-stream-frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-image-stream-frame-source.html

# 创建图像输入扩展
## 开始之前
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
* 阅读 [外部帧数据源](external-frame-source.html) 了解创建外部帧数据源所需详细接口说明。
* 阅读 [外部输入帧数据](external-input-frame.html) 了解相机帧数据和渲染帧数据。
## 创建外部帧数据源类
继承 [ExternalImageStreamFrameSource](../../../api/unity/easyar.ExternalImageStreamFrameSource.html) 来创建图像输入扩展。它是 [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html) 的子类，文件名应与类名相同。
例如：
```
public class MyFrameSource : ExternalImageStreamFrameSource
{
}
```
示例 Workflow\_FrameSource\_ExternalImageStream 就是一个基于手机上使用 ARCore 录制的视频作为输入的图像输入扩展实现。该视频是使用 Pixel2 上的 ARCore 通过相机回调方式采集的（不是屏幕录制）。
## 设备定义
重写 [IsCameraUnderControl](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsCameraUnderControl) 并返回 true。
重写 [IsHMD](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsHMD) 来定义设备是否是头显。
例如，使用视频作为输入时设为 false。
```
protected override bool IsHMD => false;
```
重写 [Display](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Display) 来定义设备的显示。
例如，如果只在手机上运行，可以[Display.DefaultSystemDisplay](../../../api/unity/easyar.Display.html#u_easyar_Display_DefaultSystemDisplay)，它的旋转值根据操作系统当前显示状态而自动改变。
```
protected override IDisplay Display => easyar.Display.DefaultSystemDisplay;
```
## 可用性
重写 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 来定义设备是否可用。
例如，使用视频作为输入时始终可用：
```
protected override Optional<bool> IsAvailable => true;
```
如果 [IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable) 在 session 组装时无法判断，可以重写 [CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 协程来阻塞组装过程，直到确定是否可用为止。
## 虚拟摄像机
重写 [Camera](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_Camera) 来提供虚拟摄像机。
例如，有时可用使用 [Camera.main](https://docs.unity3d.com/ScriptReference/Camera-main.html) 作为 session 的虚拟摄像机：
```
protected override Camera Camera => Camera.main;
```
## 物理相机
使用 [FrameSourceCamera](../../../api/unity/easyar.FrameSourceCamera.html) 类型重写 [DeviceCameras](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_DeviceCameras) 以提供设备物理相机信息。这个数据会在输入相机帧数据时使用。[CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 为 true 时必须完成创建。
例如，使用示例 Workflow\_FrameSource\_ExternalImageStream 中所使用的视频：
```
private FrameSourceCamera deviceCamera;
protected override List<FrameSourceCamera> DeviceCameras => new List<FrameSourceCamera> { deviceCamera };
{
var size = new Vector2Int(640, 360);
var cameraType = CameraDeviceType.Back;
var cameraOrientation = 90;
deviceCamera = new FrameSourceCamera(cameraType, cameraOrientation, size, new Vector2(30, 30));
started = true;
}
```
> **小心**
这里的几个输入参数需要根据实际使用的视频来设置。上面代码中的参数只适用于示例中的视频。
重写 [CameraFrameStarted](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CameraFrameStarted) 来提供相机帧开始输入的标识。
例如：
```
protected override bool CameraFrameStarted => started;
```
## session 启动和停止
重写 [OnSessionStart(ARSession)](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStart_easyar_ARSession_) 然后做 AR 独有的初始化工作。需要确保先调用 base.OnSessionStart。
例如：
```
protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
...
}
```
这里是适合打开设备相机的位置，尤其是如果这些相机没有被设计成要一直打开时。同时这里也是适合获取整个生命周期内不会变化的标定数据的位置。有时在这些数据可以被获取前可能需要等待设备准备好或等待数据更新。
同时，这里也是一个适合启动数据输入循环的位置。也可以在 [Update()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Update.html) 或其它方法中写这个循环，尤其是当数据需要在 Unity 执行顺序的某个特殊时间点获取的时候。在 session 准备好（ready）之前不要输入数据。
如果需要，也可以忽略启动过程并在每次更新时做数据检查，这完全取决于具体需求。
例如，使用视频作为输入时可以在这里开始播放视频并启动数据输入循环：
```
protected override void OnSessionStart(ARSession session)
{
base.OnSessionStart(session);
...
player.Play();
StartCoroutine(VideoDataToInputFrames());
}
```
重写 [OnSessionStop()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_OnSessionStop) 并释放资源，需要确保调用 base.OnSessionStop。
例如，使用视频作为输入时可以在这里停止视频播放并释放相关资源：
```
protected override void OnSessionStop()
{
base.OnSessionStop();
StopAllCoroutines();
player.Stop();
if (renderTexture) { Destroy(renderTexture); }
cameraParameters?.Dispose();
cameraParameters = null;
frameIndex = -1;
started = false;
deviceCamera?.Dispose();
deviceCamera = null;
}
```
## 从设备或文件获取相机帧数据
可以从系统相机、USB 相机、视频文件、网络等任意来源获取图像。只要能将数据转换成 [Image](../../../api/unity/easyar.Image.html) 所需的格式即可。从这些设备或文件获取数据的方式各不相同，需要参考相关设备或文件的使用说明。
例如，使用视频作为输入时，可以使用 [Texture2D.ReadPixels(Rect, int, int, bool)](https://docs.unity3d.com/ScriptReference/Texture2D.ReadPixels.html) 从视频播放器的 RenderTexture 中获取相机帧数据，然后复制 [Texture2D.GetRawTextureData()](https://docs.unity3d.com/ScriptReference/Texture2D.GetRawTextureData.html) 的数据到 [Buffer](../../../api/unity/easyar.Buffer.html) 中：
```
void VideoDataToInputFrames()
{
...
RenderTexture.active = renderTexture;
var pixelSize = new Vector2Int((int)player.width, (int)player.height);
var texture = new Texture2D(pixelSize.x, pixelSize.y, TextureFormat.RGB24, false);
texture.ReadPixels(new Rect(0, 0, pixelSize.x, pixelSize.y), 0, 0);
texture.Apply();
RenderTexture.active = null;
...
CopyRawTextureData(buffer, texture.GetRawTextureData<byte>(), pixelSize);
}
static unsafe void CopyRawTextureData(Buffer buffer, Unity.Collections.NativeArray<byte> data, Vector2Int size)
{
int oneLineLength = size.x \* 3;
int totalLength = oneLineLength \* size.y;
var ptr = new IntPtr(data.GetUnsafeReadOnlyPtr());
for (int i = 0; i < size.y; i++)
{
buffer.tryCopyFrom(ptr, oneLineLength \* i, totalLength - oneLineLength \* (i + 1), oneLineLength);
}
}
```
> **小心**
如上面代码中一样，从 [Texture2D](https://docs.unity3d.com/ScriptReference/Texture2D.html) 的指针中复制的数据需要上下反转之后，数据的内存排列才是正常的图像。
在获取图像的同时，还需要获取相机或等效相机的标定数据并创建 [CameraParameters](../../../api/unity/easyar.CameraParameters.html) 实例。
如果数据的原始来源来自手机的相机回调，且数据没有人工裁剪，那么可以直接使用手机相机的标定数据。在使用 ARCore 或 ARKit 等接口获取相机回调数据时，可以参考相关文档获取相机内参。如果需要使用的 AR 功能是图像跟踪或物体跟踪，这种情况也可以使用 [CameraParameters.createWithDefaultIntrinsics(Vec2I, CameraDeviceType, int)](../../../api/unity/easyar.CameraParameters.html#u_easyar_CameraParameters_createWithDefaultIntrinsics_easyar_Vec2I_easyar_CameraDeviceType_System_Int32_) 来创建相机内参，这时算法效果会受到轻微影响，但一般影响不大。
如果数据来自 USB 相机或非相机回调生成的视频文件等其他来源，则需要对相机或视频帧进行标定以获取正确的内参。
> **小心**
相机回调数据不能裁剪，裁剪后需要重新计算内参。如果数据来自屏幕录制等方式获取的图像数据，通常无法使用手机相机的标定数据，这时也需要对相机或视频帧进行标定以获取正确的内参。
内参不正确会导致 AR 功能无法正常使用，常见虚拟内容与现实物体无法对齐，以及 AR 跟踪不容易成功或很容易丢失等。
例如，使用示例 Workflow\_FrameSource\_ExternalImageStream 中所使用的视频，其对应的相机内参及 [CameraParameters](../../../api/unity/easyar.CameraParameters.html) 创建过程如下：
```
var size = new Vector2Int(640, 360);
var cameraType = CameraDeviceType.Back;
var cameraOrientation = 90;
cameraParameters = new CameraParameters(size.ToEasyARVector(), new Vec2F(506.085f, 505.3105f), new Vec2F(318.1032f, 177.6514f), cameraType, cameraOrientation);
```
> **小心**
上面代码中的参数只适用于示例中的视频，该相机内参与视频是在同一时间采集的。如果需要使用其他视频或设备的数据，务必同时获取设备内参或手动进行标定。
## 输入相机帧数据
在获取相机帧数据更新后，调用 [HandleCameraFrameData(double, Image, CameraParameters)](../../../api/unity/easyar.ExternalImageStreamFrameSource.html#u_easyar_ExternalImageStreamFrameSource_HandleCameraFrameData_System_Double_easyar_Image_easyar_CameraParameters_) 来输入相机帧数据。
例如，使用视频作为输入时实现如下：
```
IEnumerator VideoDataToInputFrames()
{
yield return new WaitUntil(() => player.isPrepared);
var pixelSize = new Vector2Int((int)player.width, (int)player.height);
...
yield return new WaitUntil(() => player.isPlaying && player.frame >= 0);
while (true)
{
yield return null;
if (frameIndex == player.frame) { continue; }
frameIndex = player.frame;
...
var pixelFormat = PixelFormat.RGB888;
var bufferO = TryAcquireBuffer(pixelSize.x \* pixelSize.y \* 3);
if (bufferO.OnNone) { continue; }
var buffer = bufferO.Value;
CopyRawTextureData(buffer, texture.GetRawTextureData<byte>(), pixelSize);
using (buffer)
using (var image = Image.create(buffer, pixelFormat, pixelSize.x, pixelSize.y, pixelSize.x, pixelSize.y))
{
HandleCameraFrameData(player.time, image, cameraParameters);
}
}
}
```
> **小心**
不要忘记在使用后执行 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 或通过 `using` 等机制释放 [Image](../../../api/unity/easyar.Image.html) 、[Buffer](../../../api/unity/easyar.Buffer.html) 以及其它相关数据。否则会出现严重内存泄漏，buffer pool 获取 buffer 也可能会失败。
## 相关主题
* [帧数据源和运行时选取过程](frame-source.html)
* [AR Session](../fundamentals/session.html)
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)

---

## 外部帧数据源的输入帧数据要求
- 章节路径: `unity/cameras/external-input-frame.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/external-input-frame.html

# 外部帧数据源的输入帧数据要求
为使外部帧数据源正常工作，最重要的工作同时也是最棘手的部分是确保数据正确性。本文介绍了外部帧数据源的输入帧数据要求。
## 开始之前
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
* 了解 [外部帧数据源](external-frame-source.html) 的基本概念和常见类型。
## 输入帧数据类型
在 Unity 中，外部帧数据源通常需要在两个不同时间接收不同的数据，根据外部数据输入时间和数据特征，我们将这两组数据称为：
1. 相机帧数据（camera frame data）
2. 渲染帧数据（rendering frame data）
不同类型的外部帧数据源对这两组数据的需求不同：
* 图像和设备运动数据输入扩展：同时需要相机帧数据及渲染帧数据
* 图像输入扩展：只需要相机帧数据
## 相机帧数据
数据需求：
1. 时间戳（timestamp）
2. 原始物理相机图像数据（raw camera image data）
3. 内参（intrinsics，包括图像大小、焦距、主点。如果有畸变还需要畸变模型和畸变参数）
4. 外参（extrinsics，Tcw 或 Twc，标定的矩阵，表达物理相机相对设备/头的 pose 原点的物理偏移）
5. 跟踪状态（tracking status）
6. 设备位姿（device pose）
1. 时间戳（timestamp）
2. 原始物理相机图像数据（raw camera image data）
3. 内参（intrinsics，包括图像大小、焦距、主点。如果有畸变还需要畸变模型和畸变参数）
数据时间：
* 物理相机曝光中点
数据使用：
* API 调用时间：可根据外部代码的设计改变。一个大多数设备使用的常规方法是在 3D 引擎的渲染更新中查询，然后根据设备数据的时间戳来判断是否进一步进行数据处理
* API 调用线程：3D 引擎的 game thread 或任何其它线程（如果使用到的所有外部 API 都是线程安全的）
Unity 中 API 调用示例如下：
```
void TryInputCameraFrameData()
{
double timestamp;
if (timestamp == curTimestamp) { return; }
curTimestamp = timestamp;
PixelFormat format;
Vector2Int size;
Vector2Int pixelSize;
int bufferSize;
var bufferO = TryAcquireBuffer(bufferSize);
if (bufferO.OnNone) { return; }
var buffer = bufferO.Value;
IntPtr imageData;
buffer.tryCopyFrom(imageData, 0, 0, bufferSize);
var historicalHeadPose = new Pose();
MotionTrackingStatus trackingStatus = (MotionTrackingStatus)(-1);
using (buffer)
using (var image = Image.create(buffer, format, size.x, size.y, pixelSize.x, pixelSize.y))
{
HandleCameraFrameData(deviceCamera, timestamp, image, cameraParameters, historicalHeadPose, trackingStatus);
}
}
```
```
void TryInputCameraFrameData()
{
double timestamp;
if (timestamp == curTimestamp) { return; }
curTimestamp = timestamp;
PixelFormat format;
Vector2Int size;
Vector2Int pixelSize;
int bufferSize;
var bufferO = TryAcquireBuffer(bufferSize);
if (bufferO.OnNone) { return; }
var buffer = bufferO.Value;
IntPtr imageData;
buffer.tryCopyFrom(imageData, 0, 0, bufferSize);
var historicalHeadPose = new Pose();
MotionTrackingStatus trackingStatus = (MotionTrackingStatus)(-1);
using (buffer)
using (var image = Image.create(buffer, format, size.x, size.y, pixelSize.x, pixelSize.y))
{
HandleCameraFrameData(timestamp, image, cameraParameters);
}
}
```
## 渲染帧数据
数据需求：
1. 时间戳（timestamp）
2. 跟踪状态（tracking status）
3. 设备位姿（device pose）
无。
数据时间：
* 上屏时刻。TimeWarp 不计算在内。相同时刻的 device pose 数据会由外部（比如设备 SDK）用来设置虚拟摄像机的 transform 以渲染当前帧。
> **注意**
TimeWarp（有时也称为 Reprojection 或 ATW/PTW）是 VR/AR 头显中常用的一种降低延迟的技术。它会在渲染完成后，根据最新的头部位姿对图像进行再次扭曲变换，以补偿渲染期间产生的头部运动。EasyAR 需要的是渲染开始时用于设置虚拟摄像机的位姿对应的时刻，而不是 TimeWarp 后实际上屏的时刻。
数据使用：
* API 调用时间：3D 引擎的每个渲染帧
* API 调用线程：3D 引擎的 game thread
Unity 中 API 调用示例如下：
```
private void InputRenderFrameMotionData()
{
double timestamp = 0e-9;
var headPose = new Pose();
MotionTrackingStatus trackingStatus = (MotionTrackingStatus)(-1);
HandleRenderFrameData(timestamp, headPose, trackingStatus);
}
```
## 数据要求细节
物理相机图像数据：
* 图像坐标系：在传感器水平时获取的数据也应是水平的。数据应该以左上角为原点，行优先存储。图像不应翻转或颠倒。
* 图像 FPS：正常 30 或 60 fps 的数据都可以。如果高 fps 有特殊影响，为达到合理的算法效果，最小可接受帧率为 2。建议使用高于 2 的 fps，通常情况下使用原始数据帧率即可。
* 图像尺寸：为获取更好的计算结果，最大边应为 960 或更大。正常不鼓励在数据链路中进行耗时的图像缩放，建议直接使用原始数据，除非完整大小的数据拷贝时间已经长得无法接受。图像分辨率不能小于 640\*480。
* 像素格式：优先跟踪效果并综合考虑性能，通常格式优先顺序为 YUV > RGB > RGBA > Gray （YUV中的Y分量）。在使用 YUV 数据时，需要完整的数据定义，包括数据封装和填充细节。相较单通道图像而言，使用彩色图像 Mega 的效果会更好，但其它功能影响不大。
* 数据访问：数据指针或等价实现。最好在数据链路中消除所有可能的非必须拷贝。HandleRenderFrameData 中 EasyAR 复制一份数据，之后异步使用，该同步调用完成后就不再使用图像数据。注意数据所有权。
时间戳：
* 所有时间戳都应时钟同步，最好是硬件同步。数据单位是秒，但精度要求达到纳秒或尽可能高。
跟踪状态：
* 跟踪状态由设备定义，需要包含跟踪丢失（VIO不可用）的状态。如有更多等级则更好。
设备位姿：
* 所有 pose（包括 3D 引擎中虚拟摄像机的 transform）都应使用同一个原点。
* 所有 pose 以及外参应该使用相同的坐标轴系统。
* 在 Unity 中，pose 数据的坐标轴系统类型应为 Unity 坐标轴系统或 EasyAR 坐标轴系统。如果输入扩展由 EasyAR 实现且使用了其它坐标轴系统定义方式，应提供清晰的坐标轴系统定义或给出转换到 Unity 坐标轴系统或 EasyAR 坐标轴系统的方法。
* 在 Unity 中，如果使用 Unity XR 框架，只需要兼容 [XROrigin.TrackingOriginMode.Device](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.TrackingOriginMode.html#Unity_XR_CoreUtils_XROrigin_TrackingOriginMode_Device) 模式即可。
内参：
* 所有数值都应与图像数据匹配。如有需要应在输入 EasyAR 之前对内参进行缩放。
* 如果输入扩展由 EasyAR 实现，应说明内参是否会在每一帧变化（区别是对应 API 应该调用一次还是每帧调用）。
外参：
* 在头显上必须提供真实数据。
* 它是一个标定矩阵，表达物理相机相对设备/头的 pose 原点的物理偏移。如果设备的 pose 和物理相机 pose 相等，它应该是单位阵。
* Apple Vision Pro 对应接口为： [CameraFrame.Sample.Parameters.extrinsics](https://developer.apple.com/documentation/arkit/cameraframe/sample/parameters/4443449-extrinsics)，需要注意其数据定义与接口所需数据有区别，EasyAR 内部是进行转换之后再使用的。
* 在 Unity 中，外参的坐标轴系统类型应为 Unity 坐标轴系统或 EasyAR 坐标轴系统。如果输入扩展由 EasyAR 实现且使用了其它坐标轴系统定义方式，应提供清晰的坐标轴系统定义或给出转换到 Unity 坐标轴系统或 EasyAR 标轴系统的方法。
* 在头显设备中，通常存在多个不同定义的坐标系，这个不同可能包括坐标轴原点、朝向、左右手表达等。外参应在同一坐标系下计算，该接口数据需要同一坐标系下的坐标变换，而非两个不同定义的坐标系的变换矩阵。
性能：
* 数据应以最优效率提供。在大多数实现中，API 调用会发生在渲染过程，所以建议即使在底层需要进行耗时操作的情况下，也不要阻塞 API 调用，或者以合理的方式来使用这些 API。
* 如果输入扩展由 EasyAR 实现，需要对所有耗时 API 调用进行说明。
多相机：
* 至少一个相机的数据是需要的。这个相机可以是 RGB 相机、VST 相机、定位相机等中的任意一个。在头显上如果只输入一个相机的数据，通常推荐使用在中央或在眼睛附近的 RGB 相机或 VST 相机。
* 使用多相机可提升 EasyAR 算法效果。所有可用相机某一时刻的相机帧数据应在在同一个时间点同时输入。
>
> 多相机目前尚未完全支持，可以联系 EasyAR 获取更多细节。
>
## 后续步骤
* 创建 [图像和设备运动数据输入扩展](external-device-frame-source.html)
* 创建 [图像输入扩展](external-image-stream-frame-source.html)
* 创建 [头显扩展包](../headsets/extension.html)
## 相关主题
* [EasyAR 坐标系](../../native/fundamentals/coordinates.html)
* 图像输入扩展示例 Workflow\_FrameSource\_ExternalImageStream

---

## 内置 Frame Source 组件
- 章节路径: `unity/cameras/frame-source-builtin.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source-builtin.html

# 内置 Frame Source 组件
探索内置 Frame Source 组件窗口中的各项属性以自定义相机参数。
|接口|组件参考|
|[CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|[CameraDeviceFrameSource 组件参考](comp-CameraDeviceFrameSource.html)|
|[EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|[CameraDeviceFrameSource 组件参考](comp-CameraDeviceFrameSource.html)|
|[FramePlayer](../../../api/unity/easyar.FramePlayer.html)|[FramePlayer 组件参考](../simulation/comp-FramePlayer.html)|
|[ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)|[ThreeDofCameraDeviceFrameSource 组件参考](comp-ThreeDofCameraDeviceFrameSource.html)|
|[InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)|[InertialCameraDeviceFrameSource 组件参考](comp-InertialCameraDeviceFrameSource.html)|
|[MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)|[MotionTrackerFrameSource 组件参考](../motion-tracking/comp-MotionTrackerFrameSource.html)|
|[ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)|[ARCoreFrameSource 组件参考](../motion-tracking/comp-ARCoreFrameSource.html)|
|[ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)|[ARKitFrameSource 组件参考](../motion-tracking/comp-ARKitFrameSource.html)|
|[AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)|[AREngineFrameSource 组件参考](../motion-tracking/comp-AREngineFrameSource.html)|
|[VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)||
|[XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)||
|[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)||
|[ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)||

---

## 添加一组帧数据源
- 章节路径: `unity/cameras/frame-source-group.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source-group.html

# 添加一组帧数据源
一个 AR Session 可以包含多个帧数据源组件，称为帧数据源组（frame source group）。在运行时，session 会根据当前设备和启用的 AR 功能，从帧数据源组中选取一个最合适的帧数据源进行使用。本文介绍了如何使用和管理帧数据源组。
## 开始之前
* 了解 [帧数据源](frame-source.html) 的基本概念、类型以及运行时的选取方法。
## 使用预设 AR Session 的帧数据源组
[使用默认配置创建的 session](../fundamentals/session-creation.html) 会自带一组帧数据源，在使用单一 AR 功能时，一般就足够了。
不同预设 session 中所包含的帧数据源不同。
>
> 使用
[> ARSessionFactory.ARSessionPreset.ImageTracking
](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTracking)> 预设或
`> AR Session (Image Tracking Preset)
`> 菜单创建的 session 中只有单个帧数据源：
>
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-image-tracking.png)
>
> 使用
[> ARSessionFactory.ARSessionPreset.MegaBlock_MotionTracking_Inertial
](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)> 预设或
`> AR Session (Mega Block Default Preset)
`> 菜单创建的 session 中包含多个帧数据源组件的场景层级结构：
>
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-mega.png)
>
如果场景中一开始使用了某个预设创建了 session，在迭代过程中增加其它功能时，不仅需要添加相应的 frame filter 组件，还需要根据需要添加合适的帧数据源组件。
> **重要事项**
从 4.7 或更低版本升级后，需要整个删除 session 后重新通过菜单或 [ARSessionFactory](../../../api/unity/easyar.ARSessionFactory.html) 创建 session，才能使用预设的帧数据源组。
以下列出了所有预设的 AR 功能默认配置的帧数据源组件，注意列表中的排序与场景中帧数据源的组件排序相同：
|预设|帧数据源组|
|
* [ImageTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTracking)
* [CloudRecognition](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_CloudRecognition)
* [ObjectTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ObjectTracking)
* [SurfaceTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SurfaceTracking)|
1. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
|
* [MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MotionTracking)
* [SparseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapBuilder)
* [SparseSpatialMapTracker](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapTracker)
* [DenseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_DenseSpatialMapBuilder)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)|
|
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* [MegaLandmark\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)
* [MegaLandmark\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* [MegaLandmark\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial_3DOF)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
11. [EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|
|
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* [MegaLandmark\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaLandmark_MotionTracking_Inertial_3DOF_0DOF)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)
10. [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)
11. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
|
* [ImageTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTrackingMotionFusion)
* [ObjectTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ObjectTrackingMotionFusion)|
1. [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)
2. [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)
3. [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)
4. [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)
5. [ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)
6. [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)
7. [VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)
8. [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)
9. [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|
> **注意**
使用预设创建的组件排序可以保证在所有受内置帧数据源支持的设备上使用最优的帧数据源。
## 使用默认帧数据源配置
在使用默认参数时，帧数据源的配置会根据设备和运行时启用的 AR 功能自动调整。
如果手动修改过帧数据源的参数，在 session 中的 AR 功能发生变化时（比如在原本只包含图像跟踪的 session 中新增了运动跟踪功能），可能需要手动调整帧数据源的参数以适应新的功能需求，这样所有 AR 功能才能以最佳效果运行。
> **重要事项**
从 4.7 或更低版本升级后，需要整个删除 session 后重新通过菜单或 [ARSessionFactory](../../../api/unity/easyar.ARSessionFactory.html) 创建 session，才能使用正确的默认参数。
## 添加帧数据源组
在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `Frame Source : \*` 可以添加适合该功能的 frame source 组件。也可以通过菜单 `EasyAR Sense` > `Frame Source by Transform Type` > `\* Dof` > `Frame Source : \*` 添加需要的 frame source 组件。
在脚本中，可以使用 [ARSessionFactory.AddFrameSource<Source>(GameObject, bool)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameSource__1_UnityEngine_GameObject_System_Boolean_) 来添加 frame source 组件。
比如，通过菜单 `EasyAR Sense` > `Frame Source by Transform Type` > `3 Dof Rot-Only` > `Frame Source : Three Dof Camera Device` 可以给当前选中的 session 添加一个 [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-add.png)
对应的脚本代码如下：
```
ARSessionFactory.AddFrameSource<ThreeDofCameraDeviceFrameSource>(session);
```
## 帧数据源排序
session 组装过程中，帧数据源组中最终只有一个帧数据源会被选中后组装到 session 中，选取的规则取决于 [AssembleOptions.FrameSourceSelection](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html) 属性的值。在默认配置下，可以通过调整帧数据源组中各个组件的排序来影响最终被选中的帧数据源。
一般可以使用在 `Hierarchy` 视图中 [对场景中的物体进行排序](https://docs.unity3d.com/Manual/Hierarchy.html) 的方法直接移动 frame source 物体进行排序。
在脚本中，可以使用 [Transform.SetSiblingIndex(int)](https://docs.unity3d.com/ScriptReference/Transform.SetSiblingIndex.html) 来调整物体的排序。
比如，要将 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 排在其它帧数据源前面，可以在 `Hierarchy` 视图中选中 `Motion Tracker` 物体并拖动到最上面的位置。
相同的效果也可以通过下面的脚本代码实现：
```
motionTrackerFrameSource.transform.SetSiblingIndex(0);
```
另外还有一些预定义的排序方法可以使用。在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Utility` > `Sort Frame Source : \* > \*` 对特定的若干帧数据源组件进行排序。
在脚本中，可以使用 [ARSessionFactory.SortFrameSource(GameObject, ARSessionFactory.FrameSourceSortMethod)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_SortFrameSource_UnityEngine_GameObject_easyar_ARSessionFactory_FrameSourceSortMethod_) 实现相同的效果。
比如，通过菜单 `EasyAR Sense` > `Utility` > `Sort Frame Source : Motion Tracker > System SLAM` 可以将 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 排在 [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)、[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)、[ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)、[ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)和 [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html) 前面。
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-sort.png)
对应的脚本代码如下：
```
ARSessionFactory.SortFrameSource(session, new ARSessionFactory.FrameSourceSortMethod { MotionTracker = ARSessionFactory.FrameSourceSortMethod.MotionTrackerSortMethod.PreferEasyAR });
```
经过上面的排序之后，场景层级结构变为：
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-sorted.png)
## 相关主题
* 了解如何 [添加和配置头显用的帧数据源](../headsets/enable-headset.html)
* 尝试在运行时 [获取正在使用的帧数据源](../fundamentals/session-components.html)

---

## Unity 中的摄像头及输入帧数据来源 —— 帧数据源（Frame Source）
- 章节路径: `unity/cameras/frame-source.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/frame-source.html

# Unity 中的摄像头及输入帧数据来源 —— 帧数据源（Frame Source）
帧数据源是 Unity 中摄像头及输入帧数据的提供者。本文介绍了帧数据源的基本概念、类型以及运行时的选取方法。
## 开始之前
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程。
* 了解 [摄像头、输入帧](../../cameras/cameras.html) 等基本概念。
## 帧数据源是什么
帧数据源（[FrameSource](../../../api/unity/easyar.FrameSource.html)）是输入帧（[InputFrame](../../../api/unity/easyar.InputFrame.html)）的提供者，抽象了摄像头以及其它提供输入帧数据的设备和功能。
下图展示了帧数据源在 session 中的位置：
```
flowchart LR
F[Frame Source]
A((Input Frame))
B[Session]
C([Camera])
O([Origin])
T([Target])
F --> A
A --> B
B -. transform .-> C
B -. transform .-> O
B -. transform .-> T
style F fill:#6e6ce6,stroke:#333,color:#fff
```
帧数据源可能只是提供数据给下游 AR 功能使用，也可能它自身就实现了一些 AR 功能，比如运动跟踪。部分帧数据源会提供摄像头设备的控制接口，允许用户选择摄像头参数，比如分辨率、对焦模式等。
## 帧数据源的类型
以提供帧数据源的 Unity 包区分，帧数据源可以分为两大类：
* 内置帧数据源：由 EasyAR Sense Unity 插件包提供的帧数据源，通常支持大部分常见的使用场景和部分头显。
* 外部帧数据源：由 EasyAR Sense Unity 插件扩展包提供的帧数据源，通常用于支持特定的头显设备。很多时候，外部帧数据源是由头显厂商或第三方开发者提供的。
区分于外部帧数据源，[自定义相机](../../cameras/custom-camera.html) 并不一定是外部提供的，内置帧数据源中也有部分是自定义相机。
帧数据源可以提供不同自由度的运动数据：0DoF、3DoF、5DoF 和 6DoF，同一个帧数据源有可能在不同工作状态下提供不同自由度的运动数据。
下面的表格列出了由 EasyAR 提供的帧数据源：
|名称|内置|自定义相机|运动数据|说明|
|[CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html)|是|否|无（0DoF）|普通摄像头，支持前后摄和 PC|
|[EditorCameraDeviceFrameSource](../../../api/unity/easyar.EditorCameraDeviceFrameSource.html)|是|否|无（0DoF）|普通摄像头，仅支持在编辑器下调试使用|
|[FramePlayer](../../../api/unity/easyar.FramePlayer.html)|是|否|播放文件决定|回放 EIF 文件，实现模拟运行|
|[ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html)|是|否|3DoF|提供 3DoF 跟踪能力|
|[InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)|是|否|5DoF|提供惯性导航能力|
|[MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)|是|否|6DoF|提供 EasyAR 实现的运动跟踪|
|[ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html)|是|否|6DoF|提供 ARCore 的运动跟踪|
|[ARKitFrameSource](../../../api/unity/easyar.ARKitFrameSource.html)|是|否|6DoF|提供 ARKit 的运动跟踪|
|[AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)|是|是|6DoF|提供 AR Engine 的运动跟踪|
|[VisionOSARKitFrameSource](../../../api/unity/easyar.VisionOSARKitFrameSource.html)|是|是|6DoF|提供 VisionOS ARKit 的运动跟踪 [1](#fn:1)|
|[XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html)|是|是|6DoF|提供 XREAL 设备的运动跟踪 [1](#fn:1)|
|[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html)|是|是|6DoF|提供 ARFoundation 对应 ARCore 的运动跟踪|
|[ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)|是|是|6DoF|提供 ARFoundation 对应 ARKit 的运动跟踪|
|[PicoFrameSource](../../../api/unity/easyar.PicoFrameSource.html)|否|是|6DoF|提供 Pico 设备的运动跟踪 [1](#fn:1)|
|[RokidFrameSource](../../../api/unity/easyar.RokidFrameSource.html)|否|是|6DoF|提供 Rokid 设备的运动跟踪 [1](#fn:1)|
## 运行时帧数据源选取
session 的场景层级结构中包含了一个或多个帧数据源组件。在 session 运行时，并非所有的帧数据源组件都会被使用。
下面的截图展示了一个只有单个帧数据源组件的场景层级结构：
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-image-tracking.png)
下面的截图展示了一个包含多个帧数据源组件的场景层级结构：
![alt text](https://doc-asset.easyar.com/develop/unity/cameras/media/frame-sources-mega.png)
每个帧数据源的功能不同，这也同时决定了它们适用的使用场景和设备。在 session 组装时，会从这些组件中选取一个且只有一个作为 session 的帧数据源。
[AssembleOptions.FrameSourceSelection](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html) 属性定义了 session 运行时帧数据源的选取方法：
|名称|方法|
|[Auto](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_Auto)（默认）|自动选择，按 transform 顺序选择第一个可用且 active 的子节点。|
|[Manual](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_Manual)|手动指定。只能指定 session 子节点。|
|[FramePlayer](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_FramePlayer)|使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html)。|
> **提示**
Unity 物体的 transform 顺序可以使用 [Transform.GetSiblingIndex()](https://docs.unity3d.com/ScriptReference/Transform.GetSiblingIndex.html) 判断，也可以从 Hierarchy 视图中物体的排序判断，但是需要关闭以下选项（默认是关闭状态）： Edit > Preferences > General > Enable Alphanumeric Sorting。
session 组装过程中，帧数据源在经历如下步骤后被选定：
1. session 遍历其子节点，按 transform 顺序收集所有 active 的帧数据源组件。
2. 根据 [AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 中的选源策略（[AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource)）筛选候选列表：
* **Auto**（默认）：保留所有候选。
* **Manual**：仅保留手动指定的帧数据源。
* **FramePlayer**：更换候选列表为 [FramePlayer](../../../api/unity/easyar.FramePlayer.html)。
* 再次筛选候选列表，移除以下组件：
* 被组件自身禁用的组件。
* 关闭了自定义相机（[AssembleOptions.EnableCustomCamera](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_EnableCustomCamera) 为 false）时的所有自定义相机组件。
* （Android 平台）如果 [AssembleOptions.DeviceList](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_DeviceList) 的超时设置大于 0，且候选列表中包含 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html)、[ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html) 或 [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html)，会尝试下载对应的最新的设备支持列表。下载更新后，这些帧数据源的可用性可能会发生变化。下载完成或超时后，继续后续步骤。
* 按列表顺序依次检查剩余候选组件的可用性（调用 [FrameSource.CheckAvailability()](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_CheckAvailability) 并访问 [FrameSource.IsAvailable](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsAvailable)）。
* 选取**第一个**检查结果为可用的帧数据源。
其中，组件自身的禁用条件由组件内部定义，常见有这些情况：
* 在不支持的系统中运行，比如非 Android 系统下 [AREngineFrameSource](../../../api/unity/easyar.AREngineFrameSource.html) 会被禁用。
* 必要的第三方 SDK 未安装，比如 XREAL SDK 未安装时 [XREALFrameSource](../../../api/unity/easyar.XREALFrameSource.html) 会被禁用。
* 配置的条件未满足，比如设备的 [MotionTrackerCameraDeviceQualityLevel](../../../api/unity/easyar.MotionTrackerCameraDeviceQualityLevel.html) 低于 [MotionTrackerFrameSource.DeviceQualityLevel](../../../api/unity/easyar.MotionTrackerFrameSource.html#u_easyar_MotionTrackerFrameSource_DeviceQualityLevel) 时 [MotionTrackerFrameSource](../../../api/unity/easyar.MotionTrackerFrameSource.html) 会被禁用。
如果最终没有任何一个帧数据源被选定，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，且 session 报告中 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 字段数值是 [NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource)。
> **注意**
设备列表完成更新后，如果设备列表发生变化，帧数据源的可用性可能也会发生改变，可以参考 [设备支持和 session 报告](../fundamentals/session-report.html) 了解这时 session 的行为。
## 后续步骤
* 尝试在场景中 [添加一组帧数据源](frame-source-group.html)
## 相关主题
* [设备支持和 session 报告](../fundamentals/session-report.html)
* [EasyAR 的头显支持](../../headsets/headsets.html)
* 创建 [外部帧数据源](external-frame-source.html) 以使用 [自定义相机](../../cameras/custom-camera.html)
1. 设备支持情况可以参考 [EasyAR 的头显支持](../../headsets/headsets.html) 。[↩](#fnref:1)[↩](#fnref:2)[↩](#fnref:3)[↩](#fnref:4)

---

## Workflow\_FrameSource\_CameraDevice 示例详解
- 章节路径: `unity/cameras/sample-camera-device.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/cameras/sample-camera-device.html

# Workflow\_FrameSource\_CameraDevice 示例详解
`Workflow\_FrameSource\_CameraDevice` 是一个专注于 **帧输入源（Frame Source）底层控制** 的示例场景，展示了如何使用 `CameraDeviceFrameSource` 获取摄像头的原始图像流，并进行一些基础控制。
## 使用方法
### 1. 打开场景
在 Unity 编辑器中，打开 `Workflow\_FrameSource\_CameraDevice` 场景，位于 `Assets/` 目录中。
### 2. 构建运行
* 在编辑器中点击 **Play** 可查看 PC 上的效果画面（部分功能受限）。
* **必须构建到真机** 才能完整体验摄像头的基础控制能力。
应用启动后，将自动打开后置摄像头。
## 预期效果
当摄像头对准周围环境时：
1. 屏幕中会显示实时摄像头画面。
2. 此时会渲染一个 3D 动态熊猫模型。
3. UI 显示当前摄像头状态（如分辨率、FPS）。
4. 点击 `Loop Size` 按钮可以切换当前摄像头支持的输出帧分辨率。
5. 点击 `Flash Torch` 按钮可以 **关闭/打开** 闪光灯。
6. 点击 `HorizontalFlip` 可以切换当前画面的 **镜像显示**。
7. 点击 `CaptureIamge` 可以切换是否让模型捕获当前环境画面作为自身的贴图。
8. 点击 `CameraImage` 可以切换是否显示当前摄像头画面。
9. 点击 `Camera` 可以 **关闭/打开** 当前摄像头，关闭后画面将保持关闭前的状态不变。
10. 通过 `NextCamera` 按钮动态切换 **前置/后置摄像头**。
> **提示**
更多 FrameSource 详情，请参阅：
* [内置Frame Source参考](frame-source-builtin.html)
* [自定义相机和外部帧输入](external-frame-source.html)
通过 `Workflow\_FrameSource\_CameraDevice`，您可深入掌握 EasyAR 对底层摄像头资源的控制能力，为构建高性能、高定制化的 AR 应用奠定坚实基础。

---

## Diagnostics Controller 组件参考
- 章节路径: `unity/diagnostics/comp-DiagnosticsController.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/comp-DiagnosticsController.html

# Diagnostics Controller 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.DiagnosticsController.html)
>
探索 DiagnosticsController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/diagnostics/media/comp-DiagnosticsController.png)
默认条件下组件截图。
DiagnosticsController 组件窗口由三个部分组成：组件配置、Assembly 预览和 session 验证工具。
## 组件配置
|属性|描述|
|**Developer Mode Switch**|开发者模式开关。可以使用默认的开关（点击屏幕 8 次触发）或自定义一个开关，或提供开发者模式的等价替代。|
|**Message Output**|消息输出选项。|
|*Session Dump*|会话状态转储输出方式。选项：
* UI：显示在UI并每帧更新。在头戴设备上，显示在眼前5米处。
* Log：输出到系统日志，由于每帧都输出，对运行性能是有影响的，建议在开发或测试时使用。
* None：不输出。|
|*Sense Error*|Sense Error 输出方式，通常与 EasyAR Sense license 有关。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Session Error*|Session Error 输出方式，通常与设备不支持一些功能或错误的配置有关。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Error*|Error 输出方式。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Warning*|Warning 输出方式。选项：
* UIAndLog：输出到 UI 和日志。在头戴设备上显示在眼前 5 米处。
* Log：输出到系统日志。|
|*Show Editor Dialog On Fatal*|编辑器中，Sense Error 或 Session Error 时显示对话框。|
## Assembly 预览
Assembly 预览只在编辑模式可见。根据 [AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 显示当前 session 在组装时会选择的组件，这个是一个参考，与 session 运行时最终组装的组件可能不同。
## session 验证工具
[session 验证工具](../simulation/tool.html)用于帮助开发者在 Unity 编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。

---

## 开发者模式
- 章节路径: `unity/diagnostics/developer-mode.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/developer-mode.html

# 开发者模式
开发者模式用于设定是否启用运行时诊断面板。诊断面板可用于切换调试信息是否显示以及录制 EIF、EED 文件。
![diagnostics developer mode 1](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode.png)
## 开发者模式诊断面板
开发者模式诊断面板默认通过快速点击屏幕 8 次打开（可通过修改 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 来更改）。打开后会在屏幕右侧显示诊断面板。
![diagnostics developer mode 2](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode-panel.png)
诊断面板功能如下：
* session: session 信息控制，该信息用于了解 session 的运行状态和问题
* Toggle: 切换 [SessionDump](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionDump) 消息显示
* copy: 复制当前帧 session dump 信息
* eif: eif 录制控制，eif 文件用于 [Unity AR 模拟运行](../simulation/simulation.html)
* Auto/Obsolete: 切换 eif 格式，其中 Obsolete 表示使用原始 EIF 格式，Auto 表示根据平台支持情况自动选择 EIF MKV 格式或者原始 EIF 格式
* rec: 启动/停止 eif 录制
* eed: eed 录制控制，eed 文件用于抓取一些运行时的关键数据提供给 EasyAR 技术支持进行问题分析
* rec: 启动/停止 eed 录制
## 修改开发者模式开关
可以通过 session 上的 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 组件在编辑器中配置，或是使用 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 接口在脚本中配置。
可以选择的模式如下：
* [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default)：手机上快速点击屏幕8次进入开发者模式并会在屏幕右边打开诊断面板。
* [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom)：可以通过 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 接口来自定义开启开发者模式切换条件，未定义时诊断面板将无法在运行时打开。
可以通过设置 [DiagnosticsController.DeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_DeveloperModeSwitch) 为 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom) 并且不修改 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 来禁止开启开发者模式。
比如，下面的代码展示了如何在脚本中禁止开启开发者模式：
```
Session.Diagnostics.DeveloperModeSwitch = DiagnosticsController.DeveloperModeSwitchType.Custom;
```
> **提示**
* 建议在开发和测试阶段使用默认配置 [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default)。
* 建议在发布上线阶段使用配置 [Default](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Default) 或 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom)。
* 建议在使用 [Custom](../../../api/unity/easyar.DiagnosticsController.DeveloperModeSwitchType.html#u_easyar_DiagnosticsController_DeveloperModeSwitchType_Custom) 模式时，修改 [CustomDeveloperModeSwitch](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_CustomDeveloperModeSwitch) 以提供其它方式启用诊断面板，或提供其他自定义的方式收集运行时数据。
## 相关主题
* [录制 EED dump 文件](event-dump.html)
* [UI 消息](ui-messages.html)
* [Unity AR 模拟运行](../simulation/simulation.html)

---

## Unity 开发中的问题诊断和报告
- 章节路径: `unity/diagnostics/diagnostics.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/diagnostics.html

# Unity 开发中的问题诊断和报告
在开发基于 Unity 的插件或应用时，难免会遇到运行异常或逻辑错误。为了帮助开发者快速定位和解决问题，Unity Plugin 提供了一系列内置的诊断与调试工具。本章将介绍这些常用的调试手段和辅助功能，涵盖从实时日志查看、开发者模式启用，到问题数据采集与上报的完整流程。
* [UI 消息](ui-messages.html)
介绍运行时系统如何通过 UI 层面展示错误、警告和其他诊断信息，并说明这些消息的分类标准与含义，便于快速识别问题类型。
* [开发者模式](developer-mode.html)
说明如何在应用运行期间激活开发者模式，以及该模式下可使用的高级调试功能：可视化调试图层、EIF/EED 文件录制。
* [录制 EED dump 文件](event-dump.html)
详细讲解如何触发并录制 EED 文件，该文件包含关键事件、传感器数据、系统状态等上下文信息；同时说明如何从设备中导出和使用这些 dump 文件进行离线分析。
* [问题报告](report.html)
指导用户如何规范地提交问题反馈，包括应附带的日志、dump 文件、复现步骤等，以提高问题处理效率。
相关功能组件包括：
* [DiagnosticsController 组件](comp-DiagnosticsController.html)
该组件是诊断系统的核心控制器，负责协调日志记录、状态监控、dump 生成等功能。

---

## 录制 EED dump 文件
- 章节路径: `unity/diagnostics/event-dump.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/event-dump.html

# 录制 EED dump 文件
EED（EasyAR Event Dump）文件可用于抓取一些运行时的关键数据提供给 EasyAR 技术支持进行问题分析，例如一些跟踪器的跟踪结果、程序与 Mega 服务之间的网络请求等。通常在使用 [EIF 文件](../../simulation/simulation.html) 无法重现问题的时候使用。
## 使用开发者模式面板录制
运行程序，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。
![diagnostics eed windows](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-windows.png)
录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed windows 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-windows-2.png)
打开应用，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed android](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-android.png)
默认的 EED 文件路径位于 `/sdcard/Android/data` 中，在 Android 11 或更高版本的设备上，将无法通过文件管理器或 `adb pull` 来获得。建议使用 [Shizuku](https://shizuku.rikka.app/) 和 [MiXplorer](https://mixplorer.com/) 来获取文件。需要先在 WLAN 环境使用 Shizuku 与手机的无线调试配对并启动，然后在 Shizuku 中对 MiXplorer 授权，即可使用 MiXplorer 管理 `/sdcard/Android/data` 文件夹。
![diagnostics eed android 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-android-2.png)
打开应用，然后打开 [开发者模式诊断面板](developer-mode.html)（默认配置下快速点击屏幕8次），点击 `eed` 的 `rec`，即可录制。进行问题复现，然后点击 `stop` 即可完成录制。录制得到的 EED 文件路径会在录制时显示。
![diagnostics eed ios](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios.png)
使用示例时，可以将 iOS 设备连接到 Mac 设备，然后从 Mac 设备的 Finder 中找到 iOS 设备示例应用中录制完成的 EED 文件。
![diagnostics eed ios 2](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios-2.png)
如果无法在 Finder 中找到文件，可以在 Xcode 主菜单的 `Window -> Devices and Simulators` 中，选中应用，点击 `…`，选择 `Download Container…`，也可以获得 EED 文件。
![diagnostics eed ios 3](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-eed-ios-3.png)
## 使用脚本录制
可以使用 [EventDumpRecorder.start(string, int)](../../../api/unity/easyar.EventDumpRecorder.html#u_easyar_EventDumpRecorder_start_System_String_System_Int32_) 开始录制 EED 文件，使用 [EventDumpRecorder.stop()](../../../api/unity/easyar.EventDumpRecorder.html#u_easyar_EventDumpRecorder_stop) 停止录制。
比如，下面的代码展示了如何在脚本中录制 EED 文件：
```
EventDumpRecorder eedRecorder;
bool RecordEED(bool on)
{
if (on)
{
if (session.Assembly == null || session.Assembly.Display == null) { return false; }
var path = Path.Combine(Application.persistentDataPath, DateTime.Now.ToString("yyyy-MM-dd\_HH-mm-ss.fff") + ".eed");
eedRecorder = EventDumpRecorder.create();
eedRecorder?.start(path, session.Assembly.Display.Rotation);
}
else
{
eedRecorder?.stop();
eedRecorder?.Dispose();
eedRecorder = null;
}
return true;
}
```
## 相关主题
* [开发者模式](developer-mode.html)

---

## 问题报告
- 章节路径: `unity/diagnostics/report.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/report.html

# 问题报告
> **注意**
EasyAR Mega 用户请务必阅读 [Mega 常见问题](../../mega/faq.html) 和 [问题报告与反馈](../../mega/report.html) 。
> **注意**
在反馈问题之前，请务必使用最新版本的 SDK 并在 sample 中复现问题，很多问题可能会在新版本中得到修复，EasyAR 主要支持在最新版本上能够复现的问题。此外，Unity 本身也会存在一些问题，一些 Unity 的问题可以通过尝试删除 Unity Library 文件夹、Unity 生成的 XCode 工程来解决。
请使用插件内置的 `提问` 功能来辅助检查和收集反馈信息。
![diagnostics report ask dialog options](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
这个窗口可以从 `EasyAR > Sense > 提问` 菜单打开
![diagnostics report ask menu](https://doc-asset.easyar.com/develop/mega/media/unity-question.png)
打开后信息是不全的，需要选择使用的环境和功能
![diagnostics report ask dialog](https://doc-asset.easyar.com/mega/troubleshooting/media/localization_failure6.png)
如需反馈手机或头显上的问题，请复制Session Dump信息日志
![diagnostics report ask dialog session dump setting](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-report-3.png)
然后填写到文本框中
![diagnostics report ask dialog session dump filling](https://doc-asset.easyar.com/develop/unity/diagnostics/media/diagnostics-report-4.png)
最后根据窗口提示完成所有操作后，点击右上角的复制按钮复制所有信息
![diagnostics report ask dialog options](https://doc-asset.easyar.com/develop/mega/media/unity-checklist.png)
请注意，这个界面不只是用来获取报告的，同时它也会引导你进行初步的问题筛查，请务必认真使用。
如遇到崩溃，请参考 崩溃分析（[Android](../../diagnostics/crash-android.html) [iOS/macOS/visionOS](../../diagnostics/crash-ios.html) [Windows](../../diagnostics/crash-windows.html)） 获取相关信息，一般来说如果没有完整的信息问题报告将是无效的。

---

## UI 消息
- 章节路径: `unity/diagnostics/ui-messages.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/diagnostics/ui-messages.html

# UI 消息
EasyAR Sense Unity Plugin 运行时有三类消息。
* 运行异常，包含 Sense Error、Session Error、Error、Warning
* Session Dump
* EasyAR Mega 开发特殊异常
您可以根据需要调整前两类消息的输出方式。可以通过 session 上的 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 组件在编辑器中配置，或是使用 [DiagnosticsController.MessageOutput](../../../api/unity/easyar.DiagnosticsController.html#u_easyar_DiagnosticsController_MessageOutput) 接口在脚本中配置。
![diagnostics ui messages](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message.png)
> **提示**
在 4000 版本中，如果场景由老版本插件创建，打开场景时 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 会被自动添加到 session 中。部分 Unity 版本中可能不会自动添加，在这些 Unity 版本中，[DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 会在运行时自动以默认值创建。
## 运行异常
插件运行时有时会收到内部组件发现的一些问题，以消息形式出现在系统中。这些消息有些可能是无法继续使用的严重故障，有些可能是故意触发的，有些可能是设备不受支持等等，按严重级别从高到低分为如下几类：
* [SenseError](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SenseError)：EasyAR Sense 错误，通常与 EasyAR Sense license 有关。
* [SessionError](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionError)：ARSession 错误，通常与设备不支持一些功能或错误的配置有关。
* [Error](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_Error)：其它错误信息
* [Warning](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_Warning)：警告信息
由于 Unity 开发的特殊性，我们默认会将这些消息显示在 UI 上，以辅助开发。
可以在编辑器或脚本中控制这些消息如何展示，可以选择的输出模式如下：
* [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)：输出到UI和日志。在头显上显示在眼前5米处。
* [Log](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_Log)：输出到系统日志。
> **提示**
* 建议在开发测试阶段使用默认配置 [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)。
* 建议在发布时将选项改成 [Log](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_Log)， 也可以保留 [UIAndLog](../../../api/unity/easyar.DiagnosticsController.MessageOutputMode.html#u_easyar_DiagnosticsController_MessageOutputMode_UIAndLog)，但这些UI消息通常对终端用户是不友好的。
* 建议在运行前 [判断 session 可用性和设备支持](../fundamentals/session-assemble.html) 并对不支持的设备进行合理提示。
### Sense Error
Sense Error 是一类特殊的错误，出现错误时 EasyAR 功能无法继续使用。常见原因：
* License 未正确配置或校验失败。该错误可以通过使用正确的 license 重新初始化来恢复。
* 部分设备（包括 AR Foundation、AR Engine 等所有使用自定义相机的设备或各种头显）上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）超过固定的有限时间。该错误无法恢复。
### Session Error
Session Error 是当前 ARSession 无法继续工作的错误。修改配置并重新运行 ARSession 可能可以解决这些错误。这些错误一般是由于您的配置错误、启动流程中抛出了异常导致组装中断、设备不受当前 ARSession 配置支持或是运行过程中 ARSession 组件丢失等导致的。
常见情况有：
* Session 组装错误：比如设备不受支持或支持设备的 Frame Source 没有正确配置在 ARSession 中等。
* Session 启动错误：云服务配置信息错误导致创建云服务功能出错，或配置信息未填写（包括 Mega 服务、云识别服务、SpatialMap 服务）等。
* Session 运行中错误：ARSession 组件被外部销毁，URP 环境下未正确配置 RendererFeature 等。
通常来说，配置错误以及启动流程中的异常导致组装中断都应该在开发过程中避免。设备不支持的情况主要出现在需要运动跟踪能力的功能上，需要参考 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 了解哪些功能需要注意设备支持，并在开发阶段选择合适的设备进行调试。
## Session Dump
[SessionDump](../../../api/unity/easyar.DiagnosticsController.MessageOutputOptions.html#u_easyar_DiagnosticsController_MessageOutputOptions_SessionDump) 消息展示的是插件运行时收集的 ARSession 的运行状态，包括各个组件的一些关键状态。这些状态信息对了解 EasyAR 的运行以及分析问题有很大帮助。
可以在编辑器或脚本中控制这些状态如何展示，可以选择的输出模式如下：
* [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI)：显示在 UI 并每帧更新。在头显上，显示在眼前5米处。
* [Log](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_Log)：输出到系统日志，由于每帧都输出，对运行性能是有影响的，建议在开发或测试时使用。
* [None](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_None)：不输出。
> **提示**
* 建议在开发测试阶段使用默认配置 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI)，上面显示的信息是与 EasyAR 工作人员进行沟通所必不可少的。
* 建议在正式上线后再修改为 [None](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_None)，并保留打开 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI) 的软件开关，或通过其它系统进行数据收集。在向 EasyAR 反馈问题时， EasyAR 会向您或您的用户索取这些信息，以判断应用运行状态。
* 在绝大多数情况下，应用上线后运行出问题，应用端还是需要首先进行问题排查和分析，在排除应用问题并获取足够信息后反馈的问题才能较好解决。日志收集和分析的第三方 SDK 和平台比较多，建议上线前使用。如果您没有使用这些平台的经验或资源，保留打开 [UI](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_UI) 的开关（比如使用隐藏开关）让用户反馈看到的信息将是比较简单的。
## EasyAR Mega 开发特殊异常
Mega 开发中，还有一类无法控制的警告信息，这类信息会在满足特定配置条件时显示在 UI 上，开发者无法直接关闭。
建议关注信息本身，文字上写明了出现的原因和配置方法。开发者需要了解不同配置对不同使用方式的要求并根据开发进展合理选择。
这类信息是故意展示的，因为在特定使用条件下，这些功能用来辅助内容流程开发，但同时无法获取合理的运行结果，注意不要带着信息上线。
## 相关主题
* [判断 session 可用性和设备支持](../fundamentals/session-assemble.html)
* [开发者模式](developer-mode.html)

---

## 适用于 target 和 origin 的 active 控制策略
- 章节路径: `unity/fundamentals/active-control.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/active-control.html

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

---

## EasyAR 项目中的 AR Foundation 场景配置和用法
- 章节路径: `unity/fundamentals/arfoundation-scene-setup.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/arfoundation-scene-setup.html

# EasyAR 项目中的 AR Foundation 场景配置和用法
在 Unity 中使用 AR Foundation 往往需要依靠 EasyAR 解决 AR Foundation 的设备局限性。以下内容介绍如何在 EasyAR 场景中正确配置和使用 AR Foundation，以及如何根据设备支持情况动态启用 AR Foundation。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
* 阅读 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html) 了解如何在 EasyAR 项目中安装和配置 AR Foundation。
## 添加 AR Foundation 组件
在 EasyAR 场景中添加 AR Foundation 的 AR Session 和 XR Origin。
### 添加 AR Session
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` > `AR Session` 添加 Unity 的 [ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html) 到场景中。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session.png)
> **注意**
这个 AR Session 与 EasyAR 的 AR Session 不同，它们需要同时存在于场景中。
### 添加 XR Origin
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` > `XR Origin (Mobile AR)` 添加 Unity 的 [XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 到场景中。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-origin.png)
> **注意**
这个 XR Origin 与 EasyAR 的 XR Origin 功能是重叠的，需要使用 Unity XR Origin 而非 EasyAR 的 XR Origin。
如果场景中之前存在 EasyAR 的 XR Origin，一般名称为 `XR Origin (EasyAR)`，需要将其下面的子物体移动到新创建的 XR Origin 下面，然后将 `XR Origin (EasyAR)` 删除。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-remove-origin.png)
这时候，如果新创建的 XR Origin 下面没有 XR Origin Child，需要手动添加。
在 `Hierarchy` 视图中，选中 **XR Origin** 并点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin Child` 添加 XR Origin Child 到 XR Origin 下。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-child-creation.png)
### 配置 Camera
如果场景中之前存在 AR 用的 `Camera`，会发现场景中出现了多余的主摄像机，需要将原本的摄像机删除。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-remove-camera.png)
然后选中 XR Origin 下的 `Main Camera`，按照 [Camera 配置](camera-configs.html) 的说明对摄像机进行配置。
最后，一个完整的添加了 AR Foundation 的 EasyAR 场景结构应该类似下面这样：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/)
> **小心**
如果需要通过 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 修改 AR Foundation 的配置，需要注意部分手机自身（比如小米 10）存在问题，在修改配置之后无法获取图像，EasyAR 将无法使用（应用有图像背景但 EasyAR 功能没有任何反应），因此通常并不建议修改，如需修改需要做好 EasyAR 无法使用时的降级方案。
## 设备兼容与动态启用 AR Foundation
EasyAR 兼容的设备比 AR Foundation 多很多，因此需要配置以确保应用只在需要时启用 AR Foundation，其余情况需要完全关闭 AR Foundation。
### 检查 frame source 组件
一般来说，通过 EasyAR 菜单创建的 session 通常会自动添加 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 以及 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) （部分图像跟踪等不需要SLAM功能的除外）。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/.png)
> **重要事项**
[ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 以及 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) 是 EasyAR 提供的 frame source，用于在支持 AR Foundation 的设备上启用 AR Foundation 功能。如果场景中的 session 不包含这些 frame source，则无法在启用 AR Foundation 功能。
如果场景中的 session 不包含这些 frame source，可以通过菜单手动添加。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-frame-source-creation.png)
为了在不支持 AR Foundation 的手机上运行，还需要确保 session 包含 AR Foundation 以外的 frame source。一个典型的ARSession 应该类似下面这样，
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-easyar.png)
> **提示**
可以根据实际需要对 frame source 进行排序，在应用运行时，session 会根据设备支持情况按 transform 顺序选择第一个可用的 frame source。
### 仅在需要时启用 AR Foundation
由于 AR Foundation 在手机上底层实现是 ARCore 和 ARKit，只能在有限的设备上使用，尤其是在很多国产 Android 手机上无法使用，所以通常建议仅在受支持的设备上启用 AR Foundation 及相关功能脚本。
EasyAR 可以自动完成这些操作，该功能可以通过 在 `Project Settings` > `EasyAR` > `Sense` 中的 `Unity XR` > `Unity XR Auto Switch` 选项启用或关闭。详细说明可以参考 [自动切换 Unity XR 物体](unity-xr-switch.html) 。
## 保留 AR Foundation 兼容性的场景
正确添加了 AR Foundation 组件的场景可以在 AR Foundation 包安装或未安装时都正常工作。
未安装 AR Foundation 时 AR Foundation 的功能及对应 frame source 不可用，且场景中会有部分脚本缺失，属于正常情况。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-missing-scripts.png)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-session-missing-origin.png)
> **提示**
很多 sample 都可以在 AR Foundation 包安装或未安装时都正常工作。如果需要在这些 sample 中启用 AR Foundation 支持，仅需 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html) 即可。
## 后续步骤
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* 文中提到的相关 AR 组件：
* [ARSession](session.html)
* [XR Origin](origin.html)
* [Camera](camera.html)
* AR Foundation 提供了部分设备上的运动跟踪能力，关于运动跟踪和各个 EasyAR 功能的关系，可以参考以下内容：
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)
* 有关 AR Foundation 场景配置的更多信息可以阅读 AR Foundation 官方文档，阅读前注意选择对应的文档版本：
* [场景配置](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/project-setup/scene-setup.html)
* [XR Origin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin-setup.html)

---

## 在 EasyAR 项目中启用 AR Foundation
- 章节路径: `unity/fundamentals/arfoundation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/arfoundation.html

# 在 EasyAR 项目中启用 AR Foundation
如果需要启用 EasyAR 的 AR Foundation 支持，或使用 AR Foundation 的其它功能，需要正确安装配置 AR Foundation。以下内容介绍如何完成这些操作。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
## AR Foundation 版本兼容性
EasyAR 支持 AR Foundation 5 或更新版本。
> **重要事项**
AR Foundation 的支持是通过自定义相机实现的。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
## 安装 AR Foundation
建议参考 [AR Foundation 官方文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest) 来安装 AR Foundation。阅读前注意选择对应的文档版本。
### Unity 2022 及更新版本
如果工程中未安装过 XR 相关插件，需要在 `Project Settings` > `XR Plug-in Management` 中，点击 `Install XR Plugin Management` 按钮来安装 XR Plug-in Management 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-managment.png)
如果需要在 Android 平台使用 AR Foundation，在 Android 标签下勾选 `Google ARCore` 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-arcore.png)
如果需要在 iOS 平台使用 AR Foundation，在 iOS 标签下勾选 `Apple ARKit` 并等待安装完成。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install-arkit.png)
如果需要在 visionOS 平台使用 AR Foundation，需要阅读 [Vision Pro 工程配置](../headsets/setup-visionpro.html)。
> **提示**
建议保持 `Initialize XR On Startup` 处于勾选状态，以确保 AR Foundation 能够在默认时间点初始化。
安装完成后，打开 `Package Manager` 窗口，可以看到 `AR Foundation` 以及对应平台的插件会出现在已安装的包列表中。注意这些包的版本号应完全一致。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-install.png)
> **重要事项**
在安装和更新 AR Foundation 时，需要确保 `Google ARCore XR Plugin` 和 `Apple ARKit XR Plugin` 版本与 `AR Foundation` 版本完全一致。版本不匹配可能会导致运行时错误或功能异常。
### Unity 2021
在 Unity 2021 版本中，需要手动编辑 `Packages/manifest.json` 文件来指定版本，参考 [官方文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.2/manual/project-setup/edit-your-project-manifest.html)。
比如，如果需要安装 AR Foundation 5.2.0 版本并在 Android 和 iOS 平台使用，要确保 `Packages/manifest.json` 文件中包含以下内容：
```
{
"dependencies": {
...
"com.unity.xr.arcore": "5.2.0",
"com.unity.xr.arfoundation": "5.2.0",
"com.unity.xr.arkit": "5.2.0",
...
}
}
```
## 配置 XR Plug-in
在使用 EasyAR 时，通常 ARCore 的存在并不是必需的。因此应配置 ARCore 为可选，以避免在不支持 ARCore 的设备上应用无法正常运行。
在 `Project Settings` > `XR Plug-in Management` > `ARCore` 中，将 `Requirement` 和 `Depth` 都设置为 `Optional`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-config-arcore.png)
> **小心**
如果把 `Requirement` 设置为 `Required`，并在不支持 ARCore 的设备上安装了打包后的应用，设备会错误地报告 ARCore 是可用的并以 ARCore 运行。这会造成一个假象，似乎这些设备正在运行 ARCore 并且运行不正常（黑屏或其它异常情况），但这是错误的。
出现这个现象的原因是由于 Google Play 商店阻止在不受支持的设备上安装标记 ARCore 为必需的应用，所以这些应用总是假设它们正在受支持的设备上运行。
正常配置下，这些设备会在 session 组装时判断 ARCore 不受支持并使用 EasyAR 的功能。
如有需要，也可以参考以下官方文档来进一步配置 ARCore 和 ARKit。阅读前注意选择对应的文档版本。
* [ARCore 插件配置](https://docs.unity3d.com/Packages/com.unity.xr.arcore@6.4/manual/project-configuration-arcore.html)
* [ARKit 插件配置](https://docs.unity3d.com/Packages/com.unity.xr.arkit@6.4/manual/project-configuration-arkit.html)
## 配置 Universal Render Pipeline
如果当前工程在使用 URP，需要配置 URP 资产。如未正确配置，AR Foundation 的摄像机背景图可能无法正确渲染。
首先确保已经正确配置 EasyAR 的 URP Renderer Feature，参考 [EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html)。
然后在Renderer Features 列表中添加 [ARBackgroundRendererFeature](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARBackgroundRendererFeature.html)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-config-urp.png)
与 EasyAR 的 URP Renderer Feature 配置一样，需要关注 `Project Settings` > `Quality` 中不同平台的配置，确保在所有需要使用 AR Foundation 的平台上都使用了正确配置了 [ARBackgroundRendererFeature](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARBackgroundRendererFeature.html) 的 URP 资产。
另外也可以参考 [AR Foundation 官方的 URP 配置文档](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/project-setup/universal-render-pipeline.html) 进行配置，阅读前注意选择对应的文档版本。
> **注意**
[EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html) 仍是需要的，这样才能确保在不支持 AR Foundation 的设备上使用 EasyAR 接口的相关功能渲染仍能正常。
## 启用 EasyAR AR Foundation 支持
在 `Project Settings` > `EasyAR` > `Sense` 中，确保 `Unity XR` > `AR Foundation Support` 选项被启用。**该选项是默认开启的。**
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/arf-enable.png)
修改该选项会触发脚本重新编译，需要等待脚本编译完成修改才会生效。如果 Unity 因为某种原因未正常触发编译，可以关闭 Unity，删除 `Library/ScriptAssemblies` 文件夹来强制 Unity 重新编译脚本。
> **提示**
如果 EasyAR 与工程中的 AR Foundation 不兼容，且没有同时使用 EasyAR 和 AR Foundation 的需求，可以关闭该选项。
## 后续步骤
* 了解 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html)
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* [EasyAR 的 Universal Render Pipeline 配置](../getting-started/universal-render-pipeline.html)

---

## 配置 camera
- 章节路径: `unity/fundamentals/camera-configs.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/camera-configs.html

# 配置 camera
通过以下内容，您将了解如何配置 Unity 中 AR 场景的 camera 以获得最佳的 AR 体验。
## 开始之前
* 通过 [Camera](camera.html) 了解 AR 场景中摄像机的作用，以及 session 如何控制摄像机的属性以确保正确的 AR 体验。
## 适用于手机和 PC 设备的 camera 配置
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/camera-config.png)
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/camera-config-urp.png)
在手机和 PC 设备上使用 AR 时，建议按照以下方式进行配置：
* **Clear Flags**：需要设置为 `Solid Color` 以确保 camera 图像可以正常渲染。如果保留默认的 *Skybox* ，camera 图像将无法显示。
* **Background**：非必需。考虑到使用体验，建议将背景颜色设为黑色以便在 camera 设备打开前和切换时以黑色过度。
* **Clipping Planes**：除通常渲染及性能需求之外，需要综合考虑识别及交互的物体或现实场景的物理大小和距离。比如可以设置 `Near` 为 0.1（米）以避免摄像机离物体较近时无法显示，设置 `Far` 为 1000（米）以避免远处物体无法显示。
> **注意**
使用 AR Foundation 或其他 Unity XR Origin 下的 camera 时，Unity 通常会预设其剪裁平面为 (0.1, 20) ，这可能会导致距离真实世界中的设备超过 20 米的物体无法显示出来。请在使用前根据具体需求来修改。
## 适用于头显的 camera 配置
使用头显时，camera 通常由设备 SDK 进行配置和控制，因此建议保留设备 SDK 默认配置，或根据设备 SDK 的要求进行配置。另外可以根据需要修改 **Clipping Planes**。

---

## AR 场景中的 Unity 摄像机
- 章节路径: `unity/fundamentals/camera.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/camera.html

# AR 场景中的 Unity 摄像机
Unity 中 AR 的效果呈现离不开摄像机。通过以下内容，您将了解 AR 场景中摄像机的作用，以及 session 如何控制摄像机的属性以确保正确的 AR 体验。
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
# AR 场景中摄像机的作用
Unity 中的摄像机用于向玩家展示游戏世界，而在 AR 场景中，摄像机的作用更加重要。它不仅负责渲染虚拟内容，还需要与现实世界进行对齐，以确保虚拟对象正确地叠加在现实场景中。
>
> 这段视频展示了一个简单的 AR 场景。视频左边是
`> Scene
`> 视图，右边是
`> Game
`> 视图。视频是使用模拟运行数据，在 Unity 编辑器的
`> Play
`> 模式录制的。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
> 可以看到，在这段视频里，代表用户的摄像机（摄像机图标）会根据用户在现实世界中的移动而移动。白色锥体截取了过去一段时间内摄像机的位置和朝向轨迹。可以看到在
`> Game
`> 视图中，摄像机不仅展示了
`> Scene
`> 视图里的虚拟内容，同时在虚拟内容底部还叠加了现实世界的图像，这就是 AR 场景中摄像机的典型工作方式。
>
为了确保虚拟对象正确地叠加在现实场景中，摄像机的部分属性需要根据 AR 运行的状态进行调整。这些属性包括：
* 摄像机的 transform（位置和朝向）
* 摄像机的视野（FOV）、宽高比（aspect ratio）和投影矩阵
* 摄像机的剔除设置（[GL.invertCulling](https://docs.unity3d.com/ScriptReference/GL-invertCulling.html)）
> **警告**
在开发应用时，修改 session 摄像机的这些属性是不受支持的，因为这可能会导致虚拟内容与现实世界对齐不正确，从而影响用户体验。即使通过某些手段修改了这些属性，AR 系统也会在运行过程中覆盖这些修改，或是因为渲染数据与计算数据的不一致导致不可预期的行为。
根据控制这些属性的对象的不同，session 所使用的摄像机可以分为两类：受 session 控制的摄像机和不受 session 控制的摄像机。
## 受 session 控制的摄像机
如果 session 的摄像机不属于任何外部系统，比如头显或 AR Foundation，那么 session 会自动控制摄像机的上述属性，以确保摄像机正确地与现实世界对齐。
### transform
摄像机的 transform（位置和朝向）是由 session 根据 AR 功能的运行状态进行调整的。一般来说，session 会根据运动跟踪数据和/或 target 的跟踪数据来更新摄像机的位置和朝向，从而确保用户看到的内容和现实世界中的内容一致。
在 Unity 中，所有 AR 跟踪的中心参考点被称为 session 中心，而 session 运行过程中决定这个中心的规则被称为中心模式。在不同的中心模式下，摄像机的 transform 行为有所不同：
* **在 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 中心模式下，摄像机是可以随意移动的。**
一般 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式很少被应用使用。
* **在其它中心模式（比如 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget)）下，摄像机是不能随意移动的。**
[FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 是大部分 AR 应用会采用的模式。
> **警告**
摄像机 transform 的 scale 数值应始终保持为 (1, 1, 1)。修改摄像机的 scale 可能会导致不可预期的行为。
### 投影矩阵
摄像机的投影矩阵会在 session 每帧更新时根据物理相机的内参进行更新，以确保虚拟内容正确地叠加在现实场景中。
### 剔除设置
摄像机的剔除设置（[GL.invertCulling](https://docs.unity3d.com/ScriptReference/GL-invertCulling.html)）会根据 session 的镜像设置进行调整，以确保虚拟内容正确地渲染在现实场景中。
在 [HorizontalFlip](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_HorizontalFlip) 中对应当前使用的摄像头的设置为 [World](../../../api/unity/easyar.ARSession.ARHorizontalFlipMode.html#u_easyar_ARSession_ARHorizontalFlipMode_World) 时，[GL.invertCulling](https://docs.unity3d.com/ScriptReference/GL-invertCulling.html) 会被设置为 `true`。这是前置摄像头的默认配置。
### AR 背景视频流
在 AR 场景中，摄像机通常会渲染来自物理相机的视频流作为背景，以增强用户的沉浸感。session 会自动处理视频流的获取和渲染，并确保视频流与虚拟内容正确地对齐。
## 不受 session 控制的摄像机
在使用头显和 AR Foundation 、以及实现中指定了 [IsCameraUnderControl](../../../api/unity/easyar.FrameSource.html#u_easyar_FrameSource_IsCameraUnderControl) 为 `false` 的 [FrameSource](../../../api/unity/easyar.FrameSource.html) 时，session 不会控制摄像机的上述属性，而是由外部系统负责控制。
> **警告**
虽然在这种情况下 session 不会控制摄像机的属性，但它们会由第三方系统（比如头显 SDK 或 AR Foundation）所控制，在开发应用时修改这些属性仍然是不受支持的。
## 复制摄像机时的注意事项
有时可能需要将 session 摄像机的参数复制到另一个摄像机上，这时需要额外关注以下两点：
* 属性获取时间：在使用受控摄像机时，需要参考 [获取 session 的运行结果](session-output.html) 在正确的时间获取这些参数；在使用不受控 session 控制的摄像机时，需要参考第三方系统的文档在正确的时间获取。
* 摄像机的视野（FOV）、宽高比（aspect ratio）和投影矩阵：需要使用 [Camera.projectionMatrix](https://docs.unity3d.com/ScriptReference/Camera-projectionMatrix.html) 获取摄像机投影矩阵，并复制到另外一个摄像机。[Camera.fieldOfView](https://docs.unity3d.com/ScriptReference/Camera-fieldOfView.html) 和 [Camera.aspect](https://docs.unity3d.com/ScriptReference/Camera-aspect.html) 在数学上是投影矩阵的一部分，使用 [Camera.fieldOfView](https://docs.unity3d.com/ScriptReference/Camera-fieldOfView.html) 和 [Camera.aspect](https://docs.unity3d.com/ScriptReference/Camera-aspect.html) 是不充分的。
## 后续步骤
* 阅读 [Camera 配置](camera-configs.html) 了解如何配置摄像机以获得最佳的 AR 体验
## 相关主题
* [中心模式](center-mode.html)

---

## 选择合适的中心模式
- 章节路径: `unity/fundamentals/center-mode-choosing.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/center-mode-choosing.html

# 选择合适的中心模式
选择合适的中心模式对于内容制作来说至关重要。通过以下内容，您将了解如何获取和修改中心模式，以及选择合适中心模式的建议。
## 开始之前
* 通过 [AR Session 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [AR Session 的中心模式](center-mode.html) 了解中心模式的基本概念及其对场景中物体运动行为的影响。
## 获取可用中心模式
在 session 运行时，只有当前 session 可用的中心模式会显示在 Inspector 面板的 `Center` 下拉菜单中。如果 session 未启动，则所有中心模式均会显示。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-available.png)
这张图中显示了在编辑器中使用 CameraDeviceFrameSource 时的 session 可用的中心模式。
在脚本中，可以在 session 成功组装后通过 [ARSession.AvailableCenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AvailableCenterMode) 属性来获取当前 session 中可用的中心模式列表。
比如，下面的代码展示了如何判断某个中心模式是否在当前 session 中可用：
```
if (Session.AvailableCenterMode.Contains(mode))
{
// mode 在当前 session 中可用
}
```
## 修改中心模式
打开 Inspector 面板，在 `Center` 下拉菜单中选择需要的中心模式。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-change.png)
在脚本中，可以通过 [ARSession.CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 属性来修改中心模式。
比如，下面的代码展示了如何在可用的中心模式之间循环切换：
```
while (true)
{
Session.CenterMode = (ARSession.ARCenterMode)(((int)Session.CenterMode + 1) % Enum.GetValues(typeof(ARSession.ARCenterMode)).Length);
if (Session.AvailableCenterMode.Contains(Session.CenterMode)) { break; }
}
```
session 每帧更新时会判断当前中心模式是否有效，如果有效，session 会立即尝试使用新的中心模式。
>
> 在上面这个视频中，session 一开始使用
[> FirstTarget
](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget)> 模式，中心物体是圣诞树（亮蓝色点云）。随后我们手动将中心模式修改为
[> Camera
](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera)> 模式，中心物体变为摄像机（蓝色锥体）。视频内容的详细描述请参考
[> AR Session 的中心模式
](center-mode.html)> 。
>
session 更新时，如果修改后的中心模式在当前 session 中无效，[CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 属性会被自动修改为第一个可用的中心模式（通常是 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)），并在日志中输出一行警告信息：
```
Center mode {Value} is unavailable in this session, reset to {NewValue}.
```
## 如何选择中心模式
与现实世界中的物体进行对齐是 AR 内容制作的核心需求，而中心模式决定了 session 以哪个物体作为参考点来计算场景中其它物体的位置和朝向。因此，选择合适的中心模式对于内容制作来说至关重要。
### 通用建议
很多时候使用 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 模式，以 `target` 作为中心对内容制作是更友好的，这样放在 `target` 下的内容参考点可以保持静止不动，不会因为 `XR Origin` 或 `camera` 的移动而产生不必要的影响（比如影响物理系统计算）。不过这并不绝对，具体来说：
* 在不知道怎么选择时，使用默认值，即 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 中心
由于绝大部分 AR 功能都是有误差的，而且运行中会不断修正这个误差，这就会导致看似在现实世界中相对不动的物体（比如稀疏空间地图的 `target` 和 运动跟踪的 `XR Origin`）实际在虚拟空间中是会有相对运动的，这时采用 `target` 作为中心就要比采用 `XR Origin` 要更符合内容制作的需要。
* 多个 `target` 同时被跟踪的情况
对于多个 `target` 同时被跟踪的情况，同样由于及计算误差，即使现实世界中的物体相对是静止的，这些 `target` 之间也可能存在相对运动。如何选择中心的物体则需要根据实际需要进行判断，通常 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 模式是更合适的选择。
* 什么时候使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式
[SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 适用于只有运动跟踪在运行的场景，这时 `XR Origin` 是唯一的参考点。它还适用于一些特殊情况，如果头显厂商没有正确实现运动跟踪的参考点，这时就必须使用 Unity 的世界中心从而强制使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式。
* [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式的使用场景
[Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式则更适用于物理相机不动的场景（比如使用固定摄像头的卡片对战类 AR），这时采用 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式会更便于内容创作。
### 不同 AR 功能的常用中心模式
在单独使用部分 AR 功能时，某些中心模式会更常用一些。下面的表格列出了这些 AR 功能对应的常用中心模式：
|功能|常用中心模式|
|Mega|FirstTarget 或 SpecificTarget|
|运动跟踪|SessionOrigin|
|平面检测|SessionOrigin|
|稀疏空间地图|FirstTarget 或 SpecificTarget|
|稠密空间地图|SessionOrigin|
|表面跟踪|FirstTarget 或 SpecificTarget|
|图像跟踪|FirstTarget、SpecificTarget 或 Camera|
|图像云识别|FirstTarget、SpecificTarget 或 Camera|
|物体跟踪|FirstTarget、SpecificTarget 或 Camera|
### 跨设备需要考虑的问题
在开发跨设备的 AR 应用时，需要考虑不同设备对中心模式的支持情况。
* 如果仅涉及手机和平板，通常不会有太大问题，如果需要使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)，要确保运动跟踪可以运行。
* 如果需要使用头显，则需要格外注意
* 查阅 [有效中心模式](center-mode.html#available-center-mode) 确定将要使用的设备都支持哪些中心模式。如果在使用第三方扩展，注意查看这些扩展使用的 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType)。
* 使用 Rokid 设备时，尽量不要使用 UXR。使用 XRI 可以确保大多数中心模式可用。
* 在不支持 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 和 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 模式的头显上，需要注意使用 Mega 或图像跟踪等绝大部分功能内容都是做不到相对 Unity 世界坐标系静止的。
## 每个中心模式都能正确显示的内容
> **警告**
在 Unity AR 中，任何存在于 Unity 世界坐标系下且未根据 session 组件调整 transform 的物体都可能无法正确显示。
如果世界坐标系下放置了一些模型，那这些模型的位置和朝向可能与现实世界中任何物体都没有对应关系，实际运行效果可能碰巧正常，也可能看上去像是浮在空中或者到处乱动。
要保证内容在任何中心模式下都能正确显示，正确的做法是：
* 始终把要显示的内容放在对应的 `target` 节点下，或者放在 `XR Origin` 节点下（如果内容需要跟随 XR Origin 运动）
* 或者通过手动方式对齐内容和 `target` 或 `XR Origin` 的位置和朝向，但需要在 [ARSession.PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件后操作
> **注意**
这么做并不能保证所有内容元素都工作正常，因为 Unity 的某些功能只能在世界坐标系下工作（比如物理系统），选择合适的中心模式仍然是重要的。
## 相关主题
* [获取 session 的运行结果](session-output.html)

---

## AR Session 的中心模式
- 章节路径: `unity/fundamentals/center-mode.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/center-mode.html

# AR Session 的中心模式
中心模式是 Unity AR 的核心概念，它决定了 session 在运行过程中选择哪个物体作为所有 AR 跟踪的参考点（中心物体），以及 session 中哪些物体可以随意移动。通过以下内容，您将了解中心模式的基本概念及其对场景中物体运动行为的影响。
## 开始之前
* 通过 [AR Session 简介](session.html)了解 session 的基本概念、组成和工作流程。
* 通过 [Camera](camera.html) 了解 AR 场景中摄像机的作用，以及 session 如何控制摄像机的属性以确保正确的 AR 体验。
* 通过 [XR Origin](origin.html) 了解 XR Origin 的基本概念、组成和生命周期。
* 通过 [Target](target.html) 了解 target 的基本概念、状态和生命周期。
## 中心物体和中心模式
在一个 session 中，可能同时运行着一个或多个不同的 AR 功能。这些 AR 功能可能会跟踪不同的物体，并且可能会同时使用运动跟踪功能来跟踪设备自身的位置和朝向。
为了确保场景中物体的运动行为符合预期，session 需要选择一个参考点作为所有 AR 跟踪的中心，这个参考点在 Unity 场景中的代表就是中心物体（[CenterObject](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterObject)）。中心模式（[CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode)）是 session 运行过程中决定这个中心物体到底是哪一个物体的规则。
一个 session 的中心可以是以下几种物体之一：
* 某个被跟踪的 target
* XR Origin
* 摄像机
中心模式决定了 session 选择哪一个物体作为中心物体，以及这个物体是否可以随意移动。而这个物体以外的物体（包括非中心的摄像机、XR Origin 和 target）都是受 session 控制，以中心物体为参考点进行运动的。
在 Unity 中，session 支持以下四种中心模式：
|名称|示意图|描述|
|**FirstTarget**
**SpecificTarget**|![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-target.png)|以 target 作为中心，该 target 可以随意移动。其中，
* FirstTarget 以第一个被跟踪的 target 作为中心。
* SpecificTarget 以指定的 target 作为中心。session 中的 camera 和 XR Origin 以及其他 target 都受 session 控制，以中心 target 为参考点进行运动。|
|**SessionOrigin**|![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-origin.png)|以 XR Origin 作为中心，XR Origin 可以随意移动。
session 中的 camera 和 target 都受 session 控制，以中心 XR Origin 为参考点进行运动。|
|**Camera**|![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/center-camera.png)|以摄像机作为中心，摄像机可以随意移动。
session 中的 XR Origin 和 target 都受 session 控制，以中心摄像机为参考点进行运动。|
>
> 示意图中有三个物体，蓝色球体代表 XR Origin，蓝色锥体标代表摄像机，黄色图片代表 target。在不同的中心模式下，session 会选择不同的物体作为中心物体，图中显示了对应物体的局部坐标系。
>
> **提示**
如果您有使用 AR Foundation 的使用经验，可能会注意到 AR Foundation 中并不存在类似的概念。实际上，AR Foundation 的行为模式与 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式是一致的。
在 session 中，`target` 和 `camera` 的相对运动关系由当前 session 控制。`XR Origin` 和 `camera` 的相对运动关系，由当前 session 控制或者第三方框架（比如 AR Foundation）控制。中心模式的存在保证了在不同的运行环境下，session 都能正确地控制场景中物体的运动行为。
比如，如果 AR Foundation 或基于 Unity XR 的头显 SDK 控制了 `XR Origin` 和 `camera` 的相对运动关系，`XR Origin` 作为 Unity XR 框架的设计，是可以由 session 控制移动的，而 `camera` 则不行。这时 session 会限制中心模式为 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 、 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 或 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)，这样对于 session 来说，中心会是 `XR Origin` 或某个 `target`，而对于 Unity XR 框架来说，中心仍然是 `XR Origin`，整个系统可以完美工作。
> **警告**
在 Unity AR 中，任何存在于 Unity 世界坐标系下且未根据 session 组件调整 transform 的物体都可能无法正确显示。因为 session 会根据中心物体的位置和朝向来调整场景中其它物体的位置和朝向，如果有物体不受 session 控制，它们的位置和朝向就可能与 session 计算出来的位置和朝向不一致，从而导致不可预期的行为。
比如，如果世界坐标系下放置了一个熊猫模型，这个熊猫模型的位置和朝向就可能与现实世界中任何物体都没有对应关系，看上去像是浮在空中或者到处乱动。
正确的做法是始终把要显示的内容放在某个 `target` 节点下，或者放在 `XR Origin` 节点下（如果内容需要跟随 XR Origin 运动）。这样内容的位置和朝向就会根据 session 的计算结果进行调整，从而确保内容能够正确地叠加在现实世界中。
通过手动方式对齐内容和 `target` 或 `XR Origin` 的位置和朝向是可以的，但需要在正确的时间操作，可以参考 [选择合适的中心模式](center-mode-choosing.html) 。
## 有效中心模式
并不是所有的中心模式在任何情况下都是有效的。session 会根据当前运行环境和选用的 frame source 来决定哪些中心模式是有效的，从而保证能够正确地控制场景中物体的运动行为。[ARSession.AvailableCenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AvailableCenterMode) 属性可以用来获取当前 session 的有效中心模式列表。
根据最终选用的 frame source 的不同，session 的有效中心模式有以下这几种不同情况：
|frame source|摄像机受控|有运动数据|有原点设计|有效中心模式|
|
* CameraDeviceFrameSource
* FramePlayer 且录制时使用的 frame source 无运动数据
* ExternalImageStreamFrameSource|是|否|-|
* FirstTarget
* SpecificTarget
* Camera|
|
* ARCoreFrameSource
* AREngineFrameSource
* ARKitFrameSource
* InertialCameraDeviceFrameSource
* MotionTrackerFrameSource
* ThreeDofCameraDeviceFrameSource
* FramePlayer 且录制时使用的 frame source 有运动数据|是|是|是|
* FirstTarget
* SpecificTarget
* SessionOrigin
* Camera (\*)\* *仅在 `camera` 不是
`XR Origin` 子节点时有效*|
|
* ARCoreARFoundationFrameSource
* ARKitARFoundationFrameSource
* VisionOSARKitFrameSource
* XREALFrameSource
* ExternalDeviceFrameSource 且 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin) 或 [Custom](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_Custom)
* PicoFrameSource
* RokidFrameSource 且不使用 UXR|否|是|是|
* FirstTarget
* SpecificTarget
* SessionOrigin|
|
* ExternalDeviceFrameSource 且 [OriginType](../../../api/unity/easyar.ExternalDeviceFrameSource.html#u_easyar_ExternalDeviceFrameSource_OriginType) 是 [None](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_None)
* RokidFrameSource 且使用 UXR|否|是|否|
* SessionOrigin|
除了使用 FramePlayer 时之外，有效中心模式都是在 session 组装时确定的。使用 FramePlayer 时，有效中心模式是在 session 运行过程中每帧数据输出时根据数据中是否包含运动信息动态决定的。
## 不同中心模式的特性
接下来，我们将通过一系列示例视频来展示不同中心模式下物体的运动行为。
视频内容如下：
>
> 在现实世界中，有两个不同类型的可跟踪物体：
>
>
> 一个是
> 圣诞树
> ，它是静止不动的。它是通过稀疏空间地图功能进行跟踪的。
>
> 另一个是一张
> A4 纸
> ，纸上事先打印好了一张图片，它是可以移动的。它是通过图像跟踪功能进行跟踪的。
>
>
> 录制视频时，观察者（手机）从圣诞树的右后方开始，绕着圣诞树移动。A4 纸在观察者前方左右摆动。
>
> 为了便于观察，我们对场景中的不同物体添加了一些标识，
>
>
* **> 圣诞树
> ：处于跟踪状态时在其所占据的空间叠加了
> 亮蓝色点云
> 。跟踪丢失时这些标识会消失。
>
* **> A4 纸
> ：处于跟踪状态时在其正上方叠加了一个
> 熊猫
> 。
`> Game
`> 视图中还额外显示了一个与 A4 纸内容和大小完全相同的图片。跟踪丢失时这些标识会消失。
>
* **> XR Origin
> ：在其位置放置了一个
> 蓝色球体
>
* **> 摄像机
> ：在其位置放置了一个
> 蓝色锥体
> ，锥体的主轴与摄像机的视线方向一致。
>
>
这些视频均是使用模拟运行数据，在 Unity 编辑器的 `Play` 模式录制的。视频左边是 `Scene` 视图，右边是 `Game` 视图。`Game` 视图的内容与用户在现实世界中手机看到的内容是一样的。
### FirstTarget 和 SpecificTarget 中心模式
FirstTarget 和 SpecificTarget 中心模式是以某个 `target` 作为中心物体的模式。在这两个模式下，除了中心的 `target` 之外，session 中的 `camera` 和 `XR Origin` 以及其他 `target` 都是受 session 控制，以中心 `target` 为参考点进行运动的。
有些 target 在现实世界中是可以移动的，比如视频中的 A4 纸。
>
> 在上面这个视频中，中心物体是通过图像跟踪功能跟踪到的 A4 纸。可以看到，由于没有外部操作，A4 纸（熊猫）是静止不动的，而摄像机（蓝色锥体）、XR Origin（蓝色球体）和 圣诞树（亮蓝色点云）都在移动。
>
有些 target 在现实世界中是静止的，比如视频中的圣诞树。
>
> 在上面这个视频中，中心物体是通过稀疏空间地图功能跟踪到的圣诞树。可以看到，由于没有外部操作，圣诞树（亮蓝色点云）是静止不动的，而摄像机（蓝色锥体）和 A4 纸（熊猫）都在移动。XR Origin（蓝色球体）也没有移动，但这是因为它相对圣诞树是静止的。
>
在这两个模式下，作为参考点的中心 `target` 可以自由移动，这时 session 中的 `camera` 和 `XR Origin` 以及其他 `target` 都会跟着动，它们的 transform 不能被外部控制。
>
> 在上面这个视频中，中心物体是通过图像跟踪功能跟踪到的 A4 纸。可以看到，由于我们手动移动了 A4 纸（熊猫），摄像机（蓝色锥体）、XR Origin（蓝色球体）和 圣诞树（亮蓝色点云）都跟着动了。需要注意的是，这时
`> Game
`> 视图显示的内容并没有变化，因为摄像机的位置和朝向相对于 A4 纸和其它物体是没有变化的。
>
FirstTarget 和 SpecificTarget 模式的区别在于在运行过程中，中心 `target` 可能产生变化，但变化时中心的选择方式不同。要说明这个问题，我们要把跟踪成功和丢失的过程考虑在内。
在 session 中心物体发生变化时， [ARSession.CenterObject](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterObject) 会始终反映当前的中心物体，但 [ARSession.CenterMode](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_CenterMode) 不会发生改变。
#### FirstTarget 中心模式的中心变化
FirstTarget 中心模式下，session 始终是以第一个跟踪到的 `target` 为中心的。如果这个 `target` 跟踪丢失了，session 会重新选择中心，当 session 跟踪着或新跟踪上了另一个 `target`，另一个 `target` 就会被选作新的中心物体。
重新选择中心会出现在以下这些情况：
* 当前帧没有任何一个 `target` 在跟踪状态
这时如果 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式有效，session 会退化到 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式选择 `XR Origin` 作为中心物体；否则 session 会退化到 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式选择 `camera` 作为中心物体。
* 当前帧有 `target` 在跟踪状态，且上一帧没有任何一个 `target` 在跟踪状态
这时 session 会选择其中一个被跟踪的 `target` 作为中心物体。
* 当前帧有 `target` 在跟踪状态，且上一帧的中心 `target` 在当前帧跟踪丢失
这时 session 会选择其中一个被跟踪的 `target` 作为新的中心物体。
>
> 在上面这个视频中，一开始中心物体是通过图像跟踪功能跟踪到的 A4 纸。可以看到，当 A4 纸（熊猫）跟踪丢失时，session 重新选择了中心物体，这时圣诞树（亮蓝色点云）成为了新的中心物体，在视频结尾时，A4 纸重新被跟踪上了，但它并没有成为中心物体，因为圣诞树已经是中心物体了。
>
#### SpecificTarget 中心模式的中心变化
SpecificTarget 中心模式下，session 始终是以指定的 `target` 为中心的。如果这个 `target` 跟踪丢失了，session 会重新选择中心，但它不会选择其它 `target` 作为新的中心物体，当 session 重新跟踪上了这个指定的 `target`，它仍然会被选作中心物体。
重新选择中心会出现在以下这些情况：
* 当前帧指定的 `target` 未被跟踪
这时如果 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式有效，session 会退化到 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式选择 `XR Origin` 作为中心物体；否则 session 会退化到 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 模式选择 `camera` 作为中心物体。
* 当前帧指定的 `target` 在跟踪状态，且上一帧指定的 `target` 未被跟踪
这时 session 会选择指定的 `target` 作为中心物体。
>
> 在上面这个视频中，中心物体被指定为通过图像跟踪功能跟踪到的 A4 纸。可以看到，当 A4 纸（熊猫）跟踪丢失时，session 并没有选择其它
`> target
`> 作为新的中心物体，这时圣诞树（亮蓝色点云）并没有成为中心物体。在视频结尾时，A4 纸重新被跟踪上了，它恢复成为了中心物体。
>
### SessionOrigin 中心模式
SessionOrigin 中心模式是以 `XR Origin` 作为中心物体的模式。在这个模式下，session 中的 `camera` 和 `target` 都是受 session 控制，以中心 `XR Origin` 为参考点进行运动的。
>
> 在上面这个视频中，中心物体是 XR Origin。可以看到，由于没有外部操作，XR Origin（蓝色球体）是静止不动的，而摄像机（蓝色锥体）和 A4 纸（熊猫）都在移动。圣诞树（亮蓝色点云）也没有移动，但这是因为它相对 XR Origin 是静止的。
>
在这个模式下，作为参考点的中心 `XR Origin` 可以自由移动，这时 session 中的 `camera` 和 `target` 都会跟着动，它们的 transform 不能被外部控制。
>
> 在上面这个视频中，中心物体是 XR Origin。可以看到，由于我们手动移动了 XR Origin（蓝色球体），摄像机（蓝色锥体）、圣诞树（亮蓝色点云）和 A4 纸（熊猫）都跟着动了。需要注意的是，这时
`> Game
`> 视图显示的内容并没有变化，因为摄像机的位置和朝向相对于 XR Origin 和其它物体是没有变化的。
>
在 SessionOrigin 模式下，`XR Origin` 是必须有效的，因此这种模式下中心物体不会发生变化。
### Camera 中心模式
camera 中心模式是以 `camera` 作为中心物体的模式。在这个模式下，session 中的 `XR Origin` 和 `target` 都是受 session 控制，以中心 `camera` 为参考点进行运动的。
>
> 在上面这个视频中，中心物体是摄像机。可以看到，由于没有外部操作，摄像机（蓝色锥体）是静止不动的，而 XR Origin（蓝色球体）、圣诞树（亮蓝色点云）和 A4 纸（熊猫）都在移动。
>
在这个模式下，作为参考点的中心 `camera` 可以自由移动，这时session 中的 `XR Origin` 和 `target` 都会跟着动，它们的 transform 不能被外部控制。
>
> 在上面这个视频中，中心物体是摄像机。可以看到，由于我们手动移动了摄像机（蓝色锥体），XR Origin（蓝色球体）、圣诞树（亮蓝色点云）和 A4 纸（熊猫）都跟着动了。需要注意的是，这时
`> Game
`> 视图显示的内容并没有变化，因为摄像机的位置和朝向相对于 XR Origin 和其它物体是没有变化的。
>
在 Camera 模式下 `camera` 是必须有效的，因此这种模式下中心物体不会发生变化。
## 后续步骤
* 尝试 [选择合适的中心模式](center-mode-choosing.html)
## 相关主题
* [运动跟踪简介](../../motion-tracking/intro.html)
* [图像跟踪简介](../../image-tracking/intro.html)
* [稀疏空间地图简介](../../sparse-spatial-mapping/intro.html)

---

## AR Session 组件参考
- 章节路径: `unity/fundamentals/comp-ARSession.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/comp-ARSession.html

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

---

## 使用 License Key 初始化 EasyAR Sense
- 章节路径: `unity/fundamentals/initialization.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/initialization.html

# 使用 License Key 初始化 EasyAR Sense
在 Unity 中使用 EasyAR，需要使用 license key 初始化 EasyAR Sense，以确保功能被激活。有两种初始化方式：自动初始化和手动初始化。
初始化成功后，可以通过 Unity 控制台或操作系统日志看到 EasyAR Sense 的版本号和运行平台信息，例如：
>
> EasyAR Sense (Android-arm64) Version 4.7.0.11800-cf8e24e30
>
## 开始之前
* [EasyAR Sense 许可证](../../license-sense.html) 描述了如何获取 EasyAR Sense 许可证（license key）。在初始化 EasyAR Sense 之前，需要根据实际使用的设备和开发阶段准备好合适的许可证。
## 自动初始化
自动初始化适用于大部分使用场景。
打开 `EasyAR 全局配置`，勾选 `Initialize On Startup` 选项，并填写 `EasyAR Sense License` > `LicenseKey`
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-license-settings.png)
自动初始化会在 Unity 的 [BeforeSceneLoad](https://docs.unity3d.com/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) 时间点自动调用。
> **注意**
在编辑器下使用的 license 不会校验应用包名，所以编辑器中可以正常使用的 license，在打包到平台应用或 app 运行时仍有可能失败，这时候需要注意两种情况：
1. 填写的 license 的包名与 Unity Player Settings 中填写的 bundle id/package name 应该一致。
2. 如果 Unity 打包后，在 gradle 或 XCode 工程中修改了包名。这时需要在 Unity 中使用 gradle 或 XCode 里面的包名。
## [可选] 手动初始化
手动初始化主要用于自定义的初始化流程，比如在调用 EasyAR 接口之前弹出用户隐私说明（请参阅 [合规指南](../../compliance/guide.html) ）等。
打开 `EasyAR 全局配置` ，取消勾选 `Initialize On Startup` 选项。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-license-settings-manual.png)
然后使用 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 接口手动调用初始化。
可以通过参数传入 license，
```
EasyARController.Initialize("my-license");
```
也可以使用 `EasyAR 全局配置` 中填写的 license,
```
EasyARController.Initialize();
```
> **重要事项**
[EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 必须在 [ARSession](../../../api/unity/easyar.ARSession.html) 启动之前调用。
在一些特殊情况下，如果要多次调用 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize)，需要确保每次 [EasyARController.Initialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Initialize) 执行后通过 [EasyARController.Deinitialize()](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_Deinitialize) 进行反初始化。
## 初始化失败的解决方法
在包含了 [ARSession](../../../api/unity/easyar.ARSession.html) 的场景运行后，如果日志中没有包含类似的信息，则说明初始化失败。
>
> EasyAR Sense (Android-arm64) Version 4.7.0.11800-cf8e24e30
>
在 Unity 编辑器中，可能还会看到类似这样的弹窗
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/init-fail.png)
> **注意**
需要注意阅读弹窗中显示的文字信息，并不是所有弹窗都是初始化失败。
常见的出错信息和原因如下：
* EasyARSettings is not found
* `EasyAR 全局配置` 资源文件未创建（常见于没有填写 license）
* License Key is empty
* `EasyAR 全局配置` 中未填写 license，或工程中存在多个 `EasyAR 全局配置` 资源文件
* EasyARController.Initialize is not called (InitializeOnStartup = false)
* 手动初始化未在正确的时机调用
* EasyAR stops after script change in play mode
* 编辑器中运行时，脚本发生了改动。这时需要重新运行即可
## 相关主题
* [ARSession](session.html)
* [EasyAR 全局配置](setup-easyar.html)
* [合规指南](../../compliance/guide.html)
* 日志查看方法： [Android](../../diagnostics/log-android.html)、[iOS](../../diagnostics/log-ios.html)、[Unity 编辑器](../../diagnostics/log-windows.html)

---

## AR 驱动的 Unity 应用基础
- 章节路径: `unity/fundamentals/intro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/intro.html

# AR 驱动的 Unity 应用基础
EasyAR Sense Unity 插件包提供了在 Unity 中开发 AR 应用的基础功能。本文介绍了在 Unity 中开发 AR 应用时需要了解的基础知识和组件。
## 开始之前
* 了解 [AR 驱动的 3D 渲染](../../fundamentals/fundamentals.html)。
## Unity AR 应用开发基础
首先，您需要通过以下内容了解 EasyAR 兼容哪些 Unity 版本及平台：
* [Unity 兼容性](unity-compatibility.html)
在 Unity 中，AR 应用的典型流程与 [一般 AR 应用](../../fundamentals/fundamentals.html) 类似，但通过 AR Session 组件来管理摄像头数据的获取、跟踪器的运行以及虚拟内容的渲染。
```
flowchart TD
subgraph AR
CameraDevice[Camera Device]
Tracker[Tracker]
Renderer[Renderer]
CameraDevice -->|Image Frame| Tracker
Tracker -->|Image Frame + Tracked Pose| Renderer
end
subgraph unity["Unity AR"]
B[Session]
C([Camera])
O([Origin])
T([Target])
B -- transform --> C
B -- transform --> O
B -- transform --> T
classDef Unity fill:#6e6ce6,stroke:#333,color:#fff
class B Unity
class C Unity
class O Unity
class T Unity
end
CameraDevice -..- B
Tracker -..- B
Renderer -..- C
Renderer -..- O
Renderer -..- T
```
您将从以下这些基础组件开始，逐步了解 Unity 中 AR 应用的基础知识：
* [AR Session](session.html)
* [Camera](camera.html)
* [XR Origin](origin.html)
* [Target](target.html)
然后，您需要了解**中心模式**，这是理解 EasyAR 对 Unity 组件行为控制的关键概念：
* [中心模式](center-mode.html)
如果您有 Unity XR 框架（比如 AR Foundation）的使用经验，您可能会希望了解怎样在开发 EasyAR 应用时使用这些功能：
* [Unity XR 框架](unity-xr.html)
* [AR Foundation](arfoundation.html)
如果您已经在 Unity 编辑器内完成了 AR 开发，您可能会希望在打包发布前了解如何配置 Unity 项目以便在目标设备上运行：
* [Player 配置](setup-player.html)
* [EasyAR 配置](setup-easyar.html)
结合上面这些基础知识，您可以参考以下工作流程示例，实践您所学到的内容：
* [Workflow\_ARSession 示例](sample-arsession.html)
## 后续步骤
在掌握了 Unity AR 应用开发的基础知识后，您仍需继续了解更多 AR 开发所需的功能和组件：
* 了解 [帧数据源（Frame Source）](../cameras/frame-source.html)
* 了解 [Unity AR 模拟运行](../simulation/simulation.html) 并在开发过程中多加利用
* 了解 [诊断功能](../diagnostics/diagnostics.html) 并在开发过程中多加利用
如果您需要在头显设备上运行 EasyAR 应用，您还需要：
* 了解 [XR 头显](../headsets/headsets.html) 的使用

---

## 创建 XR Origin
- 章节路径: `unity/fundamentals/origin-creation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/origin-creation.html

# 创建 XR Origin
通过以下内容，您将了解如何在 Unity 场景中创建和配置 XR Origin 以及 XR Origin Child。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [XR Origin](origin.html) 了解 XR Origin 的基本概念、组成和生命周期。
## 创建 XR Origin (EasyAR)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin (EasyAR)` 可以创建一个完整 origin 结构。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-creation.png)
在脚本中，可以使用 [ARSessionFactory.CreateOrigin()](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateOrigin) 创建：
```
ARSessionFactory.CreateOrigin();
```
> **注意**
session 运行时，如果场景中没有正确的 XR Origin 结构，XR Origin 和一个 XR Origin Child 会被自动创建。
## [可选] 创建 XR Origin (Unity XR)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `XR` > `XR Origin (Mobile AR)` 可以创建适用于 AR Foundation 的 XR Origin。有关该 XR Origin 的详细信息和创建方法，请参考 Unity 官方文档：[添加 Unity XR 的 XR Origin 到场景](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin-setup.html)。
> **注意**
使用头显时，请务必参考对应头显 SDK 的文档进行操作。
在使用 Unity XR 框架提供的 XR Origin 时，需要手动添加 XR Origin Child。
## 添加 XR Origin Child 到 XR Origin
在 `Hierarchy` 视图中，选中 **XR Origin (EasyAR)** 或 **XR Origin** 并点击右键，通过菜单 `EasyAR Sense` > `Origin` > `Origin : XR Origin Child` 可以添加 XR Origin Child 到 XR Origin 下。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-child-creation.png)
在脚本中，可以使用 [ARSessionFactory.AddOriginChild(GameObject)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddOriginChild_UnityEngine_GameObject_)：
```
ARSessionFactory.AddOriginChild(origin);
```
可以添加任意多个 XR Origin Child，它们都会正常工作。但是对于 session 内部生成的物体来说，只会使用第一个 XR Origin Child 作为父节点。
> **注意**
session 运行时，如果场景中没有正确的 XR Origin Child 结构，XR Origin Child 会被自动创建。
## 后续步骤
* 了解 XR Origin 的 [active 控制策略](active-control.html)

---

## Unity AR 的运动跟踪中心 —— XR Origin
- 章节路径: `unity/fundamentals/origin.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/origin.html

# Unity AR 的运动跟踪中心 —— XR Origin
XR Origin 是 Unity 中运动跟踪功能的核心概念。在现代 AR 应用中，运动跟踪正在逐步成为必不可少的功能。通过运动跟踪，应用可以在不借助其它识别物的前提下了解用户在现实世界中的位置和朝向，从而实现沉浸式的 AR 体验。通过以下内容，您将了解 XR Origin 的基本概念、组成和生命周期，以及在什么情况下需要使用 XR Origin。
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
## XR Origin 是什么
运动跟踪功能初始化时会选择一个参考点作为跟踪的原点。这个参考点一般是用户启动应用时或是系统 AR 服务启动时设备所在的位置。这个参考点在 Unity 场景中的代表就是 XR Origin。在大多数情况下，XR Origin 在场景中的起始位置也是摄像机的默认起始位置。
>
> 这段视频展示了一个简单的只有运动跟踪在运行的 AR 场景。视频左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图。视频是使用模拟运行数据，在 Unity 编辑器的
`> Play
`> 模式录制的。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
> 可以看到，在这段视频里，XR Origin（蓝色球体）在场景中的位置是固定的，而代表用户的摄像机（摄像机图标）会根据用户在现实世界中的移动而移动。白色锥体截取了过去一段时间内摄像机的位置和朝向轨迹，可以更好地理解摄像机在场景中的运动情况。可以看到这些白色锥体是生成在 XR Origin 的节点下的，这也是这类场景中物体的典型组织结构。
>
在 Unity 的运动跟踪系统中，摄像机一般是跟随 XR Origin 进行运动的。虽然摄像机并不一定是 XR Origin 的子节点，但 AR Session 会根据 XR Origin 的位置来计算摄像机的位置，从而保证用户看到的内容和现实世界中的内容一致。
>
> 这段视频展示了同样的场景，不过这次我们在运行时移动了 XR Origin（蓝色球体）。可以看到，XR Origin 被移动后，摄像机会跟随 XR Origin 进行运动，而
`> Game
`> 视图中的内容并没有变化。
>
在实际的 AR 场景中，这种运动关系要更加复杂一些。
## XR Origin 在不同中心模式下的行为
在 Unity 中，所有 AR 跟踪的中心参考点被称为 session 中心，而 session 运行过程中决定这个中心的规则被称为中心模式。在不同的中心模式下，XR Origin 的行为有所不同：
* **在 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式下，XR Origin 是可以随意移动的。**
一般 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式会在只有运动跟踪在工作的场景中使用。在有其它功能同时运行时，通常不会使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式。
不过在使用头显时，如果厂商没有在 Unity 中正确实现运动跟踪的参考点，这时就必须使用 Unity 的世界中心从而强制使用 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式。这种情况要求内容根节点要跟随 AR 功能进行运动，这可能会影响内容效果，但在第三方厂商做出更改之前并没有其它办法。
* **在其它中心模式（比如 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget)）下，XR Origin 是不能随意移动的。**
一般 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 模式在非运动跟踪或有其它 AR 功能与运动跟踪同时运行的场景中使用。
在这种模式下，XR Origin 的位置是由 AR 功能决定的，因此不能随意移动 XR Origin。
关于中心模式以及场景内物体的运动方式可以详细参考： [中心模式](center-mode.html) 。
## XR Origin 的形式和组成
EasyAR 可以使用两种不同形式的 XR Origin：
* EasyAR 提供的 XR Origin
* Unity XR 框架提供的 XR Origin
### XR Origin (EasyAR)
典型的 XR Origin 结构如下所示：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin.png)
XR Origin 根节点是一个空的 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html)，它可以有一个或多个 XR Origin Child 子节点。XR Origin Child 包含了一个 [XROriginChildController](../../../api/unity/easyar.XROriginChildController.html) 组件，用于代理 XR Origin 的控制逻辑。
session 运行时，如果场景中没有正确的 XR Origin 结构，XR Origin 和一个 XR Origin Child 会被自动创建。运行过程中，XR Origin Child 会被约束在 XR Origin 相同的位置和朝向下。
由 session 生成的物体，比如稀疏空间地图建图的点云，或是稠密空间建图的网格，会被创建在 XR Origin Child 节点下。
>
> 这段视频展示相同场景下在运动跟踪同时运行了稠密空间建图的效果。可以看到生成的网格是被创建在 XR Origin Child 节点下的。
>
> 注：为了便于理解，视频中关闭了深度图生成，因此视频中
`> Scene
`> 视图的内容与实际运行时显示的内容会有差异。
`> Game
`> 视图的显示效果与关闭 mesh 透明时相同。
>
### [可选] XR Origin (Unity XR)
如果需要，可以选择使用 Unity XR 框架提供的 [XR Origin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/manual/xr-origin.html) 组件。
在使用 Unity XR 框架提供的 XR Origin 时，一个典型的结构如下所示：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-unityxr.png)
在头显场景中，一个典型的结构如下所示：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/origin-unityxr-headset.png)
XR Origin 根节点是由 Unity XR 框架创建和维护的 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html)，它可以有一个或多个 XR Origin Child 子节点。XR Origin Child 包含了一个 [XROriginChildController](../../../api/unity/easyar.XROriginChildController.html) 组件，用于代理 XR Origin 的控制逻辑。
session 运行时，如果场景中没有正确的 XR Origin Child 结构，XR Origin Child 会被自动创建。运行过程中，XR Origin Child 会被约束在 XR Origin 相同的位置和朝向下。
Unity XR 框架提供的 XR Origin 主要为以下两种情况提供支持：
* 您已经在项目中使用了 AR Foundation，并希望与 EasyAR 同时工作或根据设备支持情况在两者之间切换。
* 您所使用的头显 SDK 使用了 Unity XR 框架提供的 XR Origin 组件。
> **注意**
当 Unity XR 的核心包 `com.unity.xr.core-utils` 未被导入到工程中时，如果场景中的摄像机处于与 Unity XR 框架提供的 XR Origin 相同的层级结构中（Camera 及名为 Camera Offset 父节点），session 会假定这个结构是 Unity XR 框架创建的并使用它。这样做是为了给场景提供最大限度的兼容性，即：使用 AR Foundation 创建的场景，在 AR Foundation 未被导入工程中时，AR Foundation 不会工作但剩余的 AR 功能仍能正常工作。除了只有 AR Foundation 能提供的功能之外，这甚至不影响整个 AR 应该的功能性和设备兼容性。
大多数的 EasyAR 的示例场景都使用了这种方式来保证在没有 AR Foundation 的情况下仍然可以运行，且在 AR Foundation 存在时可以展示与 AR Foundation 的协同工作能力。
在 AR Foundation 的定义中，它的 XR Origin 是 XR 场景中跟踪空间的中心。不过需要注意的是，在 AR Foundation 的概念中，运动跟踪被作为必选功能，它所描述的 XR 场景中的跟踪就是运动跟踪。
在 EasyAR 系统中，运动跟踪是一个可选的功能，因此 XR Origin 也是可选的。XR Origin 只在启用了运动跟踪功能时才会创建和使用。
## XR Origin 的生命周期
XR Origin 的生命周期依托于 session。在 session 启动时，XR Origin 会被选定或被创建（如果场景中没有正确的 XR Origin 结构）。在 session 停止时，XR Origin 会留在原地直至被下一个 session 使用或被手动删除。
## 后续步骤
创建
* 尝试在场景中 [创建 XR Origin](origin-creation.html)
控制运行
* 了解 XR Origin 的 [Active 控制策略](active-control.html)
## 相关主题
* [中心模式](center-mode.html)
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)

---

## Workflow\_ARSession 示例详解
- 章节路径: `unity/fundamentals/sample-arsession.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/sample-arsession.html

# Workflow\_ARSession 示例详解
`Workflow\_ARSession` 是一个**轻量级**的 AR 会话管理示例，旨在展示如何以最小依赖构建一个完整的 AR 应用流程。该示例同时支持 **AR Foundation 兼容模式** 和 **简易模式** ，您可以根据项目需求灵活选择。
## 使用方法
### 场景选择（二选一）
在 Unity 编辑器中，`Workflow\_ARSession` 场景包含两组互斥的配置根对象，请**仅启用其中一组**（确保另一组处于非激活状态）：
|配置名称|适用场景|依赖|
|`ARFoundationCompatibleSceneSetup`|已使用或计划集成 **AR Foundation** 的项目|需完成 [AR Foundation 配置](arfoundation.html)|
|`SimpleSceneSetup`|**不依赖 AR Foundation**，直接使用 EasyAR 原生能力|无额外依赖，适合轻量级 AR 应用|
### 构建与运行
1. 将 `Workflow\_ARSession` 添加至菜单栏 `File` > `Build Settings` 或 `Build Profiles` > `Scene List` 中。
2. 根据所选目标平台（如 Android 或 iOS），在 `Project Settings` > `Player` 中确认构建选项。
3. 构建到真机并运行。
应用启动后，将自动初始化摄像头并等待识别目标。
## 识别目标与获取方法
本示例默认演示 **图像识别（Image Tracking）** 功能，但其架构可轻松扩展至物体跟踪、云识别等其他模式。
### 默认目标：`namecard.jpg`
* **目标类型**：2D 图像（建议打印尺寸 ≥ 90mm × 54mm）
* **下载地址**：🔗 [namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
### 如何替换目标？
1. 将您的图像（JPG/PNG）放入 `Assets/Samples/EasyAR Sense Unity Plugin/[版本号]/\_\_All Samples\_\_/Workflow/Workflow\_ARSession/Targets`。
2. 选择场景中的 `ImageTarget-namecard` 组件，在 **Inspector** 的 `Image Target Controller (Script)` 中更改 `Texture` 为您的图像。
3. 修改 `Name` 和 `Scale`。 `Scale` 是您的目标的物理尺寸（单位：米），以图像的长边为准。
![Replace Image Target](https://doc-asset.easyar.com/develop/unity/fundamentals/media/image-target-config.png)
4. 保存并重新构建。
## 预期效果
当摄像头对准目标图像时，系统将：
1. 实时检测并跟踪图像；
2. 在图像平面上叠加一个 3D 熊猫；
熊猫的位置、朝向与缩放严格绑定于图像目标的位姿，即使图像运动、部分遮挡或光照变化，仍能稳定跟踪。
## 扩展建议
* **添加物体跟踪**：替换 `ImageTracker` 为 `ObjectTracker`，加载 `.obj` 模型文件；
* **接入云识别**：使用 `CloudRecognizer` 替代本地目标列表；
* **多目标支持**：从单个图像目标扩展为多个图像，系统将自动处理并发跟踪。
> **提示**
更多功能组件请 [访问AR功能组件](session-components.html)。
通过 `Workflow\_ARSession`，您可快速掌握 EasyAR 的核心工作流，并以此为基础构建生产级 AR 应用。

---

## 判断 session 可用性和设备支持
- 章节路径: `unity/fundamentals/session-assemble.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-assemble.html

# 判断 session 可用性和设备支持
在启动 AR 之前，通常需要先判断 session 是否可用以及当前设备是否支持所需的 AR 功能。本文介绍了如何进行这些检查。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 通过 [设备支持和报告](session-report.html) 了解 Unity 中设备支持和 session 报告的基础知识
* 了解如何 [创建 session](session-creation.html)
## 在启动流程中获取报告
如果组装之后直接启动了 session，可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告。
需要在 session start 之前订阅 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件，通常在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 中完成订阅是安全的：
```
void Awake()
{
Session.StateChanged += HandleSessionStateChange;
}
```
在事件处理中需要关注的 session 的状态包括：[Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 和 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。[Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态说明 session 已经成功启动，也即说明 session 在当前设备上可用。[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态说明 session 启动失败，也即说明 session 在当前设备上不可用。
[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并不总是在设备不受支持的时候出现。所以还需要使用 [SessionReport.BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 获取具体的失败原因。
```
void HandleSessionStateChange(ARSession.SessionState status)
{
if (status == ARSession.SessionState.Ready)
{
// session 在当前设备上可用
}
else if (status == ARSession.SessionState.Broken)
{
// session 在当前设备上不可用
if (Session.Report.BrokenReason == SessionReport.SessionBrokenReason.NoAvailabileFrameSource ||
Session.Report.BrokenReason == SessionReport.SessionBrokenReason.FrameFilterNotAvailabile)
{
// 所选组件不受当前设备支持
}
else
{
// 设备无关的原因
}
}
}
```
出现 [SessionReport.SessionBrokenReason.NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource) 和 [SessionReport.SessionBrokenReason.FrameFilterNotAvailabile](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_FrameFilterNotAvailabile) 这两种原因，说明 session 组件在当前设备上不可用；而其它原因通常是设备无关的。严格来说，出现这两种原因意味着当前配置（且仅该配置）下的 AR 功能无法在该设备上运行。配置指 session 物体中选择的功能和设置。可以从 [Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 中获得详细的可用性报告。
对于 [SessionReport.SessionBrokenReason.NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource) 的情况，如果在启动 session 时联网更新设备列表时发现设备已被支持，session 有可能自动恢复。
## 在启动前获取报告
如果希望在 session 启动前做出判断，并根据具体情况决定是否启动 session，可以手动调用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 并使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告。
需要在 session assemble 之前订阅 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件，
```
Session.AssembleUpdate += OnAssembleUpdate;
```
在组装第一阶段，仍然可用利用 [ARSession.SessionState](../../../api/unity/easyar.ARSession.SessionState.html) 和 [Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 来判断 session 受支持的情况。但是第二阶段的报告不会更新到 session 中。
因此一般手动调用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 时，需要在 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件中处理组件可用性报告，从而判断 session 在当前设备上是否可用。
需要重点关注 [SessionReport.AvailabilityReport.FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 列表中组件的可用性。如果有任何一个 frame source 组件是可用的，那么 [SessionReport.AvailabilityReport.FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 部分在当前设备上就是可用的。
同时还需要关注报告中的 [SessionReport.AvailabilityReport.FrameFilters](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameFilters) 列表中组件的可用性。但是判断标准根据组装选项不同，会要求所有 frame filter 可用，或是任意数量的 frame filter 可用。默认选项下，要求所有 frame filter 可用。
在默认配置下，可以使用如下代码判断 session 组件在当前设备上是否可用：
```
void OnAssembleUpdate(SessionReport.AvailabilityReport report)
{
if (report.FrameSources.Any(f => f.Availability == SessionReport.AvailabilityReport.AvailabilityStatus.Available) &&
report.FrameFilters.All(f => f.Availability == SessionReport.AvailabilityReport.AvailabilityStatus.Available))
{
Session.AssembleUpdate -= OnAssembleUpdate;
// session 组件在当前设备上可用，可以启动 session
Session.StartSession();
}
else
{
// session 组件在当前设备上不可用
}
if (report.PendingDeviceList.Count <= 0)
{
Session.AssembleUpdate -= OnAssembleUpdate;
}
}
```
注意 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件可能会触发两次。上面的代码示例中，会在确认组件可用后取消订阅事件。
这种判断方法没法判断 session 启动过程中可能出现的其它错误，但这些错误通常是设备无关的，如有需要可以在启动 session 后通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件进行补充判断。
## session 组件不可用时的选择
在应用开发中，一般都希望对尽量多的设备提供兼容支持。因此当 session 组件在当前设备上不可用时，可以考虑以下几种选择：
* 降级使用其它 AR 功能
通过修改 session 组件配置，选择当前设备支持的 AR 功能。可以参考 [创建 session](session-creation.html) 了解如何修改 session 组件配置。
* 提供非 AR 体验
在 session 组件不可用时，提供一个非 AR 的体验。比如在导航场景下，如果 AR 导航无法实现，提供传统2D导航是非常有用的。
* 提示用户更换设备
在某些应用场景下，用户可能会使用不支持 AR 功能的设备。此时可以提示用户更换设备以获得更好的体验。
在选择这些方案时，可以结合应用的具体需求和用户群体进行权衡。在 AR 应用中，如果部分设备确实无法提供 AR 或降级方案，仍然需要提供一个良好的用户提示信息，以便让用户了解当前设备的限制。
## 后续步骤
* 了解 [控制 session 执行](session-ctrl.html) 的方法
* 了解 [帧数据源及运行时选取](../cameras/frame-source.html)
* 另外，您还可以通过下面这些示例来了解获取报告之后的应用场景：
* [Workflow\_ARSession 示例](sample-arsession.html) 使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示，同时还使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件在 UI 上展示了每个组件的可用性
* SpatialMap\_Sparse\_AllInOne 示例使用 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件对设备支持进行了提前判断和不可用提示
* MotionTracking\_DeviceMotionAndPlaneDetection 示例使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示
* MegaBlock\_Basic 示例使用了 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件并对 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态提供了 UI 提示

---

## 访问 session 中的 AR 功能组件
- 章节路径: `unity/fundamentals/session-components.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-components.html

# 访问 session 中的 AR 功能组件
在运行中的 session 里，可以通过 [Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性访问各个功能组件。本文介绍了如何访问这些组件，以及访问时需要注意的事项。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 了解如何 [创建 session](session-creation.html)
## 编辑时或启动前配置 AR 组件
有些时候，某些组件选项（比如 [DesiredFocusMode](../../../api/unity/easyar.CameraDeviceFrameSource.html#u_easyar_CameraDeviceFrameSource_DesiredFocusMode)）必需在组件启动前配置，如果不想在 session 启动后再手动配置并启动组件，一个简单的方法是在 session 组装前对所有可能使用的 frame source 组件进行配置。组装过程会保留这些组件中的一个或多个，并应用其配置。
这时可以使用 [FindAnyObjectByType<T>()](https://docs.unity3d.com/ScriptReference/Object.FindAnyObjectByType.html) 或 [GetComponent<T>()](https://docs.unity3d.com/ScriptReference/Component.GetComponent.html) 等任何 Unity 基本方法找到组件，然后对组件进行配置。
> **注意**
通过这种方法获取到的 AR 组件是否会在运行时被包含在 session 中是不确定的。因此必需对所有可能的情况进行配置。
例如，下面的代码展示了在 session 组装前修改所有 frame source 组件的对焦模式的过程：
```
void Awake()
{
var allFrameSources = Session.GetComponentsInChildren<FrameSource>();
foreach (var source in allFrameSources)
{
if (source is CameraDeviceFrameSource)
{
((CameraDeviceFrameSource)source).DesiredFocusMode = autoFocus ? CameraDeviceFocusMode.Continousauto : CameraDeviceFocusMode.Medium;
}
else if (source is MotionTrackerFrameSource)
{
((MotionTrackerFrameSource)source).DesiredFocusMode = autoFocus ? MotionTrackerCameraDeviceFocusMode.Continousauto : MotionTrackerCameraDeviceFocusMode.Medium;
}
else if (source is ARCoreFrameSource)
{
((ARCoreFrameSource)source).DesiredFocusMode = autoFocus ? ARCoreCameraDeviceFocusMode.Auto : ARCoreCameraDeviceFocusMode.Fixed;
}
else if (source is ARKitFrameSource)
{
((ARKitFrameSource)source).DesiredFocusMode = autoFocus ? ARKitCameraDeviceFocusMode.Auto : ARKitCameraDeviceFocusMode.Fixed;
}
else if (source is AREngineFrameSource)
{
((AREngineFrameSource)source).DesiredFocusMode = autoFocus ? AREngineCameraDeviceFocusMode.Auto : AREngineCameraDeviceFocusMode.Fixed;
}
else if (source is ThreeDofCameraDeviceFrameSource)
{
((ThreeDofCameraDeviceFrameSource)source).DesiredFocusMode = autoFocus ? ThreeDofCameraDeviceFocusMode.Auto : ThreeDofCameraDeviceFocusMode.Fixed;
}
else if (source is InertialCameraDeviceFrameSource)
{
((InertialCameraDeviceFrameSource)source).DesiredFocusMode = autoFocus ? InertialCameraDeviceFocusMode.Auto : InertialCameraDeviceFocusMode.Fixed;
}
else if (source is ARFoundationFrameSource)
{
cameraManager.autoFocusRequested = autoFocus;
}
}
}
```
上述过程也可以在编辑器中完成，同样需要对所有组件都进行配置：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-components-editor.png)
其中 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 和 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html) 两个 frame source 对应的配置在 `Main Camera` 的组件上。
> **警告**
通过这种方法获取到的 AR 组件只能用于运行前的配置。
由于组装过程会对 AR 组件进行筛选，通过场景树获取的 AR 组件可能并没有被包含在 session 中，无法正常工作。
## 运行中使用组装好的 AR 组件
session 中运行的 AR 组件是在组装后才确定的。在组装完成之前，任何 AR 组件都不能使用。组装好的 AR 组件可以通过 [Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性访问。
[Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 在 session 的状态 >= [Assembled](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Assembled) 的条件下可以使用。详细来说，[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 方法执行完成后，[Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性才会被赋值，可以通过它访问 session 组件。在 session 停止或损坏后，[Assembly](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assembly) 属性会被清空，无法再访问组件。
可以在脚本中检测 session 的 [State](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_State) 来判断当时是否可以访问 AR 组件：
```
if (Session.State >= ARSession.SessionState.Ready)
{
// Assembly 可以使用
}
else
{
// Assembly 不能使用
}
```
也可以通过订阅 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件来获取 session 的状态变化，从而在合适的时间点访问 AR 组件。一般来说为了能捕获到 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态，需要在 session start 之前订阅 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件，通常在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 中完成订阅是安全的：
```
void Awake()
{
Session.StateChanged += (state) =>
{
if (Session.State == ARSession.SessionState.Ready)
{
// Assembly 可以使用，在这之后 Assembly 一直可以访问，直至 session 停止或损坏
}
else if (Session.State < ARSession.SessionState.Ready)
{
// Assembly 不能使用，在这之后 Assembly 一直不可访问，直至 session 重新启动
}
else
{
// Assembly 可以使用，通常不需要处理
}
};
}
```
> **小心**
如果通过 [FindAnyObjectByType<T>()](https://docs.unity3d.com/ScriptReference/Object.FindAnyObjectByType.html) 或 [GetComponent<T>()](https://docs.unity3d.com/ScriptReference/Component.GetComponent.html) 等方法获取到 AR 组件是一定会被包含到 session 中的，也可以在运行时中使用。
只是存储这些组件的引用是安全的，但在使用这些组件时必须确保 session 处于运行状态且这些组件被正确包含在 session 中，否则可能会引发异常或不可预期的行为。
session 启动前和停止后，这些组件是无法工作的。建议即使在这样的用法中，也要关注 session 的 [State](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_State) 和 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件。
### 访问 frame source 组件
可以使用 [ARAssembly.FrameSource](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameSource) 属性访问 frame source 组件。在一个正常运行的 session 中，[ARAssembly.FrameSource](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameSource) 有且只有一个。
在使用 session 时，通常需要通过访问 [ARAssembly.FrameSource](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameSource) 才能确定运行时实际使用的 frame source 组件类型，从而访问该组件特有的属性和方法。
例如，下面的代码展示了如何根据 frame source 的不同使用不同的平面检测方法：
```
void PlaceObject(Vector2 touchPosition)
{
if (Session.Assembly.FrameSource is MotionTrackerFrameSource)
{
Ray ray = Session.Assembly.Camera.ScreenPointToRay(touchPosition);
if (Physics.Raycast(ray, out var hitInfo))
{
TouchRoot.transform.position = hitInfo.point;
}
}
else if (Session.Assembly.FrameSource is ARFoundationFrameSource)
{
var raycastManager = Session.Assembly.Origin.Value.GetComponent<UnityEngine.XR.ARFoundation.ARRaycastManager>();
var hits = new List<UnityEngine.XR.ARFoundation.ARRaycastHit>();
if (raycastManager.Raycast(touchPosition, hits, UnityEngine.XR.ARSubsystems.TrackableType.PlaneWithinPolygon))
{
var hitPose = hits[0].pose;
TouchRoot.transform.position = hitPose.position;
}
}
}
```
### 访问 frame filter 组件
可以使用 [ARAssembly.FrameFilters](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameFilters) 属性访问 frame filter 组件。在一个正常运行的 session 中，[ARAssembly.FrameFilters](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameFilters) 列表中的任何一个类型的组件都有可能有多个。
例如，下面的代码展示了如何获取 session 中的一个 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 并注册对应的事件：
```
var megaTracker = session.Assembly.FrameFilters.Where(f => f is MegaTrackerFrameFilter).FirstOrDefault() as MegaTrackerFrameFilter;
if (megaTracker)
{
megaTracker.LocalizationRespond += (response) =>
{
};
}
```
### 访问 camera 组件
可以使用 [ARAssembly.Camera](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Camera) 属性访问 camera 组件。如果场景中有多个 camera，这时一个找到 AR 使用的摄像机的快捷方式。
例如，下面的代码展示了如何获取 session 中的 camera 并对场景中的物体进行射线检测：
```
var ray = Session.Assembly.Camera.ScreenPointToRay(screenPoint);
if (Physics.Raycast(ray, out var hitInfo))
{
TouchRoot.transform.position = hitInfo.point;
};
```
### 访问 origin 组件
可以使用 [ARAssembly.Origin](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Origin) 属性访问 origin 组件。
例如，下面的代码展示了如何获取 session 中的 origin 并将一个代表当前摄像机位置和朝向的锥体显示在场景中：
```
if (session.Assembly.Origin.OnSome)
{
GameObject frustum = Instantiate(CameraFrustumPrefab, session.Assembly.Camera.transform.position, session.Assembly.Camera.transform.rotation);
frustum.transform.SetParent(session.Assembly.Origin.Value.transform);
}
```
需要注意的是，这里需要先判断 [ARAssembly.Origin](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Origin) 是否存在。
> **注意**
[ARAssembly.Origin](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Origin) 只在启用了运动跟踪功能的 session 中存在。
### 访问 CameraImageRenderer 组件
可以使用 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 属性访问 [CameraImageRenderer](../../../api/unity/easyar.CameraImageRenderer.html) 组件。
例如，下面这段代码可以获取物理相机图像的 [RenderTexture](https://docs.unity3d.com/ScriptReference/RenderTexture.html)：
```
RenderTexture renderTexture;
void Awake()
{
Session.StateChanged += (state) =>
{
if (state == ARSession.SessionState.Ready && Session.Assembly.CameraImageRenderer.OnSome)
{
Session.Assembly.CameraImageRenderer.Value.RequestTargetTexture((\_, texture) => renderTexture = texture);
}
};
}
```
需要注意的是，这里需要先判断 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 是否存在。
> **注意**
[ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 只在由 EasyAR 进行画面绘制的 session 中有效。一般来说，使用 AR Foundation 或头显时是无效的，这时物理相机画面的绘制由 AR Foundation 或头显 SDK 完成。
### 访问 FrameRecorder 组件
可以使用 [ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 属性访问 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html) 组件。
例如，下面这段代码可以启动录制，文件存储位置取决于配置，默认会存储在应用内存储目录中：
```
if (session.Assembly.FrameRecorder.OnSome)
{
var frameRecorder = session.Assembly.FrameRecorder.Value;
frameRecorder.enabled = true;
}
```
需要注意的是，这里需要先判断 [ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 是否存在。
> **注意**
[ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 在少数情况下，比如使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html) 时是不能使用的。
## 后续步骤
* 了解如何 [获取 session 的运行结果](session-output.html)，这些结果中包含了 AR 组件的运行输出
* 另外，您还可以通过下面这些示例来了解组件的访问：
* [Workflow\_ARSession 示例](sample-arsession.html) 展示了各种组件的访问和使用方法
## 相关主题
* [帧数据源](../cameras/frame-source.html) 描述了 frame source 以及运行时的选取方式
* [XR Origin](origin.html) 描述了 AR 场景中 origin 组件的用途
* [Camera](camera.html) 描述了 AR 场景中 camera 组件的用途
* [录制EIF文件](../simulation/recording.html) 描述了 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html) 的详细使用方法

---

## 创建和配置 AR session
- 章节路径: `unity/fundamentals/session-creation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-creation.html

# 创建和配置 AR session
在 Unity 中使用 AR，需要首先在场景中创建并配置 AR session。本文介绍了创建和配置 AR session 的几种主要方法。一般在成功创建 session 之后，在 `Hierarchy` 视图中可以看到如下结构：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-result.png)
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
## 创建默认配置的 session
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `AR Session ([ 功能 ] Preset)` 可以创建一个预设好的 session。session 预先配置了适合该功能的 frame source 和 frame filter 组件。
在脚本中，可以使用 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 来创建 session。
比如，通过菜单 `EasyAR Sense` > `Image Tracking` > `AR Session (Image Tracking Preset)` 可以创建一个用于图像跟踪的 session。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation.png)
对应的脚本代码如下：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.ImageTracking);
```
需要注意的是，在使用 [ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_SparseSpatialMapBuilder) 以及 [ARSessionFactory.ARSessionPreset.DenseSpatialMapBuilder](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_DenseSpatialMapBuilder) 预设时，需要同时传入资源参数。例如，下面的代码创建了一个用于稀疏空间构建的 session，并指定了点云材质：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder, new ARSessionFactory.Resources { SparseSpatialMapPointCloudMaterial = PointCloudMaterial });
```
如果脚本只在编辑器中运行，也可以使用默认编辑器资源：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder, ARSessionFactory.Resources.EditorDefault());
```
菜单 `EasyAR Sense` > `AR Session (Preset)` > `\*\*` 中列出了所有可以使用的预设 session，可以参考使用。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-presets.png)
> **注意**
同一个场景中多个 session 同时运行会相互冲突，因此在场景中最多只能保留一个被启用（[GameObject.activeInHierarchy](https://docs.unity3d.com/ScriptReference/GameObject-activeInHierarchy.html) == `true`）的 session。
## 添加组件
session 的 frame source 和 frame filter 组件可以在 session 创建后根据需要添加和删除。
在 `Hierarchy` 视图中，选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `[ AR 功能 ]` > `\*\*` 可以添加适合该功能的 frame source 和 frame filter 组件。
在脚本中，可以使用 [ARSessionFactory.AddFrameSource<Source>(GameObject, bool)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameSource__1_UnityEngine_GameObject_System_Boolean_) 来添加 frame source 组件，或使用 [ARSessionFactory.AddFrameFilter<Filter>(GameObject, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_AddFrameFilter__1_UnityEngine_GameObject_easyar_ARSessionFactory_Resources_) 来添加 frame filter 组件。
比如，通过菜单 `EasyAR Sense` > `Image Tracking` > `Frame Filter : Image Tracker` 可以给当前选中的 session 添加一个新的图像跟踪器。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-add.png)
对应的脚本代码如下：
```
ARSessionFactory.AddFrameFilter<ImageTrackerFrameFilter>(session);
```
> **小心**
添加组件必需在 assemble 前完成。session 开始执行 assemble 以及完成 assemble 后，任何对组件的增加和删除都会导致 session 进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并停止工作。
需要注意的是，在添加 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html) 以及 [DenseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.DenseSpatialMapBuilderFrameFilter.html) 时，需要同时传入资源参数。例如，下面的代码创建了一个用于稀疏空间构建的 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html)，并指定了点云材质：
```
ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, new ARSessionFactory.Resources { SparseSpatialMapPointCloudMaterial = PointCloudMaterial })
```
如果脚本只在编辑器中运行，也可以使用默认编辑器资源：
```
ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, ARSessionFactory.Resources.EditorDefault());
```
创建 frame filter 之后，可以使用 [ARSessionFactory.SetupFrameFilters(List<GameObject>, ARSessionFactory.ARSessionPreset)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_SetupFrameFilters_System_Collections_Generic_List_UnityEngine_GameObject__easyar_ARSessionFactory_ARSessionPreset_) 来根据预设配置调整 frame filter 的参数。
比如下面这段代码给 session 添加一个新的图像跟踪器，并配置成 [ARSessionFactory.ARSessionPreset.ImageTrackingMotionFusion](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_ImageTrackingMotionFusion) 的预设参数。
```
var filter = ARSessionFactory.AddFrameFilter<ImageTrackerFrameFilter>(session);
ARSessionFactory.SetupFrameFilters(new() { filter }, ARSessionFactory.ARSessionPreset.ImageTrackingMotionFusion);
```
使用菜单创建时无法按预设调整参数，需要在创建后根据具体的组件说明进行配置。
## 删除组件
要从 session 中删除组件，可以在 `Hierarchy` 视图中选中对应的组件并按 `Delete` 键，或者在脚本中销毁（`Destroy`）对应的物体。
> **注意**
禁用（`SetActive(false)`）组件的 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的效果与删除组件相同。
比如要从 session 中删除图像跟踪器，可以选中 `Image Tracker` 并按 `Delete` 键。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-del.png)
> **小心**
删除组件必需在 assemble 前完成。session 开始执行 assemble 以及完成 assemble 后，任何对组件的增加和删除都会导致 session 进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态并停止工作。
## 组件排序的影响
session 的 frame filter 子节点的排列顺序对 session 执行没有任何影响。
session 的 frame source 子节点的排列顺序将影响 frame source 在 assemble 过程中的选择顺序。只有按 **transform 顺序** 排列的第一个可用的 frame source 会被选中作为 session 的实际 frame source。
> **注意**
frame source 节点的顺序只有在 assemble 之前修改是有效的。assemble 后，调整顺序不会影响运行结果。
## [可选] 自由创建 session
如果默认配置的 session 不能满足需求，还可用根据需要自由创建和配置 session。
可用使用菜单 `EasyAR Sense` > `AR Session (Preset)` > `AR Session (Empty)` 创建一个不包含任何 frame source 和 frame filter 组件的空 session。
在脚本中，可以使用 [ARSessionFactory.CreateSession()](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession) 来实现。
```
ARSessionFactory.CreateSession();
```
然后根据实际需要，添加合适的 frame source 和 frame filter 组件。
比如，如果需要创建一个包含稀疏空间构建和稠密空间构建功能的 session，可以使用下面的代码：
```
var session = ARSessionFactory.CreateSession();
var group = new GameObject("Frame Source Group");
group.transform.SetParent(session.transform, false);
ARSessionFactory.AddFrameSource<XREALFrameSource>(session);
ARSessionFactory.AddFrameSource<AREngineFrameSource>(session);
ARSessionFactory.AddFrameSource<ARCoreFrameSource>(session);
ARSessionFactory.AddFrameSource<ARCoreARFoundationFrameSource>(session);
ARSessionFactory.AddFrameSource<ARKitFrameSource>(session);
ARSessionFactory.AddFrameSource<ARKitARFoundationFrameSource>(session);
ARSessionFactory.AddFrameSource<VisionOSARKitFrameSource>(session);
ARSessionFactory.AddFrameSource<MotionTrackerFrameSource>(session);
List<GameObject> filters = new();
filters.Add(ARSessionFactory.AddFrameFilter<SparseSpatialMapBuilderFrameFilter>(session, resources));
filters.Add(ARSessionFactory.AddFrameFilter<DenseSpatialMapBuilderFrameFilter>(session, resources));
ARSessionFactory.SetupFrameFilters(filters, ARSessionFactory.ARSessionPreset.SparseSpatialMapBuilder);
ARSessionFactory.SetupFrameFilters(filters, ARSessionFactory.ARSessionPreset.DenseSpatialMapBuilder);
```
它将创建出这样的 session 结构：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation-custom.png)
## 后续步骤
控制运行
* 了解 [初始化](initialization.html) 的方法和作用
* 了解如何 [判断可用性和设备支持](session-assemble.html)
* 了解 [控制 session 执行](session-ctrl.html) 的方法
访问组件和结果
* 尝试 [访问 AR 功能组件](session-components.html)
* 了解如何 [获取 session 的运行结果](session-output.html)
组件参考
* [ARSession](comp-ARSession.html) 组件参考
进一步了解 frame source 排序的影响和如何
* 了解 [帧数据源](../cameras/frame-source.html)
* 了解 [创建一组输入源](../cameras/frame-source-group.html) 的方法
根据应用功能创建最佳的 session
* [Mega](../mega/session-best-practice.html)

---

## session 的流程控制
- 章节路径: `unity/fundamentals/session-ctrl.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-ctrl.html

# session 的流程控制
在 session 的运行过程中，有时需要对 session 组件进行修改，这时就需要停止再重新启动 session。有时还可能需要停止 session 的某些输出。本文介绍了如何控制 session 的运行流程。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 了解如何 [创建 session](session-creation.html)
## session 的组装
通常在启动 session 时会自动触发组装过程。
下面这段代码会隐式执行组装过程。
```
Session.StartSession();
```
有些时候，比如需要提前 [判断可用性和设备支持](session-assemble.html)，也可以使用 [Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 手动触发 session 组装过程：
```
StartCoroutine(Session.Assemble());
```
> **注意**
[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 返回一个协程，需要通过 [StartCoroutine(IEnumerator)](https://docs.unity3d.com/ScriptReference/MonoBehaviour.StartCoroutine.html) 启动。
## 启动 session
[AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 控制 session 是否自动启动。如果 [AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 为 `true`（默认值），则在 [MonoBehaviour.Start()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) 时 session 会自动启动。
session 也可以手动启动，这需要提前修改 [AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) 为 `false`。然后可以使用 [StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 来启动 session。
```
Session.StartSession();
```
## 停止 session
可以使用 [StopSession(bool)](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StopSession_System_Boolean_) 来停止 session。
```
Session.StopSession(keepLastFrame);
```
可以通过参数 `keepLastFrame` 来控制 session 停止后是否保留最后一帧的物理相机图像。这在需要切换不同 session 时比较有用，可以避免画面闪烁。
> **注意**
`keepLastFrame` 只能控制那些由 EasyAR 进行画面绘制的 session。一般来说，使用 AR Foundation 或头显时该参数无效。
## 停止 session 输出
session 运行时，可以通过 [enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 来控制 session 的输出。
下面这段代码可以停止 session 的所有输出，这时 session 仍然处于运行状态，但不会更新任何内容（包括由 EasyAR 绘制的物理相机画面和所有 EasyAR 控制的节点的 transform 等）。
```
Session.enabled = false;
```
## 停止 session 绘制物理相机图像
可以使用 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 来控制物理相机图像的绘制。
下面这段代码可以停止物理相机图像的绘制：
```
if (Session.Assembly != null && Session.Assembly.CameraImageRenderer.OnSome)
{
Session.Assembly.CameraImageRenderer.Value.enabled = false;
}
```
需要注意的是，这里需要先判断 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 是否存在。
> **注意**
[ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 只在由 EasyAR 进行画面绘制的 session 中有效。一般来说，使用 AR Foundation 或头显时是无效的，这时物理相机画面的绘制由 AR Foundation 或头显 SDK 完成。
## 后续步骤
* 尝试 [访问 AR 功能组件](session-components.html)，了解更多 AR 功能的控制方法
* 了解如何 [获取 session 的运行结果](session-output.html)
* 了解如何 [判断可用性和设备支持](session-assemble.html)

---

## 获取 session 的运行结果
- 章节路径: `unity/fundamentals/session-output.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-output.html

# 获取 session 的运行结果
session 运行过程中会修改场景中部分物体的 transform，以及修改摄像机的画面等。有些时候，这些修改还不满足应用的使用需要，可能需要获取 session 每帧的运行结果，并对这些数据进行二次处理。本文介绍了如何获取和使用这些结果数据。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
* 了解如何 [创建 session](session-creation.html)
* 了解如何 [访问 AR 功能组件](session-components.html)
## 获取 [InputFrame](../../../api/unity/easyar.InputFrame.html) 更新
可以使用 [InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 事件获取 [InputFrame](../../../api/unity/easyar.InputFrame.html) 的更新。这个事件仅在 session 每帧输出数据中 [InputFrame](../../../api/unity/easyar.InputFrame.html) 产生变化时触发。
> **注意**
[InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 只在由 EasyAR 进行画面绘制的 session 中有效。一般来说，使用 AR Foundation 或头显时是无效的，这时需要使用这些第三方库提供的方法获取数据更新。
使用 [InputFrame](../../../api/unity/easyar.InputFrame.html) 可以获取物理相机图像、相机参数、时间戳、物理相机相对于世界坐标系的变换和跟踪状态等。不过由于相机变换已经被 session 应用到虚拟摄像机和其它物体上，所以通常不需要通过 [InputFrame](../../../api/unity/easyar.InputFrame.html) 获取相机变换。
### 获取当前帧的物理相机图像
可以使用 [InputFrame.image()](../../../api/unity/easyar.InputFrame.html#u_easyar_InputFrame_image) 方法获取 [Image](../../../api/unity/easyar.Image.html) 类型的物理相机图像数据。
例如，下面这段代码可以在 [InputFrame](../../../api/unity/easyar.InputFrame.html) 更新时获取物理相机图像：
```
Session.InputFrameUpdate += (inputFrame) => {
using (var image = inputFrame.image())
{
}
};
```
> **小心**
使用 [Image](../../../api/unity/easyar.Image.html) 类型数据以及从它获取的其它 class 类型数据时，必需保证 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose) 被正确调用（上面代码中的 using 语句保证了这一点），否则会出现内存泄漏甚至画面停止更新等问题。
如需保留 [InputFrame](../../../api/unity/easyar.InputFrame.html) 或 [Image](../../../api/unity/easyar.Image.html) 到下一帧使用，需要根据保留的数据量增加 [ARAssembly.ExtraBufferCapacity](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_ExtraBufferCapacity) 的数值，否则可能会因为缓冲区不足而导致数据获取失败。
如需保留 [InputFrame](../../../api/unity/easyar.InputFrame.html) ，还需要调用 [Clone()](../../../api/unity/easyar.InputFrame.html#u_easyar_InputFrame_Clone) 方法创建一个引用副本，然后在不需要时对副本调用 [Dispose()](../../../api/unity/easyar.RefBase.html#u_easyar_RefBase_Dispose)。
由于物理相机的帧率通常低于渲染帧率，所以并不是每个渲染帧都能收到 [InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 事件，但同样的，物理相机画面渲染也并不是每个渲染帧都更新的。在 [InputFrameUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_InputFrameUpdate) 下次事件触发之前的所有渲染帧的画面内容都与当前 [InputFrame](../../../api/unity/easyar.InputFrame.html) 的图像一致。
> **注意**
[InputFrame](../../../api/unity/easyar.InputFrame.html) 中的图像一定是与当前帧虚拟摄像机背景画面一致的，但是背景画面渲染时可能经过缩放和裁切，所以获取的画面大小或比例与屏幕上显示的不一致是正常的。
另外需要注意的是，[InputFrame.image()](../../../api/unity/easyar.InputFrame.html#u_easyar_InputFrame_image) 返回的图像数据是 CPU 可读的，它不是 GPU 纹理。如果需要在 GPU 上使用图像数据，需要将图像数据上传到 GPU 纹理中，或者通过 [CameraImageRenderer.RequestTargetTexture(Action<Camera, RenderTexture>)](../../../api/unity/easyar.CameraImageRenderer.html#u_easyar_CameraImageRenderer_RequestTargetTexture_System_Action_UnityEngine_Camera_UnityEngine_RenderTexture__) 接口直接获取 GPU 纹理。
### [可选] 拦截物理相机图像渲染
可以使用 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 来控制物理相机图像的绘制。
下面这段代码可以停止物理相机图像的绘制：
```
if (Session.Assembly != null && Session.Assembly.CameraImageRenderer.OnSome)
{
Session.Assembly.CameraImageRenderer.Value.enabled = false;
}
```
需要注意的是，这里需要先判断 [ARAssembly.CameraImageRenderer](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_CameraImageRenderer) 是否存在。
> **注意**
只在由 EasyAR 进行画面绘制的 session 中，才能通过上面的方法停止画面更新。一般来说，使用 AR Foundation 或头显时是无效的，这时需要使用这些第三方库提供的方法来实现相应的功能。
停止物理相机图像绘制后，应用可以通过 [InputFrame](../../../api/unity/easyar.InputFrame.html) 获取物理相机图像数据，并使用这些数据进行自定义的绘制。
## 获取 transform 更新
可以通过 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件获取 session 每帧更新后场景中物体的 transform 数据。
> **注意**
对于部分功能（比如 Mega），即使图像没有变化也没有显示地请求服务更新，AR 计算也是每个渲染帧都在运行的。因此如果需要获取所有的 transform 变化，则必需每帧获取 transform 数据，而不能只在某些帧获取。
### 获取虚拟摄像机的 transform
可以通过 [ARAssembly.Camera](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_Camera) 获取场景中摄像机的 transform。
```
Session.PostSessionUpdate += () =>
{
var position = Session.Assembly.Camera.transform.position;
var rotation = Session.Assembly.Camera.transform.rotation;
};
```
### 获取 target 的 transform
可以通过在使用的具体 target 对象获取场景中 target 的 transform。比如，对于图像跟踪来说，这个 target 就是 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html) 组件所在的物体。
```
Session.PostSessionUpdate += () =>
{
var position = target.transform.position;
var rotation = target.transform.rotation;
};
```
### [可选] 获取 pose
pose 是一种描述物体位置和朝向的数据结构，通常由 position 和 rotation 两部分组成。在 AR 应用中，pose 通常用于描述物理相机或跟踪目标相对于某个参考系的位置和朝向。
Unity 中不提供原始的 pose 数据，因为pose 一般用于驱动场景中的物体运动，而这正是 session 自动完成的工作。对于内容计算和渲染来说，只需要 transform 就足够了。
> **重要事项**
在阅读下面的方法之前，请再思考一下，场景中摄像机、跟踪目标等物体的 transform 数据，是否已经满足需求？通常来说，额外的 pose 数据并不是必需的。
如果确实出于某种原因需要 pose 数据，可以在 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件中通过 transform 计算得到所需的 pose 数值。通常来说， [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 中获取到 target 与 camera 的相对 transform 就是 pose。
下面这段代码展示了如何获取 camera 和 target 的 transform，并计算它们之间的相对 pose：
```
Session.PostSessionUpdate += () =>
{
Pose cameraToWorld = new(Session.Assembly.Camera.transform.position, Session.Assembly.Camera.transform.rotation);
Pose targetToWorld = new(target.transform.position, target.transform.rotation);
Pose worldToTarget = new()
{
position = Quaternion.Inverse(targetToWorld.rotation) \* (-targetToWorld.position),
rotation = Quaternion.Inverse(targetToWorld.rotation)
};
Pose cameraToTarget = cameraToWorld.GetTransformedBy(worldToTarget);
};
```
> **小心**
如果您同时在使用 AR Foundation、头显或其它第三方库也在运行，这些库可能也会修改场景中摄像机的 transform。需要在确保这些库的更新逻辑完成之后再进行相关 pose 计算，否则计算结果可能不正确。在这样的场景下， [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 中 target 和 origin 的相对 pose 仍然是准确的。
### [可选] 拦截 transform 更新
AR 功能运行时，Unity 中的摄像机、跟踪目标等物体 transform 通常会被 session 自动更新。这些更新过程保证了 AR 渲染的正确性和一致性，所以没有任何方法可用拦截这些更新。
但是如果您需要自定义物体的 transform 更新逻辑，可以通过监听 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件来实现。这里需要使用一个比较繁琐的方法：
1. 虽然通常情况下，应该把渲染内容以子节点或附加组件的形式挂载在 session 控制的物体下，但是如果需要自定义更新物体的 transform，就需要把这些物体从 session 控制的物体层级中移除。也就是说，这些物体不应该是 session 控制物体的子节点。
2. 在 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件中，记录下想要自定义更新的物体的 transform。
3. 最后，在 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件中，根据 session 提供的数据，使用自定义逻辑更新这些物体的 transform。
> **注意**
使用 [PostSessionUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_PostSessionUpdate) 事件是必需的，因为只有在这个时间之后，session 才不会操作场景中的物体。
需要注意的是，这种方法不能用于修改 camera，需要更加复杂的逻辑来处理摄像机的自定义更新。
另外，这种方法只能用于自定义更新物体的 transform，不能用于修改 session 控制的物体的 transform。如果 session 控制的物体的 transform 被外部修改，session 仍然会在下一帧更新时覆盖这些修改，进而可能影响一些计算正确性。
> **小心**
使用这种方法需要您保证物体 transform 的正确性，否则可能会导致 AR 渲染错误。
如果您同时在使用 AR Foundation、头显或其它第三方库，这些库可能也会修改场景中物体的 transform。需要确保这些库的更新逻辑与自定义逻辑不会冲突，否则可能会导致不可预期的结果。
## 相关主题
* [中心模式](center-mode.html) 约束了 session 会驱动哪些物体的 transform 修改
* AR基础组件介绍
* [XR Origin](origin.html)
* [Target](target.html)
* [Camera](camera.html)

---

## 设备支持和 session 报告
- 章节路径: `unity/fundamentals/session-report.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session-report.html

# 设备支持和 session 报告
由于设备硬件和性能差异，AR 功能很多时候并不能在所有设备上运行。所以在使用 AR 功能时准确判断当前设备的支持情况是非常重要的。本文介绍了在 Unity 中，设备可用性是如何表达的，以及如何通过 session 报告（[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report)）获取设备支持和 session 可用性的信息。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程
## 设备支持、session 可用性与组装
每个 AR 功能可以支持的设备是不同的。比如运动跟踪对硬件元器件有一定要求且通常需要对设备进行标定，而图像跟踪功能则可以在几乎所有摄像头可用的设备上运行。所以判断一个 AR 应用是否可以在某个设备上运行，通常需要知道当前使用哪些 AR 功能，或者换个说法就是判断某个 session 是否可以在设备上运行。
在 Unity 中，上述判断过程是在 session 组装（[Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble)）阶段完成的。组装过程会根据 session 中包含的组件和当前设备的支持情况，决定 session 启动前的最终状态。
如果组装成功，session 会进入 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态，并可以继续启动和运行；如果组装失败，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，并且可以通过 session 报告（[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report)）查询具体的失败原因。
## session 报告
[ARSession.Report](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Report) 属性提供了 session 的运行报告，一份 session 报告包含以下字段：
|属性|描述|
|Availability|完整的可用性报告|
|BrokenReason|session 损坏原因，当 session 状态为 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 时有效|
|Exception|session 损坏具体异常，当 session 状态为 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 时有效|
在 session 报告中，可以通过 [Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 查询每个组件的可用性，或是通过 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 在 session 损坏时查询损坏的详细原因。
### 一份 session 报告示例
比如，在 Windows 上，如果 session 中包含 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html)、[CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 以及若干个其它 frame source 组件，那么组装过程会检查每个组件的可用性，并生成如下报告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-report-success.png)
可以看到图中虽然 [ARCoreFrameSource](../../../api/unity/easyar.ARCoreFrameSource.html) 组件的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 是 [Unavailable](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Unavailable)，但是由于 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 和 [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 都是是 [Available](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Available)，所以整个 session 的组装是成功的，且 session 成功进入了 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 状态。
如果我们把 [CameraDeviceFrameSource](../../../api/unity/easyar.CameraDeviceFrameSource.html) 从 session 中移除，那么组装过程会生成如下报告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-report-fail.png)
可以看到 [FrameSources](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_FrameSources) 列表数目从 9 变成了 8，并且虽然 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 组件的 [Availability](../../../api/unity/easyar.SessionReport.AvailabilityReport.Item.html#u_easyar_SessionReport_AvailabilityReport_Item_Availability) 仍然是 [Available](../../../api/unity/easyar.SessionReport.AvailabilityReport.AvailabilityStatus.html#u_easyar_SessionReport_AvailabilityReport_AvailabilityStatus_Available)，但是由于没有可用的 frame source 组件，所以整个 session 的组装失败，session 进入了 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态。此时报告中 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 字段数值是 [NoAvailabileFrameSource](../../../api/unity/easyar.SessionReport.SessionBrokenReason.html#u_easyar_SessionReport_SessionBrokenReason_NoAvailabileFrameSource)，表示没有可用的 frame source。
除了组装过程之外，session 运行过程中也可能出现损坏的情况，比如某个运行中的组件被意外移除等。此时同样可以通过 session 报告查询具体的损坏原因。
### 报告更新
session 报告会在以下时间点发生变化：
* 组装第一阶段完成
这时会生成一份完整的 session 报告，包含组件可用性报告。session 报告的 [Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 部分会在这时确定并不再变化。
可以通过 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告更新。
如果组装之后直接启动了 session，也可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告更新。需要关注的 session 的状态包括： [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 和 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。
* 组装第二阶段完成
这时会生成一份新的组件可用性报告。除非 session 重启，否则 session 报告不会更新。
可以通过 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件获取组件可用性报告更新。
* session 启动或运行过程中 session 损坏时
session 报告的 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 和 [Exception](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Exception) 会更新。
可以通过 [StateChanged](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StateChanged) 事件获取 session 报告更新。需要关注的 session 的状态包括：[Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken)。
### 报告内容：session 损坏的原因
[BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 表示 session 损坏的原因，有以下这些情况：
|原因|描述|
|Uninitialized|组装过程，EasyAR Sense 未成功初始化|
|LicenseInvalid|组装过程，EasyAR Sense license 验证失败或不适用于当前使用|
|SessionObjectIncomplete|组装过程，session 物体不完整。比如在 URP 中未正确配置 RendererFeature|
|NoAvailabileFrameSource|组装过程，无可用的 frame source。比如所有 frame source 都不可用或未添加任何 frame source。在且仅在默认 session 配置下，这种情况说明设备当前选择的 AR 功能的支持|
|FrameSourceIncomplete|组装过程，frame source 不完整。一般多出现在自定义 frame source 时未正确实现 frame source 接口|
|FrameFilterNotAvailabile|组装过程，存在不可用的 frame filter。这种情况只存在于部分组装选项下。|
|StartFailed|启动失败。比如启动过程中出现异常|
|RunningFailed|运行失败。比如运行中的组件被意外移除，或是 URP 中未正确配置 RendererFeature 等。|
### 报告内容：可用性信息
[Availability](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_Availability) 提供了 session 中每个组件的可用性信息。它包含以下字段：
|字段|描述|
|FrameFilters|组装过程检查过的 frame filter 可用性列表|
|FrameSources|组装过程检查过的 frame source 可用性列表|
|PendingDeviceList|未完成的设备列表下载任务|
|DeviceList|设备列表下载结果|
其中 [PendingDeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_PendingDeviceList) 和 [DeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_DeviceList) 字段用于表示设备支持列表的下载状态。组装第一阶段完成时，当且仅当 [PendingDeviceList](../../../api/unity/easyar.SessionReport.AvailabilityReport.html#u_easyar_SessionReport_AvailabilityReport_PendingDeviceList) 非空时，组装会进入第二阶段，可以使用这个条件来判断 [AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 是否会第二次执行。
## 后续步骤
* 尝试 [判断可用性和设备支持](session-assemble.html)

---

## Unity AR 的入口 —— AR Session
- 章节路径: `unity/fundamentals/session.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/session.html

# Unity AR 的入口 —— AR Session
AR 会话（session）是所有 AR 功能的入口，通过以下内容您将了解 AR Session 的基本概念、组成、运行流程以及它与 Unity AR Foundation 的 AR Session 有什么关系。您还会了解到在 Unity 中，EasyAR Sense 的数据流到底是如何工作的。
## AR Session 是什么
所有 AR 流程（例如物体跟踪）都是在原生库，即 EasyAR Sense 内部执行的。session 是 Unity 中 AR 功能的主要入口点。它管理 AR 系统的运行过程和状态，包括从物理相机和传感器中读取数据、分析真实世界、驱动场景中虚拟摄像机等其它部分物体的移动和渲染等。
```
flowchart LR
A((图像<br>和其它数据))
B[Session]
C([Camera])
O([Origin])
T([Target])
A --> B
B -. transform .-> C
B -. transform .-> O
B -. transform .-> T
```
### [可选] EasyAR 的 session 与 AR Foundation 的 session
EasyAR 的 session 是 Unity 中使用 EasyAR 的核心组件，可以独立于任何第三方或系统 AR 功能运行。而 [AR Foundation 的 session](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/manual/features/session.html) 是 Unity XR 框架的一部分，只能使用 Unity XR 插件（如 ARKit 或 ARCore）提供的功能。
```
flowchart TD
A1[EasyAR<br>AR Session]
A2[EasyAR Sense]
A1 --> A2
B1[AR Foundation<br>AR Session]
B2[ARKit Plugin]
B3[ARCore Plugin]
B1 --> B2
B1 --> B3
```
使用 EasyAR 时，通常并不需要同时安装和使用 AR Foundation。比如图像跟踪功能，运动跟踪功能等等，都是由 EasyAR Sense 独立提供的。
在某些情况下，可能需要将 EasyAR Sense 与 AR Foundation 结合使用，以利用 AR Foundation 提供的额外功能（比如在部分设备上的平面检测）和接口。在这种情况下，EasyAR Sense 通过 AR Foundation 提供的接口与 Unity 引擎进行交互。
但是，由于 EasyAR 提供了比系统 AR 更多的功能和更完善的设备适配，独立使用 AR Foundation 通常无法达到与 EasyAR 相同的效果。
## session 的组成
一个典型的 session 主要由以下部分组成：
* frame source：提供物理相机图像和传感器数据的组件，有时这些组件也会提供运动跟踪数据。比如 *CameraDeviceFrameSource* 和 *MotionTrackerFrameSource*
* frame filter(s)：提供特定AR功能的组件，比如 *ImageTrackerFrameFilter*
* camera：场景中的虚拟摄像机对象
* origin：运动跟踪的原点对象
> **注意**
在 AR Foundation 的概念中，运动跟踪被作为必选功能，因此它始终会提供一个 origin。
而在 EasyAR 系统中，运动跟踪是一个可选的功能，因此 origin 也是可选的。
### [可选] session 的数据流
[数据流](../../native/fundamentals/dataflow.html) 是 EasyAR Sense 的核心概念之一。它不影响您在 Unity 中开发 AR 应用。如果您想要更加深入地理解 session 的工作原理，可以阅读本节内容。
在 Unity 中，一个 session 通常表达了一个 EasyAR Sense 的数据流。
```
flowchart LR
S[Frame Source]
R[Input Frame Recorder<br>Video Input Frame Recorder]
ift[iFrameThrottler]
iff[iFrameFork]
i2f[i2FAdapter]
fb[fbFrameFork]
i2o[i2OAdapter]
FOT[Object Tracker]
FIT[Image Tracker]
FMT[Mega Tracker]
FSSM[Sparse Spatial Map]
FST[Surface Tracker]
FDS[Dense Spatial Map]
FCR[Cloud Recognizer]
ofj[oFrameJoin]
off[oFrameFork]
ofb[oFrameBuffer]
O(( ))
ODS(( ))
OCR(( ))
S ==> R ==> ift ==> iff
iff --> i2f
i2f --> fb
fb -.-> FOT -.-> ofj
fb -.-> FIT -.-> ofj
iff ==> i2o ==> ofj ==> off ==> ofb ==> O
iff -.-> FMT -.-> ofj
iff -.-> FSSM -.-> ofj
iff -.-> FST -.-> ofj
iff -.-> FDS -.-> ODS
iff -.-> FCR -.-> OCR
off --> i2f
ofb --> ift
```
这个数据流是在 session 启动过程中创建的，图中除加粗数据通路外，其它部分是否连接取决于启动过程中启用的 AR 组件。
因此，通过修改 session 中启用的组件，可以灵活改变数据流的结构和功能，也可以很方便地同时启用多个 AR 功能。而这个方法将在接下来的段落中详细介绍。
## session 的流程
```
flowchart LR
i[初始化<br>Initialize]
a[组装<br>Assemble]
starta["启动（已组装的）<br>StartSession(Assembled)"]
start[启动<br>StartSession]
update((更新<br>update))
stop[停止<br>StopSession]
di[反初始化<br>Deinitialize]
i --> a --> starta --> update --> stop --> di
i --> start --> update
```
* 初始化
初始化是使用使用 license key 启动 EasyAR Sense 的过程，在初始化之前，只有极少部分 EasyAR Sense 的接口可以使用。初始化之后，AR 功能才会被激活。
* 组装（Assembling）
组装过程会根据组装选项的配置，从场景中挑选合适的组件，并将它们连接成一个整体工作单元。这个过程通常是在启动时自动完成的，但也可以在启动之前手动调用组装接口来完成这个过程。组装完成后，可以通过启动已组装的 session 来跳过组装过程，从而加快启动速度。
组装过程还有一个重要的用途就是判断AR组件以及输入源的可用性，并在所有候选输入中选择最合适的输入源。这一步骤也可以用来判断当前 session 是否可以在当前设备上运行。
组装过程分成两个阶段
1. 第一阶段会启动设备支持列表更新并根据配置等待固定时间后开始组装。如果在第一阶段等待后设备支持列表已经更新完成，那么组装过程就结束了；
2. 否则组装过程会进入第二阶段，第二阶段会在设备支持列表更新完成后执行。在这一阶段中，如果可用 frame source 从第一阶段的没有可用 frame source 变成了存在可用 frame source，且 session 在第一阶段之后启动失败，则会尝试重新启动 session。
无论第一阶段设备列表是否完成更新，session 都会在第一阶段完成后继续执行后续步骤。
3. 启动
启动是开始 AR 功能运行的过程。在启动之前，AR 功能组件不会处理任何数据。正常启动之后，session 会开始控制场景中的部分物体移动，并在使用部分输入源时控制物理相机图像的渲染。
4. 更新
更新过程在 Unity 的渲染循环的每帧执行。更新过程会根据当前使用的AR功能的运行结果，每帧修改虚拟摄像机（部分输入源）、原点以及跟踪目标的 transform。不同设备上更新过程的执行时间点并不是相同的，但一定会在渲染之前执行。
5. 停止
停止会终止 AR 功能的运行，场景中的物体将不再被 session 控制，输入源的数据也不会被处理。
6. 反初始化
反初始化会释放部分全局资源（不会卸载动态库）。反初始化之后，AR 功能组件将无法使用。
> **注意**
所有 AR 功能只能在 ARSession.StartSession 之后使用。
## session 的默认生命周期
```
flowchart LR
uload("BeforeSceneLoad")
ustart("MonoBehaviour.Start")
udestroy("MonoBehaviour.OnDestroy")
oi{Initialize<br>OnStartup}
ostart{AutoStart}
i[初始化<br>Initialize]
start[启动<br>StartSession]
update((更新<br>update))
stop[停止<br>StopSession]
uload -.-> ustart -.-> udestroy
uload --> oi -. true .-> i
ustart --> ostart -. true .-> start
udestroy --> stop
i --> start --> update --> stop
```
session 的生命周期一般由接口调用的时间决定。采用默认设置时，session 会在以下时间点自动执行：
* 初始化（[EasyARSettings.InitializeOnStartup](../../../api/unity/easyar.EasyARSettings.html#u_easyar_EasyARSettings_InitializeOnStartup) == `true`）
自动初始化会在 Unity 的 [BeforeSceneLoad](https://docs.unity3d.com/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) 时间点执行。
* 启动（[ARSession.AutoStart](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AutoStart) == `true`）
自动启动会在 session 的 [MonoBehaviour.Start()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html) 时间点执行。
* 停止
自动停止会在 session 的 [MonoBehaviour.OnDestroy()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnDestroy.html) 时间点执行。
## session 状态
ARSession.State 描述了 session 的状态。一个 session 有以下几种状态：
|状态|描述|
|None|初始状态，session 未启动或组装|
|Broken|组装失败等原因 session 被破坏|
|Assembling|在组装过程中，组装过程通常可能持续几帧|
|Assembled|成功完成组装，但尚未启动|
|Ready|session 成功启动，这个状态只会持续一帧|
|Running|session 在运行中|
|Paused|session 暂停运行|
通常 session 的状态会在调用启动和停止等接口时发生变化。运行过程中，如果出现严重错误，session 也可能进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态。进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态的 session 无法恢复运行，必需调用停止后重新启动。
可以通过 session 的状态了解当前 session 是否出于可用状态。绝大多数功能只有在 [Ready](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Ready) 或 [Running](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Running) 状态下才能使用。
## 运动跟踪状态
ARSession.TrackingStatus 描述了 session 的运动跟踪跟踪状态，它表示设备运动跟踪的质量，有这几种状态：
|状态|描述|
|Optional<MotionTrackingStatus>.Empty|运动跟踪功能未启用或 session 未运行|
|NotTracking|运动跟踪结果不可用，原因可能是正在初始化，跟踪丢失或者正在重定位|
|Limited|运动跟踪是有效的，但是结果不太好，原因可能是当前区域纹理太弱或运动过快|
|Tracking|运动跟踪质量好|
> **注意**
在 AR Foundation 的概念中，运动跟踪被作为必选功能，因此它的跟踪状态与 session 状态合并在了一起。
而在 EasyAR 系统中，运动跟踪是一个可选的功能，因此跟踪状态是独立存在且可能为空的。
## 其它 AR 功能的跟踪状态在哪
由于 AR 功能可能同时跟踪复数个对象，因此图像跟踪状态和其它 AR 功能的跟踪状态并不在 session 中，而是在跟踪目标组件中。
可以使用 TargetController.IsTracked 了解跟踪目标是否出于跟踪状态，或使用 TargetController.TargetFound 和TargetController.TargetLost 事件在跟踪状态变化时调整应用内容逻辑。
## 后续步骤
创建
* 尝试在场景中 [创建 session](session-creation.html)
控制运行
* 了解 [初始化](initialization.html) 的方法和作用
* 了解如何 [判断可用性和设备支持](session-assemble.html)
* 了解 [控制 session 执行](session-ctrl.html) 的方法
访问组件和结果
* 尝试 [访问 AR 功能组件](session-components.html)
* 了解如何 [获取 session 的运行结果](session-output.html)
组件参考
* [ARSession](comp-ARSession.html) 组件参考
在动手开发之前，您可以通过这些方法快速尝试修改 session 的工作流程并观察产生的变化：
* 尝试 [session 验证工具](../simulation/tool.html)，在编辑器上测试 session 的工作流程
* 尝试在不同平台上运行 [Workflow\_ARSession 示例](sample-arsession.html) ，了解组件可用性以及 session 组成和流程的差异
了解更多AR基础组件
* [XR Origin](origin.html)
* [Target](target.html)
* [Camera](camera.html)
了解 session 在场景中修改了哪些物体的属性
* 了解 [设备支持和报告](session-report.html)
* 了解 [中心模式](center-mode.html) 以及不同模式下物体的运动差异
了解 session 启动过程中做了什么
* 了解 [帧数据源及运行时选取](../cameras/frame-source.html)
了解如何在 EasyAR 场景中使用 Unity XR 框架和 AR Foundation
* 查看 [Unity XR 框架和 AR Foundation](unity-xr.html) 的使用方法和注意事项
如果您想了解更多关于 EasyAR Sense 的数据流，可以参考以下资源：
* [数据流](../../native/fundamentals/dataflow.html)

---

## EasyAR 配置
- 章节路径: `unity/fundamentals/setup-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/setup-easyar.html

# EasyAR 配置
EasyAR 配置页面可以从 Unity 菜单 `EasyAR > Sense > Configuration` 或 `Edit > Project Settings > EasyAR` 进入。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
这里包含所有对 EasyAR Sense Unity Plugin 的全局配置
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/settings-easyar.png)
## Initialize On Startup
在启动时初始化 EasyAR。通常建议保持这个选项打开。
如果关闭该选项，需要手动初始化 EasyAR Sense，具体方法可以参考 [初始化 EasyAR Sense](initialization.html) 。
## EasyAR Sense License
EasyAR Sense License 相关配置。
### LicenseKey
EasyAR Sense License Key。使用 EasyAR 功能必须填写可用的 license。
仅当使用接口手动初始化 EasyAR Sense 时可留空。
> **注意**
在头显设备（Vision Pro、XREAL、Pico、Rokid 等）设备上使用时，需要使用 EasyAR XR License。
> **注意**
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
### Verify When Build
在构建 Unity 工程时验证 license Key。
当这个选项打开时，Unity 项目构建过程会验证 license Key，如果 license 在构建平台上无效或不包含 Unity Player Settings 中设置的包名，构建过程将会失败。如果需要使用其它地方配置的 license key 或者需要在 Unity 构建过程之后修改包名，可以关闭这个选项。
## Lib Variants
EasyAR Sense 库变种配置。
## EasyAR Sense License
EasyAR Sense License 相关配置。
### LicenseKey
EasyAR Sense License Key。使用 EasyAR 功能必须填写可用的 license。
仅当使用接口手动初始化 EasyAR Sense 时可留空。
> **注意**
在头显设备（Vision Pro、XREAL、Pico、Rokid 等）设备上使用时，需要使用 EasyAR XR License。
> **注意**
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
### Verify When Build
在构建 Unity 工程时验证 license Key。
当这个选项打开时，Unity 项目构建过程会验证 license Key，如果 license 在构建平台上无效或不包含 Unity Player Settings 中设置的包名，构建过程将会失败。如果需要使用其它地方配置的 license key 或者需要在 Unity 构建过程之后修改包名，可以关闭这个选项。
## Permissions
应用权限配置。通常建议保持默认。
除相机权限外，其它权限配置不可更改，由其它功能配置所决定。
|权限|是否可改|启用条件|权限说明|
|`Camera`|是||相机权限，使用相机设备需要的权限|
|`AndroidMicrophone`|否|Variant 为 VideoRecording|麦克风权限，使用录屏功能需要的权限|
|`Location`|否|导入 Mega 支持包|（fine）定位权限，使用 EasyAR Mega 需要的权限|
## Unity XR
Unity XR 框架（AR Foundation 等）相关配置。
### AR Foundation Support
AR Foundation 支持开关，建议保持打开。
在极个别情况下，比如需要使用 AR Foundation 4 或 AR Foundation 更新导致编译出错，可以关闭这个选项，但插件内所有与 AR Foundation 相关的功能将同时禁用。
> **注意**
修改此选项之后脚本会自动重新编译。
### Unity XR Auto Switch
自动切换 Unity XR（比如 AR Foundation）物体的功能配置。
* `Editor` ：编辑模式选项
* `Disable AR Session` ：存在 [ARSession](../../../api/unity/easyar.ARSession.html) 时，编辑时禁用 AR Foundation 的 ARSession。
* `Player` ：运行模式选项
* `Enable` ：启用运行时控制。注意：关闭该选项，编辑模式被禁用的组件在运行时不会被恢复。
* `Enable If Desktop` ：在 Windows/Mac 上启用。
* `Enable If Mobile AR On Startup` ：切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。通常这个选项需要 XR Plug-in Management 中的 `Initialize XR on Startup` 是选中的。
* `Disable If Non Mobile AR Post Startup` ：切换器启动时，如果存在移动 AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。通常这个选项会在 XR Plug-in Management 中的 `Initialize XR on Startup` 未选中时被使用。
* `Restore AR Session When Disabled` ：功能禁用时，恢复（启用）所有被禁用的 AR Foundation 的 ARSession（无论它是否由 EasyAR 所禁用）。这个选项通常用于恢复编辑时被禁用的组件。
详细功能说明可参考 [Unity XR 自动切换](unity-xr-switch.html) 。
## Mega
EasyAR Mega 功能配置。
### InertialCameraDevice Support
只读选项，显示当前配置下惯导功能是否可用以及 ONNX 运行时信息。
如果显示信息不符合需求，需要视情况修改 `Lib Variants` 以及 `ONNX Runtime (Bundled)` 选项。
### Mega Block > Localization Service Access [Global]
全局 Mega Block 定位服务器配置。
### Mega Landmark > Localization Service Access [Global]
全局 Mega Landmark 定位服务器配置。
## Spatial Map
EasyAR 空间地图功能配置。
### Service Access [Global]
全局稀疏地图服务器配置。
## Image Tracking
EasyAR 图像跟踪功能配置。
### Target Gizmo
编辑器下 ImageTarget 的 Gizmos 配置。
打开这些选项将会在 Unity Editor 中显示对应 gizmo，如果场景中该类 target 过多，可能会影响编辑器中的启动性能。在设备上运行时的性能不会受到影响。
* `Enable Image File` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.ImageFileSourceData](../../../api/unity/easyar.ImageTargetController.ImageFileSourceData.html) 的 target 的 Gizmos。
* `Enable Target Data File` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.TargetDataFileSourceData](../../../api/unity/easyar.ImageTargetController.TargetDataFileSourceData.html) 的 target 的 Gizmos。
* `Enable Target` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.TargetSourceData](../../../api/unity/easyar.ImageTargetController.TargetSourceData.html) 的 target 的 Gizmos。
* `Enable Texture 2D` ：开启 [ImageTargetController.Source](../../../api/unity/easyar.ImageTargetController.html#u_easyar_ImageTargetController_Source) 类型为 [ImageTargetController.Texture2DSourceData](../../../api/unity/easyar.ImageTargetController.Texture2DSourceData.html) 的 target 的 Gizmos。
### Cloud Recognition (CRS) > Service Access [Global]
全局云识别服务器配置。
## Object Tracking
EasyAR 物体跟踪功能配置。
### Target Gizmo
编辑器下 ObjectTarget 的 Gizmos 配置。
* `Enable`：开启 Gizmos。
## Third-Party Libraries
第三方库配置。
### ARCore SDK
ARCore SDK 配置。
ARCore 提供了在部分 Android 设备上的运动跟踪能力，可以阅读 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 来了解 EasyAR 功能与运动跟踪的关系，以及是否需要和什么时候需要使用 ARCore。
* `AR Foundation Or Optional`: 随 EasyAR 或 `AR Foundation` 一起分发的 ARCore SDK 将会被包含在应用中，根据 ARCore XR Plugin 的设置决定。一般情况下推荐使用这个选项，它会自动处理 `AR Foundation` 的情况。
* `Optional`: ARCore 功能在支持 ARCore 并安装了 Google Play Services for AR 的设备上可以使用。
* `Required`: 应用将只能在支持 ARCore 并安装了 Google Play Services for AR 的设备上运行。
* `External`: 如果在使用 `AR Foundation` 或其它 ARCore SDK 分发，可以使用这个选项。这样随 EasyAR 一起分发的 ARCore SDK 将不会使用。也可以使用这个选项来完全排除 ARCore SDK 在应用中的使用。
> **小心**
如果把 `ARCore SDK` 设置为 `Required`，或是在 AR Foundation 的 ARCore 配置中将 `Requirement` 设置为 `Required`，并在不支持 ARCore 的设备上安装了打包后的应用，设备会错误地报告 ARCore 是可用的并以 ARCore 运行。这会造成一个假象，似乎这些设备正在运行 ARCore 并且运行不正常（黑屏或其它异常情况），但这是错误的。
出现这个现象的原因是由于 Google Play 商店阻止在不受支持的设备上安装标记 ARCore 为必需的应用，所以这些应用总是假设它们正在受支持的设备上运行。
正常配置下，这些设备会在 session 组装时判断 ARCore 不受支持并使用 EasyAR 的功能。
关于 `Optional` 和 `Required` 的详细说明及上线 Google Play Store 应用需要做的其它配置可以参考 Google 的说明（[中国大陆](https://developers.google.cn/ar/develop/java/enable-arcore)，[国际](https://developers.google.com/ar/develop/java/enable-arcore)）。
> **注意**
在 EasyAR Sense Unity Plugin 中，ARCore 的支持所需的库文件和配置已经在插件包中，但要在手机上运行，仍需在手机上安装 [Google Play Services for AR](https://play.google.com/store/apps/details?id=com.google.ar.core) 。
有三种不同来源的 ARCore SDK 可以使用：
* 使用随插件分发的 ARCore SDK
插件内集成了一个 ARCore SDK 版本，详细信息可以参考 [ARCore、AR Engine 版本兼容性](../motion-tracking/3rdparty-compatibility.html)。在使用 EasyAR 的 ARCore 封装时，可以不另外导入 AR Foundation。
* 使用 AR Foundation 的 ARCore SDK
如果需要使用 AR Foundation 的 ARCore SDK，可以参考 Google 的说明（[中国大陆](https://developers.google.cn/ar/develop/java/enable-arcore)，[国际](https://developers.google.com/ar/develop/java/enable-arcore)）进行配置，这时 `ARCore SDK` 选项需要选择 `AR Foundation Or Optional` 或 `External` 。
* 使用其它 ARCore SDK
如果有其它第三方插件或项目内有 ARCore SDK 的分发，也可以使用这些 ARCore SDK。这时 `ARCore SDK` 选项需要选择 `External` ，并根据具体插件或项目的要求进行配置。
**Warn 32-bit-only ARCore-enabled build**
根据 Google 的说明，在 arm64 的设备上运行仅有 armv7 库文件的程序，ARCore 不会正常工作。在打包时如果未选择 ARM64 会弹出警告：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/settings-arcore-warn.png)
这时需要修改项目配置，使用 IL2CPP 编译并选择 ARM64 支持。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/adnroid-64bit.png)
> **小心**
如确有需要，可以选择 `Continue and don't warn me again`，或者关闭该选项，这将关闭打包时的检查。关闭检查只是在打包时不弹出提示，但运行时在一些设备上将有可能出现异常，包括但不限于崩溃或黑屏等。
### AR Engine SDK
AR Engine SDK 配置。
AR Engine 提供了在部分 Android 设备上的运动跟踪能力，可以阅读 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 来了解 EasyAR 功能与运动跟踪的关系，以及是否需要和什么时候需要使用 AR Engine。
* `AREngineInterop` ：AREngineInterop 可用。随 EasyAR 一起分发的 AR Engine SDK 将会被包含在应用中。
* `External` ：AREngineInterop 可用。随 EasyAR 一起分发的 AR Engine SDK 将不会使用。
* `Disabled` ：AREngineInterop 不可用。随 EasyAR 一起分发的 AR Engine SDK 将不会使用。所有与 AR Engine 有关的功能将被禁用。
### ONNX Runtime (Bundled)
是否使用捆绑的 ONNX 运行时。仅在 `Lib Variant` 为 `Full` 时有效。
如需使用不同版本的 ONNX，可用从 ONNX 官方获取更新版本并关闭该选项。使用自己编译的二进制不兼容的 ONNX 将导致未知错误。
## Workaround For Unity
针对 Unity bug 或不合理行为的应对方案。
### GenerateXMLDoc
在脚本重新加载时生成 XML 文档，以使 API 文档的 intelliSense 可以工作。
### URP17RG\_DX11\_RuinedScene
Workaround URP 17 Render Graph DX11 场景渲染被毁损。Unity 6.2 及更新版本中该选项已关闭。
### URP17RG\_IOS\_Glitches\_Partial
部分规避 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture)。
问题简述：当从 EasyAR 获取相机纹理（类似 ImageTracking\_Coloring3D示例 及 [ARSession 工作流（CameraDevice）](../cameras/sample-camera-device.html) 示例中的使用），在 iOS/Mac 设备上可以观察到视觉故障和伪影。我们已经在纯 Unity 包中复现该问题并报告给了 Unity： [Glitches on iOS with AR Camera Image Rendering (URP 17 render graph)](https://discussions.unity.com/t/glitches-on-ios-with-ar-camera-image-rendering-urp-17-render-graph/1548048) 。问题进展可以关注 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 更新以及 Unity 未来版本的发布日志。

---

## Player 配置
- 章节路径: `unity/fundamentals/setup-player.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/setup-player.html

# Player 配置
本文介绍在 Unity 中使用 EasyAR Sense Unity Plugin 打包应用时需要注意的 Player 配置选项。
## 不同平台配置说明
在 Unity 打包时，需要检查并确认下列配置。
依次在 Unity 菜单 `File -> Build Settings-> Player Settings`，点击安卓图标，调出 Android平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
通常情况下需要设置以下选项。
* Package Name
设置 Android 应用的 `Package Name`, **注意 `Package Name` 要与创建 License Key 时填写的必须一致**。
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
* API Level
EasyAR 支持的 `API level` 与使用的版本有关， 使用 `Full` 变种时，需要 `Android API Level 24` 或以上; 使用其他变种时，EasyAR Sense 需要 `Android API Level 21` 或以上。
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* Target Architecture
如果需要使用 Google ARCore ，或其它情况需要编译支持 ARM64 ，需要使用 `IL2CPP` 编译并选择 `ARM64 支持`。在不需要支持 ARM64 架构的情况下无需配置。
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/adnroid-64bit.png)
* 视频录制功能的特殊配置
如果要使用视频录制功能，需设置 `Graphics API` 为 `OpenGLES3` 或 `OpenGLES2`，并去掉 `Multithreaded Rendering` 的勾选。另外还需要在 EasyAR 配置 中将 `Lib Variants > Android` 设为 `VideoRecording` 。
![androidvideorecord](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-video-recording.png)
依次在 Unity 菜单 `File -> Build Settings-> Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
通常情况下需要设置以下选项。
* Bundle ID
设置 iOS 应用的 `Bundle ID`, 注意 `Bundle ID` 与创建 License Key 时填写的**必须一致**。
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
* Target Architecture
在 `Player Settings` 中修改 `architecture` 为 `ARM64`, 不可使用 `Universal`。
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* Usage Description配置
根据 EasyAR 配置 中 Permissions 中的启用情况，需要配置不同的 Usage Description。
* 如果 `Camera` 权限开启，需要添加 `Camera Usage Description`，否则构建将失败。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-camera-permission.png)
* 如果 `Location` 权限开启，需要添加 `Location Usage Description`，否则构建将失败。
![ioslocationpermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-location-permission.png)
* 需要 EIF 录制的额外配置（XCode 工程，需要时）
若需要录制 EIF 到默认目录并通过 iOS 的文件应用投送到电脑或其他设备，需要在 `Info.plist` 中增加 `UIFileSharingEnabled` 并将值设置为 `true`。
![iosstore](https://doc-asset.easyar.com/develop/unity/fundamentals/media/ios-plist-uifilesharingenabled.png)
## 常见问题
下面是与Player 配置相关的一些常见错误和解决方案。
* License Key 异常的报错
如果 License Key 异常（比如 `Package Name` 不匹配），在打包应用时将会类似 `is not a valid EasyAR Sense license key or it does not match package name `。这时如果选择继续打包，打包出的应用将无法正常使用，请根据窗口提示仔细检查并修复问题后再继续打包。
* 关闭打包时的许可证检查
在一些特殊情况，如果你使用 EasyAR 的接口手动初始化，不使用 `Setttings` 文件中的 `License Key`，你可以选择 `Continue and don't warn me again` ，或者关闭 EasyAR 配置 中的 `EasyAR Sense License > Verify When Build` 选项，这将关闭打包时的检查。
* 非 ARM 架构的 Android 设备支持
EasyAR Sense 不直接支持 x86 及 x86-64 架构的 Android 系统，但是一般x86架构的设备芯片可以兼容 ARM 程序，因此需要配置取消选择 x86 架构，这样在一些 x86 设备上可以正常使用。

---

## 获取 target 的状态
- 章节路径: `unity/fundamentals/target-state.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/target-state.html

# 获取 target 的状态
session 运行过程中，target 会经历跟踪和丢失等状态变化。通过以下内容，您将了解如何获取和使用 target 的状态信息，以及如何使用 found 和 lost 事件来控制内容的显示。
## 开始之前
* 通过 [ARSession 简介](session.html) 了解 session 的基本概念、组成和工作流程。
* 通过 [Target](target.html) 了解 target 的基本概念、状态和生命周期。
## 判断 target 是否被跟踪
可以使用 [TargetController.IsTracked](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_IsTracked) 属性判断 target 是否被跟踪。
## 使用 target 的 found 和 lost 事件
可以使用 [TargetController.TargetFound](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetFound) 和 [TargetController.TargetLost](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetLost) 事件来处理 target 被跟踪和丢失的情况。
比如，下面的代码展示了在 target 被跟踪时播放视频，并在 target 丢失时暂停视频播放的过程：
```
target.TargetFound += () =>
{
if (player && player.gameObject.activeInHierarchy)
{
player.Play();
}
};
target.TargetLost += () =>
{
if (player && player.gameObject.activeInHierarchy)
{
player.Pause();
}
};
```
> **小心**
如果没有手动卸载 target，[TargetController.TargetLost](../../../api/unity/easyar.TargetController.html#u_easyar_TargetController_TargetLost) 有可能在 session 停止时被调用。如果没有手动停止 session，则它可能在 session 的 OnDestroy 过程中被调用，由于 Unity 的 OnDestroy 执行顺序是不受保证的，所以在事件中使用的对象需要进行有效性检查以避免在 OnDestroy 过程中访问已经被销毁的对象。
## 后续步骤
* [active 控制策略](active-control.html) 介绍了 target 下物体的默认显示和隐藏策略，以及如何根据需要进行调整。

---

## Unity AR 的跟踪目标 —— target
- 章节路径: `unity/fundamentals/target.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/target.html

# Unity AR 的跟踪目标 —— target
target 在 Unity 中表达了各种可跟踪的物体。通过以下内容，您将了解 Unity AR 中的跟踪对象 target 的基本概念、状态和生命周期。
## 开始之前
* 通过 [ARSession 简介](session.html)了解 session 的基本概念、组成和工作流程。
## target 是什么
target 是指那些被 AR 功能识别和跟踪的物体在 Unity 中的代表。真实世界中这些物体可以是图像、3D 物体、空间地图等。通过识别和跟踪这些物体，AR 应用可以在现实世界中叠加虚拟内容，实现丰富的交互体验。
有些 target 在现实世界中是静止的（比如墙上的海报）。
>
> 这段视频展示了一个简单的运行了图像跟踪的 AR 场景。视频左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图。视频是使用模拟运行数据，在 Unity 编辑器的
`> Play
`> 模式录制的。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。在这段视频里，target（
[> ImageTarget
](../../../api/unity/easyar.ImageTarget.html)> ）代表了现实世界中的名片。我们在其上方放置一个黄色球体标识便于观察它的运动。
>
> 可以看到，target 在现实世界和场景中的位置都是固定的，而代表用户的摄像机（蓝色锥体）会根据用户在现实世界中的移动而移动。白色锥体截取了过去一段时间内摄像机的位置和朝向轨迹。可以看到黄色球体是在 target （
[> ImageTarget
](../../../api/unity/easyar.ImageTarget.html)> ）节点下的，这也是这类场景中物体的典型组织结构。
>
有些 target 在现实世界中是可以移动的（比如公交车上的海报）。
>
> 这段视频展示了同样的场景，不过这次我们在现实世界中移动了 target（名片）。可以看到，target 移动后，黄色球体会跟随名片进行运动，而
`> Game
`> 视图中该球体标识仍然贴合在名片之上。
>
为了便于理解，上面两个视频中关闭了 [ImageTarget](../../../api/unity/easyar.ImageTarget.html) 的 gizmo 的显示，并且都采用了 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式，这两段视频中 `Scene` 视图中物体的运动与真实世界中相同。在实际的 AR 场景中，这种运动关系要更加复杂一些。
## target 在不同中心模式下的行为
在 Unity 中，所有 AR 跟踪的中心参考点被称为 session 中心，而 session 运行过程中决定这个中心的规则被称为中心模式。在不同的中心模式下，target 的行为有所不同：
* **在 [SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 中心模式下，target 是不能随意移动的。**
[SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin) 模式只能存在于有运动跟踪的场景中。
虽然这个模式在前面的简单场景中可以很好地展示 target 和摄像机在现实中的运动，但在实际的 AR 场景中并不常用，因为在这个模式下，session 会控制 target 的运动，且由于运动跟踪或是 AR 功能本身的计算误差，很难保证 target 是完全固定不动的。这时内容根节点就要跟随 target 进行运动，在 Unity 系统中会对内容行为（比如物理系统）产生一些影响。
* **在 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 中心模式下，如果 target 正好是被选作中心的物体，那它是可以随意移动的。**
一般 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 模式是比较常用的，它能保证第一个被跟踪的物体在场景中是不会被 session 控制的，如果没有移动 target 的需求，那它就是固定不动的，无论现实场景中对应的物体是否在运动。
* **在 [FirstTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_FirstTarget) 或 [SpecificTarget](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SpecificTarget) 中心模式下，如果 target 不是被选作中心的物体，以及在 [Camera](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_Camera) 中心模式下，target 是不能随意移动的。**
一般在同时跟踪多个物体时，即使在现实环境中这些物体是相对固定的，但是由于计算误差的存在，同一时间也只能有一个 target 是不受 session 控制的。这时根据配置不同，其它 target 的运动与否是不受保证的，即使现实中没有运动，场景中也可能会有微小的运动。应该充分考虑到多个物体同时跟踪时的这个行为，并合理调整内容策略。
关于中心模式以及场景内物体的运动方式可以详细参考： [中心模式](center-mode.html) 。
## target 的状态
target 的状态反映了 target 在当前 session 中的识别和跟踪情况。常见的状态包括：
* **被跟踪（Tracked）**：target 已被成功识别和跟踪，AR 应用可以在其上叠加虚拟内容，内容会贴合真实世界中的物体。
* **未被跟踪（Not Tracked）**：target 当前未被识别或跟踪，如果 AR 应用仍然在其上叠加虚拟内容，则内容不会贴合真实世界中的物体。
同时，在状态变化时，可以通过这些事件进行响应：
* **TargetFound**：当 target 被成功识别和跟踪时触发。
* **TargetLost**：当 target 失去跟踪状态时触发。
## target 的生命周期
在 Unity AR 场景中，target 通常由对应的 frame filter 组件进行管理。frame filter 会处理来自 frame source 的图像数据，并识别和跟踪其中的 target。而 frame filter 的生命周期则依托于 session。虽然不同 AR 功能实现上可能会有差异，但大部分情况下，在 session 启动时，target 会被加载，并在加载后受控于 session。在 session 停止时，target 会被卸载并留在原地直至被下一个 session 使用或被手动删除。
## 后续步骤
* 尝试 [获取 target 状态](target-state.html)
* 尝试在各种 AR 功能中使用对应的 target
* [Mega](../mega/target.html)
## 相关主题
* [中心模式](center-mode.html)
* [XR Origin](origin.html)

---

## Unity 兼容性
- 章节路径: `unity/fundamentals/unity-compatibility.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-compatibility.html

# Unity 兼容性
本文介绍 EasyAR Sense Unity Plugin 所兼容的 Unity 版本和配置要求。
## Unity 版本
EasyAR Sense Unity Plugin 支持 **Unity 2021.3** 或更高版本。
开发 Mega 功能所需的 EasyAR Mega Studio 支持 **Unity 2021.3.30** 或更高版本。
> **提示**
通常来说, EasyAR 不依赖很多变化的 Unity API，所以如果 Unity 发布了新版本，EasyAR Sense Unity Plugin 一般都可以正常使用。
EasyAR Sense Unity Plugin 从版本 4.6.4 开始支持 Unity 6 的 URP 17+ Render Graph。
## 开发平台
|操作系统|操作系统版本|CPU 架构|补充说明|
|**Windows**|7 及以上版本（7/8.1/10/11）|x86, x86\_64|Windows N/KN 版本需要安装 Media Feature Pack 才能使用|
|**macOS**|10.15 及以上版本|x86\_64, arm64||
另外，需要满足对应版本的 [Unity 开发系统要求](https://docs.unity3d.com/Manual/system-requirements.html) 。
## 发布平台
|操作系统|操作系统版本|CPU 架构|补充说明|
|**Windows**|7 及以上版本（7/8.1/10/11）|x86, x86\_64|Windows N/KN 版本需要安装 Media Feature Pack 才能使用|
|**macOS**|10.15 及以上版本|x86\_64, arm64||
|**Android**|5.0 及以上版本|armv7a, arm64-v8a|arm64-v8a 支持需要开启 IL2CPP|
|**鸿蒙（手机端）**|1.0 – 4.x 原生支持
5 以上通过 Android 应用兼容层支持|arm64-v8a||
|**iOS**|12.0 及以上版本|arm64|Architecture 需配置为 ARM64，不支持配置为 Universal|
|**visionOS**|2.0 及以上版本|arm64||
另外，需要满足对应版本的 Unity 的发布平台要求：
* [Windows](https://docs.unity3d.com/Manual/windows-requirements-and-compatibility.html)
* [macOS](https://docs.unity3d.com/Manual/macos-requirements-and-compatibility.html)
* [Android](https://docs.unity3d.com/Manual/android-requirements-and-compatibility.html)
* [iOS](https://docs.unity3d.com/Manual/ios-requirements-and-compatibility.html)
* [visionOS](https://docs.unity3d.com/Manual/visionOS.html)
特殊说明：
* **关于 Mac Apple silicon：**
EasyAR Sense Unity Plugin 支持在 Apple silicon 设备上原生运行，且可以在 Unity 编辑器中正常使用。
由于 Unity 对原生插件支持的 bug，在部分 Unity 版本中，为 *"Apple silicon"* 或 *"Intel 64-bit + Apple silicon"* 构建的应用可能无法正常工作。如果发现应用在 Mac 上无法使用，且显示类似 "Fail to load EasyAR library" 或 "DllNotFoundException: EasyAR assembly" 的错误，建议使用新版本的 Unity 或向 Unity 和 Unity 社区寻求帮助。
* **关于 Android 16 KB 内存页面大小支持：**
EasyAR Sense Unity Plugin 从版本 4000 开始支持具有 16 KB 内存页面大小的设备。
这是 Android 15 中引入的功能。有关该功能的更多信息，请参阅 Android 文档中关于[支持 16 KB 页面大小](https://developer.android.com/guide/practices/page-sizes)的内容。
* **关于 WebGL：**
EasyAR Sense Unity Plugin 不支持 Unity 的 WebGL。
直接使用 EasyAR 云服务接口（比如 [CRS 服务接口](../../cloud-recognition/management.html)）开发的功能可以发布到 Web 平台。
* **关于录屏功能：**
录屏功能仅支持 Android 平台，且需配置 Graphics API 为 OpenGLES2 或 OpenGLES3。
## Graphics API
EasyAR Sense Unity Plugin 直接使用 Unity 的渲染管线，所有 Unity 中可以使用的图形 API 都可以支持。
## Scriptable Render Pipeline
EasyAR Sense Unity Plugin 支持 Universal Render Pipeline (URP) 7.0.0 或更新版本。
EasyAR Sense Unity Plugin 不支持 High Definition Render Pipeline (HDRP)。
> **注意**
**关于 Unity 6 URP 17+ render graph 支持的声明**
EasyAR 支持 Unity 6 URP 17+ render graph，但是 Unity 本身仍存在部分未解决的问题。在遇到异常情形时可以尝试使用 Unity 提供的 [URP 兼容模式](https://docs.unity3d.com/6000.2/Documentation/Manual/urp/compatibility-mode.html) 。
部分问题已经在最新版本的 Unity 中得到解决，建议使用 6.2 及以上版本。
非兼容模式下的已知问题包括：
1. [未解决] 当从 EasyAR 获取相机纹理（类似 ImageTracking\_Coloring3D 示例及 [ARSession 工作流（CameraDevice）](../cameras/sample-camera-device.html) 示例中的使用），在 iOS/Mac 设备上可以观察到视觉故障和伪影。我们已经在纯 Unity 包中复现该问题并报告给了 Unity： [Glitches on iOS with AR Camera Image Rendering (URP 17 render graph)](https://discussions.unity.com/t/glitches-on-ios-with-ar-camera-image-rendering-urp-17-render-graph/1548048) 。问题进展可以关注 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 更新以及 Unity 未来版本的发布日志。
对于所有版本的 Unity 6，可以使用 [部分缓解措施](../../../api/unity/easyar.EasyARSettings.Workaround.html#u_easyar_EasyARSettings_Workaround_URP17RG_IOS_Glitches_Partial)，默认开启。
对于 Unity 6.2 及更新版本，可以将 Universal Render Pipeline Asset 中的 Render Scale 设置为 0.96-1.05 以外的数值来规避这个问题。
2. [Unity 6.2 已修复] Windows DX11 上相机画面会让场景中的物体渲染效果不可预测。在 Unity 6.0 - 6.1 版本中，EasyAR 提供 [规避选项](../../../api/unity/easyar.EasyARSettings.Workaround.html#u_easyar_EasyARSettings_Workaround_URP17RG_DX11_RuinedScene)] 且默认开启。

---

## 在 Unity 场景中自动切换 Unity XR 物体
- 章节路径: `unity/fundamentals/unity-xr-switch.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-xr-switch.html

# 在 Unity 场景中自动切换 Unity XR 物体
Unity 的 XR 组件（包括 AR Foundation）所能支持的设备有限。为了在受支持的设备上使用 AR Foundation，同时又能在其它大量设备上使用 AR 功能，EasyAR 提供了自动切换 Unity XR 物体的功能。以下内容介绍该功能对场景物体的改动及使用方法。
## 开始之前
* 阅读 [EasyAR 对 Unity XR 框架的支持](unity-xr.html) 了解 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
* 确保场景已按 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html) 所描述，添加了 AR Foundation 的 [ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html) 及 [XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html)。
## 功能介绍
由于 Unity 的 AR Foundation 在手机上底层实现是 ARCore 和 ARKit，只能在有限的设备上使用，尤其是在很多国产 Android 手机上无法使用，所以通常建议仅在受支持的设备上启用 AR Foundation 及相关功能脚本。自动切换 Unity XR 物体的功能实现了上述操作，主要为移动 AR 设计，头显上默认配置下功能会被禁用。
在完整功能启用时，
* 编辑器中，[easyar.ARSession](../../../api/unity/easyar.ARSession.html) 会禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)
* 运行时，[easyar.ARSession](../../../api/unity/easyar.ARSession.html) 会在 [Awake()](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Awake.html) 时禁用所有 Unity XR Core 组件及 AR Foundation 的组件。
* 运行时，如果被选择的 [FrameSource](../../../api/unity/easyar.FrameSource.html) 继承自 [ARFoundationFrameSource](../../../api/unity/easyar.ARFoundationFrameSource.html) 或是实现了 [XROrigin](../../../api/unity/easyar.ExternalDeviceFrameSource.DeviceOriginType.html#u_easyar_ExternalDeviceFrameSource_DeviceOriginType_XROrigin) 原点的 [ExternalDeviceFrameSource](../../../api/unity/easyar.ExternalDeviceFrameSource.html)，则被禁用的 Unity XR Core 组件及 AR Foundation 组件将在 [easyar.ARSession.StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 时启用（未被 EasyAR 禁用的不会启用）。如果其他 [FrameSource](../../../api/unity/easyar.FrameSource.html) 被选择，则在 [easyar.ARSession.StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 时会禁用所有 Unity XR Core 组件及 AR Foundation 的组件。
* 运行时，所有 Unity XR Core 组件及 AR Foundation 的组件会在 [easyar.ARSession.StopSession(bool)](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StopSession_System_Boolean_) 时禁用。
默认配置下，功能启用条件如下，
* 在 Windows/Mac 上启用。
* 切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。
* 切换器启动时，如果存在移动AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。
> **注意**
XR Interaction Toolkit 的组件不受该功能控制，但其在 EasyAR 中是否可用未经验证。理论上对于只使用 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) GameObject 及其 Camera 的功能应该可以正常使用。如果行为异常可以尝试设置 [ARSession.ARCenterMode](../../../api/unity/easyar.ARSession.ARCenterMode.html) 为 [ARSession.ARCenterMode.SessionOrigin](../../../api/unity/easyar.ARSession.ARCenterMode.html#u_easyar_ARSession_ARCenterMode_SessionOrigin)。如果功能还是不正常，则需要实现自定义的 XR Interaction Toolkit 的组件控制，在 [FrameSource](../../../api/unity/easyar.FrameSource.html) 不是继承自 [ARFoundationFrameSource](../../../api/unity/easyar.ARFoundationFrameSource.html) 时禁用相关组件。
## 配置方法
这个功能可以通过 `Project Settings` > `EasyAR` > `Sense` 中的 `Unity XR` > `Unity XR Auto Switch` 中的选项启用或关闭。
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/xr-auto-switch.png)
图中选项配置功能行为如下：
* **Editor**：编辑模式选项
* **Disable AR Session**：存在 [easyar.ARSession](../../../api/unity/easyar.ARSession.html) 时，编辑时禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)。
* **Player**：运行模式选项
* **Enable**：启用运行时控制。注意：关闭该选项时编辑模式被禁用的组件在运行时不会被恢复。
* **Enable If Desktop**：在 Windows/Mac 上启用。
* **Enable If Mobile AR On Startup**：切换器启动时，如果移动 AR（ARKit/ARCore）的 loader 是激活的，则启用。通常这个选项需要 `Project Settings` > `XR Plug-in Management` 中的 `Initialize XR on Startup` 是选中的。
* **Disable If Non Mobile AR Post Startup**：切换器启动时，如果存在移动AR（ARKit/ARCore）之外的其它 loader，但没有任何一个 loader 是激活的，则禁用。通常这个选项会在 `Project Settings` > `XR Plug-in Management` 中的 `Initialize XR on Startup` 未选中时被使用。
* **Restore AR Session When Disabled**：功能禁用时，恢复（启用）所有被禁用的 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)（无论它是否由 EasyAR 所禁用）。这个选项通常用于恢复编辑时被禁用的组件。
## 使用自定义的控制方法
如果需要自定义这些组件的切换，或是 EasyAR 的行为干扰了某些组件的正常工作，需要确保关闭这些选项，同时根据以下基本规则自定义组件切换：
1. 在编辑器中禁用 [UnityEngine.XR.ARFoundation.ARSession](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARSession.html)（它在执行时序中早于所有其它脚本）
2. 在 AR Foundation 开始工作前禁用所有 Unity XR Core 组件及 AR Foundation 的组件以及需要控制的相关组件或功能
3. 如果 [easyar.ARSession.Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 过程中选择了 [ARCoreARFoundationFrameSource](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html) 或 [ARKitARFoundationFrameSource](../../../api/unity/easyar.ARKitARFoundationFrameSource.html)，启用之前禁用的所有组件或功能，需要在 [StartSession()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_StartSession) 完成前完成，通常建议在 [easyar.ARSession.AssembleUpdate](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleUpdate) 事件响应中完成
4. 如果 [easyar.ARSession.Assemble()](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_Assemble) 过程中选择使用了其它 [FrameSource](../../../api/unity/easyar.FrameSource.html)，则保持不变
## 相关主题
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)

---

## EasyAR 对 Unity XR 框架的支持
- 章节路径: `unity/fundamentals/unity-xr.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/fundamentals/unity-xr.html

# EasyAR 对 Unity XR 框架的支持
EasyAR 并不依赖 Unity XR 框架来提供 AR 功能，但可以支持 Unity XR 框架中的部分组件包，以便在 Unity 中使用 EasyAR 的 AR 功能时可以利用 Unity XR 框架提供的功能。以下内容介绍了 EasyAR 对 Unity XR 框架的支持情况，以及在什么情况下可以考虑使用 AR Foundation。
## Unity XR 支持
Unity 通过其 [插件框架及一系列功能包和工具包](https://docs.unity3d.com/Manual/xr-support-landing.html) 支持 XR 开发。EasyAR 也支持这些 Unity XR 组件包，以便在 Unity 中使用 EasyAR 的 AR 功能时可以利用 Unity XR 框架提供的功能。
EasyAR 支持以下 Unity XR 组件包：
|显示名称|包名|最低支持版本|是否必需|用途|
|**XR Core Utilities**|com.unity.xr.core-utils|2.0.0|否|提供 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 支持|
|**AR Foundation**|com.unity.xr.arfoundation|5.0.0|否|提供 AR Foundation 支持|
|**XR Plugin Management**|com.unity.xr.management|3.0.0|否|提供 ARCore SDK 管理兼容及获取运行时 XR Loader 类型|
|**XR Interaction Toolkit**|com.unity.xr.interaction.toolkit|2.0.0|否|未直接使用|
|**PolySpatial visionOS**|com.unity.polyspatial.visionos|2.0.4[1](#fn:1)|否|未直接使用|
|**Apple visionOS XR Plugin**|com.unity.xr.visionos|2.0.4[1](#fn:1)|否|未直接使用|
|**Apple ARKit XR Plugin**|com.unity.xr.arkit|5.0.0|否|未直接使用|
|**Google ARCore XR Plugin**|com.unity.xr.arcore|5.0.0|否|提供 ARCore SDK 管理兼容|
> **注意**
EasyAR 并不依赖 Unity XR 框架来提供 AR 功能。因此，在没有 AR Foundation 等 Unity XR 组件的使用需求时，可以不安装这些组件包，EasyAR 仍然可以在受支持的设备上正常工作。
## AR Foundation 支持
[AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest) 是 Unity 提供的 AR 开发框架，其 AR 功能通过底层系统或第三方实现，常用于支持 ARCore、ARKit 以及部分头显。
### EasyAR 与 AR Foundation 的关系
```
block
columns 6
block:groupApp:6
block:groupAppWrapper
space
App1["EasyAR<br>App"]
space
App2["EasyAR + AR Foundation<br>App"]
space
App3["AR Foundation<br>App"]
end
end
block:groupSensePlugin:4
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupAREngineInterop
columns 1
AREngineInterop["EasyAR<br>AR Engine Interop"]
space
end
block:groupSense:3
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
Image["Image<br>Tracker"]
Object["Sparse<br>SpatialMap"]
MotionTracker["Motion<br>Tracker"]
MARCore["ARCore"]
MARKit["ARKit"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:6
columns 1
System["System Library"]
block:groupSystemWrapper
space
AREngine["AR Engine<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
ARCore["ARCore<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
ARKit["ARKit<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePlugin --> App1
SensePlugin --> App2
ARF --> App2
ARF --> App3
groupSense --> SensePlugin
groupAREngineInterop --> SensePlugin
AREngine --> groupAREngineInterop
XRSubsystem --> ARF
XRSubsystem --> XRI
ARCore --> MARCore
ARKit --> MARKit
ARCore --> XRSDK
ARKit --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style AREngineInterop fill:none,stroke:none,stroke-width:0px,color:#fff
style Sense fill:none,stroke:none,stroke-width:0px,color:#fff
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px,color:#fff
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class groupAREngineInterop EasyAR
class groupSense EasyAR
class SensePlugin EasyAR
classDef Unity fill:#636,stroke:#333,color:#fff
class groupXRSubsystem Unity
class ARF Unity
class XRI Unity
```
EasyAR 与 AR Foundation 是两个独立的 AR 框架，EasyAR 并不依赖 AR Foundation 来实现其 AR 功能。EasyAR 也可以通过系统中的 ARKit、ARCore 等系统库来实现运动跟踪能力。同时，EasyAR 还提供了 AR Foundation 所不具备的两种运动跟踪实现：EasyAR 自身的运动跟踪实现以及通过 AR Engine 提供的运动跟踪实现，从而提供了相比 AR Foundation 更加广泛的设备支持。
同时，EasyAR 可以获取 AR Foundation 运行时的数据，在 AR Foundation 运行时利用它所提供的运动跟踪能力驱动其它 AR 功能运行，从而提供对 AR Foundation 的兼容性。这些功能包括：
* Mega
* 稀疏空间地图
* 稠密空间地图
* 使用运动融合的图像跟踪和物体跟踪
可以参考 [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html) 了解更详细的运动跟踪与 EasyAR 功能的关系。
### 什么情况下需要使用 AR Foundation
多数情况下，可以不使用 AR Foundation，EasyAR 会在比 AR Foundation 所支持的更加广泛的设备上正常工作。通常在以下两种情况下可以考虑使用 AR Foundation：
1. 需要使用 EasyAR 未封装的 ARKit 及 ARCore 功能
如果需要使用的 ARCore 或 ARKit 提供的一些功能在 EasyAR 中未封装，可以使用 AR Foundation。比如 AR Foundation 提供了对 ARKit 人脸跟踪的支持 [ARFaceManager](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARFaceManager.html)，EasyAR 并没有封装这个功能。
2. 在部分系统存在问题的小米手机上使用 ARCore 而非 EasyAR 实现的运动跟踪
如果需要在所有支持 ARCore 的小米和红米手机上使用 ARCore，可以考虑启用 AR Foundation。由于部分小米和红米手机系统存在问题，EasyAR 的 ARCore 封装不支持这些设备，包括米 9、米 10、红米 K20、红米 K30、红米 K40 等系列（这里列出的不全，设备支持会持续更新）。在这些手机上，默认配置下将不会使用 ARCore，在支持 EasyAR 运动跟踪的手机上会使用EasyAR 运动跟踪。
使用 AR Foundation 时 EasyAR 的功能效果并不是最优的。存在两种情况：
1. 在 EasyAR 不直接支持的那部分小米和红米手机上，输入 EasyAR 的数据是灰度图而非彩色图，这会影响部分算法的效果。由于设备自身问题，这是无法通过配置解决的。
2. 在使用 Mega 时，AR Foundation 默认使用的配置并不是最优的。
> **小心**
可以通过修改 AR Foundation 的 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 来获取更优的数据输入，启用 [ARCoreARFoundationFrameSource.OptimizeConfigurationForTracking](../../../api/unity/easyar.ARCoreARFoundationFrameSource.html#u_easyar_ARCoreARFoundationFrameSource_OptimizeConfigurationForTracking) 可以自动完成最佳 [ARCameraManager.currentConfiguration](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.4/api/UnityEngine.XR.ARFoundation.ARCameraManager.html#UnityEngine_XR_ARFoundation_ARCameraManager_currentConfiguration) 选择。但需要注意部分手机自身（比如小米 10）存在问题，在修改配置之后无法获取图像，EasyAR 将无法使用（应用有图像背景但 EasyAR 功能没有任何反应），因此通常并不建议启用，如需使用需要做好 EasyAR 无法使用时的降级方案。
## 头显支持
由于 Unity XR 框架未提供足够充分的数据接口，因此 EasyAR 并不通过 Unity XR 框架来支持头显。
在支持 Unity XR 框架的头显上，EasyAR 会通过 **XR Core Utilities** 支持 [Unity.XR.CoreUtils.XROrigin](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.5/api/Unity.XR.CoreUtils.XROrigin.html) 的使用，但并不使用 Unity XR 框架来实现头显的支持。EasyAR 不会影响 **XR Interaction Toolkit** 的功能，只要设备支持就可以正常使用。
一般来说，头显厂商各自提供了 SDK 或系统接口来提供这些数据，EasyAR 通过系统接口以及厂商的 SDK 来支持头显。有些时候这些 SDK 并不是完全公开的，EasyAR 会与厂商合作提供完整支持。[Unity 中的头显支持](../headsets/headsets.html) 介绍了 EasyAR 支持的头显及其使用方法。
## 后续步骤
* 了解如何 [在 EasyAR 项目中启用 AR Foundation](arfoundation.html)
* 了解 [EasyAR 项目中的 AR Foundation 场景配置和用法](arfoundation-scene-setup.html)
* 了解如何根据设备支持情况 [自动切换 AR Foundation](unity-xr-switch.html)
## 相关主题
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)
* [Unity 中的头显支持](../headsets/headsets.html)
1. Unity 6 及更新版本中，最低支持 2.0.4。Unity 2022.3 中，最低支持 1.2.3，不支持 1.3.x。[↩](#fnref:1)[↩](#fnref:2)

---

## 充分利用 UI 诊断信息和工具
- 章节路径: `unity/getting-started/diagnostics.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/diagnostics.html

# 充分利用 UI 诊断信息和工具
本文介绍了如何快速配置和使用 UI 诊断信息和开发者模式工具，以便在开发和测试阶段更好地调试和优化应用。
## 阅读 UI 消息
默认配置下，运行 EasyAR Sense Unity Plugin 应用时，诊断信息会通过 UI 消息显示在屏幕偏上位置，方便开发者了解 session 的运行状态和问题。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message-ui.png)
> **提示**
这些文字不是水印，可以根据需要显示或隐藏。
这些信息可以帮助开发者了解 session 的运行状态和问题，建议在开发和测试阶段保持显示。
可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Message Output` 来配置 UI 消息的显示方式。其中 `Message Output` > `Session Dump` 可以控制 session 状态信息的显示，其它选项可以控制不同级别的诊断消息的显示方式。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-message.png)
通常建议在开发和测试阶段，进行以下配置：
* Message Output > Session Dump： `UI`
* Message Output > Sense Error： `UIAndLog`
* Message Output > Session Error： `UIAndLog`
* Message Output > Error： `UIAndLog`
* Message Output > Warning： `UIAndLog`
在发布上线阶段，进行以下配置：
* Message Output > Session Dump： `None`
* Message Output > Sense Error： `Log`
* Message Output > Session Error： `Log`
* Message Output > Error： `Log`
* Message Output > Warning： `Log`
## 使用开发者模式工具
默认配置下，运行 EasyAR Sense Unity Plugin 应用时，快速点击屏幕 8 次会在靠屏幕右边中间位置弹出开发者模式面板，方便开发者查看和调试 session 的运行状态以及录制用于模拟运行的数据。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode-panel.png)
* 可以通过 `session` 右边的切换按钮来切换屏幕上方信息的显示与否。
* 可以通过 `eif` 右边的 `rec` 按钮来启动或停止 EIF 录制功能。录制的 EIF 文件会保存在应用的持久化数据路径中，可以通过 `Application.persistentDataPath` 来获取该路径。
如果要禁用开发者模式面板，可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Developer Mode Switch` 为 `Custom`。
![alt text](https://doc-asset.easyar.com/develop/unity/getting-started/media/diagnostics-devmode.png)
通常建议在开发和测试阶段，进行以下配置：
* Developer Mode Switch： `Default`
在发布上线阶段，进行以下配置：
* Developer Mode Switch： `Default` 或 `Custom`
如果选择 `Custom`，建议以其它方式保证线上应用可以使用诊断面板或自定义的方式收集运行时数据。
## 延伸阅读
* [诊断功能简介](../diagnostics/diagnostics.html)
* [UI 消息](../diagnostics/ui-messages.html) 介绍了如何使用 UI 消息来显示 session 状态
* [开发者模式](../diagnostics/developer-mode.html) 介绍了如何使用开发者模式进行调试

---

## 导入 EasyAR 插件以启用 AR 功能
- 章节路径: `unity/getting-started/enable-easyar.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/enable-easyar.html

# 导入 EasyAR 插件以启用 AR 功能
本教程介绍如何在 Unity 中启用 EasyAR 插件。
## 使用兼容的 Unity 版本
确保已安装兼容的 Unity 版本（Unity 2021.3 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
## 导入 EasyAR Sense Unity Plugin
在[下载页面](https://www.easyar.cn/view/download.html)，您会看到 Unity 插件有两个版本：`EasyAR Sense Unity Plugin` 和 `EasyAR Sense Unity Plugin (for Mega)`。
这两个版本的主要差异为：
* **EasyAR Sense Unity Plugin**： 不含 Mega 支持文件，不能用于 Mega 开发。EasyAR 提供从 4.6 开始的历史版本下载。
* **EasyAR Sense Unity Plugin (for Mega)**：包含 Mega 支持文件，可以用于 Mega 开发。EasyAR 不提供历史版本下载。
在不需要开发 Mega 功能时，建议使用 `EasyAR Sense Unity Plugin`。
* 下载插件包
* 下载最新版本的 [EasyAR Sense Unity Plugin](https://www.easyar.cn/view/download.html)。
* 解压下载的 `zip` 包之后可以看到 `readme` 和 `.tgz` 文件，`.tgz` 文件可以直接导入 Unity， 不能解压。
* 将 `.tgz` 文件存放到 Unity 项目 `Packages` 文件夹内。
* 导入插件包
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`。
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`。
* 在弹出的对话框中选择前述 `.tgz` 文件。
![ImportUnityPlugin](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_easyar_unity_plugin.png)
> **注意**
`.tgz` 文件在导入 Unity 后不能被删除或移动到另一个位置，需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 填写许可证（License Key）
从 Unity 菜单中选择 `EasyAR` > `Sense` > `Configuration` 调出 EasyAR Sense 设置界面。
![FillInKey](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
在 `EasyAR Sense License` 下的输入框中填入 EasyAR Sense License。
![FillInKey2](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill-in-key2.png)
> **提示**
EasyAR Sense License 可以从 EasyAR 开发中心（[中文](https://portal.easyar.cn/sdk/list)，[英文](https://portal.easyar.cn/sdk/list)） 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `是`，名称随意填写
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
> **注意**
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
## 后续步骤
* 可以阅读 [配置 AR 场景](scene.html) 了解如何创建一个简单的 AR 场景。
## 相关主题
* 如果需要开发 Mega 功能，可以 [导入最新版本的 EasyAR 插件以启用 Mega 功能](../mega/enable-mega.html)。

---

## 使用示例快速入门 EasyAR Unity 开发
- 章节路径: `unity/getting-started/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/quickstart.html

# 使用示例快速入门 EasyAR Unity 开发
本教程介绍如何配置并运行 EasyAR Unity 示例，以快速入门 AR 开发。
## 准备空 Unity 工程
确保已安装兼容的 Unity 版本（Unity 2021.3 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
使用 `3D (Built-in Render Pipeline)` 模板创建空 Unity 工程：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/create-project.png)
> **注意**
初次使用不建议使用 URP。
如果您在使用 Unity 6，需要手动下载并使用 `3D (Built-In Render Pipeline) Template`，默认安装下它在模板列表靠后的位置。
> **重要事项**
若要使用 URP，必须按照 [Universal Render Pipeline (URP)](universal-render-pipeline.html) 进行额外配置，否则相机画面将无法显示。
## 导入 EasyAR Sense Unity Plugin
* 下载插件包
* 下载最新版本的 [EasyAR Sense Unity Plugin](https://www.easyar.cn/view/download.html)，其中包含示例（sample）。
* 解压下载的 `zip` 包之后可以看到 `readme` 和 `.tgz` 文件，`.tgz` 文件可以直接导入 Unity， 不能解压。
* 将 `.tgz` 文件存放到 Unity 项目 `Packages` 文件夹内。
* 导入插件包
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`。
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`。
* 在弹出的对话框中选择前述 `.tgz` 文件。
![ImportUnityPlugin](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_easyar_unity_plugin.png)
> **注意**
`.tgz` 文件在导入 Unity 后不能被删除或移动到另一个位置，需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 导入示例
使用菜单 `Window` > `Package Manager` 打开 Package Manager，选中 `EasyAR Sense Unity Plugin`, 在右侧选择 `\*\*All Samples\*\*` 一次性导入所有示例。
![ImportSample](https://doc-asset.easyar.com/develop/unity/getting-started/media/import_samples.png)
> **小心**
`\*\*All Samples\*\*` 和其他示例不可同时导入，否则会出现重复资产进而导致部分场景资源丢失。如不小心导入了重复的文件，需删除后重新导入。
## 修改场景列表
打开 `Build Settings` （ 或 `Build Profiles` ），
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_4.png)
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_6.png)
将 Unity 工程中的示例场景添加到 `Build Settings` 或 `Build Profiles` 的 `Scene List` 中，并将示例启动器的场景（`AllSamplesLauncher`）移动到所有场景中的第一个。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_7.png)
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_8.png)
> **小心**
注意不要这些添加头显的场景，否则可能会打包失败：
* Combination\_BasedOn\_AppleVisionPro.rst
* Combination\_BasedOn\_Xreal.rst
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_14.png)
## 填写许可证（License Key）
从 Unity 菜单中选择 `EasyAR` > `Sense` > `Configuration` 调出 EasyAR Sense 设置界面。
![FillInKey](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill_in_licence_key.png)
在 `EasyAR Sense License` 下的输入框中填入 EasyAR Sense License。
![FillInKey2](https://doc-asset.easyar.com/develop/unity/getting-started/media/fill-in-key2.png)
> **提示**
EasyAR Sense License 可以从 EasyAR 开发中心（[中文](https://portal.easyar.cn/sdk/list)，[英文](https://portal.easyar.cn/sdk/list)） 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `是`，名称随意填写
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
> **注意**
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
## 编辑器中运行
在编辑器中运行需要您的电脑上连接一个摄像头。
### 确认系统相机正常
打开 `系统相机应用`：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/camera-windows-open.png)
确认相机可以正常使用：
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/camera-windows.png)
最后注意关闭相机应用，避免运行示例时发生冲突。
> **注意**
EasyAR 仅使用系统提供的接口打开相机，需确保 `系统相机应用` 可以打开相机并正常显示。
### 运行示例
>
> 以下内容以图像跟踪示例
`> ImageTracking_Targets
`> 为例，其他示例运行方式类似。
>
打开示例启动器场景，并点击 Unity 编辑器顶部的 `Play` 按钮。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-editor.png)
进入 `ImageTracking\_Targets` 场景。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-editor-select.png)
> **提示**
也可以直接打开 `ImageTracking\_Targets` 场景并执行。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-editor.png)
将摄像头对准以下识别图：
>
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
> 下载地址
> ：🔗
[> namecard
](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
EasyAR 会识别跟踪这张图，并叠加虚拟物体。
> **注意**
部分功能无法在编辑器中连接摄像头运行，但可以在手机上运行。无法在编辑器中使用的示例在运行时会有启动失败的弹窗。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_15.png)
同时会有消息提示和错误log输出。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_s1_13.png)
## 手机上运行
在手机上运行需要进行打包，打包前需要修改 Player 配置。
### 修改 Player 配置
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击安卓图标，调出 Android 平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
* 修改 Package Name 为 License Key 页面显示的 Package Name
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Package Name 是 `com.mycompany.myproject`，则必须填写这里 Package Name 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 Minimum API Level 为 `API Level 21` 或更高版本
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* 修改 Scripting Backend 为 `IL2CPP`，并在 `Target Architecture` 中勾选 `ARM64`
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-64bit.png)
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
* 修改 Bundle ID 为 License Key 页面显示的 Bundle ID
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Bundle ID 是 `com.mycompany.myproject`，则必须填写这里 Bundle ID 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 `Architecture` 为 `ARM64`
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* 添加 `Camera Usage Description`，字符串内容可以随意填写，但必须添加。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-camera-permission.png)
### 打包应用
选择 `File` > `Build Settings`，选择目标平台 (Android/iOS)，然后选择 `switch platform`。
![switchplatform](https://doc-asset.easyar.com/develop/unity/getting-started/media/switch-platform.png)
选择 `Build` 或 `Build And Run` 编译项目并在手机上安装，运行时需允许相应权限。
![buildandrun](https://doc-asset.easyar.com/develop/unity/getting-started/media/build-and-run.png)
### 运行示例
>
> 以下内容以图像跟踪示例
`> ImageTracking_Targets
`> 为例，其他示例运行方式类似。
>
运行后启动的应是示例启动器场景。
> **提示**
如果打开后没有进入示例启动器场景，需要检查是否正确设置了 `Build Settings` 或 `Build Profiles` 的场景列表，将 `AllSamplesLauncher` 移动到第一个。
进入 `ImageTracking\_Targets` 场景。
![](https://doc-asset.easyar.com/develop/unity/getting-started/media/sample-launcher-phone-select.png)
将手机摄像头对准以下识别图：
>
![namecard](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
> 下载地址
> ：🔗
[> namecard
](https://doc-asset.easyar.com/develop/unity/fundamentals/media/namecard.jpg)
>
EasyAR 会识别跟踪这张图，并叠加虚拟物体。
## 后续步骤
您已经成功运行 Unity AR 示例，可能对示例所展示的 AR 场景是如何创建的感兴趣。可以按顺序阅读以下入门指南：
* [启用 EasyAR](enable-easyar.html)
* [配置 AR 场景](scene.html)
* [场景中的诊断信息](diagnostics.html)
关于示例启动器可以参考详细的使用说明：
* [示例启动器使用说明](sample-launcher.html)
如果您希望了解完整的工程配置，可以参考以下内容：
* [使用 Universal Render Pipeline（URP）](universal-render-pipeline.html)
* [Player 配置](../fundamentals/setup-player.html)
* [EasyAR 配置](../fundamentals/setup-easyar.html)
如果您希望进一步了解 EasyAR 的使用方法，可以从这里开始：
* [AR 驱动的 Unity 应用基础](../fundamentals/intro.html)

---

## 使用 AllSamplesLauncher 快速体验 EasyAR 样例
- 章节路径: `unity/getting-started/sample-launcher.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/sample-launcher.html

# 使用 AllSamplesLauncher 快速体验 EasyAR 样例
AllSamplesLauncher 是一个集成化的示例启动器，可以帮助您快速熟悉 EasyAR SDK 的各项功能。通过该启动器，您可以在单个 Unity 工程中一键切换并运行所有官方示例场景，无需手动配置多个独立项目。
## 准备工作
在开始之前，请确保您已经完成了以下准备工作：
1. 已安装 Unity Hub 和 Unity 编辑器
2. 创建一个新的 Unity 工程
3. 已导入 EasyAR Sense Unity Plugin 并且导入了所有 Samples
请参考 [快速入门](quickstart.html) 中的介绍按步骤进行操作。
## 详细步骤
1. 打开 Samples 中的所有场景。
![All Sample Scenes](https://doc-asset.easyar.com/develop/unity/getting-started/media/all-sample-scenes.png)
2. 点击菜单栏 `File` > `Build Settings` 或 `Build Profiles` > `Scene List` 。
3. 将所有场景都拖动到 `Scene List` 中。
4. 确保 AllSamplesLauncher 位于所有场景中的第一个。如不是，可以在窗口内拖动。
![Scene List Order](https://doc-asset.easyar.com/develop/unity/getting-started/media/scene-list-order.png)
5. 点击菜单栏 `File` > `Build And Run` 进行打包、运行。
> **注意**
打包到手机运行时，不要添加头显类的场景：
* Combination\_BasedOn\_AppleVisionPro
* Combination\_BasedOn\_Xreal
![Donot Load Headset](https://doc-asset.easyar.com/develop/unity/getting-started/media/donot-load-headset.png)
## 打包中遇到问题
在您编译、打包过程中，可能遇到一些错误。常见的问题有：
|错误信息|原因|解决办法|
|*FileNotFoundException:EasyAR Settings Asset*|未填写 License|点击菜单栏 `EasyAR` > `Sense` > `Configuration`，在 **EasyAR Sense License** 中填入您的 License Key|
|*Missing Prefab Asset: 'XR Interaction Setup'*|头显相关文件缺失|打包场景列表中删除头显相关场景。如果您确认需要打包头显，请按照 [使用头显样例](../headsets/samples.html) 中的步骤进行|
## 启动器使用
运行后，您将看到一个简洁的启动器界面。
![Lanucher Homepage](https://doc-asset.easyar.com/develop/unity/getting-started/media/lanucher-homepage.png)
点击界面底部中间的 `Samples` 按钮，即可进入所有功能的样例。
![Lanucher Samplepage](https://doc-asset.easyar.com/develop/unity/getting-started/media/lanucher-samplepage.png)
在界面左侧是功能分类，右侧则是每个功能下的场景样例列表。点击不同的样例场景，即可体验 EasyAR 提供的所有不同功能。
同时，在界面的底部还提供了 `EasyAR Sense` 和 `EasyAR Mega` 的功能演示视频，可以帮助您更好的理解 EasyAR 能为您提供怎样的功能和效果。
## 运行样例前的必读事项
在运行特定样例之前，您**必须**完成以下关键配置，否则样例将无法正常工作：
1. **设置您的 API Key**
* 部分样例（特别是涉及云识别、Mega 云定位等）需要有效的 API Key。
* 在菜单栏 `EasyAR` > `Sense` > `Configuration` 中，找到对应样例需要填写的地方。
* 从中填入您从 EasyAR 开发者中心申请到的 **App ID**、 **API Key**、 **API Secret**。
![Key Configuration](https://doc-asset.easyar.com/develop/unity/getting-started/media/key-config.png)
* **重要提示**：如果您还没有 API Key，部分本地功能的样例（如图片跟踪）可能仍能运行，但云功能会失败。请务必前往 [EasyAR 开发者中心](https://www.easyar.cn/view/login.html) 创建应用并获取 Key。
* **配置 XR/平台支持**：
* 如果您运行的是 **头显相关** 的样例，您参照 [使用头显样例](../headsets/samples.html) 中的进行。
* 请确保您的设备（如手机或头显）已正确连接并处于开发者模式。
## 深入探索样例
示例启动器是您学习的最佳起点。我们强烈建议您：
* **先运行，再研究**：通过启动器快速体验每个样例的效果，对 EasyAR 的能力建立直观印象。
* **打开场景源文件**：每个样例都是一个独立的 Unity 场景文件，位于 `Assets/Samples/EasyAR Sense Unity Plugin/[版本号]/\_\_All Samples\_\_/[功能名称]/[样例名称]/Scenes` 目录下。
* **研究并阅读脚本代码**：在样例场景中，可以打开样例附带的 `\*.cs` 脚本，查看我们是如何调用 EasyAR API 来实现特定功能的。这是学习 API 使用方法的最佳途径。
通过示例启动器，您可以快速建立对 EasyAR SDK 的功能认知。祝您探索愉快！

---

## 配置 AR 场景
- 章节路径: `unity/getting-started/scene.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/scene.html

# 配置 AR 场景
本文以图像跟踪为例，介绍如何配置一个最简单的 AR 场景。
## 开始之前
* 按 [启用 EasyAR](enable-easyar.html) 的内容导入 EasyAR Sense Unity 插件并填写许可证（License Key）。
> **注意**
如果您的工程使用了 URP (Universal Render Pipeline) ，还需要额外 [配置 URP](universal-render-pipeline.html) 。
## 添加 AR Session
在 `Hierarchy` 视图中，在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `AR Session (Image Tracking Preset)` 创建一个用于图像跟踪的 session。
![PresetImageTracking](https://doc-asset.easyar.com/develop/unity/fundamentals/media/session-creation.png)
## 配置摄像机
选中 `Main Camera`, 在 `Inspector` 设置以下参数。
* 设置 `Clear Flags` 为 `Solid Color`。
* 设置 `Background` 为黑色。
* 设置 `Clipping Planes` 的 `Near` 为 0.1（米），`Far` 为 1000（米）。
![mainCameraSetting](https://doc-asset.easyar.com/develop/unity/getting-started/media/main_camera_setting.png)
## 添加 Target
在 `Hierarchy` 视图中，在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Target : Image Target` 添加一个 Image Target，默认显示为问号图标。
![createimagetarget](https://doc-asset.easyar.com/develop/unity/getting-started/media/create_image_target.png)
选中需要跟踪的图像，设置以下参数，并点击 `Apply` 按钮应用设置：
* 设置 `Texture Type` 为 `Editor GUI and Legacy GUI`。
* Advanced 中启用 `Read/Write`。
* `Format` 设置为 `RGB 24 bit`。
![createimagetarget](https://doc-asset.easyar.com/develop/unity/getting-started/media/target-image.png)
配置 `ImageTargetController`：
* 设置 **Source Type**: 为 `Texture 2D`。
* 设置 **Texture** 为配置好的图片。
* 设置 **Name** 为 namecard。
* 设置 **Scale** 为 0.09（表示 0.09 米）。
* 设置 **Tracker** 为 ARSession 下的 `ImageTrackerFrameFilter`。
![addimagetargetcontroler](https://doc-asset.easyar.com/develop/unity/getting-started/media/image_target_controller.png)
> **提示**
Source Type 不同时，部分配置内容会有所不同。
## 添加跟随 Target 的 3D 内容
在 Image Target 节点下添加的 3D 内容相对图片的位置保持不变，即图片移动之后，虚拟内容跟随显示。
在 `Hierarchy` 视图中，选中 `Image Target`，通过菜单 `3D Object` > `Cube` 添加一个 Cube。
![add3D-1](https://doc-asset.easyar.com/develop/unity/getting-started/media/add_3D_1.png)
选中刚才添加的 Cube，配置其属性：
* 设置 Transform 的 `Scale` 为 {0.5, 0.3, 0.3}。
* 设置 Transform 的 `Position` 的 `z` 值为 -0.15 （使 Cube 底面与识别图对齐）。
![add3D-2](https://doc-asset.easyar.com/develop/unity/getting-started/media/add_3D_2.png)
到这里，一个最简单的 AR 场景就配置完成了。运行场景并对准图片，即可看到 Cube 出现在图片上方。
## 后续步骤
* 运行中会注意到屏幕上会显示黄色文字，可以阅读 [场景中的诊断信息](diagnostics.html) 了解这些信息的含义以及常用配置方法。
## 相关主题
* 了解 [AR Session](../fundamentals/session.html)
* 了解 [AR 场景中的 Camera](../fundamentals/camera.html)
* 了解 [Target](../fundamentals/target.html)

---

## 配置 Universal Render Pipeline（URP）
- 章节路径: `unity/getting-started/universal-render-pipeline.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/getting-started/universal-render-pipeline.html

# 配置 Universal Render Pipeline（URP）
这篇文档介绍了 Universal Render Pipeline（URP） 工程接入 EasyAR 功能时如何配置。
## 开始之前
* 了解[在 Unity 中使用 URP 的方法](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest?subfolder=/manual/InstallingAndConfiguringURP.html)。
* 参考[在 Unity 中启用 EasyAR](enable-easyar.html) 导入 EasyAR Unity 插件。
## 创建 Universal Render Pipeline 资产
> **注意**
如果 Unity 项目使用 URP 项目模板创建，或项目中已经存在 UniversalRenderPipelineAsset 和 Universal Renderer，可以直接跳到[确认项目已切换至 URP 渲染管线](#unity-gettingstarted-universal-render-pipeline-switch)。
在 **Project** 窗口通过右键菜单 **Create** > **Rendering** > **URP Asset(with Universal Renderer)** 创建所需资产：
![Unity6.2_URP_Create_Asset](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline06.png)
## 找到目标平台所使用的 Universal Render Pipeline 资产
1. 点击菜单栏 **Edit** > **Project Settings** > **Graphics**。
顶部的 **Default Render Pipeline** 槽位应当已分配了一个 `Universal Render Pipeline Asset`。
![Unity6.2_URP_Graphics](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline01.png)
> **提示**
该选项在旧版 Unity 中的名称为 **Scriptable Render Pipeline Settings**。
2. 点击菜单栏 **Project Settings** > **Quality**。
选择目标平台的质量级别，下方的 **Render Pipeline Asset** 即目标平台使用的 Universal Render Pipeline 资产。若为空，则目标平台使用的 Universal Render Pipeline 资产为 **Graphics** 窗口中配置的资产。
![Unity6.2_URP_Quality](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline02.png)
> **提示**
若 **Quality** 中的设置与 **Graphics** 不一致，系统将优先使用 **Quality** 中的 Asset。
## 配置 Universal Render Pipeline 资产
> **重要事项**
Unity 编辑器与 Android/iOS 等设备上使用的 Universal Render Pipeline 资产往往是不同的，在编辑器上使用和在设备上使用需要分别配置。
1. 选择目标平台使用的 `Universal Render Pipeline Asset`，然后选择它所使用的 `Universal Renderer Data`。
![Unity6.2_URP_Renderer](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline03.png)
> **提示**
如果项目中配置了多个 Renderer，确保选择的是 **AR 相机正在使用** 的那个渲染器。您可以在场景相机的 **Camera** 组件 > **Rendering** > **Renderer** 选项中确认当前的索引值。
2. 在 `Universal Renderer Data` 的 **Inspector** 面板下方点击 **Add Renderer Feature**，添加 [EasyARCameraImageRendererFeature](../../../api/unity/easyar.EasyARCameraImageRendererFeature.html)。
![Unity6.2_URP_Renderer_Add_Feature](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline04.png)
## 使用 EasyAR 示例的注意事项
EasyAR Unity 插件自带的示例场景默认使用 `Built-in` 渲染管线的材质和着色器。Unity 会自动将这些材质和着色器转换为 URP 兼容的版本，但有少部分资源可能会渲染异常，需要参考 [Convert assets using the Render Pipeline Converter](https://docs.unity3d.com/Documentation/Manual/urp/features/rp-converter.html) 手动转换。
![非 URP 渲染异常](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline08.png)
点击菜单 **Window** > **Rendering** > **Render Pipeline Converter**，选择 **Built-in to URP** 打开转换窗口。勾选 **Material Upgrade** 和 **Readonly Material Converter** > 点击下方的 **Convert Assets**。
![Render Pipeline Converter](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline09.png)
转换完成后，示例材质显示将恢复正常。
## 常见问题
若配置不正确，运行时将没有相机画面，常常为显示为黑屏，但是在跟踪上目标时，添加在跟踪目标下的内容会正常显示。
在 4000 及以上版本中，session 会进入 [Broken](../../../api/unity/easyar.ARSession.SessionState.html#u_easyar_ARSession_SessionState_Broken) 状态，这时画面或日志中会显示 [BrokenReason](../../../api/unity/easyar.SessionReport.html#u_easyar_SessionReport_BrokenReason) 为 `URP RenderPipeLineAsset not properly setup`：
![Session_Broken_Caused_By_URP](https://doc-asset.easyar.com/develop/unity/getting-started/media/universal-render-pipeline07.png)
解决该问题需按本文描述正确配置 `Universal Render Pipeline Asset`。
## 相关主题
* [Unity 兼容性](../fundamentals/unity-compatibility.html)

---

## 在 EasyAR 项目中启用头显支持
- 章节路径: `unity/headsets/enable-headset.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/enable-headset.html

# 在 EasyAR 项目中启用头显支持
本文档介绍了如何在一个已有的 EasyAR Unity 场景中启用头显支持。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
* 阅读 [Unity 中的 EasyAR 头显支持](headsets.html) 了解在 Unity 中 EasyAR 头显支持的整体架构。
本文假设您有一个已经可以使用 EasyAR 的场景。如果需要创建这样的场景，或是在一个头显场景中添加 EasyAR 组件，可以参考以下文档：
* [添加 AR Session](../fundamentals/session-creation.html)
* [配置 Camera](../fundamentals/camera-configs.html)
* [添加 XR Origin](../fundamentals/origin-creation.html)
## 在场景中添加头显组件
在场景中添加头显组件之前，通常需要移除现有的 Camera 和 XR Origin。
### 移除 Camera 和 XR Origin
删除场景中现有的 Camera。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/del-camera.png)
如果场景里已经存在 `XR Origin`，无论它来自 EasyAR 还是 Unity XR 框架，大部分情况下需要将其删除。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/del-origin.png)
> **提示**
在一些高级的用法中，可以根据自己需要判断是否删除。
### 添加头显组件
遵循头显官方说明来添加头显的组件。这里以 Pico 头显为例，与官方说明冲突时以官方说明为准。
使用菜单添加一个 `XR Interaction Manager`：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-add-manager.png)
使用菜单添加一个 `XR Origin`：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-add-origin.png)
在运行之前，需要确保阅读头显官方说明来了解一个有头显 SDK 的场景应该如何进行配置和运行。
## 配置 frame source
### 内置支持的设备
选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Head Mounted Display (Built-in)` > `Frame Source : [Name] (keep it only)` 创建 [Name] 的 frame source 并仅保留它。
比如，为 Apple Vision Pro 配置 frame source：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/visionpro-frame-source-add.png)
操作之后 session 中的 frame source 会变成这样：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/visionpro-frame-source.png)
> **提示**
如果 session 中包含设备对应的 frame srouce 并且在设备上是第一个可用的 frame source（比如上图中，在 visionOS 系统中 VisionOS ARKit 就是第一个可用的 frame source），可以不修改。部分菜单创建的默认 session 就属于这种情况。
### 扩展支持的设备
选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Extensions` > `Frame Source : [Name] (keep it only)` 创建 [Name] 的 frame source 并仅保留它。
比如，为 Pico 头显配置 frame source：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-frame-source-add.png)
操作之后 session 中的 frame source 会变成这样：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/pico-frame-source.png)
### 跨设备支持
如果需要场景可以在不同设备上运行，需要保留其它 frame source，并确保在设备当前 frame source 可以被选中。
使用不含 `(keep it only)` 的菜单项可以只添加 frame source 且不删除其它 frame source，比如 `EasyAR Sense` > `Extensions` > `Frame Source : Pico` 将在 session 所有 frame source 最后创建适用于 Pico 的 frame source。一般来说，通过这个方式添加完 frame source 之后，还需要将它移动到合适的位置。
> **提示**
在一些高级的用法中，可以根据自己需要调整 frame source 的位置，也可以在代码中修改。
## 后续步骤
* [Vision Pro 工程配置](setup-visionpro.html)
* [XREAL 工程配置](setup-xreal.html)
* [其它 Android 设备工程配置](../fundamentals/setup-player.html)
## 相关主题
* [帧数据源及运行时选取](../cameras/frame-source.html)

---

## 运行验证（bring-up）头显扩展
- 章节路径: `unity/headsets/extension-bring-up.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-bring-up.html

# 运行验证（bring-up）头显扩展
为使 EasyAR 在设备上工作，最重要的工作同时也是最棘手的部分是确保输入数据正确性。在一个新设备上首次运行 EasyAR 时，超过 90% 的问题都是由错误的数据造成的。
如果可能，建议在没有 EasyAR 存在的时候，仅通过设备及设备接口使用一些测试方法来直接验证数据的正确性。本文会介绍一些使用 EasyAR 功能来验证数据的经验方法，这个过程能帮助理解 [外部输入帧数据](../cameras/external-input-frame.html)，但由于 EasyAR 自身也存在误差，使用这个耦合在一起的系统验证数据正确性并不是最佳选择。
## 开始之前
* 完成 [让头显支持 EasyAR](extension-imp.html) 开发。
* 阅读 [快速入门](../getting-started/quickstart.html) 了解如何使用 EasyAR Sense Unity Plugin。
* 了解如何 [使用头显样例](samples.html)。
* 了解 [Android 工程配置](../fundamentals/setup-player.html)。
## 运行基础功能示例
第一次在设备上运行验证 EasyAR 时，需要确保顺序运行这些功能，尤其是不要急于运行 Mega，因为 Mega 有一些容错性，在短时间运行或单一现实场景中运行的时候难以发觉问题。
1. 观察眼前显示的 session 信息，确保没有意外情况发生，并确保 frame count 在持续增长。
2. 运行 `Image` ，即 [图像跟踪](../../image-tracking/intro.html) 功能，与手机运行效果对比一致（建议以 iPhone 为标准）。关注跟踪状态和目标覆盖显示。
在未开启运动融合时，图像跟踪的效果会有明显延迟感，这是符合预期的。运动过程正确、设备停下来的时候位置能对齐即可。
3. 运行 `Dense` ，即 [稠密空间地图](../../dense-spatial-mapping/intro.html) 功能，与手机运行效果对比一致（建议以 iPhone 为标准）。关注网格位置、生成速度和质量。
如果输入数据帧率较低，网格生成速度会变慢，但质量不会明显变差。
该功能无法在部分 Android 设备上运行，网格质量也会根据设备而变化。
> **重要事项**
头显扩展包所使用的输入扩展是一个 [自定义相机](../../cameras/custom-camera.html) 实现。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
如果 `Image` 以及 `Dense` 都和手机上的效果表现一致或更好，那么大部分 EasyAR 的功能就都可以在设备上正常工作，可以开始测试 Mega 了。
## 解决运行中的异常情况：问题分解
如果无法重现与手机上相同的结果，那接下来是一个详细的问题分解过程，可以参考它来寻找根因。建议始终关注系统日志输出。
### 步骤零：理解头显自身系统误差
还记得 [为 AR/MR 准备设备](extension-imp.html) 中所描述的运动跟踪和显示需求吗？
> **重要事项**
运动跟踪/VIO 误差会始终以不同方式影响 EasyAR 算法的稳定性。
> **重要事项**
显示系统误差可能会导致虚拟物体和现实物体无法完美对齐。
在一些误差比较大的情形下，虚拟物体会看起来悬浮于真实物体上面或下面，然后（看起来）一直在漂移。这个现象可以在 Pico 4E 上观察到，即使不使用 EasyAR 只打开它自己的 VST 也有同样的现象。
### 步骤一：查看 session 运行状态
>
[> UI 消息
](../diagnostics/ui-messages.html)> 中的 session 状态显示正常所必须正常的功能或数据：
>
>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 可用性
`>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 虚拟摄像机
`>
>
如果看不到 session 状态信息的显示，需要尝试修改选项为 [Log](../../../api/unity/easyar.DiagnosticsController.SessionDumpOutputMode.html#u_easyar_DiagnosticsController_SessionDumpOutputMode_Log) 然后在系统日志中阅读 session 的状态和正在使用的 frame source 的名字。
可以尝试删除 [ARSession](../../../api/unity/easyar.ARSession.html) 节点下所有其它 frame source，然后查看是否有什么变化。
### 步骤二：确认 EasyAR 接收到的相机帧计数
>
> 必须正常的功能或数据：
>
>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 相机帧数据
`> 在 Unity 代码层的通路（不包含数据正确性以及到原生层的数据通路）
>
>
这个数据应该随时间增长，否则会在几秒之后显示警告信息。
如果发现这个数值不增长，应该最先解决。
### 步骤三：在设备上录制 EIF，然后在 Unity 编辑器中回放
>
> 必须正常的功能或数据：
>
>
* [> ExternalFrameSource
](../../../api/unity/easyar.ExternalFrameSource.html)> 的
`> 相机帧数据
`> 输入原生层的通路（不包含数据正确性）
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> timestamp
`> （不包括时间点和数据同步）
>
>
点击 `EIF` 来启动录制，再次点击停止。
> **提示**
必须正常停止录制才能获取到可随机索引的 EIF 文件。
在 Unity 编辑器中运行 EIF 数据时最好使用纯净的 EasyAR 场景或使用 EasyAR 的示例以避免场景中存在不正确的配置。
可以在 Unity 编辑器中看到 `相机帧数据` 的回放。图像数据并不是字节相等的，整个流程中存在有损编解码。
EasyAR 会在计算中使用畸变参数但显示时不会对图像做反畸变。所以如果输入了这些数据，当在 Unity 中回放 EIF 文件时，会观察到没有反畸变的数据，这是符合预期的。
> **提示**
修改 Unity game 窗口的比例与输入相同，否则数据会被裁剪显示。
如果数据播放偏快或偏慢，需要检查 `timestamp` 输入。
> **注意**
使用 EIF 可以做很多事情，可以在 Unity 编辑器中使用 EIF 运行 [图像跟踪](../../image-tracking/intro.html) 和 [稠密空间地图](../../dense-spatial-mapping/intro.html) 。注意在设备上运行时显示效果有可能是不一样的。
### 步骤四：使用 EIF 运行图像跟踪
>
> 必须正常的功能或数据：
>
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> intrinsics
`> （数据正确性不能完全保证，因为算法对误差存在容忍度）
>
>
在 Unity 编辑器中使用 EIF 运行图像跟踪示例 ImageTracking\_Targets，需要录制一个图像可以被跟踪到的 EIF。
> **注意**
[图像跟踪](../../image-tracking/intro.html) 需要跟踪目标占据整个图像的一定比例，如果无法跟踪到图像，尝试移动头到更加接近图像的位置。
如果跟踪持续失败或虚拟物体显示在图像中远离目标的位置，则很有可能 `intrinsics` 存在问题。
如果图像数据有畸变，可能会看到虚拟物体不会完美的覆盖图像上的跟踪目标，这是符合预期的。当跟踪目标处于图像边缘时这个现象会更加明显。
### 步骤五：在设备上运行图像跟踪
>
> 必须正常的功能或数据：
>
>
> 设备自身的显示系统
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> intrinsics
`> （数据正确性不能完全保证，因为算法对误差存在容忍度）
>
* `> 相机帧数据
`> 中的
`> extrinsics
`>
* `> 相机帧数据
`> 和
`> 渲染帧数据
`> 中
`> device pose
`> 的坐标一致性
>
* `> 相机帧数据
`> 和
`> 渲染帧数据
`> 中
`> device pose
`> 的时间差
>
>
> **注意**
[图像跟踪](../../image-tracking/intro.html) 需要跟踪目标占据整个图像的一定比例，如果无法跟踪到图像，尝试移动头到更加接近图像的位置。
[图像跟踪](../../image-tracking/intro.html) 需要图像横向边长与真实世界中物体的大小一致，在示例中需要跟踪一个横向边长撑满水平摆放的 A4 纸长边的图像，因此不要跟踪显示在电脑屏幕上的图像，除非使用一把尺子并参照尺子将图像横向边长调整到 A4 大小。
如果在使用 EIF 时图像跟踪很完美但在设备上却不同，需要在继续其它测试前解决它。在后续步骤中解决问题要困难得多。
如果虚拟物体悬浮显示在某个远离真实物体的地方，而且即使人不动也是如此，那很有可能 `intrinsics` 或 `extrinsics` 不正确或 `相机帧数据` 和 `渲染帧数据` 中 `device pose` 不在同一个坐标系，或者显示系统产生了这个误差。
如果虚拟物体在移动头部的时候持续移动并且看起来就像是有延迟一样，那有很大可能性 `device pose` 不够健康。这经常发生于几种情况（不能排除有其他问题的可能性），
* `device pose` 与 `raw camera image data` 的数据时间不同步
* `相机帧数据` 和 `渲染帧数据` 中使用了相同的 pose
### 步骤六：使用 EIF 并在设备上运行稠密空间地图
>
> 必须正常的功能或数据：
>
>
> 设备自身的显示系统
>
* `> 相机帧数据
`> 中的
`> raw camera image data
`>
* `> 相机帧数据
`> 中的
`> intrinsics
`> （数据正确性不能完全保证，因为算法对误差存在容忍度）
>
* `> 相机帧数据
`> 中的
`> extrinsics
`>
* `> 相机帧数据
`> 中的
`> device pose
`>
>
如果网格生成速度非常慢和/或地面重建坑坑洼洼，那非常有可能 `device pose` 有问题。也有可能 pose 的坐标系不正确或 pose 的时间点不对。
> **提示**
如果输入数据帧率较低，网格生成速度也会变慢，但质量不会明显变差。这种情况是符合预期的。
通常分辨精确的网格位置不是非常容易，所以在使用 [稠密空间地图](../../dense-spatial-mapping/intro.html) 时显示系统误差不一定能观察出来。
## 运行 Mega 示例
阅读以下内容了解如何在 Unity 中使用 Mega。如果您还没有开通 Mega 服务，需联系 EasyAR 商务获取试用资格。
* [EasyAR Mega 简介](../../mega/intro.html)
* [我的定位库可以使用了吗？](../../mega/localization-verify.html)
* [使用 EasyAR Mega Unity 样例快速入门](../mega/quickstart.html)
然后在设备上运行 `Mega` ，与手机运行效果对比一致（建议以 iPhone 为标准）。关注
* 物体显示位置是否正确
* 远处（10M 及以外）物体显示位置和大小是否正确
* 视线中心以外物体显示位置和大小是否正确
* 转动头部时物体显示位置和大小是否正确
## 解决运行中的异常情况
>
> 必须正常的功能或数据：
>
>
> 设备自身的显示系统
>
* `> 相机帧数据
`> 和
`> 渲染帧数据
`> 中的所有数据
>
>
在完成 [图像跟踪](../../image-tracking/intro.html) 以及 [稠密空间地图](../../dense-spatial-mapping/intro.html) 两个功能的验证后，理论上 EasyAR Mega 应该已经被支持了。如果在头显上运行的表现明显比手机上差，需要关注以下内容，
* 关注 `相机帧数据` 和 `渲染帧数据` 中的 pose 数据和 timestamp
* 关注运动跟踪/VIO 系统输出。`XR Origin` 下面的熊猫会是一个好的参考
另外，还需要重点关注设备自身的显示系统，尤其是远处、视线中心以外以及转动头部时的物体显示效果。这类场景在设备自身测试时经常会被忽略，但通常问题依然是设备自身的显示系统导致的，您需要向 EasyAR 说明这些问题和可能的影响，并为开发者提供合理效果预期。
> **重要事项**
用户使用时会非常关注这些显示问题，而很多设备也确实无法在大空间场景提供非常完美的显示效果。EasyAR 无法解决设备自身的显示问题，这需要设备厂商迭代解决，与此同时，用户也需要理解这些问题。
## 后续步骤
* [发布扩展包](extension-dist.html)
## 相关主题
可以在手机上运行的示例：
* 图像跟踪示例 ImageTracking\_Targets，可以通过它了解 [图像跟踪](../../image-tracking/intro.html) 功能的预期执行效果功能
* 稠密空间地图示例 SpatialMap\_Dense\_BallGame，可以通过它了解 [稠密空间地图](../../dense-spatial-mapping/intro.html) 功能的预期执行效果
* 运动融合示例 ImageTracking\_MotionFusion，可以通过它了解 [运动融合](../../image-tracking/motion-fusion.html) 功能的预期执行效果
* Mega 示例 MegaBlock\_Basic，可以通过它了解 [Mega](../../mega/intro.html) 功能的预期执行效果

---

## 发布扩展包
- 章节路径: `unity/headsets/extension-dist.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-dist.html

# 发布扩展包
本文介绍完成开发和运行验证后，如何将为特定头显开发的 EasyAR Sense Unity Plugin 扩展打包发布，以便用户可以方便地使用该扩展。
## 开始之前
* 完成 [让头显支持 EasyAR](extension-imp.html) 开发。
* 完成 [运行验证（bring-up）](extension-bring-up.html)，确保设备上运行效果正常。
## 完成包定义
包本身的定义在 `package.json` 中，可以根据 [Unity 创建自定义 package 的指南](https://docs.unity3d.com/Manual/CustomPackages.html) 来修改这个文件或创建一个新的包。注意确保修改 package 的 `name` 和 `displayName`，注意不要与 EasyAR 提供的模板本身或其它供应商的扩展发生冲突。
## 重新生成 meta 文件
删除并重新生成 package 中所有文件的 .meta 文件。否则它们会与模板本身或其它供应商的扩展发生冲突。
> **注意**
Unity 可能会缓存 .meta 文件，建议在 Unity 关闭状态下，删除包内所有 .meta 文件，并整个删除 `Library` 目录，然后重新打开 Unity 工程以重新生成 .meta 文件。
注意场景和资源文件中的引用都会变化，有可能需要重新创建或修改场景中的部分物体。文本替换 .unity 以及其它资源文件中的 GUID 是一种可行的方法。
## 检查版本兼容性
检查扩展与设备 SDK 以及 EasyAR Sense Unity Plugin 的版本兼容性。
> **注意**
从版本 4000 开始，EasyAR Sense Unity Plugin 遵循 Unity 所要求的 semantic versioning。在这之前每个小版本都可能会包含不兼容的更改。
## 打包发布
您可能还希望修改 package 中的其它一些文件，确保在发布前仔细审查整个 package。
建议使用 Unity package 来打包文件。如果设备 SDK 并没有准备好以 Unity package 形式发布，也可以选择通过 asset package 来发布。
需要提醒用户，EasyAR license key 的所有限制（尤其是针对自定义相机的限制）都适用于您的扩展包。

---

## 让头显支持 EasyAR
- 章节路径: `unity/headsets/extension-imp.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-imp.html

# 让头显支持 EasyAR
本文介绍如何使用 EasyAR Sense Unity Plugin 的头显扩展包模板来开发一个支持头显设备的 EasyAR 扩展包。
## 开始之前
在进入开发之前，需要先了解如何使用 EasyAR Sense Unity Plugin。
* [快速入门](../getting-started/quickstart.html)
* 运行 [AR Session 示例](../fundamentals/sample-arsession.html)、图像跟踪示例 ImageTracking\_Targets 和稠密空间地图示例 SpatialMap\_Dense\_BallGame，它们的运行效果在手机上和头显上是相似的。
头显插件开发会涉及一些基础功能，需要先了解这些内容：
* 了解 [AR Session](../fundamentals/session.html)
* 了解 [帧数据源](../cameras/frame-source.html) 和 [外部帧数据源](../cameras/external-frame-source.html)
此外，还需要熟悉 [如何开发一个 Unity 的 package](https://docs.unity3d.com/Manual/CustomPackages.html)。
## 为 AR/MR 准备设备
* 准备运动跟踪/VIO 系统
确保设备跟踪误差受控。一些 EasyAR 功能比如 Mega 可以在某种程度上降低设备累积误差，但大的局部误差也会让 EasyAR 的算法变得不稳定。通常来讲，通常我们期望 VIO 漂移在 1‰ 以内。
* 准备显示系统
确保当一个与现实中某个物体大小和轮廓相同的虚拟物体被放置在虚拟世界中，且它与虚拟摄像机的相对变换关系与真实世界中对应物体与设备的变换关系相同时，虚拟物体可以贴合显示在真实物体上，且移动设备或转头不会打破显示效果。可以参考 Vision Pro 的效果。
* 准备设备 SDK
确保已经有 API 可以提供 [外部输入帧数据](../cameras/external-input-frame.html) 。这些数据应该由系统中的两个且只有两个时间点产生，需要确保不会出现数据无法对齐的情况。
## 使用头显扩展包模板
通过 Unity 的 [Package Manager window](https://docs.unity3d.com/Manual/upm-ui.html) 来 [使用本地 tarball 文件安装插件](https://docs.unity3d.com/Manual/upm-ui-tarball.html) 导入 `EasyAR Sense Unity Plugin` （package `com.easyar.sense`）。解压头显扩展模板 （package `com.easyar.sense.ext.hmdtemplate`）到 Unity 工程的 Packages 目录，并重命名 `Samples\~` 文件夹为 `Samples` 。
这时应看到这样的目录结构：
```
.
├── Assets
└── Packages
└── com.easyar.sense.ext.hmdtemplate
├── CHANGELOG.md
├── Documentation\~
├── Editor
├── LICENSE.md
├── package.json
├── Runtime
└── Samples
└── Combination\_BasedOn\_HMD
```
> **提示**
如有需要，可以使用任何 Unity 允许的方式来导入 `EasyAR Sense Unity Plugin` 和存放头显扩展模板。
如果不使用模板，也可以参考 [Unity 创建自定义 package 的指南](https://docs.unity3d.com/Manual/CustomPackages.html) 来创建一个新的 package。
如果设备 SDK 未使用 Unity 的 package 来组织，需要解压头显扩展模板到 Unity 的 Assets 文件夹，然后从解压的文件中删除 package.json 以及任何以 .asmdef 为后缀名的文件。请注意在这种使用方式下，同时使用设备 SDK 与 EasyAR 的用户将无法获得合理的版本依赖。
## 完成运行时输入扩展
遵循 [创建图像和设备运动数据输入扩展](../cameras/external-device-frame-source.html) 方法，修改 `Runtime/HMDTemplateFrameSource.cs` 并完成适用于头显的输入扩展。这是扩展包最主要的开发工作。
## 完成编辑器菜单
修改 `MenuItems` 类中的 "HMD Template" 字符串为代表设备的名称。如果需要其它自定义编辑器功能，也可以添加其它脚本。
开发者在 `Hierarchy` 视图中选中 **AR Session (EasyAR)** 并点击右键时会出现这些菜单项：
* `EasyAR Sense` > `Extensions` > `Frame Source : [Device Name]`：在当前 session 中添加一个该设备的帧数据源。
* `EasyAR Sense` > `Extensions` > `Frame Source : [Device Name (keep it only)]`：在当前 session 中添加并仅保留一个该设备的帧数据源。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-context-menu.png)
## 完成应用示例
示例位于 `Samples/Combination\_BasedOn\_HMD`。简单起见，示例模板中没有代码，全部 AR 功能靠场景内容及配置即可完成。
1. 添加支持设备运行的内容到场景中。
> **提示**
如有需要，也可以反过来做，使用一个可以在设备上运行的场景，然后添加 EasyAR 组件和 sample 场景中的其它物体到场景中。
2. 修改设计用来放在 session 原点下的物体。
如果场景中定义了 session 原点，移动 `EasyARPanda` 和 `UI` 到原点节点下。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-ui.png)
`EasyARPanda` 会提供一个设备运动跟踪行为的参照，这会帮助判断跟踪不稳定时候的原因。
这些物体名称括号内的文字是给扩展开发者看的提示，可以删除：
* `(Move into Origin if there is any)`
* `(Move into Origin if there is any, set constraint source to your rendering camera)`
* 配置 `HUD` 按钮行为。
设置 `UI` 的 constraint source 为虚拟摄像机，以确保 `HUD` 按钮可以按预期工作。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-hud.png)
* 配置 `Canvas` 的 raycast 功能。
修改 `UI` 节点下的 `Canvas`，确保 raycast 可以工作，以保证所有 UI 按钮和开关可以按预期工作。
模板中已经在 `Canvas` 节点下预先添加了 [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/index.html) 的 [Tracked Device Graphic Raycaster](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/tracked-device-graphic-raycaster.html)，导入对应的 package 之后即可看到。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-raycaster.png)
如果在设备上运行时不使用 [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.4/manual/index.html)，会看到类似下面的缺少脚本提示，可以将其删除，并添加设备所需的 raycaster 组件。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/extension-sample-raycaster-missing.png)
## 后续步骤
* 在进一步完成扩展包之前，需要先 [运行验证（bring-up）](extension-bring-up.html) 输入扩展
* 全部完成之后，可以准备 [发布扩展包](extension-dist.html)
## 相关主题
* [扩展包模板参考](extension-template.html)
* [外部输入帧数据](../cameras/external-input-frame.html)
* [创建图像和设备运动数据输入扩展](../cameras/external-device-frame-source.html)

---

## 头显扩展包模板简介
- 章节路径: `unity/headsets/extension-template.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension-template.html

# 头显扩展包模板简介
`com.easyar.sense.ext.hmdtemplate` package 是为头显扩展开发提供的示例和模板。它是一个 SDK 的实现，并且包含了给应用开发者的示例。
## 模板内容
这个 package 的包结构遵循了 [Unity 推荐的文件布局](https://docs.unity3d.com/Manual/cus-layout.html)：
```
.
├── CHANGELOG.md
├── Documentation\~
├── Editor
├── LICENSE.md
├── package.json
├── Runtime
└── Samples\~
└── Combination\_BasedOn\_HMD
```
其中一些比较重要的内容如下：
* **Runtime**：存放运行时平台资产的文件夹。这是模板中最重要的文件夹。
* **Samples\~**：存放 package 中所有示例的文件夹。它包含给下游使用的示例，可以用作测试扩展的 demo。为了原地开发这个示例，需要修改文件夹名为 `Samples` 。使用 [Client.Pack](https://docs.unity3d.com/ScriptReference/PackageManager.Client.Pack.html) 方法会在打包一个新的发布时将其自动重命名为 `Samples\~` 。
* **Editor**：存放编辑时平台资产的文件夹。这个文件夹的脚本主要用于创建菜单项。
* **package.json**：package 的清单文件。
## 模板示例的创建过程
1. [添加 AR Session](../fundamentals/session-creation.html)
在 `Hierarchy` 视图中：
* 在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Mega` > `AR Session (Mega Block Default Preset)` 添加 [ARSession](../../../api/unity/easyar.ARSession.html)。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Frame Filter : Image Tracker` 添加一个 [ImageTrackerFrameFilter](../../../api/unity/easyar.ImageTrackerFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `SpatialMap` > `Frame Filter : Dense SpatialMap Builder` 添加一个 [DenseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.DenseSpatialMapBuilderFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `SpatialMap` > `Frame Filter : Sparse SpatialMap Builder` 添加一个 [SparseSpatialMapBuilderFrameFilter](../../../api/unity/easyar.SparseSpatialMapBuilderFrameFilter.html) 到 session 中。
* 选中 **AR Session (EasyAR)** 并点击右键，通过菜单 `EasyAR Sense` > `Extensions` > `Frame Source : HMD Template (keep it only)` 添加并仅保留 HMD Template 这一个 [FrameSource](../../../api/unity/easyar.FrameSource.html)。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-session.png)
* 添加 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html)
在 `Hierarchy` 视图中，在 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Image Tracking` > `Target : Image Target` 添加一个 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html) 到 session 中。
配置 [ImageTargetController](../../../api/unity/easyar.ImageTargetController.html)：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-image-target.png)
在完成上述配置之后，`Scene` 视图中显示的图像是 gizmo。这个示例中通过一个 quad 来显示同一图像的虚拟物体。
添加显示在 target 上面的虚拟物体：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-image-target-content.png)
* 添加一个模型作为运动跟踪原点参考
这个模型对开发者以及下游用户都很重要，它用于解耦设备运动跟踪和 EasyAR 算法。
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-origin-content.png)
* 添加功能选择的 UI
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-ui.png)
* 关闭启动时启用的 EasyAR 功能，并通过 UI 开关来打开它们
例如，图像跟踪的功能在启动时可以关闭，只需要设置对应组件的 enable 为 false 即可：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-feature-off.png)
然后添加 UI 开关处理：
![alt text](https://doc-asset.easyar.com/develop/unity/headsets/media/template-ui-switch.png)
## 相关主题
* [让头显支持 EasyAR](extension-imp.html) 介绍了如何使用这个模板来创建一个新的头显扩展包
* [运行验证（bring-up）](extension-bring-up.html) 介绍了如何利用这个模板提供的示例验证输入扩展的正确性
* [发布扩展包](extension-dist.html) 介绍了如何基于这个模板完成最后的打包分发

---

## EasyAR Unity 头显扩展包
- 章节路径: `unity/headsets/extension.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/extension.html

# EasyAR Unity 头显扩展包
本文档介绍了 EasyAR Unity 头显扩展包的概念、能力边界以及创建头显扩展包所需的背景知识。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
* 阅读 [Unity 中的 EasyAR 头显支持](headsets.html) 了解在 Unity 中 EasyAR 头显支持的整体架构。
## EasyAR Unity 头显扩展包是什么
EasyAR Unity 头显扩展包是一个 Unity package，包含一系列代码和示例，帮助您在您的头显设备上使用 EasyAR Sense 的功能。通过这个扩展包，您可以将 EasyAR Sense 的大部分功能（如图像跟踪、稠密空间地图等）集成到您的设备上，从而利用 EasyAR 提供的强大 AR 功能。
使用 EasyAR Unity 头显扩展包是 EasyAR 头显支持的其中一种方式。下图展示了 EasyAR 在 Unity 中的整体架构，以及头显扩展包在其中的位置。
```
block
columns 4
block:groupApp:4
block:groupAppWrapper
space
App1["EasyAR + Device A<br>App"]
space
App2["EasyAR<br>App"]
space
App3["EasyAR + Device B<br>App"]
end
end
block:groupSensePluginExtension
columns 1
SensePluginExtension["EasyAR Sense Unity Plugin<br>Extension for Device A"]
space
end
block:groupSensePlugin
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupDeviceAUnity
columns 1
DeviceAUnity["Device A<br>Unity SDK"]
space
end
block:groupSense
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
MDeviceB["Device B<br>CameraDevice"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:4
columns 1
System["Native Library"]
block:groupSystemWrapper
space
DeviceA["Device A<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
space
DeviceB["Device B<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePluginExtension --> App1
SensePlugin --> App1
SensePlugin --> App2
SensePlugin --> App3
ARF --> App3
XRI --> App1
XRI --> App3
groupSense --> SensePlugin
groupDeviceAUnity --> SensePluginExtension
SensePlugin --> SensePluginExtension
DeviceA --> groupDeviceAUnity
DeviceA --> XRSDK
XRSubsystem --> ARF
XRSubsystem --> XRI
DeviceB --> MDeviceB
DeviceB --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style DeviceAUnity fill:none,stroke:none,stroke-width:0px
style Sense fill:none,stroke:none,stroke-width:0px,color
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePluginExtension fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class SensePluginExtension EasyAR
```
图中列出了两种典型的头显支持方式：通过 Unity 头显扩展包对接设备 SDK（Device A），以及在 EasyAR Sense 库中直接对接设备 SDK（Device B）。本文档主要介绍前者。
## 我可以创建自己的头显扩展包吗？
目前，AR/VR/MR/XR 行业内还没有形成非常统一的接口方案，虽然 OpenXR 是个很好的候选，但规范演化和行业实现还需要时间。所以通常来说市贩设备直接运行 EasyAR 并不那么容易，大概率存在数据接口缺失的情况。随着行业的发展，一些新兴设备也可能具备良好的接口支持，比如 2024 年苹果公司开放了 Vision Pro 的相关接口，这些接口已经足够用来支撑 EasyAR 运行，不过使用起来还是需要一些专业知识。
如果您无法做出判断，建议联系硬件制造商或 EasyAR 商务以获取相应的设备支持。
如果您是硬件制造商，并且希望在您的设备上支持 EasyAR 的功能，您可以参考接下来的文档内容来创建一个头显扩展包，从而让 EasyAR 的大部分功能可以在您的设备上运行。本文档在提供数据和接口规范的同时并不限定所有实现细节，任何实现方式或接口定义都可以讨论，欢迎通过商务渠道联系沟通。
本文档覆盖的硬件自身需要有运动跟踪或 SLAM 能力，EasyAR 的功能需要运行在良好的设备跟踪能力之上，通常不建议靠 EasyAR 的功能优化设备的跟踪，这会产生循环依赖进而理论上放大误差并导致整体系统趋于不稳。如果设备本身没有运动跟踪能力，那么支持方案并不在本文档覆盖范围之内，如有需要可通过商务渠道进行沟通。
## 头显扩展包的能力边界
头显扩展包的目标是让 EasyAR Sense 的大部分功能可以在您的设备上运行。为了实现这个目标，您需要了解头显扩展包的能力边界。
### 头显扩展包所包含的内容
您将实现的扩展是：
* 使用 [自定义相机功能](../../cameras/custom-camera.html)，从您的设备 API 抓取数据并发送进 `EasyAR Sense` 的一系列代码。
* 在 Unity 中，头显扩展会使用 [外部帧数据源](../cameras/external-frame-source.html) 和 `EasyAR Sense Unity Plugin` 定义的一套 `EasyAR Sense` 数据流来简化自定义相机开发。
* 在 Unity 中，头显扩展是一个 [Unity package](https://docs.unity3d.com/Manual/Packages.html)，包含运行时脚本，编辑器脚本和扩展的 sample，您或 EasyAR 可以将它分发给下游用户。
> **提示**
如果您不希望将对接细节暴露在外部系统中，可以联系 EasyAR 进行沟通。在 EasyAR Sense 内部使用 C 接口直接对接是可行且有先例的。
您在实现扩展的时候，可能会：
* 修改您 SDK 的**接口设计和内部实现**。
* 与您的**团队**一起讨论确认数据获取和使用方案。
* 花**大量**时间进行数据正确性验证而不是写代码。
完成扩展后，您将会看到：
* 大多数 `EasyAR Sense` 功能在您的设备上可以使用，这些功能会利用您设备的运动跟踪能力。
* `EasyAR Sense` 内支持的 EasyAR 云服务在您的设备上可以使用。
* 只能使用 EasyAR XR license。个人版、专业版以及经典版的 license 无法在您的设备上使用。
* 使用自定义相机时的所有 EasyAR license 的限制以相同方式适用于您的设备。
### 头显扩展包所不包含的内容
这个扩展不能脱离 `EasyAR Sense` 使用：
* 这个头显扩展不会独立运行，作为依赖，`EasyAR Sense` 也是需要的。在 Unity 中则必须使用 `EasyAR Sense Unity Plugin`。
* 它不会直接调用 EasyAR 云服务 API（比如 EasyAR Mega 定位服务），这些调用会在 `EasyAR Sense` 内部完成。
* 在 Unity 中，它不会直接调用 AR 功能（比如图像跟踪）的接口方法，它们在 `EasyAR Sense Unity Plugin` 内部完成。
* 在 Unity 中，它不会修改场景中物体或跟踪目标的 transform，它们在 `EasyAR Sense Unity Plugin` 内部完成。
这个扩展不能脱离您的设备 SDK 使用：
* 在 Unity 中，头显扩展或 `EasyAR Sense Unity Plugin` 不会修改场景中相机的 transform，这必须在您的设备 SDK 或其依赖路径中完成。
通过头显扩展有一些 EasyAR 功能仍是无法使用的：
* 表面跟踪功能将无法使用。
* EasyAR 自身的运动跟踪将无法使用。
* 平面检测（EasyAR 运动跟踪的一部分）将无法使用。
## 如何在我的设备上使用 Mega？
在设备上运行 Mega 是很多用户关心的问题。在 Unity 中，Mega 服务是运行在 `EasyAR Sense` 诸多基础功能之上的一个功能模块，所以只要您的设备完整支持 `EasyAR Sense`，那么 Mega 也会被支持。
一般来说，不建议在一开始就直接在设备上运行 Mega 示例来验证设备对 Mega 的支持情况，因为 Mega 会综合利用所有输入数据，并且其对这些数据的误差容忍度较大。直接运行 Mega 示例很可能会因为数据接口不匹配或数据质量不佳而导致无法获得合理的运行效果，并且无法判断问题出在哪里，这会为日后的调试带来很大困难。
> **重要事项**
Mega 服务对设备的运动跟踪能力有一定要求。如果设备的运动跟踪能力不佳，那么 Mega 的表现也会受到影响。在大范围 AR 场景中，还需要特别关注室内外的表现差异。
> **重要事项**
Mega 一般服务于大空间场景，因此需要格外关注远距离物体以及转动头部或移动时物体的 **显示** 效果。如果设备的显示系统误差较大，那么即使 Mega 本身运行正常，用户也会感觉虚拟物体无法正确贴合现实物体。
## 需要的背景知识和团队配置
创建头显扩展包不是一个简单的任务，需要您和您的团队在多个领域进行深入的工作。通常来说，要完成头显扩展，需要 Unity 开发参与的同时投入 Unity 开发之外的团队人员。由于缺少标准，只在 3D 引擎上面修改通常无法完成头显扩展，建议从第一天起就让系统工程师和 SDK 工程师等底层开发工程师参与进来。
打造 AR/VR 设备需要一些领域知识，相似地，在设备上运行和验证 EasyAR Sense 将需要您或您的团队是如下领域的专家：
* 您设备的物理结构和渲染系统
* 相机系统几何
* SDK 开发
* 常规 Android debug 技能，比如 adb（[中国大陆](https://developer.android.google.cn/tools/adb)，[国际](https://developer.android.com/tools/adb)）
如果您工作在 Unity 上，您还需要知道这些：
* [Unity 开发基础和 package 使用](https://docs.unity3d.com/Manual/Packages.html)
* [Unity package 开发](https://docs.unity3d.com/Manual/CustomPackages.html)
* C# 语言基础，包括 [IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable) 等
另外，有一点在这些领域的知识将帮助您更好地理解系统，尤其是如何发送正确的数据到 EasyAR：
* Android 开发（[中国大陆](https://developer.android.google.cn)，[国际](https://developer.android.com)）
* 几何视觉，尤其是图像匹配和 3D 重建
## 后续步骤
在接下来的文章中，您将了解创建头显扩展包的完整流程：
* [让头显支持 EasyAR](extension-imp.html) 介绍了如何使用模板来创建一个新的头显扩展包，并完成基本的输入扩展开发
* [运行验证（bring-up）](extension-bring-up.html) 介绍了如何在设备上验证输入扩展的正确性
* [发布扩展包](extension-dist.html) 介绍了如何将头显扩展包打包并分发给下游用户
## 相关主题
* [扩展包模板参考](extension-template.html)
* [运动跟踪](../../motion-tracking/intro.html)
* [运动跟踪与 EasyAR 功能](../../motion-tracking/motion-tracking-and-easyar.html)

---

## Unity 中的 EasyAR 头显支持
- 章节路径: `unity/headsets/headsets.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/headsets.html

# Unity 中的 EasyAR 头显支持
本文档介绍了在 Unity 中 EasyAR 头显支持的整体架构和注意事项。
## 开始之前
* 阅读 [EasyAR 的头显支持](../../headsets/headsets.html) 了解 EasyAR 已经支持的头显类型和头显上可以运行的 EasyAR 功能。
## 头显支持概述
EasyAR 在 Unity 中支持头显的方式比较灵活，常见有两种方式：
* 内置支持：通常在 EasyAR Sense 库中直接对接设备 SDK，并在 Unity 中提供对应的接口 （比如 Apple Vision Pro）
* 扩展支持：通过 Unity 头显扩展包对接设备 SDK （比如 Pico）
```
block
columns 4
block:groupApp:4
block:groupAppWrapper
space
App1["EasyAR + Device A<br>App"]
space
App2["EasyAR<br>App"]
space
App3["EasyAR + Device B<br>App"]
end
end
block:groupSensePluginExtension
columns 1
SensePluginExtension["EasyAR Sense Unity Plugin<br>Extension for Device A"]
space
end
block:groupSensePlugin
columns 1
SensePlugin["EasyAR Sense Unity Plugin"]
space
end
block:groupXRI
columns 1
XRI["XR Interaction Toolkit"]
space
end
block:groupARF
columns 1
ARF["AR Foundation"]
space
end
block:groupDeviceAUnity
columns 1
DeviceAUnity["Device A<br>Unity SDK"]
space
end
block:groupSense
columns 1
Sense["EasyAR Sense"]
block:groupSenseWrapper
MDeviceB["Device B<br>CameraDevice"]
Others["..."]
end
end
block:groupXRSubsystem:2
columns 1
XRSubsystem["XR Subsystems"]
XRSDK["Unity XR SDK"]
end
block:groupSystem:4
columns 1
System["Native Library"]
block:groupSystemWrapper
space
DeviceA["Device A<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
space
DeviceB["Device B<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Library&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
space
end
end
SensePluginExtension --> App1
SensePlugin --> App1
SensePlugin --> App2
SensePlugin --> App3
ARF --> App3
XRI --> App1
XRI --> App3
groupSense --> SensePlugin
groupDeviceAUnity --> SensePluginExtension
SensePlugin --> SensePluginExtension
DeviceA --> groupDeviceAUnity
DeviceA --> XRSDK
XRSubsystem --> ARF
XRSubsystem --> XRI
DeviceB --> MDeviceB
DeviceB --> XRSDK
style groupApp fill:none,stroke:none,stroke-width:0px
style groupAppWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePlugin fill:none,stroke:none,stroke-width:0px
style groupARF fill:none,stroke:none,stroke-width:0px
style groupXRI fill:none,stroke:none,stroke-width:0px
style DeviceAUnity fill:none,stroke:none,stroke-width:0px,color:#fff
style Sense fill:none,stroke:none,stroke-width:0px,color:#fff
style groupSenseWrapper fill:none,stroke:none,stroke-width:0px
style XRSubsystem fill:none,stroke:none,stroke-width:0px,color
style System fill:none,stroke:none,stroke-width:0px
style groupSystemWrapper fill:none,stroke:none,stroke-width:0px
style groupSensePluginExtension fill:none,stroke:none,stroke-width:0px
classDef EasyAR fill:#6e6ce6,stroke:#333,color:#fff
class groupSense EasyAR
class SensePlugin EasyAR
class SensePluginExtension EasyAR
classDef Device fill:#636,stroke:#333,color:#fff
class groupDeviceAUnity Device
class DeviceB Device
class DeviceA Device
```
>
> 图中：
>
>
> 设备 A 属于扩展支持
>
> 实践中设备 A 通常会有对应的 Unity SDK，用于对接 Unity XR SDK 或者独立实现头显渲染能力。
>
> 设备 A 的头显扩展包负责将 EasyAR Sense Unity Plugin 和设备 A 的 Unity SDK 对接起来，从而实现 EasyAR 在设备 A 上的运行。这个支持包可能由 EasyAR 提供，也可能由设备厂商提供。
>
>
> 设备 B 属于内置支持
>
> 实践中设备 B 可能有也可能没有对应的 Unity SDK，取决于设备厂商的实现。比如 Apple Vision Pro 没有对应的 Unity SDK，XREAL 有对应的 Unity SDK。
>
>
>
内置支持和扩展支持的头显都支持使用了 [自定义相机](../../cameras/custom-camera.html)。
> **重要事项**
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
在 Unity 中，虚拟摄像机的渲染、投影矩阵 和 transform 等不受 EasyAR 控制，它们通常由设备 SDK 或 Unity XR SDK 控制。设备自身的功能，比如手势识别、眼动追踪等，仍然由设备及设备 SDK 提供。在使用时，通常需要同时使用 EasyAR 和设备 SDK。
## 后续步骤
* [使用头显样例](samples.html)
* [启用头显支持](enable-headset.html)
* 工程配置
* [Vision Pro 工程配置](setup-visionpro.html)
* [XREAL 工程配置](setup-xreal.html)
* [其它 Android 设备工程配置](../fundamentals/setup-player.html)
* [创建 EasyAR 头显扩展包](extension-imp.html)

---

## 在 XR 头显或眼镜上使用 EasyAR 样例
- 章节路径: `unity/headsets/samples.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/samples.html

# 在 XR 头显或眼镜上使用 EasyAR 样例
EasyAR 对所有头显提供统一的样例，样例中没有任何代码，全部由场景中配置实现。功能本身的使用可以参考相关功能在 Android/iOS 手机上样例实现。
头显样例名称为 `Combination\_BasedOn\_\*` , 比如 Pico 的样例为 `Combination\_BasedOn\_Pico`。 该样例在一个场景中演示了大部分 EasyAR 功能，它们可以动态开关，可以单独使用，也可以同时打开。
## 准备工作
* 确定您的头显或眼镜当前在 EasyAR [支持列表](../../headsets/headsets.html)
* 下载并导入 [EasyAR Unity 插件包](https://www.easyar.cn/view/download.html)
* 下载并导入 [EasyAR Unity XR设备扩展包](https://www.easyar.cn/view/download.html)
* 获取适合 XR 头显或者眼镜的 EasyAR 许可证，头显或眼镜可用 License 类型包括
* EasyAR Sense 4.x **XR License** 试用版（试用，在 EasyAR 网站自主开通）
* EasyAR Sense 4.x **XR License** 正式版（付费后使用，请联系商务购买开通）
* EasyAR Sense 4.x **XR License** 企业版（企业版 SDK 使用）
> **小心**
头显和眼镜上**仅允许使用 XR License**，普通 License 无法使用 EasyAR 功能。
## 导入官方样例
1. 内建支持的设备的样例位于 EasyAR Unity 插件包中，根据设备单独导入需要的样例。
![xr-samples-location](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-samples-location.png)
2. 通过扩展支持的设备样例随对应的头显扩展一起分发。可以使用 Unity 将样例导入工程中。以Pico为例。
![xr-pico-extension](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-pico-extension.png)
## 样例打包并运行
分别完成头显工程配置和样例使用说明。
* 严格参照对应头显官方的文档和说明做好对应的配置，EasyAR 文档中不会覆盖相关内容。
* 按照 EasyAR 文档中各平台说明进行配置。
Android: 请参考 [Android 工程配置](../fundamentals/setup-player.html)
visionOS: 请参考 [visionOS 工程配置](setup-visionpro.html)
XREAL 除了按照 Android 平台设置外，额外需要 [XREAL 工程配置](setup-xreal.html)
* 样例打包
在 Unity 里打包样例使用，并部署到设备上运行。具体方法参见 [Unity上运行样例](../getting-started/quickstart.html)。
## 用法说明
样例内置多个按钮，其具体功能如下。
![xr-sample-usage-7](https://doc-asset.easyar.com/develop/unity/headsets/media/xr-sample-usage-7.png)
* 按钮1 `HUD`：切换UI显示模式，初始状态UI会固定在现实世界中，打开HUD之后UI会始终显示在眼前。
* 按钮2 `Record`：开关EIF录制。打开之后必须关闭才能录制正常的EIF文件，否则录出来的文件将无法使用。
* 按钮3 `Image`：开关图像跟踪。
* 按钮4 `Image Fusion`：开关图像跟踪+运动融合模式。
* 按钮5 `Dense`：开关稠密空间建图。
* 按钮6 `Sparse`：开关稀疏空间建图。
* 按钮7 `Mega`：开关 Mega。
## 功能详解
* 默认功能开关
所有功能启动时默认都是**关闭**的，这是通过在编辑器上将对应脚本停用实现的，按钮操作操作的是对应脚本的启用/停用，可以根据实际要运行的样例设置默认启用的功能。
![hmd-default-disable](https://doc-asset.easyar.com/develop/unity/headsets/media/hmddefault-all.png)
* 坐标系原点参照
样例中在[运动跟踪](../../motion-tracking/intro.html)的坐标系原点都放置了一个静止的熊猫模型，用于检查运动跟踪状态。这个模型对于解耦问题是有帮助的，比如在运行 Mega 的时候，有些快速漂移就是设备运动跟踪（即设备自身缺陷）导致的，这时候这个模型也会跟着一起漂移/可以根据需要，调整或删除这个熊猫模型。
* 使用内嵌图像跟踪的识别图
* 样例中预设了平面图像跟踪使用的图像的大小，您需要使用 A4 纸打印 namecard.jpg，必须保持图像的比例不拉伸，不裁剪，尽量充满纸张（下图）。
![namecard](https://doc-asset.easyar.com/develop/unity/headsets/media/namecard.jpg)
* 测量打印完成纸张上名片图案的长度，根据测量的结果，需将 Unity 场景中 `Image Target` 的 `Scale` 设为**与真实物理大小一致**（单位是米）。
![set-the-actual-size](https://doc-asset.easyar.com/develop/unity/headsets/media/set-the-actual-size.png)
* 在 `EasyAR 运动融合` 打开时，只能跟踪固定位置（不能移动）的图像。如果运动融合关闭，图像超出视野的时候就无法跟踪。
* 有时候眼镜视角不能很好的反应相机图像大小，如果识别不到可以尝试让眼镜相机靠近图像。实际使用时建议跟踪更大的图像，比如 5米\*5米 大小。
> **注意**
在头显上无论 EasyAR 运动融合功能是开是关，`image target` 的 `Scale` 参数都必须设置为真实的物理大小，否则显示位置会是错误的。
* Mega 配置
如果你在使用 EasyAR Mega，你需要参考 [Mega Unity 快速入门](../mega/quickstart.html)。

---

## 如何在 Apple Vision Pro 上使用 EasyAR 能力
- 章节路径: `unity/headsets/setup-visionpro.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/setup-visionpro.html

# 如何在 Apple Vision Pro 上使用 EasyAR 能力
本指南将引导您完成 Unity 与 Xcode 的工程配置，为 Apple Vision Pro 应用解锁包括 Mega 云定位在内的全部 EasyAR 核心能力。
## 开始之前
* 学习如何使用[头显样例](samples.html)
* 确保开发环境符合以下要求：
* visionOS 2.0 及以上
* 对应 visionOS 版本的 Xcode 16.0 及以上并安装 visionOS simulator
* 推荐的 Unity 版本 6000.0.23 以上的 LTS 版本
## 向 Apple Inc. 申请企业级 API 许可
由于在 Apple Vision Pro 上获取相机画面及参数是一个需要 **entitlement** 的 **企业级 API**，您需要向 **Apple Inc.** 申请包含该 **entitlement** 的 **license** 文件。该 license 的申请和使用方式请参考 [Building spatial experiences for business apps with enterprise APIs for visionOS](https://developer.apple.com/documentation/visionos/building-spatial-experiences-for-business-apps-with-enterprise-apis)。
> **重要事项**
向苹果公司申请得到的 **entitlement** 中的 **Bundle ID** 应与创建 **EasyAR Sense License Key** 时填写的完全一致。
## 如何选择 visionOS App Mode
运行在 visionOS 上的 App 仅在 **Immersive Space** 下能够获取 ARKit 数据。而 Unity 编辑器打包的 App 在 **Immersive Space** 下基于渲染流程及 API 不同需要选择使用 **RealityKit with PolySpatial** 或 **Metal Rendering with Compositor Services** 模式。
关于 **Immersive Space** 的定义,可以参考苹果[官方文档](https://developer.apple.com/documentation/swiftui/immersive-spaces)。
关于 Unity 的 App Mode 的详细介绍，可以参考 Unity PolySpatial 文档中的 [visionOS Platform Overview](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/visionOSPlatformOverview.html)。
> **提示**
**App Mode 选择建议**
* **首选推荐：RealityKit with PolySpatial**
如果您是首次接触 visionOS，建议优先选择此模式。其优势在于能深度集成 visionOS 的系统级渲染特性，稳定性高，渲染效果好。
此模式不支持自定义代码着色器（HLSL/ShaderLab），必须使用 **Shader Graph**，且仅支持经 PolySpatial 兼容性检查后的特性（会被转换为 MaterialX）。
Unity 内置的 `Standard (Built-in)` 和 `Lit (URP)` 着色器已由官方预先适配，可直接使用。
* **进阶/特定需求：Metal Rendering with Compositor Services**
适用于有大量现有 3D 资产迁移需求或必须使用自定义着色器的复杂项目。
由于该模式下 Unity 负责全部渲染逻辑，绕过了系统的 RealityKit 管线，渲染效果一般不如 RealityKit 并且可能会遇到不可预见的渲染问题。
**EasyAR 接入建议：**
在尝试接入 EasyAR 时，请务必先使用 **RealityKit with PolySpatial** 模式跑通基础流程。这样可以有效隔离变量，避免因 Metal 底层适配问题与 AR 相关问题交织，从而导致难以定位故障成因。
## Unity 工程中的配置
Unity 工程中需要进行以下配置：
### 为 Unity 工程导入必要的 Package
**Unity 6 （推荐）**：
* `com.unity.xr.visionos` (2.0.4+)
* `com.unity.polyspatial` (2.0.4+)
* `com.unity.polyspatial.visionos` (2.0.4+)
* `com.unity.xr.visionos` (2.0.4+)
> **重要事项**
所有 Package 的版本号必须保持严格一致。
建议优先使用 Unity 6，部分早期的 Unity 2023.x 版本对 visionOS 尚不支持。
**Unity 2022.3**：
* `com.unity.xr.visionos` (1.2.3)
* `com.unity.polyspatial` (1.2.3)
* `com.unity.polyspatial.visionos` (1.2.3)
* `com.unity.xr.visionos` (1.2.3)
> **重要事项**
所有 Package 版本号必须保持严格一致。
不支持 **1.3.x** 版本，请务必锁定在 **1.2.3**。
### 选择 Build Platform
点击菜单栏中的 **File** > **Build Profiles** 将 Platform 切换至 **visionOS**。
![切换Build_Platform](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro01.png)
### 配置 Input System
确保使用新版的 `Input System Package`：
点击菜单栏中的 **Edit** > **Project Settings** > **Player**，将 **Active Input Handling** 槽设置为 **Input System Package(New)**。
此后 Unity 可能会要求重启工程，点击 **Apply** 使改动生效。
![InputSystem改动生效](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro02.png)
### 配置 XR Plug-in Management
点击菜单栏中的 **Edit** > **Project Settings** > **XR Plug-in Management**，在 visionOS 选项卡中的 Plug-in Providers 勾选 **Apple visionOS**。
![选择visionOS插件](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro03.png)
### 配置 Apple visionOS 插件
点击菜单栏中的 **Edit** > **Project Settings** > **XR Plug-in Management** > **Apple visionOS**。
根据[前文介绍](#setup-visionpro-how-to-choose-app-mode)选择合适的 **App Mode**。
![选择AppMode](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro04.png)
> **注意**
**Windowed** 模式由于不是运行于 **Immersive Space**，无法使用 AR 能力。
**Hybrid** 模式指开发者需要手动在 **Metal** 和 **RealityKit** 模式间切换，由于使用方式比较复杂，不推荐使用，具体可以参考 [Unity 官方对该模式的说明](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/PolySpatialHybridApps.html)。
接下来在同页面中进行以下修改：
* 在 **World Sensing Usage Description** 槽中添加一段描述。
* 将 **Metal Immersion Style** 设置为 **Mixed**。
* 将 **Reality Kit Immersion Style** 设置为 **Mixed**。
* 勾选 **IL2CPP Large Exe Workaround**。
![修改visionOS插件配置](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro05.png)
### [仅 RealityKit 模式需要] 导入 TextMesh Pro Essentials
点击菜单栏中的 **Edit** > **Project Settings** > **TextMesh Pro** > 点击 **Import TMP Essentials**
![Import TMP Essentials](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro09.png)
> **注意**
目前 **RealityKit with PolySpatial** 模式仅支持 **TextMesh Pro** 文字，若不导入则无法渲染文字。
### [仅 RealityKit 模式需要] PolySpatial 相关设置
点击菜单栏中的 **Edit** > **Project Settings** > **PolySpatial**，在该页面中进行以下修改：
* 设置 **Default Volume Camera Window Config** 为 `Default Unbounded Configuration`。
* 勾选 **Auto-Create Volume Camera**
![设置 PolySpatial](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro06.png)
如果需要另外指定 **Default Volume Camera Window Config**，必须确保其 **Mode** 为 **Unbounded**。
![确认 Mode 是 Unbounded](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro07.png)
场景中如果存在 `Volume Camera`，将其删除。
![删除场景中的 Volume Camera](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro08.png)
> **警告**
* **不支持** `World Transform` 数值不是 `identity` 的 `Volume Camera`。
* 若因**特殊原因**需要在场景中添加一个**唯一**的自定义 `Volume Camera`，请务必：
* 将其 `World Transform` 设为 `identity`。
* 确保其 `Volume Camera Window Configuration` 的 `Mode` 设置为 `Unbounded`。
* 在完全清楚 [Unity 官方文档](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@3.0/manual/VolumeCamera.html)中其含义和用途的前提下使用。
### [使用 Mega 时]添加 Location Usage Description
> **小心**
若在 EasyAR 配置中启用了 **Location** 权限（使用 Mega 功能时），必须添加权限描述信息，否则 Build 将失败。
由于目前 Unity 的 **Project Settings** > **Player** > **visionOS** 选项卡中未显示 **Location Usage Description** 字段，请按照以下步骤配置：
1. **切换平台标签**：将选项卡暂时切换至 **iOS**。
2. **填入描述**：在 **Location Usage Description** 槽位中填入必要的权限用途说明。
3. **切回 visionOS**：将选项卡切回 **visionOS**，刚才填写的配置会自动保留并生效。
![Location Description](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro10.png)
## Xcode 工程中的配置
通过 Unity 打包得到的 Xcode 工程中需要进行以下配置：
### 配置相机数据 entitlement
* 将申请得到的 `Enterprise.license` 文件复制到 Xcode 工程文件目录。
![Copy to Xcode project folder](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro11.png)
* 将 Xcode 工程文件目录中的 `Enterprise.license` 拖入 Xcode 工程中。
![Move into Xcode project](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro12.png)
### 修改 info.plist 使应用能够保存和投送文件
若需要在应用中录制 EIF 并通过 visionOS 的文件应用投送到电脑或其他设备，需要在 `Info.plist` 中增加以下字段并修改：
* 添加 `LSSupportsOpeningDocumentsInPlace` 并将值设置为 `true`。
* 添加 `UIFileSharingEnabled` 并将值设置为 `true`。
![Modify Info.plist](https://doc-asset.easyar.com/develop/unity/headsets/media/setup-visionpro13.png)
> **提示**
添加字段后 Xcode 界面上显示的 `Key` 与手动添加的字符串不同（比如输入了 `LSSupportsOpeningDocumentsInPlace` 但显示 **Supports opening documents in place**，这是正常的）。

---

## XREAL 工程配置方法
- 章节路径: `unity/headsets/setup-xreal.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/headsets/setup-xreal.html

# XREAL 工程配置方法
本章介绍如何配置 Unity 工程使其在 XREAL 头显上使用 EasyAR 的相关功能。
## 准备工作
* 获取适合 XR 头显或者眼镜的 EasyAR 许可证，头显或眼镜可用 License 类型包括
* EasyAR Sense 4.x **XR License 试用版**（试用，在 EasyAR 网站自主开通）
* EasyAR Sense 4.x **XR License 正式版**（付费后使用，请联系商务购买开通）
* EasyAR Sense 4.x **XR License 企业版**（企业版 SDK 使用）
其他许可证均不支持。
* 请通过商务获取 **XREAL** 的企业 License （注意，这个 License 是 XREAL 公司分发的文件，与 EasyAR 的 License 不同）。
* 下载并导入 [XREAL 的 SDK](https://developer.xreal.com/download)
* 下载并导入[EasyAR Unity 插件包](https://www.easyar.cn/view/download.html)
* 下载并导入 [EasyAR Unity XR设备扩展包](https://www.easyar.cn/view/download.html)
* 参考 [Android 工程配置](../fundamentals/setup-player.html)
> **注意**
当前仅支持 XREAL SDK >= 3.1
## 启用 XREAL 插件
1. 在 `Project Settings > XR Plug-in Management > XREAL` 中勾选 `Enable Native Session Manager`
![enablenativesession](https://doc-asset.easyar.com/develop/unity/headsets/media/xreal-enable-sdk-manager.png)
2. 在 `Project Settings > XR Plug-in Management > XREAL` 中配置 `License Asset` 为 XREAL 的企业许可证
![addxreallicense](https://doc-asset.easyar.com/develop/unity/headsets/media/xreal-add-license.png)
> **注意**
在 XREAL 上， 如果 `Frame Recorder` 的 `Format` 为 `Auto` 或 `H264` ，录制的数据质量被有意降低，Mega 的成功率和准确度都有不同程度的降低，因此其在电脑上的运行效果仅作为参考。
> **注意**
如需向 EasyAR 反馈问题数据，请设置 ARSession 上的 `Frame Recorder` 的 `Format` 为 `Obsolete` 进行录制，注意录制完成必须调用停止（设置 `enabled` 为 `false`）否则无法使用。这样录制出来的数据在 Unity 中使用会显示数据加密无法播放，这是正常的。

---

## BlockController 组件参考
- 章节路径: `unity/mega/comp-BlockController.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockController.html

# BlockController 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockController.html)
>
探索 BlockController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockController.png)
默认条件下组件截图。
|属性|描述|
|**Active Control**|选项：
* Hide Before First Found（默认）：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活。
* Hide When Not Tracking：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用。
* None：不控制 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的激活与否。|
|**ID**|Block ID。
只读。|

---

## BlockHolder 组件参考
- 章节路径: `unity/mega/comp-BlockHolder.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockHolder.html

# BlockHolder 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html)
>
探索 BlockHolder 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockHolder.png)
默认条件下组件截图。
|属性|描述|
|**Multi Block**|定位到多个Block时的策略。选项：
* Disable（默认）：不允许多个 block。运行中检测到多个 block 时，会抛出致命错误。
* PlayMode：block 间的相对变换会在运行时计算，（通常）由 Mega Studio 在编辑模式下设置的数值将会保持到相关的两个 block 都被定位到为止。
* EditMode：block 间的相对变换在运行时不会发生变化，会保持（通常）由 Mega Studio 在编辑模式下设置的数值不变。|
|**Block Root Source**|Block root 的来源。
* External（默认）：外部，比如 Mega Studio 生成的节点或事先组装好的节点。
* Internal：内部，需要时由 [BlockHolder](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html) 自身创建。
* Mixed：混合，可以来自外部或内部。|
|**Block Root**|所有 Mega block 的父节点。它通常由 Mega 工具生成。如未设置，一个新的 root 节点会在第一个 block 被持有的时候自动生成。|

---

## BlockRootController 组件参考
- 章节路径: `unity/mega/comp-BlockRootController.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-BlockRootController.html

# BlockRootController 组件参考
>
[> 切换到 API
](../../../api/unity/EasyAR.Mega.Scene.BlockRootController.html)
>
探索 BlockRootController 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-BlockRootController.png)
默认条件下组件截图。
|属性|描述|
|**Active Control**|选项：
* Hide Before First Found：在第一次跟踪之前，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用；一旦被成功跟踪，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被持续激活。
* Hide When Not Tracking（默认）：被跟踪时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被激活；跟踪丢失时，[GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 会被停用。
* None：不控制 [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) 的激活与否。|
|**Root Location**|Block Root 的 GNSS（GPS、北斗等）信息。
它只在如下两种情况下有值：
1. 在编辑时，它下面其中一个 block 模型由 Mega Studio 导入且 block 数据含有GPS信息；
2. 在运行时，主动调用 [BlockHolder.Hold(BlockController.BlockInfo, Location)](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_Hold_EasyAR_Mega_Scene_BlockController_BlockInfo_EasyAR_Mega_Scene_Location_) 持有了一个 block。|
|*Latitude*|纬度。|
|*Longitude*|经度。|
|*Altitude*|海拔高度。|
|**Studio Tool**|当前控制 block 的 Studio 工具，仅用来在编辑模式下指示工具。|

---

## MegaTrackerFrameFilter 组件参考
- 章节路径: `unity/mega/comp-MegaTrackerFrameFilter.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/comp-MegaTrackerFrameFilter.html

# MegaTrackerFrameFilter 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.MegaTrackerFrameFilter.html)
>
探索 MegaTrackerFrameFilter 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter.png)
默认条件下组件截图。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter-nomega.png)
未导入 `com.easyar.mega` 包，组件不可时的截图。
MegaTrackerFrameFilter 组件窗口由两个部分组成：组件配置和测试区域。
## 组件配置
|属性|描述|
|**Service**|服务访问信息。|
|*Type*|EasyAR Mega 服务类型。选项：
* Block：Mega Block。
* Landmark：Mega Landmark。|
|*Access Source*|服务访问数据源类型。选项：
* Global Config：使用全局服务器配置。根据 Service Type 选择 [GlobalMegaBlockLocalizationServiceConfig](../../../api/unity/easyar.EasyARSettings.html#u_easyar_EasyARSettings_GlobalMegaBlockLocalizationServiceConfig) 或 [GlobalMegaLandmarkLocalizationServiceConfig](../../../api/unity/easyar.EasyARSettings.html#u_easyar_EasyARSettings_GlobalMegaLandmarkLocalizationServiceConfig)。全局配置可以点击 Unity 菜单 EasyAR > Sense > Configuration 后在属性面板里面进行填写。
* API Key：使用 [APIKeyAccessData](../../../api/unity/easyar.APIKeyAccessData.html) 类型的访问数据。
* Token：使用 [TokenAccessData](../../../api/unity/easyar.TokenAccessData.html) 类型的访问数据。|
|*App ID*|Access Source 是 API Key 或 Token 时显示。
服务AppID。|
|*Server Address*|Access Source 是 API Key 或 Token 时显示。
服务地址。|
|*API Key*|Access Source 是 API Key 时显示。
API Key。|
|*API Secret*|Access Source 是 API Key 时显示。
API Secret。|
|*Token*|Access Source 是 Token 时显示。
Token。|
|**Request Time Parameters**|请求时间参数。|
|*Timeout*|与服务器通信的超时时间（毫秒）。|
|*Request Interval*|期望的请求间隔时间（毫秒），值越大整体误差越大。|
|**Location Input Mode**|位置输入模式。选项：
* Onsite：在现场使用的情况的输入模式。GNSS 数据通常从设备获取并输入到 Mega，通常由 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 内部处理。
* Simulator：远程调试或电脑上运行必须使用的输入模式，GNSS 数据需要模拟成现场数据并通过对应接口输入 Mega。可选。
* FramePlayer：在使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html) 时的输入模式。这个模式是只读的。远程调试或电脑上运行必须设置成 Simulator 模式，否则将无法使用。现场使用要设置成 Onsite 以达到最佳效果。|
|**Min Input Frame Level**|输入帧最小允许的 [MegaInputFrameLevel](../../../api/unity/easyar.MegaInputFrameLevel.html)。如果 frame source 只能给出维度更低的 [CameraTransformType](../../../api/unity/easyar.CameraTransformType.html) 的数据，session 会启动失败。选项：
* ZeroDof：0DoF。
* ThreeDof：3DoF。
* FiveDof：5DoF。
* SixDof：6DoF。|
## 测试区域
测试功能在 Unity play 模式下可用。
服务类型是 Block 时，测试区域显示 Block 测试功能：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter-test-block.png)
可以模拟 GNSS 数据进行测试。
服务类型是 Landmark 时，测试区域显示 Landmark 测试功能：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/comp-MegaTrackerFrameFilter-test-landmark.png)
可以模拟 GNSS 数据进行测试。
可以模拟 [MegaLandmarkFilterWrapper.FilterBySpotId(string, Action<MegaLandmarkFilterResponse>)](../../../api/unity/easyar.MegaLandmarkFilterWrapper.html#u_easyar_MegaLandmarkFilterWrapper_FilterBySpotId_System_String_System_Action_easyar_MegaLandmarkFilterResponse__) 和 [MegaLandmarkFilterWrapper.FilterByLocation(Action<MegaLandmarkFilterResponse>)](../../../api/unity/easyar.MegaLandmarkFilterWrapper.html#u_easyar_MegaLandmarkFilterWrapper_FilterByLocation_System_Action_easyar_MegaLandmarkFilterResponse__) 执行。

---

## 如何使用 Mega Studio 创建与实景精确对齐的 3D 内容
- 章节路径: `unity/mega/content-realworld-alignment.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/content-realworld-alignment.html

# 如何使用 Mega Studio 创建与实景精确对齐的 3D 内容
这篇文档将介绍如何使用 Unity 上的 Mega Studio 将虚拟物体准确地摆放在现实空间的某个位置，在 AR 体验中与现实空间精确对齐。
## 开始之前
* 参考文档 [我的定位库可以使用了吗？](../../mega/localization-verify.html) 确认定位库已正确创建并添加 **Mega Block**。
* 准备好 Unity 项目中要使用的 3D 资产。
## 精确摆放 3D 内容
通过完成以下步骤可以将虚拟内容准确地摆放在现实空间中。
### 将 3D 内容挂载至 Block 节点下
加载 Block 稠密模型后，将 3D 内容挂载至场景中的 Block 节点下，作为其子节点。
![挂载模型](https://doc-asset.easyar.com/develop/unity/mega/media/content-realworld-alignment05.png)
### 精确调整模型位置
在场景中对着稠密模型调整 3D 内容的位置和旋转，将其调整至期望的位置和朝向。
### [可选] 根据全景图精确调整模型位置
点击 **Inspector** 面板中的全景标记右侧的加载按钮，场景中出现全景标记。
![加载全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation13.png)
![显示全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation14.png)
点击任意一个**全景标记**，就可以在其位置进行全景下的摆放。您可以通过点击不同的**全景标记**切换全景，以确认 3D 内容在不同视角下的位置都是准确的。
![全景编辑](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation15.png)
## 如果加载的 Block 模型不水平怎么办
在 **Hierarchy** 面板中选择 **Block Root** ，在 **Inspector** 面板中修改 **Rotation** 直到稠密模型的朝向朝向在 Unity 编辑器中看起来正确。
> **重要事项**
Block Root 是在 3D 引擎场景节点树上所有 Block 节点的父节点。
Block Root 在世界坐标系下的 Transform **不会**影响 Block 的**本地坐标系**，也因此**不会影响作为 Block 子节点 3D 内容的渲染结果**。它的 Transform 和最终的显示效果**无关**。
## 如果加载的 Block 模型有破碎，缺损的部分怎么办
在三维重建过程中，若受采集视角覆盖不全的影响，生成的密模型中可能会出现破碎或缺损的部分。
![破碎缺损](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment02.png)
面对不完整的模型，若破碎/缺损部分的 3D 内容对齐精度要并不高，可以通过点击**全景标记**对照**全景图**的方式来摆放 3D 内容。之后可以通过点击附近不同的**全景标记**位置来验证效果。
![通过全景图摆放](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment03.png)
若破碎/缺损部分的 3D 内容对齐精度要求非常高，则需要通过[补充更新](../../../mega/scene-update/incremental.html)或[无损全量更新](../../../mega/scene-update/full.html)进行地图的补充或更新。一般来说这样的区域意味着采图过程中没有覆盖，在这样的区域内部 Mega 定位效果会受到影响，仅在编辑器中对齐 3D 内容是不够的。
## 后续步骤
* 通过[使用 session 验证工具模拟运行](verify-session-tool.html)进一步验证摆放的准确性。
* 为场景添加准确的[环境遮挡](occlusion.html)以增强 AR 的真实感。

---

## 导入最新版本的 EasyAR 插件以启用 Mega 功能
- 章节路径: `unity/mega/enable-mega.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/enable-mega.html

# 导入最新版本的 EasyAR 插件以启用 Mega 功能
本文介绍了如何导入最新版本的 EasyAR Sense Unity Plugin (for Mega) 以启用 Mega 功能。
## 使用 Mega 应导入最新版本的 EasyAR 插件
>
> 需要使用 Unity 2021.3.30 或更高版本。
>
在[下载页面](https://www.easyar.cn/view/download.html)，您会看到 Unity 插件有两个版本：`EasyAR Sense Unity Plugin` 和 `EasyAR Sense Unity Plugin (for Mega)`。
这两个版本的主要差异为：
* **EasyAR Sense Unity Plugin**： 不含 Mega 支持文件，不能用于 Mega 开发。EasyAR 提供从 4.6 开始的历史版本下载。
* **EasyAR Sense Unity Plugin (for Mega)**：包含 Mega 支持文件，可以用于 Mega 开发。EasyAR 不提供历史版本下载。
在使用 4000 之后的版本时，只要版本号相同，两个压缩包内的 EasyAR Sense Unity Plugin（即 `com.easyar.sense`）文件是完全相同的，可以互相替换。因此，如果您已经下载并导入了最新版本的 EasyAR Sense Unity Plugin，可以直接从 EasyAR Sense Unity Plugin (for Mega) 压缩包中提取 `com.easyar.mega` 文件导入到 Unity 项目中，而不需要重新导入整个插件包。
> **注意**
在 4000 版本之后，导入不兼容的 `com.easyar.sense` 和 `com.easyar.mega` 时，脚本编译器会报错，提示版本不匹配。请确保 `com.easyar.sense` 和 `com.easyar.mega` 来自同一版本的插件包或互相兼容。
4.7 版本的 `com.easyar.sense` 和 `com.easyar.mega` 的版本号包含后面的所有数字和字母在内必须完全一致，才能保证兼容性。
在应用上线前，建议再次查看 EasyAR 网站，如果有更新版本的 EasyAR Sense Unity Plugin (for Mega)，请下载并导入最新版本以确保应用可以正常使用最新的 Mega 服务，以确保最长的兼容性和最佳的性能。
> **重要事项**
使用过时的 EasyAR Sense Unity Plugin (for Mega) 开发的应用，可能无法使用最新的 Mega 服务。
在线上服务没有变化时（即 Mega 定位库的版本没有更新时），使用旧版本的 EasyAR Sense Unity Plugin (for Mega) 打包的应用仍然可以正常使用。
## 导入 EasyAR 插件和 Mega 支持包
解压下载的 zip 包之后可以看到 `readme` 和两个 `tgz` 文件，`tgz` 文件可以直接导入 Unity 不要再解压。
导入方法：
* 从菜单栏依次点击 `Window` 并选择 `Package Manager`
* 在弹出的窗口中单击左上角的 `+` 号， 选择 `Install Package from tarball ...`
* 在弹出的对话框中选择下载并解压得到的 `.tgz` 文件
两个 `.tgz` 文件 导入顺序不限，可以先导入 `com.easyar.sense`，也可以先导入 `com.easyar.mega`。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/package-import.png)
> **提示**
`com.easyar.mega` 依赖一些第三方包，如 `com.unity.cloud.ktx` 和 `com.unity.cloud.gltfast`，导入时请确保网络连接正常，以便 Unity 可以自动下载和导入这些依赖包。
在部分网络环境下，Unity 导入这些依赖包的过程可能比较缓慢，建议修改网络环境或多次尝试导入，直到所有依赖包都成功导入。
导入成功后，在 Unity 的 `Console` 窗口中不应看到任何错误提示，同时打开 `Package Manager` 窗口，可以看到 `EasyAR Sense Unity Plugin` 和 `EasyAR Mega Studio` 均已导入且显示为刚刚导入的版本号。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/package-imported.png)
> **注意**
在导入插件包后， `tgz` 文件不能被删除或移动到另一个位置，因此通常需要在导入前将这个文件放在合适的地方。通常建议放在 Unity 项目 `Packages` 文件夹内，方便版本管理。
## 后续步骤
* [快速入门](quickstart.html) Unity Mega 开发
* 使用 Mega 开发应用
* [AR Session 最佳实践](session-best-practice.html)
* [添加跟踪目标](target.html)
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)

---

## 在 Unity 中使用 EasyAR Mega 实现遮挡
- 章节路径: `unity/mega/occlusion.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/occlusion.html

# 在 Unity 中使用 EasyAR Mega 实现遮挡
遮挡 （Occlusion） 是提升 AR 虚实融合沉浸感的关键技术。本文将介绍如何在 Unity 中通过 EasyAR Mega 实现遮挡效果。
## 开始之前
* 完成[使用 EasyAR Mega Unity 样例快速入门](quickstart.html)。
* 能够[创建与实景对齐的内容](content-realworld-alignment.html)。
## 遮挡的实现方式
* 离线建模：在 Block 坐标系下，针对现实世界中的实体（如墙体、立柱、大型设备）创建 1:1 匹配的几何体；或通过对 Block 稠密模型进行裁剪与减面处理得到优化后的模型。
* 运行时对齐：在运行时，通过云定位将 Block 坐标系与现实空间对齐，并加载对应的几何体。
* 材质替换：为这些几何体赋予特殊的遮挡材质。
* 视觉效果：当 GPU 渲染其他虚拟物体时，会因深度测试未通过而自动剔除被遮挡部分的像素，从而使虚拟物体遵循现实物理空间的遮挡逻辑。
## 如何使用几何体作为遮挡
根据以下步骤可以在场景中添加作为遮挡使用的几何体并验证效果。
### 摆放遮挡几何体
根据 Mega Block 的稠密模型使用内置几何体或自建几何体作为遮挡摆放在 Block 坐标系下的正确位置。
![摆放遮挡几何体](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion01.png)
### [可选]根据全景图微调几何体的位置
![根据全景图微调遮挡](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion02.png)
### 为几何体赋予遮挡材质
将几何体材质修改为遮挡材质，可以使用 Unity 自带的 `SpatialMappingOcculusion`。
![根据全景图微调遮挡](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion03.png)
### 使用 EIF 数据模拟运行或实机运行
可以根据运行效果微调遮挡模型的摆放。
## 如何使用裁剪并减面的稠密模型作为遮挡
根据以下步骤将导出后的 Mega Block 稠密模型裁剪并减面得到用于遮挡的白模，并导入场景作为遮挡。
### 在 **Mega Blocks** 中导出
在 **Inspector** 面板中的 **Mega Blocks** 工具选择导出
![选择导出](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion04.png)
### 修改导出选项
在导出时注意修改导出选项。
![导出选项](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion05.png)
图中 1 为 LOD 层级，层级越低模型越简单，面数越少，若需要最高的精度选择2，若能接受降低精度以减少面数选择 1 或者 0。
图中 2 为导出贴图选项，由于我们只需要白模作为遮挡，不需要贴图。
### 对模型进行裁剪并减面
将导出后的模型在数字内容创建软件（例如 Blender）中进行裁剪，减面，保存为 `Glb`。
> **提示**
例子中使用的是 Blender 的 Decimate Modifier。
![裁剪前](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion06.png)
裁剪并减面后：
![裁剪后](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion07.png)
### 将遮挡模型导入 Unity 并挂载到场景中 Block 节点下方
![导入遮挡模型](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion09.png)
### 修改模型的 Transform
修改模型的 **Transform** 使 **Position**，**Rotation** 均全部为 **0**。
此时用于遮挡的白模应该和稠密模型贴合，这是因为在数字内容创建软件中进行裁剪和减面操作时，并没有改变 Block 坐标系的定义。
![遮挡模型贴合](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion10.png)
### 为模型赋予遮挡材质
将模型材质修改为遮挡材质，可以使用 Unity 自带的 `SpatialMappingOcculusion`。
![遮挡模型更换材质](https://doc-asset.easyar.com/develop/unity/mega/media/occlusion11.png)
### 使用 EIF 数据模拟运行或实机运行
使用 EIF 数据模拟运行或实机运行，查看效果。
## 遮挡的效果预期
遮挡的效果主要由以下几点影响：
* 定位跟踪本身的精度
* 模型摆放的准确程度
* 模型本身的精度（如果不是简单的几何体）
在定位漂移时出现数公分未对齐的情况是正常的。
遮挡用的模型面数太多容易影响性能，建议只在必要区域使用，并且尽量使用简单的几何体作为遮挡。
## 相关主题
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [使用 session 验证工具模拟运行](verify-session-tool.html)

---

## 现场使用和模拟运行
- 章节路径: `unity/mega/onsite-and-simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/onsite-and-simulation.html

# 现场使用和模拟运行
本文介绍了 Mega 在现场使用和非现场模拟运行时的配置差异，以及如何根据需求进行配置。
## 现场使用和模拟运行的差异
Mega 会使用 GNSS（GPS、北斗等）信息对定位过程进行辅助，以提升定位的精度和稳定性。在现场使用时，设备的 GNSS 信息是准确的可以用来辅助定位。而在非现场模拟运行时，设备的 GNSS 信息与环境是不匹配的，这个数据不能用来辅助定位，反而会影响定位效果。因此，Mega 提供了两种不同的配置以适应现场使用和非现场模拟运行的需求。
默认配置为模拟运行配置，以避免初次使用时因错误配置导致的定位失败的问题。
在模拟运行的配置下，屏幕上会始终显示警告信息，这段信息无法关闭，以确保应用不会以错误的配置发布到最终用户手中。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/warn-simulation.png)
> **提示**
如果要关闭警告信息，需要确保应用只会在现场使用，并使用现场配置。
## 配置以用于非现场模拟运行
选中 session 下的 `Mega Tracker` 物体，找到 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件，选择 `Location Input Mode` 为 `Simulator` 选项即可启用模拟运行配置。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-simulator.png)
在脚本中，可以设置 [MegaTrackerFrameFilter.LocationInputMode](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocationInputMode) 为 [Simulator](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_Simulator) 来达到同样的效果。
> **注意**
[使用 EIF 文件模拟运行](../simulation/playback.html) 时，该选项会被自动设置为 [FramePlayer](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_FramePlayer) 且不可更改，以确保 EIF 文件内记录的 GNSS 数据被正确使用。
## 配置以用于现场使用
选中 session 下的 `Mega Tracker` 物体，找到 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件，选择 `Location Input Mode` 为 `Onsite` 选项即可启用现场使用配置。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-onsite.png)
在脚本中，可以设置 [MegaTrackerFrameFilter.LocationInputMode](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocationInputMode) 为 [Onsite](../../../api/unity/easyar.MegaLocationInputMode.html#u_easyar_MegaLocationInputMode_Onsite) 来达到同样的效果。
> **小心**
如果在非现场模拟运行时错误地使用了现场配置，可能会导致定位失败进而影响内容的显示。

---

## 使用示例快速入门 EasyAR Mega Unity 开发
- 章节路径: `unity/mega/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/quickstart.html

# 使用示例快速入门 EasyAR Mega Unity 开发
本教程介绍如何配置并运行 EasyAR Mega Unity 示例，以快速入门 EasyAR Mega 开发。
## 开始之前
阅读本篇之前，需要确保您已完成：
* 有一个 [有效的云定位库](../../mega/localization-verify.html)。
* 安装 Unity（2021.3.30 LTS 或更高版本），建议使用 Unity 2022.3 或 Unity 6.3 的最新版本。
* 按 [启用 Mega](enable-mega.html) 的方法导入 `com.easyar.sense-\*\*.tgz` 和 `com.easyar.mega-\*\*.tgz` 包。
## 示例使用方法（六步走）
下面将分六个步骤介绍如何配置并运行 EasyAR Mega 的核心示例 `MegaBlock\_Basic`。
### 第一步：导入示例
> **注意**
如果通过 `\*\*All Samples\*\*` 导入了全部示例，需要跳过此步骤。
1. 使用菜单 `Window` > `Package Manager` 打开 Package Manager，选中 `EasyAR Sense Unity Plugin`, 在右侧的 **Samples** 中展开所有示例。
2. 选择示例（如 `MegaBlock\_Basic`），点击 **Import**。
![Import Sample](https://doc-asset.easyar.com/develop/unity/mega/media/sample-import.png)
> **注意**
* 本教程不能直接适用于头显设备，但在开发头显设备之前，需要使用手机开发了解流程。
* 如果您先前已经导入过旧版 SDK 的示例，在升级 SDK 之后需先删除旧示例再重新导入。
### 第二步：填写 License Key 并配置 Mega 云定位服务
1. 菜单栏选择 `EasyAR` > `Sense` > `Configuration`；
![License Guide](https://doc-asset.easyar.com/develop/unity/mega/media/fill-license-where.png)
2. 在打开的 **Project Settings** 面板中粘贴您的 License Key；
![Fill License](https://doc-asset.easyar.com/develop/unity/mega/media/fill-license-text.png)
> **提示**
EasyAR Sense License 可以从 [EasyAR 开发中心](https://www.easyar.cn/view/login.html) 创建。初次使用可以按以下步骤创建：
![](https://doc-asset.easyar.com/develop/unity/mega/media/license.png)
* 创建 `EasyAR Sense 4.x 个人版`
* 稀疏空间地图选 `否`
* 应用名称随意填写，Bundle ID 和 Package Name 填写 `com.mycompany.myproject`
* 选择刚创建的 License，进入之后点击右侧复制按钮
![copykey](https://doc-asset.easyar.com/develop/unity/getting-started/media/copykey.png)
> **注意**
Bundle ID 和 Package Name 后续可以更改，但次数有限。如果您有明确的应用包名，也可以填写您自己的包名。
个人版创建没有个数限制，其它类型可以正式使用时按需创建。
1. 将您的 Mega 云定位库的各项信息配置到 **Project Settings** 面板中的 `Mega Block` 项；
![Mega Config Guide](https://doc-asset.easyar.com/develop/unity/mega/media/fill-mega-config-where.png)
> **提示**
Mega 云定位库配置可以从EasyAR开发中心获取。
![Mega Config Detail](https://doc-asset.easyar.com/develop/unity/mega/media/mega-config-detail.png)
确保您的 `API Key` 具有 `Mega Block` 的权限，如果没有需要进行更改或重新创建。
![API Key Auth](https://doc-asset.easyar.com/develop/unity/mega/media/check-apikey-auth.png)
### 第三步：摆放 3D 内容
1. 在 `Hierachy` 面板空白处右键点击，添加 Block 浏览工具（Unity 开发）；
![Add Block Viewer](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer.png)
2. 访问 Mega 定位服务；
1. 选中 `EasyAR.Mega.BlockViewer (Dev)` 节点，在 **Inspector** 面板中填写您的 EasyAR 账号信息并登录；
![login](https://doc-asset.easyar.com/develop/unity/mega/media/login.png)
2. 点击 Mega Cloud Service 右侧按钮；
![Click Mega CLS](https://doc-asset.easyar.com/develop/unity/mega/media/click-cls.png)
3. 选择您所要使用的 `Mega定位服务`，点击**确定**。
![Select Mega CLS](https://doc-asset.easyar.com/develop/unity/mega/media/select-cls.png)
4. 加载 Block
在选择服务之后，当前库中的 Block 列表会显示在 `MegaBlocks` 节点下，并显示在工具面板上。点击**加载**选择的Block：
![Load Block](https://doc-asset.easyar.com/develop/unity/mega/media/load-block.png)
加载完成后，Block 会显示在 `Scene` 窗口中。您可以在 `Scene` 窗口中操作，调整查看的视角、位置。同时检查下 Block 文件是否可用（比如 Block 坐标系是否正常，是否存在分层，是否过于模糊、存在缺损而无法找到位置摆放 AR 资源等）。
![Display Block](https://doc-asset.easyar.com/develop/unity/mega/media/block-in-scene.png)
5. 摆放 3D 内容
此时，您可以参考 Block 摆放 3D 物体。
![Place 3D Object](https://doc-asset.easyar.com/develop/unity/mega/media/annotate-in-block.png)
> **注意**
* 3D 物体必需摆放在工具自动生成的 `MegaBlocks` > `Block\_\*` 节点之下，以确保在运行时虚拟内容的渲染位置是正确的。
* 请不要修改 `Block\_\*` 节点的名字和 `local transform`，它由工具自动管理。
### 第四步：配置 MegaTracker
1. 配置 **Block Root**；
展开 `AR Session` ，选择 `Mega Block Tracker` 并设置 `Block Root` 为工具生成的 `MegaBlocks` 节点。
![Set Block Root](https://doc-asset.easyar.com/develop/unity/mega/media/set-block-root.png)
### 第五步：修改 Player 配置
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击安卓图标，调出 Android 平台 相应的设置。
![switchtoandroid](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-switch-unity.png)
* 修改 Package Name 为 License Key 页面显示的 Package Name
![androidPackageName](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-package_name.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Package Name 是 `com.mycompany.myproject`，则必须填写这里 Package Name 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 Minimum API Level 为 `API Level 21` 或更高版本
![androidAPILevel](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-api-level.png)
* 修改 Scripting Backend 为 `IL2CPP`，并在 `Target Architecture` 中勾选 `ARM64`
![androidarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/android-64bit.png)
依次在 Unity 菜单 `File` > `Build Settings` > `Player Settings`，点击 `iOS` 调出 iOS 平台相关设置面板。
![switchtoios](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-swicth-unity.png)
* 修改 Bundle ID 为 License Key 页面显示的 Bundle ID
![iosbundleid](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-bundle-id.png)
> **提示**
比如，如果您在创建 License Key 时填写的 Bundle ID 是 `com.mycompany.myproject`，则必须填写这里 Bundle ID 为 `com.mycompany.myproject`，否则会运行失败。
* 修改 `Architecture` 为 `ARM64`
![iosarm64](https://doc-asset.easyar.com/develop/unity/getting-started/media/ios-arm64.png)
* 添加 `Camera Usage Description` 和 `Location Usage Description`，字符串内容可以随意填写，但必须添加。
![ioscamerapermission](https://doc-asset.easyar.com/develop/unity/mega/media/ios-permissions.png)
### 第六步：构建并运行
1. 添加当前场景至 `File` > `Build Settings` 或 `Build Profiles` > `Scene List` 中；
2. 切换到目标平台（如Android / iOS），检查包名（Bundle ID）与 License Key 是否一致；
![Switch Platform](https://doc-asset.easyar.com/develop/unity/mega/media/build-switch-platform.png)
3. 点击 **Build And Run**。
![Build And Run](https://doc-asset.easyar.com/develop/unity/mega/media/build-and-run.png)
现场实拍的运行效果如下：
## 关于屏幕上的黄色文字
运行时，您可能会看到屏幕上显示了两处黄色文字。
1. 模拟运行的警告信息
它位于屏幕下方：
![](https://doc-asset.easyar.com/develop/unity/mega/media/warn-simulation.png)
出现这个警告的原因是因为在默认配置下，应用可以不在现场运行。它对应用的运行效果有些微影响，如果您正好在现场使用，可以在打包前 [修改 MegaTracker 配置](onsite-and-simulation.html)。
2. 诊断信息
它位于屏幕上方，用于了解 session 的运行状态和问题，建议在开发和测试阶段保持显示：
![](https://doc-asset.easyar.com/develop/unity/mega/media/ui-message.png)
可以参考 [场景中的诊断信息](../getting-started/diagnostics.html) 来快速了解如何配置和使用这些诊断信息。
## 下一步：从入门到精通
恭喜！通过以上步骤，您已成功在 **10 分钟内** 运行了 EasyAR Mega 的核心示例，亲身体验了空间定位与 AR 内容叠加的魅力。
现在，您已经掌握了基础。如果您希望：
* **构建更稳定、更高效的 AR 应用**
* **实现复杂的虚实遮挡、内容对齐等效果**
* **在没有设备或无法前往现场时进行调试**
请参考以下深入指南，它们将帮助您解决开发过程中的实际问题。
### 开发进阶
如果您希望了解完整的工程配置，可以参考以下内容：
* [使用 Universal Render Pipeline（URP）](../getting-started/universal-render-pipeline.html)
* [Player 配置](../fundamentals/setup-player.html)
* [EasyAR 配置](../fundamentals/setup-easyar.html)
如果您希望进一步了解 EasyAR 的使用方法，可以从这里开始：
* [AR 驱动的 Unity 应用基础](../fundamentals/intro.html)
同时，建议阅读以下内容来帮助您开发和调试：
* [Unity 开发中的问题诊断和报告](../diagnostics/diagnostics.html)
* [Unity AR 模拟运行](../simulation/simulation.html)
### 精细化控制 Mega 功能
下面的这些内容将帮助您更好地在您的应用中使用 Mega：
* [现场使用和模拟运行](onsite-and-simulation.html)
* [ARSession 最佳实践](session-best-practice.html)
* [添加跟踪目标](target.html)
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [环境遮挡 (Occlusion)](occlusion.html)
* [控制跟踪过程](tracker.html)
下面的这些内容将帮助您无需到达现场即可验证 Mega 功能：
* [使用 PC 相机进行快速验证](verify-pc-camera.html)
* [使用 Session 验证工具进行模拟运行](verify-session-tool.html)
### 高级主题
下面的这些内容更加适合在有一定 EasyAR 使用经验后阅读。
如果您希望在头显上运行 EasyAR Mega，可以参考以下内容：
* [Unity 中的 EasyAR 头显支持](../headsets/headsets.html)
* [在 XR 头显或眼镜上使用 EasyAR 样例](../headsets/samples.html)
如果您希望使用 AR Foundation，可以从这里开始：
* [EasyAR 对 Unity XR 框架的支持](../fundamentals/unity-xr.html)

---

## 适用于 Mega 的 AR Session 最佳实践
- 章节路径: `unity/mega/session-best-practice.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/session-best-practice.html

# 适用于 Mega 的 AR Session 最佳实践
本文介绍了如何创建和配置适用于 Mega 的 AR session，以便在不同类型的设备上获得最佳的运行效果。
## 开始之前
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 了解如何 [创建 session](../fundamentals/session-creation.html)
## 默认配置的 session
对于大部分应用，推荐使用默认的 Mega session 配置，这些配置已经过优化，适用于大部分常见的使用场景。
默认的 session 支持以下类型的设备：
* 支持 6DoF 运动跟踪的设备（部分现代手机和头显）
* 支持 5DoF 惯性导航功能的设备（大部分有陀螺仪和加速度计的 Android 手机）
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Mega` > `AR Session (Mega Block Default Preset)` 可以创建默认的 Mega session。
对应的脚本代码如下：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.MegaBlock\_MotionTracking\_Inertial)
```
该 session 使用 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设：
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Sense` > `Mega` > `AR Session (Mega Landmark Default Preset)` 可以创建默认的 Mega session。
对应的脚本代码如下：
```
ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset.MegaLandmark\_MotionTracking\_Inertial)
```
该 session 使用 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设：
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组。
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Landmark](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Landmark)
## 选择不同的预设
除了默认配置的 Mega session 外，还可以根据具体需求选择不同的预设来创建 session，它们的主要差别在于支持设备类型不同。
使用菜单和 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 创建 session 时可选的预设包括：
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)（默认）
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ZeroDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ZeroDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
使用菜单和 [ARSessionFactory.CreateSession(ARSessionFactory.ARSessionPreset, ARSessionFactory.Resources)](../../../api/unity/easyar.ARSessionFactory.html#u_easyar_ARSessionFactory_CreateSession_easyar_ARSessionFactory_ARSessionPreset_easyar_ARSessionFactory_Resources_) 创建 session 时可选的预设包括：
* [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial)（默认）
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [FiveDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_FiveDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
* [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF)
* frame source 组件及排序可以参考 [预设 AR Session 的帧数据源组](../cameras/frame-source-group.html) 中 [MegaBlock\_MotionTracking\_Inertial\_3DOF\_0DOF](../../../api/unity/easyar.ARSessionFactory.ARSessionPreset.html#u_easyar_ARSessionFactory_ARSessionPreset_MegaBlock_MotionTracking_Inertial_3DOF_0DOF) 预设对应的帧数据源组
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ZeroDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ZeroDof)
* [MegaTrackerFrameFilter.ServiceType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ServiceType) 为 [Block](../../../api/unity/easyar.MegaApiType.html#u_easyar_MegaApiType_Block)
> **注意**
Mega 在不同类型的设备上运行效果是不一样的，详情可以参考 [Mega 支持的设备和平台应用](../../mega/devices.html)。
## 后续步骤
* [添加跟踪目标](target.html)
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)
## 相关主题
* 阅读 [帧数据源](../cameras/frame-source.html) 了解帧数据源的基本概念及运行时帧数据源选取过程
* 阅读 [添加一组帧数据源](../cameras/frame-source-group.html) 了解数据源组的配置和使用方法
* 阅读 [Mega 支持的设备和平台应用](../../mega/devices.html) 了解 Mega 支持的设备以及在不同设备上的运行效果

---

## 添加 Mega 跟踪目标
- 章节路径: `unity/mega/target.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/target.html

# 添加 Mega 跟踪目标
本文介绍了如何添加 Mega 的跟踪目标以及如何在 Unity 编辑器中加载环境模型以辅助开发。
## 开始之前
* 检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
* [导入最新版本的 EasyAR 插件以启用 Mega 功能](enable-mega.html)
* 了解 [Unity AR 的跟踪目标](../fundamentals/target.html) 的基本概念和使用方法
> **注意**
以下内容及工具仅适用于使用 EasyAR Mega 开发 Unity 应用的过程。
如果您在开发小程序，请参考 [使用 Unity 编辑器创建并上传标注（小程序开发）](../../wechat/mega/content-annotation-creation.html)。
如果您只希望查看 Mega 建图结果，请参考 Mega 使用指南中的 [预览3D 实景网格](../../../mega/mapping/textured-mesh.html)。
如果您需要模拟运行查看定位效果，但您并没有一个可以使用的 Unity 应用工程，请参考 Mega 使用指南中的 [模拟运行效果预览](../../../mega/simulation-verification/intro.html)。
## Mega 的跟踪目标
Mega 的跟踪目标是包含 [BlockController](../../../api/unity/EasyAR.Mega.Scene.BlockController.html) 组件的空物体，称为 block。在场景中，block 会被组织在一个包含 [BlockRootController](../../../api/unity/EasyAR.Mega.Scene.BlockRootController.html) 组件的空物体下，这个物体的默认名称为 `MegaBlocks`。`MegaBlocks` 下所有的 block 物体代表了当前定位库中的所有跟踪目标。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/target-block.png)
开发中经常需要使用 block 模型来辅助查看和摆放 3D 内容。这个模型可以使用工具加载到场景中，方便查看和参考。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/target-block-model.png)
模型位置是与 block 跟踪目标对齐的，可以直接在模型上摆放 3D 内容。
> **提示**
模型存储于工具节点下，仅存在于编辑器模式下，不会被打包进最终应用。
## 在编辑器中添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [External](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_External)（默认） 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/block-root-source.png)
### 添加 Block Viewer for Unity Developer 工具
在 `Hierarchy` 视图中 **空白** 处点击右键，通过菜单 `EasyAR Mega` > `Tool` > `Block Viewer for Unity Developer (Edit Mode)` 可以添加 Unity 开发用的 Block Viewer 工具。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer.png)
> **重要事项**
使用 Unity 开发 Mega 应用时，必须使用 `Block Viewer for Unity Developer` 工具。`EasyAR Mega` > `Tool` 菜单下的其它工具不适合做 Unity 应用开发。
虽然 `Annotation Tool` 也有类似的功能，但这个工具的部分功能将在未来版本中被移除，因此不建议使用。
`Annotation Tool` 的标注功能（仅标注本身）即将迁移至 EasyAR 开发中心网页，block mesh 加载和模型摆放不受影响。
工具添加成功后，场景层级中会多出一个 `EasyAR.Mega.BlockViewer (Dev)` 节点和一个 `MegaBlocks` 节点。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/add-block-viewer-result.png)
### 生成跟踪目标 —— block
选中 `EasyAR.Mega.BlockViewer (Dev)` 节点，在 **Inspector** 面板中填写 EasyAR 账号信息并登录；
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/login.png)
点击 Mega Cloud Service 右侧按钮；
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/click-cls.png)
选择需要使用的 `Mega定位服务`，点击**确定**。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/select-cls.png)
在选择服务之后，当前库中的 block 列表会显示在 `MegaBlocks` 节点下，并显示在工具面板上。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/load-block.png)
> **提示**
为什么我的 `MegaBlocks` 下面是空的？
建议检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
到这里已经生成了跟踪目标 block，`MegaBlocks` 节点下每个 `Block\_` 开头的子节点即代表一个 block 跟踪目标。
### 加载 block 模型
点击**加载**选择的Block：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/load-block-2.png)
加载完成后，Block 会显示在 `Scene` 窗口中。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/block-in-scene.png)
## 定位成功时自动添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [Internal](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Internal) 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)。
在这两个模式下，如果定位到一个新的 block 且 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下没有该 block，这个新的 block 会被自动添加到 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下。如果 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 不存在会被自动创建。
> **提示**
定位成功时自动添加跟踪目标时，无法加载 block 模型，仅能添加 block 跟踪目标。
## 在脚本中添加跟踪目标
使用这个方法需要配置 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [Internal](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Internal) 或 [Mixed](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_Mixed)，这时如果 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 不存在会被自动创建。或者也可以在 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 为 [External](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.BlockRootSourceType.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSourceType_External) 时在编辑器中事先指定好 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 物体。
> **注意**
如果 block 不在定位库中，即使使用脚本添加到场景中，block 也无法被定位到。
可以使用 [BlockHolder.Hold](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_Hold_) 方法添加一个新的 block 到 [BlockHolder.BlockRoot](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRoot) 节点下。这个方法通常用在使用 ema 标注文件时，脚本读取到标注信息后添加 block。
比如，下面的代码片段展示了如何使用标注文件中的信息添加 block：
```
foreach (var item in ema.blocks)
{
var info = new BlockController.BlockInfo { ID = item.id.ToString(), Timestamp = item.timestamp };
if (!item.keepTransform && item.location.OnSome)
{
blockHolder.Hold(info, item.location.Value);
}
else
{
blockHolder.Hold(info, item.transform.ToUnity());
}
}
```
> **提示**
使用脚本在运行时添加跟踪目标时，无法加载 block 模型，仅能添加 block 跟踪目标。
## 后续步骤
* [添加与实景对齐的 3D 内容](content-realworld-alignment.html)
* [控制跟踪过程](tracker.html)
## 相关主题
* [Mega Studio（Unity）操作手册](../../../mega/reference/studio-unity/intro.html)

---

## 控制 Mega 跟踪过程
- 章节路径: `unity/mega/tracker.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/tracker.html

# 控制 Mega 跟踪过程
本文介绍了如何控制 Mega 跟踪过程中的各项功能和参数，以满足不同应用场景的需求。
## 开始之前
* 检查 [我的定位库可以使用了吗？](../../mega/localization-verify.html)
## 调整设备支持等级
[MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 的 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 属性用于指定 Mega 支持的最低设备等级。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-level.png)
Mega 可以在几乎所有类型的帧数据源上运行，但不同的帧数据源对跟踪效果有不同的影响。
默认情况下，Mega 会选择设备支持的最高等级的帧数据源进行跟踪。[默认配置下的支持 Mega 的 session](session-best-practice.html) 已经配置了支持 6DoF 和 5DoF 的帧数据源。
在 Mega 运行时要支持某个等级的帧数据源需要满足两个条件：
* 所需的帧数据源在 session 的可选帧数据源组中。
* [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 大于或等于所需的帧数据源的 [CameraTransformType](../../../api/unity/easyar.CameraTransformType.html) 等级。
比如，要在默认 session 中支持 3DoF 跟踪，需要：
* 添加 [ThreeDofCameraDeviceFrameSource](../../../api/unity/easyar.ThreeDofCameraDeviceFrameSource.html) 到 session 的帧数据源组中。
* 修改 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [ThreeDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_ThreeDof)。
又比如，要在默认 session 中删除 5DoF 跟踪支持，需要：
* 从 session 的帧数据源组中删除 [InertialCameraDeviceFrameSource](../../../api/unity/easyar.InertialCameraDeviceFrameSource.html)。
* 修改 [MegaTrackerFrameFilter.MinInputFrameLevel](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_MinInputFrameLevel) 为 [SixDof](../../../api/unity/easyar.MegaInputFrameLevel.html#u_easyar_MegaInputFrameLevel_SixDof)（即使不修改，由于没有 5DoF 帧数据源，5DoF 也不会被使用）。
在没有满足条件的帧数据源可用时，session 组装会失败。
## 跟踪目标管理
使用 Mega 时，需要指定 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 使用的 target 即 block。
### block 来源控制
大部分情况下，建议保持默认配置，即在编辑器中使用 Mega Studio 导入 block。
选中 session 下的 `Mega Tracker` 物体，`Block Root Source` 选项应该保持为 `External`（默认）。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-rootsource.png)
同时，需要指定 `Block Root` 为场景中的 `MegaBlocks` 物体。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-rootsource-external.png)
修改 `Block Root Source` 选项可以指定其它 block 来源方式，比如使用 ema 导入数据时，通常会选择 `Internal` 或 `Mixed` 选项。
在脚本中，可以修改 [BlockHolder.BlockRootSource](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_BlockRootSource) 来达到同样的效果。
### 多目标跟踪控制
在大部分的 Mega 使用场景下，没有使用多目标的必要。在熟练掌握如何避免多个 block 互相影响之前，建议一个定位库中只放一个block。
> **提示**
原理上，Mega 会计算设备在所有 block 中的位置，而不是从定位库中抽选设备看到的 block。考虑不周的使用可能会因数据混淆等原因导致效果劣化。
选中 session 下的 `Mega Tracker` 物体，修改 `Multi Block` 选项可以启用或禁用多目标跟踪功能。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-multi-block.png)
在脚本中，可以修改 [BlockHolder.MultiBlock](../../../api/unity/EasyAR.Mega.Scene.BlockHolder.html#u_EasyAR_Mega_Scene_BlockHolder_MultiBlock) 来达到同样的效果。
> **警告**
一般情况下，一个定位库里只能同时有一个 block。
修改多目标配置会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中该配置被修改过，向 EasyAR 反馈问题时请务必说明这一点。
## 了解当前系统状态
在默认 session 配置下，[UI 消息](../diagnostics/ui-messages.html) 会显示在屏幕上，其中包含了 Mega 跟踪状态的信息。
在定位成功时，Mega Block 下会包含 `Found` 状态文字以及当前跟踪的 block 名称和 ID：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-status-found.png)
在定位失败时，Mega Block 下会包含 `NotFound` 状态文字：
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-status-notfound.png)
> **提示**
`NotFound` 是正常状态，在 Mega 工作的整个过程中经常会出现该状态，出现该状态时跟踪仍然在继续。通常应用开发中不需要对 `NotFound` 状态进行特殊处理。
使用 [MegaTrackerFrameFilter.LocalizationRespond](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_LocalizationRespond) 事件可以获取当前的定位状态，从而了解系统当前是否找到了跟踪目标。
以下代码展示了如何使用该事件，以及常见的需要应用关注的异常状态的处理方法：
```
private void Awake()
{
megaTracker.LocalizationRespond += HandleLocalizationStatusChange;
}
private void HandleLocalizationStatusChange(MegaLocalizationResponse response)
{
var status = response.Status;
wakingUpCount = status == MegaTrackerLocalizationStatus.WakingUp ? wakingUpCount + 1 : 0;
if (wakingUpCount >= 5)
{
// 服务正在唤醒中，需要让终端用户等待
}
if (status == MegaTrackerLocalizationStatus.QpsLimitExceeded)
{
// QPS 超限，会随机有终端用户定位失败（总体跟踪质量下降）
// 这时一般需要付费提升 QPS 上限以保障当前用户量下的跟踪质量
}
if (status == MegaTrackerLocalizationStatus.ApiTokenExpired)
{
// Token过期，这只会出现在使用 Token 接口访问服务时
// 接近该问题需要应用请求自己的后台获取 Token，并调用 MegaTrackerFrameFilter.UpdateToken 进行更新
}
}
```
如果应用经常遇到 [MegaTrackerLocalizationStatus.RequestTimeout](../../../api/unity/easyar.MegaTrackerLocalizationStatus.html#u_easyar_MegaTrackerLocalizationStatus_RequestTimeout) 状态，通常说明设备连接服务的网络状况不佳，建议优化网络环境以提升跟踪质量。在网络状况无法改善的场景下，可以考虑增加请求超时时间。
> **注意**
无法通过该事件获取定位返回的 pose。
事实上，定位返回的 pose 在应用开发中是不需要的，EasyAR 会在定位返回后通过本地算法计算出更准确的 pose 并返回给开发者使用，而该 pose 已经体现在 block 的 transform 中，可以参考 [获取 session 的运行结果](../fundamentals/session-output.html)。
## 暂停和继续
Mega 的跟踪和定位功能可以分别暂停和继续。
### 暂停跟踪
设置 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 为 false 可以暂停跟踪。
默认在跟踪暂停后，所有 block 节点下的内容都会隐藏。
### 暂停定位
设置 [MegaTrackerFrameFilter.ResultPoseType](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_ResultPoseType).[EnableLocalization](../../../api/unity/easyar.MegaResultPoseTypeParameters.html#u_easyar_MegaResultPoseTypeParameters_EnableLocalization) 为 false 可以暂停定位。
> **警告**
暂停定位会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中定位被暂停过，向 EasyAR 反馈问题时请务必说明这一点。
## 服务和请求控制
可以通过修改 [MegaTrackerFrameFilter](../../../api/unity/easyar.MegaTrackerFrameFilter.html) 组件的参数来控制请求服务的行为。
### 请求间隔和超时
选中 session 下的 `Mega Tracker` 物体，修改 `Request Time Parameters` 下的选项可以调整请求服务的时间间隔和超时时间。
![alt text](https://doc-asset.easyar.com/develop/unity/mega/media/tracker-timep.png)
在脚本中，可以修改 [MegaTrackerFrameFilter.RequestTimeParameters](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_RequestTimeParameters) 来达到同样的效果。
> **警告**
修改请求间隔会影响跟踪效果，一般不建议修改。请在 EasyAR 技术支持的指导下使用。
如果应用执行过程中请求间隔被修改过，向 EasyAR 反馈问题时请务必说明这一点。
### 切换定位库
使用 [MegaTrackerFrameFilter.SwitchEndPoint(ExplicitAddressAccessData, BlockRootController)](../../../api/unity/easyar.MegaTrackerFrameFilter.html#u_easyar_MegaTrackerFrameFilter_SwitchEndPoint_easyar_ExplicitAddressAccessData_EasyAR_Mega_Scene_BlockRootController_) 可以在运行时切换定位库。使用这个接口时相机画面及 session 不会中断。
## 相关主题
* [适用于 Mega 的 AR Session 最佳实践](session-best-practice.html) 介绍了如何创建和配置适用于 Mega 的 AR Session
* [添加 Mega 跟踪目标](target.html) 介绍了如何添加 Mega 的跟踪目标 block 以及如何在 Unity 编辑器中加载 block 模型以辅助开发
* [添加一组帧数据源](../cameras/frame-source-group.html) 介绍了如何修改 session 的帧数据源组
* [获取 session 的运行结果](../fundamentals/session-output.html) 介绍了如何获取 session 组件的跟踪结果
* [UI 消息](../diagnostics/ui-messages.html) 介绍了如何使用 UI 消息来显示 session 状态

---

## 使用 PC 摄像头快速跑通 Mega （一种快捷但不推荐的远程调试方式）
- 章节路径: `unity/mega/verify-pc-camera.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/verify-pc-camera.html

# 使用 PC 摄像头快速跑通 Mega （一种快捷但不推荐的远程调试方式）
本文档旨在指导开发者如何在没有 EIF 录制文件的情况下，利用 PC 摄像头配合现场图片，验证 Mega 云定位服务是否能跑通。
## 开始之前
* 完成[快速入门](quickstart.html)，了解如何运行包含 Mega 功能的 Unity 应用。
* PC 连接一个摄像头设备，并确保其功能正常。
* **功能预期**：
该方式**并非**我们推荐的远程调试方式，在有条件录制的情况[使用 EIF 文件进行调试](verify-session-tool.html)是我们推荐的最佳实践。
该方式仅用于**在没有 EIF 文件**情况下调试**与跟踪效果无关**的流程开发，比如用于验证 Mega 服务是否通畅。
PC 上使用相机看到的效果与实机的跟踪效果**完全无关**。
## 操作步骤
完成以下步骤即可快速跑通 Mega 服务验证。
### 获取现场照片
获取一张现场较为清晰的照片，可以现场拍摄也可以在编辑器中使用全景预览功能截取一张图片。
**如何使用全景预览功能截取图片**
>
> 点击场景
> Hierarchy
> 面板中的
> Mega Block Viewer(Dev)
> > 在
> Inspector
> 面板中点击
> 全景标记
> 右侧的
> 加载
> 。
>
![全景加载](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera02.png)
>
> 此时场景中会出现许多代表
> 全景标记
> 的黄色小球：
>
![全景标记](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera06.png)
>
> 点击
> 需要预览的位置的全景标记
> > 点击场景
> Hierarchy
> 面板中的
> Mega Block Viewer(Dev)
> > 在
> Inspector
> 面板中点击
> 全景标记
> 左侧的
> 隐藏
> 。
>
![全景标记隐藏](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera07.png)
>
> 即可在
> Mega Panorama
> 窗口中得到一张现场图片，将其截图保存：
>
![现场图片](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera05.png)
>
### 对照 Block 稠密模型或全景摆放一些 3D 内容
![摆放3D内容](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera03.png)
### 确认 Session 验证工具没有开启
点击场景中的 **AR Session (EasyAR)** > 确认其 **Inspector** 面板上的 **Frame Player** 被关闭。
![确认FramePlayer关闭](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera12.png)
点击场景中的 **EasyAR.Mega.BlockViewer(Dev)** > 确认其 **Inspector** 面板上的验证工具没有被 **Enable** (若不需要使用稠密模型，也可以直接删除或隐藏 **EasyAR.Mega.BlockViewer(Dev)**)。
![确认验证工具关闭](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera10.png)
### 点击运行，使用现场图片跑通 Mega
* **操作示范：**
> **重要事项**
Mega 定位服务对于用于定位的输入比较“宽容”，但这种调试方式的结果仅用于区分“通”与“不通”（即 0 或 1 的区别）。它能证明 Mega 定位服务已跑通，但完全不能代表真机上的实际跟踪体验。若要观察定位速度和跟踪稳定性，务必[使用 EIF 文件调试](verify-session-tool.html)或真机实测。
* **可以使用相机对着图片或视频运行**，如果定位成功，将会看到 3D 物体贴屏显示并跳跃更新。由于在场景中加载了 Block 模型，Block 模型也会显示出来。
* 如果将工具 `EasyAR.Mega.BlockViewer (Dev)` 关闭（`active` 设成 `false` 或删除节点），看到的就是在现实场景中叠加了虚拟物体的效果。
* **屏幕上的警告信息是无法关闭的**，因为这种使用方式并不能反映真实效果，我们限制这种方式只能在开发过程中使用，且开发人员应该清楚这样使用的影响。
![屏幕警告信息](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera11.png)
* 可以**通过诊断信息时间戳更新判断系统是否正常运行**：如果看到屏幕上显示的诊断信息中时间戳在不断更新，就说明系统已经正常在运行了。
![通过时间戳判断](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera12.gif)
> **重要事项**
在使用时，你一定会注意到运行时显示在屏幕上或目视前方的诊断信息文字，仔细阅读 [UI 消息输出](../diagnostics/ui-messages.html)，仔细斟酌在开发阶段、测试阶段、应用上线之后应该采取何种配置，以及保留何种控制开关。与 EasyAR 的沟通通常需要提供这些信息，建议多利用而不是立马关闭。
## 后续步骤
* 尽可能[使用 session 验证工具模拟运行](verify-session-tool.html)。

---

## 使用 session 验证工具模拟运行使用 Mega 能力的 AR 工程
- 章节路径: `unity/mega/verify-session-tool.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/mega/verify-session-tool.html

# 使用 session 验证工具模拟运行使用 Mega 能力的 AR 工程
本文旨在指导开发者如何在 Unity 编辑器上利用 session 验证工具加载录制的 EIF 数据，模拟运行使用 Mega 能力的 AR 工程。
## 开始之前
* 完成[快速入门](quickstart.html)，了解如何运行包含 Mega 功能的 Unity 应用。
* 了解什么是 [EIF](../../simulation/simulation.html)。
* 学习如何[采集模拟运行数据](../../mega/input-recording.html)。
## 为什么用 session 验证工具模拟运行是个好办法
**远程开发**：无需顶着烈日或严寒驻场，利用 EIF 数据，您在办公室就能开发基于大规模地理空间的 AR 应用。
**跨平台调试**：无需频繁连接各种移动设备，在 Windows PC 上即可模拟手机、头显等不同终端的定位和跟踪效果。
**问题反馈的“金标准”**：一个**能够复现异常的 EIF 文件**，是 EasyAR 团队为您解决定位与跟踪问题的**关键依据**。
> **注意**
尽管 EIF 数据记录得非常精确，模拟效果和实际使用效果可能依然存在差异。
并且模拟数据对现场的覆盖有限，在最终发布前务必进行实地测试。
## 操作步骤
通过以下步骤使用 session 验证工具模拟运行。
### 准备好现场录制的 EIF 文件
根据所选录制格式不同，录制好的EIF数据应为 `.mkveif` 文件（或 `.eif` 文件和 `.eif.json` 文件，这两个文件缺一不可）。
**`.eif` 和 `.eif.json`：**
![旧EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool05.png)
**`.mkveif`：**
![新EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool06.png)
### 对照 Block 稠密模型或全景摆放一些 3D 内容
![摆放3D内容](https://doc-asset.easyar.com/develop/unity/mega/media/verify-pc-camera03.png)
### 开启 Session 验证工具
点击场景中的 **AR Session (EasyAR)** > 确认其 **Inspector** 面板上的 **Frame Player** 已经**开启**。
![确认FramePlayer开启](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool03.png)
### 运行
点击工具栏按钮或点击 **Session Validation Tool** 上的运行按钮在 Unity 编辑器上开始运行这个工程。
![运行按钮](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool07.png)
运行后会弹出一个提示框，**这是正常的**，它只是提示现在正在使用 `Frame Player`。
![提示弹窗](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool08.png)
点击工具上的按钮打开 EIF 文件。
![打开EIF](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool09.png)
正常打开后它会自动播放，可以使用工具栏进行暂停/继续等控制，有些新格式的 EIF 也支持进度条跳转。
![控制进度](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool10.png)
运行效果：
若在工具 `EasyAR.Mega.BlockViewer (Dev)` 中加载了 Block 稠密模型，Block 稠密模型也会保持显示。这在进行位置比对或未放置模型的地方查看定位效果的情况下还是有用的。
一般来说可以将工具 `EasyAR.Mega.BlockViewer (Dev)` 关闭（`active` 设成 `false` 或删除场景节点），然后运行看到的就是在现实场景中叠加了虚拟物体的效果。
> **重要事项**
在使用时，你一定会注意到运行时显示在屏幕上或目视前方的诊断信息文字，仔细阅读 [UI 消息输出](../diagnostics/ui-messages.html)，仔细斟酌在开发阶段、测试阶段、应用上线之后应该采取何种配置，以及保留何种控制开关。与 EasyAR 的沟通通常需要提供这些信息，建议多利用而不是立马关闭。
默认设置下，启动后，在第一次定位到 `Block` 之前，整个 `MegaBlocks` 及其子节点的 `active` 都是 `false`，内容不会显示。
![MegaBlock显示状态](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool13.png)
在定位到之后，上述节点的 `active` 会变成 `true`，内容会显示出来并不断更新位置。
![MegaBlock定位到后显示](https://doc-asset.easyar.com/develop/unity/mega/media/verify-session-tool14.png)
如果要改变相关行为，或是更加自由的控制 active 行为，可以参考 [BlockRootController 组件参考](comp-BlockRootController.html) 和 [BlockController 组件参考](comp-BlockController.html)。
## 相关主题
* [session 验证工具](../simulation/tool.html)

---

## ARCore、AR Engine 版本兼容性
- 章节路径: `unity/motion-tracking/3rdparty-compatibility.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/3rdparty-compatibility.html

# ARCore、AR Engine 版本兼容性
本文介绍 EasyAR Sense Unity Plugin 对第三方运动跟踪 SDK 版本的兼容性。
## ARCore 版本兼容性
EasyAR Sense Unity Plugin 集成了 ARCore SDK 1.46.0。
* 使用集成的 ARCore SDK 时：支持至少 ARCore （Google Play Services for AR） 1.46.0 及以上版本。更早版本的 ARCore 服务是否支持需要看 Google 自身的兼容性。
* 使用 AR Foundation 或其它 ARCore SDK 的发布时，ARCore 兼容性将由这些框架决定。
## 华为 AR Engine 版本兼容性
EasyAR Sense Unity Plugin 集成了 AR Engine SDK 3.7.0.3。
* 支持至少 AR Engine 2.18 及以上版本。详细兼容信息建议查阅 AR Engine 官方说明。
EasyAR Sense Unity Plugin 不直接支持华为官方已不再维护的 `Huawei AR Engine Unity SDK` 或是其它第三方发布的类似 SDK。使用 AR Engine 也无需在 Unity 中另行导入这些 SDK。
> **重要事项**
AR Engine 的支持是通过自定义相机实现的。
在自定义相机或头显上使用试用产品（个人版 license、试用版 XR license 或试用版 Mega 服务等）时，EasyAR Sense 每次启动后会在 100 秒（Mega 用户可经由 EasyAR 商务在审批后调整时间长度）后停止响应。使用付费版本的 EasyAR Sense 和付费的 EasyAR Mega 服务没有这个限制。
## 相关主题
* [运动跟踪简介](../../motion-tracking/intro.html)
* [支持 ARCore 运动跟踪的设备](../../motion-tracking/devices-arcore.html)
* [支持 AR Engine 运动跟踪的设备](../../motion-tracking/devices-arengine.html)
* [AR Foundation 版本兼容性](../fundamentals/arfoundation.html)
* [EasyAR 全局配置参考](../fundamentals/setup-player.html)

---

## ARCoreFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-ARCoreFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-ARCoreFrameSource.html

# ARCoreFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ARCoreFrameSource.html)
>
探索 ARCoreFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-ARCoreFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## AREngineFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-AREngineFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-AREngineFrameSource.html

# AREngineFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.AREngineFrameSource.html)
>
探索 AREngineFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-AREngineFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## ARKitFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-ARKitFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-ARKitFrameSource.html

# ARKitFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.ARKitFrameSource.html)
>
探索 ARKitFrameSource 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-ARKitFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Auto：自动对焦模式。
* Fixed：固定对焦模式。|
|**Desired Size**|期望的相机图像大小。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Desired Frame Rate**|期望的相机图像帧率。选项：
* Default：使用默认值。
* Input：使用指定值。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## MotionTrackerFrameSource 组件参考
- 章节路径: `unity/motion-tracking/comp-MotionTrackerFrameSource.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/motion-tracking/comp-MotionTrackerFrameSource.html

# MotionTrackerFrameSource 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.MotionTrackerFrameSource.html)
>
探索 MotionTrackerFrameSource 组件窗口中的各项属性以自定义相机和运动跟踪参数。
![alt text](https://doc-asset.easyar.com/develop/unity/motion-tracking/media/comp-MotionTrackerFrameSource.png)
默认条件下组件截图。
|属性|描述|
|**Desired Focus Mode**|期望的对焦模式。选项：
* Default：使用默认值，实际选择与使用的 AR 功能有关。
* Input：使用指定值。选择 Input 时可选项：
* Continousauto：连续自动对焦模式，图像清晰度高，跟踪效果一般。实际对焦效果取决于设备能力。
* Medium：中等距离定焦模式，图像清晰度一般，跟踪效果较好，实际对焦效果取决于设备能力。|
|**Desired Resolution**|期望的分辨率。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Resolution\_1280：标准分辨率是 1280 x 960 或者 1280 x 720，实际分辨率取决于设备能力。
* Resolution\_640：标准分辨率是 640 x 480 或者 640 x 360，实际分辨率取决于设备能力。|
|**Desired Frame Rate**|期望的相机图像帧率。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* Camera\_FPS\_30：设备图像帧率是 30fps，实际帧率取决于设备能力。
* Camera\_FPS\_60：设备图像帧率是 60fps 或者 30fps，实际帧率取决于设备能力。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Desired Min Quality Level*|期望的最低允许的质量级别。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* NotSupported：设备不支持运动跟踪，可能是适配不达标或者尚未适配。
* Bad：设备不完全达标，尺度不稳定，可用于桌面尺度内的小场景等。
* Limited：设备不完全达标，尺度接近准确，可用于房间尺度内的中等场景，类似 AR 游戏、AR 导航等。
* Good：设备达标，尺度准确，可用于建筑物尺度的大型场景，类似 AR 游戏、AR 导航、三维重建等。|
|*Desired Tracking Mode*|期望的跟踪模式。选项：
* Default：使用默认值。
* Input：使用指定值。选择 Input 时可选项：
* VIO：只有跟踪和点击碰撞点云，CPU 和内存占用少，但是不支持平面检测、重定位和锚点。
* SLAM：同时跟踪和建图，支持丢失后的重定位、点击碰撞点云和平面检测，但是没有锚点，不支持实时校正位姿，且 CPU 和内存占用稍高。
* Anchor：同时跟踪和建图，支持丢失后的重定位、点击碰撞点云、平面检测和锚点，但是 CPU 和内存占用最高。
* LargeScale：适用于大场景下，同时跟踪和建图，支持丢失后的重定位、点击碰撞点云、平面检测和锚点。大景深下跟踪更稳定。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## EasyAR Sense Unity Plugin 版本 4 发行说明
- 章节路径: `unity/release-notes/release-notes-v4.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/release-notes/release-notes-v4.html

# EasyAR Sense Unity Plugin 版本 4 发行说明
> **注意**
最新的 EasyAR Sense Unity Plugin 版本为 4000.0。更多信息请参阅 [发行说明](release-notes.html)。
从版本 4 开始，过去被大家熟知的 EasyAR SDK 被赋予了一个新的名字：EasyAR Sense。EasyAR Sense 提供感知真实世界的能力。在 Unity 上，EasyAR Sense Unity Plugin 提供了一个 EasyAR Sense 的封装，方便开发者在 Unity 中使用 EasyAR Sense 的能力。
## 版本 4.6.5
>
> 发布日期：2024-12-25
>
EasyAR Sense Unity Plugin 4.6.5 绕过了一个可能的 Unity bug。
这将是最后一个支持 Unity 2019、Unity 2020 以及 AR Foundation 4 的发布版本。从 4.7 版本开始，EasyAR Sense Unity Plugin 将只支持 Unity 2021.3+ 以及 AR Foundation 5+。众多头显和眼镜的支持也将同步到来。
详细更新内容如下：
* 🩹 绕过一个可能的 Unity 6 URP 17 render graph bug，它会使 Windows DX11 上的渲染效果变得不可预测
## 版本 4.6.4
>
> 发布日期：2024-12-17
>
EasyAR Sense Unity Plugin 4.6.4 修复了稠密空间地图的显示问题，并提供 Unity 6+、URP 17+ 及 AR Foundation 5/6+ 的兼容性。
详细更新内容如下：
* ✨ 添加 Unity 6（URP 17+）的 Render Graph 支持
* ✨ 添加 AR Foundation 5/6 的 XROrigin 支持
* 🐛 修复使用稠密空间地图时的网格撕裂问题
* 🐛 修复使用稠密空间地图时生成的碰撞网格出现的错误日志
## 版本 4.6.3
>
> 发布日期：2023-10-13
>
EasyAR Sense Unity Plugin 4.6.3 修复了几个问题，并提供在 Unity 2023 中使用 URP 时的兼容性问题。
详细更新内容如下：
* ✨ 添加 URP 15 兼容性
* 🐛 修复仅使用 AR Engine 时相机朝向错误的方向
## 版本 4.6.2
>
> 发布日期：2023-04-03
>
EasyAR Sense Unity Plugin 4.6.2 修复了一些 bug。
详细更新内容如下：
* 🐛 修复线性色彩空间下稠密空间地图 mesh 的显示问题
* 🩹 解决（workaround）Camera\_CustomCamera 样例在 Unity 2022.2 和 2023.1（可能还有其它版本）中 Android 上可能崩溃的问题，看上去 Unity 的 JNI 部分在这些版本中存在 bug
## 版本 4.6.1
>
> 发布日期：2023-03-24
>
EasyAR Sense Unity Plugin 4.6.1 增加了一些小功能，修复了一些 bug。
详细更新内容如下：
* ⬆️ 更新 Sense 到 4.6.1.10366
* 🐛 修复稠密 mesh 在某些特殊情况下使用自定义相机时显示位置不对的问题
## 版本 4.6.0
>
> 发布日期：2023-02-13
>
EasyAR Sense Unity Plugin 4.6.0 带来了许多优化和改进，主要集中在这几方面：
1. 添加原生 Apple silicon 支持
我们从 EasyAR Sense 4.3 开始发布了 Apple silicon 的库文件。但在 Unity 自己支持之前，我们并没有办法让 Unity 认识这个库。在这个新的发布版中，我们将这个库文件引入 Unity 中，以支持最近一些为 Apple silicon 编译的 Unity 编辑器版本。
2. 添加内建 AR Engine 支持
我们在插件中添加了内建的 AR Engine 支持，可以使用用以支持 EasyAR Mega 和其它 EasyAR 功能的能力。这个改动用于替换华为老旧的 Unity 包，它在新的 Unity 版本中无法使用。如果您不希望使用 AR Engine，也可以很方便地关闭。
3. 拆分 AR Foundation 和 Nreal 支持到独立的扩展包
我们将 AR Foundation 和 Nreal 支持从主体插件包中拆了出来并做成了扩展包。这两个功能最初是通过使用条件编译加入插件包的。但是 Unity 对条件编译的支持并不非常完美，从而给开发者带来了很多障碍。将它们拆成扩展包的同时也可以让眼镜等设备支持的分发变得更加容易。今后会有许多使用 EasyAR 的新设备。
详细更新内容如下：
* ✨ 添加原生 Apple silicon 支持
* ✨ 添加内建 AR Engine 支持（所有 Unity 版本可用）
* 🚚 拆分和优化 Nreal（>= 1.6）支持
* 🚚 拆分和优化 AR Foundation（>= 4.1.3）支持
* ✨ 添加对 AR Foundation 5.x 包结构的兼容性
* ✨ 添加 UnityPackage 类用于在脚本中更方便地获取包版本和名字等
* ✨ 添加关闭所有自定义相机的选项
* ⚡ 优化 EasyAR Mega 支持
* ⚡ 优化没有可用 frame source 时的信息
* ⚡ 优化右键菜单
* ⚡ 切换使用新的运动融合接口
* 🐛 修复在文件不存在时，target 文件加载卡住且不报错
* 🐛 修复某个特殊情况下 frame source 无法使用
* 🔥 删除内置华为官方 Unity 插件支持（官方已不维护）
* 🔥 删除早于 4.4 版本的废弃接口和 prefab
* 🔥 删除构建 iOS 时 Universal architecture 的支持
* ⬆️ 更新 Sense 到 4.6.0
## 版本 4.5.0
>
> 发布日期：2022-03-04
>
EasyAR Sense Unity Plugin 4.5.0 增加了一些小功能，修复了一些 bug，增强了用户体验。根据 Google 的政策，这个版本将 ARCore SDK 更新至 1.23.0，并且在构建过程中添加了更加严格的检查。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🚚 移动 EasyAR Settings 到 Unity Project Settings，settings asset 将不再以资源形式加载
* ✨ 添加在构建过程校验 license key 的选项
* ✨ 添加支持使用 AR Foundation 及其它一些组件时使用彩色图像输入的选项
* ⚡ 优化在运动跟踪状态不稳定时的运动融合
* ⚡ 优化 CloudRecognizer 或 CloudLocalizer 创建失败的错误信息
* 🐛 修复 MotionTrackerFrameSource.CheckAvailability 在非 active 的 GameObject 上无法结束的问题
* ⬆️ ARCore：更新 ARCore SDK 至 1.23.0
* ⬆️ ARCore：在使用 ARCore 的构建中，Gradle 版本必需 >= 5.6.4
* 🔧 ARCore：使用 ARCore 的构建中，如果打包仅含 32 位的应用将会弹出警告信息
* ⬆️ 更新 Sense 到 4.5.0
**EasyAR Sense Unity Plugin Samples**
* 🔧 在融合样例中关闭 AR Foundation 的更新尝试
* 🔧 修改 ImageTracking\_CloudRecognition 样例，以更好的使用连接超时参数
## 版本 4.4.0
>
> 发布日期：2021-10-28
>
EasyAR Sense Unity Plugin 4.4.0 增加了许多新功能和改进，主要集中在这几方面：
1. 支持 Unity AR Foundation
EasyAR 现在可以与 AR Foundation 协同工作，这增强了 EasyAR 与 AR Foundation 双方的能力，可以同时获得双方的优势。比如，在现实环境中使用 EasyAR 稀疏空间地图定位设备的同时，可以利用 AR Foundation 暴露的 ARKit 或 ARCore 的能力，比如环境探针。
AR Foundation 支持是通过插件底层 EasyAR Sense 的灵活功能之一，自定义相机实现的。以此作为参考，现在可以比以往更容易地自定义插件来支持其它 AR 框架。
2. 支持 Nreal 眼镜（带有 VIO 能力的 AR 眼镜）
EasyAR 现在可以支持 Nreal 眼镜。Nreal 支持是通过插件底层 EasyAR Sense 的灵活功能之一，自定义相机实现的。
3. 支持 Unity 通用渲染管线（Universal Render Pipeline）
从这个版本开始，URP 支持将会内置在插件中。
4. 支持 EasyAR Cloud SpatialMap
EasyAR Cloud SpatialMap 提供城市级 AR 云方案。EasyAR Sense Unity Plugin 是在应用端支撑 EasyAR Cloud SpatialMap 的重要开发工具之一。
5. 新增运动融合功能
只要任意一种运动跟踪功能可以使用，EasyAR 运动融合就可以让静止图像和物体的跟踪更加稳定，并且可以在目标离开相机视野之后继续跟踪。这个新功能不是像在之前版本中可以做到的那样简单的同时运行运动跟踪和图像跟踪，而是在融合两个跟踪的基础上提供了更优的跟踪结果。
6. 全新的 AR Session 创建流程
AR session 及其它 AR 组件的创建现在可以使用 GameObject 菜单完成，使用更加灵活方便。Prefab 已经标记为过时，并将在将来的发布中删除。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🚀 添加 Unity AR Foundation 支持
* 🚀 添加 Unity 通用渲染管线（URP）支持
* 🚀 添加 Nreal 眼镜支持
* 🚀 添加运动融合功能，在运动跟踪可用的时候优化图像和 3D 物体跟踪
* 🚀 添加 `CloudSpatialMapLocalizerFrameFilter` 以支持 EasyAR Cloud SpatialMap
* 🚀 引入创建 AR session 和其它 AR 组件的新方法
* ✨ 添加以功能组织的 GameObject 菜单项，用于创建 AR session 和其它 GameObject
* ✨ 添加许多有用的 GameObject 预设菜单项
* 🔥 prefab 已经标记为过时，并将在将来的发布中删除
* ✨ 添加更多 frame source 以扩展 AR 框架和设备支持
* ✨ 添加 `ARCoreFrameSource` & `ARKitFrameSource` & `MotionTrackerFrameSource` 以替换 `VIOCameraDeviceUnion`，运行时的策略选择由更灵活的 `ARComponentPicker` 替换
* ✨ 添加 `ARFoundationFrameSource` 以支持 Unity AR Foundation
* ✨ 添加 `HuaweiAREngineFrameSource` 以支持华为 AR Engine
* 🔥 `VIOCameraDeviceUnion` 已经标记为过时，并将在将来的发布中删除
* 🚚 `VideoCameraDevice` 重命名为 `CameraDeviceFrameSource`
* 🚚 `RenderCamera` 被移动到了 `FrameSource` GameObject 上
* 🔧 AR session 中的 `Camera` 会由 `FrameSource` 在运行时进行选择
* 🔧 `MotionTrackerFrameSource` 默认会尝试从服务器更新设备支持列表，超时时间为 2s
* ✨ `ARCoreFrameSource` & `ARKitFrameSource` 获得了可以控制自动对焦开关的能力
* ✨ 优化 AR session 工作量和接口
* ✨ 添加 `ARComponentPicker` 组件来在运行时挑选可用的 frame source 及其它组件
* ✨ 添加 `ARSession.AvailableCenterMode` 以查询在一个 session 中所有可用的中心模式
* ✨ 添加 `ARSession.Origin` 以获取在运动跟踪功能在运行时，相机运动的相对物体
* ✨ 添加 `ARSession.TrackingStatus` 以获取设备运动跟踪质量
* ✨ 添加 `ARSession.State` & `ARSession.StateChanged` 以查询 ARSession 的状态
* ✨ 优化中心模式处理
* 🔧 一个 session 中可用的中心模式将由运行时选择的 frame source 来决定
* 🔧 空间地图可用在所有中心模式下使用
* 🔥 删除 `ARCenterMode.ExternalControl`，其功能被 `FrameSource.IsCameraUnderControl` == `false` 所替代
* 🚚 重命名 `ARCenterMode.WorldRoot` 为 `ARCenterMode.SessionOrigin`
* ✨ 优化初始化过程，尤其是首次使用体验
* ✨ 添加 `EasyARController.Initialize` & `EasyARController.Deinitialize` 接口以在启动后支持手动初始化
* 🔧 如果 EasyAR 库文件未加载成功，会由错误提示
* 🔧 改善许可证校验失败的弹出信息
* ✨ 优化构建过程，尤其是首次使用体验
* ✨ 如果插件包未由 Unity 包管理器正确导入，将会生成编译时和加载时错误
* ✨ 在 pre-build 或 post-build 过程中如果出错，构建将会失败
* ✨ 在使用 ARCore XR Plugin 的时候，ARCore SDK 的选择默认将会自动处理
* ✨ 添加在构建中检查 iOS usage description 的功能
* 🔧 构建中将不再使用 `Assets/HiddenEasyAR`
* ⚡ 优化稀疏空间地图的跟踪稳定性
* 🔧 `SurfaceTrackerFrameFilter` 可用与运动跟踪设备一同使用
* 🐛 修复在某些情况下， target controller 事件可能会在组件销毁后触发的问题
* 🐛 修复 `MotionTrackerCameraDevice` 的跟踪模式未正确设置
* 🔧 相机的 `field of view` 现在将被设置成与投影矩阵一致
* ⬆️ 更新 Sense 到 4.4.0
**EasyAR Sense Unity Plugin Samples**
* ✨ 添加新样例 `ARFoundation` 以展示结合 Unity AR Foundation 的使用
* ✨ 添加新样例 `HuaweiAREngine` 以展示结合华为 AR Engine 的使用
* ✨ 添加新样例 `Eyewear\_Nreal\_SpatialMap\_Building` 以展示如何在 Nreal 眼镜上使用空间地图
* ✨ 添加新样例 `Eyewear\_Nreal\_ImageTracking\_InWorld` 以展示如何在 Nreal 眼镜上使用图像跟踪
* ✨ 添加新样例 `MotionTracking\_Fusion` 以展示在单一场景中启动时自动选择以及运行时手动切换可用的 frame sources，以支持最多的设备并在支持的设备上启用每个 AR 框架的独有功能
* 🔧 修改 `FrameRecording` 样例以在运动跟踪功能可用时自动录制运动跟踪 session
* 🚚 重命名样例 `ImageTracking\_MotionExtend` 为 `ImageTracking\_MotionFusion` 以展示新的运动融合功能
* 🚚 重命名样例 `Eyewear\_ImageTracking` 为 `Eyewear\_DeviceHasNoTracking` 以明确样例的用途
* 🚚 重命名样例 `MapLocalizing\_Sparse` 为 `SpatialMap\_Sparse\_Localizing`
* 🚚 重命名样例 `SpatialMap\_Dense\_BallGame` 为 `SpatialMap\_Dense\_BallGame`
* 🚚 重命名样例 `SpatialMap\_Sparse\_ImageTarget` 为 `SpatialMap\_Sparse\_ImageTarget`
* 🚚 重命名样例 `MapBuilding\_Sparse` 为 `SpatialMap\_Sparse\_Building`
* 🚚 重命名样例 `MapBuilding\_Sparse\_Dense` 为 `SpatialMap\_Sparse\_Dense\_Building`
## 版本 4.3.0
>
> 发布日期：2021-04-07
>
EasyAR Sense Unity Plugin 4.3.0 使用 [Unity package](https://docs.unity3d.com/Manual/Packages.html) 组织文件，简化了打包过程中的配置，解决了插件更新难的问题。从这个版本开始，仅支持 Unity 2019.4 及更高版本。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🚀 使用 Unity Package 替换 Asset Package，兼容 Unity 2019.4 及以上版本，老版本不再兼容
* ✨ iOS：自动配置 bitcode，不再需要修改 XCode 工程的 bitcode 设置
* ✨ iOS：使用 Sense 的动态库 framework，不再需要修改 XCode 工程的 framework 设置
* ✨ Android：使用 Sense 的 aar 文件，包含 proguard rule
* ✨ Android：不再使用 Plugins 文件夹中的 Android Manifest，可以根据使用的功能控制 Manifest 中的权限设置
* ⬆️ ARCore：替换随插件分发的 ARCore SDK 为官方 ARCore SDK 1.6 版本的 aar 文件
* ✨ ARCore：添加控制 ARCore 使用的选项，解决与 AR Foundation 的冲突
* 🔧 合并菜单项
* ⬆️ 更新 Sense 到 4.3.0
**EasyAR Sense Unity Plugin Samples**
* 🔥 删除为老版本 Unity 准备的视频播放 workaround
* 🐛 修复 custom camera sample 在某些 Android 设备上无法打开 camera
## 版本 4.2.0
>
> 发布日期：2021-01-25
>
EasyAR Sense Unity Plugin 4.2.0 增加了 InputFrameRecorder/InpuptFramePlayer 支持，可以用于在编辑器中测试和调试设备上的运行效果。同时修复了一些 bug，增强了用户体验。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* ✨ 添加 InputFrameRecorder/InpuptFramePlayer 支持
* ✨ 运动跟踪标定参数默认会从服务器更新
* 🚚 重新组织文件
* ⚡ 简化 hit test 调用
* 🐛 修复 tracker 销毁后 target 不会丢失
* 🐛 修复某些情况下相机图像旋转 180 度
* 🐛 修复线性颜色空间下相机图像色彩
* ⬆️ 更新 Sense 到 4.2.0
**EasyAR Sense Unity Plugin Samples**
* ✨ 添加 FrameRecording sample 以演示 InputFrameRecorder/InpuptFramePlayer 的使用
* ⚡ 优化运动跟踪 sample 的平面检测
## 版本 4.1.0
>
> 发布日期：2020-07-16
>
EasyAR Sense Unity Plugin 4.1.0 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* ✨ 插件脚本中添加完整的文档
* ✨ 插件详细的使用说明和样例解析文档上线
* ♻️ 重写 CloudLocalizerFrameFilter 以支持单次扫描
* 🐛 修复当 camera 图像使用 ARHorizontalFlipMode.World 进行翻转时 invert culling 对场景中其它相机的污染
* 🐛 修复高 dpi 显示器上 image target gizmo 的显示问题
* 🐛 修复 RGB/RGBA 像素类型的 camera 图像旋转
* ⬆️ 更新 Sense 到 4.1.0
**EasyAR Sense Unity Plugin Samples**
* ♻️ 重写 MotionTracking sample，演示运动跟踪的平面检测功能
* ♻️ 重写 ImageTracking\_CloudRecognition sample，使用新的接口功能
* 🔧 修改 ImageTracking\_Targets sample，使用水平和垂直摆放的 image target
## 版本 4.0.1
>
> 发布日期：2020-05-13
>
EasyAR Sense Unity Plugin 4.0.1 增加了一些小功能，修复了一些 bug，增强了用户体验。
详细更新内容如下：
**EasyAR Sense Unity Plugin**
* 🐛 小修复
* ⬆️ 更新 Sense 到 4.0.1
**EasyAR Sense Unity Plugin Samples**
* ♻️ 重写 TargetOnTheFly sample，更加简洁和稳定
## 版本 4.0.0
>
> 发布日期：2019-12-30
>
EasyAR 已经成长为一个大家族，从版本 4 开始，过去被大家熟知的 EasyAR SDK 将被赋予一个新的名字：EasyAR Sense。EasyAR Sense 提供感知真实世界的能力。这个版本包含了所有 3.0 的功能。
EasyAR Sense 是一个独立 SDK，它不依赖于非系统组件或是像 Unity3D 这样的工具，可以提供灵活的基于数据流的组件化 API。
而关于 Unity 的支持，EasyAR Sense Unity Plugin 是一个非常薄的封装，用于在 Unity 中暴露 EasyAR Sense 的功能。EasyAR Sense Unity Plugin 的所有代码经过良好的接口设计且都是开源的。您可以直接使用这个插件来快速创建 AR 体验，也可以参考插件代码来更加灵活和自定义的使用 EasyAR Sense 接口和功能，或是创建属于自己的 Unity 插件。
EasyAR Sense Unity 插件获得了巨大提升，主要集中在这几方面：
1. 连贯的设计演化
EasyAR Sense 1/2/3 的 Unity 插件的所有功能和优点都在这个版本中保留了下来。
这个版本的插件尽可能多的使用了 Unity 本身的功能，比如使用 OnEnable/OnDisable 来控制 start/stop。大多数 EasyAR Sense 功能都可以不需要写脚本直接工作。
所有 EasyAR Sense 4.0 的新功能都已经支持，许多 bug 也已经修复。
2. 编辑器体验优化
编辑器中可以显示 image target 的 gizmo，以更好的体验替代过去版本中编辑模式下自动生成的 mesh。
严重错误（比如 license key 验证失败）会通过弹出消息在屏幕上显示，用于帮助 debug。
除 API外，提供了 Unity 工具窗口来生成 image target data。
3. 更多样例，覆盖更多细节 API
添加了展示所有新功能以及不同算法组合工作的样例。
添加了 AR 眼镜支持的样例，预先标定了两款 AR 眼镜：影创 Action One 及 EPSON BT-350。
社区中许多关于“如何使用”的问题在这些样例中都有解答。感谢大家的反馈！
EasyAR Sense 4.0 提供免费个人版、月付费专业版和定制化功能企业版三种订阅模式。
功能、定价、付款方式等的详细信息可以在 [产品页面](https://www.easyar.cn/view/sdk.html) 及 [价格页面](https://www.easyar.cn/price.html) 了解。
详细更新内容如下：
**Unity Plugin for EasyAR Sense 4.0.0**
* 🚀 支持 EasyAR Sense 4.0.0 的所有新功能: 稀疏空间地图、稠密空间地图以及运动跟踪
* 🚀 恢复类似 Sense 2.3 的接口设计和行为，并有非常多改进
* ✨ 添加严重出错情况的弹出消息（可在 EasyARController 上关闭）
* ✨ Components: 大多数组件可以使用 Unity 组件的 enabled 来控制 start/stop
* ✨ Component ARSenssion: AR 入口，控制 center mode，具备支持外部设备的能力，比如自定义相机及 AR 眼镜
* ✨ Component ARAssembly: 展示 EasyAR Sense 组件化 API 的组装过程，支持所有 EasyAR Sense 的组件
* ✨ Component ImageTargetController: 改善对不同类型输入的支持，可以从本地文件系统或 web URL 加载图像和 .etd 文件
* ✨ Component CameraImageRenderer: camera 图像渲染可由 disable 该组件来关闭
* ✨ Component VIOCameraDeviceUnion: 运动跟踪，可自动选取使用设备可用的 ARKit、ARCore 或 EasyAR 运动跟踪功能
* ✨ Scene: 添加 target gizmo，可在 Unity 编辑器中显示 target 细节
* ✨ Asset: 添加全局服务配置及 gizmo 控制选项
* ✨ Window: 添加生成 image target data（.etd 文件）的窗口
* ✨ Window: 添加菜单跳转到 license key 设置界面和其他全局配置
* 🐛 修复目标跟踪存在一帧延迟的问题
* 🐛 修复阻塞式 target 加载，减少 target 加载时间
* 🐛 修复 target size 获取
* 🐛 许多其他改进及 bug 修复
* ⬆️ 更新 Sense 到 4.0.0
**Samples of Unity Plugin for EasyAR Sense 4.0.0**
* 🚀 添加许多 sample，展示 Sense 功能及接口使用
* 🚀 添加回所有 Sense 2.3 的 sample
* 🚀 添加展示新功能的 sample，包括稀疏空间地图、稠密空间地图以及运动跟踪，还有这些功能如何与图像跟踪等其他组件同时使用的 sample
* ✨ 添加 sample 启动器，可以通过启动器加载所有 samples
* ✨ 添加屏幕上显示的组件状态信息，覆盖所有 sample
* ✨ 添加展示 AR 眼镜支持的 sample
* ✨ 添加表面跟踪与图像跟踪同时使用的 sample
* ✨ 添加获取 camera 图像贴图和控制 camera 显示的 sample
* ✨ 添加修改视频 aspect ratio （Unity VideoPlayer 功能） 适配 image target 的 sample
* ✨ 添加展示从图像扩展跟踪的 sample
* ♻️ 云识别 sample 现在使用本地缓存，并在跟踪状态下停止云端识别，以覆盖常见的使用场景
* 🐛 优化 coloring3D sample，修复 bug

---

## EasyAR Sense Unity Plugin 发行说明
- 章节路径: `unity/release-notes/release-notes.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/release-notes/release-notes.html

# EasyAR Sense Unity Plugin 发行说明
我们很高兴地宣布 EasyAR Sense Unity Plugin 4000 发布。此版本标志着 EasyAR 具备了完善的 API 和与时俱进的设备支持，同时新版本发布也将比以往更加频繁。
下载 [EasyAR Sense Unity Plugin 4000](https://www.easyar.cn/view/download.html) 以享受这些新功能和改进。
## 历史版本
* [EasyAR Sense Unity Plugin 版本 4 发行说明](release-notes-v4.html)
## 版本 4000.0.1
>
> 发布日期：2025-11-14
>
* 🐛 修复：解决了在启用 minify 打包的 Android 构建中，因缺少静态方法（ `loadLibraries` 、 `setupActivity` ）而可能触发的运行时 `AndroidJavaException` 异常，该错误会导致 EasyAR 无法运行。
## 版本 4000.0.0
>
> 发布日期：2025-10-20
>
从这个版本开始，EasyAR Sense Unity Plugin 将遵循 Unity 所要求的 [包版本控制（使用 Semantic Versioning）](https://docs.unity3d.com/Manual/upm-semver.html) ，因此版本号将与 EasyAR Sense 相异，发布频率也可能不同。该版本插件内包含 EasyAR Sense 4.7.0 正式版。
EasyAR Sense Unity Plugin 4000.0.0 迎来了大幅改变，主要集中在这几方面：
1. Unity 及 AR Foundation 兼容性变化
从这个版本开始，EasyAR Sense Unity Plugin 将只支持 Unity 2021.3 及更新版本，Unity 6 支持也已经完善。同时，AR Foundation 支持已经合并到插件包内，这个版本将只支持 AR Foundation 5 及更新版本，其使用经过大量简化。如果场景中添加了 AR Foundation 的组件，无论运行之后 AR Foundation 是否最终使用，场景配置和脚本代码都可以不变。
2. 与时俱进的头显支持，新增支持多款 OST/VST 头显
经过与行业内多家企业多年的打磨，EasyAR 对头显的支持已经标准化。现在您可以通过 EasyAR Sense Unity Plugin 扩展实现第三方头显设备的支持（可能需要头显厂商提供部分数据接口）。这个版本内置了 Apple Vision Pro 以及 XREAL Air2 Ultra 的支持，同时通过 EasyAR Sense Unity Plugin 扩展包支持 Pico 4 Ultra Enterprise 及 Rokid AR Studio。
同时您也可以从 EasyAR 的一些合作伙伴那里获取其它设备的支持扩展包（比如 Xrany 元霓）。
3. 完善 Unity 组件接口，大幅优化 ARSession 工作流
这个版本是第一个通过 Unity 组件完整封装 EasyAR Sense 功能的版本。ARSession 经过了大量优化和重写，现在您可以轻松实现设备或功能的支持判断，根据具体情况启动或停止 ARSession 以实现运行时切换 ARSession 或不同 AR 功能。同时，您也可以使用 ARSessionFactory 在运行时创建 ARSession 及相关组件。这个版本还添加了惯性导航和 3DoF 相机功能，这些功能主要为 EasyAR Mega 所设计，但也可以单独使用。
4. 新增多个开发及诊断工具
这个版本增加了提供了全新的 EIF 录制和播放功能，虽然 EIF 录制和播放在过去的版本中也能使用，但使用 EIF 从未如此简单。您现在可以在 Unity 编辑器中使用时诊断工具 Session Validaion Tool 直接播放 eif 并驱动您的场景，无论是图像跟踪、空间地图还是 EasyAR Mega，都可以在电脑上还原设备上的运行效果。现在您可以使用运行时诊断面板 EasyAR Diagnostics Panel 在 app 中轻松开启 eif 录制功能，或是随时开关 ARSession 及其组件的关键状态信息显示。同时，这个版本的 sample 已经全部重写，运行 sample 就可以直接看到 ARSession 状态以及录制 eif 的按钮以方便使用。
5. EasyAR Mega 工具全面公开
这个版本集成发布了 Mega Studio 2.12。今后插件的更新将更加频繁，Unity 侧 Mega 工具将逐步合并进插件内部并与插件常规更新合并发布。除了过去预发布版本中的更新之外，这个版本会默认开启惯导支持，进一步大幅拓展 EasyAR Mega 的设备支持。这个版本还包含对最新版本 EasyAR Mega Landmark 服务的支持。使用 EasyAR Mega 可以通过 [EasyAR 网站页面](https://www.easyar.cn/view/apply.html) 进行申请。
详细更新内容如下：
**Unity 及 AR Foundation 兼容性变化：**
* 🔧 Unity：支持 Unity 2021.3 及更新版本（包括 Unity 2022.x/Unity 6.x）
* 🔥 移除对 Unity 2019/Unity 2020 的支持
* 🔥 移除用于 Unity 2019 的 gradle 版本检测
* 🔥 移除用于 Unity 2019 的选项 DisableARCoreAREngine
* ✨ Unity 6：全面支持 Unity 6
* ✨ 支持 URP 17+ 及 Render Graph
* 🐛 已修复：Unity 6 上 ClassLoader 行为变化导致 ARCore 失效
* 🐛 已修复：Render Scale 非 1 时相机渲染失效
* 🐛 Unity 6 自身 BUG：在 iOS/Mac 设备上可以观察到视觉故障和伪影。该问题仅发生在需要获取相机纹理的情况，我们添加了部分缓解措施但无法完全消除。已反馈至 Unity，见 [Unity Issue UUM-87787](https://issuetracker.unity3d.com/issues/ios-visual-artifacts-are-visible-when-the-cameras-feed-is-rendered-to-a-texture) 。Unity 6.2 以上可以通过设置 Universal Render Pipeline Asset 中的 Render Scale 为 0.96-1.05 以外的数值来规避这个问题。
* 🐛 Unity 6 自身 BUG：Windows DX11 上的渲染效果不正常。我们在 Unity 6.0-6.1 中已添加缓解措施。实测 Unity 6.2 已修复该问题。
* ✨ AR Foundation：支持 AR Foundation 5 及更新版本，大幅简化使用
* ✨ AR Foundation 支持已经合并到插件包内，不再需要单独导入包（特殊需要可以通过配置选项关闭）
* ✨ 支持复用 `Unity.XR.CoreUtils.XROrigin` 作为 ARSession 的原点，支持复用 XROrigin 的 Camera
* ✨ 添加 `Unity XR Auto Switch` 配置选项，默认处理 Unity XR（包含 AR Foundation）物体的切换
* ✨ 通过 EasyAR 菜单创建的 ARSession 自动包含并默认开启 AR Foundation 支持
* ✨ 绝大部分 sample 都已添加 AR Foundation 支持（AR Foundation 本身需要手动导入并正确配置）
* 🔧 ARCore 及 ARKit 可单独控制，且可控制 EasyAR 内置的 ARCore/ARKit 与 AR Foundation 的 ARCore/ARKit 的优先顺序
* 🔥 移除对 AR Foundation 4 的支持
* 🔥 移除对 ARSessionOrigin 的支持，仅支持 XROrigin
* 🔥 移除代理执行 AR Foundation 的 ARCore 安装流程
* ✨ 全面兼容 Input System Package
**与时俱进的头显支持，新增支持多款 OST/VST 头显：**
* 🚀 头戴显示设备接口已稳定，支持第三方接入
* ✨ 支持第三方设备接入（需要头显厂商提供特定数据接口）
* ✨ 支持 XROrigin 及 XR Interaction Toolkit
* ✨ 简化并统一所有头显样例，零代码，并支持功能切换
* ✨ 支持鱼眼相机输入
* ✨ 支持自定义相机输入 3DOF 数据
* ✨ 添加菜单功能：Extensions，整合所有扩展菜单项
* 🐛 修复部分头显运行 DenseSpatialMap 时出现渲染异常
* 🔥 移除 ActionOne 和 BT350 等古早眼镜 sample
* ✨ 内建支持 Apple Vision Pro
* ✨ 支持 Metal、RealityKit 及 Hybrid 模式
* ✨ 支持 visionOS >= 2.0，支持 visionOS 26
* ✨ 内建支持 XREAL Air2 Ultra（需要 XREAL SDK >= 3.1）
* ✨ 不再需要导入单独的支持包
* ⚡ 优化 XREAL 上的运行效果
* 🔥 移除 XREAL Light 支持
* ✨ 通过 EasyAR Sense Unity Plugin 扩展分发 Pico 及 Rokid 等其它设备支持
* ✨ 提供第三方设备接入的参考模板 `com.easyar.sense.ext.hmdtemplate`
* ✨ 支持 Pico 4 Ultra Enterprise（需要 PICO Unity Integration SDK >= 3.1）
* ✨ 支持 Rokid AR Studio（需要 Rokid Unity OpenXR Plugin >= 3.0.3）
* ✨ 这些扩展将支持今后多个版本的 EasyAR Sense Unity Plugin
* ✨ 支持 EasyAR XR License
* 🔧 头显上使用 EasyAR 需要 EasyAR XR License 并保证首次联网（试用需每次联网）
**完善 Unity 组件接口，大幅优化 ARSession 工作流：**
* 🚀 完善 Unity 组件层封装
* ✨ 完善场景组件，提供所有 EasyAR Sense 功能
* 🔥 移除所有通过组件封装的 EasyAR Sense 层接口
* 🔥 移除所有内部接口
* ✨ ARSession：重写并大幅优化工作流
* ✨ 支持在任意时刻启动和停止 session
* ✨ 支持 session 自动启动控制
* ✨ 支持不黑屏切换 session 功能和输入源
* ✨ 简化设备支持判断，以一致接口提供
* ✨ 启动时更新 MotionTracker、ARCore、AR Engine 的设备支持列表
* ✨ 支持设备列表更新后 session 自动重启
* ✨ 支持获取详细 session 损坏信息
* ✨ 添加 session 内部状态自检
* 🔥 移除 ARComponentPicker，其功能由其余 session 流程替代
* 🔥 禁止多个 ARSession 同时运行
* ✨ ARSessionFactory：提供运行时创建 ARSession 及相关组件的功能
* ✨ 支持通过 ARSessionFactory 运行时创建与编辑器菜单相同的 session
* ✨ 添加 Frame Source 排序功能（含菜单项）
* ✨ FrameSource：添加惯导和 3DoF 支持
* ✨ 添加 InertialCameraDeviceFrameSource 用于支持惯性导航
* ✨ 添加 ThreeDofCameraDeviceFrameSource 用于支持 3DoF 的相机
* ✨ 添加菜单功能：Frame Source by Transform Type，提供所有内置 FrameSource 的列表
* ⚡ 优化 Inspector 选项
* ✨ 其它接口调整及功能更新
* ✨ 添加使用 Texture2D 创建 ImageTarget 的功能
* ✨ 添加 ImageMaterial 用于渲染 Image 类型的数据（相机图像或 Target 图像等）
* ✨ 添加 ActiveController 用于控制 GameObject 的 active，统一相关控制逻辑
* ✨ 添加在桌面上模拟屏幕旋转的功能
* ✨ 添加 XROriginChildController，控制 Session 原点下物体的行为
* 🔥 移除 WorldRootController
* 🔧 稀疏空间地图接口拆分成 Builder 和 Tracker 两个不同功能组件
* 🔧 调整 EasyARController，提供应用/系统级静态功能
* 🔧 统一 Target 组件接口
* 🔧 统一服务访问数据的接口
**新增多个开发及诊断工具：**
* 🚀 添加编辑时诊断工具：Session Validaion Tool
* ✨ 简化在任意场景中播放 eif
* ✨ 支持控制 eif 播放流程
* ✨ 支持控制 session 流程
* 🚀 添加运行时诊断面板：EasyAR Diagnostics Panel
* ✨ 添加 Developer Mode 开关，默认点击屏幕 8 次开启和关闭 Diagnostics Panel，简化线上 app 录制 eif 和问题反馈
* ✨ 支持自定义 Developer Mode 开关，使用自定义交互开关 Diagnostics Panel
* ✨ 支持控制 eif 录制
* ✨ 支持控制 session 信息显示
* ✨ 支持控制 eed 录制
* ✨ 添加全新的 EIF 录制和播放功能
* ✨ FrameRecorder 会自动组装进 ARSession，不再需要手动选择
* ✨ FrameRecorder 会默认自动生成文件名以支持无脚本使用
* ✨ FramePlayer 使用新格式录制的数据支持播放跳转及速度调节，文件体积降低
* 🔧 支持在电脑上使用 eif 驱动场景和 AR 功能（非新功能）
* ✨ 添加 DiagnosticsController，统一和优化诊断功能
* ✨ 添加信息分级显示及控制，默认所有错误及警告信息都会通过 UI 展示
* ✨ 添加显示 ARSession 及其组件的关键状态信息的功能，默认会通过 UI 展示并每帧更新
* 🔧 使用诊断功能简化问题反馈信息的获取
* 🔥 删除 GUIPopup
* 🔧 优化异常状态行为及错误信息展示
* 🔧 优化无可用 frame source 时的错误信息
* 🔧 URP 环境使用 EasyAR 而非 AR Foundation 或头显渲染相机图像时，未正确配置 RendererFeature 会报错并中断 ARSession 执行
* 🔧 修改 Origin 默认的 Active 控制策略，在跟踪丢失时内容贴屏而非消失
* 🔧 自定义相机或头显上使用试用产品时，到达限制时间将隐藏所有内容以避免效果误判
* 🔧 优化配置页面内容和选项
* ✨ 支持选择 EasyAR Sense 库的变种
* 🔒 应用权限部分除相机权限外，其余权限不再可改，由 EasyAR Sense 库变种及 Mega 是否启用而决定
* 🔧 功能及服务器配置按 EasyAR 功能分组
* 🔧 集中管理第三方 AR SDK 配置
* 🔧 集中管理针对 Unity 的 Workaround 配置
**EasyAR Mega 工具全面公开：**
* 🚀 全面公开，同步更新
* ✨ 集成发布 Mega Studio 2.12
* 🔧 Unity 侧 Mega 工具将逐步合并进插件内部，今后仍将只提供最新版本的整合包，但将与 EasyAR Sense Unity Plugin 常规更新合并发布
* 🔧 EasyAR Mega 仍需通过 [EasyAR 网站页面](https://www.easyar.cn/view/apply.html) 申请并通过后才能使用
* ✨ 新增支持 EasyAR Mega Landmark
* ✨ 新增支持 5DOF 惯导并默认开启，进一步大幅拓展 EasyAR Mega 的设备支持
* ✨ 新增支持使用 API Token 访问 Mega 服务
* 🔧 优化 Mega 效果及开发体验（包含在过去更新的 4.7.x 版本内）
* ✨ 支持 3DOF 纯旋转模式和 0DOF 模式（默认未启用）
* ✨ 添加 EditorCameraDeviceFrameSource 用于编辑器诊断，避免由于不完整的复制 sample 导致手机上错误运行
* ✨ 使用 Mega时录制老版本 eif 数据，FrameRecorder 将自动生成 .eif.json 文件
* 🔧 使用 LocationInputMode 替代远程调试的退化选项
* 🔧 拆分无跟踪模式为独立组件，通常不再需要使用和关注
* 🔧 添加 BlockRootSource 选项，默认配置下忘记设置 BlockRoot 将报错
* 🔧 调整定位到多 block 时的默认行为，确保多 block 不会被默认使用
* 🔧 调整部分接口命名
* 🔧 在 Session 包含 Mega 但无法使用时抛出更明确的异常
* 🔧 调整 Mega 支持的 MotionTracker 最低 QualityLevel 为 Limited
* 🐛 修复 CloudLocalizerStatus.WakingUp 状态未正确转义导致运行报错
* 🔧 部分优化及修改见 EasyAR Sense 的更新日志
**Sample 重写及优化：**
* ✨ 重写所有 sample
* ✨ 兼容不同 Input System 配置
* ✨ 兼容 URP17+
* ✨ 兼容使用 AR Foundation
* 🔧 兼容不使用 AR Foundation
* 🔧 保留少量不含 AR Foundation 支持的 sample
* ⚡ 优化脚本及接口调用
* 🚚 部分 sample 已重命名
* 🔧 替换 sample 内模型和视频等资源
* ⚡ 减少 streaming assets的使用，仅在展示特定功能的 sample 中使用并导入
* ✨ 使用 Texture2D 创建 ImageTarget
* ✨ 增加新功能和接口演示
* ✨ 添加 Workflow\_ARSession sample，用于学习 session 基础流程和设备支持等
* ✨ 添加 Workflow\_FrameSource\_ExternalImageStream sample，以视频作为自定义相机（不能用于头显）
* ✨ 添加 Combination\_BasedOn\_MotionTracking sample，用于学习运动跟踪可用时各种功能的使用、切换以及 AR Foundation 切换
* ✨ 添加 Combination\_BasedOn\_AppleVisionPro sample，用于展示 Apple Visio Pro 上各种功能的使用和切换
* ✨ 添加 Combination\_BasedOn\_Xreal sample，用于展示 XREAL 设备上各种功能的使用和切换
* ✨ 添加多个 Mega sample（包含在过去更新的 4.7.x 版本内）
* ✨ 添加 Workflow\_FrameSource\_CameraDevice 中切换相机尺寸和 torch 模式的功能
* 🔥 移除单独的 AR Foundation sample，其功能已经包含在其它 sample 中
* 🔥 移除 FrameRecording sample，其功能已经包含在其它 sample 中
* 🔥 移除 MotionTracking\_Fusion sample，其功能已经包含在 Combination\_BasedOn\_MotionTracking 中
* 🔥 移除 SurfaceTracking\_ImageTarget sample，功能组合仍可用轻松实现
* 🔥 移除 Camera\_CustomCamera sample，如有需要仍可自行实现
* 🔥 移除 ActionOne 和 BT350 等古早眼镜 sample
* ✨ 简化 eif 录制和播放使用
* ✨ 所有 sample 均添加 eif 录制按钮，录制的 eif 文件可在编辑器内使用
* ✨ 重写 launcher，加入 sample 说明
* 🐛 修复通过 launcher 加载 sample 场景偏暗的问题
**EasyAR 及第三方 AR 功能集成：**
* ⬆️ 更新 EasyAR Sense 到 4.7.0 正式版
* ⬆️ 更新 EasyAR AR Engine Interop
* ⬆️ 更新 ARCore SDK 到 1.46.0
* 🔧 在部分无法合理运行 AR Engine 的手机上禁用 AR Engine
* 🐛 修复 Unity 6 上 ClassLoader 行为变化导致 ARCore 失效

---

## FramePlayer 组件参考
- 章节路径: `unity/simulation/comp-FramePlayer.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/comp-FramePlayer.html

# FramePlayer 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.FramePlayer.html)
>
探索 FramePlayer 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/comp-FramePlayer.png)
默认条件下组件截图。
|属性|描述|
|**File Path Type**|路径类型。选项：
* Absolute：绝对路径。
* PersistentDataPath：Unity 沙盒路径 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|**File Path**|文件路径。|
|**Advanced Options**|高级选项。大多数情况下无需修改。|
|*Camera Candidate*|[Camera](https://docs.unity3d.com/ScriptReference/Camera.html) 的备选，仅当未使用 Unity XR Origin 时有效，如未设置会使用 Camera.main。|

---

## FrameRecorder 组件参考
- 章节路径: `unity/simulation/comp-FrameRecorder.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/comp-FrameRecorder.html

# FrameRecorder 组件参考
>
[> 切换到 API
](../../../api/unity/easyar.FrameRecorder.html)
>
探索 FrameRecorder 组件窗口中的各项属性以自定义相机参数。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/comp-FrameRecorder.png)
默认条件下组件截图。
|属性|描述|
|**Auto Start**|session 启动后自动启动录制。|
|**Format**|录制的格式。选项：
* Auto：自动选择可用的格式。
* H264：H264。MacOS、iOS、Android上支持。
* Obsolete：原始 EIF 格式，在Windows上只支持该格式。|
|**Auto File Path**|自动生成文件路径。文件将被存储在 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|*Type*|Auto File Path 未选中时显示。
路径类型。选项：
* Absolute：绝对路径。
* PersistentDataPath：Unity 沙盒路径 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html)。|
|*Folder Path*|Auto File Path 未选中时显示。
文件夹路径。|
|*File Name*|Auto File Path 未选中时显示。
文件名（不含扩展名）。|
|**Events**|可注册事件。|
|*OnReady*|可以开始录制的事件。|
|*OnRecording*|录制启动的事件。|
|*OnFinish*|录制结束的事件。|

---

## 在 Unity 中使用 EIF 文件模拟运行
- 章节路径: `unity/simulation/playback.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/playback.html

# 在 Unity 中使用 EIF 文件模拟运行
本文介绍了如何在 Unity 中使用 EIF 文件进行模拟运行，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
## 开始之前
模拟运行使用 EIF 文件作为输入，因此在开始之前需要先录制 EIF 文件：
* 参考 [录制 EIF 文件](recording.html) 录制 EIF 文件
另外还需要了解：
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 通过 [访问 session 中的 AR 功能组件](../fundamentals/session-components.html) 了解如何访问录制组件
## 启用 session 的 frame player
[ARSession.AssembleOptions](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_AssembleOptions) 提供了多种方式来配置 session 组件的组合方式，其中一种方式是设置 [AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource) 为 [FramePlayer](../../../api/unity/easyar.AssembleOptions.FrameSourceSelection.html#u_easyar_AssembleOptions_FrameSourceSelection_FramePlayer) 来启用 frame player 组件，从而可用使用 EIF 文件进行模拟运行。
例如：
```
Session.AssembleOptions.FrameSource = AssembleOptions.FrameSourceSelection.FramePlayer;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Assemble Options` 中对应的选项：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-assemble.png)
这样 session 启动时就会启用 frame player 组件，而不会选择其它 frame source 组件。
使用 frame player 播放 EIF 文件的效果如下面这个视频所示：
>
> 这段视频展示了使用 frame player 在电脑上运动稠密空间建图的效果。视频左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
在播放 EIF 文件的过程中，session 中的各个 AR 功能组件都可以正常工作，场景中的内容和交互逻辑也可以正常工作，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
> **提示**
在电脑上使用 frame player 播放 EIF 看到的效果，与录制 EIF 文件时手机上的效果是基本一致的。
> **重要事项**
场景内播放 EIF 时的运行效果与录制时使用的设备以及设备上当时选用的 frame source 有关，因此在录制 EIF 文件时，建议使用和目标设备相同或接近的设备进行录制，从而保证播放时的效果与目标设备上的效果一致。同时需要重点关注录制场景中的运动跟踪功能是否启用，如果录制时未启用运动跟踪功能，那么播放时也无法启用运动跟踪功能，依赖运动跟踪的 AR 功能（比如稠密空间地图、Mega等）也无法和设备上工作一致。
## 在 session 启动时播放
默认情况下，session 启动时 frame player 会自动开始播放 EIF 文件，但是在播放前需要指定 EIF 文件路径，可以通过 [FramePlayer.FilePathType](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_FilePathType) 和 [FramePlayer.FilePath](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_FilePath) 属性来设置。
例如：
```
var player = Session.GetComponent<FramePlayer>();
player.FilePathType = WritablePathType.Absolute;
player.FilePath = path;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Frame Player` 组件中的对应选项：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-file.png)
如果未指定文件，或文件路径无效，session 启动时 frame player 会启动失败，并输出错误日志：
>
> File not found:
>
## 手动播放
如果要手动控制播放时机，可以在 session 启动前将 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 设为 `false`，
```
Session.GetComponent<FramePlayer>().enabled = false;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中取消 `Frame Player` 组件的 `Enabled` 勾选：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/player-auto-disable.png)
在需要播放时，使用 [Play()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Play) 来启动播放。
例如：
```
if (Session.Assembly.FrameSource is FramePlayer player)
{
player.Play();
}
```
每次调用 [Play()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Play) 都会停止前一次播放后（如果之前播放过）从头开始播放。
> **小心**
播放新数据时，场景中原本的数据不会被清空。AR 组件的状态也不会被重置，它们会表现得像是摄像头数据突然从上一个数据停止的地方跳到新数据开始的地方一样。
虽然这对一部分功能没太大影响，但是对于依赖运动跟踪的功能（比如稠密空间地图、Mega等）来说，可能会导致功能状态异常，从而影响运行效果。因此建议在播放新数据前，重新启动 session 来重置所有 AR 组件的状态。
## 暂停和继续
使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 来控制播放的暂停和继续。
例如，设置 [FramePlayer](../../../api/unity/easyar.FramePlayer.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `false` 来暂停播放：
```
player.enabled = false;
```
播放暂停后，所有 AR 功能组件都会暂停工作。场景中的内容和交互逻辑不一定会停止，与内容本身有关。继续播放后，AR 功能组件会从暂停的位置继续工作。
## 停止播放
使用 [Stop()](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Stop) 来停止播放。
```
player.Stop();
```
播放停止后，所有 AR 功能组件都会停止工作。场景中的内容和交互逻辑不一定会停止，与内容本身有关。
## 跳转到指定时间点播放（seek）
使用 [Seek(double)](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Seek_System_Double_) 来跳转到指定时间点播放。
例如，跳转到 5 秒后播放：
```
player.Seek(player.Time + 5);
```
> **注意**
跳转之后可能不是从精确的时间点开始播放，具体取决于 EIF 文件的编码方式和关键帧间隔。
并不是所有 EIF 文件都支持跳转播放，可以使用 [IsSeekable](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_IsSeekable) 属性来检查当前播放的 EIF 文件是否支持跳转播放。
> **注意**
只有使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制且正常调用停止录制的 EIF 文件才支持跳转播放。如果 EIF 文件不支持跳转播放，调用 [Seek(double)](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Seek_System_Double_) 不会有任何效果。
## 播放速度控制
使用 [Speed](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Speed) 属性来控制播放速度。
例如，设置播放速度在原来的基础上增加 0.1 倍：
```
player.Speed += 0.1;
```
并不是所有 EIF 文件都支持播放速度控制，可以使用 [IsSpeedChangeable](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_IsSpeedChangeable) 属性来检查当前播放的 EIF 文件是否支持播放速度控制。
> **注意**
只有使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制且正常调用停止录制的 EIF 文件才支持播放速度控制。如果 EIF 文件不支持播放速度控制，设置 [Speed](../../../api/unity/easyar.FramePlayer.html#u_easyar_FramePlayer_Speed) 不会有任何效果。
## 相关主题
* 尝试 [使用 session 验证工具](tool.html)，这个工具包含了一个简单的 EIF 播放器，可以更加快速地使用 EIF 文件进行模拟运行

---

## 在 Unity 中录制 EIF 文件
- 章节路径: `unity/simulation/recording.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/recording.html

# 在 Unity 中录制 EIF 文件
本文介绍了如何在 Unity 中录制 EIF 文件，以便用于模拟运行。
## 开始之前
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
* 通过 [访问 session 中的 AR 功能组件](../fundamentals/session-components.html) 了解如何访问录制组件
## 启动录制
使用 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `true` 来启动录制，例如：
```
if (Session.State >= ARSession.SessionState.Ready && Session.Assembly.FrameRecorder.OnSome)
{
var frameRecorder = Session.Assembly.FrameRecorder.Value;
frameRecorder.enabled = true;
}
```
需要注意的是，这里需要先判断 [ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 是否存在。
> **注意**
[ARAssembly.FrameRecorder](../../../api/unity/easyar.ARAssembly.html#u_easyar_ARAssembly_FrameRecorder) 在少数情况下，比如使用 [FramePlayer](../../../api/unity/easyar.FramePlayer.html) 时是不能使用的。
[FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 默认值为 `false`，表示录制处于关闭状态，即使在编辑器中手动配置也是无效的。
录制在 session 运行过程中，[FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) >= [FrameRecorder.RecorderStatus.Ready](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Ready) 时才会开始。
如果 [FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) < [FrameRecorder.RecorderStatus.Ready](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Ready)，可以使用 [OnReady](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnReady) 事件来等待录制准备就绪。
```
Session.GetComponent<FrameRecorder>().OnReady.AddListener(() => {
// 可以开始录制
});
```
可以使用 [OnRecording](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnRecording) 事件来确认启动成功：
```
frameRecorder.OnRecording.AddListener((file) =>
{
Debug.Log($"Recording started: {file}");
});
```
启动失败没有事件触发，但可以通过检查 [FrameRecorder.Status](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Status) 是否为 [Error](../../../api/unity/easyar.FrameRecorder.RecorderStatus.html#u_easyar_FrameRecorder_RecorderStatus_Error) 来确认。
> **重要事项**
场景内播放 EIF 时的运行效果与录制时使用的设备以及设备上当时选用的 frame source 有关，因此在录制 EIF 文件时，建议使用和目标设备相同或接近的设备进行录制，从而保证播放时的效果与目标设备上的效果一致。同时需要重点关注录制场景中的运动跟踪功能是否启用，如果录制时未启用运动跟踪功能，那么播放时也无法启用运动跟踪功能，依赖运动跟踪的 AR 功能（比如稠密空间地图、Mega等）也无法和设备上工作一致。
## 停止录制
使用 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) = `false` 来停止录制，例如：
```
frameRecorder.enabled = false;
```
该操作会立即停止录制，并阻塞直至文件写入完成。
> **重要事项**
必须调用停止录制，否则录制文件写入不完整，会导致部分功能或整个文件无法使用：
* 录制格式为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 时，EIF 文件无法跳转到指定的时间点进行播放（seek），只能从头播放
* 录制格式为 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 时，EIF 文件无法使用
## 文件存储和导出
可以使用 [OnRecording](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_OnRecording) 事件来获取录制文件的完整真实路径：
```
frameRecorder.OnRecording.AddListener((file) =>
{
Debug.Log($"Recording started: {file}");
});
```
默认配置下，录制文件会存储在应用的持久化数据路径下，可以通过 [Application.persistentDataPath](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) 来访问该路径。
可以通过 [FrameRecorder.Configuration](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Configuration).[FilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_FilePath) 来修改录制文件的存储路径。该路径必须在录制启动前设置，且需要关闭 [AutoFilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_AutoFilePath) 后才能生效。需要提前创建好目录。
> **重要事项**
必须保证录制文件的存储目录存在且应用可写入，否则录制启动时会失败。
例如，下面的代码展示了如何将录制文件存储在自定义目录下，并根据 session 使用的 FrameSource 类型和当前时间生成文件名：
```
if (!Directory.Exists(SavePath))
{
Directory.CreateDirectory(SavePath);
}
var frameRecorder = Session.Assembly.FrameRecorder.Value;
frameRecorder.Configuration.AutoFilePath = false;
frameRecorder.Configuration.FilePath.Type = WritablePathType.Absolute;
frameRecorder.Configuration.FilePath.FolderPath = SavePath;
frameRecorder.Configuration.FilePath.FileName = ARSessionFactory.DefaultName(Session.Assembly.FrameSource.GetType()).Replace(" ", "") + DateTime.Now.ToString("\_yyyy-MM-dd\_HH-mm-ss.fff");
frameRecorder.enabled = true;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中取消 Frame Recorder 的 `Auto File Path` 勾选之后配置：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-filepath.png)
> **提示**
通过 [FrameRecorder.RecordingConfiguration.FilePath](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_FilePath) 可以修改文件的存储目录和文件名（不含扩展名），文件扩展名会根据录制格式自动添加。
* 录制格式为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 时，文件扩展名为 `.mkveif`
* 录制格式为 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 时，文件扩展名为 `.eif`
如果文件存储在应用的持久化数据路径或其他应用私有路径下，可以通过以下方式将文件导出到电脑上：
* Android 平台可以通过 USB 连接电脑后，使用 `adb pull` 或其他方式将文件导出到电脑上，文件通常在 `/sdcarad/Android/data/<app package name>/files` 下面。
* iOS 平台可以通过 Xcode 的 Devices 窗口将文件导出到电脑上，或者通过 iTunes 或 Finder 文件共享访问应用的私有目录。
* 通过代码将文件存储到公共目录下，比如 Android 的下载目录或 iOS 的相册等。
> **注意**
对于 iOS 应用，如果希望通过 iTunes 或 Finder 文件共享访问应用的私有目录，在打包前需要在 XCode 项目的 `Info.plist` 中添加 `UIFileSharingEnabled` 键，并将值设置为 `YES`：
![alt text](https://doc-asset.easyar.com/develop/unity/fundamentals/media/ios-plist-uifilesharingenabled.png)
添加之后显示的文字与添加的字符串不同，这是正常的。
## 更换录制格式
通过 [FrameRecorder.Configuration](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_Configuration).[Format](../../../api/unity/easyar.FrameRecorder.RecordingConfiguration.html#u_easyar_FrameRecorder_RecordingConfiguration_Format) 改变录制格式，必须在录制启动前设置。
例如，下面的代码展示了如何将录制格式强制设置为 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264)：
```
frameRecorder.Configuration.Format = FrameRecorder.InternalFormat.H264;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中修改 `Format`：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-format.png)
> **注意**
[H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 在部分设备（比如 Windows）上无法使用，一般推荐使用 [Auto](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Auto)，这样会根据设备自动选择合适的格式。
> **注意**
在 XREAL 上，使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制数据无法用来模拟运行，用于且只用于反馈问题。
* 模拟运行时，应使用 [H264](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_H264) 格式录制数据。
* 反馈问题时，应使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制数据。
可以使用 [RecordingFormat](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_RecordingFormat) 来查看当前录制格式。
## 在 session 启动时自动录制
在 session 启动前设置 [AutoStart](../../../api/unity/easyar.FrameRecorder.html#u_easyar_FrameRecorder_AutoStart) 为 `true`，可以在 session 启动时启动录制，例如：
```
frameRecorder.AutoStart = true;
```
也可以在编辑器中，选中 `AR Session (EasyAR)`，在 `Inspector` 窗口中勾选 Frame Recorder 的 `Auto Start`：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/recorder-autostart.png)
> **注意**
编辑器上修改 [FrameRecorder](../../../api/unity/easyar.FrameRecorder.html).[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html) 是无效的。
## Mega 可用的数据
在使用 Mega 时，对 EIF 及相关文件内容有一些特殊要求，在老版本的 Unity 插件中未集成相关功能，那些版本录制的数据不能用于 Mega。
以下这些情况录制的数据可以用于 Mega：
* 使用 Unity 插件 4000 或更高版本录制的数据
* 使用 Mega Toolbox 录制的数据
* 如果数据是使用 [Obsolete](../../../api/unity/easyar.FrameRecorder.InternalFormat.html#u_easyar_FrameRecorder_InternalFormat_Obsolete) 格式录制的，比如文件 `x.eif`，需要在文件相同目录同时存在 `x.eif.json` 文件才能使用
以下这些情况录制的数据不能用于 Mega：
* 使用 Unity 插件 4.6 或更低版本录制的数据
* 使用原生 EasyAR Sense，且未添加与 Unity 插件中相同内容的数据
另外，虽然 Mega 可以不使用运动跟踪进行工作，但运行效果是不一样的。建议在录制 EIF 文件时启用运动跟踪功能，从而保证播放时的效果能符合大部分使用场景。
## 后续步骤
* 尝试 [使用 EIF 文件模拟运行](playback.html)
* 尝试 [使用 session 验证工具](tool.html)

---

## Unity AR 模拟运行
- 章节路径: `unity/simulation/simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/simulation.html

# Unity AR 模拟运行
Unity 的 AR 开发有时受限于设备能力差异，经常需要打包到手机上进行测试。在使用一些与真实环境有关的功能时（比如稀疏空间地图或 Mega），AR 功能需要真实的环境才能使用，这往往需要在特定的环境驻场开发和测试。为了提高开发效率，EasyAR 提供了模拟运行的功能，可以在 Unity 编辑器中模拟 AR 设备的工作效果。
基于 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html)，Unity 中可以使用这些功能：
* [录制 EIF 文件](recording.html)
在 Unity 中录制 EIF 文件，以便用于模拟运行。
* [使用 EIF 文件模拟运行](playback.html)
在 Unity 中使用 EIF 文件进行模拟运行，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
* [使用 session 验证工具](tool.html)
使用 session 验证工具，在编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
相关功能组件包括：
* [FrameRecorder 组件](comp-FrameRecorder.html)
该组件提供了录制 EIF 的功能。
* [FramePlayer 组件](comp-FramePlayer.html)
该组件提供了使用 EIF 文件进行模拟运行的功能。
* [DiagnosticsController 组件](../diagnostics/comp-DiagnosticsController.html)
该组件是诊断系统的核心控制器，提供了 session 验证工具。

---

## 使用 session 验证工具
- 章节路径: `unity/simulation/tool.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/unity/simulation/tool.html

# 使用 session 验证工具
本文介绍了如何使用 session 验证工具，在编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
## 开始之前
模拟运行使用 EIF 文件作为输入，因此在开始之前需要先录制 EIF 文件：
* 参考 [录制 EIF 文件](recording.html) 录制 EIF 文件
另外还需要了解：
* 了解 [录制 EIF 文件并用于模拟运行](../../simulation/simulation.html) 的基本概念
* 了解 [AR Session](../fundamentals/session.html) 的基本概念、组成和工作流程
## session 验证工具
session 验证工具用于帮助开发者在 Unity 编辑器中快速验证 session 工作流以及使用 EIF 文件进行模拟运行。
默认情况下可以在 `AR Session (EasyAR)` 物体的 `Inspector` 窗口中看到 session 验证工具，它是 [DiagnosticsController](../../../api/unity/easyar.DiagnosticsController.html) 编辑器的一部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool.png)
点击工具右上角 `↗` 按钮可以将工具弹出为独立窗口，方便查看和操作，在窗口关闭或按下 `↘` 按钮后，工具会重新在 `Inspector` 窗口中显示。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-window.png)
工具运行时的效果如下面这个视频所示：
>
> 这段视频展示了 session 验证工具的使用效果，录制于 Unity 的 play 模式。视频上半部分左边是
`> Hierarchy
`> 视图，中间是
`> Scene
`> 视图，右边是
`> Game
`> 视图，视频下半部分是 session 验证工具。
`> Game
`> 视图的内容与用户在现实世界中手机看到的内容是一样的。
>
> 工具左边偏上部分展示了 EIF 播放的进度条，可以看到它在随着播放进度不断变化。工具左边偏下部分展示了当前 session 的状态。工具右边展示了 session 的组件和可用中心模式。
>
> 在场景中，可以看到同时工作的 3 个 AR 功能：
>
>
> 运动跟踪：它是由 frame player 提供的，蓝色球体是 XR Origin，蓝色锥体代表用户位置。
>
> 稠密空间建图：可用看到随着视角的移动，半透明的网格模型在不断生成。
>
> 稀疏空间跟踪：视频中在被跟踪的是一棵圣诞树，叠加的虚拟物体是浅蓝色点云。
>
>
## 启动工具
点击工具顶部的 `▶` 按钮即可启动工具。按下这个按钮的效果与直接按下 [Unity 工具栏](https://docs.unity3d.com/Manual/Toolbar.html) 的 `▶` 按钮是一样的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-run.png)
如果工具已经启动，则按钮会变为 `■`，点击即可停止工具。
当工具以独立窗口展示时，`▶` 按钮右边的选择框可以选择工具使用的 session 物体，如果窗口被重置导致 session 丢失，可以从这里重新选择。
## 控制 EIF 播放
要使用工具的 EIF 播放功能，需要在运行前勾选工具的 `Frame Player` 选项，这时工具会托管 session 组装过程中 frame source 的选择，无论 [AssembleOptions.FrameSource](../../../api/unity/easyar.AssembleOptions.html#u_easyar_AssembleOptions_FrameSource) 设置为何种值，都会启用 frame player 组件。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-player-enable.png)
因此，运行时会有弹窗提示，说明当前 session 所使用的 frame source 已被工具托管：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-notice.png)
> **注意**
工具只会在 Unity 编辑器上托管组装过程中 frame source 的选择，在应用打包运行时该选项没有任何影响。
正常运行时，EIF 播放控制功能会显示在工具的上方图中框出的部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-player.png)
可以通过这些按钮控制 EIF 文件的播放：
* `▶`：播放，从暂停或停止状态恢复播放
* `▮▮`：暂停
* `■`：停止
* `▮◀`：跳到 5 秒之前（文件支持时）
* `◀◀`：降低播放速度（文件支持时）
* `▶▶`：提高播放速度（文件支持时）
* `▶▮`：跳到 5 秒之后（文件支持时）
* `▲`：打开文件
* 进度条：点击可以跳转播放位置（文件支持时）
可以在播放的同时调整优化场景中的内容和交互逻辑，从而可以在电脑上进行大部分的开发工作，并直观地看到效果。
> **注意**
播放新数据和跳转播放时，场景中原本的数据不会被清空。AR 组件的状态也不会被重置，它们会表现得像是摄像头数据突然从上一帧数据跳到新数据一样。
虽然这对一部分功能没太大影响，但是对于依赖运动跟踪的功能（比如稠密空间地图、Mega等）来说，可能会导致功能状态异常，从而影响运行效果。
## 控制 session 工作流
使用工具的 session 工作流控制功能，需要在运行前勾选工具的 `Session Workflow` 选项，该选项是默认勾选的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-enable.png)
正常运行时，session 工作流控制功能会显示在工具的播放控制下方图中框出的部分：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-workflow.png)
在整块区域的上方，展示了 [EasyARController.IsReady](../../../api/unity/easyar.EasyARController.html#u_easyar_EasyARController_IsReady) 和 [ARSession.State](../../../api/unity/easyar.ARSession.html#u_easyar_ARSession_State) 两个状态信息。
在整块区域的下方，提供了这些按钮来控制 session 的工作流：
* `Initialize`：初始化 session，可以选择使用 `Project Settings` 中配置的 license key 或手动输入 license key
* `Assemble`：组装但不启动 session
* `StartSession (Assembled)`：启动已组装的 session
* `StartSession`： 组装并启动 session
* `StopSession`：停止 session
* `StopSession (keep image)`：停止 session，但保留图像背景
* `Deinitialize`：反初始化 session
> **注意**
由于这些控制功能直接调用了 [ARSession](../../../api/unity/easyar.ARSession.html) 和 [EasyARController](../../../api/unity/easyar.EasyARController.html) 的相关方法，因此可以通过这些按钮来验证 session 状态变化对内容的影响，但同时需要注意如果在应用脚本中也调用了类似方法，应用的运行流程可能超出应用本身的预期。
## 控制 session 组件
使用工具的 session 组件控制功能，需要在运行前勾选工具的 `Session Workflow` 选项，该选项是默认勾选的。
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-enable.png)
正常运行时，session 组件控制会显示在工具的下方或右方图中框出的部分，具体位置视窗体宽度而变：
![alt text](https://doc-asset.easyar.com/develop/unity/simulation/media/tool-session-assembly.png)
这块区域显示的内容与具体的 session 有关，比如上图使用的 session 中包含了图像跟踪、稠密空间建图和稀疏空间跟踪三种功能组件，因此工具中显示了这三种功能的控制选框。
一般来说，这块区域会显示 session 中所有可用的 AR 功能组件，并提供这些组件的启用/禁用（[enabled](https://docs.unity3d.com/ScriptReference/Behaviour-enabled.html)）控制，包括：
* AR Session：控制 session 本身的启用/禁用
* Image Renderer：控制物理相机图像渲染的启用/禁用
* Camera：控制虚拟摄像机的启用/禁用
* Frame Source：控制 frame source 的启用/禁用，只有未启用 frame player 时才可控制，启用 frame player 时，功能控制由 EIF 播放控制部分替代
* Frame Filter：控制具体 AR 功能的启用/禁用
* Frame Recorder：控制录制 EIF 组件的启用/禁用，只有未启用 frame player 时才可见，启用 frame player 时，该组件不会被组装进 session
同时区域内还会显示 session 可用的中心模式和 [session 报告](../fundamentals/session-report.html)。
> **注意**
工具中展示的可用中心模式和 session 报告是编辑器下运行的结果，实际设备上运行时会不同。
## 相关主题
* 尝试 [使用 EIF 文件模拟运行](tool.html)，通过脚本控制 EIF 文件的播放
* 尝试在脚本中 [控制 session 执行](../fundamentals/session-ctrl.html)
* 尝试在脚本中 [访问 AR 功能组件](../fundamentals/session-components.html)
* 尝试在脚本中 [获取 session 的运行结果](../fundamentals/session-output.html)
* 尝试在脚本中 [初始化](../fundamentals/initialization.html)
* 尝试在脚本中 [获取 session 报告并判断设备支持](../fundamentals/session-assemble.html)

---

## 图像云识别 Web 开发者指南
- 章节路径: `web/cloud-recognition/guide.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/guide.html

# 图像云识别 Web 开发者指南
在 Web 端实现图像云识别的关键流程涵盖以下几个核心环节：首先通过浏览器调用摄像头捕获实时画面，随后将采集到的图像数据上传至云端服务器进行识别处理，最终接收并解析云端返回的结果，完成整个图像识别闭环。
## 开发步骤
不同浏览器对摄像头处理的实现存在差异，本文示例代码未涵盖所有浏览器兼容性问题，建议根据实际环境进行调整。
流程如下：
```
flowchart LR
A((初始化摄像头)) --> B[截取摄像头图片] --> C{调用云识别 API}
C ----> |未识别到目标| B
C ----> |识别到目标| D((业务逻辑处理))
```
### 前置设置
在 html 页面中添加以下元素：
```
<video id="video"></video>
<canvas id="canvas"></canvas>
```
在 js 代码中添加以下内容，获取必需的对象：
```
const videoEl = document.querySelector('#video');
const canvasEl = document.querySelector('#canvas');
const canvasCtx = canvasEl.getContext('2d');
```
* `videoEl` 为 `video` 元素，将摄像头视频流绑定到 `video` 上实时预览
* `canvasEl` 为 `canvas` 元素
* `canvasCtx` 为 `canvas` 的 context 2d 对象
### 初始化摄像头
```
const constraints = {
audio: false,
video: true,
};
navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
videoEl.srcObject = stream;
videoEl.play();
}).catch((err) => {
console.error(err);
alert('打开摄像头错误');
});
```
* 摄像头参数设置
* `constraints.video` 为 `true`，自动选择摄像头
* `constraints.video` 为 `{facingMode: {exact: 'user'}}`，使用前置摄像头
* `constraints.video` 为 `{facingMode: {exact: 'environment'}}`，使用后置摄像头
> **提示**
更多摄像头参数，参考 [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)。
### 截取摄像头图片
```
canvasCtx.drawImage(videoEl, 0, 0, videoEl.offsetWidth, videoEl.offsetWidth);
const image = canvasElement.toDataURL('image/jpeg', 0.8).split('base64,').pop();
```
### 调用云识别 API
```
// 云图库的 Client-end URL
const clientendUrl = '您云图库的 Client-end URL';
// 云图库的 Cloud Token
const token = '这里是云图库的 Cloud Token';
// 云图库的 CRS AppId
const appId = '这里是云图库的 CRS AppId';
// image 为上一步骤中截取的图片
const image = '/9j/4AAQSkZJRgABAQ......';
fetch(`${clientendUrl}/search`, {
method: 'POST',
body: `{ "image": "${image}", "appId": "${appId}", "notracking": true }`,
headers: {
'Content-Type': 'application/json;Charset=UTF-8',
'Authorization': token
}
}).then(res => res.json()).then(data => {
console.info(data);
// TODO: 识别结果处理
});
```
> **提示**
发送网络请求可以使用 `fetch`、`XMLHttpRequest` 或 `axois` 库等。
### 识别结果处理
云识别服务 API 接收到请求后，若成功识别到目标则返回识别结果；若未识别到目标，则返回未识别到状态码；若是其它错误，返回对应错误码及提示信息。
#### 未识别到目标
如果未识别到目标，`statusCode` 为 17， 返回结果如下：
```
{
"statusCode" : 17,
"result" : {
"message" : "No result: there is no matching."
},
"date" : "2026-01-05T05:49:02.651Z",
"timestamp" : 1767592142651
}
```
#### 识别到目标
如果识别到目标，`statusCode` 为 0，返回结果如下：
```
{
"statusCode" : 0,
"result" : {
"target" : {
"targetId" : "375a4c2e\*\*\*\*\*\*\*\*915ebc93c400",
"allowSimilar" : "0",
"detectableDistinctiveness" : 1,
"detectableFeatureCount" : 3,
"type" : "ImageTarget",
"trackableDistinctiveness" : 0,
"detectableFeatureDistribution" : 1,
"trackableFeatureCount" : 3,
"detectableRate" : 2,
"trackableFeatureDistribution" : 1,
"size" : "1",
"trackablePatchContrast" : 0,
"meta" : "eyJ2aWRlb1VybCI6Im\*\*\*\*\*\*\*\*pL0Vhc3lBUi1NZWdhLm1wNCJ9",
"grade" : "2",
"trackablePatchAmbiguity" : 3,
"name" : "Mega video",
"appKey" : "f7ff497\*\*\*\*\*\*\*\*f8068c",
"trackableRate" : 2,
"active" : "1",
"date" : "1746609056804",
"modified" : 1746609056804
}
},
"date" : "2026-01-05T05:50:36.484Z",
"timestamp" : 1767592236484
}
```
主要字段说明：
* targetId: 目标 id
* meta: base64 编码的附加信息，在上传识别图时添加的 3D 内容或视频 URL 等内容
* name: 目标名称
* active: "1" 为启用状态，"0" 为禁用状态
> **提示**
完整字段信息查看 [API 参考](../../../api/cloud/cloud-recognition/apis.html)
### 业务逻辑处理
您可以使用 `meta` 中的信息处理后续业务逻辑，如播放视频，渲染 3D 模型等。
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)

---

## 图像云识别 Web 开发快速入门
- 章节路径: `web/cloud-recognition/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/quickstart.html

# 图像云识别 Web 开发快速入门
EasyAR WebAR 基于 Web 技术实现 AR 功能，与原生 AR 应用相比，具有轻量化、部署快、传播性广的特点。它无需安装 APP，即可在 Android、iOS、Windows、Mac 等系统的主流浏览器中运行，真正实现跨平台。
## 开始之前
在开始之前确保已经做好以下准备工作：
1. 支持云识别的 [API Key](../../apikey-auth.html)
2. 运行中的[云识别库](../../cloud-recognition/management.html)
## 上传云识别图片
准备一张识别图片，并上传到云识别库，上传方法参考 [图库管理](../../cloud-recognition/management-adding.html)。
## 下载 sample
为方便开发者快速开发，我们提供了示例代码 sample。开发者可下载这些示例，快速体验 WebAR 功能。
[点击下载](https://dl.easyar.cn/samples/EasyAR-WebAR-Demo.zip)
## 配置 sample
sample 代码中已预留配置项，请根据实际环境进行配置。
* 编辑 `config/application.txt` 文件
* 将 `API Key`、 `API Secret` 与 `CRS AppId` 替换到配置文件中
![云识别配置](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-config-1.jpg)
* 编辑示例目录下的 `asset/js/app.js` 文件
* 将云识别的 `Client-end (Target Recognition) URL` 替换到 `app.js` 中
![云识别配置](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-config-2.jpg)
## 运行 sample
`EasyAR-WebAR\_\*` 文件为 http 与 token 生成服务，如启动成功，会显示监听的端口号，启动方式如下：
* Linux 系统：
```
./EasyAR-WebAR\_linux
```
* macOS 系统：
```
./EasyAR-WebAR\_darwin
```
* Windows 系统：
```
// 鼠标双击或在 cmd 中运行
EasyAR-WebAR\_windows.exe
```
## 体验 sample
在 PC 浏览器（需要摄像头）中输入 [http://127.0.0.1:3001/](http://127.0.0.1:3001/) ，建议使用火狐浏览器。
对准识别目标并查看 sample 的运行效果。
> **提示**
如果在手机上体验，需要配置支持 HTTPS 的域名。
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)

---

## 图像云识别 Web 示例
- 章节路径: `web/cloud-recognition/sample.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/cloud-recognition/sample.html

# 图像云识别 Web 示例
本篇将带您深入分析样例代码，帮助您理解并在此基础上开发自己的实例。
sample 下载与配置说明，请参考[快速入门](quickstart.html)。
## 识别目标设置
在云识别管理中，[上传一张识别图片](../../cloud-recognition/management-adding.html)。
* 识别图片名称：给识别目标一个名称，如 demo。
* 上传识别图片：选择并上传一张图片，本样例中使用的图片为：
`https://www.easyar.cn/assets/images/webar/xiaoxiongmao.png`。
* 宽度：识别图的宽度（cm）。识别图的高度将由系统根据您上传的图片自动计算。识别图的大小和虚拟内容的大小对应，本样例中未使用。
* Meta：附加信息，一般用于存储AR内容信息，本样例中使用的内容为：` {"modelUrl": "asset/model/trex\_v3.fbx", "scale": 0.02}`。
![crs sample](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-sample-1.jpg)
## 识别目标获取
在调用云识别 API，识别到目标后，会返回目标信息，结构如下：
```
{
"statusCode" : 0,
"result" : {
"target" : {
"targetId" : "375a4c2e\*\*\*\*\*\*\*\*915ebc93c400",
"meta" : "eyJtb2RlbFVybCI6ICJhc3NldC9tb2RlbC90cmV4X3YzLmZieCIsICJzY2FsZSI6IDAuMDJ9",
"name" : "demo",
"modified" : 1746609056804
}
},
"date" : "2026-01-05T05:50:36.484Z",
"timestamp" : 1767592236484
}
```
> **提示**
完整字段信息查看 [API 参考](../../../api/cloud/cloud-recognition/apis.html)
将 meta 使用 base64 解码，获取 meta 原始信息。
```
// data 为返回的数据
const meta = data.result.target.meta;
const modelInfo = JSON.parse(atob(meta));
```
## 主要代码说明
* src/webar.js
封装了几个基本的操作，如初始化摄像头、截取图片、调用云识别等功能。
* src/app.js
封装了界面的基本操作，如摄像头切换、界面交互、以及 WebAR 的初始化操作。
* TokenVideoExample/asset/js/app.js 与 TokenThreeJsExample/asset/js/app.js
云识别的配置，及识别成功后的业务处理。
## 预期效果
* 摄像头初始化后界面
![预期效果](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-s-1.jpg)
* 播放视频效果
![预期效果](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-s-2.jpg)
* 渲染模型效果
![预期效果](https://doc-asset.easyar.com/develop/web/cloud-recognition/media/crs-web-s-3.jpg)
## 代码深入理解
若您期望对云识别开发进行更为深入的学习，强烈建议您阅读 sample 源码。在此基础上，您可以尝试对源码进行修改与扩展。
> **提示**
以下内容讲解基于您已具备一定程度的 HTML 与 JavaScript 开发能力这一前提条件。若您尚未掌握这些基础技能，建议先系统学习相关知识，以便更好地理解后续内容。
我们将以 TokenThreeJsExample （渲染3D模型）为例，介绍 sample 中主要的源码说明。
### 业务处理
文件 `TokenThreeJsExample/asset/js/app.js` 主要方法说明。
* 初始化 App 对象
```
// 使用云识别的 Client-end URL 初始化 App 对象
const app = new App('https://af0c1ca3b........0601c74.cn1.crs.easyar.com:8443');
```
* 设置云识别相关信息
```
// 设置云识别库 AppId 与 token，与 app.useEasyAr() 只能选一个使用
app.setToken({
'crsAppId': 'f7ff4977......9984ef8068c', // 云别库的 CRS AppId
'token': 'pQWnZo1Qt4drnc........QXUQambomdPWEj9So' // APIKey + APISecret 生成的 Token
});
// 如果使用 EasyAR 提供的集成环境
// app.useEasyAr();
```
* 业务逻辑处理
```
app.callback = (msg) => {
// msg 为识别到目标的信息
// 解析其中的 meta 字段，处理业务逻辑
};
```
### UI 及初始化云识别
文件 `html/src/app.js`　主要方法说明。
* 初始化摄像头选择
```
constructor(url = '') {
}
```
* 使用自定义 Token 配置云别识
```
setToken(token) {
}
```
* 使用 EasyAR 集成环境配置云别识
```
useEasyAr() {
}
```
### 云识别处理
文件 `html/src/webar.js` 主要方法说明。
* 摄像头截图与云识别配置
```
constructor(interval, recognizeUrl, token, container) {
}
```
* 打开摄像头，检测设置横/竖屏视频流预览
```
openCamera(constraints) {
}
```
* 开启识别
```
startRecognize(callback) {
}
```
* 截图
```
captureVideo() {
}
```
* 发送截图到云识别服务识别
```
httpPost(data) {
}
```
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [云识别开快速入门](quickstart.html)
* [云识别开者指南](guide.html)
* [摄像头设置参数](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints)
* [three.js](https://threejs.org/)

---

## 在 Web 中使用 EasyAR
- 章节路径: `web/getting-started/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/web/getting-started/quickstart.html

# 在 Web 中使用 EasyAR
EasyAR WebAR 是以 Web 平台来集成 AR 技术，具有模式轻、部署快、传播性强等特点，可以轻松地运行在 Android，iOS，Windows，Mac 等系统的 Web 浏览器上，无需APP，真正实现跨平台。 EasyAR WebAR 当前支持 EasyAR 云识别服务，实现图像跟踪、图片云识别、3D渲染等功能。
> **注意**
目前 Web 平台仅支持图片云识别（CRS）功能，其他功能如物体识别、运动跟踪等不支持。
# 后续步骤
进一步了解如何快速在 Web 上部署 AR 内容，请参考。
* [web 快速入门](../cloud-recognition/quickstart.html)

---

## 图像云识别微信小程序开发者指南
- 章节路径: `wechat/cloud-recognition/guide.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/guide.html

# 图像云识别微信小程序开发者指南
本章主要介绍 EasyAR 云识别和微信小程序结合的常用功能以及实现方法。
## 功能和使用
微信小程序 XR-FRAME 是微信官方推出的 XR/3D 应用开发解决方案，采用混合渲染技术实现接近原生的性能表现，兼具视觉效果与开发便捷性，可快速构建 AR 应用。该框架支持图像跟踪、3D 模型加载、动画控制、视频播放及粒子特效等核心功能，开发模式以 WXML 模板化编程为主，仅需少量逻辑代码即可实现高质量视觉效果。
EasyAR 云识别（CRS）服务专注于海量图像库的以图搜图场景，通过云端算法实现高效目标识别，具有高性价比和低接入门槛的特点，开发者可快速集成并完成功能开发。
### 数据流
```
flowchart TB
B[API 或者 EasyAR Web] --> A[云识别 CRS] <--> D[设备端 微信小程序]
C[虚拟内容] <--> D[设备端 微信小程序]
```
XR-FRAME 和云识别两者结合以后，本地设备将不再受目标图数量的限制，可以解决应用对超大范围的需求。
### 实现流程
1. 云识别服务调用‌
* 通过 EasyAR 云识别（CRS）API 发起图像识别请求
* 处理识别结果（识别成功/失败，处理 Meta 等）
* 跟踪图配置‌
* 根据识别结果中的 trackingImage，动态设置 xr-ar-tracker
‌
* 虚拟资源加载‌
* 解析 Meta 数据中的资源标识符
* 使用 xr-asset 下载 3D 模型或视频等虚拟资产
* 将虚拟资产加入到场景中，并配置资源属性（如缩放比例、初始位置等）
‌
* AR 内容呈现‌
* 将虚拟资产与识别标记进行空间绑定
* 实现虚实融合的渲染效果
* 处理用户交互事件（如点击、拖拽等）
## 常用功能
云识别获取结果以后，微信小程序中常用的 AR 功能包括以下几种：
* 仅识别并展示识别结果
* 仅识别并展示识别目标关联的视频、动画、模型、脚本
* 识别 + 跟踪叠加视频、动画、模型、脚本
## 相关主题
* [微信小程序开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)

---

## 图像云识别微信小程序开发快速入门
- 章节路径: `wechat/cloud-recognition/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/quickstart.html

# 图像云识别微信小程序开发快速入门
本篇将带大家快速开发微信小程序上基于 EasyAR 图像云识别的 AR 应用，通过本文介绍，开发者可以掌握如何在微信小程序环境中集成 EasyAR 的云识别能力，并利用 XR-FRAME 框架构建交互式 AR 体验。
## 开发准备
1. [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。
2. 获取 “AppID(小程序ID)”，如果没有，请注册[微信公众平台账号](https://mp.weixin.qq.com/)或[申请测试账号](https://developers.weixin.qq.com/miniprogram/dev/devtools/sandbox.html)。
3. 微信开发者工具[下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。
4. 支持云识别的 [API Key](../../apikey-auth.html)。
5. 运行中的[云识别库](../../cloud-recognition/management.html)。
## 上传云识别图片
准备一张识别图片，并上传到云识别库，上传方法参考 [图库管理](../../cloud-recognition/management-adding.html)。
## 下载 Sample
在 [EasyAR 下载页面](https://www.easyar.cn/view/download.html)下载 “EasyAR CRS 微信小程序Sample”。
![crs-wx](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-dl-1.jpg)
## 配置 sample
* 将下载的 “EasyAR-miniprogram-WebAR-Demo-tracking.zip”，解压到你的目录。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-21.png)
* 导入微信开发者工具。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-22.jpg)
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-23.jpg)
* 在“详情”下的“本地设置”中勾选“不检验合法域名、web-view（业务域名）、TLS版本以及HTTPS证书”。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-24.jpg)
* “微信开发者工具”中的预览效果。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-25.jpg)
* sample 代码中已预留配置项，请根据实际环境进行配置。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-26.jpg)
## 效果预览
* 在“微信开发者工具”上点击“预览”。
* 选择“启动手机端自动预览”。
* 点击“编译并预览”
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-27.jpg)
> **提示**
不要使用“真机调试”。
* 在手机上的运行效果。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-1.jpg)
* 如果你未将域名添加到合法请求列表中，请开启“开发调试”。打开方法如下：
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-2.jpg)
* 如果是首次运行，点击“允许”授权摄像头访问权限。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-3.jpg)
* 点击预览页面中的“云识别功能”。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-5.jpg)
* 将手机摄像头对准您上传的识别图片，点击“点击识别”，如果识别到目标，则会弹出识别目标的名称。
![image](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-4.jpg)
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)

---

## 图像云识别微信小程序示例说明
- 章节路径: `wechat/cloud-recognition/sample.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/cloud-recognition/sample.html

# 图像云识别微信小程序示例说明
本篇将带您深入分析样例代码，帮助您理解并在此基础上开发自己的实例。
sample 下载与配置说明，请参考[快速入门](quickstart.html)。
## 识别目标设置
在云识别管理中，[上传一张识别图片](../../cloud-recognition/management-adding.html)。
* 识别图片名称：给识别目标一个名称，如“熊猫”。
* 上传识别图片：选择并上传一张图片，本样例中使用的图片为：
![sample](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/model.jpg)
* 宽度：识别图的宽度（cm）。识别图的高度将由系统根据您上传的图片自动计算。识别图的大小和虚拟内容的大小对应，本样例中未使用。
* Meta：附加信息，一般用于存储 AR 内容信息，本样例中使用的内容：
```
{"modelUrl": "https://sightp-assets.sightp.com/crs-mini/xiaoxiongmao.glb", "scale": 0.4}
```
![sample](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-sample-1.jpg)
## 识别目标获取
在调用云识别 API，识别到目标后，会返回目标信息，结构如下：
```
{
"statusCode" : 0,
"result" : {
"target" : {
"targetId" : "375a4c2e\*\*\*\*\*\*\*\*915ebc93c400",
"meta" : "eyJtb2RlbFVybCI6ICJhc3NldC9tb2RlbC90cmV4X3YzLmZieCIsICJzY2FsZSI6IDAuMDJ9",
"name" : "demo",
"trackingImage": "/9j/4AAQSkZJRgABAQ\*\*\*\*\*\*\*\*\*\*\*\*/9k=",
"modified" : 1746609056804
}
},
"date" : "2026-01-05T05:50:36.484Z",
"timestamp" : 1767592236484
}
```
> **提示**
完整字段信息查看 [API 参考](../../../api/cloud/cloud-recognition/apis.html)
将 meta 使用 base64 解码，获取 meta 原始信息。
```
// data 为返回的数据
const meta = data.result.target.meta;
const modelInfo = JSON.parse(atob(meta));
```
> **注意**
微信小程序中没有 `atob` 方法，需要自行实现。
实现方法在示例目录 `libs/atob.js` 文件中。
## 主要代码说明
* components/easyar-cloud/easyar-cloud.js
使用 `wx.createCameraContext` 打开摄像头、截取图片及访问云识别的等方法。
* components/easyar-ar/easyar-ar.js
使用 xr-frame 打开摄像头、截取图片、访问云识别及播放视频与渲染模板的等方法。
* components/libs/crs-client.js
Token 生成及云识别访问等方法。
> **警告**
不要在客户端（如 Web，微信小程序等）应用上直接使用 API Key 与 API Secret。
这里仅作演示使用，生产环境使用时请在服务端生成 Token。
## 代码深入理解
若您期望对云识别开发进行更为深入的学习，强烈建议您阅读 sample 源码。在此基础上，您可以尝试对源码进行修改与扩展。
> **提示**
以下内容讲解基于您已具备一定程度的 HTML 与 JavaScript 开发能力这一前提条件。若您尚未掌握这些基础技能，建议先系统学习相关知识，以便更好地理解后续内容。
微信小程序上使用的 XR/3D 引擎是 [XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)，如果您不熟悉，建议先参考一下文档。
我们将以渲染 3D 模型为例，介绍 sample 中主要的源码说明。
### UI 及场景处理
文件 `components\\easyar-ar\\easyar-ar.wxml`说明。
XR 场景及 Marker 设置。
```
<xr-scene ar-system="modes:Marker" id="xr-scene" bind:ready="handleReady" bind:ar-ready="handleARReady" bind:tick="handleTick">
<xr-node>
<xr-ar-tracker wx:if="{{markerImg != ''}}" mode="Marker" src="{{markerImg}}" id="arTracker"></xr-ar-tracker>
<xr-camera id="camera" node-id="camera" position="0.8 2.2 -5" clear-color="0.925 0.925 0.925 1" background="ar" is-ar-camera></xr-camera>
</xr-node>
<xr-shadow id="shadow-root"></xr-shadow>
<xr-node node-id="lights">
<xr-light type="ambient" color="1 1 1" intensity="2" />
<xr-light type="directional" rotation="180 0 0" color="1 1 1" intensity="1" />
</xr-node>
</xr-scene>
```
> **提示**
markerImg 为识别图片地址，云识别识别到目标时会返回。
### 业务处理
文件 `components\\easyar-ar\\easyar-ar.js` 主要代码说明。
```
handleTick() {
// 截图并发送到云识别服务
this.capture().then(base64 => this.crsClient.searchByBase64(base64.split('base64,').pop())).then(res => {
// 云识别返回的结果
console.info(res)
// 返回为 0 表示未识别到目标
if (res.statusCode != 0) {
return;
}
const target = res.result.target;
// 设置marker
this.loadTrackingImage(target.trackingImage.replace(/[\\r\\n]/g, ''));
// 从meta信息中检测是模型，还是视频
try {
const setting = JSON.parse(atob(target.meta));
if (setting.modelUrl) {
this.loadModel(target.targetId, setting);
} else if (setting.videoUrl) {
this.loadVideo(target.targetId, setting);
}
} catch (e) {
console.error(e);
}
}).catch(err => {
console.info(err)
});
},
capture() {
// 获取摄像头图片
const opt = { type: 'jpg', quality: this.properties.config.jpegQuality };
if (this.scene.share.captureToDataURLAsync) {
return this.scene.share.captureToDataURLAsync(opt);
}
return Promise.resolve(this.scene.share.captureToDataURL(opt));
},
```
> **提示**
完整代码请查看示例源文件。
### 云识别处理
文件 `components/libs/crs-client.js` 主要方法说明。
发送图片 base64 数据到云识别服务 API。
```
searchByBase64(img) {
const params = {
image: img,
notracking: 'false',
appId: this.config.crsAppId,
};
return this.queryToken().then(token => {
return new Promise((resolve, reject) => {
wx.request({
url: `${this.config.clientEndUrl}/search`,
method: 'POST',
data: params,
header: {
'Authorization': token,
'content-type': 'application/json'
},
success: res => resolve(res.data),
fail: err => reject(err),
});
});
});
}
```
## 预期效果
* 示例首页
![预期效果](https://doc-asset.easyar.com/develop/wechat/cloud-recognition/media/crs-wx-demo-xr-frame.jpg)
* 渲染模型效果
## 相关主题
* [APIKey 认证](../../apikey.html)
* [图像云识别简介](../../cloud-recognition/intro.html)
* [云识库管理](../../cloud-recognition/management.html)
* [云识别开快速入门](quickstart.html)
* [云识别开者指南](guide.html)
* [微信小程序开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework)
* [微信 XR-FRAME](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame)

---

## 微信小程序问题报告
- 章节路径: `wechat/diagnostics/report.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/diagnostics/report.html

# 微信小程序问题报告
为了能够快速、准确地定位您在开发或使用使用 EasyAR 提供的能力（Mega 或 CRS）的微信小程序时遇到的问题，在提交反馈前参考本指南提供必要的信息和数据以显著减少排查问题的往返沟通时间。
## 问题预检
在报告问题前，可以先尝试通过一些基本手段或阅读文档快速解决问题。
**使用 Mega 插件：**
* 确认使用 2.x 版本的小程序插件（1.x 版本的 Mega 小程序插件已不再维护）
* 阅读 [Mega 插件已知问题和限制](../mega/known-issues.html)确认是否为已知问题。
* 参考修改为 [Mega Sample](../mega/sample.html) 或 [CRS Sample](../cloud-recognition/sample.html) 中的实现方式，确认问题依然存在。
## 反馈问题时需要的数据
一份完整的问题报告通常需要包含以下数据，使 EasyAR 开发团队能够进行准确的分析。
### 运行环境数据
* **设备型号**：可以尝试通过 `wx.getDeviceInfo().model` 获取。
* **微信客户端平台**：通过 `wx.getDeviceInfo().system` 获取。
* **微信版本号**: 通过 `wx.getAppBaseInfo().version` 获取。
* **微信小程序客户端基础库版本**：通过 `wx.getAppBaseInfo().SDKVersion` 获取。
* **（若使用 Mega 插件）使用的 Mega 插件版本**：可以通过工程 `app.json` 文件中的 `plugins` 字段中的 `version` 获取。
### [Mega] AR Session dump 文件（至关重要）
能够复现问题的 AR Session dump 文件是分析微信小程序上定位、跟踪问题最重要的数据。
参考 [如何使用你的小程序录制 AR Session dump 文件](../../../mega/data-collection/wechat/wechat-dump.html)实现 dump 文件的记录与转发。
此外若定位问题可以稳定复现，您也可以通过 Mega toolbox 来录制这段数据并转发，参考[使用微信小程序 Mega Toolbox 记录与转发 session dump 数据](../../../mega/data-collection/wechat/toolbox-dump.html)。
### 屏幕录制（建议）
若使用 Mega 插件，请务必在录制屏幕的同时进行 AR Session dump。这能让我们将视频中的视觉现象与底层算法数据对齐。
### 运行日志
若在 vConsole 中出现了报错，您需要提交详细的错误信息，详细方法参考 [微信小程序上的日志分析](../../diagnostics/log-wechat.html)
> **重要事项**
如果使用 Mega 时遇到定位或跟踪相关的问题而不是程序异常，请务必提供当时的 **session dump 文件和录屏文件**。纯日志文件仅能提供侧面参考，dump 数据与录屏才是排查问题的**核心依据**。

---

## 在微信小程序中使用 AR
- 章节路径: `wechat/getting-started/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/getting-started/quickstart.html

# 在微信小程序中使用 AR
在微信小程序中开发 AR 应用，依赖微信提供的 VisionKit 和 xr-frame 组件。开发者可以实现图像跟踪、运动跟踪等功能。通过 EasyAR，在微信小程序上还支持 Mega 和图像云识别（CRS）功能。
为了实现小程序上的 AR 体验，需要多个组件共同工作：
* XR-Frame 负责小程序上相机控制和 3D 虚拟内容的渲染和叠加。
* VisionKit 负责提供图像跟踪、设备本地运动跟踪等。
* EasyAR CRS 提供图像云识别相对于已知平面目标的位置和姿态。
* Mega 提供设备相对于已知空间环境的六自由度位置和姿态。
## 后续步骤
为方便您快速开发微信小程序的应用，请参阅相关入门指南和示例代码。
* [图像云识别快速入门](../cloud-recognition/quickstart.html)
* [Mega 快速入门](../mega/quickstart.html)

---

## 使用 Unity 编辑器创建并上传标注
- 章节路径: `wechat/mega/content-annotation-creation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-annotation-creation.html

# 使用 Unity 编辑器创建并上传标注
这篇文章介绍了如何使用 Unity 编辑器上的 Mega Studio 创建并上传标注。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)
* 准备模型： 使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[XRFame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)，准备符合 xr-frame 要求的模型文件。
* 将模型的文件导入 Unity 。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
## 为什么需要标注
EasyAR Mega Annotation（EMA） 可用于同步跨平台的（坐标系定义不同）空间位置。
![Unity](https://doc-asset.easyar.com/develop/wechat/mega/media/content-transform-sync01.png)
Unity 环境下标注的本地坐标系： X 正方向朝后，Y 正方向朝上，Z 正方向朝右。
![xr-frame](https://doc-asset.easyar.com/develop/wechat/mega/media/content-transform-sync02.png)
xr-frame 环境下标注的本地坐标系： X 正方向朝后，Y 正方向朝上，Z 正方向朝左。
上述方向差异源于 Unity 与 xr-frame 采用的坐标系定义（左手/右手系）不同。
使用 EMA 同步空间位置有以下显著优势：
1. 简化开发流程： 自动处理跨平台坐标转换，规避了手动计算导致的繁琐逻辑及易错性。
2. 提升调试效率： 能够直接在 [MegaToolbox](../../../mega/reference/toolbox-wechat/intro.html) 上加载，便于快速进行真机测试与数据验证。
## 操作步骤
1. **创建标注工具**
在 Unity 的 **Hierarchy** 面板中点击右键，依次选择： **EasyAR Mega** > **Tool** > **Annotation Tool（Edit Mode）**。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation01.png)
创建完成后，场景中生成 EasyAR.Mega.Annotation 和 MegaBlocks 两个节点。
选中 EasyAR.Mega.Annotation 节点，在其 **Inspector** 面板中会出现用户名/邮箱及密码输入框。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation02.png)
2. **登录账号**
输入 EasyAR 账号，密码后点击登录，若成功 **Inspector** 面板中会出现 Studio 工具。
3. **选择 Mega 云定位库**
点击 Mega Cloud Service 右侧的图标。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation04.png)
选择要使用的库。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation05.png)
加载定位库及 Mega Blocks 信息成功后， Studio 工具面板如图所示。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation06.png)
4. **加载Block稠密模型**
点击 Block 名称右侧的 加载 即可动态加载该 Block 的稠密模型。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation07.png)
模型加载完成后出现在 Scene 标签页面中，注意当左下角出现图中标识时当前视野内的模型尚未加载完成，稍等一会儿待该标识消失表示加载已经完成。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation08.png)
5. **创建标注**
在场景中按住 Ctrl （Windows） / Command （Mac） 键，然后在需要标注的地方点击鼠标左键即可。
6. **使用模型**
将导入的模型拖到场景节点，作为标注的子节点。
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0** ， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
7. **[可选] 精确调整模型位置**
如果需要精确调整模型位置和朝向，可以参考[如何使用 Unity 编辑器使 3D 内容与实景精确对齐](content-realworld-alignment.html#wechat-mega-content-realworld-alignment-precise-adjustment)。
8. **新建标注数据包**
点击 **Inspector** 面板中的标注数据包右侧的图标。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation16.png)
在框中填入标注数据的名称，并点击右侧的勾。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation17.png)
创建成功后应如图所示，之后点击下方的确定。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation18.png)
点击上传图标进行上传。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation19.png)
上传成功后弹出提示。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation20.png)
9. **记录标注 ID**
您需要记录标注数据的名称或 ID 以在 xr-frame 上加载对应的标注数据。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation21.png)
在上传成功后，您在云定位库中也可以看到相应的信息。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation22.png)
此处也可以查看上传的标注数据名称和 ID。
![annotation](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 后续步骤
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* 尝试[在 Unity 编辑器上模拟运行](content-simulation.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)

---

## 如何在 xr-frame 运行时加载 AR 场景下的 3D 内容
- 章节路径: `wechat/mega/content-load.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-load.html

# 如何在 xr-frame 运行时加载 AR 场景下的 3D 内容
本文详细阐述了 xr-frame 资源加载与节点挂载的分离机制，通过脚本动态实现 3D 内容在 Block 节点下的灵活挂载，实现 AR。
## 官方资料
* [xr-frame 开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)：微信官方 XR 引擎文档。
* [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)：包含各类基础与进阶用法示例。
官方资料中已经有充分的内容说明如何在运行时加载 3D 内容，本文中仅简要说明一些 AR 场景下常用的内容和加载方式。
## 资源加载 vs 节点挂载
在 xr-frame 中，显示一个 3D 模型分为两个阶段：
1. 资源加载：指将模型文件（如 `.glb` ）从网络或本地下载并解析到内存中。此时模型已就绪，但在场景中不可见。
2. 节点挂载：指在场景树中创建一个节点，并将已加载的资源关联到该节点上。此时模型才会正式出现在渲染画布中。
## 如何使用代码动态加载 3D 内容
1. 资源加载
通过 xr-frame 场景的资源管理系统调用 [loadAsset](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/AssetsSystem.html#loadAsset)手动加载资源。
参数中的 `type` 指资源类型，`assetId` 指加载后的资源 id，`src` 指资源的 url，一般是资源托管服务器的地址。
需要记录 `assetId` 用于后续的挂载和释放资源。
```
try {
await scene.assets.loadAsset({type: 'gltf', assetId: 'panda', src: 'url/EasyARPanda.glb'});
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
```
2. 节点挂载
使用 `element.addChild()` 将加载好的模型放在 ShadowRoot 下。
```
const root = scene.getElementById("shadow-root");
let panda = scene.createElement(xrFrameSystem.XRGLTF,
{
"model": "panda",
"anim-autoplay": ""
}
);
root.addChild(panda);
```
ShadowRoot 元素是 xr-frame 专门用来防止动态创建和移除节点的根节点，详见 [Shadow节点](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/shadow.html)。
使用插件对象提供的 [createXRNodeFromNodeAnnotation](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_createXRNodeFromNodeAnnotation_member) 方法能够根据 EMA 数据创建 Block 的子节点，确保 3D 内容显示在正确的空间位置。
```
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
let panda = scene.createElement(xrFrameSystem.XRGLTF,
{
"model": "panda",
"anim-autoplay": ""
}
);
xrNode.addChild(panda);
```
## 如何在 Block 下不使用标注直接挂载内容
> **警告**
使用此方法的前提是，您已验证该 LocalTransform 的数值在 xr-frame 坐标系下能够实现预期的渲染效果。
除此以外的情况请[使用 Unity 编辑器的标注功能](content-annotation-creation.html)实现。
通过 [getBlockById(id)](../../../api/wechat/easyar.BlockHolder.html#w_easyar_BlockHolder_getBlockById_member_1_) 获取场景树上的 block 节点对象，如果不存在相应的 block 节点说明对这个 Block 的定位还未成功过（在第一次定位到该 Block 时节点会被自动创建）。可以用 [holdBlock(blockInfo, blockTransformInput)](../../../api/wechat/easyar.BlockHolder.html#w_easyar_BlockHolder_holdBlock_member_1_) 创建一个该 Block 的节点，也可以在定位回调中判断对该 Block 的定位成功再挂载内容。
> **提示**
在 Unity 编辑器的场景树中选择 **Block 节点** 记录它 **Inspector** 面板上显示的 **ID**
![Unity编辑器中的BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/content-load01.png)
也可以在云定位库页面中查到 **Block ID**
![定位库中的BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/content-load02.png)
```
const blockID = "aaaa1234-bbbb-cccc-dddd-eeeeee123456"
if (!blockHolder.getBlockById(blockParent.id)) {
// 没有存在的 Block 节点，创建一个
blockHolder.holdBlock({
id: blockID
})
}
let blockElement = blockHolder.getBlockById(blockParent.id).el;
```
将模型节点以挂载到指定的 Block 下，分别用 `position.setArray()`，`quaternion.set()` 和 `scale.setArray()` 把修改模型节点的 **LocalTransform** 。
```
export interface LocalTransform {
/\*\* @description 位置 \*/
position: xrfs.Vector3;
/\*\* @description 旋转 \*/
rotation: xrfs.Quaternion;
/\*\* @description Scale \*/
scale: xrfs.Vector3;
}
// 假设有一个已知的在 Block 下的 LocalTransform
const targetTransform: LocalTransform;
blockElement.addChild(modelNode);
let modelTransform = modelNode.getComponent(xrFrameSystem.Transform);
modelTransform.position.setArray([
targetTransform.position.x,
targetTransform.position.y,
targetTransform.position.z
]);
let annoRotation = new xrFrameSystem.Quaternion().setValue(
targetTransform.rotation.x,
targetTransform.rotation.y,
targetTransform.rotation.z,
targetTransform.rotation.w
);
modelTransform.quaternion.set(annoRotation);
modelTransform.scale.setArray([
targetTransform.scale.x,
targetTransform.scale.y,
targetTransform.scale.z
]);
```
## xr-frame 支持的资源类型
* Texture 纹理和图像
* CubeTexture 立方体纹理
* VideoTexture 视频纹理
* EnvData 环境
* GLTF 模型
* Keyframe 帧动画
* Atlas 图集
每种资源的加载方法详细见[微信官方文档](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/render)及 [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)
> **注意**
支持的 GLTF 格式及拓展参考 [xr-frame 官方 GLTF 使用说明](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)

---

## 如何使用 Unity 上的 Mega Studio 创建与实景精确对齐的 3D 内容
- 章节路径: `wechat/mega/content-realworld-alignment.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-realworld-alignment.html

# 如何使用 Unity 上的 Mega Studio 创建与实景精确对齐的 3D 内容
尽管 xr-frame 没有提供 3D 编辑器功能，您还是可以借助 Mega Studio 将虚拟物体准确地摆放在现实空间的某个位置，在 AR 体验中与现实空间精确对齐。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* 准备模型： 使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[XRFame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)，准备符合 xr-frame 要求的模型文件。
* 将模型的文件导入 Unity 。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
## 将 3D 内容作为标注的子节点
将导入的模型拖到场景节点，作为标注的子节点。
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0**， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![修改模型Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
## 精确调整模型位置
选择 **标注节点** 在场景中对着稠密模型调整模型的位置和旋转。
> **注意**
模型相对于标注的 Position 和 Rotation 必须始终全部为 **0** ，否则您无法在 xr-frame 上得到正确的渲染结果。
## [可选] 根据全景图精确调整模型位置
点击 **Inspector** 面板中的全景标记右侧的加载按钮，场景中出现全景标记。
![加载全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation13.png)
![显示全景标记](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation14.png)
点击任意一个全景标记，就可以在其位置进行全景下的摆放，您可以切换全景的位置以确认模型在不同视角下的位置都是准确的。
![全景编辑](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation15.png)
## 如果加载的 Block 模型不水平怎么办
在 **Hierarchy** 面板中选择 **Block Root** ，在 **Inspector** 面板中修改 **Rotation** 直到稠密模型的朝向在 Unity 编辑器中看起来正确。
> **重要事项**
Block Root 是在 3D 引擎场景节点树上所有 Block 节点的父节点。
Block Root 在世界坐标系下的 Transform **不会**影响 Block 的**本地坐标系**，也因此**不会影响标注和标注下模型的渲染结果**。它的 Transform 和最终的显示效果**无关**。
## 如果加载的 Block 模型有破碎，缺损的部分怎么办
在三维重建过程中，若受采集视角覆盖不全的影响，生成的密模型中可能会出现破碎或缺损的部分。
![破碎缺损](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment02.png)
面对不完整的模型，若破碎/缺损部分的 3D 内容对齐精度要并不高，可以通过点击**全景标记**对照**全景图**的方式来摆放 3D 内容。之后可以通过点击附近不同的**全景标记**位置来验证效果。
![通过全景图摆放](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment03.png)
得到摆放结果。
![摆放结果](https://doc-asset.easyar.com/develop/wechat/mega/media/content-realworld-alignment04.png)
若破碎/缺损部分的 3D 内容对齐精度要求非常高，则需要通过[补充更新](../../../mega/scene-update/incremental.html)或[无损全量更新](../../../mega/scene-update/full.html)进行地图的补充或更新。一般来说这样的区域意味着采图过程中没有覆盖，在这样的区域内部 Mega 定位效果会受到影响，仅在编辑器中对齐 3D 内容是不够的。
## 后续步骤
* 尝试[在 Unity 编辑器中模拟运行](content-simulation.html)
* [完整运行示例工程](fullstart.html)
## 相关主题
**微信小程序 Mega 插件**：
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
**Mega Studio**：
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)

---

## 如何使用 Unity 上的 Mega Studio 摆放 3D 内容
- 章节路径: `wechat/mega/content-simple.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-simple.html

# 如何使用 Unity 上的 Mega Studio 摆放 3D 内容
这篇文档将带您快速学习如何在 Unity 编辑器上使用标注工具进行模型摆放，为后续在 xr-frame 上的渲染做准备。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)
## 准备 GLTF 模型并拖入 Unity Assets
可以使用示例工程中使用的模型（一个憨态可掬的熊猫），或者使用 xr-frame 官方 Demo 中使用的[小机器人模型](https://dldir1.qq.com/weixin/miniprogram/RobotExpressive_aa2603d917384b68bb4a086f32dabe83.glb)，或者参考[xr-frame 可加载的 GLTF 格式及支持的拓展](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/gltf/specification.html)准备自己的模型并上传到资源托管服务器。
> **提示**
Mega 插件中已经添加了对 [com.unity.cloud.gltfast](https://docs.unity3d.com/Packages/com.unity.cloud.gltfast@6.8/manual/index.html) 的依赖，因此您可以直接将模型文件拖入 Unity Assets。
![模型拖入 Unity Assets](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple01.png)
## 选择Mega云定位库
点击 **Mega Cloud Service** 右侧的图标。
![Studio工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation04.png)
选择要使用的库。
![选择库](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation05.png)
加载定位库及 Mega Blocks 信息成功后， Studio 工具面板如图所示。
![加载后的Studio工具](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation06.png)
## 加载Block稠密模型
点击 Block 名称右侧的 加载 即可动态加载该 Block 的稠密模型。
![点击Block加载](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation07.png)
## 创建标注
在场景中按住 Ctrl （Windows） / Command （Mac） 键，然后在需要标注的地面上点击鼠标左键即可。
![创建标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple06.png)
## 将 3D 内容作为标注的子节点
将导入的模型拖到场景节点，作为标注的子节点。
![拖入模型](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple07.png)
将模型 **Inspector** 面板中的 Position 和 Rotation 全部改为 **0**， Scale 可以根据需要自行调整。
> **注意**
EMA 承载了所有的坐标转换逻辑。将模型 Position 和 Rotation 设为 0，是为了让模型的几何中心与标注点完全重合。所有的位移和旋转调整，都应该通过操作其父节点（标注节点）来完成。
![修改模型Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation11.png)
## [可选]调整模型位置
选择 **标注节点** 在场景中对着稠密模型调整模型的位置和旋转。
> **注意**
模型相对于标注的 Position 和 Rotation 必须始终全部为 **0** ，否则您无法在 xr-frame 上得到正确的渲染结果。
![修改标注节点Transform](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple09.png)
## 新建标注数据包
点击 **Inspector** 面板中的标注数据包右侧的图标。
![添加标注数据](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation16.png)
在框中填入标注数据的名称，并点击右侧的勾。
![填入标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation17.png)
创建成功后应如图所示，之后点击下方的确定。
![确定创建标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation18.png)
点击上传图标进行上传。
![上传标注](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple13.png)
上传成功后弹出提示。
![成功提示](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation20.png)
## 确认标注数据
您需要记录标注数据的 **ID** 以在 xr-frame 上加载对应的标注数据。
![标注数据面板](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation21.png)
在上传成功后，您在云定位库中也可以看到相应的信息，这个页面中列表里的 ID 是 **标注数据包 ID**。
![云定位库中的标注信息](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple16.png)
此处也可以查看上传的标注数据名称和 ID，这个页面中列表里的 ID 是 **标注点 ID**。
![云定位库中的标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 后续步骤
* 使用上传的标注[完整运行示例工程](fullstart.html)
* 尝试[使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
## 相关主题
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)

---

## 在 Unity 编辑器中模拟运行
- 章节路径: `wechat/mega/content-simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-simulation.html

# 在 Unity 编辑器中模拟运行
这篇文档将指引您通过 Unity 编辑器模拟真实场景定位，帮助您在小程序上线前完成虚拟内容的静态对齐检查。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* [确认定位库已经可以使用](../../mega/localization-verify.html)。
* 使用 Mega Toolbox 工具[采集模拟运行数据](../../mega/input-recording.html)。
* [使用标注工具创建标注](content-annotation-creation.html)。
* [创建与实景对齐的 3D 内容](content-realworld-alignment.html)，比如：
![摆放完成的场景](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation08.png)
> **重要事项**
使用现场录制的 EIF 数据可以直观地验证虚拟内容的位置摆放是否准确。
但由于 xr-frame 和 Unity 平台环境不同，代码脚本逻辑和渲染结果无法在模拟运行中得到验证。
## 模拟运行
1. 创建一个 **Sense 许可证**
由于在 Unity 上模拟运行需要用到 EasyAR Sense ，需要准备一个 Sense 的许可证（它可以是试用的）。
在 EasyAR 开发中心中选择 [**Sense 授权管理**] > [**创建一个新的 Sense 许可证密钥**]：
![Sense许可证](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation01.png)
* 选择 EasyAR Sense 个人版。
* 在‘是否使用稀疏空间’选项中选择‘否’。
* 填写任意的应用名称，iOS Bundle ID 及 Android Package Name。
* 点击确定，此后在开发中心的 Sense 授权管理中会出现申请的许可证。
![Sense许可证信息](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation02.png)
* 在 EasyAR 开发中心中选择准备工作中申请的 Sense 许可证。
![Sense许可证列表](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation03.png)
点击复制：
![Sense许可证复制](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation04.png)
* 点击 Unity 编辑器上方菜单栏中的 **[EasyAR]** > **[Mega]** > **[Configuration]** 进入配置页面：
![Configuration](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation05.png)
* 点击左侧 **Sense** 进行配置，填入 **Sense 许可证**。
![Sense许可证填入](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation06.png)
* 启用验证工具，点击**运行**。
![摆放完成的场景](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation09.png)
在弹出窗口中点击 **OK**。
![弹出窗口](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation10.png)
* 点击**加载按钮**，加载 EIF 文件。
![加载按钮](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation11.png)
选择准备工作中保存的 EIF 文件（后缀名为 `.eif` 或 `.mkveif`）。
![选择EIF](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation12.png)
* **隐藏 Block Mesh**。
* 可以将 Block Mesh 全部设置为**隐藏**。
![隐藏Block Mesh](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation13.png)
* 可以在验证工具中将 **Block Mesh Alpha** 设置为 0，即透明。
![更改Alpha](https://doc-asset.easyar.com/develop/wechat/mega/media/simulation14.png)
将控制条拖至最左侧。
* **播放 EIF**
> **重要事项**
在 Unity 编辑器上播放 EIF 时使用的 SDK 以及输入帧数据与 xr-frame 小程序使用的均不同，因此这种方式：
✅ 可以用于直观地验证虚拟内容的位置摆放是否准确，验证云定位服务在该位置的定位准确度。
❌ 不能用于验证 xr-frame 小程序实机运行的最终效果。
工作原理与预期： 在 Unity 播放 EIF 数据时，EasyAR SDK 会调用录制的输入帧数据，向配置的定位服务发起**真实**的云端请求。
* **若定位成功且表现稳定**： 模型位置准确且无漂移，则可预期该场景在 xr-frame 小程序上也能达到较理想的效果。
* **若定位失败或表现异常**： 模型出现频繁跳动、偏移或无法定位，通常意味着 xr-frame 小程序实机运行时也会面临相似的问题。
## 相关主题
* [使用Session验证工具播放EIF文件](../../unity/simulation/tool.html)

---

## 如何安装 Unity 并使用 Mega Studio
- 章节路径: `wechat/mega/content-unity-setup.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/content-unity-setup.html

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
> **重要事项**
注意：请勿解压 `.tgz` 文件。 这些是 Unity 软件包，需通过 Unity Package Manager 直接导入。
```
.
└── EasyARSenseUnityPluginForMega\_\*\*.zip # 完整安装包
├── com.easyar.mega-\*\*.tgz # 包含标注工具及 Block 浏览工具
├── com.easyar.sense-\*\*.tgz # 包含 EasyAR Sense 核心库及 Unity 插件
├── readme.cn.txt # 中文自述文件
└── readme.en.txt # 英文自述文件
```
版本号说明： 文件名中的 \*\* 代表版本号，格式为：**Major.Minor.Patch + BuildNum.BuildHash** 。请以官方发布的最新版本为准。
## 在项目中导入 package （UPM 包）
请依次导入：
```
com.easyar.sense-\*\*.tgz
com.easyar.mega-\*\*.tgz
```
> **注意**
在导入之前，建议将 `.tgz` 文件先拷贝到您的 Unity 项目文件夹内（例如存放在 Packages 目录下）。
导入后请勿移动或删除这些 `.tgz` 源文件，否则 Unity 将无法加载对应的包。
点击 **Window** > **Package Management** > **Package Manager** ，在弹出的窗口左上角点击 **+** 号，选择 **Install package from tarball...**
![Install package](https://doc-asset.easyar.com/develop/wechat/mega/media/content-unity-setup10.png)
## 创建标注工具
在 **Hierarchy** 面板中空白处右键 **EasyAR Mega** > **Tool** > **Annotation Tool（Edit Mode）** 创建标注工具
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

---

## 完整运行微信小程序 Mega 插件示例工程
- 章节路径: `wechat/mega/fullstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/fullstart.html

# 完整运行微信小程序 Mega 插件示例工程
这篇文章将介绍如何完整运行微信小程序 Mega 插件的示例项目（包含标注的使用）。
## 开始之前
* 完成[快速运行示例工程](quickstart.html)。
* 完成[使用 Unity 上的 Mega Studio 摆放 3D 内容](content-simple.html)，获取**标注数据包 ID 和标注点 ID**。
**[Block 云定位]** > **[标注数据]** 在云定位库列表里的 ID 是 **标注数据包 ID**。
![云定位库中的标注信息](https://doc-asset.easyar.com/develop/wechat/mega/media/content-simple16.png)
点击右侧 **[查看]** 可以查看上传的标注数据名称和 ID，这个页面中列表里的 ID 是 **标注点 ID**。
![云定位库中的标注数据名称](https://doc-asset.easyar.com/develop/wechat/mega/media/content-annotation-creation23.png)
## 配置 Mega 标注数据包 ID
在 `miniprogram/components/sample-data/easyar-settings.ts` 中填入标注数据包 ID：
```
/\*\* 填 Mega 标注数据包 ID \*/
export const MegaAnnotationId: string = "";
```
## 配置标注点要展示的模型
在 `miniprogram/components/sample-data/annotation-metadata.ts` 中通过将 `key` 改成标注点 id 配置要替换的标注，如果要替换多个则用逗号隔开。
```
export const AnnotationMetaData: Record<string, any> = {
/\*\* 填标注点 ID \*/
"aaaaaaaa-bbbb-cccc-dddd-123456789012": {
assetId: "panda",
scale: "1 1 1"
},
"aaaaaaaa-bbbb-cccc-dddd-123456789013": {
assetId: "panda",
scale: "1 1 1"
}
};
```
>
> 关于如何记录和对应标注点 ID 可以参考
[> 确认标注数据
](content-simple.html#wechat-mega-content-simple-save-annotation-id)> 。
>
## 实机运行
1. 点击小程序开发工具上方栏的实机预览按钮，通过扫描二维码加载。
> **注意**
不能在开发工具上直接模拟运行带有 AR 功能的 xr-frame 组件。
![二维码加载](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart06.png)
2. 点击 **EasyAR Mega Samples** 进入示例项目的 AR 场景。
![Sample入口](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart08.png)
3. 屏幕中提示 `EasyAR Session is initializing` 表示微信平面检测正在初始化。
> **提示**
确保在光线充足的环境下测试，避开大面积纯色墙面或纯色地板。
对着地面或其他平面匀速左右摆动以加快这个过程。
![初始化](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart09.png)
4. 初始化完成后，将手机竖直使相机拍到正常的现实画面，当定位成功， debug 信息中出现 `Found` 字样，并且右下方的状态指示物变为绿色。
![定位](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart10.png)
5. 将在标注的位置加载并渲染 GLTF 模型或方块（取决于是否配置了 `assetId`）。
运行效果：
## 相关主题
* [Mega 简介](../../mega/intro.html)
* [获取和使用 APIKey](../../apikey-auth.html)
* [开始开发之前](../../mega/localization-verify.html)
* [使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)
* [使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)
* [示例说明](sample.html)

---

## 将 Mega 插件接入您的微信小程序
- 章节路径: `wechat/mega/integration.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/integration.html

# 将 Mega 插件接入您的微信小程序
本文档将带您完成 Mega 插件在 xr-frame 小程序环境下的接入。
## 开始之前
* 参考 [xr-frame 开发指南](https://developers.weixin.qq.com/miniprogram/dev/framework/xr-frame/)及 [xr-frame 官方样例](https://github.com/dtysky/xr-frame-demo)学习如何使用微信官方提供的 XR-3D 引擎，内容包括：
* 常规微信小程序页面中引入 xr-frame 组件的方式。
* xr-frame 组件与小程序传统组件的通信方式。
* 如何从场景中获取或创建一个元素并修改部分属性比如 `Transform`。
* 加载和释放资源，例如 GLTF 模型。
## 全局配置
在小程序根目录下的 `app.json` 全局配置文件中添加对 Mega 小程序插件的依赖，并将[依赖加载](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/lazyload.html)改为**按需注入**。
```
{
"lazyCodeLoading": "requiredComponents",
"plugins": {
"easyar-wechat-miniprogram": {
"version": "2.0.2", //使用最新的插件版本
"provider": "wx27fa3b52b5462e8f" // Mega 小程序插件固定 id
}
}
}
```
## 加载插件
您可以通过[插件接口](https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/using.html#js-接口)引入插件，直接使用插件的部分方法以验证插件是否已经被正确加载。
例如使用通过微信提供的 `requirePlugin(string path)` 接口拿到 [EasyARWechatMiniprogramPlugin](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html) 后，使用它的 [isMegaTrackerSupported](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_isMegaTrackerSupported_member) 方法判断设备是否支持。
```
//如果已经引入了 typings 文件
//const easyarPlugin: easyar.EasyARWechatMiniprogramPlugin = requirePlugin("easyar-wechat-miniprogram") as easyar.EasyARWechatMiniprogramPlugin;
const easyarPlugin = requirePlugin("easyar-wechat-miniprogram") as any;
//调用 isMegaTrackerSupported 判断当前设备是否支持，若不支持则弹窗提示
if (!easyarPlugin.isMegaTrackerSupported()) {
const message = `当前设备不支持 VK v1 和 v2，请参考微信官方文档：https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html`;
wx.showModal({
title: "设备不支持",
content: message,
showCancel: false,
});
console.error(message);
return;
}
```
>
> 这个例子中首先通过微信提供的
`> requirePlugin(string path)
`> 接口拿到了
`> easyarPlugin
`> 即插件暴露的接口对象，之后调用了其提供的
[> isMegaTrackerSupported
](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_isMegaTrackerSupported_member)> 方法判断当前运行环境下是否可用。若不可用则弹窗提示。
>
## 引入类型
建议使用 **Typescript** 进行开发。
样例工程中的路径：`/typings/types/easyar/lib.easyar.d.ts` 。
拷贝到工程相同目录，并在 `/typings/types/index.d.ts` 中以**三斜杠指令**引用：
```
/// <reference path="./easyar/lib.easyar.d.ts" />
```
当需要使用类型对象时，可以通过 [getMegaSystem](../../../api/wechat/easyar.EasyARWechatMiniprogramPlugin.html#w_easyar_EasyARWechatMiniprogramPlugin_getMegaSystem_member) 获取 EasyAR Mega 微信小程序插件的类型系统 [IMegaSystem](../../../api/wechat/easyar.IMegaSystem.html)。
```
const mega: easyar.IMegaSystem = easyarPlugin.getMegaSystem();
```
之后可以使用 [IMegaSystem](../../../api/wechat/easyar.IMegaSystem.html) 中暴露的类型进行类型比较，例如可以用 `state` 比较与 `mega.SessionState.Running` 是否相等判断 session 是否初始化成功：
```
const newState: easyar.SessionState = event.detail.value;
if (newState === mega.SessionState.Running) {
console.log("EasyAR Session initialized succeeded. Start running.");
}
```
## xr-frame 场景搭建（WXML）
在页面的 WXML 文件中，`xr-easyar-mega` 组件必须作为 `xr-scene` 的子节点，并正确绑定相机与追踪器的 `id` ，若不填写 `id` 则组件会使用在场景中第一个查找到的 `xr-camera` 和 `xr-ar-tracker` 组件。
```
<xr-scene id="xr-scene" ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
<xr-easyar-mega
id="easyar-mega"
camera-id="xrCamera"
ar-tracker-id="xrARTracker"
></xr-easyar-mega>
<xr-node>
<xr-ar-tracker id="xrARTracker" mode="Plane"></xr-ar-tracker>
<xr-camera id="xrCamera" node-id="xrCamera" clear-color="0.925 0.925 0.925 1" background="ar" is-ar-camera></xr-camera>
</xr-node>
<xr-shadow id="shadow-root" node-id="xrShadow"></xr-shadow>
</xr-scene>
```
> **小心**
`ar-system` 的 `planeMode` 必须设置为 `1`
## 注册 Mega 插件的事件回调
```
<xr-easyar-mega
id="easyar-mega"
camera-id="xrCamera"
ar-tracker-id="xrARTracker"
bind:sessionStateChange="onSessionStateChange"
bind:megaLocalizationResult="onMegaLocalizationResult"
bind:postSessionUpdate="onPostSessionUpdate"
></xr-easyar-mega>
```
在 WXML 中绑定 xr-frame Element 代理分发的事件，xr-frame 的事件分发机制请参考 [xr-frame 事件机制](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/core/event.html)
插件分发的事件有：
|事件名称|参数类型|说明|
|`SessionStateChange`|[SessionState](../../../api/wechat/easyar.SessionState.html)|Session 状态改变时立即触发。参数为 Session 新的状态，用于处理 Session 初始化开始与成功的回调。|
|`MegaLocalizationResult`|[MegaLocalizationResult](../../../api/wechat/easyar.MegaLocalizationResult.html)|收到 Mega 定位结果的渲染帧完成更新后触发。事件触发时，该渲染帧内所有受 EasyAR 控制的 Transform 变化已经完成。|
|`PostSessionUpdate`|无参数|Session 在该渲染帧完成更新后立即触发。此时该帧内所有受 EasyAR 控制的 Transform 变化已经完成。|
## AR Session
session 的创建，启动及销毁请见 [AR Session 流程控制](session-state.html)
通过 `sessionStateChange` 事件回调确认初始化是否成功。当状态变为 [Running](../../../api/wechat/easyar.SessionState.html#w_easyar_SessionState_Running_member) 时，即可认为 ARSession 已就绪。
在 WXML 中通过 `bind:sessionStateChange="onSessionStateChange"` 将 xr-frame 组件中的 `onSessionStateChange()` 函数注册为 `sessionStateChange` 事件的回调：
```
<xr-easyar-mega
bind:sessionStateChange="onSessionStateChange"
></xr-easyar-mega>
```
在 xr-frame 组件中的回调函数 `onSessionStateChange()` 中将 session 状态与 [SessionState](../../../api/wechat/easyar.SessionState.html) 的各个枚举进行比较可判断 session 当前状态。
```
onSessionStateChange(event) {
const newState: easyar.SessionState = event.detail.value;
console.log(`EasyAR Session state changed to: ${mega.SessionState[newState]}`);
let displayInfoStr: string = "";
if (newState === mega.SessionState.None) {
displayInfoStr = "EasyAR Session is inactive.";
} else if (newState === mega.SessionState.Initializing) {
displayInfoStr = "EasyAR Session is initializing...";
} else if (newState === mega.SessionState.Running) {
displayInfoStr = "EasyAR Session initialized succeeded. Start running.";
}
this.triggerEvent("sessionDisplayInfoEvent", displayInfoStr);
}
```
>
> 上述代码中，初始化完成后控制台应打印 "EasyAR Session initialized succeeded. Start running."
>
## 相关主题
* [完整运行示例工程](fullstart.html)
* [AR Session 流程控制](session-state.html)
* [示例工程说明](sample.html)

---

## 微信小程序 Mega 插件已知问题与限制
- 章节路径: `wechat/mega/known-issues.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/known-issues.html

# 微信小程序 Mega 插件已知问题与限制
这篇文章介绍了 Mega 小程序插件在使用过程中的已知问题和限制。
## 微信已知问题
当前微信 xr-frame 或 VisionKit 已确认的缺陷。发生时将导致 AR 功能失效，请在开发时留意相关触发场景。
### 微信平面检测异常
在特定情况下（如画面中出现大片白墙、相机长时间被遮挡等），微信提供的平面检测可能出现状态异常。在这种状态下，MegaTracker 无法正常工作。
处理方法参考 [平面 AR 追踪器异常处理](session-plane-detection-error.html)。
### Session 初始化时间较长
AR Session 需要等待微信平面检测初始化完成后才能完成初始化。在某些情况下，微信平面检测初始化时间较长。
AR Session 需要等待 xr-frame ARTracker 初始化完成的原因 请见 [MegaTracker 是如何在 xr-frame 上工作的](tracker.html)。
* **状态参考**：[微信小程序 AR 追踪器状态文档](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#获取追踪状态)。
* **监听示例**：
```
<xr-ar-tracker id="xrARTracker" mode="Plane" bind:ar-tracker-state="handleARTrackerState"></xr-ar-tracker>
```
```
handleARTrackerState({detail}) {
if (detail.value.state == xrFrameSystem.EARTrackerState.Detected) {
console.log('Plane is now detected by XR-Frame ARTracker.');
}
}
```
### 节点的 worldPosition 在当前帧不会被立刻更新
这个例子中 `trs.worldPosition` 未被及时更新：
```
public onTick(delta, data) {
const trs = this.el.getComponent(xrFrameSystem.Transform);
// 更新前该节点的 WorldPosition
console.log(`World Position before update: ${trs.worldPosition.x}, ${trs.worldPosition.y}, ${trs.worldPosition.z}`);
// 更新前该节点的 LocalPosition
console.log(`Local Position before update: ${trs.Position.x}, ${trs.Position.y}, ${trs.Position.z}`);
trs.position.x += 0.1;
trs.position.y += 0.1;
trs.position.z += 0.1;
// 该节点的 WorldPosition 未被更新
console.log(`World Position after update: ${trs.worldPosition.x}, ${trs.worldPosition.y}, ${trs.worldPosition.z}`);
// 该节点的 LocalPosition 被更新
console.log(`Local Position after update: ${trs.Position.x}, ${trs.Position.y}, ${trs.Position.z}`);
}
```
在开发中建议一直使用 LocalTransform ， 即 `el.getComponent(xrFrameSystem.Transform).position` 和 `el.getComponent(xrFrameSystem.Transform).rotation`。
### 屏幕方向切换异常
在微信小程序全局配置 `app.json` 中的 `window` 若填入 "auto"。
设备以横屏模式离开小程序后，若以竖屏模式重新进入，会出现 AR 画面异常的情况。
因此任何时候**不要**在 AR 小程序应用中使用 "auto"。
## 使用限制
功能运行的硬性要求。未满足时功能不可用，但可通过调整配置或环境予以避免。
### 机型限制
运行 Mega 小程序插件的设备需要至少支持 **微信 VisionKit V1 平面接口**。为获得理想效果，建议使用支持 **微信 VisionKit V2 平面接口** 的设备。
* **支持机型列表**：参考 [V2 平面 AR 接口支持列表](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html#附录)。
* **快速判断方法**：
1. 扫描微信小程序官方 Sample 二维码。
![微信小程序官方 Sample 二维码](https://doc-asset.easyar.com/develop/wechat/mega/media/prerequisites01.png)
2. 进入小程序后，导航至 **接口** > **VisionKit 视觉能力** > **水平面 AR-v2**，即可快速判断当前设备是否支持。
如果需要在不支持 VisionKit 的设备上使用 Mega 服务，请参考[导航场景最佳实践](../../mega/navigation.html) 使用支持几乎所有设备的**视＋ AR 导航产品**。
### PlaneMode 强制配置
受部分微信接口支持限制，**planeMode** 必须设置为 **1** 。
```
<xr-scene ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
```
### GPS 功能限制
暂不支持通过 GPS 对齐 Block。
暂不支持通过 GPS 摆放标注数据。
## 相关主题
* [MegaTracker的概念与工作流](tracker.html)
* [平面 AR 追踪器异常处理](session-plane-detection-error.html)
* [AR Session 屏幕旋转适配](session-device-orientation.html)

---

## 使用 Mega 插件实现遮挡
- 章节路径: `wechat/mega/occlusion.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/occlusion.html

# 使用 Mega 插件实现遮挡
遮挡 （Occlusion） 是提升 AR 虚实融合沉浸感的关键技术。本文将指导您如何在 xr-frame 环境下，通过 EasyAR 云定位与标注实现遮挡效果。
## 开始之前
* 能够[在 Unity 中使用 Mega Studio](content-unity-setup.html)。
* 能够[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
* 能够[创建与实景对齐的内容](content-realworld-alignment.html)。
## 遮挡的实现方式
* 离线建模：利用 Unity 编辑器在 Block 坐标系下，针对现实世界中的实体（如墙体、立柱、大型设备）创建 1:1 匹配的几何体；或通过对 Block 稠密模型进行裁剪与减面处理得到优化后的模型。
* 运行时对齐：在 xr-frame 运行时，通过云定位将 Block 坐标系与现实空间对齐，并加载对应的几何体。
* 材质替换：为这些几何体赋予特殊的遮挡材质。
* 视觉效果：当 GPU 渲染其他虚拟物体时，会因深度测试未通过而自动剔除被遮挡部分的像素，从而使虚拟物体遵循现实物理空间的遮挡逻辑。
## 如何布置简单几何体的遮挡
1. 对照稠密模型及全景图精确摆放方块标注。摆放后标注看起来就像是一面“墙”或者“柱子”。
![标注作为遮挡](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion02.png)
2. 修改标注的名称（如 `occlusion\_wall` ），记录 ID ，上传标注。
3. 在 xr-frame 小程序中利用其内置几何体加载作为遮挡的标注。
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRMesh,{})` 创建简单的几何体赋予 `easyar-occulusion` 材质。
> **注意**
`easyar-occulusion` 材质的加载，注册，反注册，卸载由 AR Session 控制。
```
````ts
handleEmaResult(ema: easyar.ema.v0\_5.Ema) {
let blockHolder: easyar.BlockHolder = session.blockHolder;
ema.blocks.forEach(emaBlock => {
const blockInfo: easyar.BlockInfo = {
id: emaBlock.id
};
// 若 Block 节点不存在，创建 Block 节点
blockHolder.holdBlock(blockInfo, easyarPlugin.toXRFrame(emaBlock.transform));
});
ema.annotations.forEach(annotation => {
if (annotation.type != mega.EmaV05AnnotationType.Node) {
return;
}
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
const emaName: string = nodeAnnotation.name;
const geometryStr: string = nodeAnnotation.geometry === "cube" ? "cube" : "sphere";
const assetInfo = AnnotationMetaData[nodeAnnotation.id as keyof typeof AnnotationMetaData];
let model: xrfs.Element;
if (assetInfo) {
// GLTF部分
} else {
model = scene.createElement(
xrFrameSystem.XRMesh,
{
// 使用插件注册好的遮挡材质
material: "easyar-occlusion",
// 使用 xr-frame 内置几何体，此处也可以直接使用 "cube"
geometry: geometryStr,
name: emaName,
"receive-shadow": "false",
"cast-shadow": "false"
// 注意不要修改 Scale
}
);
xrNode.addChild(model);
}
})
}
```
```
```
<video src="https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion03.mp4" style="width:480px; max-width:100%; height:auto;" muted playsinline controls></video>
> 有了遮挡后，这个熊猫就可以躲在墙后面跳舞了。
```
## 如何布置复杂几何体的遮挡
适用于异形设备、不规则建筑等需要高精度遮挡的场景。
您可以利用 Block 的稠密模型裁剪并减面得到您需要用于遮挡的白模。
1. 在 Unity 场景中点击 **Mega Block** 节点，在 **Inspector** 面板中记录 BlockID
![记录BlockID](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion08.png)
2. 在 Mega Studio 的 **Block** 中选择导出。
![选择导出](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion04.png)
3. 修改导出选项后导出。
![导出选项](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion05.png)
图中 1 为 LOD 层级，层级越低模型越简单，面数越少，若需要最高的精度选择2，若能接受降低精度以减少面数选择 1 或者 0。
图中 2 为导出贴图选项，由于我们只需要白模作为遮挡，不需要贴图。
4. 将导出后的模型在数字内容创建软件（例如 Blender）中进行裁剪，减面，保存为 `Glb`。
> **提示**
例子中使用的是 Blender 的 Decimate Modifier
![裁剪前](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion06.png)
裁剪并减面后：
![裁剪后](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion07.png)
5. 将遮挡用的 `Glb` 文件挂载到文件服务器，得到一个用于加载的 url。
6. 在 xr-frame 小程序中加载作为遮挡的 GLTF。
首先**加载**遮挡用的 GLTF 模型，然后使用 `scene.createElement(xrFrameSystem.XRGLTF,options)` 创建 GLTF 模型。
使用 `assets.getAsset("material", "easyar-occlusion")` 获取材质对象
使用 `model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {m.setData({ neverCull: true, material: occlusionMaterial });}` 修改 GLTF 模型的材质。
> **注意**
`easyar-occulusion` 材质的加载，注册，反注册，卸载由 AR Session 控制。
```
````ts
const sampleAssets = {
occlusion1: {
assetId: "occlusion1",
type: "gltf",
src: "url/occlusion1.glb",
options: {}
}
}
async loadAsset() {
if (!scene) {console.error("Empty scene"); return;}
try {
await scene.assets.loadAsset(sampleAssets.occlusion1);
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
},
addOcclusion() {
model = scene.createElement(
xrFrameSystem.XRGLTF,
{
"model": assetInfo.assetId,
"anim-autoplay": assetInfo.animation ? assetInfo.animation : "",
"scale": assetInfo.scale ? assetInfo.scale : "1 1 1",
name: "tree"
}
);
const blockID = "aaaa1234-bbbb-cccc-dddd-eeeeee123456" //此处应填写 Block ID
if (!blockHolder.getBlockById(blockParent.id)) {
// 若没有存在的 Block 节点，则创建一个
blockHolder.holdBlock({
id: blockID
})
}
// 获取 xr-frame 场景中的 Block 节点
let blockElement = blockHolder.getBlockById(blockParent.id).el;
// 将裁剪后的遮挡模型挂载到 Block 节点下，作为其子节点
blockElement.addChild(model);
/\*\*
\* 由于 GLTF 加载器的行为不同，为了保证模型在 xr-frame 上的朝向 与 Unity 的渲染结果完全一致
\* 有时需要对加载后的模型原地绕 Y 轴旋转 180 度
\*/
let modelTransform = model.getComponent(xrFrameSystem.Transform);
let currentRotation = modelTransform.quaternion.clone();
let targetRotation = currentRotation.multiply(new xrFrameSystem.Quaternion().setValue(0, 1, 0, 0));
modelTransform.quaternion.set(targetRotation);
//注意必须在修改 Transform 后修改材质
if (assetInfo.assetId == 'occlusion1') {
//获取 mega 插件提供的遮挡材质
let occlusionMaterial = scene.assets.getAsset("material", "easyar-occlusion");
//修改遮挡材质
model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {
m.setData({ neverCull: true, material: occlusionMaterial });
});
}
}
```
```
```
> [!NOTE]
> 这里使用 Mega Block 稠密模型进行裁剪后作为遮挡不需要使用标注同步空间位置，这是因为在数字内容创建软件（如 Blender） 中，可以在不改变坐标系定义的情况下对模型进行减免和裁剪。
>
> 若需要精确摆放自己制作的 GLTF 模型遮挡，请参考[如何摆放与空间对齐的遮挡模型](./sample.md#wechat-mega-sample-precise-occulusion-model)
最终实机运行效果见文章顶部视频。
```
## 遮挡的效果预期
xr-frame 小程序上遮挡的效果主要由以下几点影响：
* 定位跟踪本身的精度
* 模型摆放的准确程度
* 模型本身的精度（如果不是简单的几何体）
在定位漂移时出现数公分未对齐的情况是正常的。
遮挡用的模型面数太多容易影响性能，建议只在必要区域使用，并且尽量使用简单的几何体作为遮挡。
## 后续步骤
* [完整运行示例工程](fullstart.html)
* [示例工程说明](sample.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)

---

## 快速运行微信小程序 Mega 插件示例工程
- 章节路径: `wechat/mega/quickstart.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/quickstart.html

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

---

## EasyAR Mega 微信小程序插件发布日志
- 章节路径: `wechat/mega/release-notes.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/release-notes.html

# EasyAR Mega 微信小程序插件发布日志
本页面记录了 EasyAR Mega 微信小程序插件各个版本的发布日志。
> **重要事项**
**版本维护及升级建议**
* **2.0.0 及以上版本**：建议所有用户升级至 [最新版本 (2.0.2)](#mega-wechat-miniprogram-plugin-v202) 以获得最佳稳定性。
* **2.0.0 以下版本**：已完全重构并不再维护，请迁移至新版本。
## 快速导航
* [🚀 最新版本 (2.0.2)](#mega-wechat-miniprogram-plugin-v202)
* [📦 2.x 版本历史记录](#mega-wechat-miniprogram-plugin-v2-series)
* [📜 1.x 历史版本 (已不再维护)](#mega-wechat-miniprogram-plugin-v1-series)
## 2.0.2
>
> 发布日期：2025-11-19
>
* 修复了高网络延迟环境下，初始的定位跟踪效果不如预期的问题。
## 2.x 版本历史记录
2.x 是重构后稳定版本，提供了更加鲁棒的 AR 体验和更清晰的 API 调用方式。
### 2.0.1
* 优化了跟踪效果。
### 2.0.0
* **新增**：Sample, Toolbox 及 API 文档全面更新。
* **新增**：支持 APIToken。
* **新增**：全方位支持 TypeScript 类型推断。
* **新增**：支持使用旋转后的屏幕。
* **优化**：提供了更流畅的 AR 体验，不再会因获取图片卡顿。
* **优化**：使用微信原生提供的图片接口，更鲁棒。
* **优化**：AR 内容的跟踪更平滑，更稳定。
* **重构**：重写了 MegaSession 的工作流，大幅简化流程，支持纯代码创建。
* **重构**：解耦 Ema 标注数据的获取和场景中加载过程。
## 1.x 历史版本记录
1.x 是历史版本，已停止维护，以下内容仅供参考。
### 1.1.12
* 支持 v4DH CLS 库。
### 1.1.10
* 修复了上个版本中 `viewLocalizationInfo` 的版本兼容性问题。
### 1.1.9
* 增加了定位成功时的上报信息。
### 1.1.2 - 1.1.8
* 优化跟踪效果。
* 修复 Android 8.0.37 获取图像为纯黑问题。
* 修复无 Ema 时 Block 默认位置到世界原点。
### 1.1.1
* 修复不设置配置信息时运行错误。
### 1.1.0
* **新增**：导出数学方法。
* **新增**：调整为组件，使用 XML 标签方式引入插件。
* **修复**：修复重新设置 Mega 参数时的异常。
* **优化**：插件退出时增加资源释放，优化内部实现。
### 1.0.5
* 首次上线。

---

## 微信小程序 Mega 插件示例工程说明
- 章节路径: `wechat/mega/sample.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/sample.html

# 微信小程序 Mega 插件示例工程说明
这篇文章详细说明了示例工程展示的各功能使用方法，实现方式与注意事项。
## 开始之前
* 能够[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)，并记录标注名称与其 ID。
* 能够[使用 Unity 编辑器创建与实景对齐的 3D 内容](content-realworld-alignment.html)。
* 能够[完整运行示例工程](fullstart.html)。
## 如何在标注位置展示模型
1. **在 Unity 编辑器中精确摆放并上传标注，记录标注名称与其 ID**
![Unity标注位置](https://doc-asset.easyar.com/develop/wechat/mega/media/sample01.png)
2. **添加 GLTF 模型资源**
在 `miniprogram/components/sample-easyar-mega/index.ts` 中的 `sampleAssets` 中添加模型资源。
```
const sampleAssets = {
your\_model\_name: {
assetId: "your\_model\_asset\_id",
type: "gltf",
src: "url/model.glb",
options: {}
}
}
```
3. **加载添加的模型资源**
在 `miniprogram/components/sample-easyar-mega/index.ts` 中的 `loadAsset()` 函数中加载模型。
```
async loadAsset() {
try {
await scene.assets.loadAsset(sampleAssets.your\_model\_name);
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
}
```
4. **配置要替换的标注**
在 `miniprogram/components/sample-data/annotation-metadata.ts` 中配置要替换的标注，如果要替换多个则用逗号隔开。
```
export const AnnotationMetaData: Record<string, any> = {
"aaaaaaaa-bbbb-cccc-dddd-123456789012": {
assetId: "panda",
scale: "0.5 0.5 0.5"
},
"aaaaaaaa-bbbb-cccc-dddd-123456789013": {
assetId: "your\_model\_asset\_id",
scale: "1 1 1"
}
};
```
5. **替换标注加载模型**
在 EMA 加载的回调中使用 xr-frame 的“工厂方法” `scene.createElement(xrFrameSystem.XRGLTF, options)`创建模型节点。
* 参数：
* `xrFrameSystem.XRGLTF`：指定创建的元素类型为 GLTF 模型。
* `options`：初始化配置项，对应组件的属性。
* 代码中的关键属性：
* `"model"`：必填，指向已加载的资源 ID（asset-id）。
* `"anim-autoplay"`：选填，指定加载后自动播放的动画名称。
* `"scale"`: 选填， `assetInfo.scale` 或 "1 1 1"。
* `name`: 必填，标注名称。
> **小心**
注意区分属性 Key 的字符串和非字符串，完全按照示例中的方式填写。
将模型挂载到标注节点下 `xrNode.addChild(child)`。
为了保证 GLTF 模型在不同平台的加载器下看到一样的结果，需要对加载后的模型原地绕 Y 轴旋转 180 度。
```
if (assetInfo && assetInfo.assetId && assetInfo.assetId.trim().length > 0) {
model = scene.createElement(
xrFrameSystem.XRGLTF,
{
/\*\* 即前一步骤中的 assetId \*/
"model": assetInfo.assetId,
/\*\* 可以在此处指定播放的模型动画 \*/
"anim-autoplay": assetInfo.animation ? assetInfo.animation : "",
"scale": assetInfo.scale ? assetInfo.scale : "1 1 1",
name: emaName
}
);
xrNode.addChild(model);
/\*\*
\* 由于 GLTF 加载器的行为不同，为了保证模型在 xr-frame 上的朝向 与 Unity 的渲染结果完全一致
\* 需要对加载后的模型原地绕 Y 轴旋转 180 度
\*/
let modelTransform = model.getComponent(xrFrameSystem.Transform);
let currentRotation = modelTransform.quaternion.clone();
let targetRotation = currentRotation.multiply(new xrFrameSystem.Quaternion().setValue(0, 1, 0, 0));
modelTransform.quaternion.set(targetRotation);
}
```
* **实机运行**
* 实机运行的结果如下，可以与**第 1 步**中 Unity 编辑器上的位置进行比照：
* 打开左侧透明视频按钮，世界坐标系原点（坐标为 `(0, 0, 0)` 的位置）出现透明视频材质的方块。
> **注意**
原点位置可能是随机在空间中的任意位置。可以利用标注将遮挡模型放置到您希望的位置，详见[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
* 打开左侧遮挡按钮，世界坐标系原点（坐标为 `(0, 0, 0)` 的位置）出现熊猫模型和上下层叠的方块，中间的方块具有遮挡材质，另一侧有一个带有遮挡材质的静态熊猫模型。
> **注意**
原点位置可能是随机在空间中的任意位置。可以利用标注将遮挡模型放置到您希望的位置，详见[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
![模型和遮挡](https://doc-asset.easyar.com/develop/wechat/mega/media/quickstart11.png)
## 如何将透明视频在标注位置播放
1. **加载类型为 `video-texture` 的视频资源**。
```
async loadAsset() {
const videoTexture = {
assetId: "fireball",
type: "video-texture",
// 视频资源 URL
src: "url/video-resource.mp4",
options: {
autoPlay: true,
loop: true,
}
};
try {
// 加载 video-texture 类型资源
await scene.assets.loadAsset(videoTexture);
} catch (err) {
console.error(`Failed to load video texture: ${err.message}`);
}
}
```
2. **修改 EMA 加载回调**
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRMesh,options)` 创建简单的几何体赋予 `easyar-video-tsbs` 材质， 并修改 `uniform` 为 `u\_baseColorMap:video-{$assetId}`。
* 参数：
* `xrFrameSystem.XRMesh`：指定创建的元素类型为基础几何体。
* `options`：初始化配置项，对应组件的属性。
* 代码中的关键属性：
* `"geometry"`: "cube"：使用 xr-frame 内置的立方体几何数据。
* `"material"`: "easyar-video-tsbs"：指定一个预定义的材质（根据命名推测，这是一个支持视频纹理的特殊材质）。
* `"uniforms"`: "u\_baseColorMap:video-{$assetId}"：
> **小心**
注意区分属性 Key 的字符串和非字符串，完全按照示例中的方式填写。
这是材质参数的动态绑定。
它将名为 `video-{$assetId}` 的视频资源（纹理）映射到了材质的基色图上。
效果：这会产生一个表面正在播放视频的立方体。
```
model = scene.createElement(xrFrameSystem.XRMesh, {
geometry: "cube",
material: "easyar-video-tsbs",
uniforms: "u\_baseColorMap:video-fireball",
});
xrNode.addChild(model);
```
> **注意**
在使用 `video-texture` 时，若控制台出现 `wx.createVideoDecoder with type: 'wemedia' is deprecated` 警告，请忽略。
经与微信官方团队确认，该警告不影响使用。
* **实机运行**
## 如何摆放与空间对齐的遮挡模型
1. **精确摆放用于遮挡的模型并上传标注。**
![精确对齐](https://doc-asset.easyar.com/develop/wechat/mega/media/occlusion10.png)
2. **在 xr-frame 小程序中加载作为遮挡的 GLTF。**
通过 `scene.assets.loadAsset()` 加载模型资源（需要手动卸载）。
```
const sampleAssets = {
occlusion1: {
assetId: "occlusion1",
type: "gltf",
src: "url/occlusion1.glb",
options: {}
}
}
async loadAsset() {
if (!scene) {console.error("Empty scene"); return;}
try {
await scene.assets.loadAsset(sampleAssets.occlusion1);
} catch (err) {
console.error(`Failed to load assets: ${err.message}`);
}
}
```
3. **运行时在 EMA 加载回调中加载模型并赋予遮挡材质**
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRGLTF,options)` 创建模型节点。
* 参数：
* `xrFrameSystem.XRGLTF`：指定创建的元素类型为 GLTF 模型。
* `options`：初始化配置项，对应组件的属性。
* 代码中的关键属性：
* `"model"`：必填，指向已加载的资源 ID（asset-id）。
* `"scale"`: 选填 `assetInfo.scale` 或 "1 1 1"。
* `name`: 必填，标注名称。
> **小心**
注意区分属性 Key 的字符串和非字符串，完全按照示例中的方式填写。
将模型挂载到标注节点下 `xrNode.addChild(child)`。
为了保证 GLTF 模型在不同平台的加载器下看到一样的结果，需要对加载后的模型原地绕 Y 轴旋转 180 度。
最终使用 `model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {m.setData({ neverCull: true, material: occlusionMaterial });}` 修改 GLTF 模型的材质。
> **注意**
`easyar-occulusion` 材质的加载，注册，反注册，卸载由 AR Session 控制。
使用模型在标注位置作为遮挡：
```
if (...) {
model = scene.createElement(
xrFrameSystem.XRGLTF,
{
"model": assetInfo.assetId,
"scale": assetInfo.scale ? assetInfo.scale : "1 1 1",
name: emaName
}
);
/\*\*
\* 由于 GLTF 加载器的行为不同，为了保证模型在 xr-frame 上的朝向 与 Unity 的渲染结果完全一致
\* 有时需要对加载后的模型原地绕 Y 轴旋转 180 度
\*/
let modelTransform = model.getComponent(xrFrameSystem.Transform);
let currentRotation = modelTransform.quaternion.clone();
let targetRotation = currentRotation.multiply(new xrFrameSystem.Quaternion().setValue(0, 1, 0, 0));
modelTransform.quaternion.set(targetRotation);
//注意必须在修改 Transform 后修改材质
if (assetInfo.assetId == 'occlusion1') {
//获取 mega 插件提供的遮挡材质
let occlusionMaterial = scene.assets.getAsset("material", "easyar-occlusion");
//修改遮挡材质
model.getComponent(xrFrameSystem.GLTF).meshes.forEach((m: any) => {
m.setData({ neverCull: true, material: occlusionMaterial });
});
}
}
```
* **实机运行**
可与 Unity 编辑器上模拟运行的结果进行比照。
## 相关主题
* [环境遮挡](occlusion.html)
* [透明视频](transparent-video.html)
* [使用 Unity 编辑器模拟运行](content-simulation.html)

---

## AR Session 屏幕旋转适配
- 章节路径: `wechat/mega/session-device-orientation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-device-orientation.html

# AR Session 屏幕旋转适配
这篇文章介绍了当需要横屏运行微信小程序时如何配置 AR Session。
## 开始之前
* 通过 [AR 驱动的 3D 渲染](../../fundamentals/fundamentals.html)了解相机图像相对于屏幕方向的旋转角是什么。
* 了解 [AR Session 的概念与流程](session-state.html)。
## Mega 小程序插件的屏幕朝向枚举
> **注意**
手机屏幕的朝向定义请参考 IOS, Android 等系统的官方定义。
Mega 小程序插件的屏幕朝向枚举 [DeviceOrientation](../../../api/wechat/easyar.DeviceOrientation.html):
|Constant|Value|Description|
|`Portrait`|0|Portrait|
|`LandscapeLeft`|90|LandscapeLeft|
|`PortraitUpsideDown`|180|PortraitUpsideDown|
|`LandscapeRight`|270|LandscapeRight|
## 在微信小程序全局配置中修改屏幕朝向
在 `app.json` 中添加 `window` 配置，具体定义见 [响应显示区域变化](https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html) 。
```
"window": {
"pageOrientation": "landscape"
}
```
根据实际情况填入 "portrait"（竖屏） 或者 "landscape"（横屏）。
> **小心**
任何时候**不要**在 AR 小程序应用中使用 "auto"，在某些情况下会导致 AR 画面严重异常。
## 设置屏幕朝向
调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_) 传入屏幕旋转的方向，可随时调用，立即生效。
比如需要在屏幕相对自然竖直位置逆时针旋转 90 度的横屏模式下使用：
```
let deviceOrientation = mega.DeviceOrientation.LandscapeLeft;
session.setDeviceOrientation(deviceOrientation);
```
mega 插件提供的屏幕朝向设置是为了**弥补微信小程序屏幕朝向监听缺失**。微信在 `pageOrientation` 设置中仅提供了 `portrait` 和 `landscape` 两个选项，而对于 AR 应用来说仅这两个选项是不够的。例如自然朝向逆时针旋转90度的横屏和自然朝向逆时针旋转270度的横屏完全不同。
因此当 `app.json` 中 `pageOrientation` 设置为 `portrait` 时，可以不调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_)，因为一般手机的自然竖直方向是 session 的默认朝向。
当 `app.json` 中 `pageOrientation` 设置为 `landscape` 时，必须调用 [setDeviceOrientation(deviceOrientation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setDeviceOrientation_member_1_) 将屏幕朝向固定为 [LandscapeLeft](../../../api/wechat/easyar.DeviceOrientation.html#w_easyar_DeviceOrientation_LandscapeLeft_member) 或 [LandscapeRight](../../../api/wechat/easyar.DeviceOrientation.html#w_easyar_DeviceOrientation_LandscapeRight_member)

---

## 如何记录与转发 AR Session dump 文件
- 章节路径: `wechat/mega/session-dump.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-dump.html

# 如何记录与转发 AR Session dump 文件
AR Session dump 文件是 EasyAR 团队排查定位、跟踪问题的核心依据。
## 开始之前
* 了解什么是 [AR Session](session.html)。
* 确保您的项目已经[启用 EasyAR Mega](integration.html)。
## 什么是 AR Session dump 文件
> **重要事项**
AR Session dump 文件是微信小程序上分析和解决 Mega 定位、跟踪问题**最重要的依据**。
AR Session dump 文件记录了小程序进行 Mega 定位请求时的关键时空上下文。
## 如何记录与转发
通过调用 `session.dumpSession(signal: boolean)` 接口控制记录流程：
* **传入 `true`**：启动记录。
* **传入 `false`**：停止记录，并返回生成的 **文件临时路径 (tempFilePath)**。
通常建议将记录逻辑与 UI 按钮绑定，在开始记录时通过 [wx.showToast()](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html) 方法提示记录开始，在记录结束时通过 [wx.shareFileMessage()](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareFileMessage.html) 方法将记录的文件通过微信聊天转发。
```
/\*\*
\* 处理 Session 记录逻辑
\* @param signal true 为开始记录，false 为结束记录并转发
\*/
dumpSession(signal: boolean): void {
// 调用接口获取路径
const recordPath = session.dumpSession(signal);
// signal 为 true 时，接口返回空字符串，表示正在记录
if (recordPath.length == 0) {
wx.showToast({
title: '开始记录数据',
icon: 'success',
duration: 2000
});
return;
}
// signal 为 false 时，处理返回的文件路径
wx.shareFileMessage({
filePath: recordPath,
success() {
wx.showToast({
title: '记录转发成功',
icon: 'success',
duration: 2000
});
},
fail() {
wx.showToast({
title: '记录转发失败',
icon: 'error',
duration: 2000
});
}
})
}
```
>
> 这个例子演示了如何在 xr-frame 组件中使用
`> session.dumpSession()
`> 方法记录并转发 AR Session dump 文件，并且给出相应的 Toast 提示。
>
> **注意**
由于小程序本地空间限制（通常为 200MB），建议单次录制时间不要过长，且最长录制时间不能超过 10 分钟。
## 相关主题
* [使用微信小程序 Mega Toolbox 记录与转发 session dump 数据](../../../mega/data-collection/wechat/toolbox-dump.html)
* [使用你的小程序录制 AR Session dump 文件](../../../mega/data-collection/wechat/wechat-dump.html)
* [微信小程序问题报告注意事项](../diagnostics/report.html)

---

## AR Session 非现场使用
- 章节路径: `wechat/mega/session-gnss-simulation.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-gnss-simulation.html

# AR Session 非现场使用
这篇文章介绍了如何不在现场时使用 AR Session。
## 开始之前
* 了解 [AR Session 的概念与流程](session-state.html)
## 启用 Simulator 模式
使用 **Simulator** 模式可以避免开发 AR 应用过程中开发者必须长期驻场的情况。
在该模式下，session 不使用 GNSS 数据或使用虚假的 GNSS 数据输入。
> **警告**
启用 Simulator 模式后，画面会出现特定水印。
小程序正式发布时，AR Session 不允许使用 Simulator 模式。请务必在上线前移除相关配置。
### 不使用 GNSS 数据
使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [setGeoLocationInput(inputMode, geoLocation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setGeoLocationInput_member_1_) 方法 仅传入 "Simulator" 字符串。此后 session 不进行任何经纬度相关的定位。
```
session.setGeoLocationInput("Simulator");
```
### 使用模拟的 GNSS 数据
若需模拟用户处于特定位置，使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [setGeoLocationInput(inputMode, geoLocation)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setGeoLocationInput_member_1_) 方法传入 "Simulator" 字符串和指定的经纬度。此后 session 使用模拟的经纬度数据进行定位。
```
const targetLongitude = 123.45; // 经度
const targetLatitude = 32.1; // 纬度
session.setGeoLocationInput("Simulator", { longitude: targetLongitude, latitude: targetLatitude });
```
> **警告**
模拟输入必须使用 WGS-84 坐标系的经纬度数据。
使用错误的经纬度数据可能会导致定位失败或错乱。

---

## 平面 AR 追踪器异常处理
- 章节路径: `wechat/mega/session-plane-detection-error.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-plane-detection-error.html

# 平面 AR 追踪器异常处理
这篇文章介绍了如何通过注册回调处理微信平面 AR 追踪器的异常。
## 开始之前
* 通过[MegaTracker 工作流](tracker.html)了解：
* xr-frame 的[平面AR追踪器](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#Plane) 本质上是 [VisionKit 6DoF-平面能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)的封装。
* MegaTracker 是如何在 xr-frame 上工作的。
* 了解 [AR Session 的概念与流程](session-state.html)
## 为什么会出现平面检测异常
在特定情况下（如画面中出现大片白墙、摄像头长时间被遮挡等），微信平面 AR 追踪器可能出现状态异常。
此时平面 AR 追踪器无法正常输出每帧的相机位姿（即 6DoF 数据）这会导致 MegaTracker 无法工作。
当画面正常（纹理丰富，摄像头不被遮挡）一段时间后平面 AR 追踪器会恢复工作，同时 MegaTracker 也会恢复工作。
## 设置平面检测异常时的行为
通过 [setPlaneDetectionErrorBehavior(behavior)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setPlaneDetectionErrorBehavior_member_1_) 注册异常处理回调。当检测到异常时，该回调会被触发，开发者可在其中实现自定义提示，隐藏 3D 内容或其他处理逻辑。
```
session.setPlaneDetectionErrorBehavior(() => {
wx.showToast({
icon: 'none',
title: `微信平面检测结果异常，请将相机对着平面来回移动以恢复跟踪`,
duration: 2000,
});
});
```
>
> 这个例子中使用 session 的
[> setPlaneDetectionErrorBehavior(behavior)
](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_setPlaneDetectionErrorBehavior_member_1_)> 接口注册了一个弹出 Toast 窗口的回调，当平面检测异常时触发。
>

---

## AR Session 流程控制
- 章节路径: `wechat/mega/session-state.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session-state.html

# AR Session 流程控制
这篇文档将介绍 AR Session 流程控制，包括如何创建、启动、停止并销毁 AR Session。
## 开始之前
* 了解 [AR Session 的概念与流程](session-state.html)
## 创建
使用配置中的云定位库 `appId`，云服务 `serverAddress`，云服务 `apiKey` 和 `apiSecret` 创建 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)。
然后使用创建的 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member) 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
再使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
```
createSession() {
// 获取场景中挂载的 megaComponent
const megaElement = scene.getElementById('easyar-mega');
const megaComponent = megaElement.getComponent("easyar-mega") as easyar.EasyARMegaComponent;
// MegaTracker 云服务鉴权配置
const apiKeyAccess = new mega.APIKeyAccessData(this.data.appId, this.data.serverAddress, this.data.apiKey, this.data.apiSecret);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess
}
// Session 配置
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
}
// 创建实例
session = megaComponent.createSession(sessionConfigs);
}
```
>
> 这段代码演示了如何从场景中获取
`> megaComponent
`> 之后使用配置创建 session 实例。
>
> **小心**
单实例限制：一个场景中仅允许存在一个 Session 实例。在创建新 Session 前，必须确保已调用 [closeSession()](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_closeSession_member_1_) 销毁旧实例，否则将导致创建失败。
## 启动
一般在 xr-frame 的 AR 系统准备就绪的回调中使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 方法启动 session。
> **警告**
MegaTracker 依赖于平面 AR 追踪器提供的数据，在平面追踪器初始化完成前无法工作。
在 WXML 中使用 `bind:ready="handleReady"` 注册 AR 系统准备就绪事件：
```
<xr-scene ar-system="modes:Plane; planeMode: 1" bind:ready="handleReady">
```
在 xr-frame 组件中的回调函数 `handleReady` 中使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 方法启动 session。
```
handleReady: function(event) {
try {
//启动 Session，默认失败重试 5 次
await session.start();
} catch (err) {
console.error(`EasyAR Session initialization failed: ${err.message}`);
return;
}
}
```
## 停止并销毁
使用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [closeSession()](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_closeSession_member_1_) 方法销毁 session。
建议在 xr-frame 组件生命周期的 [detached](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html) 中调用保证在离开页面时（即组件实例被从页面节点树移除时）销毁。
```
lifetimes: {
detached: function() {
const megaElement = scene.getElementById('easyar-mega');
const megaComponent = megaElement.getComponent("easyar-mega") as easyar.EasyARMegaComponent;
megaComponent.closeSession();
}
}
```
## 前后台切换
在页面退到后台时使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [pause()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_pause_member_1_) 方法暂停 session。
在页面回到前台时使用 [EasyARSession](../../../api/wechat/easyar.EasyARSession.html) 的 [resume()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_resume_member_1_) 方法恢复 session。
```
/\*\* 小程序页面的调用\*/
onHide() {
if (this.ar) {
this.ar.pauseSession();
}
},
onShow() {
if (this.ar) {
this.ar.resumeSession();
}
}
/\*\* xr-frame 组件中的函数\*/
pauseSession(): void {
if (!session) { console.error("EasyAR Session is not ready"); return;}
session.pause();
},
resumeSession(): void {
if (!session) { console.error("EasyAR Session is not ready"); return;}
session.resume();
}
```
>
> 这段代码中 xr-frame 组件暴露了
`> pauseSession()
`> 和
`> resumeSession()
`> 两个函数。
>
> 在小程序页面中在
[> onHide
](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onHide)> 即小程序从前台进入后台时调用
`> pauseSession()
`> 暂停 session。
>
> 在
[> onShow
](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppShow.html)> 即小程序从后台进入前台时调用
`> resumeSession()
`> 恢复 session。
>

---

## Mega 微信小程序插件上的 AR Session 概念与流程
- 章节路径: `wechat/mega/session.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/session.html

# Mega 微信小程序插件上的 AR Session 概念与流程
这篇文档将介绍 Mega 微信小程序插件上的 AR Session 的概念与流程。
## AR Session 是什么
Mega 微信小程序插件提供的 AR Session 是所有 AR 功能的入口。它管理运行过程和状态：包括从 VisionKit 和微信提供的传感器 API 获取数据、融合云定位与本地 AR 跟踪器结果、驱动场景中相机等其它部分物体的移动和渲染等。
```
flowchart LR
Pose(VisionKit 相机位姿) -- 每帧同步 --> Session[Session]
Image(计算该帧相机位姿所使用的相机图片) -. 仅 Mega 定位时发送 .-> Session
Sensor(微信传感器数据) -. 异步 .-> Session
Session -- Transform --> Camera(xr-frame 摄像机)
```
## AR Session 的流程
```
flowchart LR
Start((" "))
End((" "))
Init[Initializing]
Run[Running]
Check{Success?}
Start -->|调用 start| Init
Init --> Check
Check -->|是| Run
Check -->|否 / 重试次数超过上限| End
Run -->|调用 stop| End
```
启动： session 状态转为 Initializing 。包含环境检查、资源加载以及等待微信 xr-frame 的 AR 系统就绪。
运行： session 状态转为 Running 。在此阶段，session 每帧输出跟踪结果并更新 xr-frame 相机的 Transform。
停止： session 状态转为 None 。包含释放资源、重置状态、销毁 MegaTracker。
> **警告**
AR 功能必须在 session 启动成功后才能使用。
AR Session 状态：
|状态|描述|
|None|初始状态，session 未启动或初始化失败|
|Initializing|初始化过程中|
|Running|运行状态，session已启动且初始化完成|
## [可选] 微信小程序插件上的 AR Session 与 Unity 上的 AR Session
> **注意**
仅针对 Unity 项目迁移的开发者。
Mega 微信小程序插件上的 AR Session 是 Unity 上 AR Session 的简化版本。由于不支持其他算法组件同时使用，微信小程序上的 AR Session 使用预集成的数据源组件和算法组件，用户不能选择数据源和/或组装算法组件。
此外，可以认为 Mega 微信小程序插件仅支持以 Block 为 target 且使用以 target 为中心的中心模式。
## 后续步骤
* [AR Session 流程控制](session-state.html)
## 相关主题
* [MegaTracker 的概念与工作流](tracker.html)

---

## MegaTracker 云服务鉴权
- 章节路径: `wechat/mega/tracker-access.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-access.html

# MegaTracker 云服务鉴权
这篇文章介绍了如何指定 MegaTracker 使用云服务时的鉴权方式。
## 开始之前
* 了解[MegaTracker 的概念与工作流](tracker.html)
* [获取和使用 APIKey](../../apikey-auth.html)
## 使用 API Key 和 API Secret 鉴权
这种方式适用于传统的密钥对验证。你需要使用 [APIKeyAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member) 来构造 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 中的 `access` 对象。
```
const apiKeyAccess = new mega.APIKeyAccessData(
settings.MegaTrackerAppID, // Mega 定位服务 AppID
settings.MegaTrackerServerAddress, // Mega 定位服务地址
settings.EasyARAPIKey, // APIKey 字符串
settings.EasyARAPISecret // APISecret 字符串
);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
>
> 这个例子中先使用配置中的云定位库
`> appId
`> ，云服务
`> serverAddress
`> ，云服务
`> apiKey
`> 和
`> apiSecret
`> 创建了
[> APIKeyAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)> 。
>
> 然后使用了创建的
[> APIKeyAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_APIKeyAccessData_member)> 创建
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> 。 这代表将使用 API Key 和 API Secret 鉴权
>
## 使用 API Token 鉴权
若能够使用服务器定时（每几分钟或几个小时）更新和下发 `APIToken`，使用这种方式避免了直接使用 APISecret 对定位请求进行签名，安全性更高。`APIToken` 的更新方式请参考 [Token的创建和使用方法](../../apikey-auth.html)。
可以根据 Token 的有效期，在前端设置定时器进行更新。
首先使用设置中的 Mega 定位库 AppID 和定位服务地址创建 [TokenAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member)。
然后使用创建的 [TokenAccessData](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member) 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
然后使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
当 Token 过期时，必须调用 [updateToken(apiToken)](../../../api/wechat/easyar.MegaTracker.html#w_easyar_MegaTracker_updateToken_member_1_) 进行更新，否则 Mega 服务将不可用，定位结果中的状态始终为 [ApiTokenExpired](../../../api/wechat/easyar.MegaLocalizationStatus.html#w_easyar_MegaLocalizationStatus_ApiTokenExpired_member)。
```
const tokenAccess = new mega.TokenAccessData(
settings.MegaTrackerAppID, // Mega 定位服务 AppID
settings.MegaTrackerServerAddress, // Mega 定位服务地址
"your\_api\_token" // APIToken 字符串
);
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: tokenAccess
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
>
> 这个例子演示了如何使用
[> TokenAccessData
](../../../api/wechat/easyar.IMegaSystem.html#w_easyar_IMegaSystem_TokenAccessData_member)> 创建
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> ，并且用这个
[> MegaTrackerConfigs
](../../../api/wechat/easyar.MegaTrackerConfigs.html)> 创建 session 以使用
`> APIToken
`> 鉴权。
>

---

## MegaTracker 传感器外部控制
- 章节路径: `wechat/mega/tracker-external-sensor.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-external-sensor.html

# MegaTracker 传感器外部控制
默认情况下，MegaTracker 会自动管理加速度计和 GNSS 数据的监听接口。但在某些复杂应用场景中，开发者可能需要手动控制这些接口的开启和关闭，以实现更精细的功耗管理或权限控制。
## 开始之前
* 了解[MegaTracker 的概念与工作流](tracker.html)
## 外部控制约束逻辑
在 session 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 时，可以通过 [MegaTrackerSensorOptions](../../../api/wechat/easyar.MegaTrackerSensorOptions.html) 配置传感器的监听接口。
|参数名|类型|默认值|说明|
|isAcceExternalControl|`boolean`|`false`|加速度计是否由外部（开发者）控制。|
|isGeoExternalControl|`boolean`|`false`|GNSS 数据是否由外部（开发者）控制。|
> **提示**
**适用场景**：如果您的应用除了 Mega 功能外，本身不直接订阅传感器数据，建议保持默认值 `false`，由 Mega 自动处理。
当上述参数设置为 `true` 时，开发者必须严格遵守以下调用顺序：
* **启动流程**
在调用 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) **之前**，必须确保已手动开启对应的传感器监听：
* **加速度计**：调用 [wx.startAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.startAccelerometer.html)。
* **GNSS**：调用 [wx.startLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)。
* **停止流程**
在调用 [stop()](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_stop_member_1_) **之后**，方可关闭对应的传感器监听：
* **加速度计**：调用 [wx.stopAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.stopAccelerometer.html)。
* **GNSS**：调用 [wx.stopLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.stopLocationUpdate.html)。
> **小心**
**冲突警告**：若设置为 `false`（Mega 托管），不能在 Session 运行期间调用微信原生的停止传感器接口，否则会导致数据中断。
```
const megaTrackerSensorOptions: easyar.MegaTrackerSensorOptions = {
isAcceExternalControl: false,
isGeoExternalControl: true
};
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess,
options: megaTrackerSensorOptions
};
session = megaComponent.createSession(megaTrackerConfigs);
```
>
> 这个例子演示了如何外部控制开启和关闭微信地理位置数据监听，在调用
[> start(options)
](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_)> 之前，需要调用
[> wx.startLocationUpdate
](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)> 以开启微信地理位置数据监听。
>

---

## 使用 Mega Landmark 服务
- 章节路径: `wechat/mega/tracker-landmark.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker-landmark.html

# 使用 Mega Landmark 服务
这篇文章介绍了在微信小程序 Mega 插件接入后，如何使用 Mega Landmark 的定位服务。
## 开始之前
* [获取和使用 APIKey](../../apikey-auth.html)（必须包括**Mega Landmark**）。
* 了解 [MegaTracker 的概念与工作流](tracker.html)。
* 了解 [MegaTracker 云服务鉴权](tracker-access.html)。
## 启用 Mega Landmark
首先使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 作为 `apiType` 创建 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html)。
然后使用 [MegaTrackerConfigs](../../../api/wechat/easyar.MegaTrackerConfigs.html) 和配置中的 `licenseKey` 创建 [SessionConfigs](../../../api/wechat/easyar.SessionConfigs.html)。
最终用 xr-frame 场景中挂载的 [EasyARMegaComponent](../../../api/wechat/easyar.EasyARMegaComponent.html) 的 [createSession(sessionConfigs)](../../../api/wechat/easyar.EasyARMegaComponent.html#w_easyar_EasyARMegaComponent_createSession_member_1_) 方法创建 session。
```
const megaTrackerConfigs: easyar.MegaTrackerConfigs = {
access: apiKeyAccess,
apiType: mega.MegaApiType.Landmark
};
const sessionConfigs: easyar.SessionConfigs = {
megaTrackerConfigs: megaTrackerConfigs,
licenseKey: settings.EasyARLicenseKey
};
session = megaComponent.createSession(sessionConfigs);
```
## 如何使用 LandmarkFilter
当使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 创建时，MegaTracker 会自动内部实例化 [MegaLandmarkFilter](../../../api/wechat/easyar.MegaLandmarkFilter.html)。
它的功能是 MegaTracker 在使用 Landmark 服务时通过 SpotId 或 GNSS 数据筛选当前最合适的 Mega 定位库。
筛选接口只能在 [start(options)](../../../api/wechat/easyar.EasyARSession.html#w_easyar_EasyARSession_start_member_1_) 成功后调用。
当 MegaTracker 使用 Landmark 服务而**没有**筛选成功时，定位状态始终为 [MissingSpotVersionId](../../../api/wechat/easyar.MegaLocalizationStatus.html#w_easyar_MegaLocalizationStatus_MissingSpotVersionId_member)
* **使用提供的 SpotID 匹配定位库**：
使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 的 [filterBySpotId(spotId)](../../../api/wechat/easyar.MegaLandmarkFilter.html#w_easyar_MegaLandmarkFilter_filterBySpotId_member_1_) 方法通过 SpotID 匹配定位库：
```
async landmarkFilter() {
const res = await session.megaTracker.landmarkFilter.filterBySpotId(settings.LandmarkSpotId);
if (res.status != mega.MegaLandmarkFilterStatus.Found) {
console.error(`LandmarkFilter Failed, status: ${mega.MegaLandmarkFilterStatus[res.status]}, exceptionInfo : ${res.exceptionInfo}`)
}
}
```
* **使用当前的 GNSS 数据匹配定位库**：
使用 [Landmark](../../../api/wechat/easyar.MegaApiType.html#w_easyar_MegaApiType_Landmark_member) 的 [filterByLocation()](../../../api/wechat/easyar.MegaLandmarkFilter.html#w_easyar_MegaLandmarkFilter_filterByLocation_member_1_) 方法通过使用当前的 GNSS 数据 匹配定位库：
```
async landmarkFilter() {
const res = await session.megaTracker.landmarkFilter.filterByLocation();
if (res.status != mega.MegaLandmarkFilterStatus.Found) {
console.error(`LandmarkFilter Failed, status: ${mega.MegaLandmarkFilterStatus[res.status]}, exceptionInfo : ${res.exceptionInfo}`)
}
}
```

---

## MegaTracker 的概念与工作流
- 章节路径: `wechat/mega/tracker.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/tracker.html

# MegaTracker 的概念与工作流
这篇文档将介绍 MegaTracker 的基本概念及 MegaTracker 与微信原生的 AR 系统 VisionKit 和渲染框架 xr-frame 的关系。
## 开始之前
通过 [Mega 简介](../../mega/intro.html) 了解：
* Mega 定位与跟踪的基本原理。
* 什么是 Mega Block。
* 集成 Mega 后的预期结果。
## 平面 AR 追踪器 是什么
xr-frame 的[平面AR追踪器](https://developers.weixin.qq.com/miniprogram/dev/component/xr-frame/ar/tracker.html#Plane) 本质上是 [VisionKit 6DoF-平面能力](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/visionkit/plane.html)的封装。
在 xr-frame 的摄像机组件开启 `isARCamera` 后，摄像机的三维变换**每帧**都会与 AR 系统 （VisionKit） 同步。
由 xr-frame 提供 3D 渲染能力，由 VisionKit 提供在现实空间坐标系下的**运动跟踪能力**。
平面 AR 跟踪器不能和其他 AR 跟踪器一起使用。
## MegaTracker 是什么
MegaTracker 是连接微信 AR 系统 （VisionKit） 与 Mega 空间计算服务的核心算法组件，由它提供云定位功能。
* **输入**：每一帧 VisionKit 计算出的**在 VisionKit 坐标系下的相机位姿**（即 6DoF 数据） 及 进行 Mega 定位那一帧时的**相机图片**。
* **输出**：当前定位和跟踪的 **Mega Block** 下的相机位姿 。
## MegaTracker 是如何在 xr-frame 上工作的
```
flowchart BT
subgraph Using xr-frame Only
direction BT
PlaneARTracker\_1[PlaneARTracker] -->|MotionData & Image| XRFrame\_1[xr-frame]
end
subgraph Using Mega Plugin
direction BT
PlaneARTracker\_2[PlaneARTracker] -->|MotionData & Image| MegaTracker
MegaTracker -->|CameraTransform| XRFrame\_2[xr-frame]
end
```
* 在微信原生提供的数据流中 xr-frame 的摄像机组件每帧由**平面 AR 追踪器**的结果直接更新。
* 在 Mega 小程序提供的数据流中 **在 VisionKit 坐标系下的相机位姿**（即 6DoF 数据）及定位帧的图片数据会输入给 **MegaTracker**，在云定位和本地计算之后输出当前定位和跟踪的 **Mega Block** 下的相机位姿 ，最终更新 xr-frame 场景中摄像机在 **Mega Block** 节点下的 LocalTransform，此时 **MegaTracker** 接管了摄像机的控制权， xr-frame **不再**根据 AR 追踪器更新摄像机。
**MegaTracker 的运行深度依赖于平面追踪器提供的 6DoF 运动数据**。 因此，在平面追踪器完成初始化并建立稳定的追踪状态前，MegaTracker 无法介入工作。此外，AR 追踪的稳定性受限于环境特征；在遇到大面积无纹理区域（如白墙）、相机长时间遮挡等极端场景时，若微信底层平面追踪发生漂移或丢失，MegaTracker 将因失去可靠的输入源而同步进入失效状态。
## 后续步骤
* [指定 MegaTracker 云服务鉴权方式](tracker-access.html)

---

## 在 xr-frame 微信小程序上播放透明视频
- 章节路径: `wechat/mega/transparent-video.md`
- 来源: https://www.easyar.cn/doc/zh-cn/develop/wechat/mega/transparent-video.html

# 在 xr-frame 微信小程序上播放透明视频
## 开始之前
* 准备需要播放的透明视频：将透明视频上传至文件服务器并获取用于在 xr-frame 中加载的 URL。
* 由于透明视频的播放依赖于替换场景中的贴图，需要事先标注播放透明视频的位置。
需要能够[使用 Unity 编辑器创建并上传标注](content-annotation-creation.html)。
## 什么是透明视频
**透明视频** 是一种为了在不原生支持透明通道的视频编码格式（如 H.264/AVC， H.265/HEVC） 中实现透明背景效果的技术方案。
该方案通过将视频画面的**颜色信息 （RGB）** 和**透明度信息 （Alpha）** 拆分，并按照特定的空间布局拼接到同一帧图像中，从而生成一个带有黑白遮罩的普通视频文件。在播放端，通过图形渲染管线实时采样并将两部分合成，还原出具有透明背景的动态画面。
根据颜色区域与 Alpha 区域的拼接方式，主要分为两种格式：
1. Side-by-Side （SBS）
Side-by-Side 是一种将 RGB 颜色帧与 Alpha 遮罩帧在**水平方向**上并排拼接的格式。通常约定左侧为颜色区域，右侧为对应的灰度 Alpha 区域。
2. Top-by-Bottom （TBB）
Top-by-Bottom 是一种将 RGB 颜色帧与 Alpha 遮罩帧在**垂直方向**上堆叠拼接的格式。通常约定上半部分为颜色区域，下半部分为对应的灰度 Alpha 区域。
## 在 xr-frame 小程序上标注位置播放透明视频
首先加载类型为 `video-texture` 的视频资源。
```
async loadAsset() {
const videoTexture = {
assetId: "fireball",
type: "video-texture",
// 视频资源 URL
src: "url/video-resource.mp4",
options: {
autoPlay: true,
loop: true,
}
};
try {
// 加载 video-texture 类型资源
await scene.assets.loadAsset(videoTexture);
} catch (err) {
console.error(`Failed to load video texture: ${err.message}`);
}
}
```
在 EMA 加载的回调中使用 `scene.createElement(xrFrameSystem.XRMesh,{})` 创建简单的几何体赋予 `easyar-video-tsbs` 材质， 并修改 `uniform` 为 `u\_baseColorMap:video-{$assetId}`。
> **注意**
`easyar-video-tsbs` 和 `easyar-video-ttbb` 材质的加载，注册，反注册，卸载由 AR Session 控制。
```
handleEmaResult(ema: easyar.ema.v0\_5.Ema) {
const blockHolder: easyar.BlockHolder = session.blockHolder;
ema.blocks.forEach(emaBlock => {
const blockInfo: easyar.BlockInfo = {
id: emaBlock.id
};
// 若 Block 节点不存在，创建 Block 节点
blockHolder.holdBlock(blockInfo, easyarPlugin.toXRFrame(emaBlock.transform));
});
ema.annotations.forEach(annotation => {
if (annotation.type !== mega.EmaV05AnnotationType.Node) {
return;
}
const nodeAnnotation = annotation as easyar.ema.v0\_5.Node;
const xrNode: xrfs.XRNode = easyarPlugin.createXRNodeFromNodeAnnotation(nodeAnnotation, blockHolder);
const assetInfo = AnnotationMetaData[nodeAnnotation.id as keyof typeof AnnotationMetaData];
let model: xrfs.Element;
if (assetInfo) {
// GLTF 部分
} else {
// 利用内置 Mesh 创建用于渲染的几何体
model = scene.createElement(xrFrameSystem.XRMesh, {
geometry: "cube",
material: "easyar-video-tsbs",
uniforms: "u\_baseColorMap:video-fireball",
});
xrNode.addChild(model);
}
});
}
```
> **注意**
在使用 `video-texture` 时，若控制台出现 `wx.createVideoDecoder with type: 'wemedia' is deprecated` 警告，请忽略。
经与微信官方团队确认，该警告不影响使用。
## 后续步骤
* [完整运行示例工程](fullstart.html)
* [示例工程说明](sample.html)
## 相关主题
* [Block数据组件](../../../mega/reference/studio-unity/block-viewer.html)
* [标注工具](../../../mega/reference/studio-unity/annotation-tool.html)
