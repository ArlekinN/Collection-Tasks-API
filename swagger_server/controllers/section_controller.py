from swagger_server.metrics import REQUEST_COUNT_SECTION
import logging

sections = [
    {
        "id": "1",
        "name": "Математика",
    },
    {
        "id": "2",
        "name": "Химия",
    }
]

def get_all_sections():
    logging.info("Processed request to /section.")
    try:
        REQUEST_COUNT_SECTION.labels(method='GET', endpoint='/section').inc()
        response = sections, 200
    except Exception as e:
        logging.error(f"Error processing request to /section: {e}")
    return response
