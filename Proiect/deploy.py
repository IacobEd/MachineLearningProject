from azureml.core import Model, Workspace, Environment
from azureml.core.model import InferenceConfig
from azureml.core.compute import ComputeTarget, AksCompute
from azureml.core.webservice import AksWebservice

cluster_name = 'aks-cluster'

classifier_deploy_config = AksWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 0.5)
workspace = Workspace.from_config(_file_name= 'config.json')
model = Model(workspace, 'lightGBM')
#cluster AKS
compute_config = AksCompute.provisioning_configuration(location = 'northeurope')
production_cluster = ComputeTarget.create(workspace, cluster_name, compute_config)
production_cluster.wait_for_completion(show_output = True)

env = Environment.from_conda_specification(name = "EnergyPrediction", file_path = "env.yml")
inference_config = InferenceConfig(entry_script = "score.py" , environement = env)


service = Model.deploy(workspace = workspace,
                       name = "energy_prediction",
                       models = [model],
                       inference_config = inference_config,
                       deployment_config = classifier_deploy_config)
