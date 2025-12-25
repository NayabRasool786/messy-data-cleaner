# ... (Previous code where we filled NaNs) ...

# 5. Validate Email Addresses
# Regex explanation:
# ^          -> Start of string
# [\w\.-]+   -> One or more letters, numbers, dots, or dashes
# @          -> The @ symbol
# [\w\.-]+   -> Domain name (e.g., "gmail")
# \.         -> A literal dot
# [a-zA-Z]+  -> The extension (e.g., "com", "org")
# $          -> End of string

def validate_email(email):
    # Basic email regex pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$'
    
    # Check if the email matches the pattern
    if pd.isna(email) or not re.match(pattern, str(email)):
        return "Invalid Email" # Or you could use np.nan to treat it as null
    return email

# Apply the validation
df['Email'] = df['Email'].apply(validate_email)

print("--- Email Validation Check ---")
print(df[['Name', 'Email']])
