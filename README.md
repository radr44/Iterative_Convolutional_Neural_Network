# Iterative_Convolutional_Neural_Network
This repository contains PyTorch implementation of the paper titled "ICNN: An iterative implementation of convolutional neural networks to enable energy and computational complexity aware dynamic approximation" for the purpose of time/threshold dependent image classification(hand gestures captured using a leap motion sensor),the dataset used was formed by combining the front sensor data from the publicly available datasets mentioned below,total 15 different gestures were used in training.<br />
<br />
A slightly lighter architecture was used than the one mentioned in the paper(trained on Imagenet~1.2 million images) with fewer filters in each layer due to unavailability of large datasets and advanced hardware accelerators to train a heavier network.The same code can be also used to train more complex networks if one changes the parameters corresponding to the number of filters and maximum number of iterations.<br />
<br />
Parallel training(details available in the paper) was used to train the network(with maximum 6 iterations) using adam optimizer and a varying learning rate.Subsamples of the images were obtained using standard combinations of sobel x,y ,laplacian filters and gaussian downscale unlike discrete wavelet transform used in the paper.Subsampling was slightly redundant but obtained better results compared to dwt for this particular training set,interpolation used during resizing was cv.INTER_NEAREST to favour faster computation over quality.Subsampling results can be found [here](https://github.com/radr44/Iterative_Convolutional_Neural_Network/tree/master/subsamples)<br />
<br />
References
- [K. Neshatpour, F. Behnia, H. Homayoun and A. Sasan, "ICNN: An iterative implementation of convolutional neural networks to enable energy and computational complexity aware dynamic approximation," 2018 Design, Automation & Test in Europe Conference & Exhibition (DATE), Dresden, 2018, pp. 551-556, doi: 10.23919/DATE.2018.8342068.](https://ieeexplore.ieee.org/document/8342068)
- [ICNN: The Iterative Convolutional Neural Network:ACM Transactions on Embedded Computing SystemsDecember 2019 Article No.: 119 https://doi.org/10.1145/3355553](https://dl.acm.org/doi/10.1145/3355553)<br />
<br />
Datasets
- [Multi-Modal Dataset for Hand Gesture Recognition](https://www.kaggle.com/gti-upm/multimodhandgestrec)
- [LeapMotion Hand Gesture Dataset for UAV Management](https://www.kaggle.com/gti-upm/leaphandgestuav)
