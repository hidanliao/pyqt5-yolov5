import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('登录')
        self.setGeometry(200, 200, 300, 150)

        self.username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        self.password_label = QLabel('密码:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('登录')
        self.login_button.clicked.connect(self.login)
        self.register_button = QPushButton('注册')
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def login(self):
        # 获取输入的用户名和密码
        username = self.username_input.text()
        password = self.password_input.text()

        # 在这里编写登录逻辑
        # 可以连接到数据库进行用户名和密码验证

        # 示例：如果用户名和密码都是admin，则登录成功
        if username == 'admin' and password == 'admin':
            print('登录成功')
            self.show_yolov5_window()

    def register(self):
        # 在这里编写注册逻辑
        # 可以连接到数据库将新用户信息存储起来
        print('注册')

    def show_yolov5_window(self):
        # 在这里编写打开Yolov5检测画面的逻辑
        print('打开Yolov5检测画面')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
