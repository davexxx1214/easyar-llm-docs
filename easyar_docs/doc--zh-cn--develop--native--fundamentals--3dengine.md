---
source: https://www.easyar.cn/doc/zh-cn/develop/native/fundamentals/3dengine.html
---

在 3D 引擎中使用 EasyAR | EasyAR 文档
**
##### Table of Contents
**
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
##### 注意
当屏幕图像旋转时，需要在旋转发生后的第一帧立刻重新计算 \\(\\theta\\)，否则可能出现瞬间的屏幕图像方向不正常。
## 相机背景和虚拟物体的渲染
在手机上渲染虚拟物体，需要将虚拟物体和相机画面对准。这要求我们将渲染相机和物体都放置在和真实空间完全对应的虚拟空间中，并使用物理相机相同的视场角、宽高比来进行渲染。相机画面和虚拟物体经过的透视投影变换几乎一模一样，只有一点区别，即相机画面的透视投影变换大部分是发生在物理相机中，而虚拟物体的透视投影变换完全是一个计算过程。
以下均采用 OpenGL 惯例，使用其他惯例，需要进行相应的坐标轴映射。假设相机坐标系的坐标轴定义如下：x 轴指向右，y 轴指向上，z 轴出屏幕向外。剪裁坐标系的坐标轴定义如下：x 轴指向右，y 轴指向上，z 轴出屏幕向外，w 轴为虚拟轴。
此时，渲染相机画面需要的透视投影变换矩阵如下：
\\[
P\_i=\\left(
\\begin{array}{cccc}
(-1)^{\\text{flip}} &amp; \\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; 1 &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; 1 &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} &amp; 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
\\cos (-\\theta ) &amp; -\\sin (-\\theta ) &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\sin (-\\theta ) &amp; \\cos (-\\theta ) &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; 1 &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} &amp; 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
s\_x &amp; \\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; s\_y &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; 1 &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} &amp; 1 \\\\
\\end{array}
\\right)
\\]
其中：`flip`是指画面是否左右翻转，翻转时值为 1，不翻转时值为 0；\\(\\theta\\) 是图像沿顺时针旋转角，单位为弧度； \\(s\_x\\) 、 \\(s\_y\\) 是缩放系数，用于进行等比缩放或等比填充，它们随 \\(\\theta\\) 变化。此变换矩阵首先对相机图像进行缩放，然后进行旋转，最后进行翻转。渲染时应使用一个矩形铺满屏幕，例如在 OpenGL 中，可以将矩形的顶点放在 \\((-1, -1, 0)\\) 、 \\((1, -1, 0)\\) 、 \\((1, 1, 0)\\) 、 \\((-1, 1, 0)\\) ，UV 坐标设置在对应的四个角上，然后使用此透视投影矩阵渲染。
渲染虚拟物体需要的透视投影矩阵如下：
\\[
P=P\_i\\left(
\\begin{array}{cccc}
1 &amp; \\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; 1 &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; -\\frac{f+n}{f-n} &amp; -\\frac{2 f n}{f-n} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; -1 &amp; \\phantom{0} \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
\\frac{2}{w} &amp; \\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\frac{2}{h} &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; 1 &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} &amp; 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 &amp; \\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; -1 &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; -1 &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} &amp; 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
f\_x &amp; \\phantom{0} &amp; c\_x &amp; \\phantom{0} \\\\
\\phantom{0} &amp; f\_y &amp; c\_y &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; 1 &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} &amp; 1 \\\\
\\end{array}
\\right)\\left(
\\begin{array}{cccc}
1 &amp; \\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; -1 &amp; \\phantom{0} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; -1 &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; \\phantom{0} &amp; 1 \\\\
\\end{array}
\\right)
\\]
其中： \\(n\\) 、 \\(f\\) 是通常 3D 渲染的透视投影矩阵中使用的近裁和远裁参数； \\(w\\) 、 \\(h\\) 是相机图像的像素宽高； \\(f\_x\\) 、 \\(f\_y\\) 、 \\(c\_x\\) 、 \\(c\_y\\) 为相机模型中常用的内参，其中 \\(f\_x\\) 、 \\(f\_y\\) 是像素焦距， \\(c\_x\\) 、 \\(c\_y\\) 为主点像素位置。此投影投影矩阵依次进行如下变换：相机内参的透视投影变换（由于 OpenCV 中图像坐标系 y、z 轴方向和 OpenGL 相机坐标系相反，进行了两次坐标系变换），从图像像素坐标系转换到图像矩形坐标系的变换，近裁和远裁的变换，渲染相机画面时的透视投影变换。
经过整理，可得
\\[
P=P\_i\\left(
\\begin{array}{cccc}
\\frac{2 f\_x}{w} &amp; \\phantom{0} &amp; 1-\\frac{2 c\_x}{w} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\frac{2 f\_y}{h} &amp; -1+\\frac{2 c\_y}{h} &amp; \\phantom{0} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; -\\frac{f+n}{f-n} &amp; -\\frac{2 f n}{f-n} \\\\
\\phantom{0} &amp; \\phantom{0} &amp; -1 &amp; \\phantom{0} \\\\
\\end{array}
\\right)
\\]
从上述过程可知，渲染通常需要分两次进行，一次渲染相机画面，一次渲染虚拟物体，虚拟物体覆盖在相机画面之上。
有些 3D 引擎中将透视投影矩阵表示为横向视场角、宽高比等参数，如果不考虑旋转、翻转，忽略主点偏移，是可以计算的，其中横向视场角 \\(\\alpha=2 arctan{\\frac{w}{2 f\_x}}\\) ，宽高比 \\(r=\\frac{w}{h}\\) 。
需要注意这个过程中没有考虑相机畸变的情况，因为目前大部分手机的相机畸变非常轻微。