from azureml.core.image import ContainerImage, Image
from azureml.core import Model, Workspace

def container_img(ws, model, score_script, env_file):
    image_config = ContainerImage.image_configuration(
            execution_script = score_script,
            runtime = "python",
            conda_file = env_file
            )
    image = Image.create(
            name = "TeamOmega",
            models = [model],
            image_config = image_config,
            workspace = ws
            )
    image.wait_for_creation(show_output = True)
    return image

ws = Workspace.from_config(_file_name = 'config.json')
container_img(ws, Model(ws, "lightGBM"), "score.py", "env.yml")
