#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = ['Embarked']

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = ['Cabin']

#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Age', 'Fare']

#Varibles para transformación logaritmia
NUMERICALS_LOG_VARS = ["Fare"]

#Variable a extraer la primera letra
FIRST_CHAR_VARS = ['Cabin']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['Sex', 'Embarked', 'Cabin']

#Variables seleccionadas para la predicción
FEATURES = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']