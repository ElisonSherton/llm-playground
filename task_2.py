from pydantic import BaseModel, Field
from openai import OpenAI
from enum import Enum

client = OpenAI()


class TransactionStatus(Enum):
    """Enum to denote the status of a bank transaction"""

    pending = "pending"
    completed = "completed"
    failed = "failed"


class TransactionItem(BaseModel):
    """Structure to denote a bank transaction"""

    sender: str = Field(..., description="The name of the sender.")
    receiver: str = Field(..., description="The name of the receiver.")
    amount: int = Field(..., description="The amount of money transferred.")
    currency: str = Field(
        ..., description="The currency in which the transaction was made."
    )
    transaction_id: str = Field(
        ..., description="An alphanumeric unique identifier for the transaction."
    )
    timestamp: str = Field(
        ..., description="The date and time of the transaction in ISO 8601 format."
    )
    status: TransactionStatus = Field(..., description="The status of the transaction.")


info_strings = [
    "Dear John Doe, your transaction of $500 USD to Alice Smith has been successfully processed. Transaction ID: TXN123456789. Timestamp: 2025-02-01T10:30:00Z. Thank you for banking with us.",
    "Hey John! Your $500 transfer to Alice Smith went through successfully. Transaction ID: TXN123456789. Done at 10:30 AM (UTC) on Feb 1, 2025. Let us know if you need anything else!",
    "Cha-ching! $500 has left your account and made its way to Alice Smith. Transaction ID: TXN123456789. Completed at 10:30 AM UTC on Feb 1, 2025. No refunds from Alice—good luck!",
]

for info_str in info_strings:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {"role": "user", "content": info_str},
        ],
        response_format=TransactionItem,
    )

    response = completion.choices[0].message.parsed
    print(info_str, response, "", sep="\n")