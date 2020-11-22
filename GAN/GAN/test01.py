import copy
import numpy as np
import tensorflow as tf
from RSBF import attitute
from tensorflow import keras
from tensorflow.keras import layers
from flieToLst import fileToList
from readTensor import tensorTransToArr, uniqueList


'''
    在numpy数组上对数据进行归一化
'''
def Normaliztion():
    normaliztionLst = []
    trainData = fullPos()
    for ele in trainData:
        tmpList = []
        for elem in ele[0]:
            tmpList.append((elem - 60)/ 60)
        normaliztionLst.append(copy.deepcopy(tmpList))
    return normaliztionLst

'''
    将真值表中空余位置填充0
'''
def fullPos():
    data = fileToList("unique240.txt")
    tmpdata = data
    for i in range(len(data)):
        for j in range(1, 61):
            if j not in data[i][0]:
                tmpdata[i][0].insert(j - 1, 0)
    return tmpdata

'''
    将numpy数据转化为tensor张量
'''
def transToTensor(dataMatrix):
    dataMatrix = np.array(dataMatrix)
    dataMatrix = dataMatrix.reshape(dataMatrix.shape[0], 60, 1).astype('float32')
    data = tf.convert_to_tensor(dataMatrix)
    dataset = tf.data.Dataset.from_tensor_slices(data)
    dataset = dataset.shuffle(256).batch(256)
    return dataset

def generator_model():  # 用60个随机数（噪音）生成数据集
    model = keras.Sequential()
    model.add(layers.Dense(256, input_shape=(60,), use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(512, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(60 * 1, use_bias=False, activation='tanh'))
    model.add(layers.BatchNormalization())

    model.add(layers.Reshape((60, 1, 1)))

    return model

def discriminator_model():  # 识别输入的真值表
    model = keras.Sequential()
    model.add(layers.Flatten())

    model.add(layers.Dense(60, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(256, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(1))

    return model


cross_entropy = keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_out, fake_out):
    real_loss = cross_entropy(tf.ones_like(real_out), real_out)
    fake_loss = cross_entropy(tf.zeros_like(fake_out), fake_out)
    return real_loss + fake_loss


def generator_loss(fake_out):
    return cross_entropy(tf.ones_like(fake_out), fake_out)



generator_opt = keras.optimizers.Adam(1e-4)
discriminator_opt = keras.optimizers.Adam(1e-4)
#
generator = generator_model()
discriminator = discriminator_model()

noise_dim = 60  # 即用100个随机数生成图片


def train_step(images):
    noise = tf.random.normal([256, noise_dim])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        real_out = discriminator(images, training=True)
        gen_image = generator(noise, training=True)
        fake_out = discriminator(gen_image, training=True)

        gen_loss = generator_loss(fake_out)
        disc_loss = discriminator_loss(real_out, fake_out)
    gradient_gen = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradient_disc = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    generator_opt.apply_gradients(zip(gradient_gen, generator.trainable_variables))
    discriminator_opt.apply_gradients(zip(gradient_disc, discriminator.trainable_variables))

def unNormaliztion(matrix):
    pass

def judgeTruth(matrix):
    for ele in matrix:
        tmp = tf.reshape(((tf.cast(((ele * 60) + 60), tf.int32)) % 60), [60])
        res = tensorTransToArr(tmp)
        res = uniqueList(res)
        attitute(9, res)
        # with open("res.txt", mode = "a+", encoding="utf-8") as f:
        #     f.write(str(tmp) + "\n")
    #     print(tmp)
    # print("*************************")

EPOCHS = 200000  # 训练200次
num_exp_to_generate = 4  # 生成4个真值表
seed = tf.random.normal([num_exp_to_generate, noise_dim])  # 16组随机数组，每组含30个随机数，用来生成16个真值表。

def generateRes(gen_model, test_noise):
    pre_truth = gen_model(test_noise, training=False)
    judgeTruth(pre_truth)

def train(dataset, epochs):
    count = 0
    for epoch in range(epochs):
        for image_batch in dataset:
            train_step(image_batch)
            count += 1
            if count % 100 == 0:
                print(count, " check")
        generateRes(generator, seed)


data = Normaliztion()
datasets = transToTensor(data)
train(datasets, EPOCHS)
