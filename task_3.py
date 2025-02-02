from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List
from enum import Enum


class LineItem(BaseModel):
    item: str = Field(..., title="Item name")
    quantity: int = Field(..., title="Quantity of item")
    unit_price: float = Field(..., title="Unit price of item in dollars")


class ShippingStatus(Enum):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"


class Order(BaseModel):
    order_id: str = Field(..., title="Order ID")
    customer_name: str = Field(..., title="Customer name")
    items_ordered: List[LineItem] = Field(..., title="List of items ordered")
    total_price: float = Field(..., title="Total price of order in dollars")
    shipping_status: ShippingStatus = Field(..., title="Shipping status of order")
    estimated_delivery_date: str = Field(..., title="Estimated delivery date")
    cot: str = Field(
        ...,
        title="Your description for how you extracted each of the order details in a step by step manner",
    )


client = OpenAI()

info_strings = [
    "Dear Sarah Johnson, your order (Order ID: ORD987654) is in transit. Your purchase includes 1 Wireless Headphones ($70) and 2 Laptop Stands ($25 each), totaling $120. Estimated delivery date: February 5, 2025. Thank you for shopping with us!",
    "Sarah, your package (ORD987654) is cruising toward you! 🚀 Inside: 1 Wireless Headphones and 2 Laptop Stands—because one stand just wasn’t enough! Total: $120. ETA: Feb 5, 2025. Get ready!",
]

for info_str in info_strings:
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant whose job is to extract information from any document.",
            },
            {"role": "user", "content": info_str},
        ],
        response_format=Order,
    )

    response = response.choices[0].message.parsed

    print(info_str, response, "", sep="\n")
