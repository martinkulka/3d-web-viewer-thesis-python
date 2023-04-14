import SimpleITK as sitk

def fast_marching_segmentation(input_filename, output_filename, sigma, alpha, beta, time_threshold, stopping_time, seeds):
    #'BrainProtonDensitySlice.png', 'fastMarchingOutput.mha', 81 114 1.0 -0.5 3.0 100 110)
    # 117 174 125
    inputImage = sitk.ReadImage(input_filename, sitk.sitkFloat32)

    smoothing = sitk.CurvatureAnisotropicDiffusionImageFilter()
    smoothing.SetTimeStep(0.02)
    smoothing.SetNumberOfIterations(5)
    smoothing.SetConductanceParameter(9.0)
    smoothingOutput = smoothing.Execute(inputImage)

    gradientMagnitude = sitk.GradientMagnitudeRecursiveGaussianImageFilter()
    gradientMagnitude.SetSigma(sigma)
    gradientMagnitudeOutput = gradientMagnitude.Execute(smoothingOutput)

    sigmoid = sitk.SigmoidImageFilter()
    sigmoid.SetOutputMinimum(0.0)
    sigmoid.SetOutputMaximum(1.0)
    sigmoid.SetAlpha(alpha)
    sigmoid.SetBeta(beta)
    sigmoidOutput = sigmoid.Execute(gradientMagnitudeOutput)

    fastMarching = sitk.FastMarchingImageFilter()

    seedValue = 0

    for seed in seeds:
        trialPoint = (seed[0], seed[1], seed[2], seedValue)
        fastMarching.AddTrialPoint(trialPoint)

    fastMarching.SetStoppingValue(stopping_time)

    fastMarchingOutput = fastMarching.Execute(sigmoidOutput)

    thresholder = sitk.BinaryThresholdImageFilter()
    thresholder.SetLowerThreshold(0.0)
    thresholder.SetUpperThreshold(time_threshold)
    thresholder.SetOutsideValue(0)
    thresholder.SetInsideValue(255)

    result = thresholder.Execute(fastMarchingOutput)

    sitk.WriteImage(result, output_filename)



