'''
Created by the GiraffeTools Tensorflow generator.
Warning, here be dragons.

'''
from keras.layers import Conv2D
from keras.layers import Activation
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dense

# Model
def NeuralNet(shape):
    model = Sequential()

    model.add(Conv2D(
      32,  # filters
      (3, 3),  # kernel_size,
      strides=(1, 1),
      padding='valid',
      dilation_rate=(1, 1),
      use_bias=True,
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros'
    ))

    model.add(Activation(
      'relu',  # activation
    ))

    model.add(Conv2D(
      32,  # filters
      (3, 3),  # kernel_size,
      strides=(1, 1),
      padding='valid',
      dilation_rate=(1, 1),
      use_bias=True,
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros'
    ))

    model.add(Activation(
      'relu',  # activation
    ))

    model.add(MaxPooling2D(
      pool_size=(2, 2),
      padding='valid'
    ))

    model.add(Dropout(
      0.25,  # rate
    ))

    model.add(Conv2D(
      64,  # filters
      (3, 3),  # kernel_size,
      strides=(1, 1),
      padding='valid',
      dilation_rate=(1, 1),
      use_bias=True,
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros'
    ))

    model.add(Activation(
      'relu',  # activation
    ))

    model.add(Conv2D(
      64,  # filters
      (3, 3),  # kernel_size,
      strides=(1, 1),
      padding='valid',
      dilation_rate=(1, 1),
      use_bias=True,
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros'
    ))

    model.add(Activation(
      'relu',  # activation
    ))

    model.add(MaxPooling2D(
      pool_size=(2, 2),
      padding='valid'
    ))

    model.add(Dropout(
      0.25,  # rate
    ))

    model.add(Flatten(

    ))

    model.add(Dense(
      512,  # units,
      use_bias=True,
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros'
    ))

    model.add(Activation(
      'relu',  # activation
    ))

    model.add(Dropout(
      0.5,  # rate
    ))

    model.add(Dense(
      0.5,  # units,
      use_bias=True,
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros'
    ))

    model.add(Activation(
      'softmax',  # activation
    ))

    # Returning model
    return _model
