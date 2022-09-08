class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

class Tree:
    def create(raiz, nodos):
        # Cria uma árvore binária de pesquisa.
        raiz = NodoArvore(raiz)
        for chave in nodos:
            nodo = NodoArvore(chave)
            Tree.input(raiz, nodo)
        
        return raiz
    
    def input(tree, nodo):
        """Insere um nodo em uma árvore binária de pesquisa."""
        # Nodo deve ser inserido na raiz.
        if tree is None:
            tree = nodo

        # Nodo deve ser inserido na subárvore direita.
        elif tree.chave < nodo.chave:
            if tree.direita is None:
                tree.direita = nodo
            else:
                Tree.input(tree.direita, nodo)

        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if tree.esquerda is None:
                tree.esquerda = nodo
            else:
                Tree.input(tree.esquerda, nodo)
            
