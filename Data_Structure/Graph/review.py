"""
class GraphNode:
    #그래프에 들어갈 노드 클래스
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits
        self.adjacent_stations = []
"""

class StationNode:
    """지하철역 노드 클래스, 이름만 포함"""
    def __init__(self, name):
        self.station_name = name
        self.adjacent_stations = []

    def add_connection(self, other_station):
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)

    def __str__(self):
        """지하철 역 이름과 연결된 역들을 모두 출력해준다."""
        res_str = "{}: ".format(self.station_name)
        for station in self.adjacent_stations:
            res_str += "{} ".format(station.station_name)

        return res_str


def create_subway_graph(input_file):
    """input file에서 데이터를 읽어와 지하철 그래프 노드를 리턴하는 함수"""
    stations = {}

    #파라미터로 받은 input file을 연다
    with open(input_file, 'rt', encoding = 'utf-8') as stations_raw_file:
        for line in stations_raw_file: # 파일을 한 줄씩 받아온다
            subway_line = line.strip().split("-") # 앞 뒤 띄어쓰기를 없애고 - 를 기준점으로 데이터를 나눈다.
            former_station = None

            for name in subway_line:
                station_name = name.strip() # 앞 뒤 띄어쓰기 없애기

                if station_name not in stations:
                    station = StationNode(station_name)
                    stations[station_name] = station
                if former_station is not None:
                    stations[station_name].add_connection(former_station)

                former_station = stations[station_name]

    return stations




"""
station_0 = GraphNode("교대역", 14)
station_1 = GraphNode("사당역", 14)
station_2 = GraphNode("종로 3가역", 16)
station_3 = GraphNode("서울역", 16)

#노드들을 파이썬 리스트에 저장
stations = [station_0, station_1, station_2, station_3]

#노드들을 딕셔너리에 저장

stations = {
    "교대역" : station_0,
    "사당역" : station_1,
    "종로 3가역" : station_2,
    "서울역" : station_3
}

node_1 = stations["교대역"]


#stations = create_station_nodes("C:/Users/choyj/Desktop/Python/Data_Structure/Graph/stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

# stations에 저장한 역들 이름 출력 (체점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station].station_name)

"""

stations = create_subway_graph("./stations.txt")  # stations.txt 파일로 그래프를 만든다

# stations에 저장한 역 인접 역들 출력 (체점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
        print(stations[station])