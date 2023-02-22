import pyarrow as pa
import pandas as pd
import vaex
import numpy as np

import pdb

from pyspark.sql import SparkSession
import sys
sys.path.append("/Users/chihwei/playground/design_patten_study") # setup working dir
from lib.tool import start_end, timeit

@timeit
@start_end
def generate_pyspark_dataframe(n=1000):
    """
    Description:
        產生 dummy 資料
    -------------------
    parameter 
       n 
         - type: int
         - desc: data length
    """
    spark_session = SparkSession.builder.master("local[2]")\
                        .appName("read data into spark dataframe").getOrCreate()
     
    col_1 = [np.random.randint(123) for x in range(n)]
    col_2 = [np.random.randint(12312) for x in range(n)]
    cols = ["col1", "col2"]

    return spark_session.createDataFrame(data=zip(col_1, col_2), schema=cols)

class SparkDataFrame:
    """
    Description:
        Spark dataframe 的操作
    """
    def __init__(self, data):
        """
        Description:
            初始化 class 與設定屬性
        -------------------
        parameter:
            - data:
                - type: spark dataframe
                - desc: spark dataframe
        """
        self.data = data

    @timeit
    @start_end
    def to_arrow_object(self):
        """
        Description:
            將 Spark DataFrame 轉換成 apache arrow 的物件
        """
        return self.data._collect_as_arrow()


class ArrowOption(SparkDataFrame):
    """
    Description:
        Apache Arrow 的操作
    """
    def __init__(self, data):
        """
        Description:
            初始化 class 與設定屬性
        -------------------
        parameter:
            - data:
                - type: dataframe
        """
        #super().__init__(data) # super 繼承的方法
        SparkDataFrame.__init__(self, data) # 如果有多個 class 需要繼承
                                            # 可以用這種方式初始化
        self.data = data
    @timeit
    @start_end
    def to_arrow_table(self):
        """
        Description:
            將 Spark dataframe 轉換成 arrow table
        """
        arrow_object = self.to_arrow_object()
        return pa.Table.from_batches(arrow_object)


if __name__ == "__main__":

    data = generate_pyspark_dataframe()
    arrow_talbe = ArrowOption(data).to_arrow_table()
    print(arrow_talbe)
