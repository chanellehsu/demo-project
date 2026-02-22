import pandas as pd

# Create a DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "Dave"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "LA", "Chicago", "Houston"],
}

df = pd.DataFrame(data)
df
