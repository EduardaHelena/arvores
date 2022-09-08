from tree import Tree 

class Operations_Tree:
    def height_nodo(root, nodo):
        if root:
            nodo += 1

            if root.right:
                return Operations_Tree.height_nodo(root.right, nodo)
            
            if root.left:
                return Operations_Tree.height_nodo(root.left, nodo)
  
        return nodo
    
    def getHeight(raiz):
        if raiz:
            altura_esquerda = Operations_Tree.height_nodo(raiz.esquerda, 0)
            altura_direita  = Operations_Tree.height_nodo(raiz.direita, 0)
            if  altura_esquerda >= altura_direita:
                return altura_esquerda
            else: 
                return altura_direita
        else:
            return None
        
tree = Tree.create(3, [1, 2, 5, 4, 6,7])
print(Operations_Tree.getHeight(tree))