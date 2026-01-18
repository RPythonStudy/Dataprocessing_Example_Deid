import pandas as pd

def make_sheet_list(file_path, output_path):
    print(f"Reading {file_path}...")
    try:
        xl = pd.ExcelFile(file_path)
        sheet_names = xl.sheet_names
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for sheet in sheet_names:
                f.write(sheet + '\n')
        
        print(f"Sheet list saved to {output_path}")
        print(f"Total sheets: {len(sheet_names)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    make_sheet_list("deid_clinicaldata.xlsx", "sheet_list.txt")
