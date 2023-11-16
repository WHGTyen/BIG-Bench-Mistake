"""Prompts for mistake identification for the tracking shuffled objects dataset."""

import textwrap

DIRECT_TEMPLATE = (
    '{input}\n{steps}\nQ: Is there a mistake in this sequence? Write "No"'
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
            Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a blue ball, and Claire has a pink ball.
            As the game progresses, pairs of players trade balls. First, Claire and Alice swap balls. Then, Alice and Bob swap balls. Finally, Claire and Bob swap balls. At the end of the game, Bob has the
            Options:
            (A) yellow ball
            (B) blue ball
            (C) pink ball
            Thought 1: At the start: Alice: yellow, Bob: blue, Claire: pink.
            Thought 2: Claire and Alice swap balls: Alice: pink, Bob: blue, Claire: yellow.
            Thought 3: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
            Thought 4: Claire and Bob swap balls: Alice: yellow, Bob: pink, Claire: blue.
            Thought 5: At the end of the game, Bob has the pink ball. So the answer is (C)
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "3"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a white ball, Bob has a purple ball, and Claire has a pink ball.
            As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Bob and Claire swap balls. Finally, Bob and Alice swap balls. At the end of the game, Alice has the
            Options:
            (A) white ball
            (B) purple ball
            (C) pink ball
            Thought 1: At the start: Alice: white, Bob: purple, Claire: pink.
            Thought 2: Bob and Alice swap balls: Alice: purple, Bob: white, Claire: pink.
            Thought 3: Bob and Claire swap balls: Alice: purple, Bob: pink, Claire: white.
            Thought 4: Bob and Alice swap balls: Alice: pink, Bob: purple, Claire: white.
            Thought 5: At the end of the game, Alice has the pink ball. So the answer is (C)
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "No"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Lola, Bob is dancing with Rodrigo, and Claire is dancing with Patrick.
            Throughout the song, the dancers often trade partners. First, Alice and Bob switch partners. Then, Claire and Bob switch partners. Finally, Bob and Alice switch partners. At the end of the dance, Alice is dancing with
            Options:
            (A) Lola
            (B) Rodrigo
            (C) Patrick
            Thought 1: At the start: Alice: Lola, Bob: Rodrigo, Claire: Patrick.
            Thought 2: Alice and Bob switch partners: Alice: Rodrigo, Bob: Lola, Claire: Patrick.
            Thought 3: Claire and Bob switch partners: Alice: Rodrigo, Bob: Patrick, Claire: Lola.
            Thought 4: Alice and Claire switch partners: Alice: Lola, Bob: Patrick, Claire: Rodrigo.
            Thought 5: At the end of the dance, Alice is dancing with Lola. So the answer is (A)
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "4"},
)


DIRECT_PERSTEP_TEMPLATE = (
    '{input}\n{steps}\nQ: Is Thought {current_step} correct? Write "Yes" if it'
    ' is correct, and "No" if it is not.'
)

DIRECT_PERSTEP_MESSAGES = (
    {
        "role": "user",
        "content": (
            "Identify whether a thought is correct and contributes towards"
            ' solving the question. Write "Yes" if it is correct, and "No" if'
            " it is not."
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a blue ball, and Claire has a pink ball.
            As the game progresses, pairs of players trade balls. First, Claire and Alice swap balls. Then, Alice and Bob swap balls. Finally, Claire and Bob swap balls. At the end of the game, Bob has the
            Options:
            (A) yellow ball
            (B) blue ball
            (C) pink ball
            Thought 1: At the start: Alice: yellow, Bob: blue, Claire: pink.
            Thought 2: Claire and Alice swap balls: Alice: pink, Bob: blue, Claire: yellow.
            Thought 3: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
            Q: Is Thought 3 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "No"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a white ball, Bob has a purple ball, and Claire has a pink ball.
            As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Bob and Claire swap balls. Finally, Bob and Alice swap balls. At the end of the game, Alice has the
            Options:
            (A) white ball
            (B) purple ball
            (C) pink ball
            Thought 1: At the start: Alice: white, Bob: purple, Claire: pink.
            Q: Is Thought 1 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "Yes"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Lola, Bob is dancing with Rodrigo, and Claire is dancing with Patrick.
            Throughout the song, the dancers often trade partners. First, Alice and Bob switch partners. Then, Claire and Bob switch partners. Finally, Bob and Alice switch partners. At the end of the dance, Alice is dancing with
            Options:
            (A) Lola
            (B) Rodrigo
            (C) Patrick
            Thought 1: At the start: Alice: Lola, Bob: Rodrigo, Claire: Patrick.
            Thought 2: Alice and Bob switch partners: Alice: Rodrigo, Bob: Lola, Claire: Patrick.
            Thought 3: Claire and Bob switch partners: Alice: Rodrigo, Bob: Patrick, Claire: Lola.
            Thought 4: Bob and Alice switch partners: Alice: Patrick, Bob: Rodrigo, Claire: Lola.
            Thought 5: At the end of the dance, Alice is dancing with Rodrigo. So the answer is (B)
            Q: Is Thought 5 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "No"},
)


COT_PERSTEP_TEMPLATE = (
    "{input}\n{steps}\n\nIs Thought {current_step} correct? Check through"
    " each part of the text and determine whether there are any errors."
)

COT_PERSTEP_MESSAGES = (
    {
        "role": "user",
        "content": (
            "Identify whether a thought is correct and contributes towards"
            " solving the question. End your response with Yes if the"
            " thought is correct, No if the thought is incorrect."
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a blue ball, and Claire has a pink ball.
            As the game progresses, pairs of players trade balls. First, Claire and Alice swap balls. Then, Alice and Bob swap balls. Finally, Claire and Bob swap balls. At the end of the game, Bob has the
            Options:
            (A) yellow ball
            (B) blue ball
            (C) pink ball
            Thought 1: At the start: Alice: yellow, Bob: blue, Claire: pink.
            Thought 2: Claire and Alice swap balls: Alice: pink, Bob: blue, Claire: yellow.
            Thought 3: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
            
            Is Thought 3 correct? Check through each part of the text and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 3 by checking through each part of the text. Remaining: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
            Comment 2: Checking: Alice and Bob swap balls. This is the second swap in the sequence, after the swap between Claire and Alice. This matches the description in the original question. So Alice and Bob swap balls is correct. Remaining: Alice: yellow, Bob: blue, Claire: pink.
            Comment 3: Checking: Alice: yellow. In Thought 2, Alice had a pink ball and Bob had a blue ball. If Alice and Bob swapped balls, Alice should have a blue ball and Bob should have a pink ball. So Alice: yellow is incorrect.
            Comment 4: Alice: yellow is incorrect. So Thought 3 is incorrect. No"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a white ball, Bob has a purple ball, and Claire has a pink ball.
            As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Bob and Claire swap balls. Finally, Bob and Alice swap balls. At the end of the game, Alice has the
            Options:
            (A) white ball
            (B) purple ball
            (C) pink ball
            Thought 1: At the start: Alice: white, Bob: purple, Claire: pink.
            
            Is Thought 1 correct? Check through each part of the text and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 1 by checking through each part of the text. Remaining: At the start: Alice: white, Bob: purple, Claire: pink.
            Comment 2: Checking: At the start. This is the first thought in the sequence, so this is correct. Remaining: Alice: white, Bob: purple, Claire: pink.
            Comment 3: Checking: Alice: white. In the description of the original question, at the start of the game, Alice has a white ball. So Alice: white is correct. Remaining: Bob: purple, Claire: pink.
            Comment 4: Checking: Bob: purple. In the description of the original question, at the start of the game, Bob has a purple ball. So Bob: purple is correct. Remaining: Claire: pink.
            Comment 5: Checking: Claire: pink. In the description of the original question, at the start of the game, Claire has a pink ball. So Clare: pink is correct. Remaining:
            Comment 6: I have checked through all parts of the text and found no errors. So Thought 1 is correct. Yes"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Lola, Bob is dancing with Rodrigo, and Claire is dancing with Patrick.
            Throughout the song, the dancers often trade partners. First, Alice and Bob switch partners. Then, Claire and Bob switch partners. Finally, Bob and Alice switch partners. At the end of the dance, Alice is dancing with
            Options:
            (A) Lola
            (B) Rodrigo
            (C) Patrick
            Thought 1: At the start: Alice: Lola, Bob: Rodrigo, Claire: Patrick.
            Thought 2: Alice and Bob switch partners: Alice: Rodrigo, Bob: Lola, Claire: Patrick.
            Thought 3: Claire and Bob switch partners: Alice: Rodrigo, Bob: Patrick, Claire: Lola.
            Thought 4: Bob and Alice switch partners: Alice: Patrick, Bob: Rodrigo, Claire: Lola.
            Thought 5: At the end of the dance, Alice is dancing with Rodrigo. So the answer is (B)
            
            Is Thought 5 correct? Check through each part of the text and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 5 by checking through each part of the text. Remaining: At the end of the dance, Alice is dancing with Patrick. So the answer is (A)
            Comment 2: Checking: At the end of the dance. In Thought 4, Bob and Alice switch partners. According to the description in the original question, this is the final swap. Thought 5 is at the end of the dance, so At the end of the dance is correct. Remaining: Alice is dancing with Patrick. So the answer is (A)
            Comment 3: Checking: Alice is dancing with Rodrigo. In Thought 4, after the final swap, Alice's partner is Patrick. So Alice is dancing with Rodrigo is incorrect.
            Comment 4: Alice is dancing with Rodrigo is incorrect. So Thought 5 is incorrect. No"""
        ),
    },
)
