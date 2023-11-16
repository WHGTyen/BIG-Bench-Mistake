"""Prompts for mistake identification for the word sorting dataset."""

import textwrap

DIRECT_TEMPLATE = (
    "Q: Sort the following words alphabetically: List: {input}\n{steps}\nIs"
    ' there a mistake in this sequence? Write "No" if there are no mistakes, or'
    " the number N if there is a mistake in Thought N."
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
            Q: Sort the following words alphabetically: List: oven costume counterpart
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
            Thought 2: We now have: (3) ["costume" ? "counterpart"] < (15) "oven".
            Thought 3: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their second letters. The second letter: "costume": "o" (15). "counterpart": "o" (15).
            Thought 4: We now have: (15) ["costume" ? "counterpart"] for the subpart. Hence, we have ["costume" ? "counterpart"] < "oven".
            Thought 5: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their third letters. The third letter: "costume": "s" (19). "counterpart": "n" (14).
            Thought 6: We now have: (14) "counterpart" < (19) "costume" for the subpart. Hence, we have "counterpart" < "costume" < "oven".
            Thought 7: I have now sorted all the words. The answer is counterpart costume oven
            Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "5"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Q: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
            Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "mugho" < (14) "newt" < (16) "parthia" < (19) "seismography".
            Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
            Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "mugho" < "newt" < "parthia" < "seismography".
            Thought 5: I have now sorted all the words. The answer is arson aspect census mugho newt parthia seismography
            Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "No"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Q: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
            Thought 2: We now have: (3) "credulity" < (8) "hypochlorite" < (16) ["ponderosa" ? "phone"].
            Thought 3: Now let's sort this subpart ["ponderosa" ? "phone"] by looking at their second letters. The second letter: "ponderosa": "o" (15). "phone": "h" (8).
            Thought 4: We now have: (8) "phone" < (15) "ponderosa" for the subpart. Hence, we have "credulity" < "phone" < "ponderosa".
            Thought 5: I have now sorted all the words. The answer is credulity phone ponderosa
            Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "4"},
)

DIRECT_PERSTEP_TEMPLATE = (
    "Task: Sort the following words alphabetically: List: {input}\n{steps}\nQ:"
    ' Is Thought {current_step} correct? Write "Yes" if it is correct, and "No"'
    " if it is not."
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
            Task: Sort the following words alphabetically: List: oven costume counterpart
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
            Q: Is Thought 1 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "Yes"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
            Thought 2: We now have: (8) "hypochlorite" < (16) ["ponderosa" ? "phone"] < (3) "credulity".
            Q: Is Thought 2 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "No"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
            Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "mugho" < (14) "newt" < (16) "parthia" < (19) "seismography".
            Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
            Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography".
            Q: Is Thought 4 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {"role": "assistant", "content": "No"},
)

COT_TEMPLATE = (
    "Task: Sort the following words alphabetically: List: {input}\n{steps}\nQ:"
    " Is there a mistake in this sequence? If so, where is the first mistake?"
    " Break down your thought process and show your reasoning step-by-step."
    ' Your answer should be "No" if there are no mistakes, or the number N if'
    " there is a mistake in Thought N."
)
COT_MESSAGES = (
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
            Task: Sort the following words alphabetically: List: oven costume counterpart
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
            Thought 2: We now have: (3) ["costume" ? "counterpart"] < (15) "oven".
            Thought 3: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their second letters. The second letter: "costume": "o" (15). "counterpart": "o" (15).
            Thought 4: We now have: (15) ["costume" ? "counterpart"] for the subpart. Hence, we have ["costume" ? "counterpart"] < "oven".
            Thought 5: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their third letters. The third letter: "costume": "s" (19). "counterpart": "n" (14).
            Thought 6: We now have: (14) "counterpart" < (19) "costume" for the subpart. Hence, we have "counterpart" < "costume" < "oven".
            Thought 7: I have now sorted all the words. The answer is counterpart costume oven
            Q: Is there a mistake in this sequence? If so, where is the first mistake? Break down your thought process and show your reasoning step-by-step. Your answer should be "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: This sequence of thoughts sorts words alphabetically by rearranging them by the first letter, then the second letter, etc. and keeping track of the sorted order. To find the first mistake, I need to check the correctness of each Thought one by one, starting with Thought 1.
            Comment 2: Thought 1 lists the first letter of "oven" ('o'), the first letter of "costume" ('c'), and the first letter of "counterpart" ('c'). It identifies their positions in the alphabet: 'o' is the 15th letter; 'c' is the 3rd letter. So Thought 1 is correct.
            Comment 3: Thought 2 rearranges the words according to the alphabet position of the first letter. There are two words starting with 'c', so we don't know which one comes first. The words from the original question, "oven", "costume", and "counterpart", are all included and sorted correctly. So Thought 2 is correct.
            Comment 4: The question asks to sort the words "oven", "costume", and "counterpart", but "costume" and "counterpart" both start with 'c'. Thought 3 lists the second letter of "costume" ('o') and the second letter of "counterpart" ('o'). It identifies their positions in the alphabet: 'o' is the 15th letter. So Thought 3 is correct.Comment 5: Thought 4 rearranges the words according to the alphabet position of the second letter. There are two words starting with 'co', so we don't know which one comes first. "oven" is included once and sorted correctly; "costume" is included once and sorted correctly; "counterpart" is included once and sorted correctly. So Thought 4 is correct.
            Comment 6: The question asks to sort the words "oven", "costume", and "counterpart", but "costume" and "counterpart" both start with 'co'. Thought 5 lists at the third letter of "costume" ('s'), and the fourth letter of "counterpart" ('u'). Thought 5 should look at the third letter of counterpart ('u'). So Thought 5 is incorrect.
            Comment 7: Thoughts 1 to 4 are correct, but Thought 5 is incorrect. So the answer is 5"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
            Thought 2: We now have: (3) "credulity" < (8) "hypochlorite" < (16) ["ponderosa" ? "phone"].
            Thought 3: Now let's sort this subpart ["ponderosa" ? "phone"] by looking at their second letters. The second letter: "ponderosa": "o" (15). "phone": "h" (8).
            Thought 4: We now have: (8) "phone" < (15) "ponderosa" for the subpart. Hence, we have "credulity" < "hypochlorite" < "phone" < "ponderosa".
            Thought 5: I have now sorted all the words. The answer is credulity hypochlorite phone ponderosa
            Q: Is there a mistake in this sequence? If so, where is the first mistake? Break down your thought process and show your reasoning step-by-step. Your answer should be "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: This sequence of thoughts sorts words alphabetically by rearranging them by the first letter, then the second letter, etc. and keeping track of the sorted order. To find the first mistake, I need to check the correctness of each Thought one by one, starting with Thought 1.
            Comment 2: Thought 1 lists the first letter of "hypochlorite" ('h'), the first letter of "ponderosa" ('p'), the first letter of "phone" ('p'), and the first letter of "credulity" ('c'). So Thought 1 is correct. It identifies their positions int he alphabet: 'h' is the 8th letter, 'c' is the 3rd letter, and 'p' is the 16th letter. So Thought 1 is correct.
            Comment 3: Thought 2 rearranges the words according to the alphabet position of the first letter. There are two words starting with 'p' so we don't know which one comes first. 'hypochlorite' is included once and sorted correctly; 'ponderosa' is included once and sorted correctly; 'phone' is included once and sorteed correctly; and 'credulity' is included once and sorted correctly. So Thought 2 is correct.
            Comment 4: The question asks to sort the words "hypochlorite", "ponderosa", "phone", and "credulity", but "ponderosa" and "phone" both start with 'p'. Thought 3 lists the second letter of "ponderosa" ('o') and the second letter of "phone" ('h'). It identifies their positions in the alphabet: 'o' is the 15th letter, and 'h' is the 8th letter. So Thought 3 is correct.
            Comment 5: Thought 4 rearranges the words ponderosa and phone according to the alphabet position of the second letter. "hypochlorite" is included once and sorted correctly; "ponderosa" is included once and sorted correctly; "phone" is included once and sorted correctly; and "credulity" is included once and sorted correctly. So Thought 4 is correct.
            Comment 6: Thought 5 is the final thought and provides the answer. According to Thought 4, the correct order is "credulity" < "hypochlorite" < "phone" < "ponderosa", so Thought 5 is correct. So the answer is No"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
            Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "newt" < (14) "newt" < (16) "parthia" < (19) "seismography".
            Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
            Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "newt" < "newt" < "parthia" < "seismography".
            Thought 5: I have now sorted all the words. The answer is arson aspect census newt newt parthia seismography.
            Thought 6: Answer: arson aspect census newt parthia seismography
            Q: Is there a mistake in this sequence? If so, where is the first mistake? Break down your thought process and show your reasoning step-by-step. Your answer should be "No" if there are no mistakes, or the number N if the first mistake in Thought N."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: This sequence of thoughts sorts words alphabetically by rearranging them by the first letter, then the second letter, etc. and keeping track of the sorted order. To find the first mistake, I need to check the correctness of each Thought one by one, starting with Thought 1.
            Comment 2: Thought 1 lists the first letter of "newt" ('n'), the first letter of "arson" ('a'), the first letter of "parthia" ('p'), the first letter of "seismography" ('s'), the first letter of "mugho" ('m'), the first letter of "aspect" ('a'), and the first letter of "census" ('c'). It identifies their positions in the alphabet: 'n' is the 14th letter, 'a' is the 1st letter, 'p' is the 16th letter, 's' is the 19th letter, 'm' is the 13th letter, and 'c' is the 3rd letter. So Thought 1 is correct.
            Comment 3: Thought 2 rearranges the words according to the alphabet position of the first letter. There are two words starting with 'a', so we don't know which one comes first. "mugho" is not included; "newt" is included twice. So Thought 2 is incorrect.
            Comment 4: Thought 1 is correct, but Thought 2 is incorrect. So the answer is 2"""
        ),
    },
)

COT_PERSTEP_TEMPLATE = (
    "Task: Sort the following words alphabetically: List: {input}\n{steps}\nQ:"
    " Is Thought {current_step} correct? Check through each word in the"
    " original list and determine whether they are correctly described."
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
            Task: Sort the following words alphabetically: List: oven costume counterpart
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
            Q: Is Thought 1 correct? Check through each word in the original list and determine whether they are correctly described."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 1 by checking each word in the list: oven costume counterpart. Remaining: oven costume counterpart
            Comment 2: Checking: oven. The first letter of "oven" is "o", which is the 15th letter of the alphabet. So "oven": "o" (15) is correct. Remaining: costume counterpart
            Comment 3: Checking: costume. The first letter of "costume" is "c", which is the 3rd letter of the alphabet. So "costume": "c" (3) is correct. Remaining: counterpart
            Comment 4: Checking: counterpart. The first letter of "counterpart" is "c", which is the 3rd letter of the alphabet. So "counterpart": "c" (3) is correct. Remaining:
            Comment 5: Thought 1 does not include any other words, and all words from the original list are included. So Thought 1 is correct. Yes"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
            Thought 2: We now have: (8) "hypochlorite" < (16) ["ponderosa" ? "phone"] < (3) "credulity".
            Q: Is Thought 2 correct? Check through each word in the original list and determine whether they are correctly described."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 2 by checking each word in the list: hypochlorite ponderosa phone credulity. Remaining: hypochlorite ponderosa phone credulity
            Comment 2: Checking: hypochlorite. hypochlorite is placed before ponderosa and phone because the first letter "h" (8) is before the first letter "p" (16). So (8) "hypochlorite" < (16) ["ponderosa" ? "phone"] is correct. Remaining: ponderosa phone credulity
            Comment 3: Checking: ponderosa. ponderosa is placed after hypochlorite because the first letter "p" (16) is after the first letter "h" (8) in the alphabet. ponderosa is placed in the same position as phone because the first letter "p" (16) is the same. ponderosa is placed before credulity, but the first letter "c" (3) is before the first letter "p" (16) in the alphabet. So (16) ["ponderosa" ? "phone"] < (3) "credulity" is incorrect.
            Comment 4: (16) ["ponderosa" ? "phone"] < (3) "credulity" is incorrect, so Thought 2 is incorrect. No"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
            Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
            Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "mugho" < (14) "newt" < (16) "parthia" < (19) "seismography".
            Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
            Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography".
            Q: Is Thought 4 correct? Check through each word in the original list and determine whether they are correctly described."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 4 by checking each word in the list: newt arson parthia seismography mugho aspect census. Remaining: newt arson parthia seismography mugho aspect census
            Comment 2: Checking: newt. newt is placed after census because the first letter "n" (14) is after the first letter "c" (3). newt is placed before parthia because the first letter "n" (14) is before the first letter "p" (16). So "census" < "newt" < "parthia" is correct. Remaining: arson parthia seismography mugho aspect census
            Comment 3: Checking: arson. arson is placed before aspect because the first letter "a" (1) is the same and the second letter "r" (18) is before the second letter "s" (19). So "arson" < "aspect" is correct. Remaining: parthia seismography mugho aspect census
            Comment 4: Checking: parthia. parthia is placed after newt because the first letter "p" (16) is after the first letter "n" (14). parthia is placed before seismography because the first letter "p" (16) is before the first letter "s" (19). So "newt" < "parthia" < "seismography" is correct. Remaining: seismography mugho aspect census
            Comment 5: Checking: seismography. seismography is placed after parthia because the first letter "s" (19) is after the first letter "p" (16). So "parthia" < "seismography" is correct. Remaining: mugho aspect census
            Comment 6: Checking: mugho. mugho is missing from the list. So "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography" is incorrect.
            Comment 7: "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography" is incorrect, so Thought 4 is incorrect. No"""
        ),
    },
)
