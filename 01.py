#!/bin/env python


import keras as kr
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Esto muestra solo errores fatales

print("==> GPUs disponibles:", tf.config.list_physical_devices('GPU'))
