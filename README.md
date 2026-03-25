# Relatório da Paralelização de Processamento de Logs

**Disciplina:** Programação Paralela  
**Aluno(s):** Gabriel Yan

**Turma:** SI  
**Professor:** Rafael  
**Data:** 25/03/2026 

---

# 1. Descrição do Problema

O problema consiste no processamento de grandes volumes de arquivos de log contendo informações operacionais. Cada arquivo deve ser analisado para extrair métricas como número de linhas, palavras, caracteres e ocorrência de palavras-chave ("erro", "warning" e "info").

O programa foi inicialmente implementado de forma sequencial, processando um arquivo por vez. Para melhorar o desempenho, foi desenvolvida uma versão paralela utilizando o modelo produtor-consumidor.

O algoritmo utilizado percorre todos os arquivos de uma pasta, lê seu conteúdo e realiza contagens básicas. A paralelização foi feita distribuindo os arquivos entre múltiplos processos.

O volume de dados utilizado nos testes foi a pasta **log2**, contendo aproximadamente 1000 arquivos grandes.

A complexidade do algoritmo é aproximadamente:

- **O(N × M)**  
Onde:
- N = número de arquivos  
- M = tamanho médio de cada arquivo  

## Respostas

- Objetivo: reduzir o tempo de processamento de arquivos de log  
- Volume de dados: ~1000 arquivos (log2)  
- Algoritmo: processamento sequencial de arquivos + contagem de palavras  
- Complexidade: O(N × M)  

---

# 2. Ambiente Experimental

| Item                        | Descrição |
| --------------------------- | --------- |
| Processador                 | 12th Gen Intel(R) Core(TM) i7-12700 |
| Número de núcleos           | 12 |
| Memória RAM                 | 16,0 GB |
| Sistema Operacional         | Windows 11 Pro |
| Linguagem utilizada         | Python |
| Biblioteca de paralelização | multiprocessing |
| Versão do Python            | Python 3.13.2 |

---

# 3. Metodologia de Testes

O tempo de execução foi medido utilizando a função `time.time()`, considerando o intervalo entre o início e o fim da execução.

Para cada configuração (1, 2, 4, 8 e 12 processos), foram realizadas **3 execuções**, sendo calculada a média dos tempos.

Os testes foram executados em máquina local, sem outras aplicações pesadas em execução.

### Configurações testadas

- 1 processo (serial)
- 2 processos
- 4 processos
- 8 processos
- 12 processos

### Procedimento

- Cada configuração foi executada 3 vezes
- Foi calculada a média dos tempos
- A máquina foi mantida com baixa carga durante os testes

---
# 4. Resultados Experimentais

| Nº Processos | Tempo (s) |
|-------------|----------|
| 1           | 88.9626  |
| 2           | 43.7899  |
| 4           | 22.4725  |
| 8           | 14.0759  |
| 12          | 13.1807  |

---

# 5. Cálculo de Speedup e Eficiência

### Fórmulas

Speedup(p) = T(1) / T(p)  
Eficiência(p) = Speedup(p) / p  

---

# 6. Tabela de Resultados

| Processos | Tempo (s) | Speedup | Eficiência |
|-----------|-----------|---------|------------|
| 1        | 88.9626    | 1.0     | 1.0        |
| 2        | 43.7899    |2.03     | 1.02       |
| 4        | 22.4725    | 3.96    | 0.99       |
| 8        | 14.0759    | 6.32    | 0.79       |
| 12       | 13.1807    |6.75     | 0.56       |

---

# 7. Gráfico de Tempo de Execução

<img width="750" height="446" alt="image" src="https://github.com/user-attachments/assets/4ba9e4aa-f4c3-40fb-b0bd-4bd12333a09b" />



---

# 8. Gráfico de Speedup

<img width="750" height="446" alt="image" src="https://github.com/user-attachments/assets/18ed63c9-f0ba-4218-a14c-6c067e9edc5f" />



---

# 9. Gráfico de Eficiência

<img width="750" height="446" alt="image" src="https://github.com/user-attachments/assets/df7b1a3d-1276-424f-8c53-d7dbd6812e40" />



---

# 10. Análise dos Resultados
Observa-se que houve uma redução significativa no tempo de execução com o aumento do número de processos.

O speedup obtido foi próximo do ideal até 4 processos, indicando boa utilização dos recursos da máquina. Para 2 processos, o speedup foi ligeiramente superior a 2, o que pode ser explicado por efeitos de cache e otimizações do sistema operacional.

A partir de 8 processos, o ganho de desempenho começa a diminuir, e a eficiência cai, indicando a presença de overhead de paralelização.

Com 12 processos, o ganho adicional é pequeno em relação a 8 processos, mostrando que o sistema atingiu um ponto de saturação.

Isso ocorre devido a fatores como:

- Overhead na criação e gerenciamento de processos
- Comunicação entre processos via filas (Queue)
- Contenção de CPU
- Limitações de acesso à memória e disco

Provavelmente o número de processos ultrapassou o número de núcleos físicos da máquina, causando competição por recursos.

Portanto, a aplicação apresenta boa escalabilidade até certo ponto, mas com perda de eficiência em níveis mais altos de paralelismo.

# 11. Conclusão
A paralelização trouxe um ganho significativo de desempenho em relação à execução serial.

O melhor desempenho foi observado entre 4 e 8 processos, onde o speedup foi mais eficiente.

A partir de 8 processos, os ganhos diminuem devido ao aumento do overhead e limitação de recursos da máquina.

O programa apresentou boa escalabilidade inicial, mas não linear para todos os níveis de paralelismo.

Como melhorias futuras, podem ser consideradas:

- Redução da comunicação entre processos
- Uso de pools de processos
- Ajuste do tamanho do buffer
- Melhor balanceamento de carga

Conclui-se que o uso de paralelismo é eficiente para este tipo de problema, mas deve ser ajustado conforme a capacidade do hardware.
