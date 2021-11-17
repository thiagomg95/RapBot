import tensorflow as tf
import json
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# TODO: Mudar o modelo em template-tf.py para prever se uma frase é provável de ser uma lyric de rap ou não
#  (involve fazer o programa escanear alguma datbase de lyrics de rap pra treinar, precisamos encontrar uma)

# TODO: Fazer o gerador de texto

# TODO: Utilizar o modelo para determinar se a lyric gerada tem uma proabilidade alta de ser de rap.
#  Se o score for > X, aceitar

# TODO: Teste...
