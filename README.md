# Typecho-Spider

开发思路视频已上传bilibili—[Python爬取Typecho博客的所有文章](https://www.bilibili.com/video/BV1PA411E7N4)

针对Typecho博客的爬虫，将自己博客的文章保存到本地，以所有分类名建立文件夹，将不同类别的文章保存到不同文件夹中，并且以文章标题作为文件名

### 使用前

请修改三个参数：`url`、`cookies`、`page_number_end`

![](https://i.loli.net/2020/10/15/XwS32saufAdjEIq.png)

![](https://i.loli.net/2020/10/15/i5JIrxEz4pv3Qen.png)

#### url的获取方法

![image-20201015215141911](https://i.loli.net/2020/10/15/VbgRaXBK6HJm7fN.png)

#### cookies的获取方法

![image-20201015215509670](https://i.loli.net/2020/10/15/VUdRS3YefjkqlTP.png)

#### page_number_end的设定

`page_number_end`不可超过你最大的页码数，最大页码数见下图

![](https://i.loli.net/2020/10/15/DAca8Wxs5wgZkTV.png#shadow)

### 使用后

文章保存到了D盘blog文件夹中，请查看~