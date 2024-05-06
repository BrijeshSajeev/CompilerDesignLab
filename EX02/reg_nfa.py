
def regex_to_nfa(regex):

  nfa = {'states': [], 
         'transitions': [],
         'start': 0,
         'accepting': []}
  
  state = 0
  i=0
  while(i < len(regex)):
    char = regex[i]
    if(len(regex) > i+1):
      charnext = regex[i+1]
    else:
      charnext = 'ε'
    
    if char.isalpha():
      
      if charnext == '*':
        nfa['states'].append(state)
        nfa['states'].append(state+1)
        nfa['states'].append(state+2)
        nfa['states'].append(state+3)

        nfa['transitions'].append((state, 'ε', state+1))
        nfa['transitions'].append((state, 'ε', state+3))
        nfa['transitions'].append((state+1, char, state+2))
        nfa['transitions'].append((state+2, 'ε', state+1))
        state += 3
      
      if charnext == '|':
        nfa['states'].append(state)
        charafter=regex[i+2]
        nfa['states'].append(state+1)
        nfa['states'].append(state+2)
        nfa['states'].append(state+3)
        nfa['states'].append(state+4)
        nfa['states'].append(state+5)
        nfa['transitions'].append((state, 'ε', state+1))
        nfa['transitions'].append((state, 'ε', state+3))
        nfa['transitions'].append((state+1, char, state+2))
        nfa['transitions'].append((state+3, charafter, state+4))
        nfa['transitions'].append((state+2, 'ε', state+5))
        nfa['transitions'].append((state+4, 'ε', state+5))
        state += 5
    i+=1
  nfa['accepting'].append(state)
  return nfa


regex = "a * b * c | d"

nfa = regex_to_nfa(regex.split())
print(regex.split(' '))
print(nfa)
