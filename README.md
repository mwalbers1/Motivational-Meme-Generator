# Motivational Meme Generator

## Overview
Meme Generator Project for Udacity Intermediate Python Nanodegree. 

## Setup Instructions

**1. Create Virtual Environment**

Create virtual environment called `.venv` by issuing the following command at the terminal. Navigate to the project folder called Meme-Generator and then open a terminal session. Issue the following command.

```bash
$ python -m venv --copies .venv
```

This command creates a new virtual environment for your project.  If you are using an IDE such as PyCharm then update the project interpreter settings to point to the pythonw.exe file located in the Scripts sub-folder in the .venv directory. Note that the Python sys.path has been updated to reflect the new .venv folder site-packages folder for Python modules to reference.

**2. Activate the virtual environment**

Run this command at the terminal to activate the new virtual environment.

```bash
$ .\.venv\Scripts\activate
```
<br/>

**3. Install dependencies into Virtual Environment**

The required packages are stored in the requirements.txt file.  Run this command to install these dependencies into the active virtual environment.

```bash
$ python -m pip install -r requirements.txt
```
<br/>

## Sub-Modules

### Quote Engine Module

The Quote Engine module is responsible for reading in motivational quotes from various file formats including TXT, PDF, DOCX, and CSV.  The motivational quotes in each source file is composed of a quote and its author.  The Quote body and author are read into a list of QuoteModel objects.  A `QuoteModel` is an object containing two properties, body and author.

The QuoteEngine Module consists of an abstract base class and sub classes where each subclass represents the specific file type of motivational quotes.

![](Meme%20Generator%20class%20diagram.png)


**<ins>Ingestor</ins>**

The Ingestor class holds a collection of all ingestor types including docx, pdf, text, and CSV ingestor objects.  The parse method in this class iterates through each ingestor sub-type and calls the parse method on the ingestor which can ingest the input file.

**<ins>DocxIngestor</ins>**

Overrides parse method to read motivational quotes from a Word document

**<ins>CSVIngestor</ins>**

Overrides parse method to read motivational quotes from a CSV file

**<ins>PDFIngestor</ins>**

Overrides parse method to read motivational quotes from a PDF document

**<ins>TextIngestor</ins>**

Overrides parse method to read motivational quotes from a text document

### Meme Generator Module

The Meme Generator module is responsible for resizing an image to a maximum width of 500px and then adding a caption quote body and author to a random location on the image.  The path to the new image file is returned.

<ins>**MemeEngine**</ins>

The Meme Engine class defines a method called make_meme which takes an input image and resizes it and adds a motivational caption.  The new image is saved to output directory specified as a parameter of the __init__ method.


## How to Run Program

**Run at Terminal**

To run from the terminal command line, run below command.  The meme.py script takes three optional CLI arguments.  This script returns a path to a generated image.  If any argument is not defined, a random selection is used.

- `--body` a string quote body
- `--author` a string quote author
- `--path` an image path

```bash
$ python meme.py
```
<br/>

**Run from Flask app**

Start the Flask server by issuing this command from a terminal window.

```bash
$ python app.py
```
<br/>



