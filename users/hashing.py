from passlib.context import CryptContext

pwd = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash():
    @staticmethod
    def bcrypt(password: str):
        return pwd.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd.verify(plain_password, hashed_password)
