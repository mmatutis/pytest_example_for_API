# pytest_example_for_API
Example project for py.test usage for API testing and JSON schema validation

## System requirements
  Python 3.5+

## Steps to set up the project
  
  1) Clone git repository
  
  2) Go in a project folder
  
  3) Install the required package
  
  ```
  pip install -r requirements.txt
  ```
  
  4) Start a project with a simple command
  
  ```
  py.test
  ```
  
  
## Documentation
### File explanation
*conftest.py* - This is configuration file for py.test project;

*test_JSON_Validation.py* - There is example test for JSON schema validation;

*test_stock_API.py* - couple example tests for simple API calls and assertation also parameterized test example;

### CI with jenkins
A simple example will be just Jenkins freestyle project. First, you must set your that your source code is in a git repository. Then in *Build environment* select `Delete workspace before build starts`. And build step is a simple bash execution where you need only two commands:
```
pip install -r requirements.txt
py.test
```
