<template>
    <div align="center" style="margin-top: 100px">
        <span>房间号:</span>
        <input type="text" id="room-id">
        <button @click="onButtonClick" style="background-color: greenyellow; margin-right: 80px;">确认</button>
        <input @change="onInputFileChange" type="file" id="file" >
        <br>
        <video id="video-id" style="width: 70%;margin-top: 50px;" controls autoplay></video>
    </div>
</template>

<script>
import { getTime } from '@/network/api'

export default {
  name: 'GuestView',
  data () {
    return {
      roomId: null,
      player: null
    }
  },
  mounted () {
    this.player = document.getElementById('video-id')
    const timer = setInterval(this.synchronizeTime, 5000)
    this.$once('hook:beforeDestroy', () => {
      clearInterval(timer)
    })
  },
  methods: {
    onButtonClick (e) {
      const inputValue = document.getElementById('room-id').value
      if (inputValue === '') {
        alert('房间号不能为空!')
      } else if (inputValue.length > 8) {
        alert('房间号不能超过8位!')
      } else {
        this.roomId = inputValue
        alert('您进入的房间号为: ' + this.roomId)
      }
    },
    onInputFileChange () {
      if (this.roomId === null) {
        alert('请先输入房间号!')
      } else {
        const file = document.getElementById('file').files[0]
        const url = URL.createObjectURL(file)
        this.player.src = url
      }
    },
    synchronizeTime () {
      if (this.roomId !== null) {
        getTime({ roomId: this.roomId }).then(response => {
          const now = Date.now()
          const correctTime = now - response.timestamp
          const hostTime = response.current_time + correctTime / 1000
          const deltaTime = hostTime - this.player.currentTime
          if (deltaTime <= -2 && deltaTime >= -10) {
            this.player.playbackRate = 0.8
          } else if (deltaTime >= 2 && deltaTime <= 10) {
            this.player.playbackRate = 1.2
          } else if (deltaTime < -10 || deltaTime > 10) {
            this.player.currentTime = hostTime
          } else {
            this.player.playbackRate = 1
          }
          console.log(response, deltaTime)
        })
      }
    }
  }
}
</script>

<style scoped>

</style>
