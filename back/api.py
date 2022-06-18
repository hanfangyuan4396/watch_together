from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import delete_item, website_clear_supervisor_thread

app = Flask(__name__)
CORS(app)
data = {}

website_clear_supervisor_thread.start()
@app.route('/api/get_time')
def get_time():
    room_id = request.args.get('roomId')
    return jsonify(data[room_id])

@app.route('/api/post_time', methods=['POST'])
def post_time():
    received_data = request.json
    time_info = {}
    time_info['timestamp'] = received_data['timestamp']
    time_info['current_time'] = received_data['currentTime']
    room_id = received_data['roomId']
    data[room_id] = time_info
    return jsonify({room_id: time_info})

@app.route('/api/clear', methods=['POST'])
def clear_room():
    received_data = request.json
    if received_data['password'] == 'hanfangyuan':
        delete_item(data)
        return jsonify({'message': 'clear room success'})
    else:
        return jsonify({'message': 'password invalid'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
