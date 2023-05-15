def banco(C,N,T,D):
    tempo = 0
    clientes = N
    fila = []
    espera = [0]*N
    atendimento = [0]*N
    #False significa que o caixa não está ocupado
    caixas = []
    for i in range(C):
        caixas.append([0,0])
        
    atendidos = [False]*N
    
    while clientes > 0:

        for i in range(N):
            if T[i] == tempo:
                fila.append(i)
    

        for i in range(len(fila)):
            for j in range(len(caixas)):
                if caixas[j][0] == 0 and not atendidos[i]:
                    caixas[j][0] = 1
                    caixas[j][1] = fila[i]
                    atendidos[i] = True
                    break
        
            
        for i in range(len(fila)):
            if not atendidos[i]:
                espera[fila[i]] +=1            
        
        for i in range(len(caixas)):
            if caixas[i][0] == 1:
                atendimento[caixas[i][1]] +=1
                
            if atendimento[caixas[i][1]] >= D[caixas[i][1]]:
                caixas[i][0] = False
                caixas[i][1] = 0
                clientes -= 1
         
        tempo+=1
        
     
    x = 0
    
    for i in range(len(espera)):
        if espera[i] > 20:
            x+=1
    
    return x
    

    
if __name__ == '__main__':
    C = 3
    N = 16
    T = [0,0,0,3,5,7,11,13,14,15,16,17,18,19,20,23]
    D = [10,10,10,10,10,10,10,10,10,10,10,10,3,10,10,3]
    atrasados = banco(C,N,T,D)
    print(atrasados)
    C = 1
    N = 5
    T = [0,0,1,2,30]
    D = [10,10,10,10,10]
    atrasados = banco(C,N,T,D)
    print(atrasados)
