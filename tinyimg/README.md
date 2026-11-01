# TinyImg – Python Image Optimizer

A lightweight Python 3 image optimization tool inspired by [TinyPNG](https://tinypng.com/). Compress images to reduce file size while maintaining good visual quality.

TinyImg supports single-image optimization as well as batch processing of multiple images.

## Features

- Optimize a single image or an entire directory.
- Batch processing with optional recursive directory scanning.
- JPEG compression with configurable quality.
- Lossless PNG optimization.
- WebP optimization.
- GIF optimization.
- Automatically creates output directories.
- Preserves original image dimensions.
- Never overwrites original images.
- Skips optimized files when compression does not reduce file size.
- Displays file-size reduction statistics.

## Supported Formats

| Format | Optimization | Default Settings |
|---|---|---|
| JPEG / JPG | Lossy | Quality 88, Progressive |
| PNG | Lossless | Maximum compression |
| WebP | Lossy | Quality 88, Method 6 |
| GIF | Lossless | Optimized encoding |

## Requirements

- Python 3.8+
- Pillow

## Installation

### 1. Install Python and dependencies

Ubuntu / Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Install Pillow:

```bash
python3 -m pip install Pillow
```

If your Linux environment uses externally managed Python packages:

```bash
sudo apt install python3-pil
```

### 2. Download or clone the project

```bash
git clone <repository-url>
cd tinyimg
```

### 3. Make the script executable

```bash
chmod +x tinyimg.py
```

## Usage

```bash
python3 tinyimg.py [OPTIONS]
```

### Optimize a Single Image

```bash
python3 tinyimg.py \
  -i ./photo.jpg \
  -o './optimize/[image_name]_optimize.[ext]'
```

Example output:

```text
[OK] photo.jpg
Original:  850.20 KB
Optimized: 245.40 KB
Saved:     71.14%

Completed: 1/1 images optimized.
```

### Optimize an Entire Directory

```bash
python3 tinyimg.py \
  -d ./images \
  -o './optimize/[image_name]_optimize.[ext]'
```

### Recursive Directory Optimization

Include images inside subdirectories:

```bash
python3 tinyimg.py \
  -d ./images \
  -o './optimize/[image_name]_optimize.[ext]' \
  -r
```

### Customize Image Quality

Default quality is 88.

Higher quality:

```bash
python3 tinyimg.py \
  -i ./photo.jpg \
  -o './optimize/[image_name]_optimize.[ext]' \
  -q 95
```

Smaller file size:

```bash
python3 tinyimg.py \
  -i ./photo.jpg \
  -o './optimize/[image_name]_optimize.[ext]' \
  -q 80
```

## Command-Line Options

| Option | Description |
|---|---|
| `-i`, `--image` | Source image file |
| `-d`, `--directory` | Source image directory |
| `-o`, `--output` | Output path/template |
| `-q`, `--quality` | JPEG/WebP quality (1–100, default: 88) |
| `-r`, `--recursive` | Include subdirectories |
| `-h`, `--help` | Display help |

**Important:** Use either `-i` or `-d`, not both.

## Output Filename

TinyImg uses two placeholders:

- `[image_name]` – Original image filename without extension.
- `[ext]` – Original file extension.

Example:

```bash
-o './optimize/[image_name]_optimize.[ext]'
```

Input:

```text
photo.jpg
banner.png
logo.webp
```

Output:

```text
optimize/
├── photo_optimize.jpg
├── banner_optimize.png
└── logo_optimize.webp
```

## Quality Recommendations

| Use Case | Quality |
|---|---:|
| Web images | 85–88 |
| Social media | 88–92 |
| High-quality photography | 92–95 |
| Maximum visual quality | 95–100 |

PNG optimization is lossless and does not use the JPEG/WebP quality setting.

## Important Notes

1. Original images are never modified.
2. Image dimensions are preserved.
3. JPEG transparency is flattened against a white background.
4. PNG compression is lossless.
5. If the optimized file is larger than or equal to the original, the output is discarded.
6. EXIF orientation is applied before saving.

## Limitations

TinyImg currently uses Pillow's built-in optimization methods. PNG compression may not match the reduction achieved by TinyPNG or advanced tools such as pngquant.

Animated GIF preservation and advanced metadata handling may vary by image format and Pillow version.

## License

MIT License – Free to use, modify, and distribute.

---

**TinyImg** – Optimize images. Preserve quality. Save bandwidth.