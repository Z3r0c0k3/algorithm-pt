import csv
import random

def generate_random_coordinates(num_points, x_range, y_range):
    """지정된 범위 내에서 랜덤 좌표를 생성합니다."""
    coordinates = []
    for _ in range(num_points):
        x = random.randint(x_range[0], x_range[1])
        y = random.randint(y_range[0], y_range[1])
        coordinates.append((x, y))
    return coordinates

def save_to_csv(coordinates, filename="xyrand.csv"):
    """좌표를 CSV 파일로 저장합니다."""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["x", "y"])  # 헤더 추가
        for x, y in coordinates:
            writer.writerow([x, y])

if __name__ == "__main__":
    try:
        num_points = int(input("생성할 좌표 개수를 입력하세요: "))
        x_min = float(input("X 좌표 최솟값: "))
        x_max = float(input("X 좌표 최댓값: "))
        y_min = float(input("Y 좌표 최솟값: "))
        y_max = float(input("Y 좌표 최댓값: "))

        if x_min >= x_max or y_min >= y_max:
            raise ValueError("최솟값은 최댓값보다 작아야 합니다.")

        coordinates = generate_random_coordinates(num_points, (x_min, x_max), (y_min, y_max))
        save_to_csv(coordinates)
        print(f"좌표 {num_points}개가 xyrand.csv 파일에 저장되었습니다.")

    except ValueError as e:
        print(f"잘못된 입력입니다: {e}")