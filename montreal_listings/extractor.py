import logging
import pandas as pd

class Extractor:
    def __init__(self):
        pass
        #self._logger = logger
        
    def extract_csv(self, filepath):
        """
        Extracts data from a CSV file and returns a pandas DataFrame.   
        
        Parameters:
        filepath (str): The path to the CSV file.
        
        Returns:
        pandas.DataFrame: The data from the CSV file.     
        """
        try:
            df = pd.read_csv(filepath)
            logging.info(f"Data extracted from {filepath}")
            return df
        except FileNotFoundError:
            logging.error(f"File not found: {filepath}")
            return None
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return None
        
    def extract_txt(self, filepath):
        """
        Extracts data from a text file and returns a list of strings.   
        
        Parameters:
        filepath (str): The path to the text file.
        
        Returns:
        list: The data from the text file.     
        """
        try:
            with open(filepath, 'r') as file:
                data = file.read().splitlines()
            logging.info(f"Data extracted from {filepath}")
            return data
        except FileNotFoundError:
            logging.error(f"File not found: {filepath}")
            return None
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return None