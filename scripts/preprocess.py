import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

INPUT_PATH = os.path.join("data", "raw_cleaned.csv")
OUTPUT_PATH = os.path.join("data", "processed.csv")


def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        logging.info("Data loaded for preprocessing")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Rename columns for Prophet
    df = df.rename(columns={'date': 'ds', 'sales': 'y'})

    # Convert ds to datetime
    df['ds'] = pd.to_datetime(df['ds'])

    # Sort values
    df = df.sort_values('ds')

    logging.info("Transformation complete")
    return df


def handle_missing_dates(df: pd.DataFrame) -> pd.DataFrame:
    # Create full date range
    full_range = pd.date_range(start=df['ds'].min(), end=df['ds'].max())

    df = df.set_index('ds').reindex(full_range).rename_axis('ds').reset_index()

    # Fill missing values (forward fill)
    # df['y'] = df['y'].fillna(method='ffill')
    df['y'] = df['y'].ffill()

    logging.info("Missing dates handled")
    return df


def main():
    logging.info("Starting preprocessing step")

    df = load_data(INPUT_PATH)
    df = transform_data(df)
    df = handle_missing_dates(df)

    df.to_csv(OUTPUT_PATH, index=False)

    logging.info(f"Processed data saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
