import pymongo
from data_service import DataServiceTushare
from vnpy.trader.constant import Exchange


if __name__ == "__main__":
    ds_tushare = DataServiceTushare()
    ds_tushare.buildStockData(update=True)
    # ds_tushare._build_top_list()
