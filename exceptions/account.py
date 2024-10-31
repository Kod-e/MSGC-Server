#exceptions/account_exceptions.py

#账户异常，错误码为1000-1999
class AccountException(Exception):
    """
    账户异常基类
    """
    code = 1000
    message = '账户异常'
    
    def __init__(self, message=None):
        if message is not None:
            self.message = message
        super().__init__(self.message)
        
    def to_dict(self) -> dict:  
        return {
            'code': self.code,
            'message': self.message
        }
        
#账户已存在异常,错误码为1001
class AccountExistException(AccountException):
    code = 1001
    message = '账户已存在'
    
    
#账户不存在异常,错误码为1002
class AccountNotExistException(AccountException):
    code = 1002
    message = '账户不存在'

#账户签名校验失败异常,错误码为1003
class AccountSignatureVerifyException(AccountException):
    code = 1003
    message = '账户签名校验失败'