# # import os
# # import time
# # import random
# # import string
# # import multiprocessing


# # # ===============================
# # # Consolidação dos resultados
# # # ===============================

# # def consolidar_resultados(resultados):
# #     total_linhas = 0
# #     total_palavras = 0
# #     total_caracteres = 0

# #     contagem_global = {
# #         "erro": 0,
# #         "warning": 0,
# #         "info": 0
# #     }

# #     for r in resultados:
# #         total_linhas += r["linhas"]
# #         total_palavras += r["palavras"]
# #         total_caracteres += r["caracteres"]

# #         for chave in contagem_global:
# #             contagem_global[chave] += r["contagem"][chave]

# #     return {
# #         "linhas": total_linhas,
# #         "palavras": total_palavras,
# #         "caracteres": total_caracteres,
# #         "contagem": contagem_global
# #     }


# # # ===============================
# # # Processamento de arquivo
# # # ===============================

# # def processar_arquivo(caminho):
# #     with open(caminho, "r", encoding="utf-8") as f:
# #         conteudo = f.readlines()

# #     total_linhas = len(conteudo)
# #     total_palavras = 0
# #     total_caracteres = 0

# #     contagem = {
# #         "erro": 0,
# #         "warning": 0,
# #         "info": 0
# #     }

# #     for linha in conteudo:
# #         palavras = linha.split()

# #         total_palavras += len(palavras)
# #         total_caracteres += len(linha)

# #         for p in palavras:
# #             if p in contagem:
# #                 contagem[p] += 1

# #         # Simulação de processamento pesado
# #         for _ in range(1000):
# #             pass

# #     return {
# #         "linhas": total_linhas,
# #         "palavras": total_palavras,
# #         "caracteres": total_caracteres,
# #         "contagem": contagem
# #     }

# # # ... (Mantenha suas funções consolidar_resultados e processar_arquivo exatamente como estão) ...

# # def executar_paralelo(pasta, num_processos):
# #     caminhos = [
# #         os.path.join(pasta, arquivo)
# #         for arquivo in os.listdir(pasta)
# #         if os.path.isfile(os.path.join(pasta, arquivo))
# #     ]

# #     inicio = time.time()

# #     with multiprocessing.Pool(processes=num_processos) as pool:
# #         resultados = pool.map(processar_arquivo, caminhos)

# #     fim = time.time()

# #     resumo = consolidar_resultados(resultados)

# #     print(f"\n=== EXECUÇÃO PARALELA ({num_processos} PROCESSOS) ===")
# #     print(f"Arquivos processados: {len(resultados)}")
# #     print(f"Tempo total: {fim - inicio:.4f} segundos")

# #     return resumo

# # if __name__ == "__main__":
    
# #     pasta = "log2"
    
# #     for n in range(1, multiprocessing.cpu_count() + 1):
# #         executar_paralelo(pasta, n)

# import os
# import time
# import random
# import string


# # ===============================
# # Consolidação dos resultados
# # ===============================

# def consolidar_resultados(resultados):
#     total_linhas = 0
#     total_palavras = 0
#     total_caracteres = 0

#     contagem_global = {
#         "erro": 0,
#         "warning": 0,
#         "info": 0
#     }

#     for r in resultados:
#         total_linhas += r["linhas"]
#         total_palavras += r["palavras"]
#         total_caracteres += r["caracteres"]

#         for chave in contagem_global:
#             contagem_global[chave] += r["contagem"][chave]

#     return {
#         "linhas": total_linhas,
#         "palavras": total_palavras,
#         "caracteres": total_caracteres,
#         "contagem": contagem_global
#     }


# # ===============================
# # Processamento de arquivo
# # ===============================

# def processar_arquivo(caminho):
#     with open(caminho, "r", encoding="utf-8") as f:
#         conteudo = f.readlines()

#     total_linhas = len(conteudo)
#     total_palavras = 0
#     total_caracteres = 0

#     contagem = {
#         "erro": 0,
#         "warning": 0,
#         "info": 0
#     }

#     for linha in conteudo:
#         palavras = linha.split()

#         total_palavras += len(palavras)
#         total_caracteres += len(linha)

#         for p in palavras:
#             if p in contagem:
#                 contagem[p] += 1

#         # Simulação de processamento pesado
#         for _ in range(1000):
#             pass

#     return {
#         "linhas": total_linhas,
#         "palavras": total_palavras,
#         "caracteres": total_caracteres,
#         "contagem": contagem
#     }



# # ===============================
# # Execução serial
# # ===============================

# def executar_serial(pasta):
#     resultados = []

#     inicio = time.time()

#     for raiz, _, arquivos in os.walk(pasta):
#         for arquivo in arquivos:
#             caminho = os.path.join(raiz, arquivo)
#             resultado = processar_arquivo(caminho)
#             resultados.append(resultado)

#     fim = time.time()

#     resumo = consolidar_resultados(resultados)

#     print("\n=== EXECUÇÃO SERIAL ===")
#     print(f"Arquivos processados: {len(resultados)}")
#     print(f"Tempo total: {fim - inicio:.4f} segundos")

#     print("\n=== RESULTADO CONSOLIDADO ===")
#     print(f"Total de linhas: {resumo['linhas']}")
#     print(f"Total de palavras: {resumo['palavras']}")
#     print(f"Total de caracteres: {resumo['caracteres']}")

#     print("\nContagem de palavras-chave:")
#     for k, v in resumo["contagem"].items():
#         print(f"  {k}: {v}")

#     return fim - inicio, resumo


# # ===============================
# # Main
# # ===============================

# if __name__ == "__main__":
#     pasta = "log2"

#     print("Executando versão serial...")
#     executar_serial(pasta)

# # import os
# # import time
# # import multiprocessing


# # # ===============================
# # # Consolidação dos resultados
# # # ===============================

# # def consolidar_resultados(resultados):
# #     total_linhas = 0
# #     total_palavras = 0
# #     total_caracteres = 0

# #     contagem_global = {
# #         "erro": 0,
# #         "warning": 0,
# #         "info": 0
# #     }

# #     for r in resultados:
# #         total_linhas += r["linhas"]
# #         total_palavras += r["palavras"]
# #         total_caracteres += r["caracteres"]

# #         for chave in contagem_global:
# #             contagem_global[chave] += r["contagem"][chave]

# #     return {
# #         "linhas": total_linhas,
# #         "palavras": total_palavras,
# #         "caracteres": total_caracteres,
# #         "contagem": contagem_global
# #     }


# # # ===============================
# # # Processamento de arquivo
# # # ===============================

# # def processar_arquivo(caminho):
# #     with open(caminho, "r", encoding="utf-8") as f:
# #         conteudo = f.readlines()

# #     total_linhas = len(conteudo)
# #     total_palavras = 0
# #     total_caracteres = 0

# #     contagem = {
# #         "erro": 0,
# #         "warning": 0,
# #         "info": 0
# #     }

# #     for linha in conteudo:
# #         palavras = linha.split()

# #         total_palavras += len(palavras)
# #         total_caracteres += len(linha)

# #         for p in palavras:
# #             if p in contagem:
# #                 contagem[p] += 1

# #         # Simulação de processamento pesado
# #         for _ in range(1000):
# #             pass

# #     return {
# #         "linhas": total_linhas,
# #         "palavras": total_palavras,
# #         "caracteres": total_caracteres,
# #         "contagem": contagem
# #     }


# # # ===============================
# # # Worker (Consumidor)
# # # ===============================

# # def worker(fila_entrada, fila_saida):
# #     while True:
# #         caminho = fila_entrada.get()

# #         if caminho is None:
# #             break

# #         resultado = processar_arquivo(caminho)
# #         fila_saida.put(resultado)


# # # ===============================
# # # Execução paralela
# # # ===============================

# # def executar_paralelo(pasta, num_processos):
# #     inicio = time.time()

# #     fila_entrada = multiprocessing.Queue(maxsize=10)  # buffer limitado
# #     fila_saida = multiprocessing.Queue()

# #     processos = []

# #     # Criar processos (consumidores)
# #     for _ in range(num_processos):
# #         p = multiprocessing.Process(target=worker, args=(fila_entrada, fila_saida))
# #         p.start()
# #         processos.append(p)

# #     # ===============================
# #     # PRODUTOR (substitui o for serial)
# #     # ===============================
# #     total_arquivos = 0

# #     for arquivo in os.listdir(pasta):
# #         caminho = os.path.join(pasta, arquivo)

# #         if os.path.isfile(caminho):  # evita erro com pastas
# #             fila_entrada.put(caminho)
# #             total_arquivos += 1

# #     # Enviar sinal de parada
# #     for _ in processos:
# #         fila_entrada.put(None)

# #     # Coletar resultados
# #     resultados = []
# #     for _ in range(total_arquivos):
# #         resultados.append(fila_saida.get())

# #     # Esperar processos terminarem
# #     for p in processos:
# #         p.join()

# #     fim = time.time()

# #     resumo = consolidar_resultados(resultados)

# #     print(f"\n=== EXECUÇÃO PARALELA ({num_processos} PROCESSOS) ===")
# #     print(f"Arquivos processados: {total_arquivos}")
# #     print(f"Tempo total: {fim - inicio:.4f} segundos")

# #     print("\n=== RESULTADO CONSOLIDADO ===")
# #     print(f"Total de linhas: {resumo['linhas']}")
# #     print(f"Total de palavras: {resumo['palavras']}")
# #     print(f"Total de caracteres: {resumo['caracteres']}")

# #     print("\nContagem de palavras-chave:")
# #     for k, v in resumo["contagem"].items():
# #         print(f"  {k}: {v}")

# #     return fim - inicio, resumo


# # # ===============================
# # # Main
# # # ===============================

# # if __name__ == "__main__":
# #     pasta = "log2"

# #     print("Executando versão paralela...")
# #     for n in [2, 4, 8, 12]:
# #         executar_paralelo(pasta, n)

import matplotlib.pyplot as plt

processos = [1, 2, 4, 8, 12]
tempos = [88.9626, 43.7899, 22.4725, 14.0759, 13.1807]
speedup = [1.0, 2.03, 3.96, 6.32, 6.75]
eficiencia = [1.0, 1.02, 0.99, 0.79, 0.56]

plt.plot(processos, tempos)
plt.xlabel("Processos")
plt.ylabel("Tempo (s)")
plt.title("Tempo de Execução")
plt.savefig("tempo_execucao.png")
plt.clf()

plt.plot(processos, speedup)
plt.xlabel("Processos")
plt.ylabel("Speedup")
plt.title("Speedup")
plt.savefig("speedup.png")
plt.clf()

plt.plot(processos, eficiencia)
plt.xlabel("Processos")
plt.ylabel("Eficiência")
plt.title("Eficiência")
plt.savefig("eficiencia.png")