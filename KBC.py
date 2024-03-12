print("\'Welcome to KBC!!\'")
questions = [
    [
        'Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test '
        'cricket?', 'Virat Kohli', 'Sunil Gavaskar', 'VVS laxman', 'Rahul Dravid', 4
    ],
    [
        'India’s official entry to Oscars 2021, ” Jallikattu” is, a film in which language?', 'Hindi', 'Punjabi',
        'Kannada', 'Malayalam', 3
    ],
    [
        'In 2020, Louise Gluck won the Nobel Prize in which category?', 'Music', 'Sports', 'Literature', 'Dance', 3
    ],
    [
        'Which of the following companies was originally started as a loom manufacturing unit in 1909?', 'Suzuki',
        'CEAT', 'Honda', 'Mercedes', 1
    ],
    [
        'What colour did Lord Shiva’s throat turn into when he drank the deadly poison during Samudra Manthan?', 'Red',
        'Yellow', 'Blue', 'Black', 3
    ],
    [
        'Which of these colors when mixed with red will produce the color orange?', 'Violet', 'Green', 'Orange',
        'Yellow', 4
    ],
    [
        'Which part of the plant absorbs water and nutrients from the soil?', 'Stem', 'Buds', 'Leafs', 'Root', 4
    ],
    [
        'Which process enables earthen pots (matkas) to keep water cool?', 'Absorption', 'Suction', 'Evaporation',
        'Adiabatic Process', 3
    ],
    [
        'Which two countries share the longest international land border?', 'Russia-Kazakhstan', 'Argentina-Chile',
        'USA-Canada', 'Mongolia-China', 3
    ],
    [
        'What is the shape of the cells in a honeycomb made by bees?', 'Octagon', 'Hexagon', 'Square', 'Oval', 2
    ],
    [
        'Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test '
        'cricket?',
        'Virat Kohli', 'Sunil Gavaskar', 'VVS laxman', 'Rahul Dravid', 4
    ],
    [
        'India’s official entry to Oscars 2021, ” Jallikattu” is, a film in which language?', 'Hindi', 'Punjabi',
        'Kannada', 'Malayalam', 3
    ],
    [
        'In 2020, Louise Gluck won the Nobel Prize in which category?', 'Music', 'Sports', 'Literature', 'Dance', 3
    ],
    [
        'Which of the following companies was originally started as a loom manufacturing unit in 1909?', 'Suzuki',
        'CEAT', 'Honda', 'Mercedes', 1
    ],
    [
        'What colour did Lord Shiva’s throat turn into when he drank the deadly poison during Samudra Manthan?', 'Red',
        'Yellow', 'Blue', 'Black', 3
    ],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000,
          10000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"Q: {question[0]}")
    print(f'a. {question[1]}             b. {question[2]}')
    print(f'c. {question[3]}             d. {question[4]}')
    reply = int(input("Enter the correct answer or 0 for quit: "))
    if reply == 0:
        money = levels[i - 1]
        break
    if reply == question[-1]:
        print(f"Correct answer, you have won {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong answer.")
        break
print(f"You take home money is {money}")
print("\'Congratulations!!!\'")
