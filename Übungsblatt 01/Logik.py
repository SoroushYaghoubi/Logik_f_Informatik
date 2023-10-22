Alpha = [  (True, True, False, False, False), 
           (True, False, True, False, False), 
           (True, False, False, True, False), 
           (True, False, False, False, True), 
           
           (False, True, True, False, False), 
           (False, True, False, True, False), 
           (False, True, False, False, True), 

           (False, False, True, True, False), 
           (False, False, True, False, True), 
            
           (False, False, False, True, True)  ]


def implication(A, B):
    return ((not A) or B)
def equivalence(A, B):
    return (A and B)     or     ((not A) and (not B))


def Phi_1(A, B, C, D, E):
    ans = int(equivalence( (not A),     (B or D or E) ))
    return ans

def Phi_2(A, B, C, D, E):
    ans = int(equivalence( (not B),     (implication((not E), C)) ))
    return ans

def Phi_3(A, B, C, D, E):
    ans = int(equivalence( (not C),     implication((not D), (B or E)) ))
    return ans

def Phi_4(A, B, C, D, E):
    ans = int(equivalence( (not D),     (A and      (B or C)) ))
    return ans

def Phi_5(A, B, C, D, E):
    ans = int(equivalence( (not E),     implication((not C),    ((not B) or (not D))) ))
    return ans

for i in range(10):
    print("Alpha ", end='')
    print(i, end='')
    print(": ", end='')
    print(Phi_1(Alpha[i][0], Alpha[i][1], Alpha[i][2], Alpha[i][3], Alpha[i][4]), end=' ')
    print(Phi_2(Alpha[i][0], Alpha[i][1], Alpha[i][2], Alpha[i][3], Alpha[i][4]), end=' ')
    print(Phi_3(Alpha[i][0], Alpha[i][1], Alpha[i][2], Alpha[i][3], Alpha[i][4]), end=' ')
    print(Phi_4(Alpha[i][0], Alpha[i][1], Alpha[i][2], Alpha[i][3], Alpha[i][4]), end=' ')
    print(Phi_4(Alpha[i][0], Alpha[i][1], Alpha[i][2], Alpha[i][3], Alpha[i][4]))

