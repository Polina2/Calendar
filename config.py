class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:' + open("secrets.txt", 'r').read() + '@localhost:5432/calendar1'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
