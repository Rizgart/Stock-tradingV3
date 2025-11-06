from __future__ import annotations

import grpc


class RecommendationServiceServicer:
    """Placeholder gRPC servicer to be implemented with protobuf definitions."""

    async def GetRecommendations(self, request, context):  # noqa: N802 - gRPC naming
        del request, context
        return None


class GRPCServer:
    def __init__(self, port: int = 50051) -> None:
        self.port = port
        self.server = grpc.aio.server()

    async def start(self) -> None:
        listen_addr = f"[::]:{self.port}"
        self.server.add_insecure_port(listen_addr)
        await self.server.start()

    async def stop(self) -> None:
        await self.server.stop(0)

    async def wait_for_termination(self) -> None:
        await self.server.wait_for_termination()
