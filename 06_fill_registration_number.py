import pandas as pd
import os

def fill_registration_numbers(mapping_path, clinical_path):
    print(f"Loading mapping from {mapping_path}...")
    try:
        mapping_df = pd.read_excel(mapping_path, engine='openpyxl')
        # Column 0: 등록번호, Column 1: 등재번호
        id_map = dict(zip(mapping_df.iloc[:, 0].astype(str).str.strip(), mapping_df.iloc[:, 1]))
        print(f"Mapping loaded: {len(id_map)} IDs")
    except Exception as e:
        print(f"Error loading mapping: {e}")
        return

    print(f"Reading {clinical_path}...")
    try:
        xl = pd.ExcelFile(clinical_path, engine='openpyxl')
        sheets = xl.sheet_names
        all_data = {}
        
        for sheet_name in sheets:
            print(f"  Reading sheet: {sheet_name}")
            df = pd.read_excel(xl, sheet_name=sheet_name)
            
            if len(df.columns) >= 2:
                reg_col = df.columns[0]
                deid_col = df.columns[1]
                
                # Convert to string and strip for matching
                df[reg_col] = df[reg_col].astype(str).str.strip()
                
                # Apply mapping
                df[deid_col] = df[reg_col].map(id_map).fillna(df[deid_col])
                
            all_data[sheet_name] = df
            
    except Exception as e:
        print(f"Error reading clinical data: {e}")
        return

    temp_output = "deid_clinicaldata_temp.xlsx"
    print(f"Writing all sheets to {temp_output}...")
    try:
        with pd.ExcelWriter(temp_output, engine='xlsxwriter') as writer:
            for sheet_name, df in all_data.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Replace original with processed if successful
        os.replace(temp_output, clinical_path)
        print(f"Successfully updated {clinical_path}")
        
    except Exception as e:
        print(f"Error writing output: {e}")
        if os.path.exists(temp_output):
            os.remove(temp_output)

if __name__ == "__main__":
    fill_registration_numbers("deid_mapping.xlsx", "deid_clinicaldata.xlsx")
