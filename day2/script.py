import numpy as np

class PasswordChecker:
	def __init__(self, path):

		try:

			with open(path, "r") as file:
				pwd_list = []
				for line in file.readlines():
					pwd_list.append(line.strip().split())
			
				self.pwd_list = pwd_list		# print(line.split()[2].count('m'))

		except FileNotFoundError:
			print(f'{path} does not exist')

	def get_wrong_pwd(self):
		correct_pwd_list = []

		for item in self.pwd_list:
			num_list = item[0].split('-')
			minimum = int(num_list[0])
			maximus = int(num_list[1])
			counter = item[2].count(item[1].replace(':',''))
			if minimum<=counter<=maximus :
				correct_pwd_list.append(item)
		return len(correct_pwd_list)

	def get_wrong_pwd_part_II(self):
		correct_pwd_list = []
		
		for item in self.pwd_list:
			num_list = item[0].strip().split('-')
			positiona = int(num_list[0])
			positionb = int(num_list[1])
			if item[2][positiona-1]!=item[2][positionb-1]:
				if item[1].replace(':','')==item[2][positiona-1] or item[1].replace(':','')==item[2][positionb-1]:
					correct_pwd_list.append(item)
		return len(correct_pwd_list)
		#	print(item[1].replace(':',''))
		# return correct_pwd_list


if __name__ == '__main__':
	


	path = './input.txt'



	results = PasswordChecker(path)
	print(results.get_wrong_pwd_part_II())