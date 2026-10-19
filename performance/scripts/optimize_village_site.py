
from pathlib import Path
import base64
import hashlib
import re
import mimetypes
import sys

source = Path.home() / "Downloads" / "Village Crafts"
output = Path.home() / "Desktop" / "village-crafts-optimized-site"
assets = output / "assets"

pages = [
    "index.html",
    "collection.html",
    "contact.html",
    "gallery.html",
    "new-pieces.html",
    "our-story.html",
]

pattern = re.compile(
    r"data:(image/[A-Za-z0-9.+-]+);base64,([A-Za-z0-9+/=\r\n\t ]+)"
)

extensions = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
    "image/avif": ".avif",
    "image/bmp": ".bmp",
}

if not source.is_dir():
    sys.exit(f"Original folder not found: {source}")

if output.exists():
    sys.exit(
        f"Output already exists: {output}\n"
        "Rename it before running this script again."
    )

missing = [p for p in pages if not (source / p).is_file()]
if missing:
    sys.exit(f"Missing original pages: {missing}")

assets.mkdir(parents=True)
saved_images = {}
print("Creating a separate experimental copy...\n")

for page in pages:
    original = (source / page).read_text(
        encoding="utf-8", errors="replace"
    )
    replaced = 0

    def extract(match):
        nonlocal_placeholder = None  # No change to original files
        nonlocal_vars = None
        mime = match.group(1).lower()
        encoded = re.sub(r"\s+", "", match.group(2))

        try:
            data = base64.b64decode(encoded, validate=True)
        except Exception:
            return match.group(0)

        digest = hashlib.sha256(data).hexdigest()

        if digest not in saved_images:
            ext = extensions.get(
                mime, mimetypes.guess_extension(mime) or ".img"
            )
            filename = f"image_{len(saved_images)+1:02d}_{digest[:10]}{ext}"
            (assets / filename).write_bytes(data)
            saved_images[digest] = filename

        return "assets/" + saved_images[digest]

    # Count references replaced in each page
    updated = pattern.sub(extract, original)
    replaced = len(pattern.findall(original))

    (output / page).write_text(updated, encoding="utf-8")

    old_size = (source / page).stat().st_size / 1024
    new_size = (output / page).stat().st_size / 1024
    print(
        f"{page}: {old_size:.1f} KB -> {new_size:.1f} KB "
        f"(image references found: {replaced})"
    )

print(f"\nUnique image files extracted: {len(saved_images)}")
print(f"Experimental website: {output}")
print("\nOriginal website files and live website were not changed.")
print("HTML sizes exclude the separate image assets.")
