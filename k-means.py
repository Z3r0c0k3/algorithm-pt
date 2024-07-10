import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 페이지 제목 설정
st.title("K-Means 클러스터링 시연")

# 데이터 업로드
uploaded_file = st.file_uploader("CSV 파일을 선택하세요.", type="csv")

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file)
    st.write("업로드 된 데이터:")
    st.dataframe(df)

    # K 값 설정
    k = st.slider("클러스터의 갯수 (K)", 2, 10, 3)

    # K-Means 클러스터링 실행
    X = df.iloc[:, :].values
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)

    # 결과 시각화
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
