from gunicorn import __version__

def app(environ, start_response):
    """Load test GET request"""
    data = b'This is load testing of a simple GET request'
    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('X-Gunicorn-Version', __version__)
    ]
    start_response(status, response_headers)
    return [data]
