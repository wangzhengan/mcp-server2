import json
import sys

from .file_tools import FileTools


class MCPServer:
    def __init__(self, root="."):
        self.files = FileTools(root)

    def handle(self, request):
        method = request.get("method")

        if method == "tools/list":
            return {
                "tools": [
                    {"name": "read_file"},
                    {"name": "list_directory"},
                    {"name": "search_files"},
                ]
            }

        if method == "tools/call":
            name = request["params"]["name"]
            args = request["params"].get("arguments", {})

            if name == "read_file":
                return {"content": self.files.read_file(args["path"])}
            if name == "list_directory":
                return {"files": self.files.list_directory(args.get("path", "."))}
            if name == "search_files":
                return {"files": self.files.search_files(args["keyword"])}

        return {"error": "unknown method"}


def main():
    server = MCPServer()
    for line in sys.stdin:
        request = json.loads(line)
        response = server.handle(request)
        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
