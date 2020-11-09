from flask import Flask, render_template
from flask_socketio import SocketIO



app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@socketio.on('stream')
def handle_message(message):
    print('received message: ' + message)
    socketio.emit('received', message, callback=messageReceived)

@socketio.on('streamVideo')
def handle_message_stream(message):
    print('received message: ')
    socketio.emit('receivedStream', message, callback=messageReceived)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)

# if __name__ == "__main__":
#     app.run(ssl_context='adhoc')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, keyfile='key.pem', certfile='cert.pem')
