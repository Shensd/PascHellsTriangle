def init():
	triangle_len = int(input("lines : "))
	print("1 \n1 1\n1 2 1")
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
		print(last_line)
	input("")

if __name__ == "__main__":
	init()
