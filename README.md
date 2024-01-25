# BIG-Bench Mistake

BIG-Bench Mistake is a dataset of chain-of-thought (CoT) outputs annotated with
the location of the first logical mistake. This dataset was released as part of
our paper, [_LLMs cannot find reasoning errors, but can correct them!_](https://arxiv.org/abs/2311.08516).

![Our user interface for annotation](https://github.com/WHGTyen/BIG-Bench-Mistake/blob/main/annotation_guidelines/ui.png)

## Tasks

Our CoT steps are generated for 5 tasks:

1.  Word Sorting
2.  Tracking Shuffled Objects
3.  Logical Deduction
4.  Multistep arithmetic
5.  Dyck Languages

In our experiments, we treat Tracking Shuffled Objects and Logical Deduction as
multiple choice tasks, while for Word Sorting, Multistep Arithmetic, and Dyck
Languages we use exact matching.

## Data description

We use PaLM 2-L (Unicorn) to generate CoT traces for all 5 tasks. We then
recruit human annotators to identify mistake steps in 4 of the 5 tasks. For Dyck
languages, we automatically annotate most of the traces using
`annotate_dyck_langauges.py`. For further details, please refer to
[our paper](https://arxiv.org/abs/2311.08516).

Each JSONL file contains outputs for a task from the
[BIGBench](https://github.com/google/BIG-bench/tree/main) dataset. Each line
contains a dictionary with the following keys:

- `input`: A string containing the input question. For multiple choice tasks
  (Tracking Shuffled Objects and Logical Deduction), this also includes the
  options.
- `steps`: A list of strings containing each step in the chain of thoughts.
  Note that this does not include the prefixes `Thought 1:`, `Thought 2:`,
  etc.
- `answer`: A string containing the model's answer, extracted from the list of
  steps using the regex `(?<=[Tt]he answer is).*$`. For multiple choice tasks
  (Tracking Shuffled Objects and Logical Deduction), this is the letter
  indicating the option (e.g. `(A)`).
- `target`: A string containing the target "correct" answer.
- `mistake_index`: The index of the step containing the first logical mistake.
  Please note that **this number is 0-indexed**, so 0 indicates a mistake in
  the first step, 1 indicates a mistake in the second step, and so on. If
  there are no mistakes, this value is null.

## Citation

```
@article{tyen2023llms,
  title={LLMs cannot find reasoning errors, but can correct them!},
  author={Tyen, Gladys and Mansoor, Hassan and C\u{a}rbune, Victor and Chen, Peter and Mak, Tony},
  journal={arXiv preprint arXiv:2311.08516},
  year={2023}
}
```
