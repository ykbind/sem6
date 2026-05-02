```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

```


```python
# 2. Load Dataset
df = pd.read_csv("titanic.csv")   # keep csv file in same folder

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

```

    First 5 Rows:
       PassengerId  Survived  Pclass  \
    0            1         0       3   
    1            2         1       1   
    2            3         1       3   
    3            4         1       1   
    4            5         0       3   
    
                                                    Name     Sex   Age  SibSp  \
    0                            Braund, Mr. Owen Harris    male  22.0      1   
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
    2                             Heikkinen, Miss. Laina  female  26.0      0   
    3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
    4                           Allen, Mr. William Henry    male  35.0      0   
    
       Parch            Ticket     Fare Cabin Embarked  
    0      0         A/5 21171   7.2500   NaN        S  
    1      0          PC 17599  71.2833   C85        C  
    2      0  STON/O2. 3101282   7.9250   NaN        S  
    3      0            113803  53.1000  C123        S  
    4      0            373450   8.0500   NaN        S  
    


```python
    print("\nDataset Loaded Successfully")
```

    
    Dataset Loaded Successfully
    


```python
print("\nShape of Dataset:")
print(df.shape)
```

    
    Shape of Dataset:
    (891, 12)
    


```python
print("\nColumns:")
print(df.columns)

```

    
    Columns:
    Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
           'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
          dtype='str')
    


```python
print("\nData Types:")
print(df.dtypes)
```

    
    Data Types:
    PassengerId      int64
    Survived         int64
    Pclass           int64
    Name               str
    Sex                str
    Age            float64
    SibSp            int64
    Parch            int64
    Ticket             str
    Fare           float64
    Cabin              str
    Embarked           str
    dtype: object
    


```python
print("\nMissing Values:")
print(df.isnull().sum())
```

    
    Missing Values:
    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64
    


```python
print("\nStatistical Summary:")
print(df.describe())

```

    
    Statistical Summary:
           PassengerId    Survived      Pclass         Age       SibSp  \
    count   891.000000  891.000000  891.000000  714.000000  891.000000   
    mean    446.000000    0.383838    2.308642   29.699118    0.523008   
    std     257.353842    0.486592    0.836071   14.526497    1.102743   
    min       1.000000    0.000000    1.000000    0.420000    0.000000   
    25%     223.500000    0.000000    2.000000   20.125000    0.000000   
    50%     446.000000    0.000000    3.000000   28.000000    0.000000   
    75%     668.500000    1.000000    3.000000   38.000000    1.000000   
    max     891.000000    1.000000    3.000000   80.000000    8.000000   
    
                Parch        Fare  
    count  891.000000  891.000000  
    mean     0.381594   32.204208  
    std      0.806057   49.693429  
    min      0.000000    0.000000  
    25%      0.000000    7.910400  
    50%      0.000000   14.454200  
    75%      0.000000   31.000000  
    max      6.000000  512.329200  
    


```python
print("\nDataset Info:")
print(df.info())
```

    
    Dataset Info:
    <class 'pandas.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  891 non-null    int64  
     1   Survived     891 non-null    int64  
     2   Pclass       891 non-null    int64  
     3   Name         891 non-null    str    
     4   Sex          891 non-null    str    
     5   Age          714 non-null    float64
     6   SibSp        891 non-null    int64  
     7   Parch        891 non-null    int64  
     8   Ticket       891 non-null    str    
     9   Fare         891 non-null    float64
     10  Cabin        204 non-null    str    
     11  Embarked     889 non-null    str    
    dtypes: float64(2), int64(5), str(5)
    memory usage: 83.7 KB
    None
    


```python
print(df["Age"].isnull().sum())   # check missing values

df["Age"] = df["Age"].fillna(df["Age"].mean()).astype(int)

print(df["Age"].head())
```

    177
    0    22
    1    38
    2    26
    3    35
    4    35
    Name: Age, dtype: int64
    


```python
# Check missing values
print(df["Embarked"].isnull().sum())

# Fill with mode (most common value)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Check again
print(df["Embarked"].isnull().sum())
```

    2
    0
    


```python
df.drop("Cabin", axis=1, inplace=True)
```


```python
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

```

    
    Missing Values After Cleaning:
    PassengerId    0
    Survived       0
    Pclass         0
    Name           0
    Sex            0
    Age            0
    SibSp          0
    Parch          0
    Ticket         0
    Fare           0
    Embarked       0
    dtype: int64
    


```python
df["Age"] = df["Age"].astype(int)
```


```python
df["Fare"] = df["Fare"].astype(float)
```


```python
print("\nUpdated Data Types:")
print(df.dtypes)

```

    
    Updated Data Types:
    PassengerId      int64
    Survived         int64
    Pclass           int64
    Name               str
    Sex                str
    Age              int64
    SibSp            int64
    Parch            int64
    Ticket             str
    Fare           float64
    Embarked           str
    dtype: object
    


```python
scaler = MinMaxScaler()
```


```python
df[["Age", "Fare"]] = scaler.fit_transform(df[["Age", "Fare"]])

```


```python
print("\nAfter Normalization:")
print(df[["Age", "Fare"]].head())

```

    
    After Normalization:
          Age      Fare
    0  0.2750  0.014151
    1  0.4750  0.139136
    2  0.3250  0.015469
    3  0.4375  0.103644
    4  0.4375  0.015713
    


```python
le = LabelEncoder()
```


```python
df["Sex"] = le.fit_transform(df["Sex"])
```


```python
df["Embarked"] = le.fit_transform(df["Embarked"])
```


```python
print("\nAfter Encoding Categorical Variables:")
print(df[["Sex", "Embarked"]].head())

```

    
    After Encoding Categorical Variables:
       Sex  Embarked
    0    1         2
    1    0         0
    2    0         2
    3    0         2
    4    1         2
    


```python

print("\nFinal Dataset Preview:")
print(df.head())

```

    
    Final Dataset Preview:
       PassengerId  Survived  Pclass  \
    0            1         0       3   
    1            2         1       1   
    2            3         1       3   
    3            4         1       1   
    4            5         0       3   
    
                                                    Name  Sex     Age  SibSp  \
    0                            Braund, Mr. Owen Harris    1  0.2750      1   
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...    0  0.4750      1   
    2                             Heikkinen, Miss. Laina    0  0.3250      0   
    3       Futrelle, Mrs. Jacques Heath (Lily May Peel)    0  0.4375      1   
    4                           Allen, Mr. William Henry    1  0.4375      0   
    
       Parch            Ticket      Fare  Embarked  
    0      0         A/5 21171  0.014151         2  
    1      0          PC 17599  0.139136         0  
    2      0  STON/O2. 3101282  0.015469         2  
    3      0            113803  0.103644         2  
    4      0            373450  0.015713         2  
    


```python

```
