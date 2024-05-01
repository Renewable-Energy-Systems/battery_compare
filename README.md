# BATTERY DATA Comparator

## Introduction
This Python script compares two CSV files and identifies any differences between them. It's particularly useful for comparing CSV files with similar data structures.

## Requirements
- Python 3.x
- pandas library (`pip install pandas`)

## Usage
1. Place the script (`compare_csv.py`) in the directory containing the CSV files you want to compare.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script and CSV files.
4. Run the script using the command: `python compare_csv.py`.
5. Follow the on-screen prompts.

## File Structure
- `main.py`: The Python script for comparing CSV files.
- `battery1.csv`: Sample CSV file 1 for testing.
- `battery2.csv`: Sample CSV file 2 for testing.

## Output
The script will output any differences found between the two CSV files. It will identify the row number (S.No) and the column where the difference occurred, along with the old and new values.

## Example
```
Differences found:
In S.No 1, Operator has been changed from Ramu to Somu
```

## Contributors
- [kiranpranay](https://github.com/kiranpranay)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.