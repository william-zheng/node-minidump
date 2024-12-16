# minidump - Process minidump files

[![CI](https://github.com/electron/node-minidump/actions/workflows/CI.yml/badge.svg)](https://github.com/electron/node-minidump/actions/workflows/CI.yml)
[![npm version](http://img.shields.io/npm/v/minidump.svg)](https://npmjs.org/package/minidump)

## Installing

```sh
npm install minidump
```

## Building (for development)

* `git clone --recurse-submodules https://github.com/electron/node-minidump`
* `npm install`

## Docs

```javascript
var minidump = require('minidump');
```

### minidump.addSymbolPath(path1, ..., pathN)

Add search paths for looking up symbol files.

### minidump.walkStack(minidumpFilePath, [symbolPaths, ]callback)

Get the stack trace from `minidumpFilePath`, the `callback` would be called
with `callback(error, report)` upon completion.

### minidump.dump(minidumpFilePath, callback)

Parse and dump the raw contents of the minidump as text using `minidump_dump`.

### minidump.dumpSymbol(binaryPath, callback)

Dump debug symbols in minidump format from `binaryPath`, the `callback` would
be called with `callback(error, minidump)` upon completion.


## Releasing a new npm version
- Ensure you have checked out the `deps/breakpad` submodule. If you don't check
  this out, then the source code of breakpad will not be included in the npm
  package, and it will not be possible to build from source.
- Change the version in `package.json`, make a new git tag, and push it to GitHub.
- Wait until the GitHub Actions on the main branch pass.
- The artifacts of the latest GitHub Action run should be downloaded and placed under the `bin` folder
  (replacing the old folder if it exists).

	The bin folder should look like the following.
	```
	bin
	 |_linux-x64
		|_dump_syms
		|_minidump_dump
		|_minidump_stackwalk
	 |_darwin-x64
		|_dump_syms
		|_minidump_dump
		|_minidump_stackwalk
	```

- Then:
	```
	npm publish
	```
## 为什么要fork

说实话，这个项目管理的像x一样，很多年了也没有发布v1.0，而且代码质量也说不上好，
本质上还是一个缝合怪。
拼拼凑凑，总算让nodejs圈子里的人也能享受一下`breakpad`这种纯底层架构的东西。
粗看高大上，亲自试一下才知道都是坑。至于我，fork出来也不是为了造福大众，
能解决我自己的问题，并且能让我自己开心一下，就够了。

在说目标之前，先说一下目前发现的坑。

### 坑s

#### 1.git submodule 更换过指向

在 commit:cc15fce2b21afb9b454b41b45ece5bf4a1ac2a0a 提交中，有过如下修改
````
-	url = https://github.com/electron/chromium-breakpad.git
+	url = https://chromium.googlesource.com/breakpad/breakpad
````

提交注释没有任何解释。

但是仔细分析后发现，github上的项目根本就不是chromium.googlesource.com上
项目的代码镜像，而是一个完完全全的另一个项目。npm包里的东西更像是代码预编译
产物的缓存（至少在windows平台是）。

所以在项目0.0.0~0.15.0与0.16.0~至今，其实思路是完全不相同的，如果是小于
0.16.0版本的npm包，升级时请务必谨慎。

#### 0.15.0及之前的包在windows平台上的问题

在0.15.0及之前的版本，npm包的制作者贴心的为windows平台的使用者附上了预编译的
可执行文件，但是由于整个breakpad都是基于POSIX标准构建的（这个坑一会细说），
windows平台下并不能直接执行，还需要你自己找一个`cygwin1.dll`放上去。

#### 0.16.0之后的版本windows平台上的问题

迁移到googlesource平台的代码之后，可以看到官方团队维护的breakpad代码，真的不错。
开心过1分钟以后，就发现，如果不使用POSIX那一套库，在windows上根本构建不了。
（不得不怀疑windows系统在国外到底有没有人在做开发，全是写游戏的吗。）

原因有二：

1. 跨平台的构建系统被删了....

在 breakpad库的commitid: d31ce76161ba9ce0f7fd54e67ad582f777337e08 上，
把整个GYP构建系统都删了，只剩下了`./configure && make` 那一套。

提交注释写的倒是很详细，说是很早没人维护gyp了，干脆删了吧。看着闹心。
````
gyp: drop unused build system

Chromium moved to GN a long time ago, and CrOS has never used this.
Let's remove one of the build systems to make it easier on people.
Especially since the GYP tool is completely unmaintained now.
````

看到这个我是又生气又纳闷，真就不顾windows平台上的开发者死活了呗。

今年本人做了不少Nodejs上原生插件的开发，感觉使用gyp + visual studio build tools
做些跨平台的构建还是很简单的。于是我决定把删除之前的gyp配置文件挪到这个minidump项目中。

2. 写代码的时候真没考虑过跨平台...

在一些通用类里，直接引用的是`#include <unistd.h>` 这种POSIX库，一点没考虑windows平台怎么办。

#### gyp文件真的好久没人维护了

即使我不是要构建整个breakpad项目，只需要其中几个小工具。也拷贝了不少原来的GYP文件。

这才发现，gyp里的源码和Makefile.am里的都对不上，有多的，也有缺的。看来在breakpad团队里，gyp体系真的舅舅不疼，姥姥不爱的。但是在nodejs里，因为自带，我觉得还行。

还是那句话，幸亏这个minidump项目小，我也不管测试，能把js里的单元测试跑通就行。
C++里测试构建一律不管。

## 项目目标

### 解析dump文件

给mini-breakpad-server提供一个minidump解析库，能在windows、mac平台开发，
在linux上部署就行。

最主要的保证 `minidump.addSymbolPath`、`minidump.walkStack` 这两个方法能用就行。

### 跨平台，且在windows平台上用本平台编译器构建

使用posix在windows上搞，太不友好了

## 未来怎么办

如果有精力，就跟踪breakpad库的提交，即使更新windows平台的修改；即使更新gyp中的源代码和构建指令。

如果还有精力，至少把breakpad里那些不能跨平台的写法改了，提个PR。

如果没有精力，那就散戏吧。如果有同仁还有热情与精力，如果我这些懒代码能帮你们解决二三困惑，
那这次fork应该就没有白费。