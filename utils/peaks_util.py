def get_echo_peaks(peaks, window_size=1024, echo_left_size=256):
# Anuj's code:  
#     prev_value = peaks[0] #old
#     echos = []
#     if peaks[0] > echo_left_size:
#         echos.append(peaks[0])
#     # if peaks[-1] < echo_right_size 
#     for i in peaks:
#         if len(echos):
#             if i - prev_value - echo_left_size > window_size:
#                 prev_value = i
#                 echos.append(i)

# #My modification: 
    echos = []
    for peak in peaks:
        prev_value = peak
        if prev_value > echo_left_size:
            echos.append(prev_value)
            break
    for new_peak in peaks: 
        if len(echos):
            if new_peak - prev_value > window_size:
                prev_value = new_peak 
                echos.append(new_peak)
    return echos
