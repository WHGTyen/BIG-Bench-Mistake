"""Prompts for mistake identification for the multistep arithmetic dataset."""

import textwrap


DIRECT_TEMPLATE = (
    '{input} ?\n{steps}\nQ: Is there a mistake in this sequence? Write "No"'
    " if there are no mistakes, or the number N if there is a mistake in"
    " Thought N."
)

DIRECT_MESSAGES = (
    {
        "role": "user",
        "content": (
            "For each sequence of steps, identify the first mistake made, if"
            " any."
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)) = ?
            Thought 1: This equation can be written as "(A + B) * (C * D)", where A = (-4 * -9 + -9 * 5) and B = (4 * 6 - -6 - 4) and C = (9 - 6 + -2 - 2) and D = (-2 * -5 - 6 * 7).
            Thought 2: Let's calculate A = (-4 * -9 + -9 * 5) = ((-4 * -9) + (-9 * 5)) = (36 + (-9 * 5)) = (36 + -45) = -9.
            Thought 3: Let's calculate B = (4 * 6 - -6 - 4) = ((4 * 6) - -6 - 4) = ((24) - -6 - 4) = ((24 - -6) - 4) = ((30) - 4) = 26.
            Thought 4: Let's calculate C = (9 - 6 + -2 - 2) = ((9 - 6) + -2 - 2) = ((3) + -2 - 2) = ((3 + -2) - 2) = ((1) - 2) = -1.
            Thought 5: Let's calculate D = (-2 * -5 - 6 * 7) = ((-2 * -5) - (6 * 7)) = ((10) - (6 * 7)) = (10 - (42)) = -32.
            Thought 6: Then, the final equation is (A + B) * (C * D) = (-9 + 26) * (-1 * -32) = (17) * (-1 * -32) = 17 * (32) = 544. So the answer is 544
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "No"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((((9 * 7 - -5 + 4) * (7 * -1 * -2 + 1)) - ((-4 - 6 + -6 * -8) * (5 + 7 - -6 - -7))) - (((-3 - -4 - -7 - 3) + (-3 * 4 - 3 + -5)) - ((7 - 2 - 2 - -7) + (5 + -1 - -3 * 7)))) = ?
            Thought 1: This equation can be written as "((A * B) - (C * D)) - ((E + F) - (G + H))", where A = (9 * 7 - -5 + 4) and B = (7 * -1 * -2 + 1) and C = (-4 - 6 + -6 * -8) and D = (5 + 7 - -6 - -7) and E = (-3 - -4 - -7 - 3) and F = (-3 * 4 - 3 + -5) and G = (7 - 2 - 2 - -7) and H = (5 + -1 - -3 * 7).
            Thought 2: Let's calculate A = (9 * 7 - -5 + 4) = ((9 * 7) - -5 + 4) = ((63) - -5 + 4) = ((63 - -5) + 4) = ((68) + 4) = 72.
            Thought 3: Let's calculate B = (7 * -1 * -2 + 1) = ((7 * -1 * -2) + 1) = ((-7) * -2 + 1) = ((-7 * -2) + 1) = ((14) + 1) = 15.
            Thought 4: Let's calculate C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
            Thought 5: Let's calculate D = (5 + 7 - -6 - -7) = ((5 + 7) - -6 - -7) = ((12) - -6 - -7) = ((12 - -6) - -7) = ((18) - -7) = 25.
            Thought 6: Let's calculate E = (-3 - -4 - -7 - 3) = ((-3 - -4) - -7 - 3) = ((1) - -7 - 3) = ((1 - -7) - 3) = ((8) - 3) = 5.
            Thought 7: Let's calculate F = (-3 * 4 - 3 + -5) = ((-3 * 4) - 3 + -5) = ((-12) - 3 + -5) = ((-12 - 3) + -5) = ((-15) + -5) = -20.
            Thought 8: Let's calculate G = (7 - 2 - 2 - -7) = ((7 - 2) - 2 - -7) = ((5) - 2 - -7) = ((5 - 2) - -7) = ((3) - -7) = 10.
            Thought 9: Let's calculate H = (5 + -1 - -3 * 7) = (5 + -1 - (-3 * 7)) = (5 + -1 - (-21)) = ((5 + -1) - -21) = ((4) - -21) = 25.
            Thought 10: Then, the final equation is ((A * B) - (C * D)) - ((E + F) - (G + H)) = ((72 * 15) - (128 * 25)) - ((5 + -20) - (10 + 25)) = ((1080) - (3200)) - ((-15) - (35)) = (-2120) - (-50) = -2070. So the answer is -2070
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "4"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((-3 + 5 * 8 * -4) - (9 - 8 * -7 + -9)) = ?
            Thought 1: This equation can be written as "A - B", where A = (-3 + 5 * 8 * -4) and B = (9 - 8 * -7 + -9).
            Thought 2: Let's calculate A = (-3 + 5 * 8 * -4) = (-3 + (5 * 8) * -4) = (-3 + (40) * -4) = (-3 + (40 * -4)) = (-3 + (-160)) = -163.
            Thought 3: Let's calculate B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
            Thought 4: Then, the final equation is A - B = -163 - 49 = -212. So the answer is -212
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "3"},
)


DIRECT_PERSTEP_TEMPLATE = (
    '{input} ?\n{steps}\nQ: Is Thought {current_step} correct? Write "Yes" if'
    ' it is correct, and "No" if it is not.'
)

DIRECT_PERSTEP_MESSAGES = (
    {
        "role": "user",
        "content": (
            "Identify whether a thought is correct and contributes towards"
            ' solving the math question. Write "Yes" if it is correct, and "No"'
            " if it is not."
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)) = ?
            Thought 1: This equation can be written as "(A + B) * (C * D)", where A = (-4 * -9 + -9 * 5) and B = (4 * 6 - -6 - 4) and C = (9 - 6 + -2 - 2) and D = (-2 * -5 - 6 * 7).
            Q: Is Thought 1 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "Yes"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((((9 * 7 - -5 + 4) * (7 * -1 * -2 + 1)) - ((-4 - 6 + -6 * -8) * (5 + 7 - -6 - -7))) - (((-3 - -4 - -7 - 3) + (-3 * 4 - 3 + -5)) - ((7 - 2 - 2 - -7) + (5 + -1 - -3 * 7)))) = ?
            Thought 1: This equation can be written as "((A * B) - (C * D)) - ((E + F) - (G + H))", where A = (9 * 7 - -5 + 4) and B = (7 * -1 * -2 + 1) and C = (-4 - 6 + -6 * -8) and D = (5 + 7 - -6 - -7) and E = (-3 - -4 - -7 - 3) and F = (-3 * 4 - 3 + -5) and G = (7 - 2 - 2 - -7) and H = (5 + -1 - -3 * 7).
            Thought 2: Let's calculate A = (9 * 7 - -5 + 4) = ((9 * 7) - -5 + 4) = ((63) - -5 + 4) = ((63 - -5) + 4) = ((68) + 4) = 72.
            Thought 3: Let's calculate B = (7 * -1 * -2 + 1) = ((7 * -1 * -2) + 1) = ((-7) * -2 + 1) = ((-7 * -2) + 1) = ((14) + 1) = 15.
            Thought 4: Let's calculate C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
            Q: Is Thought 4 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "No"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((-3 + 5 * 8 * -4) - (9 - 8 * -7 + -9)) = ?
            Thought 1: This equation can be written as "A - B", where A = (-3 + 5 * 8 * -4) and B = (9 - 8 * -7 + -9).
            Thought 2: Let's calculate A = (-3 + 5 * 8 * -4) = (-3 + (5 * 8) * -4) = (-3 + (40) * -4) = (-3 + (40 * -4)) = (-3 + (-160)) = -163.
            Thought 3: Let's calculate B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
            Q: Is Thought 3 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "No"},
)


COT_PERSTEP_TEMPLATE = (
    "{input} ?\n{steps}\nQ:"
    " Is Thought {current_step} correct? Check through"
    " each equation and determine whether there are any errors."
)

COT_PERSTEP_MESSAGES = (
    {
        "role": "user",
        "content": (
            "Identify whether a thought is correct and contributes towards"
            " solving the math question. End your response with Yes if the"
            " thought is correct, No if the thought is incorrect."
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)) = ?
            Thought 1: This equation can be written as "(A + B) * (C * D)", where A = (-4 * -9 + -9 * 5) and B = (4 * 6 - -6 - 4) and C = (9 - 6 + -2 - 2) and D = (-2 * -5 - 6 * 7).
            Q: Is Thought 1 correct? Check through each equation and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 1 by checking each equation. Thought 1 rewrites the original equation as (A + B) * (C * D). I can check if this is correct by replacing each letter with the corresponding equation, and checking the final result against the original equation. Current equation: (A + B) * (C * D)
            Comment 2: Replacing A: According to Thought 1, A is (-4 * -9 + -9 * 5). The current equation is (A + B) * (C * D), so after the replacement: ((-4 * -9 + -9 * 5) + B) * (C * D).
            Comment 3: Replacing B: According to Thought 1, B is (4 * 6 - -6 - 4). The current equation is ((-4 * -9 + -9 * 5) + B) * (C * D), so after the replacement: ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * (C * D)
            Comment 4: Replacing C: According to Thought 1, C is (9 - 6 + -2 - 2). The current equation is ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * (C * D), so after the replacement: ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * D)
            Comment 5: Replacing D: According to Thought 1, D is (-2 * -5 - 6 * 7). The currnet equation is ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * D), so after the replacement: ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7))
            Comment 6: The final equation is ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)). The original equation was ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)). So Thought 1 is correct. Yes"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((((9 * 7 - -5 + 4) * (7 * -1 * -2 + 1)) - ((-4 - 6 + -6 * -8) * (5 + 7 - -6 - -7))) - (((-3 - -4 - -7 - 3) + (-3 * 4 - 3 + -5)) - ((7 - 2 - 2 - -7) + (5 + -1 - -3 * 7)))) = ?
            Thought 1: This equation can be written as "((A * B) - (C * D)) - ((E + F) - (G + H))", where A = (9 * 7 - -5 + 4) and B = (7 * -1 * -2 + 1) and C = (-4 - 6 + -6 * -8) and D = (5 + 7 - -6 - -7) and E = (-3 - -4 - -7 - 3) and F = (-3 * 4 - 3 + -5) and G = (7 - 2 - 2 - -7) and H = (5 + -1 - -3 * 7).
            Thought 2: Let's calculate A = (9 * 7 - -5 + 4) = ((9 * 7) - -5 + 4) = ((63) - -5 + 4) = ((63 - -5) + 4) = ((68) + 4) = 72.
            Thought 3: Let's calculate B = (7 * -1 * -2 + 1) = ((7 * -1 * -2) + 1) = ((-7) * -2 + 1) = ((-7 * -2) + 1) = ((14) + 1) = 15.
            Thought 4: Let's calculate C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
            Q: Is Thought 4 correct? Check through each equation and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 4 by checking each equation. The order of operations in mathematics is parentheses, exponents, multiplication and division, addition and subtraction, so I need to ensure that the equations follow this order. Remaining: C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
            Comment 2: Checking: C = (-4 - 6 + -6 * -8). According to Thought 1, C is (9 - 6 + -2 - 2). So C = (-4 - 6 + -6 * -8) is correct. Remaining: (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
            Comment 3: Checking: (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8). So the first operation in (-4 - 6 + -6 * -8) should be the multiplication -6 * -8. The equation (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) places parentheses around the subtraction -4 - 6, which is incorrect.
            Comment 4: (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) is incorrect. So Thought 4 is incorrect. No"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            ((-3 + 5 * 8 * -4) - (9 - 8 * -7 + -9)) = ?
            Thought 1: This equation can be written as "A - B", where A = (-3 + 5 * 8 * -4) and B = (9 - 8 * -7 + -9).
            Thought 2: Let's calculate A = (-3 + 5 * 8 * -4) = (-3 + (5 * 8) * -4) = (-3 + (40) * -4) = (-3 + (40 * -4)) = (-3 + (-160)) = -163.
            Thought 3: Let's calculate B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 56.
            Q: Is Thought 3 correct? Check through each equation and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 7 by checking each equation. The order of operations in mathematics is parentheses, exponents, multiplication and division, addition and subtraction, so I need to ensure that the equations follow this order. Remaining: B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
            Comment 2: Checking: B = (9 - 8 * -7 + -9). According to Thought 1, B is (9 - 8 * -7 + -9). So B = (9 - 8 * -7 + -9) is correct. Remaining: (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
            Comment 3: Checking: (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9). The first operation in (9 - 8 * -7 + -9) should be the multiplication 8 * -7. The equation (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) places parentheses around the multiplication 8 * -7, which is correct. Remaining: (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
            Comment 4: Checking: (9 - (8 * -7) + -9) = (9 - (-49) + -9). The first operation in (9 - (8 * -7) + -9) should be the parentheses (8 * -7), which equals -56. The equation (9 - (8 * -7) + -9) = (9 - (-49) + -9) replaces 8 * -7 with -49, which is incorrect.
            Comment 5: (9 - (8 * -7) + -9) = (9 - (-49) + -9) is incorrect. So Thought 7 is incorrect. No"""
        ),
    },
)
