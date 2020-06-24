from wwo_hist import retrieve_hist_data

API_KEY = '62c4f496efb147c1b2160953202406'

frequency = 24
start_date = '01-JAN-2020'
end_date = '22-JUN-2020'
api_key = API_KEY
county_list = ['Cook', 'Los Angeles', 'Queens', 'Kings', 'Bronx', 'Nassau', 'Suffolk', 'Westchester']
location_list = ['60120','90012','11365','11217','10453','12123','23433','10502']
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)