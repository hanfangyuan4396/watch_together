<template>
    <div align="center" style="margin-top: 100px">
        <span>房间号:</span>
        <input type="text" id="room-id">
        <button @click="onButtonClick" style="background-color: deepskyblue; margin-right: 80px;">创建</button>
        <input @change="onInputFileChange" type="file" id="file" >
        <br>
        <video id="video-id" style="width: 70%;margin-top: 50px;" controls autoplay></video>
    </div>
</template>

<script>
import { postTime } from '@/network/api'

export default {
  name: 'HostView',
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
        alert('创建成功, 房间号: ' + this.roomId + ' 快去把房间号分享给你的小伙伴吧!')
      }
    },
    onInputFileChange () {
      if (this.roomId === null) {
        alert('请先创建房间!')
      } else {
        const file = document.getElementById('file').files[0]
        const url = URL.createObjectURL(file)
        this.player.src = url
      }
    },
    synchronizeTime () {
      if (this.roomId !== null) {
        const timestamp = Date.now()
        const currentTime = this.player.currentTime
        const data = {
          roomId: this.roomId,
          timestamp,
          currentTime
        }
        postTime(data).then(response => {
          console.log(response)
        })
      }
    }
  }
}
</script>

<style scoped>

</style>
