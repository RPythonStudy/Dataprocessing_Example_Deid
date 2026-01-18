import pandas as pd

def verify_updates(clinical_path):
    print(f"Verifying {clinical_path}...")
    try:
        xl = pd.ExcelFile(clinical_path, engine='openpyxl')
        sheets = xl.sheet_names
        
        results = []
        for sheet_name in sheets:
            df = pd.read_excel(xl, sheet_name=sheet_name)
            if len(df.columns) >= 2:
                deid_col = df.columns[1]
                missing_count = df[deid_col].isna().sum()
                total_count = len(df)
                
                # Sheet might have dummy rows or be empty
                if total_count > 0:
                    results.append({
                        "sheet": sheet_name,
                        "total": total_count,
                        "missing": int(missing_count),
                        "completed": total_count - int(missing_count)
                    })
        
        print("\nVerification Summary:")
        print(f"{'Sheet Name':<30} | {'Total':<8} | {'Missing':<8}")
        print("-" * 50)
        for res in results:
            print(f"{res['sheet']:<30} | {res['total']:<8} | {res['missing']:<8}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_updates("deid_clinicaldata.xlsx")
