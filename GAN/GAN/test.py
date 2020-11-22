import copy
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from flieToLst import fileToList

def fullPos():
    data = fileToList("unique240.txt")
    tmpdata = data
    for i in range(len(data)):
        for j in range(1, 61):
            if j not in data[i][0]:
                tmpdata[i][0].insert(j - 1, 0)
    return tmpdata



def Normaliztion():
    normaliztionLst = []
    trainData = fileToList("unique240.txt")
    for ele in trainData:
        tmpList = []
        for elem in ele[0]:
            tmpList.append((elem - 60)/ 60)
        normaliztionLst.append(copy.deepcopy(tmpList))
    return normaliztionLst



(train_images, train_labels), (_, _) = keras.datasets.mnist.load_data()
print(type(train_images))
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')

train_images = (train_images-127.5)/127.5

BATCH_SIZE = 256
BUFFER_SIZE = 60000
# print(type(train_images))
datasets = tf.data.Dataset.from_tensor_slices(train_images)
print(datasets, "++")

# 按顺序取出256个样本
datasets = datasets.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
print(datasets)
print(type(datasets))


def generator_model():  # 用100个随机数（噪音）生成数据集
    model = keras.Sequential()
    model.add(layers.Dense(256, input_shape=(100,), use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(512, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Dense(pow(2, 8) * 1, use_bias=False, activation='tanh'))
    model.add(layers.BatchNormalization())

    model.add(layers.Reshape((pow(2, 8), 1, 1)))

    return model


def discriminator_model():  # 识别输入的图片
    model = keras.Sequential()
    # model.add(layers.Flatten())

    model.add(layers.Dense(pow(2, 8), use_bias=False))
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

noise_dim = 100  # 即用100个随机数生成图片


def train_step(images):
    noise = tf.random.normal([BATCH_SIZE, noise_dim])

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

def generate_plot_image(gen_model, test_noise):
    pre_images = gen_model(test_noise, training=False)
    fig = plt.figure(figsize=(4, 4))
    for i in range(pre_images.shape[0]):
        plt.subplot(4, 4, i+1)
        plt.imshow((pre_images[i, :, :, 0] + 1)/2, cmap='gray')
        plt.axis('off')
    plt.show()

EPOCHS = 200  # 训练100次
num_exp_to_generate = 16  # 生成16张图片
seed = tf.random.normal([num_exp_to_generate, noise_dim])  # 16组随机数组，每组含100个随机数，用来生成16张图片。

def generateRes(gen_model, test_noise):
    pre_images = gen_model(test_noise, training=False)
    print(pre_images)

def train(dataset, epochs):
    count = 0
    for epoch in range(epochs):
        for image_batch in dataset:
            train_step(image_batch)
            count += 1
            if count % 100 == 0:
                print(count, " check")
        generateRes(generator, seed)
        # generate_plot_image(generator, seed)
train(datasets, EPOCHS)