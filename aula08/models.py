from pydantic import BaseModel, Field

class VendaItem(BaseModel):
    Quantidade: int = Field(gt=0)
    Venda: float = Field(gt=0)
    Produto: str