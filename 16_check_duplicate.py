import pandas as pd
import json
import yaml

def check_duplicates(clinical_path):
    print(f"Checking duplicates in {clinical_path}...")
    try:
        xl = pd.ExcelFile(clinical_path, engine='openpyxl')
        sheets = xl.sheet_names
        
        duplicate_results = {}
        
        for sheet_name in sheets:
            df = pd.read_excel(xl, sheet_name=sheet_name)
            if len(df.columns) > 0:
                reg_col = df.columns[0] # Column A: 등록번호
                
                # Filter out nulls before checking duplicates
                mask = df[reg_col].notna()
                duplicates = df[mask][df[mask].duplicated(subset=[reg_col], keep=False)]
                
                if not duplicates.empty:
                    # Count occurrences per patient
                    counts = duplicates[reg_col].value_counts().to_dict()
                    # Convert keys to string for JSON/YAML compatibility
                    counts_str = {str(k): int(v) for k, v in counts.items()}
                    duplicate_results[sheet_name] = counts_str
                    print(f"  Found duplicates in sheet: {sheet_name} ({len(counts)} patients)")
        
        # Save results
        with open("duplicates.json", "w", encoding='utf-8') as f:
            json.dump(duplicate_results, f, indent=4, ensure_ascii=False)
            
        with open("duplicates.yaml", "w", encoding='utf-8') as f:
            yaml.dump(duplicate_results, f, allow_unicode=True, default_flow_style=False)
            
        print("\nDuplicate check completed. Results saved to duplicates.json and duplicates.yaml")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_duplicates("deid_clinicaldata.xlsx")
