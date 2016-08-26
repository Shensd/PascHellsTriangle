pascal = ["1", "1 1", "1 2 1"]

def create_file(text):
	f = open('big.py', 'w')
	f.write(text)

def make_file():
	final_text = "if __name__ == '__main__':\n    lines = int(input('lines : '))\n    if lines == 1:\n        print('1')\n        input('')\n    elif lines == 2:\n        print('1')\n"
	final_text = final_text + "        print('1 1')\n        input('')\n    elif lines == 3:\n        print('1')\n        print('1 1')\n        print('1 2 1')\n        input('')\n"
	for i in range(4, len(pascal)):
		final_text = final_text + "    elif lines == {}:\n".format(i)
		for j in range(0, i):
			final_text = final_text + "        print('{}')\n".format(pascal[j])
		final_text = final_text + "        input('')\n"
	final_text = final_text + "    else:\n        print('To High.')\n        input('')"
	create_file(final_text)

def make_triangle():
	global pascal

	triangle_len = 100
	last_line = "1 2 1"

	for i in range(2, triangle_len):
		end        = "1"
		line_len   = len(last_line)
		last_split = last_line.split(" ")

		for j in range(0, len(last_split) - 1):
			if j == len(last_split) - 1:
				continue

			tmp = int(last_split[j]) + int(last_split[j+1])
			end = end + " " + str(tmp)

		last_line = end + " 1"
		pascal.append(end + " 1")
	make_file()


if __name__ == "__main__":
	make_triangle()
