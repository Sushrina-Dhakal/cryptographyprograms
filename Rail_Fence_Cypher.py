name = "SUSHRINADHAKAL"
rails = 3

def encrypt(name,rails):
	grid = [[" "for i in range(len(name))]for j in range(rails)]

	row = 0
	flag = 0
	for i in range(len(name)):
		grid[row][i] = name[i]
		if row==0:
			flag = 0;
		elif row == rails-1:
			flag = 1

		if flag==0:
			row+=1
		else:
			row = row - 1; 

	print("Rail grid:")
	for i in range(rails):
		print("".join(grid[i]))
	print()

	encrypted = ""
	for i in range(rails):
		for j in range(len(name)):
			if grid[i][j]!=' ':
				encrypted+=grid[i][j]

	return encrypted


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
     
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         
       	
        if dir_down:
            row += 1
        else:
            row -= 1
             
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

print("Original Text: "+name)
cipher = encrypt(name,rails)
plain = decrypt(cipher,rails)
print("After encryption, cipher text is: "+cipher)
print("After decryption, plain text is: "+plain)