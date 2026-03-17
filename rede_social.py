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


