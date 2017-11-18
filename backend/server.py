from concurrent import futures
import time

import grpc

import history_pb2
import history_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Historian(history_pb2_grpc.HistorianServicer):

  def GetCommand(self, request, context):
    
    print(request)
    return history_pb2.Response(
      status=history_pb2._STATUS.values_by_name['OK'].name)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  history_pb2_grpc.add_HistorianServicer_to_server(Historian(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()