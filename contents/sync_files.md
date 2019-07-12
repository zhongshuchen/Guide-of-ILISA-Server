# 在代码编辑器上同步服务器文件

当前，如果用户在本地上编辑程序并希望在 ILISA 服务器上运行它，需要进行以下步骤：

> 保存本地程序 -> 登录 FTP 服务器 -> 上传本地程序 -> 在服务器上运行程序

一些代码编辑器可以通过安装插件或扩展完成本地文件与服务器文件的同步，以免去使用 FTP 工具上传的步骤，如果配置了自动保存，甚至可以免去手动上传的步骤，实现两步运行：

> 保存本地程序 -> 在服务器上运行程序



## 在 Sublime Text 3 上使用 SFTP

使用 Package Control 安装 SFTP 后，在左侧 Sidebar 的工程目录右键单击，可找到 STP -> Map to Remote 选项，单机后，插件将在工程目录创建配置文件，用户需要完成以下的配置：

``` json
"host": "192.168.1.123", // ILISA 服务器地址
"user": "", // 用户名
"password": "", // 密码
"port": "2000", // 端口
"remote_path": "home/[username]/mycode", // 远程目录地址（配置的路径必须存在）
```

配置完成后，重新在工程目录右键单击，即可在 STP 选项卡下找到更多的选项，其中 Upload File 和 UpLoad Folder 可将文件或目录上传到远程目录。

如果用户配置了自动保存：

```json
"upload_on_save": true,
```

则插件会在文件被保存的同时将它上传到服务器。 

参考文档：

> [Installation - Package Control](https://packagecontrol.io/installation)



## 在 Visual Studio Code 上使用 SFTP

在 VS Code 扩展商店中安装 SFTP 后，切换至工作目录。按 Ctrl + Shift + P (macOS: Command + Shift + P) 调出命令框，运行 SFTP: config 命令，插件会在工作目录下创建 sftp.json 文件，用户需要完成以下配置：

```json
"host": "192.168.1.123", // ILISA 服务器地址
"protocol": "sftp", // 协议
"port": 2000, // 端口
"username": "", // 用户名
"password":"", // 密码
"remotePath": "/home/czs/lab/vscodetest", // 远程目录地址
```

配置完成后，在资源管理器工作目录或文件右键单击，可找到 Upload File 和 UpLoad Folder 等选项，使用这些选项可将文件或目录上传到远程目录。

如果用户配置了自动保存：

```json
"upload_on_save": true,
```

则扩展会在文件被保存的同时将它上传到服务器。 