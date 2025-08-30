import os
import logging

def setup_logging(log_file='app.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def load_config(config_file='config.json'):
    if not os.path.exists(config_file):
        logging.error(f"Configuration file {config_file} not found.")
        return None
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def save_to_csv(dataframe, file_path):
    try:
        dataframe.to_csv(file_path, index=False)
        logging.info(f"Data saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data to {file_path}: {e}")

def load_from_csv(file_path):
    try:
        dataframe = pd.read_csv(file_path)
        logging.info(f"Data loaded from {file_path}")
        return dataframe
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {e}")
        return None