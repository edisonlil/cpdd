# CPDD - Copy Deep Designate

Copy Deep Designate 是项目深度克隆工具，用于从源项目工程进行深度复制，并自动为新克隆的项目分配新的项目代号和权限设置。

> "Copy"：复制源项目或工程。"Deep"：进行深度复制，包括所有相关的文件和目录结构。"Designate"：指定或赋予新的项目代号或权限。


## 功能特性
* **深度复制**：全面复制源项目的所有文件和目录结构，确保新项目与源项目完全一致。
* **项目代号指定**：在复制完成后，自动为新项目分配一个新的项目代号，便于管理和区分不同的项目版本。

## 环境依赖
![img_1.png](img_1.png)

## 安装

//TODO

## 使用示例

```shell
cpdd -d 'targetChars:sourceChars,targetChars:sourceChars' -o outputPath  <项目路径>
```
* `-h --help`：查看帮助命令
