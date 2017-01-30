from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.session import SignedCookieSessionFactory


def hello_world(request):
    if "count" not in request.session:
        request.session["count"] = 0
    else:
        request.session["count"] += 1
    return Response("Count is {count}".format(count=request.session["count"]))


def make_app():
    session_factory = SignedCookieSessionFactory(secret="blah")
    config = Configurator(session_factory=session_factory)
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()

app = make_app()


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

