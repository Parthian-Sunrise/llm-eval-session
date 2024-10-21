class PromptManager:
    def __init__(self, template, inputs={}):
        self.template = template
        self.inputs = inputs
        self.formatted = False

    def validate_inputs(self):
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
                return None

    def format_inputs(self):
        if self.validated:
            print("Previous validation successful")
        else:
            print("Validating inputs")
            self.validate_inputs()
        if self.formatted:
            print("Already formatted")
        else:
            self.formatted = True
            self.prompt = self.template
            for key in self.inputs:
                self.prompt = self.prompt.replace(key, self.inputs[key])
            return self.prompt
