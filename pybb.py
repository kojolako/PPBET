import json
import fonbet
from multiprocessing import Process
import os

def write_jsonNT(data, filename='answer.json'):
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False)

def ProcentNMB(a, b):
        r = a/b*100
        return str(r)+'%'
clear = lambda: os.system('cls')



def main():
        STARTED = 'stop'
        TIME_Q=0
        NMB = 1
        Cycle = input('Сколько повторов')
        STARTED = input('Начать?')
        while STARTED=='start':
                TIME_Q +=1
                if TIME_Q == 100:
                        write_jsonNT(fonbet.get_Live(), filename='upd/ans_'+str(NMB)+'.json')
                        #print('Wrt' + str(NMB) + '-----'+fonbet.RNM())
                        clear()
                        print('Количество запросов:'+ str(Cycle)+'     =============    ' +str(ProcentNMB(NMB,int(Cycle)))+' до конца')
                        NMB += 1
                        TIME_Q=0
                elif NMB > int(Cycle):
                        STARTED='stop'
        print('END')
        
                

        
        


if __name__ == '__main__':
    main()


