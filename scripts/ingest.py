import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DATA_PATH = os.path.join("data", "sales.csv")


def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        logging.info("Data loaded successfully")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise


def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = ['date', 'sales']

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Convert date column
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop invalid rows
    df = df.dropna(subset=['date', 'sales'])

    # Ensure sales is numeric
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
    df = df.dropna(subset=['sales'])

    logging.info("Data validation successful")
    return df


def main():
    logging.info("Starting ingestion process")

    df = load_data(DATA_PATH)
    df = validate_data(df)

    output_path = os.path.join("data", "raw_cleaned.csv")
    df.to_csv(output_path, index=False)

    logging.info(f"Cleaned data saved to {output_path}")


if __name__ == "__main__":
    main()
