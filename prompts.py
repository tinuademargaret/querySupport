def get_prompt(version, name, user_content,  test_content, assistant_content=None):
    prompts_map = {
        "v0": {
            "zero": [
                {
                    "role": "system",
                    "content": "You are a customer support agent. You are given a sentence that can "
                               "occur in a conversation between a customer and a customer support agent. Your"
                               "task is to classify the sentence as TRUE or FALSE. A sentence is TRUE"
                               "if it is clear and easy to understand. It should include a specific subject, it should "
                               "be actionable or "
                               "at least talk about a specific subject that a customer support agent "
                               "can help with or follow up on, not just consisting of general expressions "
                               "). Your output should be a python dictionary in "
                               "the format: {'query': '', 'classification': ''}, {'query': '', 'classification':'' } "
                },
                {
                    "role": "user",
                    "content": f"{test_content}"
                }
            ],
            "few": [
                {
                    "role": "system",
                    "content": "You are a customer support agent. You are given a sentence that can "
                               "occur in a conversation between a customer and a customer support agent. Your"
                               "task is to classify this sentence as TRUE or FALSE. A sentence is TRUE"
                               "if it is clear and easy to understand. It should include a specific subject, it should "
                               "be actionable or "
                               "at least talk about a specific subject that a customer support agent "
                               "can help with or follow up on, not just consisting of general expressions "
                               ").Your output should be a python dictionary in "
                               "the format: {'query': '', 'classification': ''}"
                },
                {
                    "role": "user",
                    "content": f"{user_content}"

                },
                {
                    "role": "assistant",
                    "content": f"{assistant_content}"

                },
                {
                    "role": "user",
                    "content": f"{test_content}"
                }
            ],
            "cot": [
                {
                    "role": "system",
                    "content": "You are a customer support agent. You are given a sentence that can "
                               "occur in a conversation between a customer and a customer support agent. Your"
                               "task is to classify the sentence as TRUE or FALSE. A sentence is TRUE"
                               "if it is clear and easy to understand. It should include a specific subject, it should "
                               "be actionable or "
                               "at least talk about a specific subject that a customer support agent "
                               "can help with or follow up on, not just consisting of general expressions "
                               "). Your output should be a python dictionary in "
                               "the format: {'query': '', 'reasoning': '', 'classification':'' }"
                },
                {
                    "role": "user",
                    "content": f"{user_content}"

                },
                {
                    "role": "assistant",
                    "content": f"{assistant_content}"

                },
                {
                    "role": "user",
                    "content": f"{test_content}"
                }
            ],
            "carp": [
                {
                    "role": "system",
                    "content": "You are a customer support agent. You are given a sentence that can "
                               "occur in a conversation between a customer and a customer support agent. Your"
                               "task is to classify the sentence as TRUE or FALSE. A sentence is TRUE"
                               "if it is clear and easy to understand. It should include a specific subject, it should "
                               "be actionable or "
                               "at least talk about a specific subject that a customer support agent "
                               "can help with or follow up on, not just consisting of general expressions "
                               "). First, list CLUES (i.e., specific request subjects, "
                               "action keywords, tasks, phrases, contextual information, tones, references) for "
                               "determining the overall clarity and purpose of the sentence. "
                               "Based on the sentence and clues, articulate the diagnostic reasoning process that "
                               "supports the classification of the sentence. Finally, based on clues, the reasoning "
                               "and the sentence, categorize the overall sentence as TRUE or FALSE."
                               "Your output should be a python dictionary in "
                               "the format: {'query': '', 'clues': '', 'reasoning':'', 'classification':'' }, "
                },
                {
                    "role": "user",
                    "content": f"{user_content}"
                },
                {
                    "role": "assistant",
                    "content": f"{assistant_content}"
                },
                {
                    "role": "user",
                    "content": f"{test_content}"
                }
            ]
        }
    }
    return prompts_map[version][name]
