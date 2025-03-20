import pandas as pd

class SpreadsheetGenerator:
    def create_sheet(self, data, output_path):
        df = pd.DataFrame([data])
        df.to_excel(output_path, index=False)