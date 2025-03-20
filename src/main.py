from src.pdf_processor import PDFProcessor
from src.data_extractor import DataExtractor
from src.spreadsheet import SpreadsheetGenerator
import os

def main():
    pdf_processor = PDFProcessor()
    data_extractor = DataExtractor()
    spreadsheet_gen = SpreadsheetGenerator()

    for filename in os.listdir("input"):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join("input", filename)
            text = pdf_processor.extract_text(pdf_path)
            data = data_extractor.extract_fields(text)
            
            output_filename = f"output/{os.path.splitext(filename)[0]}.xlsx"
            spreadsheet_gen.create_sheet(data, output_filename)

if __name__ == "__main__":
    main()