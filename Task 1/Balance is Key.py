request_spending={
    'Mahek':{
        "balance":3000.00,
        'transaction':[
            {"amount":-9000,"category":"Creatives"}
            ,{"amount":7000,'category':"sponsor"}
            ,{"amount":-2000,"category":"Prize-Money"}
        ]
    },
'Arham':{
    "balance":5000.00,
    "transaction":[
        {"amount":8000.00,"category":"Stalls"},
        {"amount":7500.00,"category":"Seminars"},
    ]
},
'Unnati':{
    'balance':3500.00,
    'transaction':[{
        "amount":-5000.00,"category":"Attraction"},
        {"amount":25000.00,"category":"Promo"},
        {"amount":-900.00,"category":"Lighting"},
        {"amount":-3000.00,"category":"Games"},
    ]
},
"Gaurang":{
    "balance":2000.00,
    'transaction':[
        {"amount":-1500,"category":"Website"},
        {"amount":-1000,"category":"C2C"},
        {"amount":-500,'category':"Posters"}
    ]
}
}

def total_spending(request_spending,account_id:str,category:str):
    transactions=request_spending[account_id]["transaction"]
    total=sum(transaction['amount'] for transaction in transactions if transaction['category'] == category and transaction['amount'] < 0)
    return abs(total)
def account_balance(request_spending,account_id:str):
    initial_balance=request_spending[account_id]["balance"]
    transaction=request_spending[account_id]["transaction"]
    for transactions in transaction:
        initial_balance+=transactions["amount"]
    return initial_balance
def money_owed(request_spending,account_id:str):
    balance=account_balance(request_spending,account_id)
    return max(0,-balance)

total_spending(request_spending,'Mahek',"Creatives")
account_balance(request_spending,'Mahek')
money_owed(request_spending,'Mahek')