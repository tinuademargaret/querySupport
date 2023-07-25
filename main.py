import os
import ast
import openai
import time
import pandas as pd
from collections import Counter
from dotenv import load_dotenv
from prompts import get_prompt
from evaluations import evaluate
from embedding import get_embedding, get_samples

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def classifier(prompt_type, n, random_samples=True):
    y_true = []
    y_pred = []
    test_df = pd.read_csv('./test.csv', dtype={'classification': str})
    train_df = pd.read_csv('./train.csv', dtype={'classification': str})

    for i in range(len(test_df)):
        test = test_df.iloc[i]
        y_true.append(1 if test["classification"] == "TRUE" else 0)
        test_embed = ''
        if random_samples is False:
            test_embed = get_embedding(test["sentence"])
        sample_idx = get_samples(test_embed, 6, is_random=random_samples)
        # content used as an example of test prompts
        user_content = [train_df.iloc[idx, 0] for idx in sample_idx]
        # content used as an example of model response
        assistant_content = ''
        if prompt_type == "few":
            assistant_content = [{"query": train_df.iloc[idx, 0],
                                  "clues": train_df.iloc[idx, 2]
                                  } for idx in sample_idx]
        if prompt_type == "cot":
            assistant_content = [{"query": train_df.iloc[idx, 0],
                                  "reasoning": train_df.iloc[idx, 3],
                                  "classification": train_df.iloc[idx, 1]
                                  } for idx in sample_idx]

        if prompt_type == "carp":
            assistant_content = [{"query": train_df.iloc[idx, 0],
                                  "clues": train_df.iloc[idx, 2],
                                  "reasoning": train_df.iloc[idx, 3],
                                  "classification": train_df.iloc[idx, 1]
                                  } for idx in sample_idx]

        prompt = get_prompt("v0", prompt_type, user_content, test["sentence"], assistant_content)

        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=prompt,
            temperature=0,
            max_tokens=1000,
            n=n,
        )
        # get all the responses and choose the mode
        final_class = []
        for i in range(n):
            if response['choices'][i]['finish_reason'] == 'stop':
                content = ast.literal_eval(response['choices'][i]['message']['content'])
                final_class.append(content["classification"])
        classification = Counter(final_class).most_common(1)[0][0]
        y_pred.append(1 if classification == "TRUE" else 0)

        # sleep to avoid rate limit
        time.sleep(20)

    return evaluate(y_true, y_pred)


if __name__ == '__main__':
    print(classifier("zero", 1, random_samples=False))
