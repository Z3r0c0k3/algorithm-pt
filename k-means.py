import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import io

# 페이지 제목 설정
st.title("K-Means 클러스터링 시연")

# 예시 데이터 (CSV 형식 문자열)
sample_data = """
X,Y
-9,-5
6,-4
-10,-3
1,8
1,-4
8,10
4,6
-9,-8
-5,-1
5,8
10,-7
-1,-9
-5,-1
-9,-8
-2,10
4,-5
9,-9
-3,-7
-8,5
-2,-1
-9,-7
-2,7
-8,0
-2,-4
-2,-8
-2,5
2,-5
3,-1
4,-3
-4,-10
4,-6
-10,-3
-10,5
6,0
1,-3
-4,-7
-6,5
-7,-5
-5,0
0,2
5,-2
7,3
-1,-9
-1,-3
6,9
-8,2
-4,-1
-2,-10
-1,0
3,-3
"""

# 예시 데이터를 StringIO를 통해 DataFrame으로 변환
df_sample = pd.read_csv(io.StringIO(sample_data))

# 데이터 업로드 (선택 사항)
uploaded_file = st.file_uploader("CSV 파일을 선택하세요. (선택 사항)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.write("예시 데이터를 사용합니다.")
    df = df_sample

# 데이터 표시
st.write("사용되는 데이터:")
st.dataframe(df)

# K 값 설정
k = st.slider("클러스터의 개수 (K)", 2, 10, 3)

# K-Means 클러스터링 실행
X = df.iloc[:, :].values  # 모든 열을 사용
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)

# 결과 시각화
plt.figure(figsize=(8, 6))  # 그림 크기 설정
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='*', label='Centroid')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title(f"K-Means Algorithm (K={k})")
plt.legend()
st.pyplot(plt)

# 클러스터링 결과 출력
st.write("클러스터링 결과:")
df["Cluster"] = kmeans.labels_
st.dataframe(df)
