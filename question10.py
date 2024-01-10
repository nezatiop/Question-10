import numpy as np

def net_hook_force(anchors, ks, rest_lengths, position):
    lengths = []  # réponse F, nous n'avons pas besoin d'avoir un array étant donné que ce n'est q'une longueur d'arc (les 4 ressorts sont de même taille)
    directions = [] # réponse A, nous aurons besoin d'une liste de différentes directions (les vecteurs seront directement placés dedans, pas besoin que direction soit directement un vecteur)
    for anchor in anchors: 
        PA = np.array(position) - anchor # réponse C, PA est le vecteur permettant d'aller de la position de la balle aux anchors donc nous avons besoin d'un vecteur
        length = np.linalg.norm(PA) # réponse E, nous souhaitons avoir la longueur des ressorts qui est calculable par la norme des vecteurs de chacun des ressort (la réponse E fait une multiplication matricielle bizzare mohem)
        lengths.append(length) # réponse G, la liste lengths permet de retenir la longueur de chacun des ressorts
        directions.append(PA/length) # réponse H, permet de donner les directions en x et en y (nous avons donc un vecteur directeur / par une norme ce qui donnera un nouveau vecteur (x/length;y/length))
    forces = -(np.array(lengths) - rest_lengths) * ks # réponse I, formule -k*(delta l) 
    net = 0 
    for i in range(len(forces)): # réponse B,  nous avons 4 forces à additionner donc autant prendre une longueur de 4 pour la boucle
        net += forces[i] # réponse D, la bonne réponse, nous avons qu'à la fin nous devons avoir un vecteur (x,y) hélas nous avions qu'une valeur mais en multipliant force par directions, étant donné que directions est un vecteur, nous obtenons bel et bien un vecteur en (x;y)
    return net # réponse J, en retournant les forces, la boucle ne servirait à rien (celle juste au dessus) et nous aurions juste la premiere force calculé comme output

anchors = [(0.0,0.0),(2.0,0.0),(2.0,2.0),(0.0,2.0)]
lengths = [1.0,1.0,1.0,1.0]
ks = [0.5,1.0,1.0,0.5]

print(net_hook_force(anchors, ks, lengths, (1.0,1.0)))
