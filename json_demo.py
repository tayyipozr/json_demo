import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json files
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding=("utf-8")) as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user["username"], password=user["password"], email=user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("kullanıcı oluşturuldu")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("login oldunuz")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış yapıldı")

    def identity(self):
        if self.isLoggedIn:
            print(f"username : {self.currentUser.username}")
        else:
            print("giriş yapılmadı")

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json", "w") as file:
            json.dump(list, file)


reporsitory = UserRepository()

while True:
    print("MENU".center(50, "*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz : ")
    if secim == "5":
        break
    else:
        if secim == "1":
            if reporsitory.isLoggedIn:
                print("ilk önce çıkış yapınız!")
            else:
                username = input("username: ")
                password = input("password: ")
                email = input("email: ")
                user = User(username=username, password=password, email=email)
                reporsitory.register(user)
                print(reporsitory.users)

        elif secim == "2":
            if reporsitory.isLoggedIn:
                print("zaten giriş yapılmış")
            else:
                username = input("username: ")
                password = input("password: ")
                reporsitory.login(username, password)

        elif secim == "3":
            if not reporsitory.isLoggedIn:
                print("zaten giriş yapılmadı")
            else:
                reporsitory.logout()

        elif secim == "4":
            reporsitory.identity()

        else:
            print("yanlış bir seçim yaptınız!!!")
