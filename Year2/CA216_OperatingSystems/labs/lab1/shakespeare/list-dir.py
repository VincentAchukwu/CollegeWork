from __future__ import print_function
import os,sys

path = "."
if len(sys.argv) == 2:
	path = sys.argv[1]

files = os.listdir(path)
for name in files:
	print(name)
	full_path = os.path.join(path, name)
	print(full_path)

	inode = os.stat(full_path)
	print(" " + str(inode.st_size))
	print(" " + str(inode.st_mode))
	print(" " + ("f" if (inode.st_mode & 0o100000) else "-" ))
	print(" " + ("d" if (inode.st_mode & 0o040000) else "-" ))
	if os.path.isdir(full_path):
		print(" dir")
	elif os.path.isfile(full_path):
		print(" file")
	print(" " + str(os.path.getsize(full_path)))

# from cmd import Cmd

# class MyPrompt(Cmd):
# 	def do_hello(self, args):
# 		# Says hello. Give name = will greet you
# 		if len(args) == 0:
# 			name = "Stranger"
# 		else:
# 			name = args
# 		print "Hello, %s" %name
# 	def do_quit(self,args):
# 		#Quits program
# 		print("Quitting")
# 		raise SystemExit
# if __name__ == '__main__':
# 	prompt = MyPrompt()
# 	prompt.prompt = ">"
# 	prompt.cmdloop("Starting prompt...")
