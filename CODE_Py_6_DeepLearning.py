
### DEEP LEARNING ###
https://keras.io/
# Lots of good documentations here.

# REMEMBER:
# 1 - Scale the data!!!

# 0) PRE PROCESSING

# KERAS MAIN ARCHITECTURE: Create sequential empty object, then add layers.
# 1) REGRESSION KERAS
# 2) CLASSIFICATION KERAS
# 3) SAVING/LOADING MODEL FOR PREDICTIONS
# 4) SGD: Stochastic Gradient Descent w/Optimizer
# 5) VALIDATION SPLITTING
#		- Early Stopping		
# 6) CONVOLUTIONAL NETWORK - CNN
# 7) RECURRENT NETWORK - RNN

# Activations: 'relu','leakyRelu','linear','softmax','softplus','tanh','sigmoid'
# Optimizer: 'adam','sgd'
# Loss: 'mean_squared_error','mse','categorical crossentropy','binary cross entropy'
# Metrics : Needs to take (y_pred & y_true)

# Check here for the rest https://keras.io/

#####################################################
################# PRE PROCESSING







#####################################################

# 1) REGRESSION Build Architecture
import numpy as np
import keras
from keras.layers import Dense
from keras.models import Sequential

predictors = np.loadtxt('predictor_data.csv', delimiter = ',')
n_cols = predictors.shape[1]
model = Sequential()

model.add(Dense(100, activation='relu', input_shape = (n_cols,))) # input layer, first hidden layer has 100 nodes
model.add(Dense(100, activation='relu'))
model.add(Dense(1))

# Compile Model
model.compile(optimizer='adam', loss='mean_squared_error') #adam is like a smart optimizer rate


# Fit the Model
model.fit(predictors, target, 
	epochs = 50,
	shuffle = True,
	verbose = 2)

# I BUILT A LINEAR NETWORK FROM END TO END IN JUPYTER NOTEBOOKS > PROJECTS > LYNDA KERAS

#####################################################

# 2) CLASSIFICATION Build Architecture
import numpy as np
import keras
from keras.layers import Dense
from keras.models import Sequential

from keras.utils import to_categorical
data = pd.read_csv('basketball_data.csv')
predictors = data.drop(['shot_result'], axis = 1).as_matrix() # REMOVES the target column
target = to_categorical(data.shot_results)
model = Sequential()

model.add(Dense(100, activation='relu', input_shape = (n_cols, )))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(optimzer = 'sgd', loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.fit(predictors, target,
	epochs = 50,
	shuffle = True)
predictions = model.predict(pred_data)

#####################################################

# 3) SAVING MODEL FOR PREDICTIONS

from keras.models import load_model
model.save('model_file.h5') # .h5 is the convention to use for models
my_model = load_model('my_model.h5')
predictions = my_model.predict(data_to_predict_with)
probability_true = predictions[:, 1] # Saves where predictions are TRUE for classification

#####################################################

# 4) SGD: Stochastic Gradient Descent
# We're using multiple learning rates for optimization too!!!
import numpy as np
import keras
from keras.layers import Dense
from keras.models import Sequential

from keras.optimizers import SGD

def get_new_model(input_shape = input_shape):
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape = input_shape))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    return(model)
lr_to_test = [0.000001, 0.01, 1]
for lr in lr_to_test:
    model = get_new_model()
    my_optimizer = SGD(lr = lr)
    model.compile(optimzer = my_optimizer, loss = 'categorical_crossentropy')
    model.fit(predictors, target,
    	epochs = 50,
    	shuffle = True)

#####################################################

# 5) VALIDATION SPLITTING
model.compile(optimzer = adam, loss = 'categorical_crossentr', metrics = ['accuracy'])
model.fit(predictors, target, validation_split = 0.3, epochs = 20)

# EARLY STOPPING
from keras.callbacks import EarlyStopping

early_stopping_monitor = EarlyStopping(patience = 2) # patience means it will wait for 2 fails of lower loss score

model.fit(predictors, target, 
	validation_split = 0.3, 
	epochs = 20, 
	callbacks = [early_stopping_monitor])
# callbacks takes a list!
# Now we can set a high maximum epochs since we have early stopping
