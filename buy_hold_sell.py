def simulate(actions, prices):
    capital = 1.0
    position = 0.0
    values = []
    flag_sell = 0
    flag_buy = 0
    
    for action, price in zip(actions, prices):
        
        if action == 'buy' and flag_buy == 0:
            if capital > 0 and position == 0:
                shares = capital / price
                position += shares
                capital = 0.0
                flag_buy = 1
                flag_sell = 0                
            elif position < 0 and capital > 0:  
                
                cover_cost = abs(position) * price
                if capital >= cover_cost:
                    capital -= cover_cost
                    position = 0.0
                    
                    if capital > 0:
                        shares = capital / price
                        position += shares
                        capital = 0.0
                else:
                    
                    shares_covered = capital / price
                    position += shares_covered
                    capital = 0.0
                
                flag_buy = 1
                flag_sell = 0
                
        elif action == 'sell' and flag_sell == 0:
            if position > 0:
                capital += position * price
                position = 0.0
                flag_sell = 1
                flag_buy = 0
                print(f'sell_1: capital={capital}, position={position:.4f}')
                
            elif position <= 0:
                if capital > 0:
                    shares = capital / price
                    position -= shares
                    capital += shares * price
                    flag_sell = 1
                    flag_buy = 0
        
        elif action == 'hold':
            flag_buy = 0
            flag_sell = 0
            # print(f'hold: flags reset')
        
        if position > 0:  
            value = capital + (position * price)
        elif position < 0: 
            value = capital + (position * price) 
        else:  
            value = capital
            
        value = round(value, 2)
        values.append(value)

    
    return values



# actions1 = ['buy', 'hold', 'sell']
# prices1 = [100, 90, 80]
# result1 = simulate(actions1, prices1)
# print(f"Result: {result1}\n")
# print("Expected: [1, 0.9, 0.9]")

# actions2 = ['buy', 'sell', 'hold']
# prices2 = [100, 90, 80]
# result2 = simulate(actions2, prices2)
# print(f"Result: {result2}\n")
# print("Expected: [1, 0.9, 0.9]")

# actions3 = ['sell', 'sell', 'buy']
# prices3 = [100, 90, 90]
# result3 = simulate(actions3, prices3)
# print(f"Result: {result3}\n")
# print("Expected: [1, 1.1, 1.1]")

# actions4 = ['sell', 'sell', 'sell']
# prices4 = [100, 110, 110]
# result4 = simulate(actions4, prices4)
# print(f"Result: {result4}\n")
# print("Expected: [1, 0.9, 0.9]")

# actions5 = ['sell', 'hold', 'sell']
# prices5 = [100, 110, 110]
# result5 = simulate(actions5, prices5)
# print(f"Result: {result5}\n")
# print("Expected: [1, 0.9, 0.9]")

# actions6 = ['sell', 'hold', 'hold']
# prices6 = [100, 110, 110]
# result6 = simulate(actions6, prices6)
# print(f"Result 6: {result6}")
# print("Expected: [1, 0.9, 0.9]")

actions7 = ['sell', 'sell', 'sell']
prices7 = [100, 90, 80]
result7 = simulate(actions7, prices7)
print(f"Result 7: {result7}\n")
print("Expected: [1, 1.1, 1.2]")



