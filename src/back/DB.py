import pymysql


class DB:
    def __init__(self):
        super().__init__()
        self.db_ = pymysql.connect(
            host="localhost", db="bcnet", user="root", passwd="2233")
        self.cursor_ = self.db_.cursor()

    def HasUser(self, user):
        sql = "SELECT * FROM user WHERE user='{}'".format(user)
        self.cursor_.execute(sql)
        res = self.cursor_.fetchall()
        if len(res) > 1:
            return True
        else:
            return False

    def HasUserSha(self, sha):
        sql = "SELECT * FROM user WHERE sha='{}'".format(sha)
        self.cursor_.execute(sql)
        res = self.cursor_.fetchall()
        if len(res) > 1:
            return True
        else:
            return False

    def AddUser(self, user, passwd, sha, sk, pk):
        if self.HasUser(user) == True:
            return False
        else:
            sql = "INSERT INTO user(user,passwd,sha,sk,pk)VALUES('{}','{}','{}','{}','{}')".format(
                user, passwd, sha, sk, pk)
            try:
                self.cursor_.execute(sql)
                self.db_.commit()
                return True
            except:
                self.db_.rollback()
                return False

    def Login(self, user, passwd):
        sql = "SELECT sha from user WHERE user='{}' AND passwd='{}'".format(
            user, passwd)
        self.cursor_.execute(sql)
        res = self.cursor_.fetchone()
        if res != None:
            return res[0]
        else:
            return None

    def UpdatePasswd(self):
        pass

    def CheckBalance(self, sha):
        sql = "SELECT balance from user WHERE sha='{}'".format(sha)
        self.cursor_.execute(sql)
        res = self.cursor_.fetchone()
        if res != None:
            return res[0]
        else:
            return None

    def UpdateBalance(self, sha, amount):
        balance = self.CheckBalance(sha)
        new_balance = balance+amount
        sql = "UPDATE user SET balance='{}' where sha='{}'".format(
            new_balance, sha)
        try:
            self.cursor_.execute(sql)
            self.db_.commit
        except:
            self.db_.rollback()

    def GetSHA(self, user):
        sql = "SELECT sha from user WHERE user='{}'".format(user)
        self.cursor_.execute(sql)
        res = self.cursor_.fetchone()
        if res != None:
            return res[0]
        else:
            return None

    def GetSK(self, sha):
        sql = "SELECT sk from user WHERE sha='{}'".format(sha)
        self.cursor_.execute(sql)
        res = self.cursor_.fetchone()
        if res != None:
            return res[0]
        else:
            return None

    def GetPK(self, sha):
        sql = "SELECT pk from user WHERE sha='{}'".format(sha)
        self.cursor_.execute(sql)
        res = self.cursor_.fetchone()
        if res != None:
            return res[0]
        else:
            return None


if __name__ == '__main__':
    db = DB()
    sha = db.GetSHA("0x0")
    print(sha)
    sk = db.GetSK(sha)
    print(sk)
    pk = db.GetPK(sha)
    print(pk)
