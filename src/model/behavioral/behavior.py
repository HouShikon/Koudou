from src.model.behavioral.activity.action_move import ActionMove

class Behavior:
	def __init__(self,name):
		self.name = name
		self.activities = []

	def add_activity(self,activity):
		self.activities.append(activity)

	def step(self,kd_sim,kd_map,ts,step_length,rng,agent):
		move_action_pool = []
		for act in self.activities:
			if (act.check_conditions(agent) == True):
				actions = act.generate_actions(agent,kd_map,rng)
				agent.actions.extend(actions)
				for action in actions:
					if action.__class__ is ActionMove:
						move_action_pool.append(action)
				break
		return move_action_pool


	def __str__(self):
		tempstring = "[Behavior]\n"
		tempstring += f"   Name = {self.name}"

		return tempstring