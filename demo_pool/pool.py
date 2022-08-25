from  multiprocessing import Pool
import time
  
def Foo(i):
    print('foo',i)
    time.sleep(0.5)
    return i+100
  
def Bar(arg):
    print('-->exec done:',arg)

if __name__ == '__main__':
    with Pool(processes=5) as pool:
        rs = []
        for i in range(10):
            print('i: ', i)
            r = pool.apply_async(func=Foo, args=(i,),callback=Bar)
            rs.append(r)
            #pool.apply(func=Foo, args=(i,))
        #for r in rs:
        #    r.wait()
        print('after apply_async, before close & join.')
        pool.close()
        pool.join()
    print('after pool with clause')