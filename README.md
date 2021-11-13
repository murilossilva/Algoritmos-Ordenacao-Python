<h1>Algoritmos de Ordenação em Python</h1>

Esse repositório é resultado de um estudo sobre Estrutura de Dados, com os principais métodos de ordenação. Os algoritmos aqui estruturados e estudados são:

- Bubble Sort
- Insertion Sort
- Selection Sort

<h4>Requirements</h4>

- Os programas foram estruturados e testados em Python v3.9, caso sejam utilizadas versões diferentes não é possível assegurar a sua total funcionalidade.

<h3>Bubble Sort</h3>
O Bubble Sort geralmente é o pontapé inicial para o estudo de algoritmos de ordenação, principalmente os de origem simples, pois seu entendimento é mais simplista, o que um algoritmo de ordenação ruim considerando a situação. O caso ideal para a sua utilização é em momentos em que o vetor está quase ordenado, ou seja, poucos elementos precisam ser iterados. Mas por quê? 
<br></br>
O método utilizado pelo bubble sort é a varredura de elemento por elemento de um determinado vetor, onde para cada elemento ele verifica se o mesmo é maior do que o elemento seguinte, caso seja, os elementos trocam suas posições no vetor, seguindo esses pasos por todo o vetor, até o seu penúltimo elemento. Por conta dessas trocas exaustivas, o algoritmo acaba tornando-se lento para vetores que possuem muitos índices desordenados, onde o seu pior caso são para vetores ordenados de forma inversa. Uma melhoria implementada no código desse repositório é a verificação de se é necessária a troca, caso não seja necessária o laço de repetição passa para o próximo índice (ou elemento), o que diminui consideralvemente o número de vezes que o vetor é percorrido, o que gera um aumento do desempenho.

<h3>Insertion Sort</h3>
O algoritmo de inserção ou Insertion Sort é um algoritmo superior ao Bubble Sort em casos como: vetor totalmente desordenado, vetor invertido. O seu método assemelha-se muito com a forma de organizar as mãos em jogos de cartas, onde seleciona-se uma carta e observa-se se as suas cartas à esquerda são maiores, caso haja alguma carta que não é menor do que a carta em questão, posiciona-se a carta à frente daquela de menor valor, repetindo esse passo até ter todas as cartas organizadas de forma crescente.
<br></br>
A implementação desse algoritmo também é relativamente fácil, o valor do índice atual é guardado numa variável auxiliar e após isso um laço de repetição percorre os índices anteriores, caso o valor do índice anterior seja maior, o laço continua percorrendo o vetor até que haja um valor menor, realizando a troca entre o último índice e o valor na variável auxiliar. A grande diferença desse algoritmo pro Bubble Sort é a capacidade de trocar diretamente pro índice apropriado, diminuindo o número de passagens do laço pelo vetor, assim como o número de atribuições em seu melhor caso.
<br></br>
Mas quando é o pior caso do Insertion Sort? O pior caso para esse algoritmo é quando o vetor está invertido, pois a condição de o elemento anterior ser maior que o atual vai ser sempre verdadeira, até que o vetor esteja completamente ordenado, o que eleva o algoritmo ao máximo de iterações possíves.

<h3>Selection Sort</h3>
O algoritmo de seleção ou Selection Sort é bem parecido com o Insertion Sort, o objetivo do Selection Sort é realizar a menor quantia de atribuições possíveis, ou mantê-las em um nível próximo independente do vetor. Mas como funciona esse algoritmo?
<br></br>
O Selection Sort tem o seu funcionamento baseado em percorrer todo o vetor em busca do menor valor presente nele. Ao encontrar esse menor valor ele o posiciona na primeira posição do vetor e repete esse funcionamento para os índices seguintes. O menor valor sempre é guardado em uma variável auxiliar e comparado com o valor do índice atual, caso esse seja menor que o valor na auxiliar, a variável assume o seu valor. Ou seja, ele funciona por seleção, já que seleciona sempre o menor número e o aloca no índice atual do primeiro laço. O seu pior caso é quando o vetor já está quase ordenado, pois ele continua realizando as comparações entre os índices, ou seja, a principal característica do Selection Sort é manter um desempenho linear.

<h3>Social Medias</h3>

- Instagram: https://www.instagram.com/original.mancha/
- Twitter: https://twitter.com/printmurilo
- LinkedIn: https://www.linkedin.com/in/murilossilva/
