from datetime import datetime
object_collection = {}
template_collection = {}
# index:{start:'', end:''}
object_points = []
template_points = []

def convert_to_int(string):
    result = ""
    for item in string:
        try:
            result += str(int(item))
        except ValueError:
            pass
    if result == '':
        return 0
    return int(result)

object_start_time = datetime.strptime("2017-04-28 04:56:34,028", '%Y-%m-%d %H:%M:%S,%f')
template_start_time = datetime.strptime("2017-04-28 04:56:34,035", '%Y-%m-%d %H:%M:%S,%f')

with open('worker.log', 'r') as f:
    data = f.readlines()
for item in data:
    date = datetime.strptime(item.split(';')[1], '%Y-%m-%d %H:%M:%S,%f')
    message = item.split(';')[3]
    if 'requested' in message:
        object_collection[convert_to_int(message[:5])] = {'start': date}
    elif 'completed' in message:
        object_collection[convert_to_int(message[:5])]['end'] = date
    elif 'Started' in message:
        template_collection[convert_to_int(message[:5])] = {'start': date}
    elif 'Ended' in message:
        template_collection[convert_to_int(message[:5])]['end'] = date
    else:
        raise ValueError('Wrong data in log')
### Total: 777 data, range: 111, points: 7
# 0 point:
item = template_collection[2]
template_points.append((item['end']-item['start']).total_seconds())
item = object_collection[1]
object_points.append((item['end']-item['start']).total_seconds())
# remove recorded data
# del(template_collection[2])
# del(object_collection[1])
# iterate other points
diff = 0.0
counter = 1
# for item in template_collection:
#     diff += (template_collection[item]['end'] - template_collection[item]['start']).total_seconds()
#     if not (counter % 112):
#         template_points.append(diff/111)
#         print((template_collection[item]['start'] - template_start_time).total_seconds())
#         counter = 1
#         diff = 0.0
#     else:
#         counter += 1
# if counter:
#     # Add remaining
#     template_points.append(diff/counter)
#     print((template_collection[item]['start'] - template_start_time).total_seconds())
for item in object_collection:
    diff += (object_collection[item]['end'] - object_collection[item]['start']).total_seconds()
    if not (counter % 112):
        object_points.append(diff/111)
        print((object_collection[item]['start'] - object_start_time).total_seconds())
        counter = 1
        diff = 0.0
    else:
        counter += 1
if counter:
    # Add remaining
    object_points.append(diff/counter)
    print((object_collection[item]['start'] - object_start_time).total_seconds())

print("|_____|")
print(object_points)
print("|_____|")
print(template_points)
print("|-----|")
