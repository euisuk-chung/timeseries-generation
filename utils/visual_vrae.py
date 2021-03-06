from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def visualization(original_data, generated_data, analysis, name, x_zoom=False, y_zoom=False):
    """Using PCA or tSNE for generated and original data visualization.

    Args:
      - ori_data: original data
      - generated_data: generated synthetic data
      - analysis: tsne or pca
    """
    plt.rcParams["figure.figsize"] = (10,10)

    # Data preprocessing
    original_data = np.asarray(original_data)
    generated_data = np.asarray(generated_data)
    
    # get row & column
    row, col = original_data.shape
    print(f'row : {row}, col : {col}')

    if analysis == 'pca':
        # PCA Analysis
        pca = PCA(n_components=2)
        
        # fit PCA with original data
        pca.fit(original_data)
        
        # transform
        pca_org = pca.transform(original_data)
        pca_gen = pca.transform(generated_data)

        # Plotting
        f, ax = plt.subplots(1)
        
        plt.scatter(pca_org[:, 0], pca_org[:, 1],
                    c='tab:blue', alpha=0.2, label="Original")
        plt.scatter(pca_gen[:, 0], pca_gen[:, 1],
                    c='tab:orange', alpha=0.2, label="Synthetic")

        ax.legend()
        
        if x_zoom != False and y_zoom != False:
            plt.xlim(x_zoom[0],x_zoom[1])
            plt.ylim(y_zoom[0],y_zoom[1])
        
        plt.title(f'{name} PCA')
        plt.xlabel('PC_1')
        plt.ylabel('PC_2')
        plt.show()

    elif analysis == 'tsne':
        # TSNE Analysis
        tsne = TSNE(n_components=2, verbose=1, perplexity=50, n_iter=1000)
        
        # conat data
        concat_data = np.concatenate((original_data, generated_data), axis=0)
        
        # fit and transform
        tsne_results = tsne.fit_transform(concat_data)
        
        # Plotting
        f, ax = plt.subplots(1)
              
        plt.scatter(tsne_results[:row, 0], tsne_results[:row, 1],
                    c='tab:blue', alpha=0.2, label="Original")
        plt.scatter(tsne_results[row:, 0], tsne_results[row:, 1],
                    c='tab:orange', alpha=0.2, label="Synthetic")

        ax.legend()
        
        if x_zoom != False and y_zoom != False:
            plt.xlim(0,x_zoom)
            plt.ylim(0,y_zoom)
        
        plt.title(f'{name} T-SNE')
        plt.xlabel('x-tsne')
        plt.ylabel('y-tsne')
        plt.show()