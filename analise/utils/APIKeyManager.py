class APIKeyManager:
    def __init__(self, api_keys):
        self.api_keys = [key for key in api_keys if key]  # Remove chaves nulas ou inválidas
        self.current_index = 0

    def get_key(self):
        """Retorna a chave atual."""
        if not self.api_keys:
            raise Exception("Nenhuma chave de API válida foi fornecida.")
        return self.api_keys[self.current_index]

    def rotate_key(self):
        """Avança para a próxima chave."""
        self.current_index = (self.current_index + 1) % len(self.api_keys)

    def use_key(self):
        """Retorna a chave atual e avança para a próxima chave."""
        key = self.get_key()
        self.rotate_key()
        return key