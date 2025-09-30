import inspect
import time
import logging
import functools
from typing import Type
from pydantic import BaseModel, ValidationError
import pandas as pd

# Decorator de Log
def log_execution(func):
    """Decorator para registrar o inicio e fim da execução de uma função."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__)
        logger.info(f"Starting execution of {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished execution of {func.__name__}")
        return result
    return wrapper

# Decorator de Tempo de Execução
def time_execution(func):
    """Decorator para medir o tempo de execução de uma função."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

# Decorator de Validação de Dados
def validate_dataframe(model: Type[BaseModel]):
    """Decorator Factory para validar as linhas de um DataFrame usando um modelo Pydantic."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs): # <--- 1. Usar a assinatura genérica
            # 2. Deixar o inspect analisar TODOS os argumentos recebidos
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs).arguments
            
            # 3. Pegar o nome do primeiro parâmetro da função original
            param_name = list(sig.parameters.keys())[0]
            df = bound_args.get(param_name) # Usar .get() para mais segurança
            
            if not isinstance(df, pd.DataFrame):
                raise TypeError(f"O argumento '{param_name}' deve ser um DataFrame do Pandas.")
            
            try:
                records = df.to_dict(orient='records')
                validated_records = [model.model_validate(record) for record in records]
                print(f"-> Qualidade de dados: {len(validated_records)} linhas validadas com sucesso.")
            
            except ValidationError as e:
                print(f"!!! Erro de qualidade de dados na função '{func.__name__}' !!!")
                raise e

            # 4. Chamar a função original com os argumentos originais
            return func(*args, **kwargs)
        return wrapper
    return decorator