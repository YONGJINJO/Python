from collections import deque

class StationNode:
    """지하철역 노드 클래스, 이름만 포함"""
    def __init__(self, name):
        self.station_name = name
        self.adjacent_stations = []
        self.visited = False

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

def dfs(graph, start_node):
    """최단경로용 dfs 함수"""
    stack = deque()

    # 모든 노드를 처음 보는 노드로 초기화
    for station in graph.values():
        station.visited = 0

    stack.append(start_node)                                # 시작 노드를 스택에 넣는다
    start_node.visited = 1                                  # 시작 노드를 방문표시한다.

    while stack:
        current_station = stack.pop()                       # 스택에서 노드를 빼서 방문표시한다
        current_station.visited = 2
        for station in current_station.adjacent_stations:   # 노드의 인접 노드를 하나씩 확인하면서
            if station.visited == 0:                        # 처음 방문하는 노드이면
                stack.append(station)                       # 스택에 넣는다
                station.visited = 1                         # 회색표시 해준다

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

stations = create_station_graph("./stations.txt")  # stations.txt 파일로 그래프를 만든다

# stations에 저장한 역 인접 역들 출력 (체점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
        print(stations[station])

stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)

# 최단 경로 알고리즘

def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque()

    # 모든 노드를 방문하지 않은 노드 표시
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None
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


def back_track(destination_node):
    """최단 경로를 찾기 위한 back tracking 함수"""
    res_str = ""        # 리턴할 결과 문자열
    current_node = destination_node
    while current_node is not None:
        res_str = "{} ".format(current_node.station_name) + res_str
        current_node = current_node.predecessor

    return res_str

stations = create_station_graph("./new_stations.txt")  # stations.txt 파일로 그래프를 만든다

bfs(stations, stations["을지로3가"])  # 지하철 그래프에서 을지로3가역을 시작 노드로 bfs 실행
print(back_track(stations["강동구청"]))  # 을지로3가에서 강동구청역까지 최단 경로 출력

