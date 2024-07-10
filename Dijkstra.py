import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# 페이지 제목 설정
st.title("Shortest Path Finding Demo (Dijkstra Algorithm)")

# 미로 형태의 그래프 생성 (또는 다른 방식으로 그래프 생성)
G = nx.grid_2d_graph(10, 10)
remove_edges = [(x, y) for x in range(10) for y in range(10) if (x + y) % 3 == 0]
G.remove_edges_from(remove_edges)

# 모든 노드 가져오기
nodes = list(G.nodes)

# 시작 노드 및 도착 노드 선택
start_node = st.selectbox("Start Node", nodes)
end_node = st.selectbox("End Node", nodes)

# Dijkstra 알고리즘 실행
if start_node and end_node:
    try:
        shortest_path = nx.shortest_path(G, source=start_node, target=end_node)
        shortest_path_length = nx.shortest_path_length(G, source=start_node, target=end_node)

        # 결과 출력
        st.write(f"Shortest Path: {shortest_path}")
        st.write(f"Shortest Path Length: {shortest_path_length}")

        # 시각화
        pos = {(x, y): (y, -x) for x, y in G.nodes()}  # 격자 그래프에 맞게 위치 조정
        nx.draw(G, pos, with_labels=True, node_size=200, font_size=10)
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='r')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
        st.pyplot(plt)

    except nx.NetworkXNoPath:
        st.error("No path found between the selected nodes.")
