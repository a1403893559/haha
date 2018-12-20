import threading
import time





def download(url):
    print (url)
    time.sleep(1)
    print (threading.current_thread().name)


def  main():
    starttime = time.time()
    task_list = ['url1','url2','url3']
    for url in task_list:
        thread = threading.Thread(target=download,name='线程',args=[url,])
        thread.setDaemon(True) #false是前台线程等子线程，true是后台线程，不等子线程
        thread.start()
        #download(url)
    endtime = time.time()
    print ('耗时'+str(endtime-starttime))

main()