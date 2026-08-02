from mcp.server.fastmcp import FastMCP
from .file_tools import FileTools


mcp = FastMCP("local-files")
files = FileTools(".")


@mcp.tool()
def read_file(path: str) -> str:
    """Read a local text file."""
    return files.read_file(path)


@mcp.tool()
def list_directory(path: str = ".") -> list[str]:
    """List files in a directory."""
    return files.list_directory(path)


@mcp.tool()
def search_files(keyword: str) -> list[str]:
    """Search keyword in local files."""
    return files.search_files(keyword)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
