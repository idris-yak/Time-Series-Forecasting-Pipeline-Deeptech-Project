import pandas as pd
import os
import logging
from prophet import Prophet
import matplotlib.pyplot as plt

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

INPUT_PATH = os.path.join("data", "processed.csv")
OUTPUT_PATH = os.path.join("data", "forecast.csv")


def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        logging.info("Processed data loaded")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise


def train_model(df: pd.DataFrame) -> Prophet:
    model = Prophet()
    model.fit(df)
    logging.info("Model training complete")
    return model


def make_forecast(model: Prophet, periods: int = 30) -> pd.DataFrame:
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    logging.info("Forecast generated")
    return forecast


def save_forecast(forecast: pd.DataFrame):
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(OUTPUT_PATH, index=False)
    logging.info(f"Forecast saved to {OUTPUT_PATH}")


def plot_forecast(model: Prophet, forecast: pd.DataFrame):
    fig = model.plot(forecast)
    plt.title("Sales Forecast")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()


def main():
    logging.info("Starting forecasting process")

    df = load_data(INPUT_PATH)

    model = train_model(df)
    forecast = make_forecast(model)

    save_forecast(forecast)
    plot_forecast(model, forecast)


if __name__ == "__main__":
    main()
