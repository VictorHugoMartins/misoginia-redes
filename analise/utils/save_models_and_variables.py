import pickle
import plotly.io as pio

def load_variable(param_key):
    """
    Carrega uma variável genérica a partir de um arquivo .pkl.

    Args:
        param_key (str): Nome da variável (chave) a ser carregada.
    
    Returns:
        A variável carregada ou None, caso não seja possível carregar.
    """
    try:
        var_path = f"{param_key}.pkl"
        with open(var_path, "rb") as file:
            variable = pickle.load(file)
        print(f"Loaded variable: {var_path}")
        return variable
    except Exception as e:
        print(f"Failed to load variable from {var_path}: {e}")
        return None

def save_variable(variable, param_key):
    """
    Salva uma variável genérica em um arquivo .pkl.

    Args:
        variable: A variável a ser salva.
        param_key (str): Nome do arquivo (chave) onde será salva.
    """
    try:
        var_path = f"{param_key}.pkl"
        with open(var_path, "wb") as file:
            pickle.dump(variable, file)
        print(f"Saved variable: {var_path}")
    except Exception as e:
        print(f"Failed to save variable to {var_path}: {e}")

def save_fig(fig, name):
    try:
        pio.write_image(fig, name, scale=2)
    except:
        print(f"Não foi possível salvar '{name}'")

def load_model(param_key):
    try:
        model_path = f"{param_key}.pkl"
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        print(f"Loaded model: {model_path}")
        return model
    except:
        return None

def save_model(model, param_key):
    try:
        model_path = f"{param_key}.pkl"
        # Save model
        with open(model_path, "wb") as file:
            pickle.dump(model, file)
            print(f"Saved model: {model_path}")
    except:
        print("Não foi possível salvar o modelo em {model_path}")