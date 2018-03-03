# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:26:25 2018

@author: kcchi
"""

import numpy as np

get_scenario_d = {"assets": {"blue0": {"class": "remote", "pos": [407.92073628850466, 4717.220135236664], "team": 0, "vision_range": 400, "health": 100, "etype": "ISR_DRONE_1", "modules": {"sensors": [{"type": "A", "rate": 1, "range": 350}], "fuel": [{"cap": 100, "rate": 0.01, "rate2": 0.1, "min_clamp": 0.005, "type": "acceleration"}]}}, "blue1": {"class": "remote", "pos": [420.92073628850466, 4717.220135236664], "team": 0, "vision_range": 400, "health": 100, "etype": "ISR_DRONE_1", "modules": {"sensors": [{"type": "A", "rate": 1, "range": 350}], "fuel": [{"cap": 100, "rate": 0.01, "rate2": 0.1, "min_clamp": 0.005, "type": "acceleration"}]}}, "blue2": {"class": "remote", "pos": [431.92073628850466, 4717.220135236664], "team": 0, "vision_range": 400, "health": 100, "etype": "ISR_DRONE_1", "modules": {"sensors": [{"type": "A", "rate": 1, "range": 350}], "fuel": [{"cap": 100, "rate": 0.01, "rate2": 0.1, "min_clamp": 0.005, "type": "acceleration"}]}}, "blue3": {"class": "remote", "pos": [395.92073628850466, 4717.220135236664], "team": 0, "vision_range": 400, "health": 100, "etype": "ISR_DRONE_1", "modules": {"sensors": [{"type": "A", "rate": 1, "range": 350}], "fuel": [{"cap": 100, "rate": 0.01, "rate2": 0.1, "min_clamp": 0.005, "type": "acceleration"}]}}}, "step": 0.5, "map_settings": {"size": [5000, 5000]}, "mission_length": 1}

assets_d                    = get_scenario_d['assets']
assets_name                 = np.array(list(assets_d.keys()))
assets_state_basic_keys     = np.array(['class', 'health', 'etype', 'team', 'vision_range'])
assets_state_fuel_keys      = np.array(['cap', 'min_clamp', 'rate', 'rate2', 'type'])
assets_state_sensors_keys   = np.array(['range', 'rate', 'type'])
assets_state_pos_keys       = np.array(['pos'])

num_assets                  = len(assets_name)
num_assets_state_basic      = len(assets_state_basic_keys)
num_assets_state_fuel       = len(assets_state_fuel_keys)
num_assets_state_sensors    = len(assets_state_sensors_keys)
num_assets_state_pos        = 2

assets_state_basic_vals     = np.empty([num_assets, num_assets_state_basic], dtype='U25')
assets_state_fuel_vals      = np.empty([num_assets, num_assets_state_fuel], dtype='U25')
assets_state_sensors_vals   = np.empty([num_assets, num_assets_state_sensors], dtype='U25')
assets_state_pos_vals       = np.empty([num_assets,num_assets_state_pos], dtype='U25')

for idx, a in enumerate(assets_name):
    
    for i in range(num_assets_state_basic):
        assets_state_basic_vals[idx,i] = assets_d[a][assets_state_basic_keys[i]]
        
    for i in range(num_assets_state_fuel):
        fuel = assets_d[a]['modules']['fuel']
        fuel = fuel[-1]

        assets_state_fuel_vals[idx,i] = fuel[assets_state_fuel_keys[i]]
        
    for i in range(num_assets_state_sensors):
        sensors = assets_d[a]['modules']['sensors']
        sensors = sensors[-1]
        assets_state_sensors_vals[idx,i] = sensors[assets_state_sensors_keys[i]]

    for i in range(num_assets_state_pos):
        assets_state_pos_vals[idx,i] = assets_d[a][assets_state_pos_keys[0]][i]

assets_state_basic_vals     = np.c_[assets_name, assets_state_basic_vals]
assets_state_fuel_vals      = np.c_[assets_name, assets_state_fuel_vals]
assets_state_sensors_vals   = np.c_[assets_name, assets_state_sensors_vals]
assets_state_pos_vals       = np.c_[assets_name, assets_state_pos_vals]

env = np.array([get_scenario_d['map_settings']['size'][0], 
                get_scenario_d['map_settings']['size'][1], 
                get_scenario_d['mission_length'], 
                get_scenario_d['step']])
    
print(env)
print(assets_state_basic_vals)
print(assets_state_fuel_vals)
print(assets_state_sensors_vals)
print(assets_state_pos_vals)