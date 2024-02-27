# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import json

bus_list = []


def add_route(origin, destin, hours, minutes, bus_type, original_time_table,
              start_time_increment, time_table_increment, station_num, start_range, end_range):
    copy_time_table = original_time_table
    for i in range(start_range, end_range + 1):
        minutes += start_time_increment[i - start_range]
        hours += minutes // 60
        minutes %= 60
        copy_time_table[-1] = copy_time_table[-1] + time_table_increment[i - start_range]
        print(copy_time_table)
        data = {
            "id": str(i),
            "from": origin,
            "to": destin,
            "startHour": hours,
            "startMin": minutes,
            "timeTable": copy_time_table.copy(),
            "type": bus_type,
            "stationNum": station_num
        }
        bus_list.append(data)


add_route("东区", "高新", 6, 50, "weekday",
    [10, 0, 40],
    [0, 70, 290, 100, 240, 170, 45],
    [0, 10, -10, 5, 5, -20, 15],
    4, 1, 7
)

add_route("高新", "东区", 6, 40, "weekday",
    [5, 0, 40],
    [0, 80, 95, 195, 100, 240, 215],
    [0, 5, -5, 0, 10, 0, -10],
    4, 8, 14
)

add_route("东区", "高新", 7, 00, "weekend",
    [10, 0, 40],
    [0, 350, 340, 200],
    [0, 0, 0, 10],
    4, 15, 18
)

add_route("高新", "东区", 8, 00, "weekend",
    [5, 0, 45],
    [0, 340, 140, 350],
    [0, 0, 0, 0],
    4, 19, 22
)

add_route("东区", "西区", 7, 25, "all",
    [0, 10],
    [0, 250, 115, 240, 70, 155],
    [0, 0, 0, 0, 0, 0],
    3, 23, 28
)

add_route("东区", "西区", 9, 20, "weekday",
    [0, 10],
    [0, 15, 165, 190, 20, 120, 140, 120],
    [0, 0, 0, 0, 0, 0, 0, 0],
    3, 29, 36
)

add_route("西区", "东区", 7, 35, "all",
    [0, 10],
    [0, 250, 115, 240, 70, 155],
    [0, 0, 0, 0, 0, 0, 0, 0],
    3, 37, 42
)

add_route("西区", "东区", 9, 30, "weekday",
    [0, 10],
    [0, 15, 165, 190, 20, 120, 140, 120],
    [0, 0, 0, 0, 0, 0, 0, 0],
    3, 43, 50
)

add_route("东区", "南区", 11, 45, "all",
    [15],
    [0, 360, 75, 155],
    [0, 0, 0, 0],
    2, 51, 54
)

add_route("南区", "东区", 7, 30, "all",
    [15],
    [0, 370, 335, 155],
    [0, 0, 0, 0],
    2, 55, 58
)

add_route("东区", "南区", 7, 35, "weekday",
    [15],
    [0, 55, 185, 30, 35, 110, 175, 45, 140, 120],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    2, 59, 68
)

add_route("南区", "东区", 7, 10, "weekday",
    [15],
    [0, 50, 30, 30, 180, 80, 40, 70, 190, 145, 120],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    2, 69, 79
)

add_route("西区", "南区", 11, 35, "all",
    [0, 20],
    [0, 360, 75, 165],
    [0, 0, 0, 0],
    3, 80, 83
)

add_route("南区", "西区", 7, 30, "all",
    [0, 20],
    [0, 370],
    [0, 0],
    3, 84, 85
)

add_route("西区", "南区", 7, 35, "weekday",
    [0, 20],
    [0, 295, 330, 140, 120],
    [0, 0, 0, 0, 0],
    3, 86, 90
)

add_route("南区", "西区", 7, 10, "weekday",
    [0, 20],
    [0, 50, 30, 30, 260, 40, 70],
    [0, 0, 0, 0, 0, 0, 0],
    3, 91, 97
)

bus_data = {
    "update_time": "20231120",
    "buses": bus_list
}

json_data = json.dumps(bus_data, indent=4)

with open("bus_data.json", "w") as json_file:
    json_file.write(json_data)





# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
