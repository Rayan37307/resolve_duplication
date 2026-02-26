# /// script
# dependencies = [
#   "pandas",
#   "openpyxl",
# ]
# ///

import pandas as pd
import argparse
import os

def deduplicate_excel(input_file, output_file, columns):
    """
    Removes duplicates from an Excel file based on specified columns.
    """
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        # Load the Excel file
        df = pd.read_excel(input_file)
        
        # Check if columns exist
        missing_cols = [col for col in columns if col not in df.columns]
        if missing_cols:
            print(f"Warning: Columns {missing_cols} not found in the file.")
            print(f"Available columns: {list(df.columns)}")
            # Filter to only existing columns
            columns = [col for col in columns if col in df.columns]
            
        if not columns:
            print("No valid columns provided for deduplication. Deduplicating based on all columns.")
            subset = None
        else:
            subset = columns

        # Remove duplicates
        initial_count = len(df)
        df_deduped = df.drop_duplicates(subset=subset)
        final_count = len(df_deduped)

        # Save to a new Excel file
        df_deduped.to_excel(output_file, index=False)
        
        print(f"Successfully processed '{input_file}'.")
        print(f"Removed {initial_count - final_count} duplicate rows.")
        print(f"Saved cleaned data to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deduplicate Excel records (Email, Name, Number, etc.)")
    parser.add_index = False
    parser.add_argument("input", help="Path to the input Excel file")
    parser.add_argument("-o", "--output", help="Path to the output Excel file (default: cleaned_input.xlsx)")
    parser.add_argument("-c", "--columns", nargs="+", help="Column names to check for duplicates (e.g., Email Name)")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output if args.output else f"cleaned_{os.path.basename(input_file)}"
    # If no columns specified, we can try to guess or use all
    columns = args.columns if args.columns else []

    deduplicate_excel(input_file, output_file, columns)
