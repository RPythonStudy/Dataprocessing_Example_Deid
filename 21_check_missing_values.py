import pandas as pd
import json
import yaml

def check_missing_values(clinical_path):
    print(f"Checking missing values in {clinical_path}...")
    try:
        xl = pd.ExcelFile(clinical_path, engine='openpyxl')
        sheets = xl.sheet_names
        
        missing_report = {}
        
        for sheet_name in sheets:
            df = pd.read_excel(xl, sheet_name=sheet_name)
            
            # Count missing values per column
            null_counts = df.isnull().sum()
            # Filter only columns with missing values
            null_cols = null_counts[null_counts > 0].to_dict()
            
            if null_cols:
                missing_report[sheet_name] = {str(k): int(v) for k, v in null_cols.items()}
                print(f"  Sheet: {sheet_name} - {len(null_cols)} columns have missing values")
        
        # Save results
        with open("missing_values.json", "w", encoding='utf-8') as f:
            json.dump(missing_report, f, indent=4, ensure_ascii=False)
            
        with open("missing_values.yaml", "w", encoding='utf-8') as f:
            yaml.dump(missing_report, f, allow_unicode=True, default_flow_style=False)
            
        print("\nMissing values check completed. Results saved to missing_values.json and missing_values.yaml")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_missing_values("deid_clinicaldata.xlsx")
