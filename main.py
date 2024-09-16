#Lucas Brinks
#9/16/24
#Mad-Lib

verb = input('Enter a verb: ')
verb2 = input('Enter a verb: ')

verb = verb.lower()

noun = input('Enter a noun: ')
noun2 = input('Enter a noun: ')
noun3 = input('Enter a noun: ')
noun4 = input('Enter a noun: ')

noun = noun.upper()

adj = input('Enter an adjective: ')
adj2 = input('Enter an adjective: ')
adj3 = input('Enter an adjective: ')
adj4 = input('Enter an adjective: ')

madlibs = 'I was ' + verb + ' down the ' + noun + ' When out the conner of my eye, i saw a ' + adj + '  little thing ' + verb2 +  ' me. She said, I\'ve never seen a ' + noun2 + ' who looked so all' + adj2 + '  Uh, could you use a little company? If you pay the right price your ' + noun3 + ' will be nice and you can go and send me on my way. ' + noun4 + ' said, You\'re such a ' + adj3 + adj4 + ' thing, why\'d you do this to yourself?'

print(madlibs)