#!/bin/sh

# val
python interaction_preprocessor_v3.py -m val -f DR_DEU_Roundabout_OF.json & python interaction_preprocessor_v3.py -m val -f DR_CHN_Merging_ZS2.json & python interaction_preprocessor_v3.py -m val -f DR_CHN_Roundabout_LN.json & python interaction_preprocessor_v3.py -m val -f DR_CHN_Merging_ZS0.json & python interaction_preprocessor_v3.py -m val -f DR_USA_Intersection_GL.json & python interaction_preprocessor_v3.py -m val -f DR_USA_Intersection_MA.json & python interaction_preprocessor_v3.py -m val -f DR_USA_Roundabout_FT.json & python interaction_preprocessor_v3.py -m val -f DR_USA_Intersection_EP0.json & python interaction_preprocessor_v3.py -m val -f DR_USA_Roundabout_EP.json & python interaction_preprocessor_v3.py -m val -f DR_USA_Intersection_EP1.json & python interaction_preprocessor_v3.py -m val -f DR_DEU_Merging_MT.json & python interaction_preprocessor_v3.py -m val -f DR_USA_Roundabout_SR.json


# train
#python interaction_preprocessor_v3.py -m train -f DR_DEU_Roundabout_OF.json & python interaction_preprocessor_v3.py -m train -f DR_CHN_Merging_ZS2.json & python interaction_preprocessor_v3.py -m train -f DR_CHN_Roundabout_LN.json & python interaction_preprocessor_v3.py -m train -f DR_CHN_Merging_ZS0.json & python interaction_preprocessor_v3.py -m train -f DR_USA_Intersection_GL.json & python interaction_preprocessor_v3.py -m train -f DR_USA_Intersection_MA.json & python interaction_preprocessor_v3.py -m train -f DR_USA_Roundabout_FT.json & python interaction_preprocessor_v3.py -m train -f DR_USA_Intersection_EP0.json & python interaction_preprocessor_v3.py -m train -f DR_USA_Roundabout_EP.json & python interaction_preprocessor_v3.py -m train -f DR_USA_Intersection_EP1.json & python interaction_preprocessor_v3.py -m train -f DR_DEU_Merging_MT.json & python interaction_preprocessor_v3.py -m train -f DR_USA_Roundabout_SR.json