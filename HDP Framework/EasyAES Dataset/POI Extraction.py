import numpy as np

def extract_poi_window(traces, begin_index, end_index):
    """
    Extracts a window of Points of Interest (POIs) from a set of traces.
    
    Args:
        traces (np.ndarray): The input traces (e.g., shape (30000, 24000)).
        begin_index (int): The starting sample index for the window.
        end_index (int): The ending sample index for the window.
        
    Returns:
        np.ndarray: The new array of traces containing only the POI window.
    """
    num_traces = traces.shape[0]
    window_length = end_index - begin_index + 1
    
    # Create an empty array for the POI traces
    poi_traces = np.zeros((num_traces, window_length), dtype=traces.dtype)
    
    # Extract the window from each trace
    for i in range(num_traces):
        poi_traces[i] = traces[i][begin_index : end_index + 1]
        
    return poi_traces

# Example usage:
# raw_traces = np.load('EasyAES.npy')
# poi_traces = extract_poi_window(raw_traces, 1000, 1999)
# np.save('EasyAES_pois.npy', poi_traces)

# Define the path to your dataset files
DATA_PATH = './' # Or 'C:/path/to/your/data/'

# Load the traces, plaintexts, and POIs
traces = np.load(f'{DATA_PATH}EasyAES.npy')
plains = np.load(f'{DATA_PATH}EasyAES_plain.npy')
pois = np.load(f'{DATA_PATH}EasyAES_pois.npy')

print(f"Traces shape: {traces.shape}")
print(f"Plaintexts shape: {plains.shape}")
print(f"POIs shape: {pois.shape}")

