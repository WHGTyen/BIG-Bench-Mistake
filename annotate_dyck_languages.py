"""Identify the location of mistakes in generated traces for the Dyck languages task.

The input JSONL file should contain dictionaries with the following keys:
  input: The input string for each question, e.g. "< > ( ( [ [ ( { } ) [ < > ]"
  steps: A list of strings containing the steps (without the Thought 1, Thought
    2, etc. prefix), e.g. ["We should process each input one by one and keep
    track of the stack configuration.", "stack: empty", ...]

The output JSONL file will contain the same dictionaries but with the additional
key "mistake_index", a zero-indexed number indicating the step in which the
first mistake occurs. None / null indicates that there are no mistakes.


For each input question in the task, we first generate a synthetic trace using
the standard format (see generation_prompts/dyck_languages_prompt.txt for
examples). We then compare each step of the synthetic trace to the corresponding
step in the model-generated trace.
"""

import json
import os
import re
from typing import Any, Dict, List, Sequence

from absl import app
from absl import flags
from absl import logging
import immutabledict
import tabulate

_INPUT_FILE = flags.DEFINE_string(
    "input_file",
    None,
    "JSONL file containing generated traces for Dyck languages.",
    required=True,
)
_OUTPUT_FILE = flags.DEFINE_string(
    "output_file", None, "Output JSONL filepath", required=True
)

# Regex corresponding to intermediate steps that lists the next symbol and the
# current stack
# Example matches:
# [ ; stack: [ ( {
# > ; stack: empty
STACK_REGEX = re.compile(
    r"[{}\(\)\[\]<>] ; stack: (([{}\(\)\[\]<> ]+)|(empty))"
)

# Regexes corresponding to the last three steps of a typical trace
THIRD_LAST_REGEX = re.compile(
    r"Now, we have reached the end\. The final stack is ([{}\(\)\[\]<> ]+)\.?"
)
SECOND_LAST_REGEX = re.compile(
    r"We will need to pop out ([{}\(\)\[\]<> ]+),? one by one in that order\.?"
)
LAST_REGEX = re.compile(
    r"So, we need [{}\(\)\[\]<> ]+\. So the answer is ([{}\(\)\[\]<> ]+)\.?"
)

# Regex corresponding to an alternative version of the last step + second to
# last step, which combines both into one step, e.g.
# Synthetic:
#   We will need to pop out "{" one by one in that order.
#   So, we need "}". So the answer is }
# Model:
#   We will need to pop out "{". So the answer is }
LAST_REGEX_ALTERNATIVE = re.compile(
    r"We will need to pop out ([{}\(\)\[\]<> ]+). So the answer is"
    r" ([{}\(\)\[\]<> ]+)\.?"
)

OPEN_TO_CLOSE_BRACKET = immutabledict.immutabledict({
    "[": "]",
    "(": ")",
    "<": ">",
    "{": "}",
})
CLOSE_TO_OPEN_BRACKET = immutabledict.immutabledict(
    {
        close_bracket: open_bracket
        for open_bracket, close_bracket in OPEN_TO_CLOSE_BRACKET.items()
    }
)


def pretty_print_comparison(steps1: List[str], steps2: List[str]) -> None:
  """Prints 2 sequences of strings in 2 columns.

  Args:
    steps1: List of strings to be displayed in the left column
    steps2: List of strings to be displayed in the right column. String will be
      replaced by "SAME" if it is the same as the corresponding step in the left
      column.
  """
  table = []
  table_length = max(len(steps1), len(steps2))
  for i in range(table_length):
    if i < len(steps1) and i < len(steps2):
      step1 = steps1[i]
      step2 = steps2[i]

      if step1 == step2:
        table.append([step1, "SAME"])
      else:
        table.append([step1, step2])

    elif i < len(steps1):
      table.append([steps1[i], ""])
    else:
      assert i < len(steps2)
      table.append(["", steps2[i]])

  col_width = int(os.get_terminal_size()[0] / 2)
  print(
      tabulate.tabulate(
          table, maxcolwidths=[col_width, col_width], tablefmt="fancy_grid"
      )
  )


def save_traces(traces: List[Dict[str, Any]], filepath: str):
  with open(filepath, "w") as results_file:
    results_file.write("\n".join(json.dumps(trace) for trace in traces) + "\n")


def load_traces(filepath: str) -> List[Dict[str, Any]]:
  traces = []
  with open(filepath, "r") as trace_file:
    for line in trace_file:
      traces.append(json.loads(line))
  return traces


def generate_correct_traces(input_str: str) -> List[str]:
  """Generate the "correct" steps for the Dyck languages task algorithmically.

  We follow the trace format used in the prompt (see
  generation_prompts/dyck_languages_prompt.txt). All
  traces begin with the same two steps:
    We should process each input one by one and keep track of the stack
    configuration.
    stack: empty
  which is followed by a series of steps going through each symbol in the input.
  For example, if the first symbol is [, we add it onto the stack like so:
    [; stack: [
  If we encounter a closing symbol, it should match up to the most recent symbol
  on the stack, which is then removed, e.g.
    [; stack: [
    ]; stack: empty
  Finally, when the whole input has been processed, we add three more steps to
  the end, in order to process the final stack and produce an answer. For
  example:
    Now, we have reached the end. The final stack is "[ { [".
    We will need to pop out "[", "{", "[" one by one in that order.
    So, we need "]", "}", "]". So the answer is ] } ]

  Args:
    input_str: The input string for the question, e.g. "< > ( ( [ [ ( { }"

  Returns:
    A list of algorithmically generated steps following the format in prompt
    examples.
  """
  steps = [
      (
          "We should process each input one by one and keep track of the stack"
          " configuration."
      ),
      "stack: empty",
  ]
  stack = []
  stack_str = "empty"
  for symbol in input_str.split(" "):
    assert symbol in "[]{}()<>", "Invalid symbol: {} Input: {}".format(
        symbol, input_str
    )
    if (
        stack
        and symbol in CLOSE_TO_OPEN_BRACKET
        and stack[-1] == CLOSE_TO_OPEN_BRACKET[symbol]
    ):
      stack.pop()
    else:
      stack.append(symbol)

    stack_str = " ".join(stack)
    if len(stack) == 0:
      stack_str = "empty"
    steps.append(f"{symbol} ; stack: {stack_str}")

  assert stack_str != "empty", "Final stack should not be empty"
  reverse_stack_str_with_brackets = '"' + '", "'.join(reversed(stack)) + '"'

  steps.append(
      f'Now, we have reached the end. The final stack is "{stack_str}".'
  )
  steps.append(
      f"We will need to pop out {reverse_stack_str_with_brackets} one by one in"
      " that order."
  )

  for symbol in stack:
    assert (
        symbol in OPEN_TO_CLOSE_BRACKET
    ), f"Closing symbol {symbol} found in final stack"

  stack_pairing = [OPEN_TO_CLOSE_BRACKET[symbol] for symbol in reversed(stack)]
  stack_pairing_str = " ".join(stack_pairing)
  stack_pairing_str_with_brackets = '"' + '", "'.join(stack_pairing) + '"'
  steps.append(
      f"So, we need {stack_pairing_str_with_brackets}. So the answer is"
      f" {stack_pairing_str}"
  )

  return steps


def normalise(text: str) -> str:
  """Normalise Dyck languages strings to account for quotes and punctuation."""
  if not text:
    return text

  text = text.replace(" and ", ", ")
  text = text.replace('", "', " ")
  text = text.replace(' ".', '".')
  text = text.replace('"', "")

  if text[-1] == ".":
    text = text[:-1]

  return text


def has_same_format(step1: str, step2: str) -> bool:
  """Determine if two steps have the same format.

  We use regexes STACK_REGEX, THIRD_LAST_REGEX, SECOND_LAST_REGEX, LAST_REGEX to
  identify the type of the step:
  - STACK_REGEX matches steps that contain the symbol that is currently
    processed and the stack, e.g. [ ; stack: [ { [
  - THIRD_LAST_REGEX matches the third-to-last step, which states, "Now, we
    have reached the end. The final stack is {final stack}." Note that the
    final stack should only contain open brackets; otherwise, the input is not
    a well-formed Dyck language.
  - SECOND_LAST_REGEX matches the second-to-last step, which states, "We will
    need to pop out {stack in reversed order} one by one in that order." The
    order here is reversed to indicate the order in which symbols are popped
    out of the stack.
  - LAST_REGEX matches the last step, which states, "So, we need {answer}. So
    the answer is {answer}"

  Args:
    step1: one of the two steps
    step2: the other of the two steps

  Returns:
    A boolean indicating whether the two steps have the same format
  """
  return bool(
      (STACK_REGEX.fullmatch(step1) and STACK_REGEX.fullmatch(step2))
      or (
          THIRD_LAST_REGEX.fullmatch(step1)
          and THIRD_LAST_REGEX.fullmatch(step2)
      )
      or (
          SECOND_LAST_REGEX.fullmatch(step1)
          and SECOND_LAST_REGEX.fullmatch(step2)
      )
      or (LAST_REGEX.fullmatch(step1) and LAST_REGEX.fullmatch(step2))
  )


def is_combined_steps_match(
    synthetic_step: str, next_synthetic_step: str, model_step: str
) -> bool:
  """Check for cases where the final two steps are combined into one."""
  # Find the stack in the current synthetic step
  synthetic_step_match = SECOND_LAST_REGEX.search(synthetic_step)
  assert synthetic_step_match is not None
  correct_stack = synthetic_step_match.group(1)

  # Find the answer in the next synthetic step
  synthetic_next_step_match = LAST_REGEX.search(next_synthetic_step)
  assert synthetic_next_step_match is not None
  correct_answer = synthetic_next_step_match.group(1)

  # Find the stack and answer in the current model step (which should
  # be the last one)
  model_step_match = LAST_REGEX_ALTERNATIVE.search(model_step)
  assert model_step_match is not None
  model_stack = model_step_match.group(1)
  model_answer = model_step_match.group(2)

  return correct_stack == model_stack and correct_answer == model_answer


def get_mismatched_step(
    model_steps: Sequence[str], synthetic_steps: Sequence[str]
) -> int:
  """Identify the mismatched step between a model generated trace and a synthetically generated trace.

  This function goes through each step of the trace and compares it to the
  corresponding synthetic step. If we find a mismatched step, we immediately
  return the index of the step and ignore the remaining trace. If there are no
  mismatched steps at the end, return -1.

  We use regexes to determine whether a step fits into one of 4 types (see
  has_same_format). A ValueError is raised when the type of step is not detected
  (and not accounted for in our edge cases). If the two steps that we are
  comparing have type STACK and THIRD_LAST, we assume that there is a mistake as
  the model generated trace is either too long or too short.

  In addition, we use LAST_REGEX_ALTERNATIVE to check for an alternative version
  of the last two steps which have been combined into one, e.g.
  Synthetic: (2 steps)
    - We will need to pop out "{" one by one in that order.
    - So, we need "}". So the answer is }
  Model: (1 step)
    - We will need to pop out "{". So the answer is }

  More examples:
    [ ; stack: [
    [ ; stack: { [
    Both steps contain the stack and are matched by the STACK_REGEX. However,
    they do not match even after normalisation, so this is considered an
    incorrect step.

    [ ; stack: { [
    [ ; stack: "{", "["
    These steps use the same symbols but one has quotes and the other does not.
    This is captured during the normalisation process where [ ; stack: "{", "["
    is normalised to [ ; stack: { [ therefore matching the first version.

    [ ; stack: [ (
    Now, we have reached the end. The final stack is "[ ("
    These steps have different formats, suggesting that the model trace is
    either too short or too long. We assume that there is a mistake and label
    this as an incorrect step.

  Args:
    model_trace: Trace object containing a complete trace.
    synthetic_steps: The "correct" steps generated algorithmically using
      generate_correct_traces

  Returns:
    A zero-indexed number indicating which step is incorrect. -1 if all steps
    are correct.
  """
  normalised_synthetic_steps = [
      normalise(synthetic_step) for synthetic_step in synthetic_steps
  ]
  normalised_model_steps = [normalise(model_step) for model_step in model_steps]

  assert THIRD_LAST_REGEX.fullmatch(normalised_synthetic_steps[-3]) is not None
  assert SECOND_LAST_REGEX.fullmatch(normalised_synthetic_steps[-2]) is not None
  assert LAST_REGEX.fullmatch(normalised_synthetic_steps[-1]) is not None

  for i, (synthetic_step, model_step) in enumerate(
      zip(synthetic_steps, model_steps)
  ):
    normalised_synthetic_step = normalised_synthetic_steps[i]
    normalised_model_step = normalised_model_steps[i]

    # First two steps should be the same across all traces
    if i == 0 or i == 1:
      if normalised_model_step == normalised_synthetic_step:
        continue
      else:
        raise ValueError("All traces should have the same first two steps.")

    # Checks for steps with the same format
    elif has_same_format(normalised_model_step, normalised_synthetic_step):
      if normalised_model_step != normalised_synthetic_step:
        return i

    # Capture traces where the model goes into the ending text part
    # too early or too late. We assume that this is always wrong. E.g.
    # Synthetic:
    #   ( ; stack: [ (
    #   { ; stack: [ ( {
    #   Now, we have reached the end. The final stack is "[ ( {".
    # Model:
    #   ( ; stack: [ (
    #   Now, we have reached the end. The final stack is "[ (".
    elif (
        STACK_REGEX.fullmatch(normalised_model_step)
        and THIRD_LAST_REGEX.fullmatch(normalised_synthetic_step)
    ) or (
        THIRD_LAST_REGEX.fullmatch(normalised_model_step)
        and STACK_REGEX.fullmatch(normalised_synthetic_step)
    ):
      return i

    # Capture traces where the model combines the last two steps, e.g.
    # Synthetic:
    #   We will need to pop out "{" one by one in that order.
    #   So, we need "}". So the answer is }
    # Model:
    #   We will need to pop out "{". So the answer is }
    elif (
        SECOND_LAST_REGEX.fullmatch(normalised_synthetic_step)
        and LAST_REGEX_ALTERNATIVE.fullmatch(normalised_model_step)
        and i == len(model_steps) - 1
    ):
      if is_combined_steps_match(
          normalised_synthetic_step,
          normalise(synthetic_steps[i + 1]),
          normalised_model_step,
      ):
        # Since it is the last step, we can immediately return
        return None
      else:
        return i

    # Go through exceptions we've found that we manually checked are correct
    elif (
        synthetic_step
        == 'We will need to pop out "[", "{", "<" one by one in that order.'
        and model_step
        == 'We will need to pop out "[" ,"{" ,"<" one by one in that order.'
    ):
      return None
    elif (
        synthetic_step == 'So, we need ">", "}". So the answer is > }'
        and model_step == "So, we need > }"
        and model_steps[i + 1] == "So the answer is > }"
    ):
      return None
    elif (
        synthetic_step
        == 'We will need to pop out "[", "[", "<" one by one in that order.'
        and model_step == 'We will need to pop out "[" twice, then "<".'
        and synthetic_steps[i + 1]
        == 'So, we need "]", "]", ">". So the answer is ] ] >'
        and model_steps[i + 1]
        == 'So, we need "]", "]", ">". So the answer is ] ] >'
    ):
      return None
    elif (
        synthetic_step
        == 'We will need to pop out "[", "[", "{" one by one in that order.'
        and model_step
        == 'We will need to pop out "[" twice and "{" once in that order.'
        and synthetic_steps[i + 1]
        == 'So, we need "]", "]", "}". So the answer is ] ] }'
        and model_steps[i + 1]
        == 'So, we need "]", "]", "}". So the answer is ] ] }'
    ):
      return None

    else:
      raise ValueError(
          "Format mismatch. This example requires human annotation."
      )

  # Model trace is shorter, some steps have been skipped
  if len(synthetic_steps) > len(model_steps):
    raise ValueError(
        "Some steps have been skipped. This example requires human annotation."
    )

  # Model has added extra steps
  if len(model_steps) > len(synthetic_steps):
    return len(synthetic_steps)

  return None


def main(argv: Sequence[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  model_traces = load_traces(_INPUT_FILE.value)

  annotated_traces = []
  for model_trace in model_traces:
    synthetic_steps = generate_correct_traces(model_trace["input"])

    # Ignore traces that have reached max steps (200) because it is
    # likely the trace is not complete
    if len(synthetic_steps) >= 200 or len(model_trace["steps"]) >= 200:
      logging.warning(
          "Trace reached maximum number of steps and is possibly unfinished."
          " Skipping."
      )
      continue

    # Ignore traces whose steps (approximately) exceed the maximum number
    # of tokens (1024).
    maximum_output_reached = False
    for step in model_trace["steps"]:
      if len(step.split(" ")) >= 1024:
        maximum_output_reached = True
        break

    if maximum_output_reached:
      logging.warning(
          "Trace step reached maximum number of tokens and is possibly"
          " unfinished. Skipping whole trace."
      )
      continue

    # Ignore traces which we considered to be edge cases
    # Since there are only so few instances, including/excluding these examples
    # will have a negligible impact on the final benchmark scores.
    if model_trace["input"] in [
        "{ < ( { { } } )",
        "{ < [ { ( ) } ]",
        "( { ( ( ) ) } ) { ( (",
        "{ [ <",
        "[ < [ < > ( ) ]",
        "( { < [ [ { [ ] } ] ]",
    ]:
      continue

    try:
      mismatched_step = get_mismatched_step(
          model_trace["steps"], synthetic_steps
      )
    except ValueError:
      logging.warning(
          "ENTRY REQUIRES HUMAN ANNOTATION: %s", model_trace["input"]
      )
      pretty_print_comparison(synthetic_steps, model_trace["steps"])
    else:
      model_trace["mistake_index"] = mismatched_step
      annotated_traces.append(model_trace)

  print(
      f"Skipped {len(model_traces) - len(annotated_traces)} traces out of"
      f" {len(model_traces)}"
  )

  save_traces(annotated_traces, _OUTPUT_FILE.value)


if __name__ == "__main__":
  app.run(main)
