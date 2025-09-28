# Basenji Genomics AI

A reproducible project showcasing **genomics deep learning** with the Basenji model, extended to integrate **ATAC-seq** data as an additional input modality.  
This repository is designed both as a research prototype and as a **showcase for my postdoctoral application**.

---

## Goals
- **Reproduce** published Basenji results on selected ENCODE datasets  
- **Extend** the model to include ATAC-seq coverage in the input layer  
- **Track** the entire workflow with [MLflow](https://mlflow.org/)  
- **Document** experiments in a clear, portable, and reproducible way  

---

## Repository Structure
wait after the project completed

---

## Installation
1. Clone this repo:
   ```bash
   git clone https://github.com/Yuling-Zhao/basenji-genomics-ai.git
   cd basenji-genomics-ai
   ```

2. Create environment (conda recommended):
   ```bash
   conda env create -f environment.yml
   conda activate basenji-atac
   ```

3. Install in editable mode:
   ```bash
   pip install -e .
   ```

---

## Using MLflow
### Quickstart (file-based tracking)
1. Run a script that logs to MLflow:
   ```bash
   python scripts/tracking/project_creation_tracker.py
   ```

2. Launch the MLflow UI:
   ```bash
   mlflow ui --backend-store-uri ./mlruns --port 8080
   ```
   Open [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser.

### Example: Training a model
```bash
python -m src.experiments.train configs/model_baseline.yaml
```

---

## Results
wait until I complete the practice

---

## Tests
Run shape and loader checks with:
```bash
pytest tests/
```

---

## References
- Kelley et al., *Sequential regulatory activity prediction across chromosomes with convolutional neural networks* (2018)  
- ENCODE Project Consortium  
- MLflow Documentation: https://mlflow.org/docs/latest/index.html  

---

## 👩‍💻 Author
**Yuling Zhao**  
Doctoral researcher, MPI of Immunobiology & Epigenetics  
Focus: Chromatin dynamics, epigenetics, and machine learning for genomics  
