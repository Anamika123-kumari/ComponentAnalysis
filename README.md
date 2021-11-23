# ComponentAnalysis
component analysis  using PCA ,NMF,DICTIONARYLEARNING
FIRST dataset is generated consisting 22 Alphabet is generated each of 4*4 matrix i.e 16 pixel values of each
then noisy images each of 1000 samples is generated randomly with gaussain noise with mean 0 and variance 0.1
each image is saved to one folder name dataset consisting total of 22000 sample of image
then each image of 4*4 is converted to image data to 1*16 matrix
so total 22000 of 1*16 images is made 22000*16 using writing pixels img_pixels3.csv file
This is feature vector space matrix representation.
on this matrix PCA is applied  
after that NMF  is applied
and component is extracted pca.component_,nmf.component_






