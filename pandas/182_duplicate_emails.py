import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    # Use duplicated() to find rows with duplicate emails.
    df = person[person.duplicated(subset=['email'])]

    # Keep only the email column and remove duplicate email values.
    df = df[['email']].drop_duplicates()

    # Rename the column to "Email".
    df.columns = ['Email']

    # Return the final DataFrame.
    return df
