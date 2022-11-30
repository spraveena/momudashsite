import tensorflow as tf
import matplotlib.pyplot as plt
import scipy.io


original_dim = 128
latent_dim = 56


#load data
data = scipy.io.loadmat('pilotdata.mat')
labels = scipy.io.loadmat('pilotlabels.mat')

#build encoder
encoder = tf.keras.Sequential(
      [
      tf.keras.layers.InputLayer(input_shape=(original_dim,) ),
      tf.keras.layers.Dense(96, activation='relu'),
      tf.keras.layers.Dense(latent_dim, activation='relu')
      ]
  )
encoder.compile(optimizer=tf.keras.optimizers.Adam())

def plot_label_clusters(model, data, labels):
  z_mean,z_logvar = tf.split(encoder(data),num_or_size_splits=2,axis=1)
  plt.figure(figsize=(12,10))
  plt.scatter(z_mean[:,0], z_mean[:,1], c=labels)
  plt.colorbar()
  plt.show()

plot_label_clusters(encoder,data,labels)


