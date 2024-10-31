import pandas as pd

foundation = "D:\git\intensive_first\result.csv"


data = pd.read_csv(foundation)
data = data.drop_duplicates()
data.to_csv(foundation, index=False)

uni = pd.read_csv(foundation)
uni = uni.dropna(subset=['author_type', 'location', 'floors_count', 'rooms_count', 'total_meters', 'price', 'district'])
uni.to_csv(foundation, index=False)

uni = pd.read_csv(foundation)
uni = uni.loc[uni['author_type'] != 'unknown']



uni.to_csv(foundation, index=False)

uni = pd.read_csv(foundation)
uni['underground'].fillna('not available', inplace=True)
uni.to_csv(foundation, index=False)


data = pd.read_csv(foundation)

def metro(row):
    if row['underground'] == 'not available': return False
    return True

def meters(row):
    return round(row['price']/row['total_meters'])

data['availability_underground'] = data.apply(metro, axis=1)
data['price_per_meter'] = data.apply(meters, axis=1)
data.to_csv(foundation, index=False)



res = "D:\git\intensive_first\result.csv"


uni = pd.read_csv(foundation)
total = uni.drop(['street', 'house_number','residential_complex'], axis=1)
total.info()


total.to_csv( res, index=False, encoding='utf-8-sig')