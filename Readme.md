In the realm of healthcare data management, the protection of privacy is paramount. Clinical files often contain sensitive personal information that, if exposed, could lead to privacy violations and potential misuse. De-identifying clinical files even before the project is started is essential for several reasons:
    
    1. Compliance with Regulations
    
    2. Facilitating Research
    
    3. Enhancing Data Sharing

This Python tool aims to provide a robust solution for de-identifying files, ensuring that data used in research and other projects maintains the highest standards of privacy and compliance.


## Directory Structure

To use this de-identification tool effectively, your project directory should be structured as follows:

.

    ├── deidentify_pdf_tool/          # Main project folder
    │   ├── src/             # Source files for the tool
    │   │   ├── deidentify_tool.py    # Main script for the de-identification process
    │   │   └── utilities.py          # Helper scripts and utility functions
    │   ├── data/
    │   │   ├── input/                # Folder containing the PDFs to be de-identified
    │   │   └── output/               # Folder where the de-identified PDFs and Excel files will be saved
    │   ├── tests/   # Test cases for the tool
    │   ├── requirements.txt          # Required libraries
    │   └── README.md                 # Project documentation and setup instructions