class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, name, handler, description=""):
        self._tools[name] = {
            "handler": handler,
            "description": description,
        }

    def list_tools(self):
        return [
            {
                "name": name,
                "description": item["description"],
            }
            for name, item in self._tools.items()
        ]

    def call(self, name, arguments=None):
        if name not in self._tools:
            raise KeyError(name)
        return self._tools[name]["handler"](**(arguments or {}))
