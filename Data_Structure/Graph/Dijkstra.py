import math
from collections import deque

class StationNode:
    """지하철역 노드 클래스, 이름만 포함"""
    def __init__(self, name):
        self.station_name = name
        self.adjacent_stations = []
        self.visited = False
        self.distance = math.inf
        self.complete = False

    def add_connection(self, other_station):
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)

    def __str__(self):
        """지하철 역 이름과 연결된 역들을 모두 출력해준다."""
        res_str = "{}: ".format(self.station_name)
        for station in self.adjacent_stations:
            res_str += "{} ".format(station.station_name)

        return res_str


def create_station_graph(input_file):
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

def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()

    # 모든 노드를 방문하지 않은 노드 표시
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None
        station_node.complete = False
        station_node.distance = math.inf
    # 시작 노드를 방문 표시 후 큐에 넣는다
    queue.append(start_node)
    start_node.visited = True

    # 큐에 아무것도 없을 때까지 확인 작업을 반복한다
    while queue:
        current_station = queue.popleft()                   # 큐에서 노드를 하나씩 뺀다
        for station in current_station.adjacent_stations:   # 인접 노드를 모두 확인해 가면서
            if station.visited is False:                    # 처음 방문한 노드라면
                station.visited = True                      # 방문표시를 한다
                queue.append(station)                       # 큐에 넣어준다
                station.predecessor = current_station

def dijstra(graph, start_node, destination_node):
    """최단 경로를 위한 다익스트라 알고리즘 함수"""
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None
        station_node.complete = False
        station_node.distance = math.inf

    start_node.distance = 0
    while check_complete(graph) is False:
        min_node = find_min(graph, start_node)
        for station in min_node.adjacent_stations:
            if station.distance > weight[min_node.station_name][station_node.station_name] + min_node.distance:
                station.distance = weight[min_node.station_name][station_node.station_name] + min_node.distance
            station.complete = True


def check_complete(graph):

    for station_node in graph.values():
        if station_node.complete is False:
            return False

    return True

def find_min(graph, start_node):

    min_node = start_node

    for station_node in graph.values():
        if station_node.complete is False:
            if station_node.distance < min_node.disatnce:
                min_node = station_node

    return min_node