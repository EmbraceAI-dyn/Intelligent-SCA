# EasyAES Dataset

This repository contains the **EasyAES dataset**, a collection of power consumption traces from an unprotected AES-128 implementation. The data was collected to support research in Side-Channel Analysis (SCA), particularly for evaluating profiling and non-profiling attack techniques.

## Dataset Specifications

*   **Target Device:** STM32F303RDT6 (32-bit microcontroller)
*   **Acquisition Platform:** NewAE ChipWhisperer-Lite
*   **Target Algorithm:** AES-128 (Software implementation, no countermeasures/masking)

## File Structure

The dataset is provided in the NumPy (`.npy`) format and consists of three main files:

*   `EasyAES_plain.npy`
    *   **Content:** Plaintexts used for the acquisitions.
    *   **Shape:** `(30000, 16)`
    *   **Description:** Contains 30,000 plaintexts. Each row is a 16-byte plaintext corresponding to an encryption operation.

*   `EasyAES.npy`
    *   **Content:** The raw, full power consumption traces.
    *   **Shape:** `(30000, 24000)`
    *   **Description:** Contains 30,000 traces, where each trace has 24,000 sample points. These traces are captured directly and have not been pre-aligned.

*   `EasyAES_pois.npy`
    *   **Content:** Pre-processed traces containing the Points of Interest (POIs).
    *   **Shape:** `(30000, 1000)`
    *   **Description:** These are windows extracted from the raw traces to focus on the leakage from the first-round S-box operations. Each POI trace consists of 1,000 sample points, extracted from index `1000` to `1999` (inclusive) of the corresponding raw trace.

### POI Extraction Code

The following Python function demonstrates how the `EasyAES_pois.npy` file was generated from the raw traces.

```python
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
# raw_traces = np.load('EasyAES_pois.npy')
# poi_traces = extract_poi_window(raw_traces, 1000, 1999)
# np.save('EasyAES_pois.npy', poi_traces)
