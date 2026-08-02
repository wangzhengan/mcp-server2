from .protocol import JsonRpcProtocol
from ..tools.registry import ToolRegistry


class MCPServer:
    def __init__(self, name="mcp-server2", version="0.2.0-alpha1"):
        self.name = name
        self.version = version
        self.protocol = JsonRpcProtocol()
        self.tools = ToolRegistry()

    def initialize(self):
        return {
            "serverInfo": {
                "name": self.name,
                "version": self.version,
            },
            "capabilities": {
                "tools": {},
            },
        }

    def handle(self, request):
        method = request.get("method")
        request_id = request.get("id")

        if method == "initialize":
            result = self.initialize()
        elif method == "tools/list":
            result = {"tools": self.tools.list_tools()}
        else:
            return self.protocol.error(request_id, -32601, "Method not found")

        return self.protocol.response(request_id, result)
