import datetime
import random
from random import uniform
import cv2
import matplotlib.pyplot as plt
import numpy as np
#from skimage import io



random.seed()
startTime = datetime.datetime.now()

#Crea imagen aleatoria a escala de grises--------------------------------------
def create_image(shape):
	img = np.random.randint(0, 256 ,(shape[0],shape[1]))
	return img


#Generar cuadrados aleatorios de poblacion-------------------------------------
def generate_population(length, img_original, img_new):
    pt_totalY, pt_totalX = img_original.shape
    pt_initX = random.randint(0, (pt_totalX - length))	
    pt_initY = random.randint(0, (pt_totalY - length))
    pt_finalX = pt_initX + length
    pt_finalY = pt_initY + length
    genes = img_original[pt_initY:pt_finalY, pt_initX:pt_finalX]
    genes2 = img_new[pt_initY:pt_finalY, pt_initX:pt_finalX]
    return genes, genes2, (pt_initY, pt_finalY), (pt_initX, pt_finalX)

def crossover(CF, h, w, pop_original, pop_new):
    for i in range(h):
        for j in range(w):
            #Se obtiene un número aleatorio que será comparado con nuestra PC
            numRand = uniform(0, 1)
            if numRand > CF:
                #Se promedia el valor del nuevo pixel con el de la imagen leída
                prom = (pop_original[i, j] + pop_new[i, j]) / 2
                pop_new[i, j] = prom
            else:
                #si no hay cruza entonces los pixeles no se modifican
                pop_new[i, j] = pop_new[i, j]
    return pop_new

def mutate(parent):
	index = random.randrange(0,len(parent))
	childGenes = list(parent)
	newGene, alternate = random.sample(geneSet, 2)
	childGenes[index] = alternate if newGene == childGenes[index] else newGene
	#print('-------------------------------------\n' + newGene + alternate + ' ' + str(index) + ' ' + str(childGenes))
	return ''.join(childGenes)
    
#Muestra imagenes--------------------------------------------------------------
def display():
    fig = plt.figure(figsize = (8,8))
    fig.add_subplot(1, 2, 1)
    plt.imshow(image_gray, cmap = 'gray')
    fig.add_subplot(1, 2, 2)
    plt.imshow(image_new, cmap = 'gray')
    plt.show()
    
    figp = plt.figure(figsize = (3,3))
    figp.add_subplot(1, 2, 1)
    plt.imshow(population_original, cmap = 'gray')
    figp.add_subplot(1, 2, 2)
    plt.imshow(population_new, cmap = 'gray')
    plt.show()




#************************EJECUCION PRINCIPAL DEL CODIGO************************
#Inicialización de variables---------------------------------------------------
name_original = 'dog.png'
name_gray = 'lena_gray.png'
crossover_factor = 0.2
mutate_factor = 0.1
image_original = cv2.imread(name_original)


#Convierte imagenes de color a escala de grises--------------------------------
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
print(image_gray.shape)
image_new = create_image(image_gray.shape)

#Extraer poblaciones iniciales-------------------------------------------------
population_original, population_new, Ypoints, Xpoints = generate_population(50, image_gray, image_new)
print('total: ' + str(Xpoints[1] - Xpoints[0]))

population_new = crossover(crossover_factor, (Ypoints[1] - Ypoints[0]), (Xpoints[1] - Xpoints[0]), population_original, population_new)

display()













#
#pt_totalY, pt_totalX = img.shape
#	pt_initX = random.randint(0, (pt_totalX - length))
#	pt_finalY = random.randint(0, (pt_totalY - length)) + length
#	pt_finalX = pt_initX + length
#	pt_initY = pt_finalY - length
#	genes = img[pt_initY:pt_finalY, pt_initX:pt_finalX]
#	return genes, 1, 2
