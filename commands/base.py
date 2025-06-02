class Command:
    def match(self, test: str) -> bool:
        raise NotImplementedError
    
    def execute(self) -> str:
        raise NotImplementedError