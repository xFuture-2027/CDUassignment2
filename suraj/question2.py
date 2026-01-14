import glob
import statistics
import csv

# season and corresponding months defined
SEASONS ={
    'Summer': ['December', 'January','February'],
    'Autumn': ['March','April','May'],
    'Winter': ['June','July','August'],
    'Spring':['September','October','November']

}

def main():
    # store data temporarily
    all_season_temps = {s: [] for s in SEASONS}
    station_temps = {}

    # read all the CSV files in the 'Temperatures' folder and perform the following tasks
    for file_name in glob.glob('temperatures/*.csv'):
        with open(file_name,'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                station = row['STATION_NAME'].strip()
                if station not in station_temps:
                    station_temps[station]=[]
                
                # go through each month in the row
                for season,months in SEASONS.items():
                    for month in months:
                        if month in row and row[month].strip():
                            try:
                                temp = float(row[month])
                                all_season_temps[season].append(temp)
                                station_temps[station].append(temp)
                            except ValueError:
                                continue #skip NaNs or any invalid numbers
                
    # 1. Season Average
    with open('average_temp.txt','w') as f:
        for season in ['Summer','Autumn','Winter','Spring']:
            if all_season_temps[season]:
                avg = statistics.mean(all_season_temps[season])
                f.write(f"{season}: {avg:.1f}°C\n")
    
    # 2. Temperature Range
    largest_range_stations=[]
    max_range = -1

    #3. Stability
    station_stdevs ={}

    for station,temps in station_temps.items():
        if not temps: continue
    
    # Range
    rnge = max(temps) - min(temps)
    if rnge > max_range:
        max_range = rnge
        largest_range_stations = [(station,rnge,max(temps),min(temps))]
    elif rnge == max_range:
        largest_range_stations.append((station,rnge,max(temps),min(temps)))
c
    # stability
    if len(temps)>1:
        station_stdevs[station] = statistics.stdev(temps)
    
    with open('largest_temp_range_station.txt','w') as f:
        for s, r, mx, mn in largest_range_stations:
            f.write(f"Station {s}:Range {r:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")
    
    with open('temperature_stability_station.txt','w') as f:
        if station_stdevs:
            min_std = min(station_stdevs.values())
            max_std = max(station_stdevs.values())

            # find and write most stable
            for s, sd in station_stdevs.items():
                if sd == min_std:
                    f.write(f"Most Stable: Station {s}:Stdev {sd:.1f}°C\n")
            
            # find and write most variable
            for s, sd in station_stdevs.items():
                if sd == max_std:
                    f.write(f"Most Variable: Station{s}:Stdev {sd:.1f}°C\n")
            
if __name__ == '__main__':
    main()