#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Goal:

	#instantiation with all necessary data
	def __init__(self, scorer, time, team, home, ownTeamScore, oppTeamScore, r):
		self.scorer = scorer
		self.time = time
		self.team = team
		self.home = home
		self.ownTeamScore = ownTeamScore
		self.oppTeamScore = oppTeamScore
		self.round = r
