# Chatbot Virtual com Langchain

Este é um projeto de chatbot virtual criado com a biblioteca **LangChain**, **Streamlit**, e diferentes modelos de IA, como o **Hugging Face Hub**, **Ollama**, e **OpenAI GPT**. O chatbot é projetado para fornecer respostas em português e pode ser facilmente personalizado para responder a diferentes tipos de perguntas.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criação de interfaces interativas de dados.
- **LangChain**: Framework de Python para facilitar o desenvolvimento de pipelines de IA com LLMs (Modelos de Linguagem de Grande Escala).
- **HuggingFaceHub**: Interface para acessar modelos hospedados no Hugging Face Hub.
- **Ollama**: Biblioteca para integrar o modelo de IA Ollama.
- **OpenAI**: Biblioteca para acessar os modelos de IA da OpenAI.
- **dotenv**: Para carregamento de variáveis de ambiente do arquivo `.env`.

## Como Começar

Siga os passos abaixo para executar o chatbot localmente.

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-virtual.git
cd chatbot-virtual
```

### 2. Criar um ambiente virtual

Recomenda-se usar um ambiente virtual para instalar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate  # Para Windows
```

### 3. Instalar as dependências

Instale as dependências do projeto utilizando o `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API para o Hugging Face (Hugging Face API Key) ou outros serviços que você deseja utilizar:

```env
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

### 5. Executar o aplicativo

Execute o aplicativo Streamlit com o comando abaixo:

```bash
streamlit run chatbot.py
```

Isso abrirá o aplicativo do chatbot no seu navegador.

## Estrutura do Projeto

- **chatbot.py**: Arquivo principal que configura a interface com o usuário utilizando o Streamlit e interage com o modelo de IA.
- **chain.py**: Contém a lógica para gerar a resposta do chatbot, incluindo a criação do prompt e interação com o modelo de IA.
- **model.py**: Define as classes para instanciar os modelos de IA, como o HuggingFaceHub, Ollama, e OpenAI.
- **.env**: Arquivo para armazenar as variáveis de ambiente, como chaves de API.

## Como Funciona

1. O usuário envia uma mensagem via interface do **Streamlit**.
2. A mensagem é processada e enviada para a função `generate_response` em **chain.py**.
3. A função `generate_response` cria um prompt com o histórico da conversa e envia a consulta ao modelo de IA apropriado.
4. O modelo de IA retorna uma resposta que é exibida para o usuário via **Streamlit**.

## Personalização

Você pode facilmente modificar o tipo de modelo de IA a ser utilizado no arquivo `model.py`. Basta ajustar o parâmetro `model_type` ao inicializar o **FactoryModel** no arquivo `chain.py`:

- `"hf_hub"`: Para usar modelos do Hugging Face.
- `"ollama"`: Para usar o modelo Ollama.
- `"openai"`: Para usar o modelo da OpenAI.



### Exemplo da interface do chatbot:


## Licença

Este projeto é de código aberto, licenciado sob a licença MIT

## Contribuições

Sinta-se à vontade para fazer contribuições! Se você tiver alguma sugestão ou correção, envie um pull request ou abra um issue.

---