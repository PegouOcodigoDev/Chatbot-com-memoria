from langchain_core.prompts import MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from model import FactoryModel


def create_prompt(system_prompt, user_prompt, model_type):
    if model_type.startswith("hf"):
        user_prompt = (
            "<|start_header_id|>system<|end_header_id|><|eot_id|>"
            "<|start_header_id|>user<|end_header_id|>{}<|eot_id|>"
            "<|start_header_id|>assistant<|end_header_id|><|eot_id|>".format(user_prompt)
        )

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("user", user_prompt),
        ]
    )
    
    return prompt_template


def get_model(model_type):
    model_factory = FactoryModel(model_type=model_type)
    model = model_factory.get_model()
    return model


def generate_response(query, history, model_type="hf_hub"):
    try:
        prompt_template = create_prompt("Você é um assistente prestativo e está respondendo perguntas gerais. Responda as perguntas em português.",
            "{input}",
            model_type)
        
        llm = get_model(model_type)
        
        chain = prompt_template | llm | StrOutputParser()
        
        return chain.stream({"history": history, "input": query})
    
    except Exception as e:
        print(f"Erro ao gerar resposta: {str(e)}")
        return "Desculpe, houve um problema ao processar sua solicitação. Por favor, tente novamente mais tarde."
