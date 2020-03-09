import Download
import datetime

def Update(endDate, dataframe):
    startDate = max(dataframe.index)
    delta = endDate - startDate
    if delta.days < 0:
        endDate,startDate = startDate,endDate
    else:
       if delta.days==0:
           endDate=startDate+datetime.timedelta(days=2)
    new_data = Download.download(startDate,endDate)
    return dataframe.append(new_data).sort_index()
