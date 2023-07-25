# querySupport

## Problem

### Problem Statement
Given a list of 30 made up queries to customer support we would like you to predict the 
label in column B using LLM prompts and to create evaluation metrics to quantify the 
performance of your classifier. 

### Assumptions
The following assumptions were made:
1. The dataset's `queries` column comprises of sentences reflective of dialogue between a client and a customer support representative.
2. The `IsClear` column is a binary categorization that labels each query as TRUE if the customer's request is specific and actionable by a customer support agent.
## Approach

### Dataset
The available dataset was divided into training, validation, and testing subsets. 

**Train**: Comprises 4 randomly selected, class-balanced queries utilized as exemplars in prompts during prompt engineering and synthetic data generation.

**Valid**: Comprises 6 random, class-balanced queries. This subset was utilized for the initial prompt evaluation before testing.

**Test**: The test set contains 19 given queries and was used for the final evaluation of the classifier.

### Prompts
Based on existing literature, the following categories of prompts were explored and tested:
1. Zero-shot prompting
2. Few-shot prompting
3. Chain of Thought (CoT) prompting
4. Clue and Reasoning Prompting (CARP)

Each prompt type was evaluated with results subsequently discussed in the results section.

### Demonstration selection
The examples utilized within prompts during inference were selected based on their similarity to the test set (also known as in-context selection). This strategy generally enhances the performance of LLMs.

### Voting
The final result is the most frequent answer after 3 runs, to take advantage of the diverse sampling strategies
in LLMs

### Model
The gpt-4 model was used via the OpenAI API

### Evaluation

The performance of the classifier was evaluated using the following metrics
1. Accuracy
2. Recall
3. Precision
4. Fbeta score

An Fbeta score, with beta equal to 2, is employed as it lays more emphasis on recall. This scoring approach aligns with the task's objectives as false positives are more desirable than false negatives in this context.

## Results

| Prompts          | Accuracy | Precision | Recall | F2   | Avg_total_tokens |
|------------------|:---------|-----------|--------|------|------------------|
| Zero-shot        | 0.68     | 1.00      | 0.40   | 0.45 | 137.3            |
| Few-shot         | 0.79     | 1.00      | 0.60   | 0.65 | 446.0            |
| Chain-of-thought | 0.83     | 0.75      | 1.0    | 0.94 | 526.2            |
| CARP             | 0.89     | 1.0       | 0.8    | 0.83 | 764.2            |

CARP and Chain-of-thought prompts deliver superior performance compared to Zero-shot and Few-shot prompts across all evaluation metrics. Although 
the chain-of-thought prompt has a higher recall score. The CARP prompt has an higher accuracy and provides more information about the decision of the model. 
This insight can facilitate prompt modification, spurious features detection and enhance model explainability, but at the expense of more tokens. To enhance the model's recall,
the output can be converted into a probability score, with classification threshold adjustments as needed.

## References
1. Text Classification via Large Language Models https://arxiv.org/abs/2305.08377
2. What Makes Good In-Context Examples for GPT-3 https://arxiv.org/pdf/2101.06804.pdf
3. Prompt Engineering https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/