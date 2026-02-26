# Excel Deduplication Tool

A simple Python automation script to remove duplicate entries from Excel files based on specific columns like Name, Email, or Phone Number.

## Features

- **Column-Specific Deduplication**: Choose one or multiple columns to check for duplicates.
- **Automatic Cleanup**: Removes duplicate rows and saves the result to a new file.
- **Smart Validation**: Checks if specified columns exist before processing.
- **Modern Python Management**: Uses PEP 723 metadata for seamless execution with `uv`.

## Setup

### Option 1: Using `uv` (Recommended)
If you have [uv](https://github.com/astral-sh/uv) installed, no manual setup is required. The dependencies will be handled automatically.

### Option 2: Using `pip`
If you prefer standard Python:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from your terminal using one of the following methods:

### Basic Command
```bash
# Using uv (no install needed)
uv run deduplicate.py data.xlsx --columns Email

# Using standard Python
python deduplicate.py data.xlsx --columns Email
```

### Examples

**1. Deduplicate by Email:**
```bash
uv run deduplicate.py contacts.xlsx --columns Email
```

**2. Deduplicate by Name and Number:**
```bash
uv run deduplicate.py contacts.xlsx --columns Name Number
```

**3. Specify a Custom Output File:**
```bash
uv run deduplicate.py contacts.xlsx --columns Email --output cleaned_contacts.xlsx
```

## Usage Rules
- The script expects an `.xlsx` file.
- Column names are case-sensitive and must match the headers in your Excel file.
- If no columns are specified, the script will deduplicate based on entire rows matching exactly.
