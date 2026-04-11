class CountSquares:
    def __init__(self):
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        align_x = [p for p in self.points if p[0] == point[0]]
        align_y = [p for p in self.points if p[1] == point[1]]
        count = 0
        for px in align_x:
            for py in align_y:
                if abs(px[1] - point[1]) != abs(py[0] - point[0]) or px[1] == point[1]:
                    continue
                count += sum(1 for p in self.points if p[0] == py[0] and p[1] == px[1])
    
        return count
