# Reading Datasets
data1 = pd.read_csv(eurovision1.csv)
data2 = pd.read_csv(eurovision2.csv)
data3 = pd.read_csv(eurovision3.csv)
data4 = pd.read_csv(eurovision4.csv)
data5 = pd.read_csv(eurovision5.csv)
data6 = pd.read_csv(eurovision6.csv)
data7 = pd.read_csv(eurovision7.csv)
data8 = pd.read_csv(eurovision8.csv)

# Datasets before the Eurovision final
twitterDataBefore = pd.concat([data1, data2, data3, data4], ignore_index=True)

# Datasets after the Eurovision final
twitterDataAfter = pd.concat([data5, data6, data7, data8], ignore_index=True)
