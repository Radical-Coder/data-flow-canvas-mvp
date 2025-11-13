# Data Flow Canvas MVP  

This repository contains a simple end-to-end pipeline specification for a Data Flow Canvas using a Transform → API Request → End pattern. It includes:  

- `pipeline_spec.json` – defines the pipeline steps:  
  - **transform**: uses a `double_numbers` function to multiply each number in the input list by 2.  
  - **api_request**: makes a GET request to `https://jsonplaceholder.typicode.com/posts/1` and returns the JSON response.  
  - **end**: combines the results of the transform and API request.  
- `sample_data.json` – sample input data (an array of numbers).  
- `run_pipeline.py` – a minimal Python script that reads `sample_data.json`, applies the transform, calls the API, and prints the combined output.  

## Running the sample pipeline  

1. **Clone the repository**:  

   ```bash  
   git clone https://github.com/Radical-Coder/data-flow-canvas-mvp.git  
   cd data-flow-canvas-mvp  
   ```  

2. **Install dependencies**: The script requires the `requests` library. Install it via pip:  

   ```bash  
   pip install requests  
   ```  

3. **Run the pipeline script**:  

   ```bash  
   python run_pipeline.py  
   ```  

   The script will:  
   - Read numbers from `sample_data.json`.  
   - Double each number using the transform step.  
   - Fetch the sample post from the JSONPlaceholder API.  
   - Print a combined JSON object containing the doubled numbers and the API response.  

Feel free to modify `sample_data.json` with your own list of numbers or adjust the pipeline specification in `pipeline_spec.json` to experiment with different transforms or API endpoints. 
