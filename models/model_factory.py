def create_model(model_type="linear"):
    if model_type == "linear":
        print("Creating linear model")
    elif model_type == "cnn":
        print("Creating CNN model")
    else:
        print("Creating custom model")