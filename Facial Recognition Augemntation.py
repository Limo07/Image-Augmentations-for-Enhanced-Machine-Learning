import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random
def load_dataset(directory, image_size=(128, 128), batch_size=32):
    """
    Load images from a directory and prepare them for training.
    """
    dataset = tf.keras.utils.image_dataset_from_directory(
        directory,
        image_size=image_size,
        batch_size=batch_size
    )
    return dataset


def augment_image(image):
    """
    Apply five different augmentation techniques to an image.
    """
    image = tf.image.random_flip_left_right(image)  # Flip horizontally
    image = tf.image.random_flip_up_down(image)  # Flip vertically
    image = tf.image.random_brightness(image, max_delta=0.2)  # Adjust brightness
    image = tf.image.random_contrast(image, lower=0.5, upper=1.5)  # Adjust contrast
    image = tf.image.random_saturation(image, lower=0.5, upper=1.5)  # Adjust saturation
    return image


def visualize_augmentation(Faces, num_samples=5):
    """
    Randomly select images from the dataset and visualize the original and augmented images.
    """
    dataset_images = []
    for image_batch, _ in dataset.take(1):  # Take one batch from dataset
        dataset_images.extend(image_batch.numpy())

    random_images = random.sample(dataset_images, num_samples)

    fig, axes = plt.subplots(num_samples, 2, figsize=(10, num_samples * 3))
    for i, img in enumerate(random_images):
        augmented_img = augment_image(img)
        axes[i, 0].imshow(img.astype('uint8'))
        axes[i, 0].set_title("Original Image")
        axes[i, 0].axis("off")

        axes[i, 1].imshow(augmented_img.numpy().astype('uint8'))
        axes[i, 1].set_title("Augmented Image")
        axes[i, 1].axis("off")

    plt.tight_layout()
    plt.show()


# Define dataset directory
data_directory = "Faces"
dataset = load_dataset(data_directory)

# Visualize original vs augmented images
visualize_augmentation(dataset)

