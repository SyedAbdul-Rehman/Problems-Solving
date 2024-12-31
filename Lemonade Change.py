from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        transactions = []

        for bill in bills:
            if bill not in [5, 10, 20]:
                print(f"Invalid bill amount: {bill}")
                return False

            if bill == 5:
                five += 1
                transactions.append(f"Received $5, no change given. State: $5 bills: {five}, $10 bills: {ten}")
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                    transactions.append(f"Received $10, gave $5 as change. State: $5 bills: {five}, $10 bills: {ten}")
                else:
                    print("Cannot give change for $10 bill.")
                    return False
            elif bill == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                    transactions.append(f"Received $20, gave $10 and $5 as change. State: $5 bills: {five}, $10 bills: {ten}")
                elif five >= 3:
                    five -= 3
                    transactions.append(f"Received $20, gave three $5 bills as change. State: $5 bills: {five}, $10 bills: {ten}")
                else:
                    print("Cannot give change for $20 bill.")
                    return False

        print("All transactions successful.")
        for transaction in transactions:
            print(transaction)
        
        print(f"Final state: $5 bills: {five}, $10 bills: {ten}")
        return True

def main():
    user_input = input("Enter the bills separated by spaces (e.g., 5 10 5 20): ")
    bills = list(map(int, user_input.split()))
    solution = Solution()
    solution.lemonadeChange(bills)

if __name__ == "__main__":
    main()