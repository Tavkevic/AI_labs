def is_butterfly():
    print("Ответьте на вопросы (Да/Нет):")

    questions = [
        "У объекта есть крылья?",
        "Крылья покрыты чешуйками?",
        "Питается нектаром?",
        "Проходит стадию гусеницы?",
        "Активен днем?"
    ]

    answers = []
    for q in questions:
        ans = input(q + " ").strip().lower()
        answers.append(ans == 'да')

    true_count = sum(answers)

    if true_count == 5:
        print("Да, это бабочка!")
    elif true_count >= 3:
        print("Возможно, это бабочка.")
    else:
        print("Скорее всего, это не бабочка.")


is_butterfly()