import pymysql


class DB:
    def __init__(self):
        super().__init__()
        self.db_ = pymysql.connect("localhost", "root", "2233")
        cursor = self.db_.cursor()

    def HasUser(self, user):
        pass

    def AddUser(self, user, passwd, sha):
        pass

    def Login(self, user, passwd):
        pass

    def UpdatePasswd(self):
        pass

    def CheckBalance(self, user, passwd):
        pass
