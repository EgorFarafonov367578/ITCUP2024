import pandas as pd
import numpy as np
pd.read_csv("~/ITCUP2024/ITCUP2024/data_source/pos_general.csv")['pos_sales_with_tax'].plot(kind='hist',bins=20).draw()