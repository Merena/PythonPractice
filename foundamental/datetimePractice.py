from datetime import *

print('now:', dir(), '\n\n')
print('date:', dir(date), '\n\n')
print('time:', dir(time), '\n\n')
print('datetime:', dir(datetime), '\n\n')
print('timedelta:', dir(timedelta), '\n\n')


print(' date start '.center(50,'-'))

a = date.today()
b = date.fromtimestamp(datetime.today().timestamp())

c = date.max
d = date.min

e = a.year
f = a.month
g = a.day
h = a.weekday()

i = a.isocalendar()
g = a.timetuple()
h = a.isoformat()


j = a.ctime()
k = a.toordinal()

o = date.fromisoformat(h)
p = date.fromordinal(k)
q = date.fromtimestamp(1525104000)
r = a.strftime('%Y-%m-%d')


print(' date end '.center(50,'-'))

print(' time start '.center(50,'-'))

aa = datetime.now().time()
dd = aa.hour
bb = aa.minute
cc = aa.second
ee = aa.microsecond

ff = aa.utcoffset()
gg = aa.isoformat()
hh = aa.strftime('%H:%M:%S.%f')
# ii = aa.tzinfo()
jj = aa.tzname()

kk = time.max
ll = time.min
mm = time.fromisoformat(gg)
nn = aa.dst()
oo = aa.replace(hour=7)
pp = time.resolution


print(' time start '.center(50,'-'))

print(' datetime start '.center(50,'-'))

aaa = datetime.now()
bbb = aaa.year
ccc = aaa.month
ddd = aaa.day
eee = aaa.hour
fff = aaa.minute
ggg = aaa.second
hhh = aaa.microsecond
iii = aaa.isoformat()
jjj = aaa.date()
kkk = aaa.time()
lll = aaa.ctime()
mmm = aaa.timestamp()
nnn = aaa.timetuple()
ooo = aaa.toordinal()
ppp = aaa.strftime('%Y-%m-%d %H:%M:%S.%f')
qqq = aaa.replace(year=2014)
rrr = aaa.utcoffset()
sss = aaa.utctimetuple()
ttt = aaa.weekday()
uuu = datetime.fromisoformat(iii);
a4 = datetime.fromtimestamp(mmm)
b4 = datetime.fromordinal(ooo)
c4 = datetime.utcfromtimestamp(mmm)
d4 = datetime.resolution
e4 = datetime.strptime(ppp, '%Y-%m-%d %H:%M:%S.%f')



print(' datetime start '.center(50,'-'))

print(' timedelta start '.center(50,'-'))

a5 = timedelta(days=5)
d5 = timedelta(minutes=50)
b5 = datetime.today() + a5
c5 = datetime.today() - a5
f5 = b5-c5


print(' timedelta start '.center(50,'-'))