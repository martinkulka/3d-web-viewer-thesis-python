import SimpleITK as sitk

def register_image(fixed_image, moving_image):
    # Set up the registration method 
    registration_method = sitk.ImageRegistrationMethod() 
    registration_method.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50) 
    registration_method.SetMetricSamplingStrategy(registration_method.RANDOM) 
    registration_method.SetMetricSamplingPercentage(0.01) 
    registration_method.SetInterpolator(sitk.sitkLinear) 

    registration_method.SetOptimizerAsGradientDescent(learningRate=1.0, numberOfIterations=100, convergenceMinimumValue=1e-6, convergenceWindowSize=10) 

    # Set the initial transform as affine 
    initial_transform = sitk.CenteredTransformInitializer(fixed_image, moving_image, sitk.AffineTransform(3), sitk.CenteredTransformInitializerFilter.GEOMETRY) 
    registration_method.SetInitialTransform(initial_transform, inPlace=False) 

    # Perform registration 
    final_transform = registration_method.Execute(fixed_image, moving_image) 
    # Apply the registration to the moving image 
    resampled_image = sitk.Resample(moving_image, fixed_image, final_transform, sitk.sitkLinear, 0.0, moving_image.GetPixelID())

    # Save the transformed image 
    sitk.WriteImage(resampled_image, 'output.nii.gz')