# GeoJSON Winding Order Correction

This project corrects the winding order of polygons in GeoJSON files to ensure they follow the right-hand rule.

## Installation

1. Clone this repository.
2. Create a virtual environment:

   - For Mac/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - For Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. Install dependencies
   ```bash
    pip install -r requirements.txt
   ```

## Usage

1. Place your input GeoJSON file named input.json in the project directory. \*
2. Run the script:
   ```bash
   python correct_winding.py
   ```
3. The corrected GeoJSON will be saved as output.json.

> Example files are provided in the example directory:
>
> - example/input.json: An example input file demonstrating the format of GeoJSON that can be processed.
> - example/output.json: An example output file showing the expected result after processing.
>
> You can use these example files to test the script or as a reference for your own input files.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
