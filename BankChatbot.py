from Bank import bankAccount

account_number_input = int(input("Si quiere acceder a su cuenta corriente pulse 1, si quiere acceder a su cuenta de ahorro pulse 2, si quiere salir del chatbot pulse cualquier otro número. "))

if account_number_input == 1:
    account_number == checking_account
elif account_number_input == 2:
    account_number == savings_account
else:
    print("Hasta la próxima")

account == bankAccount(account_number)
print(f"Hay {account.get_balance()}€ en tu cuenta")

funds = int(input("Cuánto dinero quiere añadir a su cuenta? "))
funds1 = int(input("Cuánto dinero quiere retirar de su cuenta? "))
account.add_funds(funds)
account.retire_funds(funds1)

print(f"Ahora hay {account.get_balance()}€ en tu cuenta")