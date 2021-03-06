from app import app, socketio


if __name__ == "__main__":
    socketio.run(
        app,
        host = '0.0.0.0',
        port = 80,
        debug = app.config['DEBUG_MODE'],
        use_reloader = app.config['DEBUG_MODE']
    )
