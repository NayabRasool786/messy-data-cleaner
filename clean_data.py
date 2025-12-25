import pandas as pd
from datetime import datetime
import re

# --- STEP 1: EXTRACT ---
print("--- Loading Data ---")
try:
  df  = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/DEProjects/customer_dump.csv')
  print("Data Loaded Successfully.")
  print(f"Original shape: {df.shape}")
except FileNotFoundError:
  print("File not found. Please check the file path.")
  exit()
except Exception as e:
  print(f"An error occurred: {e}")

# --- STEP 2: TRANSFORM ---
print("\n--- Cleaning Data ---")

# 1. Remove Duplicates
# We check for duplicates based on Customer_ID and Name to be safe
initial_rows = len(df)
df.drop_duplicates(inplace=True)
print(f"Removed {initial_rows - len(df)} duplicate rows.")

# 2. Handle Null Values
# Fill missing names with "Unknown" and missing emails with "No Email"
df['Name'] = df['Name'].fillna('Unknown')
df['Email'] = df['Email'].fillna('No Email')
print("Null values handled.")

# 3. Standardize Dates
# We define a helper function to handle the messy formats
def clean_date(date_str):
  try:
    # pd.to_datetime is powerful. "errors='coerce'" turns unparseable data (like 'Not available') into NaT (Not a Time)
    # format='mixed' allows pandas to guess different formats in the same column
    return pd.to_datetime(date_str, format='mixed',dayfirst=True)
  except:
    return None

# Apply the cleaning function
df['Join_Date'] = df['Join_Date'].apply(clean_date)
print("Dates standardized.")

# Drop rows where the date could not be parsed (optional, depending on business logic)
# Here, we will fill invalid dates with today's date or a placeholder, but let's just drop nulls for this exercise
df = df.dropna(subset=['Join_Date'])

# Convert to ISO format string (YYYY-MM-DD) for the final report
df['Join_Date'] = df['Join_Date'].dt.strftime('%Y-%m-%d')

# 4. Clean Phone Numbers
# Goal: Remove anything that isn't a digit (parentheses, dots, dashes, spaces)
def clean_phone(phone_str):
  if pd.isna(phone_str) or phone_str == 'Unknown':
    return "Unknown"
  # Regex: \D matches any non-digit character. We replace them with an empty string.
  return re.sub(r'\D', '',str(phone_str))
df['Phone'] = df['Phone'].apply(clean_phone)

# --- STEP 3: LOAD ---
print("\n--- Saving Data ---")

# Generate filename with today's date
today_str = datetime.now().strftime('%Y-%m-%d')
output_file = f"/content/drive/MyDrive/Colab Notebooks/DEProjects/cleaned_data_{today_str}.xlsx"

print(f"Saving cleaned data to {output_file}")
print("\n--- Final Data Preview ---")
print(df.head(10))
df.to_excel(output_file, index=False)
print("Data saved successfully!")
