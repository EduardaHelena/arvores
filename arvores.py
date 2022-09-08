import math

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

class Caminhamentos_em_Arvore:
    def em_ordem(raiz):
        if not raiz:
            return

        # Visita filho da esquerda.
        Caminhamentos_em_Arvore.em_ordem(raiz.esquerda)

        # Visita nodo corrente.
        print(raiz.chave)

        # Visita filho da direita.
        Caminhamentos_em_Arvore.em_ordem(raiz.direita)
        
    def pre_ordem(raiz):
        if not raiz:
            return

        # Visita nodo corrente.
        print(raiz.chave)
        
        # Visita filho da esquerda.
        Caminhamentos_em_Arvore.pre_ordem(raiz.esquerda)

        # Visita filho da direita.
        Caminhamentos_em_Arvore.pre_ordem(raiz.direita)
        
    def pos_ordem(raiz):
        if not raiz:
            return

        # Visita filho da esquerda.
        Caminhamentos_em_Arvore.pos_ordem(raiz.esquerda)

        # Visita filho da direita.
        Caminhamentos_em_Arvore.pos_ordem(raiz.direita)
        
        # Visita nodo corrente.
        print(raiz.chave)
        
# raiz = NodoArvore(3)
# raiz.esquerda = NodoArvore(5)
# raiz.direita  = NodoArvore(1)
# print("Árvore: ", raiz)

#Montando a Arvore Binaria
# raiz = NodoArvore(40)

# raiz.esquerda = NodoArvore(20)
# raiz.direita  = NodoArvore(60)

# raiz.direita.esquerda  = NodoArvore(50)
# raiz.direita.direita   = NodoArvore(70)
# raiz.esquerda.esquerda = NodoArvore(10)
# raiz.esquerda.direita  = NodoArvore(30)

#Caminhamentos da Arvore Binaria
# print("Ordem")
# Caminhamentos_em_Arvore.em_ordem(raiz)
# print("----------")

# print("pre_ordem")
# Caminhamentos_em_Arvore.pre_ordem(raiz)
# print("----------")

# print("pos_ordem")
# Caminhamentos_em_Arvore.pos_ordem(raiz)
# print("----------")

#Inserção em Árvores Binárias de Pesquisa

class Operacoes_com_Arvores:
    def criaArvore(raiz, nodos):
        # Cria uma árvore binária de pesquisa.
        raiz = NodoArvore(raiz)
        for chave in nodos:
            nodo = NodoArvore(chave)
            Operacoes_com_Arvores.insere(raiz, nodo)
        
        return raiz
    
    def insere(raiz, nodo):
        """Insere um nodo em uma árvore binária de pesquisa."""
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            raiz = nodo

        # Nodo deve ser inserido na subárvore direita.
        elif raiz.chave < nodo.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                Operacoes_com_Arvores.insere(raiz.direita, nodo)

        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                Operacoes_com_Arvores.insere(raiz.esquerda, nodo)

    def buscar(raiz, busca):
        if raiz is None:
            return None
        
        if raiz.chave == busca:
            return raiz
         
        elif raiz.chave > busca:
            return Operacoes_com_Arvores.buscar(raiz.esquerda, busca)

        else:
            return Operacoes_com_Arvores.buscar(raiz.direita, busca)

    def buscarMenorElemento(raiz):
        # if raiz is None:
        #         return None

        # elif raiz.esquerda and raiz.chave > raiz.esquerda.chave:
        #     return Operacoes_com_Arvores.buscarMenorElemento(raiz.esquerda)

        # else:
        #     return raiz

        #Gabarito: O menor é o elemento mais a esquerda na arvore
        nodo = raiz
        while nodo.esquerda is not None:
            nodo = nodo.esquerda
        return nodo.chave
    
    def buscarMaiorElemento(raiz):
        nodo = raiz
        while nodo.direita is not None:
            nodo = nodo.direita
        return nodo.chave

    def checarIgualdadeArvores(raiz_1, raiz_2):
        # if not raiz_1 and not raiz_2:
        #     return True
        # elif not raiz_1 or not raiz_2:
        #     return False
        # elif raiz_1.chave == raiz_2.chave:
        #     # Visita filho da esquerda.
        #     resultado = Operacoes_com_Arvores.checarIgualdadeArvores(raiz_1.esquerda, raiz_2.esquerda)
        #     if not resultado:
        #         return resultado

        #     # Visita filho da direita.
        #     resultado = Operacoes_com_Arvores.checarIgualdadeArvores(raiz_1.direita, raiz_2.direita)
        #     if not resultado:
        #         return resultado
            
        #     return True
        # else: 
        #     return False
        
        # 1. As duas árvores são vazias.
        if raiz_1 is None and raiz_2 is None:
            return True

        # 2. Nenhuma das árvores é vazia. Precisamos compará-las.
        if raiz_1 is not None and raiz_2 is not None:
            return ((raiz_1.chave == raiz_2.chave) and
                     Operacoes_com_Arvores.checarIgualdadeArvores(raiz_1.esquerda, raiz_2.esquerda) and
                     Operacoes_com_Arvores.checarIgualdadeArvores(raiz_1.direita, raiz_2.direita))

        # 3. Uma árvore é vazia mas a outra não.
        return False

    def alturaArvoreEsquerda(raiz, nodo):
        if raiz:
            nodo += 1

            if raiz.esquerda:
                return Operacoes_com_Arvores.alturaArvoreEsquerda(raiz.esquerda, nodo)

        return nodo
        
    def alturaArvoreDireita(raiz, nodo):
        if raiz:
            nodo += 1

            if raiz.direita:
                return Operacoes_com_Arvores.alturaArvoreDireita(raiz.direita, nodo)

        return nodo
    
    def alturaArvore(raiz):
        # if raiz:
        #     altura_esquerda = Operacoes_com_Arvores.alturaArvoreEsquerda(raiz.esquerda, 1)
        #     altura_direita  = Operacoes_com_Arvores.alturaArvoreDireita(raiz.direita, 1)
        #     if  altura_esquerda >= altura_direita:
        #         return altura_esquerda
        #     else: 
        #         return altura_direita
        # else:
        #     return None

        if raiz is None:
            return 0
        return max(Operacoes_com_Arvores.alturaArvore(raiz.esquerda), Operacoes_com_Arvores.alturaArvore(raiz.direita)) + 1
        
    def check_balanceada(raiz):
        if raiz is None:
            return False
        
        altura_esquerda = Operacoes_com_Arvores.alturaArvoreEsquerda(raiz.esquerda, 1)
        altura_direita  = Operacoes_com_Arvores.alturaArvoreDireita(raiz.direita, 1)
        
        if math.fabs(altura_esquerda - altura_direita) > 1:
            return False
        
        return True
    
    def check_simetria(raiz_esquerda, raiz_direita):
        
        if raiz_esquerda is None and raiz_direita is None:
            return True

        if raiz_esquerda is not None and raiz_direita is not None:
            return (Operacoes_com_Arvores.check_simetria(raiz_esquerda.esquerda, raiz_direita.esquerda) and
                    Operacoes_com_Arvores.check_simetria(raiz_esquerda.direita, raiz_direita.direita))

        return False

# Imprime o caminhamento em ordem da árvore.
# Caminhamentos_em_Arvore.em_ordem(raiz)

#Busca um nodo
#Operacoes_com_Arvores.buscar(raiz, 20)

# Procura por valores na árvore.
# for chave in [-50, 10, 30, 70, 100]:
#     resultado = Operacoes_com_Arvores.buscar(raiz, chave)
#     print("\n")
#     if resultado:
#         print("Busca pela chave {}: Sucesso!".format(chave))
#     else:
#         print("Busca pela chave {}: Falha!".format(chave))

# ----------------------------------------------------------------
# Encontre o menor elemento em uma BST.
# resultado = Operacoes_com_Arvores.buscarMenorElemento(raiz)
# print(resultado)

# Encontre o maior elemento em uma BST.
# resultado = Operacoes_com_Arvores.buscarMaiorElemento(raiz)
# print(resultado)

# Verifique se duas árvores binárias são idênticas.
# raiz_2 = Operacoes_com_Arvores.criaArvore(40, [20, 60, 50, 70, 10, 30])
# resultado  = Operacoes_com_Arvores.checarIgualdadeArvores(raiz_1, raiz_2)
# print(resultado)


raiz_1 = Operacoes_com_Arvores.criaArvore(40, [20, 60, 50, 70, 10, 30])
altura = Caminhamentos_em_Arvore.em_ordem(raiz_1)
print(altura)