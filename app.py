from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

app = Flask(__name__)

# Load the breast cancer dataset
df = pd.read_csv('breast_cancer_detection.csv')
df.replace('?', np.nan, inplace = True)
df.dropna(inplace=True)
df.drop(['id'], axis = 1, inplace = True)
df['class'].replace(2,0, inplace = True)
df['class'].replace(4,1, inplace = True)

# Preprocess the dataset
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        clump_thickness = request.form['clump_thickness']
        unif_cell_size = request.form['unif_cell_size']
        unif_cell_shape = request.form['unif_cell_shape']
        marg_adhesion = request.form['marg_adhesion']
        single_epith_cell_size = request.form['single_epith_cell_size']
        bare_nuclei = request.form['bare_nuclei']
        bland_chrom = request.form['bland_chrom']
        norm_nucleoli = request.form['norm_nucleoli']
        mitoses = request.form['mitoses']

        try:
            # Convert user input to floats
            clump_thickness = float(clump_thickness)
            unif_cell_size = float(unif_cell_size)
            unif_cell_shape = float(unif_cell_shape)
            marg_adhesion = float(marg_adhesion)
            single_epith_cell_size = float(single_epith_cell_size)
            bare_nuclei = float(bare_nuclei)
            bland_chrom = float(bland_chrom)
            norm_nucleoli = float(norm_nucleoli)
            mitoses = float(mitoses)

            # Create a new DataFrame with user input
            new_data = pd.DataFrame({
                'clump_thickness': [clump_thickness],
                'unif_cell_size': [unif_cell_size],
                'unif_cell_shape': [unif_cell_shape],
                'marg_adhesion': [marg_adhesion],
                'single_epith_cell_size': [single_epith_cell_size],
                'bare_nuclei': [bare_nuclei],
                'bland_chrom': [bland_chrom],
                'norm_nucleoli': [norm_nucleoli],
                'mitoses': [mitoses]
            })

            # Make predictions using the trained model
            prediction = model.predict(new_data)[0]

            # Convert the prediction (0 or 1) to diagnosis ('Malignant' or 'Benign')
            diagnosis = 'Malignant' if prediction == 1 else 'Benign'

            return render_template('index.html', diagnosis=diagnosis)
        except ValueError:
            error_message = "Please enter valid numeric values in all the input fields."
            return render_template('index.html', error_message=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
