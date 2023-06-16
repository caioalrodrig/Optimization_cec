
# Otimização Combinatória: Problema do Caixeiro Viajante :compass:


- [Definições](#def)
- [Metodologia](#instrument)
- [Resultados](#result)

 <details>
<summary id ="def"><h2><strong>1 - Definições</strong></h2></summary>

---
   
O problema é levantado no trabalho conhecido como TSPLib [^1] e possui diversos *rotas*, cada um com diversas *subrotas*, em variadas dimensões (simples, médias e as mais complexas). Alguns dos problemas propõem formas de distância entre as *cidades* baseados na distância Euclidiana. Outros seguem distâncias ponderadas e outros utilizam baseam-se na distância gemétrica.

Para os exemplos deste repositório foram trabalhadas apenas as distâncias Euclidianas, e a distância ponderada (problemas ATSP).
O problema TSP com distância Euclidiana utiliza a seguinte definição de distância entre cidades:

```math
  d(\mathbf{p}, \mathbf{q}) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}
```
Já o problema ATSP trabalha com a distância em formato matricial (diagonais *dont-care*), onde a distância entre a cidade n e a cidade m vale: 

```math
d_{nm}=
\begin{bmatrix}
999999 & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & 999999 & a_{23} & \dots & a_{2n} \\
a_{31} & a_{32} & 999999 & \dots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & 999999 \\
\end{bmatrix}
```

 </details>
 <!-- ################################################################2#################################################### -->
<details>
 <summary id="instrument"> <h2> <strong>2 - Metodologia </h2> </strong> </summary>
 
---
- Importação dos arquivos .txt,
  - RunTSP.py para arquivos TSP.  
  - RunATSP.py para arquivos ATSP.
  
- Uso da biblioteca *PYGad* para algoritmo genético [^2],
- Implementações de operadores personalizados ao TSP,
    - Problema **exige** não-repetição, os básicos operadores aqui implementados (cross-over e mutação) dão esta garantia.
- Execução individual com orçamento computacional (n de execuções):
  - **Se** D<50: 50000.
  - **Se-não**: 70000.
- API com NetworkNx [^3] para visualização do *melhor* por geração.


</details>
<!-- ################################################################2#################################################### -->
<details>
 <summary id="result"> <h2> <strong>3- Resultados </h2> </strong> </summary>

Os problemas de ordem menor apresentaram erro relativo baixo

| | B52  | Ch130 | Br17  | Ftv70 |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| **Obtido**  | 8805  | 9560  | 39  | 2439  |
| **Ótimo** | 7542 | 6110 | 39  | 1950 |
| **Erro rel. (%)**  | 17  | 56 | 0  | 25  |


</details>

[^1]: Instâncias do problema, resultados ótimos e temas relacionados. [Site institucional Universitàt Heindelberg](http://comopt.ifi.uni-heidelberg.de/software/)  
[^2]: Documentação da biblioteca [PYGAD](https://pygad.readthedocs.io/en/latest/README_pygad_ReadTheDocs.html).

[^3]: Network NX
