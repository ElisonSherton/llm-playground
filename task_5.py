from pydantic import BaseModel, Field
from openai import OpenAI
from typing import List
from enum import Enum


class Intent(Enum):
    ACCOUNT_BALANCE_INQUIRY = "account_balance_inquiry"
    OPEN_ACCOUNT = "open_account"
    CLOSE_ACCOUNT = "close_account"
    TRANSFER_MONEY = "transfer_money"


class IntentPrediction(BaseModel):
    intent: Intent = Field(..., title="The intent of the provided utterance")
    confidence: float = Field(
        ..., title="The confidence of the model for the provided intent"
    )


class ClassificationOutput(BaseModel):
    utterance: str = Field(..., title="The utterance to be classified")
    predictions: List[IntentPrediction] = Field(
        ..., title="The intents to which the provided utterance can be mapped to"
    )


info_strings = [
    """
    You just said "I want to check my account balance and transfer $100 to my friend."
    Your request includes multiple actions:

    1️⃣ Account Balance Inquiry (Confidence: 92%) – Would you like to check your account balance first?

    2️⃣ Fund Transfer (Confidence: 89%) – You requested to transfer $100 to your friend. Shall we proceed?

    Please confirm how you'd like to proceed.
    """,
    """
    You just said "I want to check my account balance and transfer $100 to my friend."
    Looks like you want to do two things:

    💰 Check account balance (92% confidence)
    💸 Transfer $100 to your friend (89% confidence)

    Which one should we handle first?
    """,
    """
    You just said "I want to check my account balance and transfer $100 to my friend."
    Whoa! You’re multitasking! Here’s what I got:

    📊 Check your balance (92% sure you need this)
    💵 Send $100 to a friend (89% sure you mean business)

    What should we tackle first—money check or money move?
    """,
]

client = OpenAI()

for info_str in info_strings:
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant whose job is to extract information from provided document.",
            },
            {"role": "user", "content": info_str},
        ],
        response_format=ClassificationOutput,
    )

    response = response.choices[0].message.parsed

    print(info_str, response, "", sep="\n")
