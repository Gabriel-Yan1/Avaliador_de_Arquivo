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
Os resultados mostram uma redução significativa no tempo de execução com o aumento do número de processos, confirmando o ganho proporcionado pela paralelização.

O tempo serial foi de aproximadamente 88,96 segundos. Com 2 processos, o tempo caiu para cerca de 43,79 segundos, resultando em um speedup de aproximadamente 2,03 e eficiência de 1,02 — ligeiramente acima do ideal, possivelmente devido a otimizações internas do sistema.

Com 4 processos, o tempo caiu para 22,47 segundos, o que representa um speedup de 3,96 e uma eficiência próxima a 0,99, demonstrando excelente aproveitamento do paralelismo até esse ponto.

Ao aumentar para 8 processos, o tempo reduziu para 14,08 segundos, porém o speedup (6,32) não cresceu de forma proporcional, e a eficiência caiu para 0,79, indicando início da sobrecarga da paralelização.

Com 12 processos, o tempo foi 13,18 segundos, um ganho modesto em relação a 8 processos, com speedup de 6,75 e eficiência caindo para 0,56, evidenciando saturação do sistema.

Essa perda de eficiência após 4 processos pode ser atribuída a fatores como overhead na criação e gerenciamento dos processos, comunicação e sincronização entre eles, contenção de recursos da CPU e limitações de I/O.

Além disso, o número de processos provavelmente ultrapassou a quantidade de núcleos físicos disponíveis, o que gera competição por recursos e troca constante de contexto, reduzindo o ganho potencial.

Portanto, o paralelismo é eficiente e escalável até um certo limite, mas apresenta retornos decrescentes conforme o número de processos ultrapassa a capacidade física da máquina.

# 11. Conclusão
A implementação paralela proporcionou um ganho substancial em relação à execução serial, reduzindo significativamente o tempo total de processamento.

O desempenho ideal foi observado na faixa entre 4 e 8 processos, onde o speedup foi mais eficiente, alinhado ao número de núcleos físicos da máquina.

Acima desse limite, os ganhos se tornam menos expressivos devido ao overhead inerente à paralelização e à limitação dos recursos computacionais disponíveis.

Embora o programa apresente boa escalabilidade inicial, o aumento do paralelismo não resulta em melhorias lineares em todas as configurações testadas.

Para aprimorar o desempenho, recomenda-se investigar estratégias como a redução da comunicação entre processos, a utilização de pools de processos para minimizar custos de criação e destruição, ajuste do tamanho do buffer para otimizar o fluxo de dados e implementação de técnicas de balanceamento de carga mais refinadas.

Conclui-se que a paralelização é uma solução eficaz para o problema, desde que calibrada conforme a capacidade do hardware utilizado, garantindo assim o melhor aproveitamento dos recursos disponíveis.
