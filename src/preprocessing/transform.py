from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd

def scale_features(X, method="standard"):
    if method == "standard":
        scaler = StandardScaler()
    elif method == "minmax":
        scaler = MinMaxScaler()
    else:
        raise ValueError("Choose 'standard' or 'minmax'")
    
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler

def encode_categorical(df, categorical_cols):
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))
    df = df.drop(columns=categorical_cols).reset_index(drop=True)
    return pd.concat([df, encoded_df], axis=1), encoder

def handle_imbalance(X, y, method='smote'):
    if method == 'smote':
        sampler = SMOTE(random_state=42)
    elif method == 'undersample':
        sampler = RandomUnderSampler(random_state=42)
    else:
        raise ValueError("Method must be 'smote' or 'undersample'")
    
    X_resampled, y_resampled = sampler.fit_resample(X, y)
    return X_resampled, y_resampled
