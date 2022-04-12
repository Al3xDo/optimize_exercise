from project import create_app, make_celery

app = create_app()
# celery = make_celery(app)
if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        user_reload=True,
        threaded=True
    )