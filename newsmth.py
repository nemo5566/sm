import sys,random,time
import requests

rand = random.Random()

def mylog(msg):
    print '[%s] %s' % (time.ctime().split()[3],msg)

def run():
    global rand

    sess = requests.session()
    sess.headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}

    mylog("get homepage...")
    resp = sess.get('http://m.newsmth.net/')
    time.sleep(rand.randint(3,5))

    mylog('login...')
    postdata = {'id':'nemo5566', 'passwd':'198988', 'save':'on'}
    resp = sess.post('http://m.newsmth.net/user/login', data=postdata)
    login_time=time.time()

    mylog('online...')
    while True:
        time.sleep(rand.randint(30,60))
        resp = sess.get('http://m.newsmth.net/board/ITExpress')
        if time.time()-login_time > 3600:
            break

    mylog("logout...")
    resp = sess.get('http://m.newsmth.net/user/logout')

def main():
    global rand
    while True:
        try:
            run()
        except Exception, e:
            mylog("get exception: %s" % e)
        time.sleep(rand.randint(100,200))

if __name__ == '__main__':
    main()
