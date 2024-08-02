# Sobre Pontos Interiores
Trata-se de uma técnica poderosa utilizada na otimização linear para encontrar soluções de problemas de programação linear. Diferente do Método Simplex, que navega pelas bordas do espaço viável, o Método dos Pontos Interiores percorre o interior do espaço viável para encontrar a solução ótima.  
É particularmente útil em problemas de larga escala devido sua eficiência computacional, bem como suas aplicações em Otimização Não-Linear.  
A abordagem se baseia em uma função de barreira que impede que as iterações se aproximem das bordas do espaço viável, permitindo que o algoritmo se concentre nas regiões interiores. Como resultado, o Método dos Pontos Interiores pode convergir rapidamente para a solução ótima, tornando-se uma escolha preferida em muitas aplicações de otimização.

<img src="https://github.com/user-attachments/assets/b26ffbfc-3001-454d-99f9-c8d856fbeec4" alt="Exemplo" style="width:500px;"/>  

Os créditos da imagem são do autor [Jeremy Bleyer](https://www.scopus.com/authid/detail.uri?authorId=55574535900) em seu trabalho [Advances in the simulation of viscoplastic fluid flows using interior-point methods](https://www.sciencedirect.com/science/article/abs/pii/S0045782517307119)

## Sobre o Projeto

As implementações presentes neste repositório foram feitas com proposta educacional para aprendizado em Otimização Linear, e baseiam-se na metodologia do professor [Marcos Arenales](http://www.otm.icmc.usp.br/index.php/pt/pessoas/professores/26-arenales) em seu livro [Pesquisa Operacional](https://www.amazon.com.br/Pesquisa-Operacional-Marcos-Arenales/dp/8535214542).

# Como usar?

## Rodando pelo Colab (ambiente virtual)

1. Acesso o [Google Colab](https://colab.new/)  
2. Abra o menu de contexto **Arquivo** e selecione a opção **Abrir Notebook**  <img src="https://github.com/user-attachments/assets/613baa3f-b12c-42cd-bb8d-e53fc7fdb931" alt="Passo 2" style="width:500px;"/>  
3. Selecione o contexto **Github** e insira o link: https://github.com/rafflezs/MetodoBarreira-OtmLinear-ICMC/blob/main/notebook/pontos-interiores.ipynb  <img src="https://github.com/user-attachments/assets/7680d78f-0421-48c3-8f9c-363b8b9fe4bc" alt="Passo 3" style="width:500px;"/> 
 

Basta selecionar o arquivo e o mesmo será carregado à página.

## Rodando Localmente

Caso opte pela execução local, certifique-se de ter instalado [Python 3](https://www.python.org/downloads/) em seu computador, juntamente dos pacotes **matplotlib** e **numpy**.
Apos isso, basta executar o arquivo src/main.py

# Propostas de Melhoria

Obviamente o projeto não está completo (sinceramente nem foi despendido um tempo tão grandioso assim), então existem pontos à serem melhorados, **principalmente** na computação do sistema KKT, onde é implementado um sistema grande com alto custo.  
Caso tenha alguma proposta de melhoria, correção ou documentação, sinta-se a vontade para enviar uma _pull request_ que irei avaliar.

# Aviso
Este código foi feito para própositos educativos, como método avaliativo na disciplina de [Otimização Linear 2 - SME5902](https://www.icmc.usp.br/pos-graduacao/disciplinas?programa=55134&disciplina=SME5902).  
Por essa razão o mesmo não está completamente otimizado e pode apresentar erros ainda não testados, portanto **não use-o** em ambientes de produção.  

**Quaisquer problemas causados pelo uso desse projeto em ambientes não-educacionais ou de estudo são de responsabilidade do usuário.**
