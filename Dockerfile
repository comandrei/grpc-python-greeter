FROM python:3.8
RUN pip install grpcio==1.38.0
COPY server.py server.py
EXPOSE 50051
CMD ["python", "server.py"]