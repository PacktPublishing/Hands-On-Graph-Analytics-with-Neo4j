# Flask + neomodel application

## Usage

You can create a virtualenv to install packages (not mandatory):

    python3 -m venv venv
    source venv/bin/activate
    
Then, you can:

1. Install dependencies:

         pip install -r requirements.txt
		 
2. Populate the graph with some toy data:
    - Configure your connection parameters in `models.py`
	- Run:

            python models.py
			
3. Run the flask application:

        flask run
		
4. Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

