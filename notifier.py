import json
import datetime
from twilio.rest import Client
from tfl_api import TflApi
from messenger import Messenger

class Notifier(object):
    def run(self):
        self.tfl_api = TflApi()

    def get_route_and_direction(self):
        self.route = input("Please enter your desired bus route: ")
        self.direction = input("Are you travveling inbound (i) or outbound (o): ")
        if self.direction == "i":
            self.direction = "inbound"
        elif self.direction == "o":
            self.direction = "outbound"
        self.time_to_leave = input("When would yo like to leave (HH:MM): ")
        self.notify_minutes = int(input("How many minutes notification is required: "))

    def get_stops_data(self):
        self.stops = self.tfl_api.get_all_stops(self.route, self.direction)
        for stop in self.stops:
            print(str(stop["index"] + ". " + stop["stop_name"] + "      " + stop["stop_id"]))
        self.chosen_stop_index = int(input("Please pick a stop number: ")) - 1

    def get_bus_data(self):
        self.bus_data = self.tfl_api.fetch_bus_data_for_route((self.stops[self.chosen_stop_index]["stop_id"]), self.route)
        self.arrival_times = self.tfl_api.format_bus_data(self.bus_data)
        self.show_bus_times = self.tfl_api.display_bus_times(self.arrival_times)


    def write_user_data(self):
        user_data = {"route": self.route, "direction": self.direction, "chosen_stop_index": self.chosen_stop_index, "time_to_leave": self.time_to_leave, "notify_window": self.notify_minutes}
        with open('data.txt', 'w') as outfile:
            json.dump(user_data, outfile)

running = Notifier()
running.run()
running.get_route_and_direction()
running.get_stops_data()
running.get_bus_data()
running.write_user_data()

