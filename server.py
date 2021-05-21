from concurrent import futures
import logging
import time

import grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    server.add_insecure_port('[::]:50051')
    server.start()
    while True:
        try:
            time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()