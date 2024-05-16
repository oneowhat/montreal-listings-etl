import logging

class Loader:
    def __init__(self):
        pass
    
    def load_listings(self, data_frame, filepath):
        """
        Loads the listings DataFrame to a CSV file.
        
        Parameters:
        data_frame (pandas.DataFrame): The DataFrame to be loaded.
        filepath (str): The path to the CSV file.
        
        Returns:
        None
        """
        
        try:
            data_frame.to_csv(filepath, index=False)
            logging.info(f'Cleaned listings saved to {filepath}')
        except Exception as e:
            logging.error(f'An error occurred: {str(e)}')
            
    def load_report(self, report, filepath):
        """
        Loads the report to a text file.
        
        Parameters:
        report (str): The report to be loaded.
        filepath (str): The path to the text file.
        
        Returns:
        None
        """
        
        try:
            report.to_csv(filepath, index=False)
            logging.info(f'Report saved to {filepath}')
        except Exception as e:
            logging.error(f'An error occurred: {str(e)}')