transactions = [
    {"customer_id": 101, "transaction_type": "deposit", "amount": 5000},
    {"customer_id": 102, "transaction_type": "withdrawal", "amount": 2000},
    {"customer_id": 101, "transaction_type": "withdrawal", "amount": 1000},
    {"customer_id": 103, "transaction_type": "deposit", "amount": 7000},
    {"customer_id": 102, "transaction_type": "deposit", "amount": 3000},
    {"customer_id": 101, "transaction_type": "deposit", "amount": 2000},
    {"customer_id": 103, "transaction_type": "withdrawal", "amount": 4000},
    {"customer_id": 102, "transaction_type": "withdrawal", "amount": 1500},
]

def calculate_balance(customer_id):
    balance = 0
    for transaction in transactions:
        if transaction["customer_id"] == customer_id:
            if transaction["transaction_type"] == "deposit":
                balance += transaction["amount"]
            elif transaction["transaction_type"] == "withdrawal":
                balance -= transaction["amount"]
    return balance

def customer_summary(transactions):
    summary = {}
    for transaction in transactions:
        customer_id = transaction["customer_id"]
        if customer_id not in summary:
            summary[customer_id] = {"total_deposit": 0, "total_withdrawal": 0, "balance": 0}
        if transaction["transaction_type"] == "deposit":
            summary[customer_id]["total_deposit"] += transaction["amount"]
            summary[customer_id]["balance"] += transaction["amount"]
        elif transaction["transaction_type"] == "withdrawal":
            summary[customer_id]["total_withdrawal"] += transaction["amount"]
            summary[customer_id]["balance"] -= transaction["amount"]
    
    for customer_id, data in summary.items():
        print(f"ID Nasabah: {customer_id}")
        print(f"Total Deposit: {data['total_deposit']}")
        print(f"Total Withdrawal: {data['total_withdrawal']}")
        print(f"Saldo Akhir: {data['balance']}")
        print("------------------------------")

customer_summary(transactions)