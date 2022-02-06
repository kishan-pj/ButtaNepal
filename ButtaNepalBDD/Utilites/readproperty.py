import configparser

config = configparser.RawConfigParser()
config.read(".\\ButtaNepalBDD\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('common-info','baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common-info','userName')
        return username
    
    @staticmethod
    def getPassWord():
        password = config.get('common-info','passWord')
        return password
    