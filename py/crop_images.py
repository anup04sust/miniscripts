
#!/usr/bin/env python3
"""Batch crop images from a folder using fixed pixel coordinates."""

import argparse
from pathlib import Path
from PIL import Image, ImageOps

# Crop settings (pixels)
CROP_WIDTH = 3535
CROP_HEIGHT = 5000
CROP_TOP = 440
CROP_LEFT = 400

SUPPORTED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp"
}


def crop_images(
    input_dir: Path,
    output_dir: Path,
    rotate: int = 0,
) -> None:
    if not input_dir.is_dir():
        raise NotADirectoryError(f"Input folder not found: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    image_files = sorted(
        p for p in input_dir.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not image_files:
        print(f"No supported images found in {input_dir}")
        return

    success = 0
    failed = 0

    for image_path in image_files:
        try:
            with Image.open(image_path) as original:
                # Apply EXIF orientation before cropping.
                image = ImageOps.exif_transpose(original)
                width, height = image.size

                right = CROP_LEFT + CROP_WIDTH
                bottom = CROP_TOP + CROP_HEIGHT

                if right > width or bottom > height:
                    print(
                        f"SKIP: {image_path.name} "
                        f"({width}x{height}) is too small. "
                        f"Required at least {right}x{bottom}."
                    )
                    failed += 1
                    continue

                # Crop the image.
                cropped = image.crop((
                    CROP_LEFT,
                    CROP_TOP,
                    right,
                    bottom,
                ))

                # Rotate 180 degrees if -r 1 is specified.
                if rotate == 1:
                    cropped = cropped.rotate(180)

                output_path = output_dir / image_path.name

                save_options = {}

                if output_path.suffix.lower() in {".jpg", ".jpeg"}:
                    if cropped.mode not in ("RGB", "L"):
                        cropped = cropped.convert("RGB")

                    save_options["quality"] = 95
                    save_options["subsampling"] = 0

                cropped.save(output_path, **save_options)

                print(
                    f"OK: {image_path.name} "
                    f"{width}x{height} -> "
                    f"{cropped.width}x{cropped.height}"
                    f"{' (rotated 180°)' if rotate == 1 else ''}"
                )
                success += 1

        except Exception as exc:
            print(f"ERROR: {image_path.name}: {exc}")
            failed += 1

    print("\nFinished.")
    print(f"Successful: {success}")
    print(f"Skipped/failed: {failed}")
    print(f"Output folder: {output_dir.resolve()}")


def main():
    parser = argparse.ArgumentParser(
        description="Batch crop images using fixed pixel coordinates."
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Folder containing original images",
    )

    parser.add_argument(
        "-o", "--output",
        default="cropped",
        help="Output folder (default: cropped)",
    )

    parser.add_argument(
        "-r", "--rotate",
        type=int,
        choices=[0, 1],
        default=0,
        help="Rotate cropped image 180 degrees (1=yes, 0=no)",
    )

    args = parser.parse_args()

    crop_images(
        Path(args.input),
        Path(args.output),
        args.rotate,
    )


if __name__ == "__main__":
    main()
