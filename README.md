# Problemas de otimização em funções multimodais 

- [Definições](#def)
- [Desenvolvimento](#dev)
- [Resultados](#result)

<details>
<summary id="def"><h2><strong>1 - Definições</strong></h2></summary>
<hr>
 
As definições dos problemas estão todas [*aqui*](https://github.com/P-N-Suganthan/CEC2017-BoundContrained/tree/master) (Funções 3 a 9). \
A ênfase será em traçar o comparativo de resultados em dimensões **D = 2** e **D = 10**. \
O orçamento computacional seguirá a proporção: *ORCAMENTO* *=* *D* * *10000*. 

Este [*Repo*](https://github.com/tilleyd/cec2017-py) faz a implementação das funções multimodais e rotações, facilitando o trabalho. \
O foco aqui será em comparar os desempenhos dos algoritmos utilizando Python:
- Algoritmo Genético (*GA*), biblioteca PyGAD.
- Particle Swarm Optimization (*PSO*), biblioteca Pyswarm [^1].
</details>

<details>
<summary id="dev"><h2><strong>2 - Desenvolvimento</strong></h2></summary>
<hr>
 
Para a execução do algoritmo via PSO: PSOCec.py \
Para a execução do algoritmo GA: main.py
</details>

<details>
<summary id="result"><h2><strong>3 - Resultados</strong></h2></summary>
<hr> 
 
O resultado de ambos os algoritmos se equiparam. \
Dependendo do tipo de função a ser otimizada (f3, f4, etc.), o reajuste dos parâmetros melhora o resultado. \
Em desenvolvimento: implementação de uma melhoria no algoritmo PSO, chamado APSO [^2]. \
Aplicação em modelagem: obtenção de coeficientes em sistemas lineares [^3]. 

</details>
  
Referências:
[^1]: Exemplo de aplicação [Pyswarm](https://pyswarms.readthedocs.io/en/latest/examples/tutorials/basic_optimization.html#Optimizing-a-function-with-bounds).
[^2]: [REPO](https://github.com/ZongSingHuang/Adaptive-Particle-Swarm-Optimization) implementando PSO, já modificado para APSO.
[^3]: Cristhian Lima de Oliveira, Ewerton & Vidal, Juan & Silva, Orlando & Araújo, Jasmine. (2018). ESTUDO COMPARATIVO DE TÉCNICAS DE INTELIGÊNCIA DE ENXAME DE PARTÍCULAS NA IDENTIFICAÇÃO DE SISTEMAS LINEARES. (DOI: 10.20906/CPS/CBA2018-0200). 
