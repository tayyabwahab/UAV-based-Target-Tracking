"""
Siamese Network-based Object Tracker

This module implements a Siamese network-based object tracker for real-time
video tracking. It uses fully-convolutional Siamese networks to perform
template-based tracking with high accuracy and real-time performance.

Key Features:
- Fully-convolutional Siamese network architecture
- Template-based object tracking
- Real-time tracking performance
- GPU acceleration support
- Configurable tracking parameters

Author: UAV Security System Team
License: MIT
"""

#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017 bily     Huazhong University of Science and Technology
#
# Distributed under terms of the MIT license.

r"""Generate tracking results for videos using Siamese Model"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import os
import os.path as osp
import sys

import tensorflow as tf

CURRENT_DIR = osp.dirname(__file__)
sys.path.append(CURRENT_DIR)

from inference import inference_wrapper
from inference.tracker import Tracker
from utils.infer_utils import Rectangle
from utils.misc_utils import auto_select_gpu, mkdir_p, load_cfgs, rmdir


class SiameseTracker:
    """
    Siamese network-based object tracker for real-time video tracking.
    
    This class provides a complete Siamese network-based tracking system that
    can track objects in real-time video streams. It uses template-based tracking
    with fully-convolutional Siamese networks for high accuracy and performance.
    
    Attributes:
        tracker: Tracker instance for object tracking
        sess: TensorFlow session for model inference
        video_log_dir: Directory for logging tracking results
        graph: TensorFlow computation graph
    """
    
    def __init__(self,
                 debug=0,
                 checkpoint='Logs/SiamFC/track_model_checkpoints/SiamFC-3s-color-pretrained'):
        """
        Initialize the SiameseTracker with model configuration.
        
        Args:
            debug (int): Debug level for logging (0=minimal, higher=more verbose)
            checkpoint (str): Path to the model checkpoint file
            
        Note:
            The tracker automatically selects the best available GPU and loads
            the pre-trained Siamese network model from the specified checkpoint.
        """
        os.environ['CUDA_VISIBLE_DEVICES'] = auto_select_gpu()
        
        # run only on cpu
        # os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

        model_config, _, track_config = load_cfgs(checkpoint)
        track_config['log_level'] = debug

        g = tf.Graph()
        with g.as_default():
            model = inference_wrapper.InferenceWrapper()
            restore_fn = model.build_graph_from_config(model_config, track_config, checkpoint)
        g.finalize()
        if not osp.isdir(track_config['log_dir']):
            logging.info('Creating inference directory: %s', track_config['log_dir'])
            mkdir_p(track_config['log_dir'])


        gpu_options = tf.GPUOptions(allow_growth=True)
        sess_config = tf.ConfigProto(gpu_options=gpu_options)
        sess = tf.Session(graph=g, config=sess_config)
        # sess.run(tf.global_variables_initializer())
        restore_fn(sess)
        tracker = Tracker(model, model_config=model_config, track_config=track_config)
        video_name = "demo"
        video_log_dir = osp.join(track_config['log_dir'], video_name)
        rmdir(video_log_dir)
        mkdir_p(video_log_dir)
        self.tracker = tracker
        self.sess = sess
        self.video_log_dir = video_log_dir
        self.graph = g

    def set_first_frame(self, frame, r):
        """
        Set the first frame and initial bounding box for tracking.
        
        This method initializes the tracker with the first frame and the
        bounding box of the target object to track.
        
        Args:
            frame (numpy.ndarray): First frame image (RGB format)
            r (list): Bounding box coordinates [x, y, width, height]
            
        Note:
            The bounding box coordinates are converted to 0-indexed format
            and used to initialize the tracker's target template.
        """
        first_line = "{},{},{},{}".format(r[0], r[1], r[2], r[3])
        bb = [int(v) for v in first_line.strip().split(',')]
        init_bb = Rectangle(bb[0] - 1, bb[1] - 1, bb[2], bb[3])  # 0-index in python
        self.tracker.initialize(self.sess, init_bb, frame, self.video_log_dir)

    def track(self, frame):
        """
        Track the target object in the current frame.
        
        This method performs template-based tracking using the Siamese network
        to locate the target object in the current frame.
        
        Args:
            frame (numpy.ndarray): Current frame image (RGB format)
            
        Returns:
            list: Bounding box coordinates [x, y, width, height] of the tracked object
            
        Note:
            This method should be called after set_first_frame() has been called
            to initialize the tracker with the target object.
        """
        reported_bbox = self.tracker.track(self.sess, frame)
        return reported_bbox
