# Python Projects

A collection of small Python utility apps and scripts — each demonstrates a different concept or library.

## Projects

### Calculator (`calc.py`)
A GUI calculator built with **Tkinter**. Supports basic arithmetic operations with a clean button layout.
```bash
python3 calc.py
```

### QR Code Generator (`QR_Code_Gen.py`)
Generates a custom QR code image using the `qrcode` and `Pillow` libraries.
```bash
pip install qrcode pillow
python3 QR_Code_Gen.py
```

### Email Validator (`email_valid(regex).py`)
Validates email address format using regular expressions.
```bash
python3 "email_valid(regex).py"
```

### PDF to Excel (`pdf_to_excel.py`)
Extracts tables from a PDF file and exports them to an Excel spreadsheet using `tabula-py` and `pandas`.
```bash
pip install tabula-py pandas openpyxl
python3 pdf_to_excel.py
```
> Place your PDF file as `new.pdf` in the same directory.

### Shutdown App (`shut_app.py`)
A Tkinter GUI app to shutdown, restart, or log out of a Windows machine with one click.
```bash
python3 shut_app.py
```

### Text to Speech (`Text to Speech/`)
Converts text input to spoken audio output.

## Requirements

Install all dependencies at once:
```bash
pip install qrcode pillow tabula-py pandas openpyxl
```
