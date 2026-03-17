from info import rede_social


def engenho(redes_social, origem, destino): 
    visitados = set()
    fila = [(origem, 0)] 
    visitados.add(origem)
    #grupo_visitado = []

    while fila:
        pessoa_momento, distancia = fila.pop(0) 

        if pessoa_momento == destino:
            return f"Total de conexões: {distancia}"

        for conexao in redes_social[pessoa_momento]:
            if conexao not in visitados:
                print(f"Analisando {conexao} -> Nivel: {distancia + 1}")
                visitados.add(conexao)
                fila.append((conexao, distancia + 1))
    
    return "Conexão não encontrada" 

link = engenho(rede_social, "Vitor", "Recrutador")
print(link)  


#O problema que eu busquei trabalhar é o nivel de conexão entre pessoas dentro de uma rede social voltada ao mercado de trabalho.
# A ideia principal é encontrar pelo nivel de conexão um candidato a uma pessoa que seja recrutadora. 
# O algoritmo utilizado foi o Breadth-First Search (BFS), que vai buscar pelo nivel de conexão entre os amigos do canditado, expandindo a busca para cada amigo de amigo, até chegar ao recrutador. 
# Esse algoritmo foi escolhido por ser mais eficiente para encontrar os caminhos mais curtos dos grafos até chegar no destino final, que no caso do problema é o recrutador.
