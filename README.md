# Notebooks del Proyecto EasyMoney

### 01-EDA_Analytics.ipynb
Contiene un análisis exploratorio del conjunto de datos del estudio de caso. Está enfocado en el preprocesamiento de los datos, especialmente en la limpieza y la imputación de valores nulos, descrito en detalle, para respaldar las etapas posteriores.
El análisis exploratorio con enfoque a negocios está implementado en formato PowerBI, para una visualización más dinámica.


### 02-EDA_Pipelines_build.ipynb
Estructura el preprocesamiento del notebook de análisis en pipelines, utilizando librerías de scikit-learn (transformers).


### 03-EDA_Pipelines_execute_preprocessing.ipynb
Ejecuta el preprocesamiento con los pipelines estructurados, generando el dataframe preprocesado y limpio, base para las demás etapas del proyecto. 


### 04_Feature_Engineering.ipynb
Creación de variables/atributos extraídos de los datos originales, utilizando el conocimiento del domìnio del negocio para mejorar la calidad de los resultados.


### 05-Clustering.ipynb
Contiene la segmentación de clientes (clustering), utilizando el dataframe con las nuevas variables (ingeniería de características).

### 06_1-Purchase propensity - accounts.ipynb
Modelo de propensión de compra para la familia de productos de cuenta (account).

### 06_2-Purchase propensity - saving_and_investment.ipynb
Modelo de propensión de compra para la familia de productos de ahorro e inversión (saving and investment).

### 06_3-Purchase propensity- financing.ipynb
Modelo de propensión de compra para la familia de productos financieros (financing).

### 06-4-Predict_Purchase propensity.ipynb
Modelo con predicción de compra de todas las categorías. Resulta en el dataframe para creación de lista de clientes para envío de correos electrónicos.

### 07-Dataset_marketing.ipynb
Dataframe para selección de clientes para campaña de marketing (10.000 clientes, con mayor ROI por familia de producto) y muestra de 1000 clientes.

### 08-Customization.ipynb
Notebook con la nueva segmentación (clustering), ahora de los 10.000 clientes seleccionados para campaña.