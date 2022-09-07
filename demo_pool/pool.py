from  multiprocessing import Pool
import time
  
def Foo(i):
    print('foo',i)
    time.sleep(3.5)
    return i+100
  
def Bar(arg):
    print('-->exec done:',arg)
    return arg

if __name__ == '__main__':
    with Pool(processes=5) as pool:
        for i in range(10):
            print('i: ', i)
            r = pool.apply_async(func=Foo, args=(i,),callback=Bar)
        print('after apply_async, before close & join.')
        pool.close()
        pool.join() # 刪掉這行，主程序會不等子程序跑完就結束
    print('after pool with clause')