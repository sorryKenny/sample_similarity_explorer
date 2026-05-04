import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def compute_and_plot_pca(df, title="PCA of Samples"):
    """
    Computes PCA on the expression matrix and plots the first two principal components.
    Note: df should have samples as columns and genes as rows.
    """
    df_clean = df.dropna().T
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_clean)
    
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)
    
    pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
    pca_df['Sample'] = df_clean.index
    
    explained_variance = pca.explained_variance_ratio_ * 100
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df, s=100, color='darkblue')
    
    for i in range(pca_df.shape[0]):
        plt.text(pca_df['PC1'][i] + 0.5, pca_df['PC2'][i], pca_df['Sample'][i], 
                 horizontalalignment='left', size='medium', color='black')
        
    plt.title(title)
    plt.xlabel(f"PC1 ({explained_variance[0]:.2f}% variance)")
    plt.ylabel(f"PC2 ({explained_variance[1]:.2f}% variance)")
    plt.grid(True)
    plt.show()
    
    return pca_df
