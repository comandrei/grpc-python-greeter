from concurrent import futures
import logging
import time

import grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

logger = logging.getLogger(__name__)

def serve():
    logger.info("Starting greeter")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    server.add_insecure_port('[::]:50051')
    logger.info("Binding on port 50051")
    server.start()
    logger.info("Server started")
    server.wait_for_termination()
    logger.info("Server terminated")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()