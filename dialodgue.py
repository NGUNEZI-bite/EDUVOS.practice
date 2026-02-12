class South_african_pandemic:
    def __init__(self):
        self,outcome = None

    def interpret_answer(self, question, answer):
        if question.startswith ("C-"):
            if answer.lower() == "yes":
        return true
        else:
        return false
    def ask_question(self, question, rule_based=False):
        answer = input(f"{question} (yes/no: ").strip()
        return self.interpret_answer(question, answer)
    def run_dialogue(self):
        region_answer = self.ask_question("C-Is your green?", rule_base=True)
        if region_answer:
            self.outcome = "Positive"
            print("Outcome: Positive! (region is green.)"
            return

        vaccine_answer = self.ask_question("have you recieved the vaccine?")
        if vaccine_answer:
            self.outcome = "positive"
            print("outcome: positive! (vaccinated)")

        covid_answer = self.ask_question("Have you had COVID ealier")
        if covid_answer:
                  self.outcome = "Positive"
                  print("Outcome: Nrgative! (No positive responses.)")
dialogue = PandemicDialogue()
dialogue.run_dialogue()
