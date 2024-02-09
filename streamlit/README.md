
## Streamlit

Author/Developer of the tutorial - [Piyush Anand](https://github.com/piyush-an)

### What is Streamlit ?
> Streamlit is an open-source app framework for Machine Learning and Data Science teams to create beautiful web apps in minutes.

### Prerequisite
* IDE
* Python 3.x

### Deployed App

App is deployed on Streamlit Cloud and accessed via [link](https://piyush-an-damg7245-spring23-streamlitmain-drkgeo.streamlit.app/)

---

### Tutorial

Step 01: Create a python virtual environment and activate
```bash
python -m venv venv
sopurce ./venv/bin/activate
```

Step 02: Install python Packages
```bash
pip install streamlit
```
Step 03: Develop a python script - main.py

In this guide, you're going to use Streamlit's core features to create an interactive app; exploring a public Uber dataset for pickups and drop-offs in New York City. When you're finished, you'll know how to fetch and cache data, draw charts, plot information on a map, and use interactive widgets, like a slider, to filter results.

https://docs.streamlit.io/library/get-started/create-an-app

Step 04: Run Streamlit app
```bash
streamlit run main.py
```

Step 05: Export python dependency
```bash
pip freeze > requirements.txt
```

Step 06: Commit your code to github

**Never commit your virtual environment**. <br> 
Generate `requirements.txt` file using `pip freeze > requirements.txt` and install on the target machine by `pip install -r requirements.txt`.

Step 07: Deploy on Streamlit Cloud

https://streamlit.io/cloud



### Build docker for streamlit component

1. Docker Build to build the image

    ```bash
    docker build -t demo_streamlit:v3 .
    ```

2. Docker Run to run it locally to test

    ```bash
    docker run -p 8081:8080 demo_streamlit:v3
    ```

3. Tag the build image

    ```bash
    docker tag demo_streamlit:v3 ashrithagoramane/streamlit:latest
    #          local_image:tag   dockerhub_username/destination_image_name:tag
    ```

4. Push the image to DockerHub, make sure you are logged in into the docker desktop

    ```bash
    docker push ashrithagoramane/streamlit:latest
    ```
