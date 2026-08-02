from pathlib import Path


class FileTools:
    def __init__(self, root: str = "."):
        self.root = Path(root).resolve()

    def _safe_path(self, path: str) -> Path:
        target = (self.root / path).resolve()
        if not str(target).startswith(str(self.root)):
            raise PermissionError("Path outside sandbox")
        return target

    def list_directory(self, path: str = "."):
        target = self._safe_path(path)
        return [p.name for p in target.iterdir()]

    def read_file(self, path: str):
        target = self._safe_path(path)
        return target.read_text(encoding="utf-8")

    def search_files(self, keyword: str):
        result = []
        for p in self.root.rglob("*"):
            if p.is_file():
                try:
                    if keyword in p.read_text(encoding="utf-8", errors="ignore"):
                        result.append(str(p.relative_to(self.root)))
                except Exception:
                    pass
        return result
