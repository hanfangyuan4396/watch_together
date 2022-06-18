<template>
    <div align="center">
        <img src="../assets/watch_together.png" width="30%" alt="">
        <h3>异起看，异地一起看视频</h3>
        <p>本网站(<span class="important">异起看</span>网站)提供了一种多人同步播放<span class="important">本地视频</span>的方法。</p>
        <p>如果使用腾讯会议共享屏幕一起看电影的话，画质不能保证，而且同步效果也不好。</p>
        <p>为什么不能双方都把电影下载好，然后同步播放呢？但是靠人手动同步播放时间的话，万一对方想快进或暂停，还需要重新问一下对方播放时间。</p>
        <p>所以就简单写了本网站，只传输电脑的时间戳和视频的时间戳，主播或观众创建或进入同一个房间，打开同一个视频文件，观众页面的视频会自动与主播页面同步。</p>
    </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
    div {
        margin-top: 100px;
    }
    .important {
        font-weight: bolder;
    }
</style>
