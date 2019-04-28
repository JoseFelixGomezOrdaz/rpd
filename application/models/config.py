import web

db_host = 'i5x1cqhq5xbqtv00.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'u2gjrged012f7ifx'
db_user = 'c8w80i8y66pwea89'
db_pw = 'mjpxy276f71wo8xi'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )