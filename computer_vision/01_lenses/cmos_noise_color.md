# CCD vs CMOS

## What they are
CCD (Charge-Coupled Device) and CMOS (Complementary Metal-Oxide-Semiconductor) are the two main types of digital image sensors. Both convert incoming light into electrical signals to form an image.

## CCD — How it works
1. Photons hit each pixel and create electrical charge.
2. Charges are shifted across the chip.
3. A single readout node converts them to voltage.

### Characteristics
- Very low noise
- Excellent pixel uniformity
- Slower readout
- Higher power consumption
- More expensive

### Typical uses
- Scientific imaging
- Astronomy
- Older broadcast cameras

## CMOS — How it works
Each pixel has its own amplifier and readout circuitry, so signals are read directly from pixels.

### Characteristics
- Fast readout (good for video and high FPS)
- Low power consumption
- Cheaper to manufacture
- Easy integration with on-chip processing

### Typical uses
- Smartphones
- Modern DSLRs and mirrorless cameras
- Webcams
- Robotics and computer vision

## Quick comparison

| Feature | CCD | CMOS |
|---|---|---|
| Noise | Very low (historically) | Very low in modern sensors |
| Speed | Slower | Faster |
| Power | Higher | Lower |
| Cost | Higher | Lower |
| Market today | Niche | Dominant |

## Key takeaway
CCD historically provided the best image quality, but CMOS is now the dominant technology due to speed, efficiency, and cost.

---

# Noise in Images

## What is image noise
Image noise is random variation in brightness or color that does not come from the scene. It often appears as grain or speckles.

## Main sources of noise

### Photon (shot) noise
- Caused by randomness in photon arrival
- Fundamental and unavoidable
- More noticeable in low light

### Thermal noise (dark noise)
- Heat generates electrons even without light
- Increases with temperature and long exposures

### Read noise
- Introduced by sensor electronics during readout

### Quantization noise
- Caused by rounding when converting analog signals to digital values

## Types of visible noise
- Luminance noise: grainy brightness variation
- Chrominance noise: random color speckles

## Signal-to-Noise Ratio (SNR)

SNR = signal / noise

Higher SNR means a cleaner image. Low light reduces SNR and increases visible noise.

## Why noise matters
- Reduces detail
- Lowers dynamic range
- Makes feature detection harder
- Limits accuracy in scientific imaging

## Noise reduction

### Hardware
- Larger pixels
- Sensor cooling
- Improved electronics

### Software
- Frame averaging
- Spatial filtering (Gaussian, median)
- AI denoising

## Key takeaway
Noise is random error added to the true image signal, especially visible when the signal is weak.

---

# Colors and Wavelengths

## What is light
Light is electromagnetic radiation, and color depends on wavelength.

- Wavelength is the distance between wave peaks
- Measured in nanometers (nm)
- Visible light is a small part of the electromagnetic spectrum

## Visible spectrum

| Color | Wavelength |
|---|---|
| Violet | 380–450 nm |
| Blue | 450–495 nm |
| Green | 495–570 nm |
| Yellow | 570–590 nm |
| Orange | 590–620 nm |
| Red | 620–750 nm |

Shorter wavelengths appear violet, and longer wavelengths appear red.

## Human color perception
The retina has three cone types:

- S-cones: sensitive to short wavelengths (blue)
- M-cones: sensitive to medium wavelengths (green)
- L-cones: sensitive to long wavelengths (red)

The brain compares their responses to produce perceived color.

## Why cameras use RGB
Image sensors measure intensity, not color directly. They use color filters (red, green, blue), and software reconstructs a full-color image.

## Beyond visible light
- Ultraviolet (UV): shorter than violet
- Infrared (IR): longer than red

These are used in night vision, depth sensing, and scientific imaging.

## Key takeaway
Wavelength is the physical property of light, while color is the brain’s interpretation. Different spectra can appear identical (metamers), which is why color calibration is important.