import requests
import re


class TflApi(object):

    def __init__(self):
        pass

    def get_all_stops(self, route, direction):
        count = 0
        all_stops= []
        route_inbound = requests.get("https://api.tfl.gov.uk/Line/" + str(route) + "/Route/Sequence/" + str(direction), verify=False).json()
        print(route_inbound)
        stop_ids = route_inbound["orderedLineRoutes"][0]["naptanIds"]
        stops = route_inbound["stopPointSequences"][0]["stopPoint"]
        for index, stop in enumerate(stops):
            index = str(index + 1)
            stop_name = stop["name"]
            current_stop = {"index" : index, "stop_name" : stop_name, "stop_id": stop_ids[count]}
            all_stops.append(current_stop)
            count += 1
        return(all_stops)

    def fetch_bus_data_for_route(self, stop_id, route):
        all_bus_data = requests.get("https://api.tfl.gov.uk/StopPoint/" + stop_id + "/Arrivals").json()
        bus_data_for_route = []
        for item in all_bus_data:
            current_arrival_time = item["expectedArrival"]
            current_arrival_seconds = item["timeToStation"]
            current_bus = {"arrival_time" : current_arrival_time, "seonds" : current_arrival_seconds}
            bus_data_for_route.append(current_bus)
        return bus_data_for_route

    def format_bus_data(self, bus_data):
        arrival_times = []
        for item in bus_data:
                time = item["arrival_time"]
                seconds = item["seonds"]
                minutes = '%.1f' % round((seconds / 60), 1)
                time = re.findall(r'(?<=T).*?(?=Z)', time)[0]
                time = time[:-3]

                current_bus_info = {
                    "arrival_time": time,
                    "arrival_seconds": seconds,
                    "arrival_minutes": minutes
                }
                arrival_times.append(current_bus_info)

        return sorted(arrival_times, key=(lambda d: d["arrival_seconds"]))

    def display_bus_times(self, arrival_times):
            for bus in arrival_times:
                print("Upcoming bus at: " + str(bus["arrival_time"]) + " Estimated " + str(
                bus["arrival_minutes"]) + " Minutes away")
    

