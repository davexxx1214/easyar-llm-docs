---
source: https://www.easyar.cn/doc/zh-cn/develop/object-tracking/model-requirements.html
original_file: doc--zh-cn--develop--object-tracking--model-requirements.md
normalized_at: 2026-02-27
---
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
