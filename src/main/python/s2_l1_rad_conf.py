"""
Contains Sentinel-2 Level-1 radiometric configuration
"""

Lref = [129.11, 128, 128, 108, 74.6, 68.23, 66.70, 103, 52.39, 8.77, 6, 4, 1.70]

u_stray_rand_all = {'Sentinel-2A': [0.1, 0.1, 0.08, 0.12, 0.44, 0.16, 0.2, 0.2, 0.04, 0.8, 0, 0, 0],
                    'Sentinel-2B': [0.1, 0.1, 0.08, 0.12, 0.44, 0.16, 0.2, 0.2, 0.04, 0.8, 0, 0, 0]}

u_xtalk_all = {'Sentinel-2A': [0.05, 0.01, 0.01, 0.01, 0.04, 0.03, 0.04, 0.02, 0.03, 0.02, 0.19, 0.15, 0.02],
                    'Sentinel-2B': [0.05, 0.01, 0.01, 0.01, 0.04, 0.03, 0.04, 0.02, 0.03, 0.02, 0.19, 0.15, 0.02]}

u_DS_all = {'Sentinel-2A': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.24, 0.12, 0.16],
                    'Sentinel-2B': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.24, 0.12, 0.16]}

# values from ICCDB (S2A at S2_OPER_MSI_DIFF___20150519T000000_0009.xml and
# S2B at S2_OPER_MSI_DIFF___20160415T000000_0001.xml)
u_diff_absarray = {'Sentinel-2A': [1.09, 1.08, 0.84, 0.73, 0.68, 0.97, 0.83, 0.81, 0.88, 0.97, 1.39, 1.39, 1.58],
                    'Sentinel-2B': [1.16, 1.00, 0.79, 0.70, 0.85, 0.77, 0.80, 0.80, 0.85, 0.66, 1.70, 1.46, 2.13]}

u_diff_temp_rate = {'Sentinel-2A': [0.15, 0.09, 0.04, 0.02, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    'Sentinel-2B': [0.15, 0.09, 0.04, 0.02, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}

