import json
from notifier import get_bus_data

data = json.load(open('data.txt'))

class Updater(object):

    def send_update(self, arrival_times, time_to_leave, data["notify_window"] ):
        next_bus_to_arrive = datetime.datetime.strptime(arrival_times[0]["arrival_time"], '%H:%M')
        time_to_leave_formatted = datetime.datetime.strptime(time_to_leave, '%H:%M')
        notify_delta = datetime.timedelta(seconds=notify_window * 60)
        notify_window = time_to_leave_formatted + notify_delta
        if notify_window == next_bus_to_arrive:
            self.send_reminder(notify_minutes)
        else:
            print("No buses yet, please wait for an update.")