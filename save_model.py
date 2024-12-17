from pathlib import Path
import torch

# Creating model path directory..
MODEL_PATH = Path("models")
MODEL_PATH.mkdir(parents=True , exist_ok=True)

def save_state(state_dict:dict , model_name : str):

    try:
        torch.save(obj=state_dict, f=MODEL_PATH/model_name)
    except Exception as e:
        print(f"{e.message()}")
    print(f"File {model_name} saved...")

def save_model(model , model_name:str):
    try:
        torch.save(obj=model, f=MODEL_PATH/model_name)
    except Exception as e:
        print(f"{e.message()}")
    print(f"Model {model_name} saved...")
    
