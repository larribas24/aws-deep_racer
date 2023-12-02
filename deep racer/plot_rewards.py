import matplotlib.pyplot as plt

## Grafica rewards obtenidos para 
def fun(s, h):
    params = dict()
    params["speed"] = s
    speed = max(1, params["speed"]) + 1
    track_direction = 0
    heading = h
    reward = speed**2

    direction_diff = abs(track_direction - heading)

    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    if direction_diff >30:
        reward = 0.001
    else:
        try:
            reward = reward/abs(direction_diff)
        except:
            pass
    return reward


rews = []
speed_values = [0.5, 1, 1.5, 2, 2.5, 3.0, 3.5, 4]

h = 0

for i in speed_values:
    rews.append(fun(i, h))

plt.plot(rews, marker="o")
plt.show()
print(rews)
