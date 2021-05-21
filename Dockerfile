FROM grpc/python
COPY server.py server.py
EXPOSE 50051
CMD ["python", "server.py"]