
import matplotlib.pyplot as plt


labelList = ['200', '400', '600', '800']

dataGen1 = [1468.457 + 1274.572, 13278.138 + 11654.947, 1476.779 + 1281.413]
dataGen2 = [1472.498 + 1275.661, 65006.596 + 39315.475, 157719.752 + 76389.328]
dataGen3 = [14233.903 + 11707.096, 64824.453 + 39088.649, 158153.551 + 731937.832]
dataGen4 = [14067.503 + 11652.795, 62920.881 + 39470.871, 160821.372 + 789839.637]



x = range(len(dataGen1))


rects1 = plt.bar(x, height = dataGen1, width=0.4, alpha=0.8, color='red', label="一部门")
rects2 = plt.bar(x, left=[i + 0.4 for i in x], height=dataGen2, width=0.4, color='green', label="二部门")
rects3 = plt.bar(x, left=[i + 0.8 for i in x], height=dataGen3, width=0.4, color='black', label="二部门")
rects4 = plt.bar(x, left=[i + 1.6 for i in x], height=dataGen4, width=0.4, color='blue', label="二部门")



plt.ylabel("时间")
plt.xticks([index + 0.2 for index in x], labelList)
plt.xlabel("problem size")

for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
for rect in rects3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
    for rect in rects4:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
plt.show()



