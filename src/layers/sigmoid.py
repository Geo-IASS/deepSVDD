import lasagne.layers


class Sigmoid(lasagne.layers.NonlinearityLayer):

    # for convenience
    isdense, isbatchnorm, isconv, isdropout, ismaxpool, issvm = (False,) * 6
    isactivation, issigmoid = (True,) * 2
    isrelu = False

    def __init__(self, incoming_layer, **kwargs):

        lasagne.layers.NonlinearityLayer.__init__(
            self, incoming_layer, name="sigmoid",
            nonlinearity=lasagne.nonlinearities.sigmoid, **kwargs)

        self.num_units = self.input_shape[1]
