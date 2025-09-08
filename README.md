📌Trackin.API - Sprint 3 / CP 04 .NET
======================

📖Descrição do Projeto
--------------------

O **Trackin.API** é uma API RESTful desenvolvida com ASP.NET Core 8 para automatizar o mapeamento e monitoramento de motocicletas nos pátios da Mottu. Esta solução integra tecnologias como RFID e visão computacional (ML.NET) para localização em tempo real, utilizando uma arquitetura em camadas robusta. A implementação desta primeira sprint foca nos requisitos iniciais:

-   CRUD completo para entidades principais (`Moto`, `Patio`, `SensorRFID`, `ZonaPatio`) com mais de 3 rotas GET parametrizadas.
-   Integração com banco de dados SQL Server via Entity Framework Core (EF Core), utilizando migrations para criação de tabelas.
-   Documentação da API via OpenAPI com interface gráfica (Swagger).

O domínio está completamente mapeado com todas as entidades definidas, mas nem todas as rotas definidas foram implementadas até o momento.

## 🌐 Descrição do Domínio

O **Trackin.API** organiza e gerencia o monitoramento de motocicletas nos pátios da Mottu, fornecendo **rastreamento em tempo real**, registro de localização, status e movimentação das motos, além de gestão de pátios e sensores.  

A aplicação segue uma **arquitetura em camadas**, garantindo escalabilidade e facilidade de manutenção, e está estruturada com as seguintes regras de negócio e conceitos do domínio:

- Cada **Moto** pertence a um único **Pátio** e possui um **RFID único**. Seu modelo e ano são validados, garantindo consistência nos registros.
- Os **Pátios** são representados com dimensões físicas, endereço completo e planta baixa opcional, permitindo localizar e organizar zonas internas.
- Cada **Zona do Pátio** define uma área específica, com tipo (como entrada, saída ou estacionamento), coordenadas e cor de identificação.
- Os **Sensores RFID** são vinculados a zonas, registrando leituras automáticas das motos, incluindo posição, altura e ângulo de visão.
- As **leituras de RFID** são armazenadas com timestamp, status da moto e confiabilidade da informação, permitindo monitoramento preciso.
- A API oferece **CRUD completo** para todas as entidades principais, consultas parametrizadas, paginação e ordenação dos resultados.

O domínio garante **consistência, rastreabilidade e integridade dos dados**, permitindo expansão futura para monitoramento avançado, relatórios e integrações externas.


👨‍💻Participantes
-------------------
- Julia Brito - RM 558831
- Leandro Correia - RM 556203
- Victor Antonopoulos - RM 556313

📌Rotas Implementadas
-------------------

Abaixo estão as rotas implementadas, baseadas nos controllers fornecidos. Todas seguem padrões RESTful e retornam os status HTTP apropriados (200 OK, 201 Created, 204 No Content, 400 Bad Request, 404 Not Found, 500 Internal Server Error).

### 🚲MotoController

-   **POST /api/moto**\
    Cria uma nova moto.
-   **GET /api/moto**\
    Retorna motos com paginação.
-   **GET /api/moto/{id}**\
    Retorna uma moto pelo seu ID.
-   **PUT /api/moto/{id}**\
    Atualiza uma moto existente.
-   **DELETE /api/moto/{id}**\
    Exclui uma moto pelo ID.
-   **GET /api/moto/all**\
    Retorna todas as motos.
-   **GET /api/moto/patio/{patioid}**\
    Retorna todas as motos de um determinado pátio com paginação.
-   **GET /api/moto/status/{status}**\
    Retorna motos por status com paginação.
-   **POST /api/moto/{id}/imagem**\
    Adiciona uma imagem base64 como referência para uma moto.

### 🅿️PatioController

-   **GET /api/patio**\
    Recupera todos os pátios cadastrados no sistema com paginação.
    **POST /api/patio**\
    Cria um novo pátio.
-   **GET /api/patio/all**\
    Recupera todos os pátios cadastrados no sistema.
-   **GET /api/patio/{id}**\
    Recupera um pátio específico pelo seu ID.
-   **DELETE /api/patio/{id}**\
    Remove um pátio existente.

### 📡RFIDController

-   **POST /api/rfid**\
    Processa uma leitura RFID e atualiza a localização/status da moto.

### 🔌SensorRFIDController

-   **GET /api/sensorRFID**\
    Recupera todos os sensores RFID cadastrados com paginação.
    **POST /api/sensorRFID**\
    Cria um novo sensor RFID.
-   **GET /api/sensorRFID/all**\
    Recupera todos os sensores RFID cadastrados.
-   **GET /api/sensorRFID/{id}**\
    Recupera um sensor RFID específico pelo seu ID.
-   **PUT /api/sensorRFID/{id}**\
    Atualiza um sensor RFID existente.
-   **DELETE /api/sensorRFID/{id}**\
    Remove um sensor RFID existente.

### 🏗️ZonaPatioController

-   **GET /api/zonaPatio**\
    Recupera todas as zonas do pátio cadastradas com paginação.
    **POST /api/zonaPatio**\
    Cria uma nova zona de pátio.
-   **GET /api/zonaPatio/all**\
    Recupera todas as zonas de pátio cadastradas.
-   **GET /api/zonaPatio/{id}**\
    Recupera uma zona de pátio específica pelo seu ID.
-   **PUT /api/zonaPatio/{id}**\
    Atualiza uma zona de pátio existente.
-   **DELETE /api/zonaPatio/{id}**\
    Remove uma zona de pátio existente.

### 1️⃣ Exemplo de Requisição: Criar Moto (POST /api/Moto)

```json
{
  "patioId": 1,
  "placa": "ABC1234",
  "modelo": "HondaCG160",
  "ano": 2023,
  "rfidTag": "RFID123456"
}
```
### 2️⃣ Exemplo de Requisição: Criar Pátio (POST /api/Patio

```json
{
  "nome": "Pátio Central",
  "endereco": "Av. Brasil, 1234",
  "cidade": "São Paulo",
  "estado": "SP",
  "pais": "Brasil",
  "dimensaoX": 500,
  "dimensaoY": 300,
  "plantaBaixa": "planta_central.png"
}

```
### 3️⃣ Exemplo de Requisição: Criar Sensor RFID (POST /api/SensorRFID

```json
{
  "zonaPatioId": 1,
  "patioId": 1,
  "posicao": "Entrada Leste",
  "posicaoX": 100,
  "posicaoY": 200,
  "altura": 5,
  "anguloVisao": 90
}

```
### 4️⃣ Exemplo de Requisição: Zona de Pátio (POST /api/ZonaPatio

```json
{
  "patioId": 1,
  "nome": "Zona A",
  "tipoZona": 0,
  "coordenadaInicialX": 0,
  "coordenadaInicialY": 0,
  "coordenadaFinalX": 100,
  "coordenadaFinalY": 50,
  "cor": "#FF0000"
}

```
⚙️Instalação
----------

Siga os passos abaixo para configurar e executar o projeto localmente:

### ✅Pré-requisitos

-   **.NET 8 SDK**: [Download](https://dotnet.microsoft.com/download/dotnet/8.0)
-   **Docker**: Para executar o container do SQL Server. [Download](https://www.docker.com/get-started)
-   **Git**: Para clonar o repositório.

### Passos de Instalação

1.  **🔽Clone o Repositório**
    -   Github:

        ```bash
        git clone https://github.com/correialeo/TRACKIN.git
        ```
    -   Azure Devops:
    
        ```bash
        git clone https://Challenge2025-Mottu@dev.azure.com/Challenge2025-Mottu/Mottu/_git/trackin.dotnet.api
        # Ou via SSH:
        git clone git@ssh.dev.azure.com:v3/Challenge2025-Mottu/Mottu/trackin.dotnet.api
        ```

2.  **🗄️Configure o SQL Server via Docker**

    -   Execute o seguinte comando para criar um container do SQL Server:

        ```bash
        docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=YourStrong@Passw0rd"  -p 1433:1433 --name sqlserver-trackin  -d mcr.microsoft.com/mssql/server:2022-latest
        ```
        - ⚠Verifique e modifique de acordo com seu SO.

    -   Aguarde alguns segundos para o container inicializar completamente.

3.  **⚠️Configure as Variáveis de Ambiente**

    -   Copie o arquivo `.env.example` para `.env` na raiz do projeto:

        ```bash
        cp .env.example .env
        ```

    -   Edite o arquivo `.env` com as credenciais do SQL Server:

        ```env
        // Aqui você deve por o servidor e a porta do banco de dados SQLServer (ex: localhost,1433)
        DATABASE__SOURCE='localhost,1433'
        // Aqui você deve por o usuário do banco de dados SQLServer
        DATABASE__USER='sa'
        // Aqui você deve por a senha do banco de dados SQLServer
        DATABASE__PASSWORD='YourStrong@Passw0rd'
        DATABASE__NAME='TrackinDb'
        ```

4.  **📦Restaure as Dependências**

    -   A partir da pasta raiz do projeto, execute o comando para restaurar os pacotes NuGet:

        ```bash
        dotnet restore
        ```

5.  **🗄️Configure a Conexão com o Banco de Dados**

    -   Certifique-se de que o container do SQL Server está rodando:

        ```bash
        docker ps
        ```

    -   Você deve ver o container `sqlserver-trackin` na lista com status "Up".

6.  **🏗️Aplique as Migrations**
    
    -   Entre na pasta raíz src:
        ```bash
        cd src
        ```
    -   Aplique as migrations para criar as tabelas no banco de dados SQL Server:
      
        ```bash
        dotnet ef database update --project Trackin.Infrastructure --startup-project Trackin.Api
        ```

    -   Se houver erros, verifique se o container está rodando e se as configurações no `.env` estão corretas.

8.  **▶️Execute a Aplicação**

    -   Inicie o projeto: (ainda dentro de src):

        ```bash
        dotnet run --project Trackin.Api
        ```
        - Se preferir, rode com F5 no vscode.

    -   A API estará disponível em `https://localhost:5007` (ou a porta configurada).

9.  **Acesse a Documentação Swagger**

    -   Acesse `https://localhost:5007/swagger` para explorar e testar os endpoints.

### 🐳Comandos Úteis do Docker

-   **Parar o container:**
    ```bash
    docker stop sqlserver-trackin
    ```

-   **Iniciar o container novamente:**
    ```bash
    docker start sqlserver-trackin
    ```

-   **Remover o container:**
    ```bash
    docker rm sqlserver-trackin
    ```

-   **Ver logs do container:**
    ```bash
    docker logs sqlserver-trackin
    ```

### 📌Observações

-   O SQL Server precisa de pelo menos 2GB de RAM para funcionar adequadamente.
-   A senha do SQL Server deve atender aos requisitos de complexidade (pelo menos 8 caracteres, maiúsculas, minúsculas, números e símbolos).
-   Verifique se a porta 1433 não está sendo usada por outra aplicação.
-   O Dockerfile da aplicação está localizado dentro da pasta `Trackin.API`.

Notas Adicionais
----------------

-   Esta é a implementação da primeira sprint, atendendo aos requisitos mínimos de CRUD, integração com SQL Server via EF Core, e documentação Swagger.
-   Nem todas as rotas previstas na arquitetura estão implementadas; o foco foi nos controllers listados acima.
-   O banco de dados `TrackinDb` será criado automaticamente ao executar as migrations.

## Documentação Complementar

📄 [Baixar Documento Complementar (PDF)](doc_challenge_dotnet.pdf)

☁️Scripts Azure CLI (Devops)
----------------
Criação Resource Group e VM:
```bash
az group create --name RG-ChallengeNET --location eastus

az vm create \
  --resource-group RG-ChallengeNET \
  --name VM-ChallengeNET \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --public-ip-sku Standard
```

Abertura de Portas:
```bash
az vm open-port --resource-group RG-ChallengeNET --name VM-ChallengeNET --port 80 --priority 1001
az vm open-port --resource-group RG-ChallengeNET --name VM-ChallengeNET --port 443 --priority 1002
az vm open-port --resource-group RG-ChallengeNET --name VM-ChallengeNET --port 5000 --priority 1003
az vm open-port --resource-group RG-ChallengeNET --name VM-ChallengeNET --port 8080 --priority 1010
az vm open-port --resource-group RG-ChallengeNET --name VM-ChallengeNET --port 8081 --priority 1011
```

