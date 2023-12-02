
# InstaBot
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)

O InstaBot é uma ferramenta de automação intuitiva para o Instagram, projetada para aprimorar sua interação na plataforma. Ao facilitar o engajamento automático com postagens e perfis alinhados aos seus interesses, o InstaBot ajuda a construir uma presença digital mais autêntica e engajada. A chave aqui é a simplicidade: defina suas preferências de engajamento uma vez e deixe que o bot faça o resto, liberando você para focar no que realmente importa - criar conteúdo inspirador e cultivar uma comunidade genuína.

Criei o InstaBot porque entendo o valor do engajamento orgânico. Interações reais geram conexões reais, e é isso que impulsiona o crescimento sustentável no Instagram. Use o InstaBot para se conectar de forma consistente e significativa, sem sacrificar a personalização ou a qualidade das suas interações.

O InstaBot é seu assistente pessoal no Instagram, dando suporte para que você alcance seus objetivos de rede social com eficiência e eficácia.

## Funcionalidades
- **Autenticação Segura**: Faça login de forma segura utilizando suas credenciais do Instagram.
- **Engajamento Configurável**: Defina as porcentagens para comentar em postagens e seguir outros usuários.
- **Comentários Dinâmicos**: Crie e gerencie uma lista de comentários para serem usados pelo bot.
- **Filtragem por Localização**: Interaja com postagens baseadas em localizações específicas.
- **Registro de Atividades**: Mantenha-se informado sobre as ações do bot com um log de atividades.

## Pré-requisitos
Para utilizar o InstaBot, é necessário ter o Python instalado, bem como as bibliotecas `PyQT5` para a interface de usuário e `instagrapi` para a interação com a API do Instagram.

## Instalação
Clone o repositório ou faça o download do código-fonte, em seguida instale as dependências necessárias:

```bash
pip install -r requirements.txt
```
Para iniciar o InstaBot, execute o arquivo principal:

```bash
`python app.py` 
```
## Configuração Inicial

### Como obter as localizações e preencher o arquivo?
Siga este guia passo a passo para encontrar o código de localização no Instagram usando seu navegador e o site do Instagram. 
 1. Acessar o Instagram  
- Abra seu navegador web preferido. 
- Vá para a página de localizações do Instagram digitando na barra de endereços: `https://www.instagram.com/explore/locations/`. 
2. Procurar pela Localização  
 - Use a barra de busca para digitar o nome da localização que você está procurando. 
- Pressione `Enter` ou clique na lupa para realizar a busca. 
3. Selecionar a Localização  
  - Nos resultados da busca, clique na localização desejada. 
 4. Obter o Código de Localização  
 - Uma vez que a página da localização estiver aberta, olhe para a URL no seu navegador. 
 - A URL terá um formato parecido com: `https://www.instagram.com/explore/locations/CÓDIGO-DA-LOCALIZAÇÃO/nome-da-localização/`. 
 - O `CÓDIGO-DA-LOCALIZAÇÃO` é uma sequência de números. Este é o código de localização que você está procurando, copie-o. 
5. Salvar o Código de Localização
- Abra o arquivo `locations.txt` que você criou anteriormente no seu computador. Se você ainda não tem este arquivo, pode criá-lo usando um editor de texto como o Bloco de Notas no Windows ou o TextEdit no macOS.
- No arquivo `locations.txt`, você vai adicionar o nome da localização seguido de dois pontos `:` e então o código de localização que você copiou. Por exemplo, se você copiou o código da localização para Brasília e de São Paulo no mesmo arquivo, você escreveria assim:
```bash
Brasília, DF:112060958820146
São Paulo, SP:112047398814697
```
- Coloque cada localização e código em uma linha separada no arquivo. Isso ajudará a manter tudo organizado e fácil de encontrar mais tarde.
- Salve o arquivo `locations.txt` após adicionar o código de localização.
- Abra a aplicação seguindo os passos anteriores.

### Arquivo de comentários
- Crie um arquivo `txt` em qualquer pasta no seu computador no seu computador. Se você ainda não tem este arquivo, pode criá-lo usando um editor de texto como o Bloco de Notas no Windows ou o TextEdit no macOS.
- No arquivo, você vai adicionar um comentário por linha. Por exemplo:
```bash
Muito bom
Adorei
```
- Abra a aplicação seguindo os passos anteriores.
- Marque o checkbox Habilitar Comentários (obrigatório)
- Carregue o arquivo no botão Adicionar Comentário

## Como executar a aplicação

1.  Certifique-se que o arquivo `locations.txt` que criou anteriormente está na mesma pasta que a aplicação.
2. Execute a aplicação conforme explicado anteriormente.
3. Insira seu nome de usuário e senha do Instagram nos campos fornecidos.
4.  Configure as porcentagens para as ações de comentar, seguir e taxas de engajamento.
5.  Escolha uma localização para focar as interações.
6.  Inicie o bot e monitore as atividades através do log.

## Porcentagens recomendadas

1. **Porcentagem de comentários:** 40
2. **Porcentagem de seguir:** 25
3. **Porcentagem de engajamento:** Pode variar de acordo com a localização, teste o número que melhor funciona para você

## Lógica de Funcionamento

-   **Login**: O script tenta autenticar o usuário no Instagram, com tratamento de exceções para erros comuns, como senha incorreta.
-   **Seleção de Localização**: O bot pode interagir com postagens de uma localização específica, definida pelo usuário.
-   **Critérios de Engajamento**: São aplicados filtros para interagir apenas com postagens e usuários que atendem a certos critérios de seguidores, seguindo e taxa de engajamento.
-   **Interatividade**: O bot pode curtir postagens, seguir usuários e comentar em postagens automaticamente, baseando-se nas porcentagens configuradas.
-   **Humanização**: Pausas são implementadas para simular o comportamento humano e evitar penalidades na plataforma.
-   **Logging**: Todas as interações e ações significativas são registradas para que o usuário possa acompanhar o progresso do bot.
-   **Persistência**: As interações são salvas em um arquivo `.ini` para garantir que o bot não interaja com o mesmo usuário mais de uma vez.

## Estratégia de Engajamento

O aplicativo utiliza várias métricas para decidir se um perfil no Instagram é adequado para interação. A ideia é interagir com perfis que tenham uma boa taxa de engajamento para aumentar as chances de reciprocidade, o que, por sua vez, pode aumentar o engajamento do próprio usuário do aplicativo.

### Cálculo do Engajamento

1.  **Obtenção de Informações**: Para cada perfil identificado, o aplicativo obtém informações como a contagem de seguidores, a quantidade de pessoas que o perfil segue e as últimas postagens.
    
2.  **Taxa de Engajamento**: O aplicativo calcula a taxa de engajamento do perfil utilizando as últimas postagens. A fórmula utilizada é:
```bash
taxa_engajamento = (total_curtidas + total_comentarios) / (seguidores * postagens) * 100
```
-   **`total_curtidas`** e **`total_comentarios`** são somados das últimas postagens (limitadas a 10 pelo código).
-   **`seguidores`** é a contagem de seguidores do perfil.
-   **`postagens`** é o número de postagens que foram consideradas (até 10).

3.  **Filtros de Seleção**: O aplicativo aplica filtros baseados em critérios definidos, como a quantidade máxima de seguidores e seguindo, e a taxa mínima de engajamento configurada pelo usuário.
    
4.  **Decisão de Interação**: Se um perfil atender aos critérios de seleção e tiver uma taxa de engajamento acima do mínimo estabelecido pelo usuário do aplicativo, o bot pode interagir de várias maneiras:
    
    -   Curtindo postagens.
    -   Seguindo o perfil.
    -   Comentando nas postagens (se estiver habilitado e dentro da porcentagem configurada).

## Contribuição

Se deseja contribuir para o projeto, pode fazer um fork do repositório e enviar suas alterações através de pull requests.

## Licença

Este software é distribuído sob a licença MIT, o que permite o uso, cópia, modificação e distribuição livremente.
