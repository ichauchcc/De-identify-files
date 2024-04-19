#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:23:27 2023

@author: yuchen
"""

import os
import glob
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import PyPDF2
import io

def find_pdf_files(directory, extension="pdf", ignore_case=True):
    """
    Finds and lists all the PDF files in the specified directory with optional case sensitivity.
    """
    if ignore_case:
        extension = "".join(["[{}]".format(ch + ch.swapcase()) for ch in extension])
    return glob.glob(os.path.join(directory, "*." + extension))

def filenames_to_excel(directory, output_excel):
    """
    Extracts filenames from a directory, processes them to remove identifiable information,
    and saves the results in an Excel file.
    """
    pdf_files = glob.glob(os.path.join(directory, "*.pdf"))
    deidentified_names = []

    for filepath in pdf_files:
        filename = os.path.basename(filepath)
        parts = filename.split('.')[0].split('_')[1:]  # Assuming filenames have identifiable parts before the first '_'
        new_name = '_'.join(parts) + '.pdf'
        deidentified_names.append(new_name)

    df = pd.DataFrame({
        'Original File': pdf_files,
        'Deidentified Name': deidentified_names
    })
    df.to_excel(output_excel, index=False)
    return pdf_files, deidentified_names

def add_watermark_to_pdf(input_pdf, watermark_pdf, output_pdf, watermark_text):
    """
    Adds a watermark to each page of the specified PDF.
    """
    with open(input_pdf, "rb") as file_input, open(watermark_pdf, "rb") as file_watermark:
        reader = PyPDF2.PdfFileReader(file_input)
        watermark_reader = PyPDF2.PdfFileReader(file_watermark)
        writer = PyPDF2.PdfFileWriter()

        # Create a watermark
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(10, 10, watermark_text)
        can.save()
        packet.seek(0)
        watermark = PyPDF2.PdfFileReader(packet)

        # Apply watermark to each page
        for i in range(reader.numPages):
            page = reader.getPage(i)
            page.mergePage(watermark.getPage(0))
            writer.addPage(page)

        with open(output_pdf, 'wb') as output:
            writer.write(output)

# Example usage:
directory_path = 'path_to_your_pdf_files'
excel_output = 'path_to_output_excel.xlsx'
watermark_pdf_path = 'path_to_watermark.pdf'
output_pdf_path = 'path_to_output_pdf.pdf'

pdf_files, new_names = filenames_to_excel(directory_path, excel_output)
for pdf, new_name in zip(pdf_files, new_names):
    add_watermark_to_pdf(pdf, watermark_pdf_path, os.path.join(directory_path, new_name), "Confidential")
