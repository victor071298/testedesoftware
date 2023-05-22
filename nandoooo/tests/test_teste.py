import sys
sys.path.insert(0,'../src')
from testedeteste import banco

def testoutput1():
    resultado = banco(1,5,[0,0,1,2,30],[10,10,10,10,10])
    assert resultado == 1
    
def testoutput2():
    resultado = banco(3,16,[0,0,0,3,5,7,11,13,14,15,16,17,18,19,20,23],[10,10,10,10,10,10,10,10,10,10,10,10,3,10,10,3])
    assert resultado == 2
       
def testoutpt3():
    resultado = banco(1,5,[0,0,0,0,0],[10,10,10,10,10])
    assert resultado == 2

