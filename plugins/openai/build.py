"""Build the OpenAI upload ZIP using only the Python standard library."""

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


PACKAGE = Path(__file__).resolve().parent
REPO = PACKAGE.parents[1]


def main():
    manifest = json.loads((PACKAGE / "plugin.json").read_text())
    json.loads((PACKAGE / "mcp.json").read_text())
    version = manifest["version"]
    if not all(part.isdecimal() for part in version.split(".")) or len(version.split(".")) != 3:
        raise ValueError("Use a major.minor.patch package version.")

    output = REPO / "dist" / f"data-parrot-openai-{version}.zip"
    output.parent.mkdir(exist_ok=True)
    files = {
        "plugin.json": PACKAGE / "plugin.json",
        "mcp.json": PACKAGE / "mcp.json",
        "assets/icon.png": PACKAGE / "assets/icon.png",
        "LICENSE": REPO / "LICENSE",
    }
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, source in files.items():
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, source.read_bytes())

    print(output)
    print(f"SHA-256: {hashlib.sha256(output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
