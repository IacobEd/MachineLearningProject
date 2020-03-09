from datetime import timedelta

def dateTime_features(dataFrame,date_start,date_end):
    date_end=date_end+timedelta(days=4)
    
    dataFrame['month'] = dataFrame.index.month
    dataFrame['day'] = dataFrame.index.day
    dataFrame['year'] = dataFrame.index.year
    dataFrame['quarter'] = dataFrame.index.quarter
    dataFrame['hour'] = dataFrame.index.hour
    dataFrame['dayofweek'] = dataFrame.index.dayofweek
    dataFrame['weekofyear'] = dataFrame.index.weekofyear
    
    dataFrame['wind'] = dataFrame['wind'].astype('int64')
    dataFrame['solar'] = dataFrame['wind'].astype('int64')
    dataFrame['biomass'] = dataFrame['wind'].astype('int64')
    dataFrame['coal'] = dataFrame['wind'].astype('int64')
    
    return dataFrame


def exportCSV(data,path,nameCSV):
    data.to_csv (path+'\\'+nameCSV, index = None, header=True)
    
