import random
#RELEASE = 0 # (R, "reward" in literature) when both players collude
#TREAT = 100 # (T, "temptation" in literature) when you betray your partner
#SEVERE_PUNISHMENT = -500 # (S, "sucker" in literature) when your partner betrays you
#PUNISHMENT = -250 # (P) when both players betray each other 
team_name = 'Tiresias'
strategy_name = 'Predict'
strategy_description = '--Classified--'
#if i think the other player will betray, betray, if collude, choose random betwen c and b  
def move(my_history, their_history, my_score, their_score):
    options=('b','c')
    if 'c' in their_history:
        if 'b' in their_history:
            if their_history[-1]=='b' and their_history[-2]=='b':
                return 'b'
            if their_history[-1]=='b' and their_history[-2]=='c':
                if len(their_history)>=3:
                    if their_history[-3]=='c':
                        return 'b'
                    else:
                        choice=random.choice(options)
                        return choice
                else:
                    choice=random.choice(options)
                    return choice
            if their_history[-1]=='c' and their_history[-2]=='b':
                return 'b'
            if their_history[-1]=='c' and their_history[-2]=='c':
                choice=random.choice(options)
                return choice
            else:
                return 'b'#logically doesn't need to be here but still
        else:
            return 'c'  
    else:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'    
