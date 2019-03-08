# wox-python-plugins

Wox是国人开源的Windows平台下的快速启动神器，基于JSONRPC和插件进行通讯，也支持用Python来编辑插件。

## plugins目录

收录了几个使用Python编写的Wox插件

### Wox.Plugin.HelloWord

最基础的Wox插件例子，通过`h`激活插件，输入任意文本，按下回车后，会自动复制到剪贴板

![](https://upload-images.jianshu.io/upload_images/8377832-b135f0fb97e2fe6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

不足之处

如果代码出现了报错，Wox会呆住，没什么反馈，不方便进行错误定位和代码调试

如导入模块名称写错

```python
import pyperclip1
```

![](https://upload-images.jianshu.io/upload_images/8377832-6447ee3397da9258.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### Wox.Plugin.HelloWordEx

HelloWord升级版，加入了报错检测和提醒，日志记录，方便脚本的开发和调试

还是刚刚的错误

```python
import pyperclip1
```

![](https://upload-images.jianshu.io/upload_images/8377832-3877cfa8f503d141.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

查看error.log

```
Tue, 19 Feb 2019 17:33:16 util.py[line:29] ERROR Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Roaming\Wox\Plugins\Hello World Ex-991dfc7a-7c37-41f7-8e63-273f83c9680f\util.py", line 35, in load_module
    yield
  File "C:\Users\Administrator\AppData\Roaming\Wox\Plugins\Hello World Ex-991dfc7a-7c37-41f7-8e63-273f83c9680f\main.py", line 7, in <module>
    import pyperclip1
ModuleNotFoundError: No module named 'pyperclip1'
```

