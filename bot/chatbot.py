import openai


def get_gpt_resp(prompt):
    # openai.api_key = "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"
    openai.api_key = "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"

    model_engine = "text-davinci-003"

    completion = openai.Completion.create(
        engine=model_engine,
        # model="gpt-4",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # print(completion)

    response = completion.choices[0].text

    # response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
    #                                         # model="gpt-4",
    #                                         messages=[
    #                                             {"role": "user", "content": prompt}],
    #                                         temperature=0.5,
    #                                         max_tokens=200)
    #                                         # n=1,
    #                                         # stop=None
    #                                         # seed=i)


    return response.choices[0].message['content']

