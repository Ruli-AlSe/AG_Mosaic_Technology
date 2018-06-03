import datetime
import random
import cv2



random.seed()
startTime = datetime.datetime.now()

geneSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
target = 'Hello World'

# def generate_parent(length):
# 	genes = []
# 	while len(genes) < length:
# 		sampleSize = min(length - len(genes), len(geneSet))
# 		genes.extend(random.sample(geneSet, sampleSize))
# 		print(str(sampleSize) + '-------------------------------\n')
# 		return ''.join(genes)

def create_image():
	pass
	pt_totalY, pt_totalX = image_gray.shape
	pt_x = 0
	pt_y = 0
	img = image_gray[pt_y:pt_totalY, pt_x:pt_totalX]
	while pt_x < pt_totalX:
		pt_y = 0
		while pt_y < pt_totalY:
			img.itemset((pt_y, pt_x), random.randint(0, 255))
			pt_y += 1
		pt_x += 1
	return img
#Generar poblacion
def generate_population(length):
	gen = []
	pt_totalY, pt_totalX = image_gray.shape
	pt_initX = random.randint(0, (pt_totalX - length))
	pt_finalY = random.randint(0, (pt_totalY - length)) + length
	pt_finalX = pt_initX + length
	pt_initY = pt_finalY - length
	genes = image_gray[pt_initY:pt_finalY, pt_initX:pt_finalX]
	return genes

def get_fitness(guess):
	return sum(1 for expected, actual in zip(target, guess) if expected == actual)

def mutate(parent):
	index = random.randrange(0,len(parent))
	childGenes = list(parent)
	newGene, alternate = random.sample(geneSet, 2)
	childGenes[index] = alternate if newGene == childGenes[index] else newGene
	#print('-------------------------------------\n' + newGene + alternate + ' ' + str(index) + ' ' + str(childGenes))
	return ''.join(childGenes)

def display(guess):
	timeDiff = datetime.datetime.now() - startTime
	fitness = get_fitness(guess)
	print('{}\t{}\t{}'.format(guess, fitness, timeDiff))


name_original = 'dog.png'
name_gray = 'lena_gray.png'
image_original = cv2.imread(name_original)


#Convertir imagenes de color a escala de grises-------------------------------------
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
image_new = create_image()

#Extraer poblacion
population = generate_population(50)


#Mostrar imagenes-------------------------------------------------------------------
cv2.imshow('imagen gris', image_gray)
cv2.imshow('imagen nueva', image_new)
cv2.waitKey(0)





# bestParent = generate_parent(len(target))
# bestFitness = get_fitness(bestParent)
# display(bestParent)

# while True:
# 	child = mutate(bestParent)
# 	childFitness = get_fitness(child)
# 	if bestFitness >= childFitness:
# 		continue
# 	display(child)
# 	if childFitness >= len(bestParent):
# 		break
# 	bestFitness = childFitness
# 	bestParent = child