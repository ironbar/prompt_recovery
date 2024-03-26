import numpy as np

import tensorflow_hub as hub
import tensorflow as tf
import tensorflow_text as text  # Registers the ops.


hub_url = "https://www.kaggle.com/models/google/sentence-t5/frameworks/TensorFlow2/variations/st5-base/versions/1"
encoder = hub.KerasLayer(hub_url)


def get_sharpened_cosine_similarity(ground_truth, predictions):
    responses_embeddings = compute_t5_embeddings(ground_truth)
    ground_truth_embeddings = compute_t5_embeddings(predictions)
    similarity = np.sum(responses_embeddings * ground_truth_embeddings, axis=1)
    return similarity**3


def compute_t5_embeddings(texts):
    """ I have verified that the embeddings have unit norm """
    embeddings = encoder(tf.constant(texts))[0].numpy()
    return embeddings


def estimate_mean(values):
    mean = np.mean(values)
    uncertainty = np.std(values) / np.sqrt(len(values)) * 1.96
    return mean, uncertainty
