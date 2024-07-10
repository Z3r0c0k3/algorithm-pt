import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 페이지 제목 설정
st.title("Random Forest Classifier Demo")

# 데이터 업로드
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded data:")
    st.dataframe(df)

    # 특성 및 타겟 변수 선택
    X_cols = st.multiselect("Select features (X)", df.columns)
    y_col = st.selectbox("Select target variable (y)", df.columns)

    if X_cols and y_col:
        X = df[X_cols]
        y = df[y_col]

        # 데이터 분할 (학습용 80%, 테스트용 20%)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Random Forest 모델 생성 및 학습
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # 예측 및 정확도 평가
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        # 결과 출력
        st.write(f"Accuracy: {accuracy:.2f}")
        st.text("Classification Report:\n" + report)

        # 특징 중요도 출력
        importances = model.feature_importances_
        st.write("Feature Importances:")
        for name, importance in zip(X_cols, importances):
            st.write(f"{name}: {importance:.3f}")
