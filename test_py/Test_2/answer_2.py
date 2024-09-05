import sys
import math

# Функция для определения положения точки относительно окружности
def point_position(circle_x, circle_y, radius, point_x, point_y):
    distance = math.sqrt((point_x - circle_x) ** 2 + (point_y - circle_y) ** 2)
    if distance == radius:
        return 0  # Точка лежит на окружности
    elif distance < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Чтение данных из файла с координатами окружности и радиусом
    with open(circle_file, 'r') as f:
        circle_data = f.readlines()
        circle_x, circle_y = map(float, circle_data[0].split())
        radius = float(circle_data[1])

    # Чтение данных из файла с координатами точек
    with open(points_file, 'r') as f:
        points_data = f.readlines()

    # Обработка каждой точки
    for line in points_data:
        point_x, point_y = map(float, line.split())
        result = point_position(circle_x, circle_y, radius, point_x, point_y)
        print(result)

if __name__ == "__main__":
    main()
