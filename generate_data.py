import pandas as pd
import numpy as np

# Create a dictionary with messy data
data = {
    'Customer_ID': ['1001', '1002', '1003', '1004', '1002', '1005', '1006'],
    'Name': ['Alice Smith', 'Bob Jones', 'Charlie', 'David Brown', 'Bob Jones', np.nan, 'Frank White'],
    'Join_Date': ['15-01-2023', '02/20/2023', '2023.03.10', '05-04-2023', '02/20/2023', '01/01/2023', 'Not available'],
    'Phone': ['(555) 123-4567', '555.987.6543', '555 111 2222', 'Unknown', '555.987.6543', '555-000-0000', '555-123-4567'],
    'Email': ['alice@example.com', 'bob@example.com', np.nan, 'david@example', 'bob@example.com', 'eve@example.com', 'frank@example.com']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('/content/drive/MyDrive/Colab Notebooks/DEProjects/customer_dump.csv', index=False)
print("Dirty data file 'customer_dump.csv' created successfully!")
