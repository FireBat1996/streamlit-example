import streamlit as st
import socket

# Streamlit 애플리케이션 구성
st.title('AGV Control Panel')

# AGV와 통신할 호스트와 포트
AGV_HOST = 172.30.1.46
AGV_PORT = 2

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((AGV_HOST, AGV_PORT))

# 버튼 클릭 이벤트 핸들러
if st.button('1'):
    # AGV에 '1' 신호를 보내는 코드
    signal = '1'
    client_socket.sendall(signal.encode())
    st.write(f"Sending signal '{signal}' to AGV")

if st.button('2'):
    # AGV에 '2' 신호를 보내는 코드
    signal = '2'
    client_socket.sendall(signal.encode())
    st.write(f"Sending signal '{signal}' to AGV")

if st.button('R'):
    # AGV에 'R' 신호를 보내는 코드
    signal = 'R'
    client_socket.sendall(signal.encode())
    st.write(f"Sending signal '{signal}' to AGV")

if st.button('S'):
    # AGV에 'S' 신호를 보내는 코드
    signal = 'S'
    client_socket.sendall(signal.encode())
    st.write(f"Sending signal '{signal}' to AGV")

# 소켓 종료
client_socket.close()
