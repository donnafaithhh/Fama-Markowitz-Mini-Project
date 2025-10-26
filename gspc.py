import yfinance
import pandas as pd
import time
import pickle
from datetime import datetime, timedelta
import math

# getting closing prices for the 30 stocks with batching
start_date = '2022-08-31'
end_date = '2025-08-31'

def download_stocks_in_batches(tickers, batch_size=5, delay=1):
    """
    Download stock data in batches to avoid rate limiting
    """
    all_data = {}
    
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        print(f"Downloading batch {i//batch_size + 1}: {batch}")
        
        try:
            # Download the batch
            batch_data = yf.download(
                batch,
                start=start_date,
                end=end_date,
                progress=False
            )
            
            # Extract closing prices for this batch
            if not batch_data.empty and 'Close' in batch_data.columns:
                closes = batch_data['Close']
                # Handle single ticker case (returns Series instead of DataFrame)
                if isinstance(closes, pd.Series):
                    all_data[batch[0]] = closes
                else:
                    for ticker in closes.columns:
                        all_data[ticker] = closes[ticker]
                print(f"Successfully downloaded {len(batch)} stocks")
            else:
                print(f"No data returned for batch: {batch}")
            
        except Exception as e:
            print(f"Error downloading batch {batch}: {e}")
        
        # Add delay between batches to avoid rate limiting
        if i + batch_size < len(tickers):
            print(f"Waiting {delay} seconds before next batch...")
            time.sleep(delay)
    
    # Combine all data into a single DataFrame
    if all_data:
        return pd.DataFrame(all_data)
    else:
        return pd.DataFrame()

gspc_data = download_stocks_in_batches(['^GSPC'], batch_size = 1, delay=15)

# import yfinance as yf

# ticker_symbol = "^GSPC"
# # sp500_data = yf.download(ticker_symbol, start=start_date, end=end_date)
# spx = yf.download("^gspc", start=start_date, end=end_date)

if not gspc_data.empty:
    gspc_data.to_pickle('gspc prices.pkl')