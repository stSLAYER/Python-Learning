from Question import Question

print("\nAlright! Let's start naming the OWASP top 10 vulnerabilities in ascending order!\n")
print("To help you out, here are all the vulnerabilities in case you forgot, just put them in ascending order!\n")
print("Sensitive Data Exposure | Injection | Using Components with Known Vulnerabilities | "
      "XML External Entities\nBroken Authentication | Insufficient Logging & Monitoring | "
      "Insufficient Logging & Monitoring | Cross-Site Scripting\nSecurity Misconfiguration | "
      "Broken Access Control | Insecure Deserialization \n")
print("\n")

question_prompt = [
    "What is the first vulnerability?\n",
    "What is the second vulnerability?\n",
    "What is the third vulnerability?\n",
    "What is the fourth vulnerability?\n",
    "What is the fifth vulnerability?\n",
    "What is the sixth vulnerability?\n",
    "What is the seventh vulnerability?\n",
    "What is the eighth vulnerability?\n",
    "What is the ninth vulnerability?\n",
    "What is the tenth vulnerability?\n",
]

questions = [
    Question(question_prompt[0], "Injection"),
    Question(question_prompt[1], "Broken Authentication"),
    Question(question_prompt[2], "Sensitive Data Exposure"),
    Question(question_prompt[3], "XML External Entities"),
    Question(question_prompt[4], "Broken Access Control"),
    Question(question_prompt[5], "Security Misconfiguration"),
    Question(question_prompt[6], "Cross-Site Scripting"),
    Question(question_prompt[7], "Insecure Deserialization"),
    Question(question_prompt[8], "Using Components With Known Vulnerabilities"),
    Question(question_prompt[9], "Insufficient Logging & Monitoring"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)
print("\n")
input('Press ENTER to exit')
