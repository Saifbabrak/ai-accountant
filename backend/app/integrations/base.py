# integrations/base.py
from abc import ABC, abstractmethod

class AccountingIntegration(ABC):
    @abstractmethod
    async def authenticate(self) -> bool: 
        ...