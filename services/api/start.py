from app import application


if __name__ == "__main__":
    application.run(
        host = '0.0.0.0',
        port = 80,
        debug = application.config['DEBUG_MODE'],
        use_reloader = application.config['DEBUG_MODE']
    )
