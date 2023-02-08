import openai


def get_gpt_resp(prompt):
    openai.api_key = "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"
    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    print(completion)

    response = completion.choices[0].text
    return response

