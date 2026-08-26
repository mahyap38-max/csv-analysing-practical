import pandas as pd

data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                     111, 112, 113, 114, 115],

    "age": [22, 35, 28, 41, 19, 52, 31, 27, None, 45,
            33, 29, 38, None, 24],

    "gender": ["Female", "Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],

    "monthly_spending": [120, 450, 230, 780, 95, 620, 340, 180,
                         510, 890, 275, 410, 560, 300, 150],

    "purchases": [3, 8, 5, 12, 2, 10, 7, 4, 9, 15,
                  6, 8, 11, 5, 3],

    "satisfaction": [4, 5, 3, 5, 2, 4, 5, 3, None, 5,
                     4, 3, 5, 2, 4]
}

df = pd.DataFrame(data)

# Add an intentional duplicate
df = pd.concat([df, df.iloc[[4]]], ignore_index=True)

# Save as CSV
df.to_csv("customers.csv", index=False)

print("Dataset saved successfully!")