
from itertools import permutations
import numpy as np

class ExpenseReportFixer:
	def __init__(self, path):
		self.constant = 2020

		try:

			with open(path, "r") as file:
				
				report_entries = []
				for line in file.readlines():
					report_entries.append(int(line.strip()))
				self.report_entries = report_entries

		except FileNotFoundError : 
			print (f'{path} does not exist')
		self.permutations = permutations(list(self.report_entries),3)

	def fix_report(self, n=2):
		if n == 2:
			for entry in self.report_entries:
				test = self.constant - entry
				if test in self.report_entries :
					result = np.array([entry, test])
					break
		else:
			permus = list(permutations(self.report_entries,n))
			for permu in permus:
				test = sum(permu)

				if test == self.constant:
					result = np.array(permu)
					break
		return result.prod()

