import os
from local_variables import ROOT_DIR
import importlib.util


def fetch_prompt(
    sequence,
    version="1",
    root_directory=ROOT_DIR,
    prompt_folder="prompts",
    use_latest_version=False,
):
    """
    Fetches a prompt based on its latest version, identifying sequence and the directory set up

    Args:
        version (str): version identifying which of a given metric's prompts to fetch
        sequence (list): list of ordered keys that identify a specific prompt type and its latest version using the version, should match the prompts folder file structure
        root_directory (str): absolute path of the root directory, assumed to be the local variable specified in the repo
        prompt_folder (str): assumed to be directly inside the root_directory and named 'prompts'
        use_latest_version (bool): use largest (numerically) prompt version found in the prompts dictionary, assumes the versions are either integers or integers of strings otherwise the order is ambiguous
    Returns:
        latest_prompt (str): latest prompt identified by the sequence and version dictionary
    """

    # Create path to prompt using sequencing
    path_to_prompt = os.path.join(root_directory, prompt_folder, sequence[0])

    # Assert that the .py file containing the prompt is named appropriately and in the right directory
    assert f"{sequence[-1]}.py" in os.listdir(
        path_to_prompt
    ), f"{sequence[-1]}.py not found in {os.listdir(path_to_prompt)}"

    # Create path to the file containing prompts
    path_to_file = path_to_prompt + f"/{sequence[-1]}.py"

    # Load the module from the given file path
    spec = importlib.util.spec_from_file_location(sequence[-1], path_to_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Access the metric's prompts
    metric_prompts = module.prompts

    # Fetch latest version for prompt if specified
    if use_latest_version:
        # Identify whether keys are either integers or strings
        all_int = all(isinstance(x, int) for x in metric_prompts.keys())
        all_str = all(isinstance(x, str) for x in metric_prompts.keys())

        # Assert it is either one or the other
        assert (
            all_int or all_str
        ), "Version keys are not integers or string integers, cannot identify latest version. Please correct or specify the version manually using the version kwarg"

        # Convert keys to integers to calculate maximum
        version_int_list = [
            int(key) if key is str else key for key in metric_prompts.keys()
        ]
        latest_version = max(version_int_list)

        if all_str:
            version = f"{latest_version}"
        elif all_int:
            version = latest_version
    else:
        # Assert the latest version has an entry in the metric's prompts
        assert (
            version in metric_prompts.keys()
        ), f"Specified version not found in prompts dictionary at {path_to_file}"

    # Fetch the latest prompt
    latest_prompt = metric_prompts[version]

    return latest_prompt
