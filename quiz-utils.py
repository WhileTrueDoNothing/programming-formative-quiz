"""Tools for creating questions and quizzes."""

from random import shuffle
from string import ascii_lowercase


class Question:
    """A question that can be answered by a free text input."""

    question: str
    answers: list[str]

    def __init__(self, question, answers):
        """
        Create a new Question.

        Args:
            question (str): The text for the question to be asked.
            answers (list[str]): The correct answer(s) for the question.
        """
        self.question = question
        self.answers = answers

    def ask(self):
        """
        Asks the user the question. Returns 1 if the user inputs the correct answer, or 0 otherwise.
        """
        print(self.question)
        user_answer = input("Your answer: ")
        if user_answer.lower() in [answer.lower() for answer in self.answers]:
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0


class MultiChoiceQuestion(Question):
    """A multiple choice question. Supports up to 26 options."""

    wrong_answers: list[str]

    def __init__(self, question, answers, wrong_answers):
        """
        Create a new MultiChoiceQuestion.

        Args:
            question (str): The text for the question to be asked.
            answers (list[str]): The correct answer(s) for the question.
            wrong_answers (list[str]): Other options for the question.

        Raises:
            ValueError: If the combined length of correct and incorrect answer lists is higher than 26.
        """
        if len(answers) + len(wrong_answers) > 26:
            raise ValueError(
                "Combined length of correct and incorrect answer lists must be 26 or less. Total options received: {total}".format(
                    total=len(answers) + len(wrong_answers)
                )
            )
        self.wrong_answers = wrong_answers
        super().__init__(question, answers)

    def ask(self):
        """
        Asks the user the question. Returns 1 if the user inputs the correct answer, or 0 otherwise.
        """
        all_options = self.answers + self.wrong_answers
        shuffle(all_options)

        option_list = {}

        for letter, option in zip(list(ascii_lowercase), all_options):
            option_list[letter] = option

        full_question_text = self.question + "\n" + "\n".join(
            "{index}) {option}".format(index=key, option=value)
            for key, value in option_list.items()
        )

        print(full_question_text)

        user_answer = input("Your answer: ")
        if (
            user_answer in option_list.keys()
            and option_list[user_answer] in self.answers
        ) or user_answer.lower() in [answer.lower() for answer in self.answers]:
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0

score = 0

TestQuestions = [
    Question("What is the capital of the UK?", ["London"]),
    Question("Name a special type of movement speed in Pathfinder.", ["Climb","Fly","Swim"]),
    MultiChoiceQuestion("Which of these is a vegetable?", ["Potato"], ["Tomato","Cucumber"])
]

for q in TestQuestions:
    score += q.ask()

print(f"Your score: {score}")