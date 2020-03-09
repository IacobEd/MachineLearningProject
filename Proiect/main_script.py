#from _pickle import cPickle 
from datetime import timedelta, datetime
from dateutil.tz import tzutc
import Download
import dtFeatures
from train_Data import train

date_start = datetime(2019,1,3,0,0,tzinfo=tzutc())
date_end = date_start+timedelta(days=2)

data=Download.download(date_start,date_end)
dtFeatures.dateTime_features(data,date_start,date_end)
path = r'C:\Users\Iacob\Desktop\ProiectStrongBytes'
name = "WindCSV"
dtFeatures.exportCSV(data,path,name)

print(data.head(10))