## Ԥ�� 20 ���� 70 ������ڲ�ʿ�ٽ������ݼ۸����λ��

from keras.datasets import boston_housing
from keras import models
from keras import layers
import numpy as np

### ��ȡ���ݼ�
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

### ���ݱ�׼��
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

### ����ģ��
def build_model():
    # Because we will need to instantiate
    # the same model multiple times,
    # we use a function to construct it.
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model

### ѵ������ģ�Ͳ��ڲ��Լ��ϲ���
model = build_model()
model.fit(train_data, train_targets, epochs=80, batch_size=16, verbose=0)
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
print(test_mse_score)

