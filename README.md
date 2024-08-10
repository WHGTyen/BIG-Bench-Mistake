# BIG-Bench Mistake

BIG-Bench Mistake is a dataset of chain-of-thought (CoT) outputs annotated with the location of the first logical mistake. This dataset was released as part of our paper, [_LLMs cannot find reasoning errors, but can correct them given the error location_](https://arxiv.org/abs/2311.08516).

![Our user interface for annotation](https://github.com/WHGTyen/BIG-Bench-Mistake/blob/main/annotation_guidelines/ui.png)

## Few-shot prompting results

In our paper, we use this dataset to benchmark LLMs in terms of their mistake-finding ability. We try 3 diffrent types of prompting, and find that LLMs struggle to identify logical mistakes. Results from GPT-4-Turbo, GPT-4, GPT-3.5-Turbo, Gemini Pro, and PaLM 2 Unicorn are shown below; for further details, please refer to [our paper](https://arxiv.org/abs/2311.08516). Prompts used for mistake finding are found [here](https://github.com/WHGTyen/BIG-Bench-Mistake/tree/main/mistake_finding_prompts).

![Image of Table 4 in our paper, comparing few-shot mistake-finding performance between GPT-4-Turbo, GPT-4, GPT-3.5-Turbo, Gemini Pro, and PaLM 2 Unicorn. The best result is from GPT-4 at 52.87 overall accuracy using direct step-level prompting.](https://github.com/WHGTyen/BIG-Bench-Mistake/blob/main/results.png)

## Data description

We use PaLM 2-L (Unicorn) to generate CoT traces for 5 tasks:

1.  Word Sorting
2.  Tracking Shuffled Objects
3.  Logical Deduction
4.  Multistep arithmetic
5.  Dyck Languages

In our experiments, we treat Tracking Shuffled Objects and Logical Deduction as multiple choice tasks, while for Word Sorting, Multistep Arithmetic, and Dyck Languages we use exact matching.

We then recruit human annotators to identify mistake steps in 4 of the 5 tasks. For Dyck languages, we automatically annotate most of the traces using `annotate_dyck_langauges.py`. For further details, please refer to [our paper](https://arxiv.org/abs/2311.08516).

Each JSONL file contains outputs for a task from the [BIGBench](https://github.com/google/BIG-bench/tree/main) dataset. Each line contains a dictionary with the following keys:

- `input`: A string containing the input question. For multiple choice tasks (Tracking Shuffled Objects and Logical Deduction), this also includes the options.
- `steps`: A list of strings containing each step in the chain of thoughts. Note that this does not include the prefixes `Thought 1:`, `Thought 2:`, etc.
- `answer`: A string containing the model's answer, extracted from the list of steps using the regex `(?<=[Tt]he answer is).*$`. For multiple choice tasks (Tracking Shuffled Objects and Logical Deduction), this is the letter indicating the option (e.g. `(A)`).
- `target`: A string containing the target "correct" answer.
- `mistake_index`: The index of the step containing the first logical mistake. Please note that **this number is 0-indexed**, so 0 indicates a mistake in the first step, 1 indicates a mistake in the second step, and so on. If there are no mistakes, this value is null.

## Citation

```
@inproceedings{tyen-etal-2024-llms,
    title = "{LLMs} cannot find reasoning errors, but can correct them given the error location",
    author = "Tyen, Gladys and Mansoor, Hassan and C\u{a}rbune, Victor and Chen, Peter and Mak, Tony",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2024",
    year = "2024",
    publisher = "Association for Computational Linguistics",
}
```
