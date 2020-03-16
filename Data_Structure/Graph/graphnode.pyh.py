class StationNode:
    """지하철 역 노드를 나타내는 클래스"""
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits
        self.adjacent_stations = []


station0 = StationNode("교대역", 14)
station1 = StationNode("사당역", 14)
station2 = StationNode("종로3가역", 16)
station3 = StationNode("서울역", 16)

stations = [station0, station1, station2, station3]
station = {
    "교대역" : 14,
    "사당역" : 14,
    "종로3가역" : 16,
    "서울역" : 16
}