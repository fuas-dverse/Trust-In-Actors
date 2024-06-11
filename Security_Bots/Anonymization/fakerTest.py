import pandas as pd
from faker import Faker
from sklearn.preprocessing import MinMaxScaler

# Initialize Faker library
fake = Faker()

# Define a function to anonymize a DataFrame
def anonymize_df(df):
    # Anonymize "pk" field
    df["pk"] = [fake.uuid4() for _ in range(len(df))]

    # Anonymize "name" field
    df["name"] = [fake.name() for _ in range(len(df))]

    # Anonymize "description" field
    df["description"] = [fake.text(max_nb_chars=100) for _ in range(len(df))]

    # Anonymize "topics" field
    df["topics"] = [fake.words(nb=5, unique=True) for _ in range(len(df))]

    # Anonymize "output_format" field
    df["output_format"] = [fake.file_extension() for _ in range(len(df))]

    # Anonymize "is_active" field
    df["is_active"] = [fake.boolean() for _ in range(len(df))]

    # Anonymize "embeddings" field
    scaler = MinMaxScaler()
    # df["embeddings"] = list(scaler.fit_transform(df["embeddings"].tolist()))

    return df

# Assume that df is the DataFrame that contains the data
df = pd.read_csv("data.csv",delimiter=";")

# Anonymize the DataFrame
df = anonymize_df(df)

# Save the anonymized DataFrame to a new CSV file
df.to_csv("anonymized_data.csv", index=False,sep=";")

# Print a success message
print("The data was successfully anonymized and saved to anonymized_data.csv")
