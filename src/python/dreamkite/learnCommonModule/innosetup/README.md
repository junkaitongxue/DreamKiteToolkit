使用innosetup进行快速生成一个安装包

步骤一：
```pip install pyinstaller```

步骤二：
```angular2html
cd D:\programEr\Code\myCode\python\DreamKiteToolkit
pyinstaller -F .\src\python\dreamkite\learnCommonModule\innosetup\hello.py --icon=.\release\res\logo.ico --clean
```
步骤三：
下载innosetup: https://jrsoftware.org/isinfo.php
https://blog.csdn.net/2301_76161259/article/details/134327383

步骤四：（如何网页能够打开本地的应用程序，需要自定义对应注册表协议）
注册表位置：计算机\HKEY_CLASSES_ROOT\hello
```
[HKEY_CLASSES_ROOT\hello]
@="helloProtocol"
"URL Protocol"="helloProtocol"
```

补充pyinstaller参数：
```
-D/--onedir：生成一个包含所有依赖文件的单文件夹目录。适合以框架形式编写工具代码，易于维护。
-F/--onefile：生成一个单个的可执行文件，包含所有依赖文件。这个文件较大，但更方便分发。
-c/--console：生成一个控制台应用程序，可以在命令行中运行。
-w/--windowed：生成一个窗口应用程序，没有控制台窗口。
-i/--icon=：指定生成的可执行文件的图标。
-n/--name=：指定生成的可执行文件和spec文件的名称。14
-p/--paths=：添加额外的模块搜索路径。
-r/--add-data=：将指定的文件或目录添加为资源文件，可以在程序运行时访问。
--clean：在打包之前清理之前生成的临时文件
```