import json
import sys
import math


def load_data(filepath):
    try:
        return json.load(filepath)
    except ValueError:
        print("Это не JSON")


def get_biggest_bar(bars):
    return max(bars["features"], key=lambda x: x["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(bars):
    return min(bars["features"], key=lambda x: x["properties"]["Attributes"]["SeatsCount"])


def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


def get_closest_bar(bars, longitude, latitude):
    return min(bars["features"], key=lambda x: distance(x["geometry"]["coordinates"], [longitude, latitude]))


def print_biggest_bar(bar):
    print("Самый большой бар Москвы: "+bar["properties"]["Attributes"]["Name"])


def print_smallest_bar(bar):
    print("Самый маленький бар Москвы: "+bar["properties"]["Attributes"]["Name"])


def print_closest_bar(bar):
    print("Ближайший бар Москвы по заданным координатам: "+bar["properties"]["Attributes"]["Name"])


if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'r') as input_file:
            json_data = load_data(input_file)
            if json_data != None:
                print_biggest_bar(get_biggest_bar(json_data))
                print_smallest_bar(get_smallest_bar(json_data))
                print_closest_bar(get_closest_bar(json_data, float(sys.argv[2]), float(sys.argv[3])))
    except IndexError:
        print("Вы не ввели имя файла")
    except IOError:
        print("Такого файла не существует")

