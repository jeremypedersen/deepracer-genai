# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# NOTE: This is a rewrite of deepracer.py designed to work exclusively with models
# which are stored locally. This makes it possible to use this notebook in environments
# where access to the DeepRacer service in us-east-1 is not possible (for instance, 
# in accounts where an SCP restricts usage to a region other than us-east-1).

import os
import json
import yaml

# Model path (used to fetch local model data)
model_path = '../deepracer_models/'

# SANITY CHECK: Does a given model exist, or not?
def model_exists(model_name):
    if os.path.isdir(f'{model_path}{model_name}'):
        return True
    else:
        return False

# Generate a list of available local models
def list_models():
    dirs = os.listdir(model_path)
    return dirs

# Given a model name, extract the model's metadata
# and return it as a JSON-formatted string
def get_model_metadata(model_name):
    try:
        with open(f'{model_path}{model_name}/model_metadata.json') as file:
            data = json.load(file)
        return data
    except:
        return "Something went wrong..."
    
def get_reward_function(model_name):
    try:
        with open(f'{model_path}{model_name}/reward_function.py') as file:
            data = file.read()
        return data
    except:
        return "Something went wrong..."
    
def get_hyper_parameters(model_name):
    try:
        with open(f'{model_path}{model_name}/ip/hyperparameters.json') as file:
            data = json.load(file)
        return data
    except:
        return "Something went wrong..."
    
def get_evaluation_metrics(model_name):
    try:
        path = f'{model_path}{model_name}/metrics/evaluation/'
        json_files = [file for file in os.listdir(path) if file.endswith('.json')]

        with open(f'{path}{json_files[0]}') as file:
            data = json.load(file)
        return data
    except:
        return "Something went wrong..."

def get_training_metrics(model_name):
    try:
        path = f'{model_path}{model_name}/metrics/training/'
        json_files = [file for file in os.listdir(path) if file.endswith('.json')]

        with open(f'{path}{json_files[0]}') as file:
            data = json.load(file)

            # Only keep evaluation runs (to cut down on the amount of
            # training data returned)
            metrics = data['metrics']
            filtered_metrics = [item for item in metrics if item['phase'] == 'evaluation']
            data['metrics'] = filtered_metrics
        return data
    except:
        return "Something went wrong..."

def get_training_params(model_name):
    try:
        path = f'{model_path}{model_name}/'
        json_files = [file for file in os.listdir(path) if file.startswith('training_params_')]

        with open(f'{path}{json_files[0]}') as file:
            data = file.read()
            data = file.read()
            data = yaml.safe_load(data)
        return data
    except:
        return "Something went wrong..."

def get_evaluation_params(model_name):
    try:
        path = f'{model_path}{model_name}/'
        json_files = [file for file in os.listdir(path) if file.startswith('eval_params_')]

        with open(f'{path}{json_files[0]}') as file:
            data = file.read()
            data = yaml.safe_load(data)
        return data
    except:
        return "Something went wrong..."
