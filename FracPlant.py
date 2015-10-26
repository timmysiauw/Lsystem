import matplotlib.pyplot as plt
import math
import copy

R = {"X":"F-[[X]+X]+F[+FX]-X", "F":"FF"}

def expand(S, R, N):
	# expands the string, S, according to the L system defined by the rules, R, for N iterations. 

	if N == 0:
		return S

	T = ""

	for i in range(len(S)):
		if S[i] in R:
			T += expand(R[S[i]], R, N-1)
		else:
			T += S[i]

	return T


def render(S, angle, angle0):
	# renders L-system-generated string, S, using turn-angle, angle, and starting angle, angle0

	states = [];

	state = {"x": 0, "y": 0, "angle": angle0};

	for i in range(len(S)):

		if S[i] == "+":
			state["angle"] = (state["angle"] + angle) % 360
		elif S[i] == "-":
			state["angle"] = (state["angle"] - angle) % 360
		elif S[i] == "[":
			states.append(copy.deepcopy(state))
		elif S[i] == "]":
			state = states.pop()
		elif S[i] == "F":
			x = state["x"] + math.cos(math.radians(state["angle"]))
			y = state["y"] + math.sin(math.radians(state["angle"]))

			plt.plot([state["x"], x], [state["y"], y], "g")

			state["x"] = x
			state["y"] = y

	plt.gca().set_aspect('equal', adjustable='box')
	plt.show()


render(expand("X", R, 6), -25, 60)


