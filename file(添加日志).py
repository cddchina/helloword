#为首行字符是{，并且后面是任意个数的 空格或Tab,添加一行日志
#!/usr/bin/env python
#coding=utf-8
  
import os
import re
import sys
  
def scan_files(directory,prefix=None,postfix=None):
	files_list=[]
    
	for root, sub_dirs, files in os.walk(directory):
		for special_file in files:
			if postfix:
				if special_file.endswith(postfix):
					files_list.append(os.path.join(root,special_file))
			elif prefix:
				if special_file.startswith(prefix):
					files_list.append(os.path.join(root,special_file))
			else:
				files_list.append(os.path.join(root,special_file))
       
	return files_list

  #获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
	path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
	if os.path.isdir(path):
		return path
	elif os.path.isfile(path):
		return os.path.dirname(path)
#打印结果
print cur_file_dir()

def main():
    #dir = raw_input('please input the path:')
	dir = cur_file_dir()
	fileList = scan_files(dir, None, ".cpp")

	#for i in range(fileList.__len__()):
	#	print fileList[i]

	for fileObj in fileList:
		f = open(fileObj,'r+')
		all_the_lines=f.readlines()
		f.seek(0)
		f.truncate()
		for line in all_the_lines:
			replace_reg = re.compile(r'^{[\t|\s]*$')
			f.write(replace_reg.sub('{ \r\n	writeLogs;\r\n',line))    
		f.close()
		print fileObj

if __name__ == '__main__':
	main()
