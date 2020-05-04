import matplotlib.pyplot as plt

hours = [3,14,5,2]
activities = ["ratta","programming","rest/sleep","work"]
explode=[0.2,0,0,0]
plt.pie(hours , labels = activities, shadow =True,explode = explode)
plt.title("my day timing(Akash Rana)")
plt.show()