import requests
import json

headers = {'token': 'lFKjAdkCxPvzLTAopCafnSgcDijjVHyW'}
dataset = 'GHCND'
location = 'CITY:US360019' # New York
startdate = '2010-05-01'
enddate = '2010-05-31'
datatype = 'TMAX,TMIN'
datacategory = 'TOBS'
units = 'metric'
limit = 1000

url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?'
url += f'datasetid={dataset}'
url += f'&datatypeid={datatype}'
# url += f'datacategoryid={datacategory}'
url += f'&locationid={location}'
url += f'&units={units}'
url += f'&startdate={startdate}'
url += f'&enddate={enddate}'
url += f'&limit={limit}'

# lookup city id
# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc&limit=1000'

# all datatypes related to TEMP
# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datacategoryid=TEMP&limit=56'

# example url
# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=CITY:US360019&units=metric&startdate=2010-05-01&enddate=2010-05-31&limit=1000'

# different sources of data
# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets'

# limiting data
# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datacategoryid=TEMP&limit=1000'

# different categories
# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?limit=41'

# all datasets that contain TOBS (temperature at time of observation)
# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets?datatypeid=TOBS'

res = requests.get(url, headers=headers)
if (res.status_code != 200):
	raise(Exception(f"Request Unsuccessful {res}"))
data = json.loads(res.text)
