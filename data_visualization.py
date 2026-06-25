import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["Aman", "Rahul", "Priya", "Sneha"],
    "Marks": [85, 90, 78, 88]
}
df = pd.DataFrame(data)
# Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(
    df["Marks"],
    labels=df["Name"],
    autopct="%1.1f%%"
)
plt.title("Student Marks Distribution - Pie Chart")
plt.show()