import parsers.ENTSOE as entsoe
import datetime
import pandas as pd

def get_dataframe(data):
    index = []
    for i in range(len(data)):
        del data[i]['source']
        del data[i]['zoneKey']
        index.append(data[i].pop('datetime'))
        stor = {}
        prod = {}
        try:
            stor = data[i].pop('storage')
        except:
            None
        try:        
            prod = data[i].pop('production')
        except:
            None
        data[i] = {**data[i],**prod,**stor}
    dataframe=pd.DataFrame(data=data,index=index)
    return dataframe[['wind','solar','biomass','coal']]

def download(start,end):  
    delta=end-start
    data=[]
    while delta.days>0:
        if delta.days==3:
            start=start+datetime.timedelta(days=1)
            delta=delta+datetime.timedelta(days=-1)
        else:
            start=start+datetime.timedelta(days=2)
            delta=delta+datetime.timedelta(days=-2)
        data_prod = entsoe.fetch_production('RO', target_datetime = start)

        
        for el in data_prod:
            if el not in data:
                data.append(el)
                
    return get_dataframe(data)

