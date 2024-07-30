#show recomendation randomizer

import random

#create a list for each genre and assign 5 shows for each list
action = ['Arcane','Daredevil','Dragon Ball Z','Game of Thrones','Breaking Bad']
comedy = ['The Office','The Bear','Abbott Elementary','Succession','Its Always Sunny in Philadelphia']
cozy = ['Avatar: The Last Airbender','X-Men 97','One Piece','Midnight Diner','Gravity Falls']
horror = ['The Haunting of Hill House','American Horror Story','The Last of Us','Stranger Things','The Walking Dead']

name = input('What is your name?\n') #ask user for name
print('Hello', name) 
genre = input('What genre are you in the mood for? Choose from the following: action, comedy, cozy, or horror.\n') #ask for genre

print('Hmmm, let me think...\n')

#if/elif/else loop that takes genre input from user and recommends random show based on selected genre
if genre == 'action':

    print('Ahh, so youre an adrenaline junkie? This should get the blood pumping: ', random.choice(action))
   
elif genre == 'comedy':

    print('In the mood for some hearty laughs? Try: ', random.choice(comedy)) 

elif genre == 'cozy':

    print('Want to cuddle up under a blanket all day? In that case, watch: ', random.choice(cozy))

elif genre == 'horror':

    print('Dont like going to sleep at night, huh? In that case, I recommend: ', random.choice(horror))

else:
    print('This is not a valid genre!')
