import logging

from binance import BinanceClient
#from bitmex import BitmexClient

from root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("ZCcvS2KkixH0029MvXud1LVjhEy7xZijqDTT3ojQKYrqm8CYqCVpqKKQFCRBor3b",
                            "4pcxRxYKup2RYqXbhErhh2Qs2m3K7uGt5eiSg5aaL91xaWuJCw3Xth8AJ7waTLVJ",
                            testnet=False, futures=True)
#    bitmex = BitmexClient("", "", testnet=False)

    root = Root(binance)
    root.mainloop()
