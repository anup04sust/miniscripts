# Batch Image Cropper

A simple Python 3 script to batch-crop images in a folder using fixed pixel coordinates, with an optional 180° rotation after cropping.

## Features

- Batch-process images in a folder.
- Crop images using fixed pixel coordinates.
- Optionally rotate cropped images 180° using `-r 1`.
- Preserve original image files.
- Save processed images in a separate output folder.
- Skip images that are too small for the specified crop.
- Display processing status and a summary.
- Support common image formats: JPG, JPEG, PNG, TIFF, BMP, and WebP.

## Requirements

- Python 3.8 or later
- Pillow

## Installation

Install the required dependency:

```bash
python3 -m pip install Pillow
```

## Default Crop Settings

| Setting | Value |
|---|---:|
| Original image size | 4960 × 7015 pixels |
| Crop width | 3535 pixels |
| Crop height | 5000 pixels |
| Crop starting point — left | 400 pixels |
| Crop starting point — top | 440 pixels |
| Crop ending point — right | 3935 pixels |
| Crop ending point — bottom | 5440 pixels |
| Rotation | Optional 180° |

The crop coordinates use the following format:

```text
(left, top, right, bottom)
(400, 440, 3935, 5440)
```

The resulting image dimensions are **3535 × 5000 pixels**.

## Usage

### 1. Crop images without rotation

```bash
python3 crop_images.py -i ./images -o ./cropped
```

### 2. Crop and rotate images 180°

Use `-r 1` to rotate each cropped image 180 degrees before saving.

```bash
python3 crop_images.py -i ./images -o ./cropped -r 1
```

### 3. Specify absolute folder paths

Example on Ubuntu Linux:

```bash
python3 crop_images.py \
  -i "/media/anup/Projects/scans" \
  -o "/media/anup/Projects/scans-cropped" \
  -r 1
```

### 4. Display available options

```bash
python3 crop_images.py --help
```

## Command-Line Options

| Option | Description | Default |
|---|---|---|
| `-i`, `--input` | Input folder containing images | Required |
| `-o`, `--output` | Destination folder for cropped images | `cropped` |
| `-r`, `--rotate` | `1` rotates 180°; `0` leaves the crop unrotated | `0` |
| `-h`, `--help` | Display help information | — |

## Example Output

```text
OK: image001.jpg 4960x7015 -> 3535x5000
OK: image002.jpg 4960x7015 -> 3535x5000
OK: image003.png 4960x7015 -> 3535x5000

Finished.
Successful: 3
Skipped/failed: 0
Output folder: /path/to/cropped
```

If an image is too small for the requested crop, it will be skipped and reported.

## How Rotation Works

When `-r 1` is specified, the script performs these operations in order:

1. Opens the original image.
2. Applies its EXIF orientation, if present.
3. Crops the image using the configured pixel coordinates.
4. Rotates the cropped image 180°.
5. Saves the result in the output folder.

Rotation does not change the final width or height.

## Important Notes

- Original images are not modified.
- Output images are saved in the specified destination folder.
- Images with unsupported extensions are ignored.
- Images that are too small for the crop are skipped.
- If an output image has the same filename as an existing file, it will be overwritten.
- JPEG images are saved with quality 95 and no chroma subsampling.
- The script processes images directly inside the input folder, not recursively through subfolders.

## Project Structure

```text
image-cropper/
├── crop_images.py
├── README.md
├── images/
│   ├── image001.jpg
│   ├── image002.jpg
│   └── image003.png
└── cropped/
    ├── image001.jpg
    ├── image002.jpg
    └── image003.png
```

The `images/` and `cropped/` folders are examples; you can use any folder paths.

## License

Use and modify this script for your personal or commercial projects.
