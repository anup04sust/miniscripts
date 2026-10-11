# MiniScripts

A collection of small, practical scripts designed to simplify everyday tasks, automate repetitive workflows, and improve developer productivity.

MiniScripts brings together lightweight utilities for image processing, file management, data transformation, and development workflows. Each script is designed to solve a specific problem and be easy to use, customize, and reuse.

## Features

- **Lightweight utilities** — Small scripts focused on specific tasks.
- **Automation** — Reduce repetitive manual work.
- **File processing** — Work with images, JSON, text, and other file formats.
- **Developer tools** — Useful helpers for everyday development workflows.
- **Simple usage** — Command-line options and practical examples.
- **Open for contributions** — A growing collection of reusable utilities.

## Scripts

Scripts are organized by purpose. This list will grow as new utilities are added.

| Script | Description | Language |
|---|---|---|
| `crop_images.py` | Batch-crop images to specified dimensions with optional 180° rotation. | Python 3 |

### Image Cropper

Batch-process images using fixed crop coordinates and optionally rotate the cropped results.

**Features**
- Process multiple images in a folder.
- Configure crop dimensions and starting coordinates.
- Rotate cropped images 180° using a command-line option.
- Preserve original files by saving results to a separate directory.

**Example:**

```bash
python3 crop_images.py -i ./images -o ./cropped -r 1
```

See the script's help output for available options:

```bash
python3 crop_images.py --help
```

## Requirements

Requirements depend on the individual script.

For Python scripts, Python 3 and any dependencies documented by the script may be required.

For example, the image cropper uses Pillow:

```bash
python3 -m pip install Pillow
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/anup04sust/miniscripts.git
cd miniscripts
```

Browse the available scripts and follow the usage instructions provided in their documentation.

Individual scripts may have their own dependencies, arguments, and configuration options.

## Repository Structure

The repository may use the following structure as the collection grows:

```text
miniscripts/
├── README.md
├── image-processing/
├── file-management/
├── data-tools/
└── automation/
```

Scripts can be organized into directories by category, or kept in the repository root when they are small and independent.

## Adding a New Script

When contributing a new utility:

1. Give the script a clear, descriptive filename.
2. Keep it focused on one task.
3. Document its requirements and usage.
4. Include practical command-line examples.
5. Avoid modifying original files unless explicitly requested or documented.
6. Add an entry to the Scripts section of this README.

## Contributing

Suggestions, improvements, bug fixes, and useful small utilities are welcome.

When submitting a contribution, include a short explanation of the problem the script solves and instructions for running it.

## License

A license has not yet been specified. Add a `LICENSE` file before declaring the repository's reuse and distribution terms.
