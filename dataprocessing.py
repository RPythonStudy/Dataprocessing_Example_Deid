import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import shutil
    import os

    # Define file paths
    src_mapping = "deid_전체환자_등록번호+등재번호.xlsx"
    dst_mapping = "deid_mapping.xlsx"

    src_clinical = "deid_KQIPS eCRF (수신-전산팀) 20250508 수정_수술전후검사결과제공_20250529.xlsx"
    dst_clinical = "deid_clinicaldata.xlsx"

    # Copy files if they exist
    copy_status = []

    if os.path.exists(src_mapping):
        shutil.copy2(src_mapping, dst_mapping)
        copy_status.append(f"Copied `{src_mapping}` to `{dst_mapping}`")
    else:
        copy_status.append(f"Error: `{src_mapping}` not found.")

    if os.path.exists(src_clinical):
        shutil.copy2(src_clinical, dst_clinical)
        copy_status.append(f"Copied `{src_clinical}` to `{dst_clinical}`")
    else:
        copy_status.append(f"Error: `{src_clinical}` not found.")
    return (copy_status,)


@app.cell
def _(copy_status, mo):
    mo.md(
        f"""
        ### File Copy Operations
    
        The following operations were performed:
    
        1. {copy_status[0] if len(copy_status) > 0 else "Pending..."}
        2. {copy_status[1] if len(copy_status) > 1 else "Pending..."}
        """
    )
    return


if __name__ == "__main__":
    app.run()
