import pyarrow as pa
import pandas as pd
import vaex
import numpy as np

import pdb

from pyspark.sql import SparkSession
import sys
sys.path.append("/Users/chihwei/playground/design_patten_study")
from lib.tool import start_end, timeit

#project_home="/".join(f"{os.getcwd()}/".split('/')[:-2])

@timeit
@start_end
def generate_pyspark_dataframe(n=1000):
    
    spark_session = SparkSession.builder.master("local[2]")\
                        .appName("read data into spark dataframe").getOrCreate()
     
    col_1 = [np.random.randint(123) for x in range(n)]
    col_2 = [np.random.randint(12312) for x in range(n)]
    cols = ["col1", "col2"]

    return spark_session.createDataFrame(data=zip(col_1, col_2), schema=cols)

class SparkDataFrame:
    def __init__(self, data):
        self.data = data

    @timeit
    @start_end
    def to_arrow_object(self):
        return self.data._collect_as_arrow()


class ArrowOption(SparkDataFrame):
    def __init__(self, data):
        #super().__init__(data)
        SparkDataFrame.__init__(self, data)
        self.data = data
    def to_arrow_table(self):
        arrow_object = self.to_arrow_object()
        return pa.Table.from_batches(arrow_object)


if __name__ == "__main__":

    data = generate_pyspark_dataframe()
    arrow_talbe = ArrowOption(data).to_arrow_table()
    print(arrow_talbe)
