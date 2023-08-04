from flask import Flask, render_template, request
from model import preprocess_data, train_model, save_model, pd
import joblib

app = Flask(__name__)

file_name = 'breast_cancer_detection.csv'

X_train, X_test, y_train, y_test = preprocess_data(file_name)
model = train_model(X_train, y_train)

# Save the trained model to a file
model_file = 'model.joblib'
save_model(model, model_file)

# Load the trained model from the file
loaded_model = joblib.load(model_file)

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
            # model = joblib.load('model.joblib')
            prediction = loaded_model.predict(new_data)[0]

            # Convert the prediction (0 or 1) to diagnosis ('Malignant' or 'Benign')
            diagnosis = 'Malignant' if prediction == 1 else 'Benign'

            return render_template('index.html', diagnosis=diagnosis)
        except ValueError:
            error_message = "Please enter valid numeric values in all the input fields."
            return render_template('index.html', error_message=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
