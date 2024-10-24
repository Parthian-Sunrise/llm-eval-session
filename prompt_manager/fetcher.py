import os
from local_variables import ROOT_DIR
import importlib.util


def fetch_prompt_version(version_dict, sequence):
    """
    Gets the latest prompt version using the specified sequence of identifiers for a given prompt i.e. version_dict = {'task_1' : {'metric_type_1' : {'sub_metric' : 1, 'sub_metric_2' : 11}}} then to get the correct version for sub_metric_2 we pass the sequence ["task_1","metric_type_1","sub_metric_2"]

    Args:
        version_dict (dict): dictionary matching prompts' file structure where the terminal values are the latest version for a given prompt
        sequence (list): list of ordered keys that identify a specific prompt and its latest version using the version_dict dictionary
    Returns:
        version (str): str identifying the latest version of a prompt
    """

    # Loop through identifiers in the sequence
    for index, identifier in enumerate(sequence):

        # Different logic for the first identifier as we have yet to subset the dictionary
        if index == 0:
            subsetted_dict = version_dict
            assert (
                identifier in subsetted_dict.keys()
            ), "1st element in identifying sequence was  not found in the prompt version dictionary"
            subsetted_dict = subsetted_dict[identifier]
        else:
            assert (
                identifier in subsetted_dict.keys()
            ), f"Sequence element with index {index} not found in the prompt version dictionary at the indicated level"
            subsetted_dict = subsetted_dict[identifier]

        # subsetted_dict should be a decreasing tree of dictionaries until the final value at index=len(sequence)
        if index < len(sequence) - 1:
            assert (
                type(subsetted_dict) is dict
            ), "Prompt version dictionary structure does not match the length of the prompt identifying sequence"
        else:
            version = subsetted_dict
            return version


def fetch_prompt(
    version_dict, sequence, root_directory=ROOT_DIR, prompt_folder="prompts"
):
    """
    Fetches a prompt based on its latest version, identifying sequence and the directory set up

    Args:
        version_dict (dict): dictionary matching prompts' file structure where the terminal values are the latest version for a given prompt
        sequence (list): list of ordered keys that identify a specific prompt and its latest version using the version_dict dictionary, should match the prompts folder file structure
        root_directory (str): absolute path of the root directory, assumed to be the local variable specified in the repo
        prompt_folder (str): assumed to be directly inside the root_directory and named 'prompts'
    Returns:
        latest_prompt (str): latest prompt identified by the sequence and version dictionary
    """
    # Fetch version for prompt
    version = fetch_prompt_version(version_dict, sequence)

    # Create path to prompt using sequencing
    path_to_prompt = os.path.join(root_directory, prompt_folder, *sequence)

    # Assert that the .py file containing the prompt is named appropriately and in the right directory
    assert f"{sequence[-1]}.py" in os.listdir(path_to_prompt)

    # Create path to the file containing prompts
    path_to_file = path_to_prompt + f"/{sequence[-1]}.py"

    # Load the module from the given file path
    spec = importlib.util.spec_from_file_location(sequence[-1], path_to_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Access the metric's prompts
    metric_prompts = module.prompts

    # Assert the latest version has an entry in the metric's prompts
    assert version in metric_prompts.keys()

    # Fetch the latest prompt
    latest_prompt = metric_prompts[version]

    return latest_prompt
