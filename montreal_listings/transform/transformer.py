import logging 

class Transformer:
    def __init__(self, data_frame, neighborhoods):
        self._df = data_frame
        self._neighborhoods = neighborhoods

    def transform(self):
        """
        Transforms the DataFrame by removing unnecessary 
        columns and rows and performing validation.
        
        Parameters:
        None
        
        Returns:
        pandas.DataFrame: The transformed DataFrame.
        """
        
        self._drop_empty_columns()
        self._with_logging_length(self._remove_zero_reviews, 'listings with zero reviews')
        self._with_logging_length(self._remove_minimum_nights_too_high, 'listings with minimum nights greater than 31')
        self._with_logging_length(self._remove_complete_duplicates, 'complete duplicates')
        self._with_logging_length(self._remove_partial_duplicates, 'partial duplicates')
        self._with_logging_length(self._remove_invalid_neighborhoods, 'listings with invalid neighborhoods')
    
        return self._df
    
    def _drop_empty_columns(self):
        """
        Drops columns with all missing values.
        
        Parameters:
        None
        
        Returns:
        None
        """
        
        column_names = self._df.columns
        
        # Remove columns with all missing values
        self._df.dropna(axis='columns', how='all', inplace=True)
        
        new_column_names = self._df.columns
        
        # Log the columns that were removed
        removed_columns = set(column_names) - set(new_column_names)
        logging.info(f'Removed columns: {removed_columns}.')
        
    def _remove_zero_reviews(self):
        """
        Removes listings with zero reviews.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self._df = self._df[self._df['number_of_reviews'] > 0]
        
    def _remove_minimum_nights_too_high(self):
        """
        Removes listings with minimum nights greater than 31.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self._df = self._df[self._df['minimum_nights'] <= 31]
        
    def _remove_complete_duplicates(self):
        """
        Removes complete duplicates from the DataFrame.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self._df.drop_duplicates(inplace=True)
        
    def _remove_partial_duplicates(self):
        """
        Removes complete duplicates from the DataFrame.
        
        Parameters:
        None
        
        Returns:
        None
        """
        
        # Merge partial duplicates
        self._df = self._df.groupby('id').agg({
            'name': 'first',
            'neighbourhood': 'first', 
            'host_name': 'first',
            'latitude': 'first',
            'longitude': 'first',
            'room_type': 'first', 
            'price': 'mean',
            'minimum_nights': 'mean', 
            'number_of_reviews': 'mean', 
            'last_review': 'max', 
            'reviews_per_month': 'mean',
            'calculated_host_listings_count': 'max',
            'availability_365': 'min', 
            'number_of_reviews_ltm': 'mean',
            'license': 'first',
            }).reset_index()
        duplicates = self._df.duplicated(subset='id', keep=False)
        duplicated_listings = self._df[duplicates].sort_values(by='id')
        if len(duplicated_listings) > 0:
            logging.warning(f'Duplicate listings found: {duplicated_listings}')
        
    def _remove_invalid_neighborhoods(self):
        """
        Removes listings with invalid neighborhoods.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self._df = self._df[self._df['neighbourhood'].isin(self._neighborhoods)]
        
    def _with_logging_length(self, func, message):
        """
        Logs messages before and after calling a function.
        
        Parameters:
        func (function): The function to call.
        message (str): The message to log.
        
        Returns:
        None
        """
        length_before = len(self._df)
        func()
        length_after = len(self._df)
        logging.info(f'Removed {length_before - length_after} rows: {message}')
        