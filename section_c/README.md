# Section C: Option 4 


1. Ensure that you have Python installed on your system. You can check the version of Python by running the command python --version in your terminal.

2. Install the venv module if it is not already installed. The venv module is available in Python 3.3 and later versions. If you have an older version of Python, you can install it by running pip install virtualenv.

3. Decide on a directory where you want to create your virtual environment. Choose a location that is separate from your global Python installation to keep your project dependencies isolated.

4. Open a terminal or command prompt and navigate to the chosen directory.

5. Create a new virtual environment by running the command:

    python -m venv myenv

Replace myenv with the name you want to give to your virtual environment. This command creates a new directory called myenv (or your chosen name) in the current location, which will contain the virtual environment files.

6. Activate the virtual environment:
    source myenv/bin/activate

Running the main script : Navigate to the isbn folder and type python3 main.py on th command prompt

Running the test cases in the test file : Type pytest test.py