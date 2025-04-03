import torch
from .model import RouteOptimizer

def load_model(model_path: str) -> RouteOptimizer:
    model = RouteOptimizer()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def get_optimal_route(input_data, model: RouteOptimizer):
    # input_data should be a torch.Tensor
    with torch.no_grad():
        output = model(input_data)
    # For illustration, just return the raw output
    return output
