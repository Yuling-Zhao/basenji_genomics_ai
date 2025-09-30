# Basenji Genomics AI

A reproducible project showcasing **genomics deep learning** with the Basenji model, extended to integrate **Hi-C** data as an additional input modality.  
This repository is designed both as a research prototype and as a **showcase for my postdoctoral application**.

---

## Goals
- **Reproduce** published Basenji results on selected ENCODE datasets  
- **Extend** the model to include intra-chromatin interactions from Hi-C in the input layer  
- **Track** the entire workflow with [MLflow](https://mlflow.org/)  
- **Document** experiments in a clear, portable, and reproducible way  

---

## Installation

This project builds upon the [Basenji](https://github.com/calico/basenji) framework for genomic sequence modeling.

### Prerequisites
Generate the parent directory (ml_project/) and then separate the Basenji original repo from the repo of this project
```bash
mkdir -p ml_project
cd ./ml_project
```

### Set up the two repositories
1. **Clone this repository and set up environment:**
```bash
git clone https://github.com/Yuling-Zhao/basenji-genomics-ai.git
cd basenji-genomics-ai
conda env create -f environment.yml
conda activate basenji_genomics_ai
```
2. **Clone and install Basenji:**
```bash 
# Go back to parent directory
cd ../
# Clone and install Basenji
git clone https://github.com/calico/basenji.git
python setup.py develop --no-deps
# Recommend by the basenji authors: setting the following environmental variables.
export BASENJIDIR=~/code/Basenji
export PATH=$BASENJIDIR/bin:$PATH
export PYTHONPATH=$BASENJIDIR/bin:$PYTHONPATH
```

---

## Using MLflow
### Quickstart (server-based tracking with file-based storage)
1. Run a local Tracking Server on a new terminal
```bash
 mlflow server --host 127.0.0.1 --port 8080
 ```
2. Run a script that logs to MLflow on a separate terminal:
```bash
python scripts/tracking/project_creation_tracker.py
```
3. Check the tracking logs:
   Open [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser.

---

## References
- Kelley et al., *Sequential regulatory activity prediction across chromosomes with convolutional neural networks* (2018)  
- ENCODE Project Consortium  
- MLflow Documentation: https://mlflow.org/docs/latest/index.html  

---

## Third-Party Code

This project includes code from [Basenji](https://github.com/calico/basenji) 
which is licensed under the Apache License 2.0.

---

## Author
**Yuling Zhao**  
Doctoral researcher, MPI of Immunobiology & Epigenetics  
Focus: Chromatin dynamics, epigenetics, and machine learning for genomics  
