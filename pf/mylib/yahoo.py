from stock_stuff import get_info_on_stock


def create_yahoo_dict_for_stock(symbol):
    stock_thing = get_info_on_stock(symbol)
    #print(stock_thing.info)
    cp = stock_thing.info.get('currentPrice')
    print(symbol, 'Current Price:', cp)
    stock_dict = stock_thing.info  
    return stock_dict


class Yahoo:

    def __init__(self, stock_symbol):
        print('Yahoo Initialized', stock_symbol)
        self.symbol = stock_symbol
        self.stock_dict = create_yahoo_dict_for_stock(self.symbol)
        #print(self.stock_dict)


    def get(self):
        return(self.stock_dict)
