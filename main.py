def is_butterfly():
    print("Ответьте на вопросы (Да/Нет):")

    questions = [
        ["У объекта есть крылья?", 1],
        ["Крылья покрыты чешуйками?", 0.8],
        ["Питается нектаром?", 0.8],
        ["Проходит стадию гусеницы?", 1],
        ["Активен днем?", 0.4]
    ]

    answers = []
    for q in questions:
        ans = input(q[0] + " ").strip().lower()
        if ans == 'да':
            answers.append(1 * q[1])

    true_count = sum(answers)
    if true_count == 4:
        print("Да, это бабочка!")
    elif true_count >= 2.8:
        print("Возможно, это бабочка.")
    else:
        print("Скорее всего, это не бабочка.")


is_butterfly()