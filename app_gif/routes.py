from views import handler, ws_handler


def setup_routes(app):
    app.router.add_get('/', handler)
    app.router.add_get('/ws', ws_handler)
