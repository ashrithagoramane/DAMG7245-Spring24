# Docker compose
1. Docker in 100 seconds
1. Docker compose documentation https://docs.docker.com/compose/compose-application-model/ 
1. Streamlit docker compose from image
    ```yaml
    services:
    streamlit:
        image: streamlitdemo
        ports:
        - "8081:8080"
    ```
1. Streamlit from build context
    ```yaml
    container_name: streamlit
    build:
        context: streamlit
    restart: always
    ports:
        - "8080:8080"
    env_file:
      - .env
    ``` 

# Airflow
1. Introduction to DAG and Airflow https://piyush-an.github.io/DAMG7245-Fall2023/airflow/intro/ 
1. Installing Airflow on local https://piyush-an.github.io/DAMG7245-Fall2023/airflow/install/
1. Walkthrough of Airflow UI
1. Creating a DAG https://piyush-an.github.io/DAMG7245-Fall2023/airflow/dag/ 

# Pydantic


1. What is pydantic https://docs.pydantic.dev/latest/concepts/models/ 
1. Create venv
    ```bash
    python -m venv venv
    ```
1. Create requirements.txt with dependant libraries and install 
    ```bash
    pydantic
    lxml
    beautifulsoup4
    pandas
    pytest
    ```
    Installing libraries
    ```bash
    pip install -r requirements.txt
    ```
1. Add a **.gitignore** for Python folder

1. Simple UserModel
    ```bash
    python script_1.py
    ```
1. ORM and BaseModel
    ```bash
    python script_2.py
    ```
1. TEI parsing using Dataclass
    ```bash
    python script_3.py
    ```
1. BaseModel instead of Dataclass
    ```bash
    python script_4.py
    ```
1. TEI parsing using BaseModel
    ```bash
    python script_1.py
    ```


# Pytest

1. Create a module utils with User model
    ```python
    from pydantic import BaseModel, Field

    class User(BaseModel):
        id: int
        name: str = 'Jane Doe'
        age: int = Field(gt=0)
    ```
2. Create unit test class
    ```python
    from unittest import TestCase
    from utils.Models import User

    class UserModelTestClass(TestCase):    
    ```
3. Positive test cases
    ```python
    def test_positive_correct_user_id(self):
        user = User(id='123', age=1)
        self.assertEqual(user.id, 123)
    
    def test_positive_incorrect_user_id(self):
        user = User(id='123', age=1)
        self.assertNotEqual(user.id, 321)
    
    def test_positive_incorrect_name(self):
        user = User(id='123', age=1)
        self.assertEqual(user.name, "Jane Doe")
    ```
4. Negative test case
    ```python
    def test_negative_age(self):
        try:
            User(id=123, age=-1)
        except ValidationError:
            self.assertTrue(True)
        self.assertFalse(False)
    ```
