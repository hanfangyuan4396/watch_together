# Watch Together

**异起看，异地一起看视频**

本项目网站地址：[异起看](http://video.huohuohuo.xyz/)

本项目提供了一种多人同步播放本地视频的方法。

如果使用腾讯会议共享屏幕一起看电影的话，画质不能保证，而且同步效果也不好。为什么不能双方都把电影下载好，然后同步播放呢？但是靠人手动同步播放时间的话，万一对方想快进或暂停，还需要重新问一下对方播放时间。

所以就简单写了本网站，只传输电脑的时间戳和视频的时间戳，主播或观众创建或进入同一个房间，打开同一个视频文件，观众页面的视频会自动与主播页面同步。

## Features

- [x] 同步视频播放时间
- [x] 房间号
- [x] Vue重写前端
- [ ] 支持多种格式(mp4支持比较好，其他格式可能无法播放)
- [ ] 支持快捷键(方向键修改音量、快进快退，空格暂停与开始)，直接使用flv.js?
- [ ] 支持外挂字幕文件

## 目录结构

### back

使用python flask模块实现的后端，uwsgi部署

### front

朴素的html前端页面

### vuefront

使用vue重写的前端