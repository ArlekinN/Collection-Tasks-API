#!/usr/bin/env python3

import connexion
from prometheus_client import generate_latest
from flask import Response
from swagger_server import encoder
import logging
import os

# Определение пути для логов
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)  # Создаем папку logs, если она не существует
log_file = os.path.join(log_dir, 'app.log')
if os.path.exists(log_file):
    os.remove(log_file)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Логи сохраняются в файл
        logging.StreamHandler()         # Логи выводятся в консоль
    ]
)

def main():
    logging.info("The application is running on port 8080")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Collection of tasks'}, pythonic_params=True)

    @app.route('/metrics')
    def metrics():
        logging.info("Query to /metrics")
        return Response(generate_latest(), mimetype='text/plain')

    app.run(port=8080)



if __name__ == '__main__':
    main()
