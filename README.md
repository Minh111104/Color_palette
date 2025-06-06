# Color Palette Extractor 🎨

This is a simple Flask web application that allows users to upload an image and extract its most dominant colors. The extracted colors are displayed as a palette with their corresponding HEX codes and pixel counts.

## Features

- Upload JPG or PNG images.
- Extract the top N most common colors from the image.
- Display the uploaded image and a palette of extracted colors.
- See HEX codes and pixel counts for each color.

## How It Works

1. User uploads an image via the web interface.
2. The app processes the image, counts the most frequent colors, and converts them to HEX codes.
3. The results page shows the uploaded image and a grid of color swatches.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Minh111104/Color_palette.git
    cd Color_palette
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create required folders:**
    - Make sure you have a `static/uploads` folder for uploaded images.
    - Make sure you have a `templates` folder with `upload.html` and `results.html`.

## Usage

1. **Run the app:**

    ```bash
    python main.py
    ```

2. **Open your browser and go to:**

    ```bash
    http://127.0.0.1:5000/
    ```

3. **Upload an image and view the extracted color palette.**

## Project Structure

```bash
Color_palette/
│
├── main.py
├── requirements.txt
├── README.md
├── static/
│   └── uploads/
├── templates/
│   ├── upload.html
│   └── results.html
```

## Dependencies

- Flask
- Flask-WTF
- Pillow
- NumPy

## License

This project is created for educational purpose.

**Enjoy extracting color palettes from your images!**
