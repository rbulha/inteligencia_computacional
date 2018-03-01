# -*- coding: utf-8 -*-
import copy

class Cbalde:
    def __init__(self,capacidade):
        self.agua = 0
        self.capacidade = capacidade
        self.estado_atual = 'VAZIO'
        self.estadosfuturos = ['CHEIO']
    def enche(self,quantidade):
        if quantidade >= (self.capacidade - self.agua):
            resto = quantidade - (self.capacidade - self.agua)
            self.agua = self.capacidade
            self.estado_atual = 'CHEIO'
            self.estadosfuturos = ['VAZIO','ESVAZIA']
        else:
            resto =0
            self.agua = quantidade
            self.estado_atual = "%dL"%(self.agua)
            self.estadosfuturos = ['VAZIO','CHEIO','ESVAZIA']
        return resto
    def esvazia(self):
        agua = self.agua
        self.agua = 0
        self.estado_atual = 'VAZIO'
        self.estadosfuturos = ['CHEIO']
        return agua
    def estacheio(self):
        return self.agua == self.capacidade
    def estavazio(self):
        return self.agua == 0
    def estado(self):
        return self.estado_atual
    def estados_futuros(self):
        return self.estadosfuturos
    def __str__(self):
        return "%dL"%(self.agua)
    def __repr__(self):
        return "%dL"%(self.agua)

def aplica_estado(baldes,estados):
    if baldes[0].estado() != estados[0]:
        muda = 0
        receptor = 1
    else:
        muda = 1
        receptor = 0

    if estados[muda] == 'VAZIO':
        baldes[muda].esvazia()
    elif estados[muda] == 'CHEIO':
        baldes[muda].enche(baldes[muda].capacidade)
    elif estados[muda] == 'ESVAZIA':
        if (not baldes[muda].estavazio()) and (not baldes[receptor].estacheio()):
            resto = baldes[receptor].enche(baldes[muda].esvazia())
            if resto > 0:
                baldes[muda].enche(resto)
    else:
        print('**************  falha no mapeamento')

def estaresolvido(b):
    if b[0].agua == 2:
        return True
    else:
        return False

def estadorepedido(q,item):
    baldes = item[3]
    antigos = list(filter(lambda x: (x[3][0].estado() == baldes[0].estado()) and (x[3][1].estado() == baldes[1].estado()),q))
    if len(antigos) > 0:
        return True
    else:
        return False

def build_tree(estado_vencedor, antigos_estados):
    tree = []
    no_pai = estado_vencedor[0]
    est_pai = list(filter(lambda x: x[1] == no_pai,antigos_estados))
    tree.append(estado_vencedor)
    while no_pai > 0:
        tree.append(est_pai[0])
        no_pai = est_pai[0][0]
        est_pai = list(filter(lambda x: x[1] == no_pai,antigos_estados))
    return tree

def print_tree(tree):
    deepth = 0
    root = tree.pop()
    print('%d  %d -> %s'%(deepth+1,root[1],root[3]))
    print('   |__')
    while len(tree) > 0:
        no = tree.pop()
        deepth += 1
        print(' '*6*deepth+'\\')
        print('%d'%(deepth+1)+' '*6*deepth+' %d -> %s'%(no[1],no[3]))
        if len(tree) != 0:
            print(' '*6*deepth+'  |___')

def main(argv):
    baldes_0=[Cbalde(4),Cbalde(3)]

    q_antigos = []
    q_novos = []

    no_atual = 0
    no_pai = 0

    q_novos.append((no_pai,no_atual,[t.estado() for t in baldes_0],copy.deepcopy(baldes_0)))

    while len(q_novos) > 0:
        novo = q_novos.pop(0)
        #print(novo)
        #programPause = raw_input("...")
        baldes_n = novo[3]
        estados_n = novo[2]
        aplica_estado(baldes_n,estados_n)
        #print(novo)
        #programPause = raw_input("...")
        if estaresolvido(baldes_n):
            print(' ')
            print('** solução no estado: %d ==> trilha:\n'%(novo[1]))
            print_tree(build_tree(novo, q_antigos))
            print(' ')
        else:
            if not estadorepedido(q_antigos,novo):
                q_antigos.append(novo)
                no_pai = novo[1]
                estado_atual = [t.estado() for t in baldes_n]
                for e4L in baldes_n[0].estados_futuros():
                    no_atual += 1
                    q_novos.append((no_pai,no_atual,[e4L,estado_atual[1]],copy.deepcopy(baldes_n)))
                for e3L in baldes_n[1].estados_futuros():
                    no_atual += 1
                    q_novos.append((no_pai,no_atual,[estado_atual[0],e3L],copy.deepcopy(baldes_n)))
            #print("estados = %r"%q_novos)
            #programPause = raw_input("Press the <ENTER> key to continue...")

    print('fim da análise com %d nós!'%len(q_antigos))
if __name__ == "__main__":
    main(0)


