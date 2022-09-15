import win32com.client
import pythoncom
# 이베스트 로그인 클래스
class XASessionEventHandler:
    # 클래스 변수 : 로그인 상태 확인
    login_state = 0

    def OnLogin(code, msg):
        if code == "0000":
            print("login success!!")
            XASessionEventHandler.login_state = 1
        else:
            print("login fail!!")

    def OnDisconnect():
        print("Session disconnected...")
        XASessionEventHandler.login_state = 0

class EBest:
    def __init__(self, mode):
        self.user = ''
        self.password = ''
        self.cert_password = ''
        self.host = 'demo.ebestsec.co.kr'
        self.port = 20001

        self.xa_session_handler = win32com.client.DispatchWithEvent("XA_Session.XASession", XASessionEventHandler)

    def login(self):
        self.xa_session_handler.ConnectServer(self.host, self.port)
        self.xa_session_handler.Login(self.user, self.password, self.cert_password, 0, 0)

        while XASessionEventHandler.login_state == 0:
            pythoncom.PumpWaitingMessages()

        def logout(self):
            XASessionEventHandler.login_state = 0
            self.xa_session_handler.DisconnectServer()

ebest = EBest()
ebest.login()