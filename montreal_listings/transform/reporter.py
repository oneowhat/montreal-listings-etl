import logging

class Reporter:
    def __init__(self, data_frame):
        self._df = data_frame
        
    def create_report(self):
        """
        Creates a report from the DataFrame.
        
        Parameters:
        None
        
        Returns:
        None
        """
        
        report = self._df.groupby('neighbourhood').agg(
            number_of_listings=('id', 'count'),
            mean_price=('price', 'mean'),
        ).sort_values('number_of_listings', ascending=False)
        
        report.reset_index(inplace=True)
        
        return report