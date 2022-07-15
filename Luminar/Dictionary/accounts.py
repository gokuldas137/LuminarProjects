accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]

acc = {}

# q1 - print details of 1002
# for ac in accounts:
#     if ac["acno"]==1002:
#         transactions=ac.pop("transactions")  #remove transaction key
#         print(ac)


# ac_details=[ac for ac in accounts if ac["acno"]==1002]
# print(ac_details)


# q2- print savings type account details
# savings=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
#         #return acno only
# print(savings)


# q3 - sort accounts based balance order by descending
# accounts.sort(reverse=True,key=lambda i:i["balance"])
# print(accounts)         #list aanu...so accounts.sort
# # or
# print(sorted(accounts,reverse=True,key=lambda i:i["balance"]))


# q4 - print all transactions using phone pay
# alltrans=[ac["transactions"] for ac in accounts ]
# phonepay=[trans for tlist in alltrans for trans in tlist if trans["method"]=="phone-pay"]
# print(phonepay)


# q5 - print all transactions where transaction amount > 500
# greater =[trans for tlist in alltrans for trans in tlist if trans["amount"]>500]
# print(greater)


# phonepay=[ac for ac in accounts if ac["method"]=="phone-pay"]
# print(phonepay)


# q6 - print transactions coming to acc-1002
# credited_t=[trans for tlist in alltrans for trans in tlist if trans["to"]==1002]
# print(credited_t)

# q7 - print each payment method sum (aggregate transactions based on payment)

paymethodsum={}
alltrans=[ac["transactions"] for ac in accounts ]
transactions=[t for tlsist in alltrans for t in tlsist]
print(transactions)

for trans in transactions:

    pay_method=trans["method"]
    amount=trans["amount"]
    if pay_method in paymethodsum:
        paymethodsum[pay_method]+=amount
    else:
        paymethodsum[pay_method]=amount
#
print(paymethodsum)

print(max(paymethodsum.items(),key=lambda it:it[1]))