#!/usr/bin/env python3

import connexion
from prometheus_client import generate_latest
from flask import Response
from swagger_server import encoder

from swagger_server.metrics import REQUEST_COUNT

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Collection of tasks'}, pythonic_params=True)

    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype='text/plain')

    app.run(port=8080)



if __name__ == '__main__':
    main()
