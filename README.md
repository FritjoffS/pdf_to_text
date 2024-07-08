markdown
# PDF to Text Converter

## Description

This is a simple GUI application built with KivyMD that allows users to convert PDF files to text. The application provides an intuitive interface for selecting a PDF file and converting its contents to a text file.

## Features

- User-friendly graphical interface
- File selection using a built-in file manager
- Conversion of PDF files to text
- Error handling for invalid file selections and conversion issues

## Requirements

- Python 3.6+
- KivyMD
- PyPDF2

## Installation

1. Clone this repository:

git clone https://github.com/yourusername/pdf-to-text-converter.git

2. Navigate to the project directory:

cd pdf-to-text-converter

3. Install the required packages:

pip install kivymd PyPDF2

## Usage

1. Run the application:

python main.py

2. Use the "Select PDF" button to choose a PDF file from your system.

3. Click the "Convert to Text" button to convert the selected PDF to text.

4. The application will display a success message with the path of the output text file, or an error message if something goes wrong.

## How it works

1. The application uses KivyMD for the graphical user interface.
2. File selection is handled by the MDFileManager component.
3. PDF conversion is done using the PyPDF2 library.
4. The converted text is saved in a new file with the same name as the input PDF, but with a .txt extension.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/pdf-to-text-converter/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Fredrik