import datetime
import pytz

objd = datetime.datetime.now()
objt = pytz.timezone("America/Los_Angeles")
obja = objt.localize(objd)
print(obja.tzinfo)


