import logging
from .extractor import Extractor
from .transform import Transformer
from .transform import Reporter
from .loader import Loader

logging.basicConfig(filename='data/montreal_listing.log', level=logging.INFO)

def run():
    logging.info("Starting the program")
    extractor = Extractor()
    
    df_listings = extractor.extract_csv('data/input/montreal-listings.csv')
    neighbourhoods = extractor.extract_txt('data/input/montreal_neighbourhoods.txt')
    logging.info("Extraction finished")
    
    transformer = Transformer(df_listings, neighbourhoods)
    cleaned_df = transformer.transform()
    
    reporter = Reporter(cleaned_df)
    report = reporter.create_report()
    
    loader = Loader()
    loader.load_listings(cleaned_df, 'data/output/montreal_listings_clean.csv')
    loader.load_report(report, 'data/output/montreal_listings_by_neighbourhood.csv')
    
    logging.info("Program finished")

if __name__ == '__main__':
    run()
