Performing some tasks related to structured outputs to write in terms of pydantic schema and practise it.

---

# Task 1: Weather Chatbot Response
**Scenario:** You are building a weather chatbot. Create a structured output for the following query:  
**User Query:** *"What’s the weather like in New York?"*  
**Raw Data:**  
- **City:** New York  
- **Temperature:** 12°C  
- **Condition:** Cloudy  
- **Humidity:** 72%  
- **Wind Speed:** 15 km/h  

---

# Task 2: Banking Chatbot - Fund Transfer Confirmation  
**Scenario:** A banking chatbot processes fund transfers. Design a structured output for the following transaction.  
**Transaction Details:**  
- **Sender:** John Doe  
- **Receiver:** Alice Smith  
- **Amount:** $500  
- **Currency:** USD  
- **Status:** Successful  
- **Transaction ID:** TXN123456789  
- **Timestamp:** 2025-02-01T10:30:00Z  

---

# Task 3: E-commerce Chatbot - Order Tracking
**Scenario:** A customer asks an e-commerce chatbot for order status. Create a structured output.  
**Order Details:**  
- **Order ID:** ORD987654  
- **Customer Name:** Sarah Johnson  
- **Items Ordered:**  
  - **Item 1:** Wireless Headphones (Qty: 1, Unit Price: $70)  
  - **Item 2:** Laptop Stand (Qty: 2, Unit Price: $25)  
- **Total Price:** $120
- **Shipping Status:** In Transit  
- **Estimated Delivery:** 2025-02-05  

---

# Task 4: Search Results Structured Output
**Scenario:** A chatbot provides search results for “best programming languages in 2025.” Structure the output.  
**Search Results:**  
1. **Title:** “Top 5 Programming Languages to Learn in 2025”  
   - **URL:** www.techblog.com/top5-2025  
   - **Snippet:** Discover the best programming languages in 2025, including Python, Rust, and Go.  

2. **Title:** “Why Python Will Still Dominate in 2025”  
   - **URL:** www.devnews.com/python-2025  
   - **Snippet:** Python continues to lead in AI, web development, and data science.  

3. **Title:** “Rust vs. Go: The Best Language for Systems Programming”  
   - **URL:** www.codeworld.com/rust-vs-go  
   - **Snippet:** A comparison of Rust and Go for high-performance applications.  

---

# Task 5: Multi-Intent Classification Output  
**Scenario:** A chatbot detects multiple possible intents from a user query. Structure the output.  
**User Query:** *"I want to check my account balance and transfer $100 to my friend."*  
**Predicted Intents (with confidence scores):**  
- **Intent 1:** Account Balance Inquiry (0.92)  
- **Intent 2:** Fund Transfer (0.89)  