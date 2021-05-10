# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:07:25 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler

class StockEtfFundsIndexFundamentalData(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        # base URL's of the API
        self.URL_FUNDAMENTAL = 'https://eodhistoricaldata.com/api/fundamentals/'
        self.URL_BULK_FUNDAMENTALS = 'http://eodhistoricaldata.com/api/bulk-fundamentals/'
        super().__init__(api_key, timeout)
        
    def get_fundamentals(self, symbol:str, **query_params):
        """
        Get fundamental data for the requested stock, etf, fund or index.

        Parameters
        ----------
        symbol : str
            name of the stock to analyse, consists of two parts: {SYMBOL_NAME}.{EXCHANGE_ID}.
        **query_params :
            query parameters.

        Returns
        -------
        dict
            fundamental data.

        """
        self.endpoint = self.URL_FUNDAMENTAL + symbol.upper()
        return super().handle_request(self.endpoint, query_params)
    
    def get_bulk_fundamentals(self, symbol:str, **query_params):
        """
        With this endpoint you able to download fundamental data for thousands 
        of companies in one request. It supports only stocks and doesn’t 
        support ETFs and Mutual Funds, these types of assets will be 
        implemented later.
        
        It doesn’t work for entire US exchange, instead of it you should request
        each exchange separately,  at the moment we do support: NASDAQ, 
        NYSE (or ‘NYSE MKT’), BATS, and AMEX. 
        
        All non-US exchanges supported as is.

        Parameters
        ----------
        symbol : str
            name of the exchange to analyse.
        **query_params :
            query parameters.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        self.endpoint = self.URL_BULK_FUNDAMENTALS + symbol.upper()
        return super().handle_request(self.endpoint, query_params)