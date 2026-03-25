import random

def read_and_shuffle_questions(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    # Split questions by empty lines
    questions = [q.strip() for q in content.split('\n\n') if q.strip()]
    
    # Shuffle the list of questions
    random.shuffle(questions)
    
    return questions

def print_questions(questions):
    for question in questions:
        input("\n\n" + question + "\n(Press Enter for the next question)\n\n")
        print()

if __name__ == "__main__":
    filename = "qns.txt"
    questions = read_and_shuffle_questions(filename)
    print_questions(questions)