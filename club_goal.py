from turtle import color
import matplotlib.pyplot as plt

player_name= ['Suarez', 'Ibrahimovic', 'Lewandowski','Deak', 'Eusebio', 'Muller', 'Puskas', 'Bican', 'Leo', 'Ronaldo']
player_goal = [436,492,509,547,473,556,512,676,691,700]

plt.plot(player_name,player_goal, color='blue')
plt.show()
