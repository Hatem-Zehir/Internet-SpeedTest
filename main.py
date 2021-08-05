import sqlite3
import speedtest
from datetime import datetime

db = sqlite3.connect("SpeedTest.db")
db.row_factory = sqlite3.Row
db.execute("create table if not exists Speed(Date text, Time text, Download real, Upload real, Ping integer)")

servers = []
threads = None
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()
results_dict = s.results.dict()

DL = round(results_dict['download']/(1024*1024), 2)
UP = round(results_dict['upload']/(1024*1024), 2)
ping = round(results_dict['ping'], 0)

now = datetime.now()
dtString = now.strftime("%d %B %Y")
time = now.strftime("%H:%M")
db.execute("insert into Speed(Date, Time, Download, Upload, Ping) values (? , ? , ?, ?, ?)",(dtString, time, DL, UP, ping))
db.commit()

if __name__ == "__main__":
    print('Download: ', DL, 'Mbps')
    print('Upload: ', UP, 'Mbps')
    print('Ping: ', ping, 'ms')
