
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Dict[str, str]]] = [] # List of {"role": "user"|"model", "content": "..."}

class PhoneSpec(BaseModel):
    processor: str
    ram: str
    storage: str
    display: str
    camera: str
    battery: str
    os: str

class Phone(BaseModel):
    id: str
    name: str
    brand: str
    price: int
    specs: PhoneSpec
    features: List[str]
    description: str

class ChatResponse(BaseModel):
    type: str # 'text', 'product_list', 'comparison', 'product_detail'
    content: str
    data: Optional[List[Phone]] = None
