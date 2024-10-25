class PromptManager:
    def __init__(self, template, inputs={}):
        self.template = template
        self.inputs = inputs
        self.formatted = False

    def validate_inputs(self):
        """
        Validates that all placeholders in the inputs are present in the template

        Args:
            self (attributes: [template,inputs,formatted])

        Returns:
            self.validated: bool
        """
        if self.formatted:
            print("Already formatted, cannot validate")
        else:
            assertion_list = [
                True if key in self.template else False for key in self.inputs.keys()
            ]

            if sum(assertion_list) == len(assertion_list):
                print("Inputs validated successfully!")
                self.validated = True
            else:
                print(
                    "Inputs validation unsucessful! Check that all inputs are present in the prompt template"
                )
                self.validated = False
            return self.validated

    def format_inputs(self):
        """
        Replaces placeholders with desired input after validation of the inputs with respect to the template

        Args:
            self (attributes: [validated,formatted,template,inputs])

        Returns:
            self.prompt: str with placeholders replaced
        """
        if self.validated:
            print("Previous validation successful, proceeding with formatting")
        else:
            print("Validating inputs")
            self.validate_inputs()
            if self.validated:
                print("Proceeding with formatting")
            else:
                print("Validation failed, cannot format")
        if self.formatted:
            print("Already formatted")
        else:
            self.formatted = True
            self.prompt = self.template
            for key in self.inputs:
                self.prompt = self.prompt.replace(key, self.inputs[key])
            return self.prompt
