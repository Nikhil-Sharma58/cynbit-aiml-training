import pandas as pd
data = {
    "Name": ["Aman", "Rahul", "Priya", "Sneha"],
    "Age": [20, None, 21, 22],
    "Marks": [85, 90, None, 88]
}
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)
cleaned_df = df.dropna()
print("\nDataset After Removing Null Values:")
print(cleaned_df)