
#!/usr/bin/env python3

import argparse
from pathlib import Path
from PIL import Image, ImageOps

SUPPORTED = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def optimize_image(source, destination, quality=88):
    try:
        with Image.open(source) as original:
            image = ImageOps.exif_transpose(original)
            image.load()

            ext = source.suffix.lower()
            destination.parent.mkdir(parents=True, exist_ok=True)

            if ext in (".jpg", ".jpeg"):
                if image.mode not in ("RGB", "L"):
                    if "A" in image.getbands():
                        background = Image.new("RGB", image.size, "white")
                        background.paste(image, mask=image.getchannel("A"))
                        image = background
                    else:
                        image = image.convert("RGB")

                image.save(
                    destination,
                    format="JPEG",
                    quality=quality,
                    optimize=True,
                    progressive=True
                )

            elif ext == ".png":
                image.save(
                    destination,
                    format="PNG",
                    optimize=True,
                    compress_level=9
                )

            elif ext == ".webp":
                if image.mode not in ("RGB", "RGBA"):
                    image = image.convert(
                        "RGBA" if "A" in image.getbands() else "RGB"
                    )

                image.save(
                    destination,
                    format="WEBP",
                    quality=quality,
                    method=6
                )

            elif ext == ".gif":
                image.save(
                    destination,
                    format="GIF",
                    optimize=True
                )

        original_size = source.stat().st_size
        optimized_size = destination.stat().st_size

        if optimized_size >= original_size:
            destination.unlink()
            print(f"[SKIP] No size reduction: {source.name}")
            return False

        saved = (original_size - optimized_size) / original_size * 100

        print(f"\n[OK] {source.name}")
        print(f"Original:  {original_size / 1024:.2f} KB")
        print(f"Optimized: {optimized_size / 1024:.2f} KB")
        print(f"Saved:     {saved:.2f}%")

        return True

    except Exception as error:
        print(f"[ERROR] {source}: {error}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="TinyImg - Image Optimizer"
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-i", "--image",
        help="Single image file"
    )

    group.add_argument(
        "-d", "--directory",
        help="Directory containing images"
    )

    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output path with [image_name] and [ext] placeholders"
    )

    parser.add_argument(
        "-q", "--quality",
        type=int,
        default=88,
        help="JPEG/WebP quality (default: 88)"
    )

    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Include subdirectories"
    )

    args = parser.parse_args()

    if not 1 <= args.quality <= 100:
        parser.error("Quality must be between 1 and 100")

    template = args.output

    if "[image_name]" not in template or "[ext]" not in template:
        parser.error("Output must contain [image_name] and [ext]")

    output_template = Path(template)

    if args.image:
        source = Path(args.image).resolve()

        if not source.is_file():
            parser.error(f"Image not found: {source}")

        if source.suffix.lower() not in SUPPORTED:
            parser.error(f"Unsupported image format: {source.suffix}")

        images = [source]

    else:
        source_dir = Path(args.directory).resolve()

        if not source_dir.is_dir():
            parser.error(f"Directory not found: {source_dir}")

        files = source_dir.rglob("*") if args.recursive else source_dir.iterdir()

        images = [
            f for f in files
            if f.is_file()
            and f.suffix.lower() in SUPPORTED
            and not f.stem.endswith("_optimize")
        ]

    if not images:
        print("No supported images found.")
        return

    success = 0

    for source in images:
        if args.recursive and args.directory:
            relative = source.relative_to(source_dir)
            output_dir = output_template.parent / relative.parent
        else:
            output_dir = output_template.parent

        filename = output_template.name.replace(
            "[image_name]", source.stem
        ).replace(
            "[ext]", source.suffix.lstrip(".")
        )

        destination = output_dir / filename

        if optimize_image(source, destination, args.quality):
            success += 1

    print(f"\nCompleted: {success}/{len(images)} images optimized.")


if __name__ == "__main__":
    main()
