import sys
sys.path.append(".")

import tensorflow as tf
from models.transformers.functions import create_model, prepare_data, train_model
from utils.config import MAC_MODEL, NUM_EPOCHS, print_current_device, NUM_EXPERIMENTS
from utils.metrics import MetricsCollector

def setup():
    tf.random.set_seed(7)  # fix random seed for reproducibility
    tf.config.set_visible_devices([], "GPU")  # Désactive le GPU
    print_current_device(tf)



def main():
    setup()
    for _ in range(NUM_EXPERIMENTS):
        trainX, trainY, testX, testY, scaler, dataset, look_back = prepare_data()
        model = create_model(look_back, tf)
        metrics_collector = MetricsCollector(
            device="CPU", mac_model=MAC_MODEL, model="Transformer"
        )  # Setup metrics collector
        train_model(model, trainX, trainY, NUM_EPOCHS, metrics_collector)
        metrics_collector.export_metrics()  # Export metrics


if __name__ == "__main__":
    main()
