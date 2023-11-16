"""Prompts for mistake identification for the Dyck languages dataset."""

import textwrap

DIRECT_TEMPLATE = (
    "Task: Complete the rest of the sequence, making sure that the parentheses"
    " are closed properly. Input: {input}\n{steps}\nQ: Is there a mistake in"
    ' this sequence? Write "No" if there are no mistakes, or the number N if'
    " there is a mistake in Thought N."
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
            Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: [ { [
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: [ ; stack: [
            Thought 4: { ; stack: [ {
            Thought 5: [ ; stack: [ { [
            Thought 6: Now, we have reached the end. The final stack is "[ { [".
            Thought 7: We will need to pop out "[", "{", one by one in that order.
            Thought 8: So, we need "]", "}". So the answer is ] }
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "7"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < > ( ( [ [ ( { } ) [ < > ] ]
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: < ; stack: <
            Thought 4: > ; stack: empty
            Thought 5: ( ; stack: (
            Thought 6: ( ; stack: ( (
            Thought 7: [ ; stack: ( ( [
            Thought 8: [ ; stack: ( ( [ [
            Thought 9: ( ; stack: ( ( [ [ (
            Thought 10: { ; stack: ( ( [ [ ( {
            Thought 11: } ; stack: ( ( [ [ (
            Thought 12: ) ; stack: ( ( [ [
            Thought 13: [ ; stack: ( ( [ [ [
            Thought 14: < ; stack: ( ( [ [ [ <
            Thought 15: > ; stack: ( ( [ [ [
            Thought 16: ] ; stack: ( ( [ [
            Thought 17: ] ; stack: ( ( [
            Thought 18: Now, we have reached the end. The final stack is "( ( [".
            Thought 19: We will need to pop out "[", "(", "(" one by one in that order.
            Thought 20: So, we need "]", ")", ")". So the answer is ] ) )
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "No"},
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < [ < [ { < [ ] < { } > > } ] > { { ( ) } { < [ < > ] > }
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: < ; stack: <
            Thought 4: [ ; stack: < [
            Thought 5: < ; stack: < [ <
            Thought 6: [ ; stack: < [ < [
            Thought 7: { ; stack: < [ < [ {
            Thought 8: < ; stack: < [ < [ { <
            Thought 9: [ ; stack: < [ < [ { < [
            Thought 10: ] ; stack: < [ < [ { <
            Thought 11: < ; stack: < [ < [ { < <
            Thought 12: { ; stack: < [ < [ { < < {
            Thought 13: } ; stack: < [ < [ { < <
            Thought 14: > ; stack: < [ < [ { <
            Thought 15: > ; stack: < [ < [ {
            Thought 16: } ; stack: < [ < [
            Thought 17: ] ; stack: < [ <
            Thought 18: > ; stack: < [
            Thought 19: Now, we have reached the end. The final stack is "< [".
            Thought 20: We will need to pop out "[", "<" one by one in that order.
            Thought 21: So, we need "]", ">". So the answer is } >
            Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
        ),
    },
    {"role": "assistant", "content": "19"},
)


DIRECT_PERSTEP_TEMPLATE = (
    "Task: Complete the rest of the sequence, making sure that the brackets"
    " are closed properly. Input: {input}\n{steps}\nQ: Is Thought"
    ' {current_step} correct? Write "Yes" if it is correct, and "No" if it is'
    " not."
)


DIRECT_PERSTEP_MESSAGES = (
    {
        "role": "user",
        "content": (
            "Identify whether a thought is correct and contributes towards"
            " solving the question. Write \"Yes\" if the"
            " thought is correct, \"No\" if the thought is incorrect."
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: [ {
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: [ ; stack: [
            Thought 4: { ; stack: [ {
            Thought 5: Now, we have reached the end. The final stack is "[ {".
            Thought 6: We will need to pop out "{", "[" one by one in that order.
            Thought 7: So, we need "{", "[". So the answer is { [
            Q: Is Thought 7 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {
        "role": "assistant",
        "content": "No",
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Complete the rest of the sequence, making sure that the brackets are closed properly. Input: < > ( ( [ [ ( { } ) [ < > ] ]
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: < ; stack: <
            Thought 4: > ; stack: empty
            Q: Is Thought 4 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {
        "role": "assistant",
        "content": "Yes"
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < [ < [ { < [ ] < { } > > } ] > { { ( ) } { < [ < > ] > }
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: < ; stack: <
            Thought 4: [ ; stack: < [
            Thought 5: < ; stack: < [ <
            Thought 6: [ ; stack: < [ < [
            Thought 7: { ; stack: < [ <
            Q: Is Thought 7 correct? Write "Yes" if it is correct, and "No" if it is not."""
        ),
    },
    {
        "role": "assistant",
        "content": "No"
    },
)

COT_PERSTEP_TEMPLATE = (
    "Task: Complete the rest of the sequence, making sure that the brackets"
    " are closed properly. Input: {input}\n{steps}\nQ:"
    " Is Thought {current_step} correct? Check through"
    " each sentence and determine whether there are any errors."
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
            Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: [ {
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: [ ; stack: [
            Thought 4: { ; stack: [ {
            Thought 5: Now, we have reached the end. The final stack is "[ {".
            Thought 6: We will need to pop out "{", "[" one by one in that order.
            Thought 7: So, we need "{", "[". So the answer is { [
            Q: Is Thought 7 correct? Check through each sentence and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 7 by checking each sentence. Remaining: So, we need "{", "[". So the answer is { [
            Comment 2: Checking: So, we need "[", "{", "[". Thought 6 states that we need to pop out "{", "[", so we need to find the sequence of matching bracket pairs. So we need "}", "]". This does not match the part we are checking. So So we need "}", "]" is incorrect.
            Comment 3: So we need "}", "]" is incorrect, so Thought 6 is incorrect. No"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Complete the rest of the sequence, making sure that the brackets are closed properly. Input: < > ( ( [ [ ( { } ) [ < > ] ]
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: < ; stack: <
            Thought 4: > ; stack: empty
            Q: Is Thought 4 correct? Check through each sentence and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 4 by checking each sentence. Remaining: > ; stack: empty
            Comment 2: Checking: >. Thought 4 should look at the 2nd symbol in the input, >. This matches the symbol we are checking, >. So > is correct. Remaining: stack: empty
            Comment 3: Checking: stack: empty. Thought 4 should check if the second symbol > forms a bracket pair with the top item on the stack in Thought 3. If it does, the top item should be removed; if it does not, the new symbol should be added to the top of the stack. The stack in Thought 4 is <. After processing the symbol >, the stack should be empty. So stack: empty is correct. Remaining:
            Comment 4: > ; stack: empty is correct, so Thought 5 is correct. Yes"""
        ),
    },
    {
        "role": "user",
        "content": textwrap.dedent(
            """\
            Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < [ < [ { < [ ] < { } > > } ] > { { ( ) } { < [ < > ] > }
            Thought 1: We should process each input one by one and keep track of the stack configuration.
            Thought 2: stack: empty
            Thought 3: < ; stack: <
            Thought 4: [ ; stack: < [
            Thought 5: < ; stack: < [ <
            Thought 6: [ ; stack: < [ < [
            Thought 7: { ; stack: < [ <
            Q: Is Thought 7 correct? Check through each sentence and determine whether there are any errors."""
        ),
    },
    {
        "role": "assistant",
        "content": textwrap.dedent(
            """\
            Comment 1: I will identify any mistakes in Thought 7 by checking each sentence. Remaining: { ; stack: < [ <
            Comment 2: Checking: {. Thought 7 should look at the 5th symbol in the input, {. This matches the symbol we are checking, {. So { is correct. Remaining: stack: < [ <
            Comment 3: Checking: stack: < [ <. Thought 7 should check if the 5th symbol { forms a bracket pair with the top item on the stack in Thought 6. If it does, the top item should be removed; if it does not, the new symbol should be added to the top of the stack. The stack in Thought 6 is < [ < [. After processing the symbol {, the stack should be < [ < [ {. So stack: < [ < is incorrect. Remaining:
            Comment 4: stack: < [ < is incorrect, so Thought 7 is incorrect. No"""
        ),
    },
)
