#Pamela Ramírez González #Código: 201822262
#Manuel Gallegos Bustamante #Código: 201719942
#Análisis y procesamiento de imágenes: Proyecto3 Entrega1
##Se importan librerías que se utilizarán para el desarrollo del laboratorio
import os
import numpy as np
from skimage import io
from skimage import color
from skimage import img_as_float
from data_mp4.functions import JointColorHistogram, CatColorHistogram

def calculate_descriptors(data, parameters):
    if parameters['space'] != 'RGB':
        data = list(map(parameters['transform_color_function'], data))
    bins = [parameters['bins']]*len(data)
    histograms = list(map(parameters['histogram_function'], data, bins))
    descriptor_matrix = np.array(histograms) 
    # TODO Verificar tamaño de descriptor_matrix a # imágenes x dimensión del descriptor
    return descriptor_matrix
  
def train(parameters, action):
    data_train = os.path.join('data_mp4', 'scene_dataset', 'train', '*.jpg')
    images_train = list(map(io.imread, glob.glob(data_train)))
    if action == 'save':
        descriptors = calculate_descriptors(images_train, parameters)
        # TODO Guardar matriz de descriptores con el nombre parameters['train_descriptor_name']
        
    else:
        # Esta condición solo la tendrán que utilizar para la tercera entrega.
        # TODO Cargar matrices de parameters['train_descriptor_name']
    
    # TODO Definir una semilla y utilice la misma para todos los experimentos de la entrega.
    # TODO Inicializar y entrenar el modelo con los descriptores.
    # TODO Guardar modelo con el nombre del experimento: parameters['name_model']

def validate(parameters, action):
    data_val = os.path.join('data_mp4', 'scene_dataset', 'val', '*.jpg')
    images_val = list(map(io.imread, glob.glob(data_val)))
    if action == 'load':
        # Esta condición solo la tendrán que utilizar para la tercera entrega.
        # TODO Cargar matrices de parameters['val_descriptor_name']
    else:
        descriptors = calculate_descriptors(images_val, parameters)
        if action == 'save':
            # TODO Guardar matriz de descriptores con el nombre parameters['val_descriptor_name']
        
    # TODO Cargar el modelo de parameters['name_model']
    # TODO Obtener las predicciones para los descriptores de las imágenes de validación
    # TODO Obtener las métricas de evaluación

    return conf_mat, precision, recall, f_score

def main(parameters, perform_train, action):
    if perform_train:
        train(parameters, action = action)
    conf_mat, precision, recall, f_score = validate(parameters, action = action)
    #TODO Imprimir de manera organizada el resumen del experimento.
    # Incluyan los parámetros que usaron y las métricas de validación.

if __name__ == '__main__':
    """
    Por: Isabela Hernández y Natalia Valderrama
    Este código establece los parámetros de experimentación. Permite extraer
    los descriptores de las imágenes, entrenar un modelo de clasificación con estos
    y validar su desempeño.
    Nota: Este código fue diseñado para los estudiantes de IBIO-3470 2021-10.
    Rogamos no hacer uso de este código por fuera del curso y de este semestre.
    ----------NO OPEN ACCESS!!!!!!!------------
    """
    # TODO Establecer los valores de los parámetros con los que van a experimentar.
    # Nota: Tengan en cuenta que estos parámetros cambiarán según los descriptores
    # y clasificadores a utilizar.
    parameters= {'histogram_function': JointColorHistogram, 
             'space': 'HSV', 'transform_color_function': color.rgb2hsv, # Esto es solo un ejemplo.
             'bins': numero_bins, 'k': numero_cluster,
             'name_model': '', # No olviden establecer la extensión con la que guardarán sus archivos. 
             'train_descriptor_name': '', # No olviden asignar un nombre que haga referencia a sus experimentos y que corresponden a las imágenes de entrenamiento.
             'val_descriptor_name': ''} # No olviden asignar un nombre que haga referencia a sus experimentos y que corresponden a las imágenes de validación. 

    perform_train = True # Cambiar parámetro a False al momento de hacer la entrega
    action = 'save' # Cambiar a None al momento de hacer la entrega 
    main(parameters=parameters, perform_train=perform_train, action=action)
