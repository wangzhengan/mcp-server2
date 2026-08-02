import json


class JsonRpcError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class JsonRpcProtocol:
    """Minimal JSON-RPC 2.0 message handler for MCP."""

    def parse(self, message: str):
        return json.loads(message)

    def response(self, request_id, result):
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": result,
        }

    def error(self, request_id, code, message):
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": code,
                "message": message,
            },
        }
